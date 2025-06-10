from db.connection import connect_db
from crud.acomodacao import create_acomodacao
from crud.reserva import list_reservas, confirm_reserva
from crud.disponibilidade import create_disponibilidade, update_disponibilidade, read_disponibilidade, delete_disponibilidade
from crud.avaliacao import create_avaliacao, read_avaliacao, update_avaliacao, delete_avaliacao

def menu_confirmar_reservas(conn, id_anfitriao):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT r.id_reserva, s.nome_servico, r.data_entrada_res, r.data_saida_res
              FROM reserva r
              JOIN servico s ON r.id_servico = s.id_servico
             WHERE r.status_reserva = 'Pendente'
               AND s.id_anfitriao_resp = %s
             ORDER BY r.data_entrada_res
        """, (id_anfitriao,))
        pendentes = cur.fetchall()
    if not pendentes:
        print("Nenhuma reserva pendente.")
        return
    for rid, nome, din, dout in pendentes:
        print(f"[{rid}] {nome}: {din} → {dout}")
    escolha = input("ID para confirmar (0 sai): ").strip()
    if escolha.isdigit() and int(escolha) != 0:
        ok = confirm_reserva(conn, int(escolha))
        print("Confirmada." if ok else "Falha ao confirmar.")

def menu_anfitriao():
    print("=== LOGIN NA AIRBNB-LANDIA COMO ANFITRIAO ===")
    user = input("Usuário do banco: ")
    password = input("Senha do banco: ")
    anfitriao_id = input("Seu ID de anfitrião: ").strip()

    try:
        conn, cursor = connect_db(user, password)

        # Verifica se o ID informado está na tabela anfitriao
        cursor.execute("SELECT 1 FROM anfitriao WHERE id_usuario = %s", (anfitriao_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("❌ ID de anfitrião inválido. Acesso negado.")
            conn.close()
            return
        else:
            print("✅ Login como anfitrião autorizado.")
            # continuar fluxo do menu de anfitrião aqui

    except Exception as e:
        print("Erro ao conectar ou verificar usuário:", e)
        return

    while True:
        print("\n=== MENU ANFITRIÃO ===")
        print("1 - Cadastrar acomodação")
        print("2 - Confirmar reservas pendentes")
        print("3 - Ver todas as reservas")
        print("4 - Atualizar disponibilidade")
        print("5 - Consultar avaliações")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            # coleta parâmetros e chama create_acomodacao
            servico_id = int(input("ID do serviço existente: ").strip())
            tipo = input("Tipo de acomodação: ").strip()
            quartos = int(input("Quartos: ").strip())
            banheiros = int(input("Banheiros: ").strip())
            camas = int(input("Camas: ").strip())
            cap = int(input("Capacidade: ").strip())
            create_acomodacao(conn, servico_id, tipo, quartos, banheiros, camas, cap)

        elif opcao == '2':
            menu_confirmar_reservas(conn, anfitriao_id)

        elif opcao == '3':
            for r in list_reservas(conn):
                print(r)

        elif opcao == '4':
            # coleta parâmetros e chama create_disponibilidade
            serv = int(input("ID do serviço: ").strip())
            ini = input("Data início (YYYY-MM-DD): ").strip()
            fim = input("Data fim    (YYYY-MM-DD): ").strip()
            val = float(input("Valor diária: ").strip())
            create_disponibilidade(conn, None, serv, ini, fim, val)

        elif opcao == '5':
            try:
                sql = (
                    "SELECT a.id_reserva, u.nome_usuario, a.comentario, a.data_avaliacao "
                    "FROM anfitriao_oferta_servico aos, servico s, reserva r, avaliacao a, usuario u "
                    f"WHERE aos.id_usuario = {anfitriao_id} AND aos.id_reserva = r.id_reserva AND a.id_reserva = r.id_reserva AND a.id_usuario = u.id_usuario;"
                )

                cursor.execute(sql)
                resultados = cursor.fetchall()

                if resultados:
                    print("\Avaliações encontradas:")
                    for r in resultados:
                        print(f"ID Reserva: {r[0]} | Nome: {r[1]} | Comentario: {r[2]} | Data da avaliação: R${r[3]}")
                else:
                    print("Nenhuma avaliação encontrada.")
            except Exception as e:
                print("Erro ao buscar avaliações:", e)

        elif opcao == '6':
            conn.close()
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_anfitriao()
