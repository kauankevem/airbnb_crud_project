# crud/anfitriao_oferta_servico.py

def create_anfitriao_oferta_servico(conn, id_usuario, id_servico):
    """
    Insere uma relação entre anfitrião e serviço.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO anfitriao_oferta_servico (id_usuario, id_servico) "
            "VALUES (%s, %s);"
        )
        cursor.execute(sql, (id_usuario, id_servico))
        conn.commit()
    except Exception as e:
        print("Erro ao criar anfitriao_oferta_servico:", e)
        conn.rollback()

def read_by_anfitriao(conn, id_usuario):
    """
    Retorna todos os serviços oferecidos por um anfitrião.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_servico FROM anfitriao_oferta_servico "
            "WHERE id_usuario = %s;"
        )
        cursor.execute(sql, (id_usuario,))
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao ler por anfitrião:", e)
        return []

def read_by_servico(conn, id_servico):
    """
    Retorna todos os anfitriões que oferecem um serviço.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_usuario FROM anfitriao_oferta_servico "
            "WHERE id_servico = %s;"
        )
        cursor.execute(sql, (id_servico,))
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao ler por serviço:", e)
        return []

def update_anfitriao_oferta_servico(conn, id_usuario, id_servico, new_id_usuario, new_id_servico):
    """
    Atualiza a relação anfitrião-serviço substituindo a chave primária.
    """
    cursor = conn.cursor()
    try:
        sql_del = (
            "DELETE FROM anfitriao_oferta_servico "
            "WHERE id_usuario = %s AND id_servico = %s;"
        )
        cursor.execute(sql_del, (id_usuario, id_servico))
        sql_ins = (
            "INSERT INTO anfitriao_oferta_servico (id_usuario, id_servico) "
            "VALUES (%s, %s);"
        )
        cursor.execute(sql_ins, (new_id_usuario, new_id_servico))
        conn.commit()
    except Exception as e:
        print("Erro ao atualizar anfitriao_oferta_servico:", e)
        conn.rollback()

def delete_anfitriao_oferta_servico(conn, id_usuario, id_servico):
    """
    Remove a relação entre anfitrião e serviço.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "DELETE FROM anfitriao_oferta_servico "
            "WHERE id_usuario = %s AND id_servico = %s;"
        )
        cursor.execute(sql, (id_usuario, id_servico))
        conn.commit()
    except Exception as e:
        print("Erro ao remover anfitriao_oferta_servico:", e)
        conn.rollback()