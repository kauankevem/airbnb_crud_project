# CRUD para acomodacao (subclasse de servico)

def create_acomodacao(conn, id_servico, tipo_acomodacao, quartos, banheiros, camas, capacidade):
    """
    Insere uma nova acomodação.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "INSERT INTO acomodacao "
            "(id_servico, tipo_acomodacao, quartos, banheiros, camas, capacidade) "
            "VALUES (%s, %s, %s, %s, %s, %s);"
        )
        cursor.execute(sql, (id_servico, tipo_acomodacao, quartos, banheiros, camas, capacidade))
        conn.commit()
    except Exception as e:
        print("Erro ao criar acomodação:", e)
        conn.rollback()

def read_acomodacao(conn, id_servico):
    """
    Retorna os detalhes de uma acomodação pelo seu serviço.
    """
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT id_servico, tipo_acomodacao, quartos, banheiros, camas, capacidade "
            "FROM acomodacao WHERE id_servico = %s;"
        )
        cursor.execute(sql, (id_servico,))
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler acomodação:", e)
        return None

def update_acomodacao(conn, id_servico, **kwargs):
    """
    Atualiza campos de uma acomodação.
    Campos possíveis: tipo_acomodacao, quartos, banheiros, camas, capacidade.
    """
    if not kwargs:
        return False
    cursor = conn.cursor()
    fields, values = [], []
    for key, val in kwargs.items():
        fields.append(f"{key} = %s")
        values.append(val)
    values.append(id_servico)
    try:
        sql = f"UPDATE acomodacao SET {', '.join(fields)} WHERE id_servico = %s;"
        cursor.execute(sql, values)
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao atualizar acomodação:", e)
        conn.rollback()
        return False

def delete_acomodacao(conn, id_servico):
    """
    Remove uma acomodação pelo seu serviço.
    """
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM acomodacao WHERE id_servico = %s;"
        cursor.execute(sql, (id_servico,))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao remover acomodação:", e)
        conn.rollback()
        return False