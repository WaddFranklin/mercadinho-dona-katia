from Estoque import *
import os

estoque = Estoque()

alimento1 = Alimento("miojo", "alimento", 1.99, "nissin", "10/08/2022", 100.0)
estoque.add(alimento1)

alimento2 = Alimento("feijao", "alimento", 4.53, "carioca", "13/09/2022", 1000.0)
estoque.add(alimento2)

bebida = Bebida("vinho", "bebida", 10.0, "dom bosco", "01/09/2022", 1000.0)
estoque.add(bebida)

papelaria = Papelaria("caixa de canetas", "papelaria", 30.99, "bic", "25/08/2022", 50)
estoque.add(papelaria)

ADD = 1
EDIT = 2
REMOVE = 3
LIST = 4
REPORT = 5
SAIR = 6

def clear():
    os.system('clear')


def printHeader(title, space=7):
    titleSize = len(title)
    innerSpace = titleSize + (2 * space)

    print('+' + '-'*innerSpace + '+')
    print('|' + ' '*space + title + ' '*space + '|')
    print('+' + '-'*innerSpace + '+')

    return innerSpace


def printBody(options, innerSpace):
    i = 1
    for option in options:
        str = ""
        str += f"| {i}. {option}"
        space = innerSpace - len(str) + 1
        str += ' '*space + '|'
        print(str)
        i += 1
    print('+' + '-'*innerSpace + '+')


def promptScreen(title, options, question=">>> Escolha uma das opcoes acima: ", space=7):
    innerSpace = printHeader(title, space)
    printBody(options, innerSpace)
    return input(question)


def checkAdd(tipo, preco, peso=0.0, volume=0.0, quantidade=0):
    return tipo in ['alimento', 'bebida', 'papelaria'] and preco >= 0.0 and peso >= 0.0 and volume >= 0.0 and quantidade >= 0


def execute(selection):
    if selection == ADD:
        printHeader("Insercao de Prudotos")
        nome = input(">>> Informe o nome do produto: ")
        tipo = input(
            ">>> Informe o tipo do produto (alimento/bebida/papelaria): ")
        preco = float(input(">>> Informe o preco do produto (xx.xx): "))
        marca = input(">>> Informe a marca do produto: ")
        data_vencimento = input(
            ">>> Informe a data de vencimento do produto (dd/mm/aaaa): ")
        if tipo == 'alimento':
            peso = float(input(">>> Informe o peso do produto (em g): "))
            if checkAdd(tipo, preco, peso=peso):
                item = Alimento(nome, tipo, preco, marca,
                                data_vencimento, peso)
        elif tipo == 'bebida':
            volume = float(input(">>> Informe o volume do produto (em ml): "))
            if checkAdd(tipo, preco, volume=volume):
                item = Bebida(nome, tipo, preco, marca,
                              data_vencimento, volume)
        else:
            quantidade = int(
                input(">>> Informe a quantidade do produto (unid.): "))
            if checkAdd(tipo, preco, quantidade=quantidade):
                item = Alimento(nome, tipo, preco, marca,
                                data_vencimento, quantidade)

        estoque.add(item)
    elif selection == EDIT:
        printHeader('Edicao de Produtos')
        tipo = input(">>> Informe o tipo do produto (alimento/bebida/papelaria): ")
        id = int(input(">>> Informe o ID do prudoto: "))
        estoque.edit(tipo, id)
    elif selection == REMOVE:
        printHeader('Remocao de Produtos')
        tipo = input(">>> Informe o tipo do produto (alimento/bebida/papelaria): ")
        id = int(input(">>> Informe o ID do prudoto: "))
        estoque.remove(tipo, id)
    elif selection == LIST:
        estoque.list()
        clear()
    elif selection == REPORT:
        options = ['Por categoria', 'Por validade']
        option = int(promptScreen('Tipo de Relatório', options))
        if option in range(1, len(options)+1):
            if option == 1:
                criterio = input(">>> Informe por qual criterio deseja filtrar (categoria/mes): ")
                clear()
                estoque.reportCategoria(criterio)
                clear()
            elif option == 2:
                clear()
                estoque.reportValidade()
                clear()
        else:
            print(f"{Color.DANGER}[Erro]: A opcao informada nao eh valida.{Color.RESET}")
    else:
        print(f"{Color.DANGER}[Erro]: A opcao informada nao eh valida.{Color.RESET}")
        


def run():
    running = True
    options = ['Adicionar Produto',
               'Editar Produto',
               'Remover Produto',
               'Listar Produtos',
               'Relatórios',
               'Sair']

    while running:
        selection = int(promptScreen("Mercadinho da Dona Kátia", options))
        clear()
        if selection in range(1, len(options)+1):
            if selection == SAIR:
                running = False
            else:
                execute(selection)
        else:
            print(f"{Color.DANGER}[Erro]: A opcao informada nao eh valida.{Color.RESET}")
            input()
    print("Tchau!")
