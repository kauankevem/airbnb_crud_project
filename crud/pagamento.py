# CRUD para pagamento

def create_pagamento(
    conn,
    valor_pagamento,
    status_pagamento,
    data_pagamento,
    metodo_pagamento,
    id_reserva,
    id_usuario,
):
    """
    Insere um novo pagamento e imprime o resultado.
    """
    cursor = conn.cursor()
    sql = """
        INSERT INTO pagamento
            (valor_pagamento, status_pagamento, data_pagamento,
             metodo_pagamento, id_reserva, id_usuario)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id_pagamento;
    """
    try:
        cursor.execute(
            sql,
            (
                valor_pagamento,
                status_pagamento,
                data_pagamento,
                metodo_pagamento,
                id_reserva,
                id_usuario,
            ),
        )
        new_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Pagamento criado com id_pagamento={new_id}")
    except Exception as e:
        print("Erro ao criar pagamento:", e)
        conn.rollback()


def read_pagamento(conn, id_pagamento):
    """
    Exibe os detalhes de um pagamento pelo ID.
    """
    cursor = conn.cursor()
    sql = """
        SELECT id_pagamento, valor_pagamento, status_pagamento,
               data_pagamento, metodo_pagamento, id_reserva, id_usuario
        FROM pagamento
        WHERE id_pagamento = %s;
    """
    try:
        cursor.execute(sql, (id_pagamento,))
        registro = cursor.fetchone()
        print("Pagamento:", registro)
    except Exception as e:
        print("Erro ao ler pagamento:", e)


def update_pagamento(conn, id_pagamento, **kwargs):
    """
    Atualiza campos de um pagamento.
    Campos possíveis: valor_pagamento, status_pagamento, data_pagamento,
    metodo_pagamento, id_reserva, id_usuario.
    """
    if not kwargs:
        print("Nenhum campo para atualizar.")
        return
    cursor = conn.cursor()
    cols, vals = [], []
    for k, v in kwargs.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    vals.append(id_pagamento)
    sql = f"UPDATE pagamento SET {', '.join(cols)} WHERE id_pagamento = %s;"
    try:
        cursor.execute(sql, vals)
        conn.commit()
        print(f"Pagamento {id_pagamento} atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar pagamento:", e)
        conn.rollback()


def delete_pagamento(conn, id_pagamento):
    """
    Remove um pagamento pelo seu ID.
    """
    cursor = conn.cursor()
    sql = "DELETE FROM pagamento WHERE id_pagamento = %s;"
    try:
        cursor.execute(sql, (id_pagamento,))
        conn.commit()
        print(f"Pagamento {id_pagamento} removido com sucesso.")
    except Exception as e:
        print("Erro ao deletar pagamento:", e)
        conn.rollback()


# Função para listar todos os pagamentos de forma rápida
def list_payments(conn):
    """
    Exibe todos os pagamentos cadastrados.
    """
    cursor = conn.cursor()
    sql = """
        SELECT id_pagamento, valor_pagamento, status_pagamento,
               data_pagamento, metodo_pagamento, id_reserva, id_usuario
        FROM pagamento;
    """
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for r in registros:
            print(r)
    except Exception as e:
        print("Erro ao listar pagamentos:", e)