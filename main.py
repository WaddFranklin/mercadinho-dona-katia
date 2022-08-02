'''
Projeto: Mercadinho da Dona Kátia
Autor: Franklin Nascimento | waddinsohn@gmail.com
Data: 29/07/2022
'''

from Estoque import *


#  ---------------------- DEBUG ---------------------------
estoque = Estoque()
# estoque.status()

alimento1 = Alimento("miojo", "alimento", 1.99, "nissin", "10/08/2022", 100.0)
print(alimento1)
estoque.add(alimento1)

alimento2 = Alimento("feijao", "alimento", 4.53, "carioca", "13/09/2022", 1000.0)
print(alimento2)
estoque.add(alimento2)

bebida = Bebida("vinho", "bebida", 10.0, "dom bosco", "01/09/2022", 1000.0)
print(bebida)
estoque.add(bebida)

papelaria = Papelaria("caixa de canetas", "papelaria",
                      30.99, "bic", "25/08/2022", 50)
print(papelaria)
estoque.add(papelaria)

estoque.status()

#estoque.remove("alimento", 1)
#estoque.edit("alimento", 1)
#estoque.edit("bebida", 2)
#estoque.edit("papelaria", 3)
# estoque.status()
estoque.reportValidade()
#estoque.reportCategoria('mes')

#print(alimento1.__dict__)
#printListAsTable("Produtos em Estoque", [alimento1, alimento2, bebida, papelaria])