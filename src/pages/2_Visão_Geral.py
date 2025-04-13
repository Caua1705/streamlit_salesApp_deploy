import pandas as pd
import streamlit as st
from datetime import date, timedelta
import plotly.express as px
from carregamento_dados import carregar_dados

dataframes,dir_planilhas=carregar_dados()

#Criando dataframe completo
df_vendas=dataframes["vendas"].reset_index()

dataframes["produtos"].rename(columns={"nome" : "produto"},inplace=True)
            
df_vendas=pd.merge(df_vendas,dataframes["produtos"],on="produto",how="left")

df_vendas=df_vendas.set_index("data")

#Criando botões de data:
data_final_def=df_vendas.index.date.max()
data_inicial_def=date(year=data_final_def.year,month=data_final_def.month,day=1)

data_inicial=st.sidebar.date_input("Data inicial",data_inicial_def)
data_final=st.sidebar.date_input("Data final",data_final_def)

st.markdown("# Dashboard de Análise")

#Criando as colunas:
col1,col2,col3,col4=st.columns(4)

#Variavel que filtra o df_vendas pelo periodo
df_vendas_corte=df_vendas[(df_vendas.index.date>=data_inicial) & (df_vendas.index.date<=data_final)]
#ícones de indicação 
df_vendas_corte_indicacao=df_vendas[(df_vendas.index.date>=data_inicial - timedelta(days=30)) & (df_vendas.index.date<=data_final - timedelta(days=30)) ]

#col1:
valor_vendas_periodo=f"R$ {df_vendas_corte["preco"].sum():.2f}"

dif_metrica_valor=df_vendas_corte["preco"].sum() - df_vendas_corte_indicacao["preco"].sum()

col1.metric("Valor vendas no período",valor_vendas_periodo,float(dif_metrica_valor))

#col2:
quantidade_vendas_periodo=f"{df_vendas_corte["preco"].count()}"

dif_metrica_quantidade=df_vendas_corte["preco"].count() - df_vendas_corte_indicacao["preco"].count()

col2.metric("Quantidade de vendas no período",quantidade_vendas_periodo,int(dif_metrica_quantidade))

#col3:
principal_filial_periodo=df_vendas_corte["filial"].value_counts().index[0]
col3.metric("Principal filial",principal_filial_periodo)

#col4:
principal_vendedor_periodo=df_vendas_corte["vendedor"].value_counts().index[0]
col4.metric("Principal Vendedor",principal_vendedor_periodo)

st.divider()

#Selectbox "Analisar"
valores_analise={"Filial":"filial","Vendedor":"vendedor","Produto":"produto","Forma de Pagamento":"forma_pagamento","Gênero Cliente":"cliente_genero"}
analisar=st.sidebar.selectbox("Analisar",list(valores_analise.keys()))
analisar=valores_analise[analisar]

col21,col22=st.columns(2)

#Criando coluna dia_venda no df_vendas_corte
df_vendas_corte["dia_venda"]=df_vendas_corte.index.date

#Agrupando pela data e pelo preço:
venda_dia=df_vendas_corte.groupby("dia_venda")["preco"].sum()
venda_dia.name="Valor Venda"

#Criando gráfico de linhas:
grafico_linhas=px.line(venda_dia)
col21.plotly_chart(grafico_linhas)

#Criando gráfico de pizza:
grafico_pizza=px.pie(df_vendas_corte,names=analisar,values="preco")
col22.plotly_chart(grafico_pizza)

st.divider()

