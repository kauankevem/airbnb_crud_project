def create_comodidade_acomodacao(conn, id_servico, comodidade):
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO comodidade_acomodacao (id_servico, comodidade) VALUES (%s, %s)"
        cursor.execute(sql, (id_servico, comodidade))
        conn.commit()
        print("Registro inserido com sucesso!")
    except Exception as e:
        print("Erro na inserção:", e)
        conn.rollback()

def read_comodidade_acomodacao(conn, colunas):
    cursor = conn.cursor()
    try:
        if isinstance(colunas, list):
            colunas_str = ", ".join(colunas)
        else:
            colunas_str = colunas

        cursor.execute(f"SELECT {colunas_str} FROM comodidade_acomodacao;")
        dados = cursor.fetchall()
        print("Comodidades:")
        for linha in dados:
            print(linha)
    except Exception as e:
        print("Erro na leitura:", e)

def update_comodidade_acomodacao(conn, coluna, valor, filtro_coluna, filtro_valor):
    cursor = conn.cursor()
    try:
        sql = f"UPDATE comodidade_acomodacao SET {coluna} = %s WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (valor, filtro_valor))
        conn.commit()
        print("Registro atualizado com sucesso!")
    except Exception as e:
        print("Erro na atualização:", e)
        conn.rollback()

def delete_comodidade_acomodacao(conn, filtro_coluna, filtro_valor):
    cursor = conn.cursor()
    try:
        sql = f"DELETE FROM comodidade_acomodacao WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (filtro_valor,))
        conn.commit()
        print("Registro removido com sucesso!")
    except Exception as e:
        print("Erro na exclusao:", e)
        conn.rollback()
