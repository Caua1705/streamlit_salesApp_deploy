import streamlit as st

st.markdown('# Bem-vindo ao Analisador de Vendas')

st.divider()

st.markdown(
    '''
    Este projeto visa criar um painel de análise de vendas completo e interativo. Através de filtros dinâmicos, tabelas detalhadas e dinâmicas, e gráficos intuitivos,
    os usuários poderão explorar os dados de vendas de forma eficiente. Além disso, o painel permitirá a adição de novas vendas e a exportação de dados,
    facilitando o acompanhamento e a tomada de decisões estratégicas.
    Utilizei três principais bibliotecas para o seu desenvolvimento:

    - `pandas`: para manipulação de dados em tabelas
    - `plotly`: para geração de gráficos
    - `streamlit`: para criação desse webApp interativo que você se encontra nesse momento

    Os dados utilizados foram gerados pelo script 'gerador_de_vendas.py' que se encontra junto do código fonte do projeto. Os dados podem ser visualizados na aba de tabelas!
'''
            )