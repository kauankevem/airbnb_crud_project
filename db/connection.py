import psycopg2

def connect_db():
    """
    Estabelece conexão com o banco de dados PostgreSQL.

    Retorna:
        conn: Objeto de conexão com o banco.
    """
    try:
        conn = psycopg2.connect(
            user="postgres",            # Altere conforme seu usuário
            password="sua_senha",       # Altere para sua senha
            host="127.0.0.1",           # Ou IP do servidor remoto se for via SSH
            port="22",                # Porta padrão do PostgreSQL
            dbname="nome_do_banco"      # Altere para o nome do seu banco
        )
        return conn
    except Exception as e:
        print("Erro ao conectar no banco:", e)
        exit()
