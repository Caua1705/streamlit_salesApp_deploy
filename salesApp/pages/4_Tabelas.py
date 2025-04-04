from pathlib import Path
import pandas as pd
import streamlit as st

dir_planilhas=Path(__file__).parents[2] / "datasets"

#Lendo planilhas:
df_filiais=pd.read_excel(dir_planilhas / "filiais.xlsx",index_col=0)
df_vendas=pd.read_excel(dir_planilhas / "vendas.xlsx",index_col=0)
df_produtos=pd.read_excel(dir_planilhas / "produtos.xlsx",index_col=0)
#Configuração da página:
st.set_page_config(layout="wide")
colunas_df_vendas=list(df_vendas.columns) 

#Seleção de Tabelas:
st.sidebar.markdown("### Seleção de Tabelas: ")
escolha_tabela=st.sidebar.selectbox("Selecione a tabela que você deseja ver:",["Vendas","Produtos","Filiais"])

#Condição Tabela Vendas: 
if escolha_tabela=="Vendas":
    st.sidebar.markdown("### Filtrar tabela: ")
#Colunas Selecionadas:
    selecao_df_vendas=st.sidebar.multiselect("Selecione as colunas da tabela: ",colunas_df_vendas,colunas_df_vendas)
    df_selecionado=(df_vendas[selecao_df_vendas])
#Filtrar Colunas:
    filtro,valor_filtro=st.sidebar.columns(2)
    filtro_col1=filtro.selectbox("Filtrar coluna",colunas_df_vendas)
    filtro_col2=valor_filtro.selectbox("Valor do filtro",dict(df_vendas[filtro_col1].value_counts()).keys())
#Botões:
    filtro,limpar=st.sidebar.columns(2)

    botao_filtrar=filtro.button("Filtrar")
    botao_limpar=limpar.button("Limpar")

    if botao_filtrar:
        df_filtrado = df_selecionado[df_vendas[filtro_col1] == filtro_col2]
        st.dataframe(df_filtrado,height=800)
    elif botao_limpar:
        st.dataframe(df_selecionado,height=800)
    else:
        st.dataframe(df_selecionado,height=800)

#Condição Tabela Produtos:
if escolha_tabela=="Produtos":
    st.dataframe(df_produtos)

#Condição Tabela Filiais:
if escolha_tabela=="Filiais":
    st.dataframe(df_filiais)
