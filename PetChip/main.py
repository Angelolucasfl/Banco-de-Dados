from cliente import *
from pet import *
from veterinario import *
from consulta import *
from venda import *

def print_menu():
    menu_lines = [
        "--- Menu ---",
        "1. Ver todos os clientes",
        "2. Adicionar um novo cliente",
        "3. Atualizar um cliente",
        "4. Ver todos os pets de um cliente",
        "5. Adicionar um novo pet",
        "6. Remover pet",
        "7. Ver todos os veterinários",
        "8. Adicionar um novo veterinário",
        "9. Ver todas as consultas de um veterinário",
        "10. Adicionar uma nova consulta",
        "11. Deletar uma consulta",
        "12. Atualizar uma consulta",
        "13. Ver todas as vendas",
        "14. Adicionar uma nova venda",
        "0. Sair"
    ]
    print('\n'.join(menu_lines))

# Clientes
def ver_todos_clientes():
    print("\nTodos os clientes: ")
    get_all_clients()

def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    add_client(nome, endereco, telefone)

def atualizar_cliente():
    id = input("Digite o id do cliente a ser atualizado: ")
    nome = input("Digite o novo nome do cliente: ")
    endereco = input("Digite o novo endereço do cliente: ")
    telefone = input("Digite o novo telefone do cliente: ")
    update_client(nome, endereco, telefone, id)

#Pets
def ver_pet():
    id = input("Digite o ID do dono do pet: ")
    print("\nTodos os pets do cliente:")
    get_pets_by_cliente(id)

def adicionar_pet():
    cliente_id = input("Digite o id do dono: ")
    nome = input("Digite o nome do pet: ")
    especie = input("Digite a especie do pet: ")
    add_pet(cliente_id, nome, especie)

def deletar_pet():
    id = input("Digite o id do pet a ser removido: ")
    print("\Pet removido")
    delete_pet(id)

#Veterinarios
def ver_veterinarios():
    print("\nTodos os veterinarios: ")
    get_all_veterinarios()

def add_veterinario():
    nome = input("Digite o nome do veterinario: ")
    especialidade = input("Digite a especialidade do veterinario: ")
    add_new_veterinario(nome, especialidade)

#Consultas
def ver_consultas():
    id = input("Digite o id do veterinario a ser consultado: ")
    print("\nTodas as consultas do veterinario: ")
    get_consultas_por_veterinario(id)

def add_consulta():
    pet_id = input("Digite o id do pet: ")
    veterinario_id = input("Digite o id do veterinario: ")
    data_hora = input("Digite a data e hora da consulta: ")
    descricao = input("Digite a descrição da consulta: ")
    add_new_consulta(pet_id, veterinario_id, data_hora, descricao)

def atualizar_consulta():
    id = input("Digite o id da consulta a ser atualizada: ")
    pet_id = input("Digite o novo id do pet: ")
    veterinario_id = input("Digite o novo id do veterinario: ")
    data_hora = input("Digite a nova data e hora da consulta: ")
    descricao = input("Digite a nova descrição da consulta: ")
    update_consulta(pet_id, veterinario_id, data_hora, descricao, id)

def deletar_consulta():
    id = input("Digite o id da consulta a ser deletada: ")
    print("\Consulta removida")
    delete_consulta(id)

#Diagnosticos
def ver_todas_vendas():
    print("\nTodas as vendas: ")
    get_vendas()

def add_venda():
    produto = input("Digite o nome do produto vendido: ")
    quantidade = input("Digite a quantidade vendida: ")
    valor = input("Digite o valor total da venda: ")
    add_new_venda(produto, quantidade, valor)


def main():
    menu_options = {
        '1': ver_todos_clientes,
        '2': adicionar_cliente,
        '3' : atualizar_cliente,
        '4' : ver_pet,
        '5' : adicionar_pet,
        '6' : deletar_pet,
        '7' : ver_veterinarios,
        '8' : add_veterinario,
        '9' : ver_consultas,
        '10' : add_consulta,
        '11' : deletar_consulta,
        '12' : atualizar_consulta,
        '13' : get_vendas,
        '14' : add_venda,

        '0': exit,
    }

    while True:
        try:
            print_menu()
            choice = input("\nDigite o número da opção desejada: ")
            
            if choice in menu_options:
                menu_options[choice]()
                print("===========================================================")
                print('\n')
            else:
                print("Opção inválida. Tente novamente.")
        
        except Exception as e:
            print("Ocorreu um erro:", str(e))

if __name__ == '__main__':
    main()