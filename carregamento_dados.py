from pathlib import Path
import pandas as pd

# Lendo e carregando os dados das planilhas em DataFrames

def carregar_dados():
    dir_planilhas = Path(__file__).parent / "datasets"
    df_filiais=pd.read_excel(dir_planilhas / "filiais.xlsx",index_col=0)
    df_vendas=pd.read_excel(dir_planilhas / "vendas.xlsx",index_col=0)
    df_produtos=pd.read_excel(dir_planilhas / "produtos.xlsx",index_col=0)
    dataframes={"vendas":df_vendas,"produtos":df_produtos,"filiais":df_filiais}
    return dataframes,dir_planilhas
