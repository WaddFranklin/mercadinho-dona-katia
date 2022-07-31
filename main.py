'''
Projeto: Mercadinho da Dona Kátia
Autor: Franklin Nascimento | waddinsohn@gmail.com
Data: 29/07/2022
'''

from datetime import timedelta
from datetime import date
from math import prod


def describeProduct(attribs):
    for key, value in attribs.items():
        if key == "preco":
            print(f" {key}: R$ {value}")
        elif key == "data_adicao" or key == "data_vencimento":
            print(f" {key}: {value.strftime('%d/%m/%Y')}")
        else:
            print(f" {key}: {value}")


class Color:
    SUCCESS = '\033[92m'  # green
    WARNING = '\033[93m'  # yellow
    DANGER = '\033[91m'   # red
    RESET = '\033[0m'     # default


class Estoque:
    totalProdutos = 0

    def __init__(self):
        self.listaAlimentos = {}
        self.listaBebidas = {}
        self.listaPapelaria = {}
        self.listas = {
            "alimento": self.listaAlimentos,
            "bebida": self.listaBebidas,
            "papelaria": self.listaPapelaria
        }

    def add(self, produto):
        if (type(produto) is Alimento):
            self.listaAlimentos[produto.id] = produto
        elif (type(produto) is Bebida):
            self.listaBebidas[produto.id] = produto
        elif (type(produto) is Papelaria):
            self.listaPapelaria[produto.id] = produto
        else:
            print(
                f"{Color.DANGER}[Erro]: O produto nao eh de um tipo valido.{Color.RESET}")
            return False

        print(f"{Color.SUCCESS}{produto.nome} {produto.marca} foi adicionado ao estoque com sucesso!{Color.RESET}")
        Estoque.totalProdutos += 1
        return True

    def getProduto(self, tipo, id):
        tipo = tipo.lower()
        if tipo in self.listas:
            if id in self.listas[tipo]:
                return [True, self.listas[tipo][id]]
            else:
                print(
                    f"{Color.DANGER}[Erro]: O id deste produto nao esta cadastrado no estoque.{Color.RESET}")
                return [False, None]
        else:
            print(
                f"{Color.DANGER}[Erro]: O tipo de produto nao eh valido.{Color.RESET}")
            return [False, None]

    def remove(self, tipo, id):
        existeProduto, _ = self.getProduto(tipo, id)
        if existeProduto:
            produto = self.listas[tipo].pop(id)
            print(
                f"{Color.SUCCESS}O produto {produto.nome} {produto.marca} foi removido com sucesso!{Color.RESET}")
        else:
            print(
                f"{Color.DANGER}[Erro]: O tipo de produto nao eh valido.{Color.RESET}")
            return False

        Estoque.totalProdutos -= 1
        return True

    def editCheck(self, key, value):
        if key in ['nome', 'marca']:
            return str(value)
        elif key in ['preco', 'peso', 'volume']:
            return float(value)
        elif key == 'quantidade':
            return int(value)
        elif key == 'data_vencimento':
            return date(int(value[6:]), int(value[3:5]), int(value[:2]))
        else:
            print(
                f"{Color.DANGER}[Erro]: O valor informado nao eh valido.{Color.RESET}")
            return False

    def edit(self, tipo, id):
        existeProduto, produto = self.getProduto(tipo, id)
        if existeProduto:
            produto.toString()
            option = input(">>> Qual propriedade deseja alterar? ").lower()
            attribs = ['nome', 'preco', 'marca',
                       'data_vencimento', 'peso', 'volume', 'quantidade']
            if option in attribs:
                value = input(">>> Digite o novo valor: ")
                value = self.editCheck(option, value)
                if value:
                    oldValue = getattr(produto, option, value)
                    setattr(produto, option, value)
                    newValue = getattr(produto, option, value)
                    print(f"{Color.SUCCESS}O(A) {option} do(a) produto foi alterado(a) de {Color.WARNING}'{oldValue}'{Color.SUCCESS} para {Color.WARNING}'{newValue}'{Color.SUCCESS} com sucesso!{Color.RESET}")
                    produto.toString()
                    return True

            else:
                print(
                    f"{Color.DANGER}[Erro]: Nao eh possivel alterar a propriedade informada ou nao existe.{Color.RESET}")
                return False
        else:
            print(
                f"{Color.DANGER}[Erro]: O id deste produto nao esta cadastrado no estoque.{Color.RESET}")
            return False

    def status(self):
        print("*** Status do Estoque ***")
        print("+------------------------------")
        print(f"| Total de produtos: {self.totalProdutos}")
        print(f"| Total de alimentos: {len(self.listaAlimentos)}")
        print(f"| Total de bebidas: {len(self.listaBebidas)}")
        print(f"| Total de prod. de papelaria: {len(self.listaPapelaria)}")
        print("+------------------------------")
        print(self.listas)

    def getProductsInValidity(self, listas, dayRange=30):
        today = date.today()
        dateLimit = today + timedelta(days=dayRange)
        inValidity = []
        for lista in listas.values():
            for produto in lista.values():
                data = produto.data_vencimento
                if (data >= today) and (data <= dateLimit):
                    inValidity.append(produto)
        return inValidity

    def printProductsInValidity(self, lista):
        today = date.today()
        title = 'Produtos com Vencimento em 30 dias'
        space = int((76 - len(title)) / 2)
        print("+" + "-"*76 + "+")
        print("|" + ' '*space + title + ' '*space + '|')
        print("+" + "-"*76 + "+")
        for produto in lista:
            dayRange = produto.data_vencimento - today
            nomeMarca = produto.nome + " " + produto.marca
            print("| {:>25} | R$ {:>8.2f} | {:>10} | {:>2} dias para vencer |".format(
                nomeMarca, produto.preco, produto.getDataVencimento(), str(dayRange.days)))
        print("+" + "-"*76 + "+")

    def reportValidade(self):
        inValidity = self.getProductsInValidity(self.listas)
        self.printProductsInValidity(inValidity)


class Produto:

    idProduto = 0

    def __init__(self, nome, tipo, preco, marca, data_vencimento):
        Produto.idProduto += 1
        self.id = Produto.idProduto
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.marca = marca
        self.data_vencimento = date(int(data_vencimento[6:]), int(
            data_vencimento[3:5]), int(data_vencimento[:2]))
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

    def getDataVencimento(self):
        return self.data_vencimento.strftime('%d/%m/%Y')


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

alimento = Alimento("miojo", "alimento", 1.99, "nissin", "10/08/2022", 100.0)
alimento.toString()
estoque.add(alimento)

bebida = Bebida("vinho", "bebida", 10.0, "dom bosco", "01/09/2022", 1000.0)
bebida.toString()
estoque.add(bebida)

papelaria = Papelaria("caixa de canetas", "papelaria",
                      30.99, "bic", "25/08/2022", 50)
papelaria.toString()
estoque.add(papelaria)

estoque.status()

data = date(2022, 9, 15)
today = date.today()
todayPlus30 = today + timedelta(days=30)
print(todayPlus30)

if (data >= today) and data <= todayPlus30:
    print("Faltam 30 dias para vencer o produto!")
elif data < today:
    print("Produto vencido!")
else:
    print("Mais de 30 dias para vencer!")

#estoque.remove("alimento", 1)
#estoque.edit("alimento", 1)
#estoque.edit("bebida", 2)
#estoque.edit("papelaria", 3)
# estoque.status()
estoque.reportValidade()
