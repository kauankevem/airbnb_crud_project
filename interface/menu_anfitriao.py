# Ações típicas de um anfitrião
from db.connection import connect_db


def cadastrar_acomodacao(conn):
    cursor = conn.cursor()
    nome_servico = input("Nome do serviço (acomodação): ")
    tipo = input("Tipo de acomodação (Casa/Apartamento/Quarto Privado): ")
    quartos = input("Número de quartos: ")
    banheiros = input("Número de banheiros: ")
    camas = input("Número de camas: ")
    capacidade = input("Capacidade de hóspedes: ")
    endereco_id = input("ID do endereço (endereco.id_endereco): ")
    try:
        # Inserir em servico
        sql1 = (
            "INSERT INTO servico (id_servico, nome_servico, id_anfitriao_resp, id_endereco) "
            "VALUES (DEFAULT, %s, %s, %s) RETURNING id_servico;"
        )
        anfitriao_id = input("Seu ID de anfitrião: ")
        cursor.execute(sql1, (nome_servico, anfitriao_id, endereco_id))
        servico_id = cursor.fetchone()[0]
        # Inserir em acomodacao
        sql2 = (
            "INSERT INTO acomodacao (id_servico, tipo_acomodacao, quartos, banheiros, camas, capacidade) "
            "VALUES (%s, %s, %s, %s, %s, %s);"
        )
        cursor.execute(sql2, (servico_id, tipo, quartos, banheiros, camas, capacidade))
        conn.commit()
        print(f"Acomodação cadastrada com id {servico_id}")
    except Exception as e:
        print("Erro ao cadastrar acomodação:", e)
        conn.rollback()


def ver_reservas(conn):
    cursor = conn.cursor()
    anfitriao_id = input("Seu ID de anfitrião: ")
    try:
        sql = (
            "SELECT r.id_reserva, r.data_entrada_res, r.data_saida_res, r.status_reserva, s.id_servico "
            "FROM reserva r "
            "JOIN servico s ON r.id_servico = s.id_servico "
            "WHERE s.id_anfitriao_resp = %s;"
        )
        cursor.execute(sql, (anfitriao_id,))
        registros = cursor.fetchall()
        if registros:
            print("Reservas recebidas:")
            for res in registros:
                print(res)
        else:
            print("Nenhuma reserva encontrada.")
    except Exception as e:
        print("Erro ao buscar reservas:", e)


def atualizar_disponibilidade(conn):
    cursor = conn.cursor()
    servico_id = input("ID do serviço: ")
    inicio = input("Data início (YYYY-MM-DD): ")
    fim = input("Data fim (YYYY-MM-DD): ")
    valor = input("Valor da diária: ")
    try:
        sql = (
            "INSERT INTO disponibilidade (id_disponibilidade, id_servico, data_inicio_disp, data_fim_disp, valor_disp) "
            "VALUES (DEFAULT, %s, %s, %s, %s);"
        )
        cursor.execute(sql, (servico_id, inicio, fim, valor))
        conn.commit()
        print("Disponibilidade atualizada.")
    except Exception as e:
        print("Erro ao atualizar disponibilidade:", e)
        conn.rollback()


def consultar_avaliacoes(conn):
    cursor = conn.cursor()
    anfitriao_id = input("Seu ID de anfitrião: ")
    try:
        sql = (
            "SELECT c.id_avaliacao, ca.tipo_class, ca.nota, a.comentario "
            "FROM avaliacao a "
            "JOIN reserva r ON a.id_reserva = r.id_reserva "
            "JOIN servico s ON r.id_servico = s.id_servico "
            "JOIN classificacao_avaliacao ca ON a.id_avaliacao = ca.id_avaliacao "
            "WHERE s.id_anfitriao_resp = %s;"
        )
        cursor.execute(sql, (anfitriao_id,))
        avals = cursor.fetchall()
        if avals:
            print("Avaliações recebidas:")
            for aval in avals:
                print(aval)
        else:
            print("Nenhuma avaliação encontrada.")
    except Exception as e:
        print("Erro ao consultar avaliações:", e)


def menu_anfitriao():
    conn = connect_db()
    while True:
        print("\n=== MENU ANFITRIÃO ===")
        print("1 - Cadastrar acomodação")
        print("2 - Ver reservas")
        print("3 - Atualizar disponibilidade")
        print("4 - Consultar avaliações")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_acomodacao(conn)
        elif opcao == '2':
            ver_reservas(conn)
        elif opcao == '3':
            atualizar_disponibilidade(conn)
        elif opcao == '4':
            consultar_avaliacoes(conn)
        elif opcao == '5':
            conn.close()
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_anfitriao()
