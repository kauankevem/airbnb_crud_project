# CRUD para atividades da experiência

def create_atividade_experiencia(conn, id_servico, atividade_exp):
    """
    Insere uma atividade para uma experiência.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO atividade_experiencia (id_servico, atividade_exp) "
            "VALUES (%s, %s);"
        )
        cursor.execute(sql, (id_servico, atividade_exp))
        conn.commit()
    except Exception as e:
        print("Erro ao criar atividade_experiencia:", e)
        conn.rollback()

def read_atividades_por_servico(conn, id_servico):
    """
    Retorna lista de atividades de uma experiência.
    """
    cursor = conn.cursor()
    try:
        sql = "SELECT atividade_exp FROM atividade_experiencia WHERE id_servico = %s;"
        cursor.execute(sql, (id_servico,))
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao ler atividades_por_servico:", e)
        return []

def update_atividade_experiencia(conn, id_servico, old_atividade, new_atividade):
    """
    Atualiza uma atividade de uma experiência específica.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "UPDATE atividade_experiencia "
            "SET atividade_exp = %s "
            "WHERE id_servico = %s AND atividade_exp = %s;"
        )
        cursor.execute(sql, (new_atividade, id_servico, old_atividade))
        conn.commit()
    except Exception as e:
        print("Erro ao atualizar atividade_experiencia:", e)
        conn.rollback()

def delete_atividade_experiencia(conn, id_servico, atividade_exp):
    """
    Remove uma atividade de uma experiência.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "DELETE FROM atividade_experiencia "
            "WHERE id_servico = %s AND atividade_exp = %s;"
        )
        cursor.execute(sql, (id_servico, atividade_exp))
        conn.commit()
    except Exception as e:
        print("Erro ao remover atividade_experiencia:", e)
        conn.rollback()

# Função para listar todas as atividades de forma eficiente
def list_all_atividades(conn):
    """
    Lista todas as entradas da tabela atividade_experiencia.
    """
    cursor = conn.cursor()
    try:
        sql = "SELECT id_servico, atividade_exp FROM atividade_experiencia;"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao listar atividade_experiencia:", e)
        return []