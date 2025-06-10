# Ações típicas de um hóspede
from db.connection import connect_db


def buscar_acomodacoes(conn):
    cursor = conn.cursor()
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
            print("\nAcomodações encontradas:")
            for r in resultados:
                print(f"ID Serviço: {r[0]} | Nome: {r[1]} | Tipo: {r[2]} | Valor: R${r[3]} | Cidade: {r[4]} | Estado: {r[5]}")
        else:
            print("Nenhuma acomodação encontrada com os filtros informados.")
    except Exception as e:
        print("Erro ao buscar acomodações:", e)


def verificar_disponibilidade(conn):
    cursor = conn.cursor()
    try:
        servico_id = input("Informe o ID da acomodação que deseja verificar: ")
        sql = (
            "SELECT data_inicio_disp, data_fim_disp, valor_disp "
            "FROM disponibilidade "
            "WHERE id_servico = %s "
            "ORDER BY data_inicio_disp;"
        )
        cursor.execute(sql, (servico_id,))
        disponibilidade = cursor.fetchall()
        if disponibilidade:
            print(f"\nDisponibilidade para a acomodação {servico_id}:")
            for data_inicio, data_fim, valor in disponibilidade:
                print(f"De {data_inicio} até {data_fim} - R$ {valor:.2f}")
        else:
            print("Nenhuma disponibilidade cadastrada para essa acomodação.")
    except Exception as e:
        print("Erro ao consultar disponibilidade:", e)

def reservar_acomodacao(conn):
    cursor = conn.cursor()
    from crud.reserva import create_reserva
    from crud.hospede_faz_reserva import create_hospede_faz_reserva
    
    hospede_id = input("Seu ID de hóspede: ")
    servico_id = input("ID do serviço a reservar: ")
    entrada = input("Data de entrada (YYYY-MM-DD): ")
    saida = input("Data de saída (YYYY-MM-DD): ")
    pessoas = input("Número de pessoas: ")
    
    try:
        # valores_reserva = (entrada, saida, pessoas, 'Pendente', 0, servico_id)
        id_reserva = create_reserva(conn, entrada, saida, pessoas, 'Pendente', 0, servico_id)

        create_hospede_faz_reserva(conn, hospede_id, id_reserva)
        print(f"Reserva feita com ID {id_reserva}. Aguarde confirmação.")
    except Exception as e:
        print("Erro ao reservar:", e)
        conn.rollback()


def ver_minhas_reservas(conn):
    cursor = conn.cursor()
    
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


def avaliar_estadia(conn):
    cursor = conn.cursor()

    from crud.avaliacao import create_avaliacao
    from crud.classificacao_avaliacao import create_classificacao_avaliacao

    hospede_id = input("Seu ID de hóspede: ")
    
    try:
        sql = (
                "SELECT R.id_reserva, R.data_entrada_res, R.data_saida_res "
                "FROM hospede_faz_reserva HR, reserva R "
                "WHERE %s = HR.id_usuario AND HR.id_reserva = R.id_reserva AND R.id_reserva NOT IN (SELECT id_reserva FROM avaliacao GROUP BY id_reserva);"
            )
        cursor.execute(sql, (hospede_id,))
        reservas = cursor.fetchall()
        if reservas:
            print("Suas reservas nao avaliadas:")
            for r in reservas:
                print(r)
        else:
            print("Nenhuma reserva sem avaliacao encontrada.")
            return
    except Exception as e:
        print("Erro ao buscar reservas nao avaliadas:", e)
   

    id_reserva = input("ID da reserva que deseja avaliar: ")
    comentario = input("Comentário: ")
    data_aval = input("Data da avaliação (YYYY-MM-DD): ")

    try:
        id_avaliacao = create_avaliacao(conn, id_reserva, hospede_id, comentario, data_aval)

        while True:
            tipo = input("Tipo de classificação (ex: Limpeza, Localização): ")
            nota = input("Nota de 0 a 5: ")
            create_classificacao_avaliacao(conn, id_avaliacao, tipo, nota)

            continuar = input("Deseja adicionar outra classificação? (s/n): ")
            if continuar.lower() != 's':
                break
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
        print("2 - Verificar disponibilidade de uma acomodação")
        print("3 - Reservar acomodação")
        print("4 - Ver minhas reservas")
        print("5 - Avaliar estadia")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            buscar_acomodacoes(conn)
        elif opcao == '2':
            verificar_disponibilidade(conn)
        elif opcao == '3':
            reservar_acomodacao(conn)
        elif opcao == '4':
            ver_minhas_reservas(conn)
        elif opcao == '5':
            avaliar_estadia(conn)
        elif opcao == '6':
            conn.close()
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_hospede()
