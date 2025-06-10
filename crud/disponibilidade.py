def create_disponibilidade(conn, id_disponibilidade, id_servico, data_inicio_disp, data_fim_disp, valor_disp):
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO disponibilidade (id_disponibilidade, id_servico, data_inicio_disp, data_fim_disp, valor_disp) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (id_disponibilidade, id_servico, data_inicio_disp, data_fim_disp, valor_disp))
        conn.commit()
        print("Registro inserido com sucesso!")
    except Exception as e:
        print("Erro na inserção:", e)
        conn.rollback()

def read_disponibilidade(conn, colunas):
    cursor = conn.cursor()
    try:
        if isinstance(colunas, list):
            colunas_str = ", ".join(colunas)
        else:
            colunas_str = colunas

        cursor.execute(f"SELECT {colunas_str} FROM disponibilidade;")
        dados = cursor.fetchall()
        print("Disponibilidades:")
        for linha in dados:
            print(linha)
    except Exception as e:
        print("Erro na leitura:", e)

def update_disponibilidade(conn, coluna, valor, filtro_coluna, filtro_valor):
    cursor = conn.cursor()
    try:
        sql = f"UPDATE disponibilidade SET {coluna} = %s WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (valor, filtro_valor))
        conn.commit()
        print("Registro atualizado com sucesso!")
    except Exception as e:
        print("Erro na atualização:", e)
        conn.rollback()

def delete_disponibilidade(conn, filtro_coluna, filtro_valor):
    cursor = conn.cursor()
    try:
        sql = f"DELETE FROM disponibilidade WHERE {filtro_coluna} = %s;"
        cursor.execute(sql, (filtro_valor,))
        conn.commit()
        print("Registro removido com sucesso!")
    except Exception as e:
        print("Erro na exclusao:", e)
        conn.rollback()
