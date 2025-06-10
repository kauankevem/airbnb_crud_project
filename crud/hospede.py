# CRUD para hospede (subclasse de usuario)

def create_hospede(conn, id_usuario):
    """
    Insere um registro na tabela hospede.
    """
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO hospede (id_usuario) VALUES (%s);", (id_usuario,))
        conn.commit()
        print(f"Hóspede criado com id_usuario={id_usuario}")
    except Exception as e:
        print("Erro ao criar hóspede:", e)
        conn.rollback()


def read_hospede(conn, id_usuario):
    """
    Exibe se o hóspede existe.
    """
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM hospede WHERE id_usuario = %s;", (id_usuario,))
        existe = cursor.fetchone() is not None
        msg = "encontrado" if existe else "não encontrado"
        print(f"Hóspede {msg}: id_usuario={id_usuario}")
    except Exception as e:
        print("Erro ao ler hóspede:", e)


def update_hospede(conn, id_usuario, new_id_usuario):
    """
    Atualiza o id_usuario de um hóspede.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE hospede SET id_usuario = %s WHERE id_usuario = %s;",
            (new_id_usuario, id_usuario),
        )
        conn.commit()
        print(f"Hóspede {id_usuario} atualizado para {new_id_usuario}")
    except Exception as e:
        print("Erro ao atualizar hóspede:", e)
        conn.rollback()


def delete_hospede(conn, id_usuario):
    """
    Remove o hóspede da tabela.
    """
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM hospede WHERE id_usuario = %s;", (id_usuario,))
        conn.commit()
        print(f"Hóspede removido: id_usuario={id_usuario}")
    except Exception as e:
        print("Erro ao remover hóspede:", e)
        conn.rollback()


# Função para listar todos os hóspedes de forma eficiente
def list_hospedes(conn):
    """
    Exibe todos os id_usuario de hóspedes.
    """
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_usuario FROM hospede;")
        for (uid,) in cursor.fetchall():
            print(uid)
    except Exception as e:
        print("Erro ao listar hóspedes:", e)