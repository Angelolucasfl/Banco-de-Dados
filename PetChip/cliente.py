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
        cur.execute("UPDATE cliente SET nome = %s, endereco = %s, telefone = %s WHERE cliente_id = %s",
                    (nome, endereco, telefone, client_id))
        print('\n')
        con.commit()
        print("Cliente atualizado com sucesso!")
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()


'''
# Exemplo de uso
if __name__ == '__main__':
    # Recuperar todos os clientes
    print("Recuperando todos os clientes:")
    get_all_clients()

    # Adicionar um novo cliente
    print("Adicionando um novo cliente:")
    add_client("João da Silva", "Rua A, 123", "(11) 987654321")

    # Remover um cliente
    print("Removendo um cliente:")
    remove_client(1)

    # Atualizar um cliente
    print("Atualizando um cliente:")
    update_client(2, "Maria Souza", "Avenida B, 456", "(85) 99999999")
'''





