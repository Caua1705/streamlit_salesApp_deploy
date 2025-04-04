import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import names

FILIAIS = [
            {'estado': 'RS',
            'cidade': 'Porto Alegre',
            'vendedores': ['Rodrigo Tadewald', 'Luiza Cherobini']},

            {'estado': 'RS',
            'cidade': 'Canoas',
            'vendedores': ['Carlos Henrique', 'Luis Fernando']},

            {'estado': 'RS',
            'cidade': 'Caxias do Sul',
            'vendedores': ['Rodrigo Vanzeloti', 'Mateus Kienzle']},

            {'estado': 'RS',
            'cidade': 'Lajeado',
            'vendedores': ['Adriano Soares', 'Juliano Faccioni']},

            {'estado': 'SC',
            'cidade': 'Florianópolis',
            'vendedores': ['Claudia dos Santos', 'Mario Sérgio']},
            
            {'estado': 'SP',
            'cidade': 'São Paulo',
            'vendedores': ['Claudio Bueno', 'Cassia Moraes']},
            
            ]

PRODUTOS = [
            {'nome': 'Tenis Nike',
             'id': 0,
             'preco': 300},

            {'nome': 'Tenis Adidas',
             'id': 1,
             'preco': 450},

            {'nome': 'Tenis NB',
             'id': 2,
             'preco': 500},

            {'nome': 'Tenis Fila',
             'id': 3,
             'preco': 250},
           ]
GENEROS_CLIENTES = ['male', 'female']
FORMA_PAGAMENTO = ['pix', 'boleto'] + ['credito'] * 8


vendas = []
for _ in range(2000):
    filial = random.choice(FILIAIS)
    vendedor = random.choice(filial['vendedores'])
    produto = random.choice(PRODUTOS)
    hora_venda = datetime.now() - timedelta(days=random.randint(1, 250), hours=random.randint(-5, 5), minutes=random.randint(-30, 30))
    genero_cliente = random.choice(GENEROS_CLIENTES)
    nome_cliente = names.get_full_name(genero_cliente)
    forma_pagamento = random.choice(FORMA_PAGAMENTO)
    vendas += [{'data': hora_venda, 
                'id_venda': 0, 
                'filial': filial['cidade'], 
                'vendedor': vendedor, 
                'produto': produto['nome'],
                'cliente_nome': nome_cliente,
                'cliente_genero': genero_cliente.replace('female', 'feminino').replace('male', 'masculino'),
                'forma_pagamento': forma_pagamento,
                }]

df_vendas = pd.DataFrame(vendas).set_index('data').sort_index()
df_vendas['id_venda'] = [i for i in range(len(df_vendas))]
df_filiais = pd.DataFrame(FILIAIS)
df_produtos = pd.DataFrame(PRODUTOS)

pasta_atual = Path(__file__).parent

df_vendas.to_excel(pasta_atual / "vendas.xlsx")
df_filiais.to_excel(pasta_atual / "filiais.xlsx")
df_produtos.to_excel(pasta_atual / "produtos.xlsx")
