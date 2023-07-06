from connection import get_connection

def get_consultas_por_veterinario(veterinario_id):
    con, cur = get_connection()
    try:
        cur.execute("SELECT * FROM consulta WHERE veterinario_id = %s", (veterinario_id,))
        rows = cur.fetchall()
        print('\n')
        if rows:
            for row in rows:
                print(row)
        else:
            print("Nenhuma consulta encontrada para o veterinário com o ID:", veterinario_id)
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()


def delete_consulta(consulta_id):
    con, cur = get_connection()
    try:
        cur.execute("DELETE FROM consulta WHERE consulta_id = %s", (consulta_id,))
        print('\n')
        con.commit()
        print("Consulta deletada com sucesso!")
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def add_new_consulta(pet_id, veterinario_id, data_hora, descricao):
    con, cur = get_connection()
    try:
        cur.execute("INSERT INTO consulta (pet_id, veterinario_id, data_hora, descricao) VALUES (%s, %s, %s, %s) RETURNING consulta_id",
                    (pet_id, veterinario_id, data_hora, descricao))
        consulta_id = cur.fetchone()[0]
        print('\n')
        con.commit()
        print("Consulta cadastrada com sucesso! Consulta ID:", consulta_id)
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def update_consulta(pet_id, veterinario_id, data_hora, descricao, consulta_id):
    con, cur = get_connection()
    try:
        cur.execute("UPDATE consulta SET pet_id = %s, veterinario_id = %s, data_hora = %s, descricao = %s WHERE consulta_id = %s",
                    (pet_id, veterinario_id, data_hora, descricao, consulta_id))
        print('\n')
        con.commit()
        print("consulta atualizada com sucesso!")
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()
