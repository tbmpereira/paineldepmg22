import streamlit as st

def setup_inicio():
    # Configuração inicial do Streamlit
    st.set_page_config(
        page_title='Análise Eleições 2022 - Deputado Estadual MG',
        page_icon='🇧🇷', 
        layout='wide'
    )

def sidebar():
    with st.sidebar:
        st.page_link("app.py", label="Início", icon="🏠")
        st.page_link("pages/votacao.py", label="Resultados Eleitorais", icon="🗺️")
        st.page_link("pages/despesas.py", label="Gastos de Campanha", icon="💸")


def rodape():
    st.markdown("""
    ---
    """)

    st.markdown("""
    Desenvolvido por: [Marcelo Pereira](https://marcelo-pereira.notion.site/) |
    Fonte dos dados: [TSE](https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao/home?session=8400380217580)
    """)

def ajuda():
    st.markdown("""
        ### Guia de Uso e Interpretação do Dashboard de Análise de Gastos de Campanha

        Este dashboard foi desenvolvido para analisar os gastos de campanha dos candidatos a deputado estadual em Minas Gerais no ano de 2022. Ele permite filtrar e visualizar dados de custo por voto e gastos por tipo de despesa, além de fornecer estatísticas descritivas e gráficos interativos. Abaixo está um guia para ajudá-lo a navegar e interpretar as informações disponíveis.

        #### 1. **Filtros**
        - **Resultado Eleitoral**: Filtre os candidatos por situação eleitoral (Eleito, Não Eleito, etc.).
        - **Gênero**: Filtre os candidatos por gênero.
        - **Cor/Raça**: Filtre os candidatos por cor/raça.
        - **Partido**: Filtre os candidatos por partido político.
        - **Faixa Etária**: Selecione uma faixa etária específica para análise.

        #### 2. **Abas de Análise**
        O dashboard está dividido em duas abas principais:

        ##### **Aba 1: Custo por Voto**
        - **Tabela**: Exibe uma tabela com os candidatos filtrados, ordenados por votos nominais. Você pode ver detalhes como nome, partido, número do candidato, situação eleitoral, votos nominais, valor das despesas e custo por voto.
        - **Distribuição**: Um gráfico de dispersão que relaciona os votos nominais com o valor das despesas, colorido por partido. Passe o mouse sobre os pontos para ver detalhes sobre cada candidato.
        - **Estatísticas Descritivas**: Fornece métricas como o número total de candidatos, votação mínima para eleição, custo médio por voto, e custo mínimo/máximo por voto entre os eleitos.

        ##### **Aba 2: Gastos por Tipo**
        - **Tabela**: Exibe uma tabela com os gastos dos candidatos, agrupados por tipo de despesa. Você pode filtrar por tipo de despesa e ordenar por valor total gasto.
        - **Gráfico de Barras**: 
            - **Por Candidato**: Selecione um candidato específico para visualizar os gastos por tipo de despesa.
            - **Por Tipo de Despesa**: Visualize os gastos totais por tipo de despesa, com a opção de mostrar os primeiros 5, 10, 15 ou 20 itens.

        #### 3. **Interpretação dos Gráficos**
        - **Gráfico de Dispersão (Custo por Voto)**: Este gráfico ajuda a identificar a relação entre o número de votos recebidos e o valor gasto na campanha. Candidatos com muitos votos e baixo custo por voto são considerados mais eficientes.
        - **Gráfico de Barras (Gastos por Tipo)**: Este gráfico mostra a distribuição dos gastos por tipo de despesa. Ele pode ajudar a identificar quais tipos de despesas foram mais significativos na campanha de um candidato ou no geral.

        #### 4. **Dicas de Uso**
        - Utilize os filtros para refinar sua análise e focar em grupos específicos de candidatos.
        - Explore as diferentes abas para obter uma visão completa dos gastos de campanha.
        - Passe o mouse sobre os gráficos para obter informações detalhadas sobre cada ponto ou barra.

        Este dashboard é uma ferramenta poderosa para entender como os recursos financeiros foram utilizados nas campanhas eleitorais de 2022 em Minas Gerais. Utilize os filtros e gráficos interativos para explorar os dados e tirar suas próprias conclusões.
        """)
    
def ajuda_resultados():
    st.markdown("""
        ### Guia de Uso e Interpretação do Dashboard de Mapas Eleitorais

        Este dashboard foi desenvolvido para visualizar e analisar os resultados eleitorais por meio de mapas e gráficos interativos. Ele permite explorar os dados de votação por candidato, partido e região, além de fornecer uma visão geográfica dos resultados. Abaixo está um guia para ajudá-lo a navegar e interpretar as informações disponíveis.

        #### 1. **Filtros**
        - **Resultado Eleitoral**: Filtre os candidatos por situação eleitoral (Eleito, Não Eleito, etc.).
        - **Partido**: Filtre os candidatos por partido político.
        - **Candidato**: Selecione um candidato específico para visualizar os dados de votação no mapa.

        #### 2. **Abas de Análise**
        O dashboard está dividido em duas abas principais:

        ##### **Aba 1: Mapa de Calor**
        - **Mapa Interativo**: Exibe um mapa de calor com a distribuição dos votos para o candidato selecionado. Quanto mais intensa a cor, maior a concentração de votos naquela região.
        - **Filtros**: Utilize os filtros de resultado eleitoral, partido e candidato para refinar a visualização no mapa.
        - **Dicas**:
            - Passe o mouse sobre as áreas do mapa para ver o total de votos em cada localização.
            - Selecione um candidato para visualizar a distribuição geográfica dos votos.

        ##### **Aba 2: Resultado por Mesorregião**
        - **Nível de Agregação**: Escolha entre visualizar os resultados por **Mesorregião** ou **Município**.
        - **Gráfico de Barras**: 
            - **Por Mesorregião**: Selecione uma mesorregião para visualizar os candidatos mais votados naquela área.
            - **Por Município**: Selecione um município para visualizar os candidatos mais votados naquela localidade.
        - **Dicas**:
            - Utilize o slider para ajustar o número de candidatos exibidos no gráfico.
            - Passe o mouse sobre as barras para ver detalhes sobre o total de votos, partido e situação eleitoral de cada candidato.

        #### 3. **Interpretação dos Gráficos e Mapas**
        - **Mapa de Calor**: Este mapa ajuda a identificar as regiões com maior concentração de votos para um candidato específico. Áreas mais escuras indicam maior número de votos.
        - **Gráfico de Barras**: Este gráfico mostra os candidatos mais votados em uma mesorregião ou município, permitindo comparar o desempenho dos candidatos em diferentes áreas.

        #### 4. **Dicas de Uso**
        - Utilize os filtros para refinar sua análise e focar em candidatos, partidos ou regiões específicas.
        - Explore as diferentes abas para obter uma visão completa dos resultados eleitorais.
        - Passe o mouse sobre os mapas e gráficos para obter informações detalhadas sobre cada região ou candidato.

        Este dashboard é uma ferramenta poderosa para entender a distribuição geográfica dos votos e o desempenho dos candidatos nas eleições. Utilize os filtros e visualizações interativas para explorar os dados e tirar suas próprias conclusões.
        """)