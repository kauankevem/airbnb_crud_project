# CRUD para reserva
from datetime import date

def confirm_reserva(conn, id_reserva):
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id_servico, data_entrada_res, data_saida_res
                  FROM reserva
                 WHERE id_reserva = %s
                   AND status_reserva = 'Pendente'
                 FOR UPDATE
            """, (id_reserva,))
            row = cur.fetchone()
            if not row:
                return False
            id_servico, dt_in, dt_out = row

            cur.execute(
                "UPDATE reserva "
                "   SET status_reserva = 'Confirmada' "
                " WHERE id_reserva = %s",
                (id_reserva,)
            )
            split_disponibilidade(cur, id_servico, dt_in, dt_out)
            return True

def split_disponibilidade(cur, id_servico, entrada: date, saida: date):
    cur.execute("""
        SELECT id_disponibilidade, data_inicio_disp, data_fim_disp, valor_disp
          FROM disponibilidade
         WHERE id_servico = %s
           AND data_inicio_disp <= %s
           AND data_fim_disp   >= %s
         FOR UPDATE
    """, (id_servico, entrada, saida))
    disp = cur.fetchone()
    if not disp:
        return
    id_disp, dt_start, dt_end, valor = disp
    cur.execute(
        "DELETE FROM disponibilidade WHERE id_disponibilidade = %s",
        (id_disp,)
    )
    if dt_start < entrada:
        cur.execute("""
            INSERT INTO disponibilidade
                (id_servico, data_inicio_disp, data_fim_disp, valor_disp)
            VALUES (%s, %s, %s, %s)
        """, (id_servico, dt_start, entrada, valor))
    if saida < dt_end:
        cur.execute("""
            INSERT INTO disponibilidade
                (id_servico, data_inicio_disp, data_fim_disp, valor_disp)
            VALUES (%s, %s, %s, %s)
        """, (id_servico, saida, dt_end, valor))


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
