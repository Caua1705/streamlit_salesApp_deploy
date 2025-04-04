from pathlib import Path
import pandas as pd
import streamlit as st
from datetime import datetime

dir_planilhas=Path(__file__).parents[1] / "Planilhas"

#Lendo planilhas:
df_filiais=pd.read_excel(dir_planilhas / "filiais.xlsx",index_col=0)
df_vendas=pd.read_excel(dir_planilhas / "vendas.xlsx",index_col=0)
df_produtos=pd.read_excel(dir_planilhas / "produtos.xlsx",index_col=0)

df_produtos.rename(columns={"nome" : "produto"},inplace=True)
            
df_vendas=pd.merge(df_vendas,df_produtos,on="produto",how="left")

comissao=0.08

df_vendas["comissao"]=df_vendas["preco"]*comissao

valores_indice=["filial","vendedor","produto","cliente_genero","forma_pagamento"]

indice_selecionado=st.sidebar.multiselect("Selecione os índices",valores_indice)
coluna_selecionada=st.sidebar.multiselect("Selecione as colunas",[valor for valor in valores_indice if valor not in indice_selecionado])
valor_analise=st.sidebar.selectbox("Selecione o valor da análise:",["preco","comissao"])
metrica=st.sidebar.selectbox("Selecione a métrica:",["Soma","Contagem"])

def tabela_dinamica(df_vendas, indice_selecionado, coluna_selecionada, valor_analise, metrica):
    if indice_selecionado and coluna_selecionada:
        if metrica == "Soma":
            df_pivot = pd.pivot_table(df_vendas, values=valor_analise, index=indice_selecionado, columns=coluna_selecionada, aggfunc="sum", fill_value=0)
        else:
            df_pivot = pd.pivot_table(df_vendas, values=valor_analise, index=indice_selecionado, columns=coluna_selecionada, aggfunc="count", fill_value=0)
        st.write(df_pivot)

tabela_dinamica(df_vendas, indice_selecionado, coluna_selecionada, valor_analise, metrica)