# Ações típicas de um anfitrião
from db.connection import connect_db
from reserva import confirm_reserva  
import psycopg2

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
    anfitriao_id = input("Seu ID de anfitrião: ")
    while True:
        print("\n=== MENU ANFITRIÃO ===")
        print("1 - Cadastrar acomodação")
        print("2 - Confirmar reservas pendentes")  
        print("3 - Ver todas as reservas")         
        print("4 - Atualizar disponibilidade")
        print("5 - Consultar avaliações")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_acomodacao(conn)
        elif opcao == '2':
            menu_confirmar_reservas(conn, anfitriao_id) 
        elif opcao == '3':
            ver_reservas(conn)  
        elif opcao == '4':
            atualizar_disponibilidade(conn)
        elif opcao == '5':
            consultar_avaliacoes(conn)
        elif opcao == '6':
            conn.close()
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_anfitriao()
