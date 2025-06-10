# CRUD para reserva
def create_reserva(conn, data_entrada, data_saida, numero_pessoas, status, valor, id_servico):
    """
    Insere uma nova reserva e retorna o id gerado.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO reserva (id_reserva, data_entrada_res, data_saida_res, numero_pessoas, status_reserva, valor_reserva, id_servico) "
            "VALUES (DEFAULT, %s, %s, %s, %s, %s, %s) RETURNING id_reserva;"
        )
        cursor.execute(sql, (data_entrada, data_saida, numero_pessoas, status, valor, id_servico))
        new_id = cursor.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print("Erro ao criar reserva:", e)
        conn.rollback()
        return None

def read_reserva(conn, id_reserva):
    """Retorna os detalhes de uma reserva pelo seu ID."""
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_reserva, data_entrada_res, data_saida_res, numero_pessoas, status_reserva, valor_reserva, id_servico "
            "FROM reserva WHERE id_reserva = %s;"
        )
        cursor.execute(sql, (id_reserva,))
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler reserva:", e)
        return None

def update_reserva(conn, id_reserva, **kwargs):
    """Atualiza campos de uma reserva."""
    if not kwargs:
        return False
    cursor = conn.cursor()
    fields = []
    values = []
    for key, val in kwargs.items():
        fields.append(f"{key} = %s")
        values.append(val)
    values.append(id_reserva)
    try:
        sql = f"UPDATE reserva SET {', '.join(fields)} WHERE id_reserva = %s;"
        cursor.execute(sql, values)
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao atualizar reserva:", e)
        conn.rollback()
        return False

def delete_reserva(conn, id_reserva):
    """Remove uma reserva pelo seu ID."""
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM reserva WHERE id_reserva = %s;"
        cursor.execute(sql, (id_reserva,))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover reserva:", e)
        conn.rollback()
        return False

def list_reservas(conn):
    """Lista todas as reservas."""
    cursor = conn.cursor()
    try:
        sql = "SELECT * FROM reserva;"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao listar reservas:", e)
        return []