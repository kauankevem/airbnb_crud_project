from db.connection import connect_db
from interface.acomodacao import create_acomodacao
from interface.reserva import list_reservas, confirm_reserva
from interface.disponibilidade import create_disponibilidade, update_disponibilidade, read_disponibilidade, delete_disponibilidade
from interface.avaliacao import create_avaliacao, read_avaliacao, update_avaliacao, delete_avaliacao

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
    conn = connect_db()
    anfitriao_id = input("Seu ID de anfitrião: ").strip()
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
            aid = int(input("ID da avaliação: ").strip())
            print(read_avaliacao(conn, aid))

        elif opcao == '6':
            conn.close()
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_anfitriao()
