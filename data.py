import pandas as pd
import pickle

# Custo por voto

resultado = pd.read_parquet('dados/resultado.parquet')

votacao = resultado.groupby("numero_candidato").agg({
    "votos": "sum",
    "Nome candidato": "first",
    "Partido": "first",
    "Situação totalização": "first",
    }).sort_values(by="votos", ascending=False).reset_index()

despesas = pd.read_parquet('dados/despesas.parquet')
despesas['numero_candidato'] = despesas['numero_candidato'].astype(int)
despesas = despesas.merge(votacao, on="numero_candidato", how="left")

total_despesas = despesas.groupby("numero_candidato")["valor_despesa"].sum().reset_index()

custo_votos = votacao.merge(total_despesas, on="numero_candidato", how="left")
custo_votos['custo_voto'] = custo_votos['valor_despesa'] / custo_votos['votos']
custo_votos = custo_votos[custo_votos['votos'] > 0]
custo_votos['custo_voto'] = custo_votos['custo_voto'].round(2)

locais = pd.read_parquet('dados/locais.parquet')

resultadogeo = pd.merge(
    resultado[resultado['Situação totalização'].isin(['Eleito', 'Suplente'])], 
    locais, 
    on=['zona', 'secao'], 
    how='left')

resultadogeo = resultadogeo.groupby(['id_municipio_nome', 'Nome candidato']).agg({
    'votos': 'sum',
    'Partido': 'first',
    'Situação totalização': 'first',
    'latitude': 'first',
    'longitude': 'first',
    'mesorregiao': 'first'
}).reset_index()

resultadogeo.rename(columns={'id_municipio_nome': 'municipio'}, inplace=True)

with open('mesoregioes.pkl', 'rb') as f:
    mesoregioes = pickle.load(f)    

