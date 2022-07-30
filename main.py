'''
Projeto: Mercadinho da Dona Kátia
Autor: Franklin Nascimento | waddinsohn@gmail.com
Data: 29/07/2022
'''
from datetime import datetime
from datetime import date
from math import prod
from sqlite3 import Date


def describeProduct(attribs):
    for key, value in attribs.items():
        if key == "preco":
            print(f" {key}: R$ {value}")
        elif key == "data_adicao" or key == "data_vencimento":
            print(f" {key}: {value.strftime('%d/%m/%Y')}")
        else:
            print(f" {key}: {value}")

class Color:
    SUCCESS = '\033[92m' # green
    WARNING = '\033[93m' # yellow
    DANGER = '\033[91m'  # red
    RESET = '\033[0m'    # default

class Estoque:
    totalProdutos = 0
    
    def __init__(self):
        self.listaAlimentos = []
        self.listaBebidas = []
        self.listaPapelaria = []

    def add(self, produto):
        if (type(produto) is Alimento):
            self.listaAlimentos.append(produto)
        elif (type(produto) is Bebida):
            self.listaBebidas.append(produto)
        elif (type(produto) is Papelaria):
            self.listaPapelaria.append(produto)
        else:
            print(f"{Color.DANGER}[Erro]: O produto nao eh de um tipo valido.{Color.RESET}")
            return False
        
        print(f"{Color.SUCCESS}{produto.nome} {produto.marca} foi adicionado ao estoque com sucesso!{Color.RESET}")
        Estoque.totalProdutos += 1
        return True
        
    def remove(self):
        pass

    def edit():
        pass

    def status(self):
        print("*** Status do Estoque ***")
        print("+------------------------------")
        print(f"| Total de produtos: {self.totalProdutos}")
        print(f"| Total de alimentos: {len(self.listaAlimentos)}")
        print(f"| Total de bebidas: {len(self.listaBebidas)}")
        print(f"| Total de prod. de papelaria: {len(self.listaPapelaria)}")
        print("+------------------------------")


class Produto:
    
    idProduto = 0
    
    def __init__(self, nome, tipo, preco, marca, data_vencimento):
        Produto.idProduto += 1
        self.id = Produto.idProduto
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.marca = marca
        self.data_vencimento = date(int(data_vencimento[6:]), int(data_vencimento[3:5]), int(data_vencimento[:2]))
        self.data_adicao = date.today()

    def toString(self):
        attribs = {"id": self.id,
                   "nome": self.nome,
                   "tipo": self.tipo,
                   "preco": self.preco,
                   "marca": self.marca,
                   "data_vencimento": self.data_vencimento,
                   "data_adicao": self.data_adicao}
        describeProduct(attribs)


class Alimento(Produto):
    def __init__(self, nome, tipo, preco, marca, data_vencimento, peso):
        super().__init__(nome, tipo, preco, marca, data_vencimento)
        self.peso = peso

    def toString(self):
        super().toString()
        print(f" peso: {self.peso} g")


class Bebida(Produto):
    def __init__(self, nome, tipo, preco, marca, data_vencimento, volume):
        super().__init__(nome, tipo, preco, marca, data_vencimento)
        self.volume = volume

    def toString(self):
        super().toString()
        print(f" volume: {self.volume} ml")


class Papelaria(Produto):
    def __init__(self, nome, tipo, preco, marca, data_vencimento, quantidade):
        super().__init__(nome, tipo, preco, marca, data_vencimento)
        self.quantidade = quantidade

    def toString(self):
        super().toString()
        print(f" quantidade: {self.quantidade} unid.")


#  ---------------------- DEBUG ---------------------------
estoque = Estoque()
estoque.status()

produto = Produto("cafe", "teste", 10.0, "melita", "01/01/2023")
produto.toString()

print("-------------------")
alimento = Alimento("carne bovina", "alimento", 53.4, "friboi", "20/12/2022", 2000)
alimento.toString()

print("-------------------")
bebida = Bebida("vinho", "bebida", 53.4, "dom bosco", "20/12/2022", 1000)
bebida.toString()

print("-------------------")
papelaria = Papelaria("caixa de canetas", "papelaria", 53.4, "bic", "20/12/2022", 100)
papelaria.toString()
print("-------------------")
estoque.add(alimento)
estoque.add(bebida)
estoque.add(papelaria)
data = Date(2000, 1, 1)
estoque.add(data)
estoque.status()
