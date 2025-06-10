# CRUD para idiomas da experiência

def create_idioma_experiencia(conn, id_servico, idioma_exp):
    """
    Insere um idioma para uma experiência.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO idioma_experiencia (id_servico, idioma_exp) "
            "VALUES (%s, %s);"
        )
        cursor.execute(sql, (id_servico, idioma_exp))
        conn.commit()
    except Exception as e:
        print("Erro ao criar idioma_experiencia:", e)
        conn.rollback()

def read_idiomas_por_servico(conn, id_servico):
    """
    Retorna lista de idiomas para uma experiência.
    """
    cursor = conn.cursor()
    try:
        sql = "SELECT idioma_exp FROM idioma_experiencia WHERE id_servico = %s;"
        cursor.execute(sql, (id_servico,))
        return [r[0] for r in cursor.fetchall()]
    except Exception as e:
        print("Erro ao ler idiomas_por_servico:", e)
        return []

def update_idioma_experiencia(conn, id_servico, old_idioma, new_idioma):
    """
    Atualiza o idioma de uma experiência específica.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "UPDATE idioma_experiencia "
            "SET idioma_exp = %s "
            "WHERE id_servico = %s AND idioma_exp = %s;"
        )
        cursor.execute(sql, (new_idioma, id_servico, old_idioma))
        conn.commit()
    except Exception as e:
        print("Erro ao atualizar idioma_experiencia:", e)
        conn.rollback()

def delete_idioma_experiencia(conn, id_servico, idioma_exp):
    """
    Remove um idioma de uma experiência.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "DELETE FROM idioma_experiencia "
            "WHERE id_servico = %s AND idioma_exp = %s;"
        )
        cursor.execute(sql, (id_servico, idioma_exp))
        conn.commit()
    except Exception as e:
        print("Erro ao remover idioma_experiencia:", e)
        conn.rollback()
