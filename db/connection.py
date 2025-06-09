import psycopg2

# Estabelecendo a conexão com o PostgreSQL com o usuario gabriel_carneiro
try:
    conn = psycopg2.connect(
        user="gabriel_carneiro",
        password="misterioairbnb",
        host="10.61.49.174",
        port="5432",
        dbname="walleria"
    )
    cursor = conn.cursor()
    print("Conexão realizada com sucesso!")

    cursor.execute("SET search_path TO airbnb;")

except Exception as e:
    print("Erro durante a conexão:", e)
    exit()