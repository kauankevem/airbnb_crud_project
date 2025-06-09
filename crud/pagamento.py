# CRUD para pagamento

def create_pagamento(conn, valor_pagamento, status_pagamento, data_pagamento, metodo_pagamento, id_reserva, id_usuario):
    """
    Insere um novo pagamento.
    Retorna o id_pagamento criado.
    """
    cursor = conn.cursor()
    sql = """
        INSERT INTO pagamento
            (valor_pagamento, status_pagamento, data_pagamento, metodo_pagamento, id_reserva, id_usuario)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id_pagamento;
    """
    try:
        cursor.execute(sql, (valor_pagamento, status_pagamento, data_pagamento, metodo_pagamento, id_reserva, id_usuario))
        new_id = cursor.fetchone()[0]
        return new_id
    except Exception as e:
        print("Erro ao criar pagamento:", e)
        return None

def read_pagamento(conn, id_pagamento):
    """
    Recupera um pagamento pelo seu ID.
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
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao ler pagamento:", e)
        return None

def update_pagamento(conn, id_pagamento, **kwargs):
    """
    Atualiza campos de um pagamento.  
    Campos possíveis: valor_pagamento, status_pagamento, data_pagamento, metodo_pagamento, id_reserva, id_usuario.
    """
    if not kwargs:
        return False
    cursor = conn.cursor()
    cols = []
    vals = []
    for k, v in kwargs.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    vals.append(id_pagamento)
    sql = f"UPDATE pagamento SET {', '.join(cols)} WHERE id_pagamento = %s;"
    try:
        cursor.execute(sql, vals)
        return True
    except Exception as e:
        print("Erro ao atualizar pagamento:", e)
        return False

def delete_pagamento(conn, id_pagamento):
    """
    Remove um pagamento pelo seu ID.
    """
    cursor = conn.cursor()
    sql = "DELETE FROM pagamento WHERE id_pagamento = %s;"
    try:
        cursor.execute(sql, (id_pagamento,))
        return True
    except Exception as e:
        print("Erro ao deletar pagamento:", e)
        return False

# Função para listar todos os pagamentos, útil para validações gerais e diagnóstico de performance
def list_payments(conn):
    """
    Retorna todos os pagamentos cadastrados.
    """
    cursor = conn.cursor()
    sql = """
        SELECT id_pagamento, valor_pagamento, status_pagamento,
               data_pagamento, metodo_pagamento, id_reserva, id_usuario
        FROM pagamento;
    """
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("Erro ao listar pagamentos:", e)
        return []
