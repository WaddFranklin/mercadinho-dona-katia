from datetime import date

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

    def __str__(self):
        str = ""
        attribs = {"id": self.id,
                   "nome": self.nome,
                   "tipo": self.tipo,
                   "preco": self.preco,
                   "marca": self.marca,
                   "data_vencimento": self.data_vencimento,
                   "data_adicao": self.data_adicao}

        for key, value in attribs.items():
            if key == "preco":
                str += f" {key}: R$ {value}\n"
            elif key == "data_adicao" or key == "data_vencimento":
                str += f" {key}: {value.strftime('%d/%m/%Y')}\n"
            else:
                str += f" {key}: {value}\n"
        return str

    def getDataVencimento(self):
        return self.data_vencimento.strftime('%d/%m/%Y')


class Alimento(Produto):
    def __init__(self, nome, tipo, preco, marca, data_vencimento, peso):
        super().__init__(nome, tipo, preco, marca, data_vencimento)
        self.peso = peso

    def __str__(self):
        return super().__str__() + f" peso: {self.peso} g"


class Bebida(Produto):
    def __init__(self, nome, tipo, preco, marca, data_vencimento, volume):
        super().__init__(nome, tipo, preco, marca, data_vencimento)
        self.volume = volume

    def __str__(self):
        return super().__str__() + f" volume: {self.volume} ml"


class Papelaria(Produto):
    def __init__(self, nome, tipo, preco, marca, data_vencimento, quantidade):
        super().__init__(nome, tipo, preco, marca, data_vencimento)
        self.quantidade = quantidade

    def __str__(self):
        return super().__str__() + f" quantidade: {self.quantidade} unid."
