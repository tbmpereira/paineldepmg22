import streamlit as st
from estrutura import setup_inicio, sidebar, rodape

setup_inicio()

sidebar()

st.title('Análise Eleições 2022 - Deputado Estadual MG')

st.write("""
         Este é um painel interativo que permite analisar resultados eleitorais e gastos de campanha dos candidatos a Deputado Estadual de Minas Gerais nas eleições de 2022.
         Utilize a barra lateral para filtrar os dados que deseja visualizar.
         """)

# Explicação curta sobre o dashboard
st.markdown("""
    ### Sobre o Dashboard
    Este dashboard foi desenvolvido para fornecer uma visão detalhada dos resultados eleitorais e dos gastos de campanha dos candidatos a Deputado Estadual em Minas Gerais em 2022. Ele permite explorar dados de votação, custo por voto e distribuição de gastos por tipo de despesa, além de oferecer visualizações geográficas e gráficos interativos.

    #### Principais Funcionalidades:
    - **Mapa de Calor**: Visualize a distribuição geográfica dos votos por candidato.
    - **Resultados por Mesorregião/Município**: Analise os candidatos mais votados em cada região.
    - **Gastos de Campanha**: Explore os gastos por tipo de despesa e o custo por voto.
    - **Filtros Interativos**: Utilize filtros para refinar sua análise por partido, situação eleitoral, gênero e mais.
    """)

rodape()