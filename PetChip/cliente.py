from connection import get_connection

def get_all_clients():
    con, cur = get_connection()
    try:
        cur.execute("SELECT * FROM cliente")
        print('\n')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def add_client(nome, endereco, telefone):
    con, cur = get_connection()
    try:
        cur.execute("INSERT INTO cliente (nome, endereco, telefone) VALUES (%s, %s, %s)", (nome, endereco, telefone))
        con.commit()
        print('\n')
        print("Cliente adicionado com sucesso!")
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def remove_client(cliente_id):
    con, cur = get_connection()
    try:
        cur.execute("DELETE FROM cliente WHERE cliente_id = %s", (cliente_id,))
        con.commit()
        print('\n')
        print("Cliente removido com sucesso!")
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def update_client(nome, endereco, telefone, client_id):
    con, cur = get_connection()
    try:
        cur.execute("SELECT * FROM cliente WHERE cliente_id = %s", (client_id,))
        existing_client = cur.fetchone()
        
        if existing_client:
            cur.execute("UPDATE cliente SET nome = %s, endereco = %s, telefone = %s WHERE cliente_id = %s",
                        (nome, endereco, telefone, client_id))
            con.commit()
            print('\n')
            print("Cliente atualizado com sucesso!")
        else:
            print('\n')
            print("Cliente com o ID", client_id, "não encontrado. Nenhum cliente foi atualizado.")
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()


