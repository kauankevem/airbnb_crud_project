#CRUD para relação hospede-faz-reserva

def create_hospede_faz_reserva(conn, id_usuario, id_reserva):
    """
    Insere uma relação entre hóspede e reserva.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO hospede_faz_reserva (id_usuario, id_reserva) "
            "VALUES (%s, %s);"
        )
        cursor.execute(sql, (id_usuario, id_reserva))
        conn.commit()
    except Exception as e:
        print("Erro ao criar relação hospede_faz_reserva:", e)
        conn.rollback()


def read_by_hospede(conn, id_usuario):
    """
    Retorna todas as reservas associadas a um hóspede.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_reserva FROM hospede_faz_reserva "
            "WHERE id_usuario = %s;"
        )
        cursor.execute(sql, (id_usuario,))
        registros = cursor.fetchall()
        return [r[0] for r in registros]
    except Exception as e:
        print("Erro ao ler relações por hóspede:", e)
        return []


def read_by_reserva(conn, id_reserva):
    """
    Retorna todos os hóspedes associados a uma reserva.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_usuario FROM hospede_faz_reserva "
            "WHERE id_reserva = %s;"
        )
        cursor.execute(sql, (id_reserva,))
        registros = cursor.fetchall()
        return [r[0] for r in registros]
    except Exception as e:
        print("Erro ao ler relações por reserva:", e)
        return []


def update_hospede_faz_reserva(conn, id_usuario, id_reserva, new_id_usuario, new_id_reserva):
    """
    Atualiza a relação hóspede-reserva substituindo a chave primária.
    """
    cursor = conn.cursor()
    try:
        # Remove antiga relação
        sql_delete = (
            "DELETE FROM hospede_faz_reserva "
            "WHERE id_usuario = %s AND id_reserva = %s;"
        )
        cursor.execute(sql_delete, (id_usuario, id_reserva))
        # Insere nova relação
        sql_insert = (
            "INSERT INTO hospede_faz_reserva (id_usuario, id_reserva) "
            "VALUES (%s, %s);"
        )
        cursor.execute(sql_insert, (new_id_usuario, new_id_reserva))
        conn.commit()
    except Exception as e:
        print("Erro ao atualizar relação hospede_faz_reserva:", e)
        conn.rollback()


def delete_hospede_faz_reserva(conn, id_usuario, id_reserva):
    """
    Remove a relação entre hóspede e reserva.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "DELETE FROM hospede_faz_reserva "
            "WHERE id_usuario = %s AND id_reserva = %s;"
        )
        cursor.execute(sql, (id_usuario, id_reserva))
        conn.commit()
    except Exception as e:
        print("Erro ao remover relação hospede_faz_reserva:", e)
        conn.rollback()


# Função para listar todas as relações de hóspede-reserva de forma rápida
# Útil para validação, diagnóstico de sobrecarga e identificação de pontos críticos antes de operações mais pesadas.
def list_hospede_faz_reserva(conn):
    """
    Lista todas as relações hóspede-reserva.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id_usuario, id_reserva FROM hospede_faz_reserva;"
        )
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao listar relações hospede_faz_reserva:", e)
        return []