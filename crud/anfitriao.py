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

def menu_confirmar_reservas(conn, id_anfitriao):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT r.id_reserva, s.nome_servico, r.data_entrada_res, r.data_saida_res
              FROM reserva r
              JOIN servico s ON r.id_servico = s.id_servico
             WHERE r.status_reserva = 'Pendente'
               AND s.id_anfitriao_resp = %s
             ORDER BY r.data_entrada_res
        """, (id_anfitriao,))
        pendentes = cur.fetchall()
    if not pendentes:
        print("Nenhuma reserva pendente.")
        return
    for rid, nome, din, dout in pendentes:
        print(f"[{rid}] {nome}: {din} → {dout}")
    escolha = input("ID para confirmar (0 sai): ").strip()
    if escolha.isdigit() and int(escolha) != 0:
        ok = confirm_reserva(conn, int(escolha))
        print("Confirmada." if ok else "Falha ao confirmar.")

def menu_anfitriao(conn, id_anfitriao):
    while True:
        print("1) Confirmar reservas pendentes")
        print("0) Sair")
        op = input("Opção: ").strip()
        if op == "1":
            menu_confirmar_reservas(conn, id_anfitriao)
        elif op == "0":
            break
