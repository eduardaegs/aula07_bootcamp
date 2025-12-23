# Ler csv
# Carregar
# processar os dados para análise
# Calcular vendas
# Reportar as vendas totais

import csv
import random

# Configurações
colunas = ['produto', 'price', 'entregue']
produtos_lista = ['Smartphone', 'Notebook', 'Monitor', 'Teclado Mecânico', 'Mouse Gamer', 
                  'Fone de Ouvido', 'Cadeira Office', 'Webcam HD', 'Tablet', 'Smartwatch']
num_linhas = 5000

with open('vendas_1.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(colunas) # Cabeçalho
    
    for _ in range(num_linhas):
        produto = random.choice(produtos_lista)
        price = round(random.uniform(20.0, 5000.0), 2)
        entregue = random.choice([True, False])
        writer.writerow([produto, price, entregue])

print("Arquivo 'vendas_1.csv' com 5000 linhas gerado com sucesso!")