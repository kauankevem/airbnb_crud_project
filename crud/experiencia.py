def create_experiencia(cursor, conn, valores):
    try:
        sql = "INSERT INTO experiencia (id_servico, duracao_exp) VALUES (%s, %s)"
        cursor.execute(sql, valores)
        conn.commit()
        print("Registro inserido com sucesso!")
    except Exception as e:
        print("Erro na inserção:", e)
        conn.rollback()

def read_experiencia(cursor, colunas):
    try:
        if isinstance(colunas, list):
            colunas_str = ", ".join(colunas)
        else:
            colunas_str = colunas

        cursor.execute(f"SELECT {colunas_str} FROM experiencia;")
        dados = cursor.fetchall()
        print("Experiencias:")
        for linha in dados:
            print(linha)
    except Exception as e:
        print("Erro na leitura:", e)

def update_experiencia(cursor, conn, coluna, valor, filtro_coluna, filtro_valor):
    try:
        sql = f"UPDATE experiencia SET {coluna} = %s WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (valor, filtro_valor))
        conn.commit()
        print("Registro atualizado com sucesso!")
    except Exception as e:
        print("Erro na atualização:", e)
        conn.rollback()

def delete_experiencia(cursor, conn, filtro_coluna, filtro_valor):
    try:
        sql = f"DELETE FROM experiencia WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (filtro_valor,))
        conn.commit()
        print("Registro removido com sucesso!")
    except Exception as e:
        print("Erro na exclusao:", e)
        conn.rollback()
