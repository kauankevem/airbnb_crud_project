from db.connection import connect_db


def criar_indice(conn):
    cursor = conn.cursor()
    nome_indice = input("Nome do índice: ")
    tabela = input("Tabela (schema.tabela): ")
    colunas = input("Coluna(s) separadas por vírgula: ")
    sql = f"CREATE INDEX {nome_indice} ON {tabela}({colunas});"
    try:
        cursor.execute(sql)
        conn.commit()
        print(f"Índice '{nome_indice}' criado com sucesso em {tabela}({colunas})!")
    except Exception as e:
        print("Erro ao criar índice:", e)
        conn.rollback()
        
        
def remover_indice(conn):
    cursor = conn.cursor()
    nome_indice = input("Nome do índice: ")
    sql = f"DROP INDEX {nome_indice};"
    try:
        cursor.execute(sql)
        conn.commit()
        print(f"Índice '{nome_indice}' removido com sucesso!")
    except Exception as e:
        print("Erro ao remover índice:", e)
        conn.rollback()


def explain_query(conn):
    cursor = conn.cursor()
    query = input("Digite a query SELECT para analisar (sem ponto-e-vírgula): ")
    try:
        cursor.execute("EXPLAIN ANALYZE " + query)
        planos = cursor.fetchall()
        print("\n--- Plano de Execução (EXPLAIN ANALYZE) ---")
        for linha in planos:
            print(linha[0])
    except Exception as e:
        conn.rollback()  # <- limpa a transação para evitar bloqueio
        print("Erro no EXPLAIN ANALYZE:", e)



def listar_usuarios(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_usuario, nome_usuario, email_usuario FROM usuario;")
        registros = cursor.fetchall()
        print("\nID | Nome | Email")
        for id_u, nome, email in registros:
            print(f"{id_u} | {nome} | {email}")
    except Exception as e:
        print("Erro ao listar usuários:", e)


def listar_servicos(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_servico, nome_servico FROM servico;")
        registros = cursor.fetchall()
        print("\nID | Serviço")
        for id_s, nome in registros:
            print(f"{id_s} | {nome}")
    except Exception as e:
        print("Erro ao listar serviços:", e)


def menu_admin():
    """
    Menu de operações administrativas:
    - Criação de índices
    - Análise de planos de execução
    - Listagem de dados gerais
    - Fechar conexão e sair
    """
    print("=== LOGIN NA AIRBNB-LANDIA COMO ADMIN ===")
    user = input("Usuário do banco: ")
    password = input("Senha do banco: ")

    conn, cursor = connect_db(user, password)
    while True:
        print("\n=== MENU ADMINISTRADOR ===")
        print("1 - Criar índice")
        print("2 - Analisar plano de execução (EXPLAIN ANALYZE)")
        print("3 - Listar usuários")
        print("4 - Listar serviços")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_indice(conn)
        elif opcao == '2':
            explain_query(conn)
        elif opcao == '3':
            listar_usuarios(conn)
        elif opcao == '4':
            listar_servicos(conn)
        elif opcao == '5':
            print("Saindo do menu administrativo...")
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_admin()