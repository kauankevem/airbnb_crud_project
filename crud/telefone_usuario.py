# CRUD para telefone_usuario
def create_telefone_usuario(conn, id_usuario, telefone):
    """Adiciona um telefone para um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO telefone_usuario (id_usuario, telefone) VALUES (%s, %s);",
            (id_usuario, telefone)
        )
        conn.commit()
        return Truedef create_telefone_usuario(conn, id_usuario, telefone):
    """Adiciona um telefone para um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO telefone_usuario (id_usuario, telefone) VALUES (%s, %s);",
            (id_usuario, telefone)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao criar telefone_usuario:", e)
        conn.rollback()
        return False

def read_telefone_usuario(conn, id_usuario, telefone):
    """Retorna um telefone específico de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id_usuario, telefone FROM telefone_usuario WHERE id_usuario = %s AND telefone = %s;",
            (id_usuario, telefone)
        )
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler telefone_usuario:", e)
        return None

def delete_telefone_usuario(conn, id_usuario, telefone):
    """Remove um telefone de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM telefone_usuario WHERE id_usuario = %s AND telefone = %s;",
            (id_usuario, telefone)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover telefone_usuario:", e)
        conn.rollback()
        return False

def create_telefone_usuario(conn, id_usuario, telefone):
    """Adiciona um telefone para um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO telefone_usuario (id_usuario, telefone) VALUES (%s, %s);",
            (id_usuario, telefone)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao criar telefone_usuario:", e)
        conn.rollback()
        return False

def read_telefone_usuario(conn, id_usuario, telefone):
    """Retorna um telefone específico de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id_usuario, telefone FROM telefone_usuario WHERE id_usuario = %s AND telefone = %s;",
            (id_usuario, telefone)
        )
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler telefone_usuario:", e)
        return None

def delete_telefone_usuario(conn, id_usuario, telefone):
    """Remove um telefone de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM telefone_usuario WHERE id_usuario = %s AND telefone = %s;",
            (id_usuario, telefone)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover telefone_usuario:", e)
        conn.rollback()
        return False

def create_telefone_usuario(conn, id_usuario, telefone):
    """Adiciona um telefone para um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO telefone_usuario (id_usuario, telefone) VALUES (%s, %s);",
            (id_usuario, telefone)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao criar telefone_usuario:", e)
        conn.rollback()
        return False

def read_telefone_usuario(conn, id_usuario, telefone):
    """Retorna um telefone específico de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id_usuario, telefone FROM telefone_usuario WHERE id_usuario = %s AND telefone = %s;",
            (id_usuario, telefone)
        )
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler telefone_usuario:", e)
        return None

def delete_telefone_usuario(conn, id_usuario, telefone):
    """Remove um telefone de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM telefone_usuario WHERE id_usuario = %s AND telefone = %s;",
            (id_usuario, telefone)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover telefone_usuario:", e)
        conn.rollback()
        return False


    except Exception as e:
        print("Erro ao criar telefone_usuario:", e)
        conn.rollback()
        return False

def read_telefone_usuario(conn, id_usuario, telefone):
    """Retorna um telefone específico de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id_usuario, telefone FROM telefone_usuario WHERE id_usuario = %s AND telefone = %s;",
            (id_usuario, telefone)
        )
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler telefone_usuario:", e)
        return None

def delete_telefone_usuario(conn, id_usuario, telefone):
    """Remove um telefone de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM telefone_usuario WHERE id_usuario = %s AND telefone = %s;",
            (id_usuario, telefone)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover telefone_usuario:", e)
        conn.rollback()
        return False

def list_telefone_usuario(conn, id_usuario):
    """Lista todos os telefones de um usuário."""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM telefone_usuario WHERE id_usuario = %s;", (id_usuario,))
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao listar telefone_usuario:", e)
        return []

