from etl import extract_data, produtos_entregues, somar_valores

path_arquivo = 'vendas.csv'

lista_de_produtos = extract_data(path_arquivo)
produtos = produtos_entregues(lista_de_produtos)
valor = somar_valores(produtos)
print(valor)