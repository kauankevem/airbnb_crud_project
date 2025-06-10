# CRUD para serviços em listas de desejos
def create_servico_pertence_lista(conn, id_lista_desejos, id_servico):
    """Adiciona um serviço a uma lista de desejos."""
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO servico_pertence_lista (id_lista_desejos, id_servico) "
            "VALUES (%s, %s);"
        )
        cursor.execute(sql, (id_lista_desejos, id_servico))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao criar servico_pertence_lista:", e)
        conn.rollback()
        return False

def read_servico_pertence_lista(conn, id_lista_desejos, id_servico):
    """Retorna associação específica entre lista e serviço."""
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_lista_desejos, id_servico "
            "FROM servico_pertence_lista WHERE id_lista_desejos = %s AND id_servico = %s;"
        )
        cursor.execute(sql, (id_lista_desejos, id_servico))
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler servico_pertence_lista:", e)
        return None

def delete_servico_pertence_lista(conn, id_lista_desejos, id_servico):
    """Remove o serviço de uma lista de desejos."""
    cursor = conn.cursor()
    try:
        sql = (
            "DELETE FROM servico_pertence_lista WHERE id_lista_desejos = %s AND id_servico = %s;"
        )
        cursor.execute(sql, (id_lista_desejos, id_servico))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover servico_pertence_lista:", e)
        conn.rollback()
        return False

def list_servico_pertence_lista(conn, id_lista_desejos):
    """Lista todos os serviços de uma lista."""
    cursor = conn.cursor()
    try:
        sql = ("SELECT id_lista_desejos, id_servico FROM servico_pertence_lista WHERE id_lista_desejos = %s;")
        cursor.execute(sql, (id_lista_desejos,))
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao listar servico_pertence_lista:", e)
        return []