'''
Projeto: Mercadinho da Dona Kátia
Autor: Franklin Nascimento | waddinsohn@gmail.com
Data: 29/07/2022
'''

from Estoque import *


#  ---------------------- DEBUG ---------------------------
estoque = Estoque()
# estoque.status()

alimento = Alimento("miojo", "alimento", 1.99, "nissin", "10/08/2022", 100.0)
print(alimento)
estoque.add(alimento)

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
