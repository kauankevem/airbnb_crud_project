def create_classificacao_avaliacao(cursor, conn, valores):
    try:
        sql = "INSERT INTO classificacao_avaliacao (id_avaliacao, tipo_class, nota) VALUES (%s, %s, %s)"
        cursor.execute(sql, valores)
        conn.commit()
        print("Registro inserido com sucesso!")
    except Exception as e:
        print("Erro na inserção:", e)
        conn.rollback()

def read_classificacao_avaliacao(cursor, colunas):
    try:
        if isinstance(colunas, list):
            colunas_str = ", ".join(colunas)
        else:
            colunas_str = colunas

        cursor.execute(f"SELECT {colunas_str} FROM classificacao_avaliacao;")
        dados = cursor.fetchall()
        print("Classificacoes:")
        for linha in dados:
            print(linha)
    except Exception as e:
        print("Erro na leitura:", e)

def update_classificacao_avaliacao(cursor, conn, coluna, valor, filtro_coluna, filtro_valor):
    try:
        sql = f"UPDATE classificacao_avaliacao SET {coluna} = %s WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (valor, filtro_valor))
        conn.commit()
        print("Registro atualizado com sucesso!")
    except Exception as e:
        print("Erro na atualização:", e)
        conn.rollback()

def delete_classificacao_avaliacao(cursor, conn, filtro_coluna, filtro_valor):
    try:
        sql = f"DELETE FROM classificacao_avaliacao WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (filtro_valor,))
        conn.commit()
        print("Registro removido com sucesso!")
    except Exception as e:
        print("Erro na exclusao:", e)
        conn.rollback()
