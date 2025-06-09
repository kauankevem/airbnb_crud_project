# Ações típicas de um hóspede
from db.connection import connect_db


def buscar_acomodacoes(conn, cursor):
    estado = input("Digite o estado para buscar acomodações: ")

    print("Deseja filtrar por:")
    print("1 - Todas as cidades do estado")
    print("2 - Uma cidade específica")
    print("3 - Várias cidades específicas")
    opcao = input("Escolha uma opção: ")

    cidades = []
    if opcao == '2':
        cidade = input("Digite o nome da cidade: ")
        cidades.append(cidade)
    elif opcao == '3':
        while True:
            cidade = input("Digite o nome da cidade (ou pressione Enter para parar): ")
            if not cidade.strip():
                break
            cidades.append(cidade)

    try:
        base_sql = (
            "SELECT s.id_servico, s.nome_servico, a.tipo_acomodacao, d.valor_disp, e.cidade, e.estado "
            "FROM servico s "
            "JOIN acomodacao a ON s.id_servico = a.id_servico "
            "JOIN disponibilidade d ON s.id_servico = d.id_servico "
            "JOIN endereco e ON s.id_endereco = e.id_endereco "
            "WHERE e.estado ILIKE %s"
        )
        params = [f"%{estado}%"]

        if cidades:
            # Gera cláusulas dinâmicas para cada cidade
            cidade_placeholders = ','.join(['%s'] * len(cidades))
            base_sql += f" AND e.cidade ILIKE ANY (ARRAY[{cidade_placeholders}])"
            params.extend([f"%{c}%" for c in cidades])

        base_sql += " ORDER BY e.cidade, s.nome_servico;"
        cursor.execute(base_sql, tuple(params))
        resultados = cursor.fetchall()

        if resultados:
            print("Acomodações encontradas:")
            for r in resultados:
                print(f"Serviço: {r[1]} | Tipo: {r[2]} | Valor: R${r[3]} | Cidade: {r[4]} | Estado: {r[5]}")
        else:
            print("Nenhuma acomodação encontrada com os filtros informados.")
    except Exception as e:
        print("Erro ao buscar acomodações:", e)



def reservar_acomodacao(conn, cursor):
    
    hospede_id = input("Seu ID de hóspede: ")
    servico_id = input("ID do serviço a reservar: ")
    entrada = input("Data de entrada (YYYY-MM-DD): ")
    saida = input("Data de saída (YYYY-MM-DD): ")
    pessoas = input("Número de pessoas: ")
    try:
        sql_reserva = (
            "INSERT INTO reserva (id_reserva, data_entrada_res, data_saida_res, numero_pessoas, status_reserva, valor_reserva, id_servico) "
            "VALUES (DEFAULT, %s, %s, %s, 'Pendente', 0, %s) RETURNING id_reserva;"
        )
        cursor.execute(sql_reserva, (entrada, saida, pessoas, servico_id))
        id_reserva = cursor.fetchone()[0]

        sql_relacao = (
            "INSERT INTO hospede_faz_reserva (id_usuario, id_reserva) VALUES (%s, %s);"
        )
        cursor.execute(sql_relacao, (hospede_id, id_reserva))
        conn.commit()
        print(f"Reserva feita com ID {id_reserva}. Aguarde confirmação.")
    except Exception as e:
        print("Erro ao reservar:", e)
        conn.rollback()


def ver_minhas_reservas(conn, cursor):
    
    hospede_id = input("Seu ID de hóspede: ")
    try:
        sql = (
            "SELECT r.id_reserva, r.data_entrada_res, r.data_saida_res, r.status_reserva, s.nome_servico "
            "FROM reserva r "
            "JOIN hospede_faz_reserva hfr ON r.id_reserva = hfr.id_reserva "
            "JOIN servico s ON r.id_servico = s.id_servico "
            "WHERE hfr.id_usuario = %s;"
        )
        cursor.execute(sql, (hospede_id,))
        reservas = cursor.fetchall()
        if reservas:
            print("Suas reservas:")
            for r in reservas:
                print(r)
        else:
            print("Nenhuma reserva encontrada.")
    except Exception as e:
        print("Erro ao buscar reservas:", e)


def avaliar_estadia(conn, cursor):
    hospede_id = input("Seu ID de hóspede: ")
    id_reserva = input("ID da reserva que deseja avaliar: ")
    comentario = input("Comentário: ")
    data_aval = input("Data da avaliação (YYYY-MM-DD): ")

    try:
        sql1 = (
            "INSERT INTO avaliacao (id_avaliacao, id_reserva, id_usuario, comentario, data_avaliacao) "
            "VALUES (DEFAULT, %s, %s, %s, %s) RETURNING id_avaliacao;"
        )
        cursor.execute(sql1, (id_reserva, hospede_id, comentario, data_aval))
        id_avaliacao = cursor.fetchone()[0]

        while True:
            tipo = input("Tipo de classificação (ex: Limpeza, Localização): ")
            nota = input("Nota de 0 a 10: ")
            sql2 = (
                "INSERT INTO classificacao_avaliacao (id_avaliacao, tipo_class, nota) VALUES (%s, %s, %s);"
            )
            cursor.execute(sql2, (id_avaliacao, tipo, nota))
            continuar = input("Deseja adicionar outra classificação? (s/n): ")
            if continuar.lower() != 's':
                break

        conn.commit()
        print("Avaliação registrada com sucesso.")
    except Exception as e:
        print("Erro ao avaliar estadia:", e)
        conn.rollback()


def menu_hospede():
    print("=== LOGIN NA AIRBNB-LANDIA COMO HOSPEDE ===")
    user = input("Usuário do banco: ")
    password = input("Senha do banco: ")
    
    conn, cursor = connect_db(user, password)

    while True:
        print("\n=== MENU HÓSPEDE ===")
        print("1 - Buscar acomodações")
        print("2 - Reservar acomodação")
        print("3 - Ver minhas reservas")
        print("4 - Avaliar estadia")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            buscar_acomodacoes(conn, cursor)
        elif opcao == '2':
            reservar_acomodacao(conn, cursor)
        elif opcao == '3':
            ver_minhas_reservas(conn, cursor)
        elif opcao == '4':
            avaliar_estadia(conn, cursor)
        elif opcao == '5':
            conn.close()
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_hospede()
