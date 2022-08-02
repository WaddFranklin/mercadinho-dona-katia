from Produto import *
from Util import *
from datetime import timedelta


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

    def reportValidade(self):
        inValidity = self.getProductsInValidity(self.listas)
        printListAsTable("Produtos que vencem em 30 dias", inValidity)

    def reportCategoria(self, mode='categoria'):
        if mode == 'categoria':
            categoria = input(
                ">>> Informe qual categoria de produtos deseja listar: ")
            if categoria in ['alimento', 'bebida', 'papelaria']:
                lista = self.listas[categoria]
                result = [produto for produto in lista.values()]
                printListAsTable(f"Lista de {categoria}s", result)
            else:
                print(
                    f"{Color.DANGER}[Erro]: A categoria de produto informada nao eh valida.{Color.RESET}")
                return False
        elif mode == 'mes':
            result = []
            mes = int(
                input(">>> Informe qual o mês do ano que deseja listar (de 1 a 12): "))

            if mes in range(1, 13):
                for lista in self.listas.values():
                    for produto in lista.values():
                        if produto.data_vencimento.month == mes:
                            result.append(produto)
                printListAsTable(
                    f"Produtos com vencimento no mes {mes}", result)
            else:
                print(
                    f"{Color.DANGER}[Erro]: O mes informado nao eh valido.{Color.RESET}")
                return False
        else:
            print(
                f"{Color.DANGER}[Erro]: O modo especificado nao eh valido.{Color.RESET}")
            return False
