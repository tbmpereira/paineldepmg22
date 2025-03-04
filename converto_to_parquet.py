import os
import pandas as pd

# Caminho da pasta com os arquivos CSV
caminho_pasta_csv = 'dados'
# Caminho da pasta onde os arquivos Parquet serão salvos
caminho_pasta_parquet = 'dados_parquet'

# Cria a pasta de destino se não existir
os.makedirs(caminho_pasta_parquet, exist_ok=True)

# Lista todos os arquivos na pasta de dados
arquivos = os.listdir(caminho_pasta_csv)

# Filtra apenas os arquivos CSV
arquivos_csv = [arquivo for arquivo in arquivos if arquivo.endswith('.csv')]

# Converte cada arquivo CSV para Parquet
for arquivo_csv in arquivos_csv:
    caminho_csv = os.path.join(caminho_pasta_csv, arquivo_csv)
    df = pd.read_csv(caminho_csv)
    
    nome_arquivo_parquet = os.path.splitext(arquivo_csv)[0] + '.parquet'
    caminho_parquet = os.path.join(caminho_pasta_parquet, nome_arquivo_parquet)
    
    df.to_parquet(caminho_parquet)

print("Conversão concluída!")