import csv

def extract_data(nome_arquivo: str) -> list[dict]:
    '''
    Funçao que lê um arquivo csv e retorna uma lista de dicionários.
    '''
    lista = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            lista.append(linha)
    return lista


path_arquivo = 'vendas.csv'

vendas_consolidado: list[dict] 

vendas_consolidado = extract_data(path_arquivo)
# print(vendas_consolidado[0])


'''
Filtrar produtos entregues
'''

def produtos_entregues(lista: list[dict]) -> list[dict]:
    '''
    Função que filtra os produtos entregues de uma lista de dicionários.
    '''
    entregue = []
    for item in vendas_consolidado:
        if item['entregue']=='True':
            entregue.append(item)
    return entregue

lista_produtos = produtos_entregues(vendas_consolidado)
# print(lista_produtos[:10])


def somar_valores(lista_produtos_filtrados: list[dict]) -> float:
    '''
    Soma todos os produtos entregues da lista
    '''
    valor_total = 0
    for valor in lista_produtos:
        valor_total +=  float(valor.get('price'))
    return valor_total

vendas = somar_valores(lista_produtos)
# print(f'{vendas}')
