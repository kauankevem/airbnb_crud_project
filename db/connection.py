import psycopg2

def connect_db(user, password):
    """Add commentMore actions
    Estabelece conexão com o banco de dados PostgreSQL.
    Retorna:
        conn: Objeto de conexão com o banco.
        cursor: Objeto para consulta
    """
     
    try:
        conn = psycopg2.connect(
            user=user,
            password=password,
            host="10.61.49.174",
            port="5432",
            dbname="walleria"
        )
        cursor = conn.cursor()
        cursor.execute("SET search_path TO airbnb;")
        print("Conexão realizada com sucesso!")
        return conn, cursor
    except Exception as e:
        print("Erro durante a conexão:", e)
        exit()

def desconectar(conn, cursor):
    cursor.close()
    conn.close()
    print("Conexão encerrada.")