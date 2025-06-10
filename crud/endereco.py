def create_endereco(conn, cidade, pais, estado, endereco_postal, cep):
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO endereco (cidade, pais, estado, endereco_postal, cep) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (cidade, pais, estado, endereco_postal, cep))
        conn.commit()
        print("Registro inserido com sucesso!")
    except Exception as e:
        print("Erro na inserção:", e)
        conn.rollback()

def read_endereco(conn, colunas):
    cursor = conn.cursor()
    try:
        if isinstance(colunas, list):
            colunas_str = ", ".join(colunas)
        else:
            colunas_str = colunas

        cursor.execute(f"SELECT {colunas_str} FROM endereco;")
        dados = cursor.fetchall()
        print("Endereços:")
        for linha in dados:
            print(linha)
    except Exception as e:
        print("Erro na leitura:", e)

def update_endereco(conn, coluna, valor, filtro_coluna, filtro_valor):
    cursor = conn.cursor()
    try:
        sql = f"UPDATE endereco SET {coluna} = %s WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (valor, filtro_valor))
        conn.commit()
        print("Registro atualizado com sucesso!")
    except Exception as e:
        print("Erro na atualização:", e)
        conn.rollback()

def delete_endereco(conn, filtro_coluna, filtro_valor):
    cursor = conn.cursor()
    try:
        sql = f"DELETE FROM endereco WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (filtro_valor,))
        conn.commit()
        print("Registro removido com sucesso!")
    except Exception as e:
        print("Erro na exclusao:", e)
        conn.rollback()
