import streamlit as st
import pandas as pd
from estrutura import setup_inicio, sidebar, rodape, ajuda_resultados
import pydeck as pdk
from data import resultadogeo, mesoregioes
import geopandas as gpd
import plotly.express as px

setup_inicio()

@st.cache_data
def load_data(ttl=600):
    return resultadogeo[['Nome candidato', 'Partido', 'Situação totalização', 'votos', 'longitude', 'latitude', 'mesorregiao', 'municipio']]

@st.cache_data
def fetch_geojson():
    url = 'http://ide.dev.projetobrumadinho.ufmg.br/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Ameso_mg&outputFormat=json&srs=EPSG%3A4674&srsName=EPSG%3A4674'
    return gpd.read_file(url).to_crs(epsg=4326).__geo_interface__

st.title('Mapas Eleitorais')

# Abas para diferentes visualizações
tab1, tab2 = st.tabs(["Mapa de Calor", "Resultados Agregados"])

with tab1:
    resultadogeo = load_data()
    resultadogeo['Situação totalização'] = resultadogeo['Situação totalização'].astype('category')
    resultadogeo['Partido'] = resultadogeo['Partido'].astype('category')
    # Código existente para o mapa de calor
    filtros = st.container(border=True)
    with filtros:
        st.markdown('#### Agregar dados por:')
        cols = st.columns(3)
        with cols[0]:
            situacao = st.multiselect(
                "Resultado eleitoral",
                resultadogeo['Situação totalização'].unique(),
                default="Eleito"
            )

        with cols[1]:
            if situacao:
                partidos_filtrados = sorted(resultadogeo[resultadogeo['Situação totalização'].isin(situacao)]['Partido'].unique())
            else:
                partidos_filtrados = sorted(resultadogeo['Partido'].unique())

            partido = st.multiselect(
                "Partido",
                partidos_filtrados,
                default="PT"
            )

        with cols[2]:
            mask = pd.Series(True, index=resultadogeo.index)
            if situacao:
                mask &= resultadogeo['Situação totalização'].isin(situacao)
            if partido:
                mask &= resultadogeo['Partido'].isin(partido)

            dff = resultadogeo.loc[mask]

            candidatos_filtrados = sorted(dff['Nome candidato'].unique())
            candidato = st.selectbox(
                "Candidato",
                candidatos_filtrados,
                index=None,
                placeholder="Selecione um candidato"
            )

    if candidato:
        geojson_data = fetch_geojson()

        dff = dff[dff['Nome candidato'] == candidato]

        geojson_layer = pdk.Layer(
            'GeoJsonLayer',
            data=geojson_data,  # Use os dados reprojetados
            opacity=0.8,
            stroked=True,  # Habilita as bordas
            filled=False,  # Desabilita o preenchimento (para ver apenas os contornos)
            extruded=False,
            wireframe=False,
            get_line_color=[0, 0, 0, 255],  # Cor das bordas (preto)
            get_line_width=350,  # Largura das bordas
            pickable=False,
        )

        heatmap = pdk.Layer(
            'HeatmapLayer',
            data=dff,
            get_position='[longitude, latitude]',
            get_weight='votos / 100',
            opacity=0.8,
            radius_pixels=50,
            intensity=10,
            threshold=0.05
        )

        initial_view_state = pdk.ViewState(
            latitude=-18.554376,
            longitude=-48.0922571,
            zoom=6,
            pitch=10,
            bearing=10
        )

        r = pdk.Deck(
            map_style='light',
            layers=[geojson_layer, heatmap],
            initial_view_state=initial_view_state
        )

        st.pydeck_chart(r)

    if not candidato:
        st.markdown('#### Selecione um candidato para visualizar o mapa.')

with tab2:
    st.markdown('#### Resultados Agregados')

    nivel = st.pills(label="Selecione o nível de agregação", options=["Mesorregião", "Município"], default=None)
    
    if nivel == "Mesorregião":
        
        mesorregiao_selecionada = st.pills(label="Selecione a mesorregião", options=mesoregioes.keys(), default=None)

        head = st.slider("Número de candidatos", 5, 20, 5)

        if mesorregiao_selecionada:
            data_forplot = resultadogeo[resultadogeo['mesorregiao'] == mesorregiao_selecionada].groupby(['Nome candidato']).agg({'votos': 'sum',
                                                                 'Partido': 'first',
                                                                 'Situação totalização': 'first'
                                                                 }).sort_values(by='votos', ascending=False).head(head).reset_index()
            fig = px.bar(data_forplot, 
                         x="votos", 
                         y="Nome candidato",
                         color="Partido", 
                         labels={"votos": "Total de votos", "Nome candidato": "Candidato"},
                         orientation='h')
            
            fig.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig)

    elif nivel == "Município":
        municipio_selecionado = st.selectbox(label="Selecione o município", 
                                         options=sorted(list(set([municipio for municipios in mesoregioes.values() for municipio in municipios]))), 
                                         index=None,)

        head = st.slider("Número de candidatos", 5, 20, 5)

        if municipio_selecionado:
            data_forplot = resultadogeo[resultadogeo['municipio'] == municipio_selecionado].groupby(['Nome candidato']).agg({'votos': 'sum',
                                                                 'Partido': 'first',
                                                                 'Situação totalização': 'first'
                                                                 }).sort_values(by='votos', ascending=False).reset_index().head(head)
            fig = px.bar(data_forplot, 
                         x="votos", 
                         y="Nome candidato", 
                         color="Partido", 
                         labels={"votos": "Total de votos", "Nome candidato": "Candidato"},
                         orientation='h')
            fig.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig)

sidebar()

expander_ajuda = st.expander("Ajuda", icon="ℹ️", expanded=False)

with expander_ajuda:
    ajuda_resultados()

rodape()

