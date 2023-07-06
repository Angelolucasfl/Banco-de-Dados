from connection import get_connection

def add_pet(cliente_id, nome, especie):
    con, cur = get_connection()
    try:
        cur.execute("INSERT INTO pet (cliente_id, nome, especie) VALUES (%s, %s, %s)",
                    (cliente_id, nome, especie))
        print('\n')
        con.commit()
        print("Pet cadastrado com sucesso!")
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def get_pets_by_cliente(cliente_id):
    con, cur = get_connection()
    try:
        cur.execute("SELECT * FROM pet WHERE cliente_id = %s", (cliente_id,))
        rows = cur.fetchall()
        print('\n')
        if rows:
            for row in rows:
                print(row)
        else:
            print("Nenhum pet encontrado para o cliente com o ID:", cliente_id)
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def delete_pet(pet_id):
    con, cur = get_connection()
    try:
        cur.execute("DELETE FROM pet WHERE pet_id = %s", (pet_id,))
        print('\n')
        con.commit()
        print("Pet deletado com sucesso!")
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

