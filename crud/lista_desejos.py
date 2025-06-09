# CRUD para lista de desejos

def create_lista_desejos(conn, id_usuario, nome_lista='Minha Lista de Desejos'):
    """
    Insere uma nova lista de desejos para o usuário.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO lista_desejos (id_usuario, nome_lista) "
            "VALUES (%s, %s) RETURNING id_lista_desejos;"
        )
        cursor.execute(sql, (id_usuario, nome_lista))
        new_id = cursor.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print("Erro ao criar lista_de_desejos:", e)
        conn.rollback()
        return None

def read_lista_desejos(conn, id_lista):
    """
    Retorna os detalhes de uma lista de desejos pelo seu ID.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_lista_desejos, id_usuario, nome_lista "
            "FROM lista_desejos "
            "WHERE id_lista_desejos = %s;"
        )
        cursor.execute(sql, (id_lista,))
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler lista_de_desejos:", e)
        return None

def update_lista_desejos(conn, id_lista, **kwargs):
    """
    Atualiza campos de uma lista de desejos.
    """
    if not kwargs:
        return False
    cursor = conn.cursor()
    fields = []
    values = []
    for key, val in kwargs.items():
        fields.append(f"{key} = %s")
        values.append(val)
    values.append(id_lista)
    try:
        sql = f"UPDATE lista_desejos SET {', '.join(fields)} WHERE id_lista_desejos = %s;"
        cursor.execute(sql, values)
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao atualizar lista_de_desejos:", e)
        conn.rollback()
        return False

def delete_lista_desejos(conn, id_lista):
    """
    Remove uma lista de desejos pelo seu ID.
    """
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM lista_desejos WHERE id_lista_desejos = %s;"
        cursor.execute(sql, (id_lista,))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover lista_de_desejos:", e)
        conn.rollback()
        return False

# Função para listar todas as listas de desejos de forma rápida
# Útil para validação, diagnóstico de sobrecarga e identificação de pontos críticos antes de operações mais pesadas.
def list_lista_desejos(conn):
    """
    Lista todas as listas de desejos existentes.
    """
    cursor = conn.cursor()
    try:
        sql = "SELECT id_lista_desejos, id_usuario, nome_lista FROM lista_desejos;"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao listar lista_de_desejos:", e)
        return []