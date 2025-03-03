import streamlit as st
from estrutura import setup_inicio, sidebar, rodape, ajuda
from data import custo_votos, despesas
import plotly.express as px

setup_inicio()

# Cache de dados para evitar recarregamento
@st.cache_data
def load_data():
    return custo_votos, despesas

custo_votos, despesas = load_data()

sidebar()

st.title("Análise de Gastos de Campanha - Deputado Estadual MG 2022")

filtros = st.container(border=True)

with filtros:
    st.markdown("#### Filtrar dados 🔍")
    cols = st.columns(2)
    with cols[0]:
        situacao = st.multiselect("Resultado eleitoral", custo_votos['Situação totalização'].unique(), default=None)
    with cols[1]:
        partido = st.multiselect("Partido", custo_votos['Partido'].unique(), default=None)

tabs = st.tabs(["Custo por Voto", "Gastos por Tipo"])

with tabs[0]:
    st.markdown("## Custo por Voto")

    df = custo_votos[['Nome candidato', 'Partido', 'numero_candidato', 'Situação totalização', 'votos', 'valor_despesa', 
                      'custo_voto']]

    dff = df.copy()

    if situacao:
        dff = dff[dff['Situação totalização'].isin(situacao)]
    if partido:
        dff = dff[dff['Partido'].isin(partido)]

    tabela, distribuicao, descritiva = st.tabs(["Tabela", "Distribuição", "Estatísticas Descritivas"])

    with tabela:
        st.dataframe(dff.sort_values(by='votos', ascending=False))

    with distribuicao:
        fig = px.scatter(dff, x='votos', y='valor_despesa', color='Partido', hover_name='Nome candidato')
        st.plotly_chart(fig, use_container_width=True)
    
    with descritiva:
        st.markdown(f'''
        ### Estatísticas Descritivas
        - **Total de candidatos**: {df.shape[0]}
        - **Votação mínima para eleição**: {df[df['Situação totalização'] == 'Eleito']['votos'].min()}
        - **Custo médio por voto (R$)**: {df['custo_voto'].mean():.2f}
        - **Custo mínimo por voto entre os eleitos (R$)**: {df[df['Situação totalização'] == 'Eleito']['custo_voto'].min()}
        - **Custo máximo por voto entre os eleitos (R$)**: {df[df['Situação totalização'] == 'Eleito']['custo_voto'].max()}
        - **Custo médio por voto entre os eleitos (R$)**: {df[df['Situação totalização'] == 'Eleito']['custo_voto'].mean():.2f}
        ''')

with tabs[1]:
    st.markdown("## Gastos por Tipo")
    selecao = st.expander(label="Tipo de despesa", expanded=False)
    with selecao:
        tipo_despesa = st.selectbox("Tipo de despesa", sorted(despesas['origem_despesa'].unique()), index=None, placeholder="Selecione um tipo de despesa")

    df = despesas.groupby(["Nome candidato", "origem_despesa"]).agg({
        "Partido": "first",
        "numero_candidato": "first",
        "Situação totalização": "first",
        "votos": "first",
        "valor_despesa": "sum",
    }).reset_index()    
    
    dff = df.copy()
        
    if situacao:
        dff = dff[dff['Situação totalização'].isin(situacao)]
    if partido:
        dff = dff[dff['Partido'].isin(partido)]
    if tipo_despesa:
        dff = dff[dff['origem_despesa'] == tipo_despesa]

    tabela, barra = st.tabs(["Tabela", "Gráfico de Barras"])

    with tabela:
        st.dataframe(dff.sort_values(by='valor_despesa', ascending=False).reset_index(drop=True))

    with barra:
        cols = st.columns(2)
        with cols[0]:
            head = st.select_slider("Mostrar os primeiros", options=[5, 10, 15, 20], value=5)
        with cols[1]:
            candidato = st.selectbox("Para mostrar despesas de apenas um candidato", sorted(dff['Nome candidato'].unique()), index=None, placeholder="Selecione um candidato")
        
        if tipo_despesa:
            df_forplot = dff.groupby('Nome candidato')['valor_despesa'].sum().sort_values(ascending=False).head(head).reset_index()
            fig = px.bar(df_forplot, x='Nome candidato', y='valor_despesa', hover_name='Nome candidato',
                        labels={'Nome candidato': '', 'valor_despesa': ''})
            st.plotly_chart(fig, use_container_width=True)
        elif candidato:
            df_forplot = dff[dff['Nome candidato'] == candidato].sort_values(by='valor_despesa', ascending=False).head(head).reset_index()
            fig = px.bar(df_forplot, x='origem_despesa', y='valor_despesa', hover_name='origem_despesa',
                        labels={'origem_despesa': '', 'valor_despesa': ''})
            st.plotly_chart(fig, use_container_width=True)
        else:
            df_forplot = dff.groupby('origem_despesa')['valor_despesa'].sum().sort_values(ascending=False).head(head).reset_index()
            fig = px.bar(df_forplot, x='origem_despesa', y='valor_despesa', hover_name='origem_despesa',
                        labels={'origem_despesa': '', 'valor_despesa': ''})
            st.plotly_chart(fig, use_container_width=True)

expander_ajuda = st.expander("Ajuda", icon="ℹ️", expanded=False)

with expander_ajuda:
    ajuda()

rodape()