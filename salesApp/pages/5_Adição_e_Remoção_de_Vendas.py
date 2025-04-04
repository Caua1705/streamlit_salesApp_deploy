from pathlib import Path
import pandas as pd
import streamlit as st
from datetime import datetime

dir_planilhas=Path(__file__).parents[1] / "Planilhas"

#Lendo planilhas:
df_filiais=pd.read_excel(dir_planilhas / "filiais.xlsx",index_col=0)
df_vendas=pd.read_excel(dir_planilhas / "vendas.xlsx",index_col=0)
df_produtos=pd.read_excel(dir_planilhas / "produtos.xlsx",index_col=0)


 #session_state É um dicionário especial fornecido pelo Streamlit para armazenar variáveis que persistem entre as reexecuções do seu script.

#A ideia aqui é garantir que os DataFrames sejam carregados e armazenados no st.session_state apenas na primeira execução do script.
if not "dados" in st.session_state:
    dados={"df_vendas":df_vendas,
           "df_filiais":df_filiais,
           "df_produtos":df_produtos}
    st.session_state["dados"]=dados
    # Inicializa o session_state com o DataFrame original de vendas
    st.session_state["df_vendas_copia"] = df_vendas.copy()
    df_vendas = st.session_state['dados']['df_vendas']
    df_filiais = st.session_state['dados']['df_filiais']
    df_produtos = st.session_state['dados']['df_produtos']

#Configuração da página:
st.set_page_config(layout="wide")
colunas_df_vendas=list(df_vendas.columns)

#Adição de Vendas:

#Seleção Filial:
lista_filiais=(df_vendas["filial"].unique().tolist())
st.sidebar.markdown("### Adição de Vendas")
filial_selecionada=st.sidebar.selectbox("Selecione a filial:",lista_filiais)

#Seleção Vendedor:
vendedores_filtrados=df_vendas.loc[df_vendas["filial"]==filial_selecionada,"vendedor"].unique().tolist()
vendedor_selecionado=st.sidebar.selectbox("Selecione o vendedor:",vendedores_filtrados)

#Seleção Produto:
produto_selecionado=st.sidebar.selectbox("Selecione o produto",df_vendas["produto"].unique().tolist())

#Nome do Cliente:
nome_cliente=st.sidebar.text_input("Nome do cliente:")

#Gênero do Cliente:
genero_cliente=st.sidebar.selectbox("Gênero cliente",df_vendas["cliente_genero"].unique().tolist())

#Forma de Pagamento:
forma_pagamento=st.sidebar.selectbox("Forma de pagamento:",df_vendas["forma_pagamento"].unique().tolist())

#Adicionar Venda:
adicionar_venda=st.sidebar.button("Adicionar Venda")

if adicionar_venda:
    dados_venda_adicionada={"data":datetime.now(),
                            "id_venda":st.session_state["df_vendas_copia"]["id_venda"].max()+1,
                            "filial":filial_selecionada,
                            "vendedor":vendedor_selecionado,
                            "produto":produto_selecionado,
                            "cliente_nome":nome_cliente,
                            "cliente_genero":genero_cliente,
                            "forma_pagamento":forma_pagamento,
                            }

    df_venda_adicionada=pd.DataFrame([dados_venda_adicionada])
    df_venda_adicionada=df_venda_adicionada.set_index("data")
    # Concatena a nova venda com o DataFrame armazenado no session_state
    st.session_state["df_vendas_copia"] = pd.concat([st.session_state["df_vendas_copia"], df_venda_adicionada])

    #Escreve o df atualizado de volta para o excel 
    st.session_state["df_vendas_copia"].to_excel(dir_planilhas / "vendas.xlsx")

# Exibe o DataFrame concatenado atualizado
st.dataframe(st.session_state["df_vendas_copia"], height=800)

#Remover Venda:
st.sidebar.markdown("### Remoção de Vendas")
id_removido= st.sidebar.selectbox("Id venda a ser removido",st.session_state["df_vendas_copia"]["id_venda"])
remover_venda=st.sidebar.button("Remover Venda")
if remover_venda:
    st.session_state["df_vendas_copia"] = st.session_state["df_vendas_copia"][st.session_state["df_vendas_copia"]["id_venda"] != id_removido]
     #Escreve o df atualizado de volta para o excel 
    st.session_state["df_vendas_copia"].to_excel(dir_planilhas / "vendas.xlsx")
    st.dataframe(st.session_state["df_vendas_copia"], height=800)