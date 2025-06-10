# CRUD para servico
def create_servico(conn, nome_servico, id_anfitriao_resp, id_endereco):
    """Insere um novo serviço e retorna o id gerado."""
    with conn.cursor() as cur:
        try:
            cur.execute(
                """
                INSERT INTO servico (nome_servico, id_anfitriao_resp, id_endereco)
                VALUES (%s, %s, %s)
                RETURNING id_servico
                """,
                (nome_servico, id_anfitriao_resp, id_endereco)
            )
            new_id = cur.fetchone()[0]
            conn.commit()
            return new_id
        except Exception:
            conn.rollback()
            return None

 def read_servico(conn, id_servico):
    """Retorna os dados de um serviço pelo seu ID."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id_servico, nome_servico, id_anfitriao_resp, id_endereco "
            "FROM servico WHERE id_servico = %s",
            (id_servico,)
        )
        return cur.fetchone()

 def update_servico(conn, id_servico, **kwargs):
    """Atualiza campos de um serviço."""
    if not kwargs:
        return False
    fields = []
    values = []
    for k, v in kwargs.items():
        fields.append(f"{k} = %s")
        values.append(v)
    values.append(id_servico)
    with conn.cursor() as cur:
        try:
            cur.execute(
                f"UPDATE servico SET {', '.join(fields)} WHERE id_servico = %s",
                values
            )
            conn.commit()
            return True
        except Exception:
            conn.rollback()
            return False

 def delete_servico(conn, id_servico):
    """Remove um serviço pelo seu ID."""
    with conn.cursor() as cur:
        try:
            cur.execute(
                "DELETE FROM servico WHERE id_servico = %s",
                (id_servico,)
            )
            conn.commit()
            return True
        except Exception:
            conn.rollback()
            return False

 def list_servicos(conn):
    """Lista todos os serviços cadastrados."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id_servico, nome_servico, id_anfitriao_resp, id_endereco FROM servico"
        )
        return cur.fetchall()
