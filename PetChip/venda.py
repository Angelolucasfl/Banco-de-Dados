from connection import get_connection

def get_vendas():
    con, cur = get_connection()
    try:
        cur.execute("SELECT * FROM venda")
        print('\n')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()


def add_new_venda(produto, quantidade, valor):
    con, cur = get_connection()
    try:
        cur.execute("INSERT INTO venda (produto, quantidade, valor) VALUES (%s, %s, %s) RETURNING venda_id",
                    (produto, quantidade, valor))
        venda_id = cur.fetchone()[0]
        print('\n')
        con.commit()
        print("Venda cadastrada com sucesso! Venda ID:", venda_id)
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

'''
# Example usage
if __name__ == '__main__':
    # View diagnóstico por consulta
    print("Viewing diagnóstico por consulta:")
    get_diagnostico_por_consulta(1)

    # Update diagnóstico
    print("Updating diagnóstico:")
    update_diagnostico(1, "Descrição atualizada", "Prescrição atualizada")

    # Add diagnóstico
    print("Adding diagnóstico:")
    add_diagnostico(1, "Nova descrição", "Nova prescrição")
'''