# CRUD para hospede (subclasse de usuario)

def create_hospede(conn, id_usuario):
    """
    Insere um registro na tabela hospede (subclasse de usuario).
    """
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO hospede (id_usuario) VALUES (%s);"
        cursor.execute(sql, (id_usuario,))
        conn.commit()
    except Exception as e:
        print("Erro ao criar hóspede:", e)
        conn.rollback()

def read_hospede(conn, id_usuario):
    """
    Retorna True se o hóspede existir, False caso contrário.
    """
    cursor = conn.cursor()
    try:
        sql = "SELECT 1 FROM hospede WHERE id_usuario = %s;"
        cursor.execute(sql, (id_usuario,))
        return cursor.fetchone() is not None
    except Exception as e:
        print("Erro ao ler hóspede:", e)
        return False

def update_hospede(conn, id_usuario, new_id_usuario):
    """
    Atualiza o id_usuario de um hóspede.
    """
    cursor = conn.cursor()
    try:
        sql = "UPDATE hospede SET id_usuario = %s WHERE id_usuario = %s;"
        cursor.execute(sql, (new_id_usuario, id_usuario))
        conn.commit()
    except Exception as e:
        print("Erro ao atualizar hóspede:", e)
        conn.rollback()

def delete_hospede(conn, id_usuario):
    """
    Remove o hóspede da tabela.
    """
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM hospede WHERE id_usuario = %s;"
        cursor.execute(sql, (id_usuario,))
        conn.commit()
    except Exception as e:
        print("Erro ao remover hóspede:", e)
        conn.rollback()

# Função para listar todos os hóspedes de forma eficiente
# Útil para validação, diagnóstico de sobrecarga e identificação de pontos críticos antes de operações mais pesadas.
def list_hospedes(conn):
    """
    Retorna lista com todos os id_usuario de hóspedes.
    """
    cursor = conn.cursor()
    try:
        sql = "SELECT id_usuario FROM hospede;"
        cursor.execute(sql)
        return [r[0] for r in cursor.fetchall()]
    except Exception as e:
        print("Erro ao listar hóspedes:", e)
        return []