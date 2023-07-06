from connection import get_connection

def get_all_veterinarios():
    con, cur = get_connection()
    try:
        cur.execute("SELECT * FROM veterinario")
        print('\n')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def add_new_veterinario(nome, especialidade):
    con, cur = get_connection()
    try:
        cur.execute("INSERT INTO veterinario (nome, especialidade) VALUES (%s, %s) RETURNING veterinario_id",
                    (nome, especialidade))
        veterinario_id = cur.fetchone()[0]
        print('\n')
        con.commit()
        print("Veterinário cadastrado com sucesso! Veterinário ID:", veterinario_id)
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

