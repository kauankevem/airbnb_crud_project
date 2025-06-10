# CRUD para lista de desejos

def create_lista_desejos(conn, id_usuario, nome_lista="Minha Lista de Desejos"):
    """
    Insere uma nova lista de desejos para o usuário.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO lista_desejos (id_usuario, nome_lista)
            VALUES (%s, %s) RETURNING id_lista_desejos;
            """,
            (id_usuario, nome_lista),
        )
        new_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Lista de desejos criada com id={new_id}")
    except Exception as e:
        print("Erro ao criar lista_de_desejos:", e)
        conn.rollback()


def read_lista_desejos(conn, id_lista):
    """
    Exibe os detalhes de uma lista de desejos pelo ID.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT id_lista_desejos, id_usuario, nome_lista
            FROM lista_desejos
            WHERE id_lista_desejos = %s;
            """,
            (id_lista,),
        )
        registro = cursor.fetchone()
        print("Lista de desejos:", registro)
    except Exception as e:
        print("Erro ao ler lista_de_desejos:", e)


def update_lista_desejos(conn, id_lista, **kwargs):
    """
    Atualiza campos de uma lista de desejos.
    Campos possíveis: id_usuario, nome_lista.
    """
    if not kwargs:
        print("Nenhum campo para atualizar.")
        return
    cursor = conn.cursor()
    campos, valores = [], []
    for k, v in kwargs.items():
        campos.append(f"{k} = %s")
        valores.append(v)
    valores.append(id_lista)
    try:
        cursor.execute(
            f"UPDATE lista_desejos SET {', '.join(campos)} WHERE id_lista_desejos = %s;",
            valores,
        )
        conn.commit()
        print(f"Lista {id_lista} atualizada com sucesso.")
    except Exception as e:
        print("Erro ao atualizar lista_de_desejos:", e)
        conn.rollback()


def delete_lista_desejos(conn, id_lista):
    """
    Remove uma lista de desejos pelo seu ID.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM lista_desejos WHERE id_lista_desejos = %s;", (id_lista,)
        )
        conn.commit()
        print(f"Lista de desejos {id_lista} removida.")
    except Exception as e:
        print("Erro ao remover lista_de_desejos:", e)
        conn.rollback()
