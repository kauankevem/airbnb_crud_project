# CRUD para anfitriao (subclasse de usuario)


def create_anfitriao(conn, id_usuario, super_host=False):
    """
    Insere um novo anfitrião (subclasse de usuário).
    """
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO anfitriao (id_usuario, super_host) VALUES (%s, %s);"
        cursor.execute(sql, (id_usuario, super_host))
        conn.commit()
    except Exception as e:
        print("Erro ao criar anfitrião:", e)
        conn.rollback()

def read_anfitriao(conn, id_usuario):
    """
    Retorna True se o anfitrião existir, False caso contrário.
    """
    cursor = conn.cursor()
    try:
        sql = "SELECT 1 FROM anfitriao WHERE id_usuario = %s;"
        cursor.execute(sql, (id_usuario,))
        return cursor.fetchone() is not None
    except Exception as e:
        print("Erro ao ler anfitrião:", e)
        return False

def update_anfitriao(conn, id_usuario, **kwargs):
    """
    Atualiza campos de um anfitrião.
    Campos possíveis: super_host.
    """
    if not kwargs:
        return False
    cursor = conn.cursor()
    fields, values = [], []
    for key, val in kwargs.items():
        fields.append(f"{key} = %s")
        values.append(val)
    values.append(id_usuario)
    try:
        sql = f"UPDATE anfitriao SET {', '.join(fields)} WHERE id_usuario = %s;"
        cursor.execute(sql, values)
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao atualizar anfitrião:", e)
        conn.rollback()
        return False

def delete_anfitriao(conn, id_usuario):
    """
    Remove um anfitrião pelo seu id_usuario.
    """
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM anfitriao WHERE id_usuario = %s;"
        cursor.execute(sql, (id_usuario,))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover anfitrião:", e)
        conn.rollback()
        return False

# Função para listar todos os anfitriões de forma eficiente
def list_anfitriao(conn):
    """
    Retorna todos os registros de anfitrião (id_usuario, super_host).
    """
    cursor = conn.cursor()
    try:
        sql = "SELECT id_usuario, super_host FROM anfitriao;"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao listar anfitriões:", e)
        return []