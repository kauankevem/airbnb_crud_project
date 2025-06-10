# CRUD para avaliação (ligada à reserva)

def create_avaliacao(conn, id_reserva, id_usuario, comentario, data_avaliacao):
    """
    Insere uma avaliação vinculada a uma reserva.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO avaliacao (id_reserva, id_usuario, comentario, data_avaliacao) "
            "VALUES (%s, %s, %s, %s) RETURNING id_avaliacao;"
        )
        cursor.execute(sql, (id_reserva, id_usuario, comentario, data_avaliacao))
        new_id = cursor.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print("Erro ao criar avaliação:", e)
        conn.rollback()
        return None

def read_avaliacao(conn, id_avaliacao):
    """
    Retorna os detalhes de uma avaliação pelo seu ID.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_avaliacao, id_reserva, id_usuario, comentario, data_avaliacao "
            "FROM avaliacao WHERE id_avaliacao = %s;"
        )
        cursor.execute(sql, (id_avaliacao,))
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler avaliação:", e)
        return None

def update_avaliacao(conn, id_avaliacao, **kwargs):
    """
    Atualiza campos de uma avaliação.
    Campos possíveis: comentario, data_avaliacao.
    """
    if not kwargs:
        return False
    cursor = conn.cursor()
    fields, values = [], []
    for key, val in kwargs.items():
        fields.append(f"{key} = %s")
        values.append(val)
    values.append(id_avaliacao)
    try:
        sql = f"UPDATE avaliacao SET {', '.join(fields)} WHERE id_avaliacao = %s;"
        cursor.execute(sql, values)
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao atualizar avaliação:", e)
        conn.rollback()
        return False

def delete_avaliacao(conn, id_avaliacao):
    """
    Remove uma avaliação pelo seu ID.
    """
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM avaliacao WHERE id_avaliacao = %s;"
        cursor.execute(sql, (id_avaliacao,))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover avaliação:", e)
        conn.rollback()
        return False
