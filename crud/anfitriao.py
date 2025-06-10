# CRUD para anfitriao (subclasse de usuario)
from reserva import confirm_reserva  
import psycopg2

def create_anfitriao(conn, id_usuario, super_host=False):
    with conn.cursor() as cur:
        try:
            cur.execute(
                "INSERT INTO anfitriao (id_usuario, super_host) VALUES (%s, %s);",
                (id_usuario, super_host)
            )
            conn.commit()
        except:
            conn.rollback()

def read_anfitriao(conn, id_usuario):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT 1 FROM anfitriao WHERE id_usuario = %s;",
            (id_usuario,)
        )
        return cur.fetchone() is not None

def update_anfitriao(conn, id_usuario, **kwargs):
    if not kwargs:
        return False
    fields = [f"{k} = %s" for k in kwargs]
    values = list(kwargs.values()) + [id_usuario]
    with conn.cursor() as cur:
        try:
            cur.execute(
                f"UPDATE anfitriao SET {', '.join(fields)} WHERE id_usuario = %s;",
                values
            )
            conn.commit()
            return True
        except:
            conn.rollback()
            return False

def delete_anfitriao(conn, id_usuario):
    with conn.cursor() as cur:
        try:
            cur.execute(
                "DELETE FROM anfitriao WHERE id_usuario = %s;",
                (id_usuario,)
            )
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
