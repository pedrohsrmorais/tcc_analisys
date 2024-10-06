import pandas as pd
import numpy as np

# Extração dos arquivos xls para dataframe
num_amostras = 27
dataframes_amostras = []
for i in range(2, num_amostras + 1):
    filename = f'./amostra{i}.xls'
    df = pd.read_excel(filename, sheet_name='Plan1')
    
    # Adicionando as colunas com valores iniciais 0
    df["[Tartrazina]"] = 0
    df["[Amaranto]"] = 0
    df["[Sunset Yellow]"] = 0

    # Ajustando valores de absorção e nm
    df[' Abs'] = df[' Abs'].str.replace(',', '.').astype(float)
    df['nm'] = df['nm'].str.replace(',', '.').astype(float)

    # Fazendo o pivot para colocar comprimentos de onda como colunas
    df_pivot = df.pivot(index=['[Tartrazina]', '[Amaranto]', '[Sunset Yellow]'], columns='nm', values=' Abs')

    # Resetando o índice para retornar as concentrações de A e B como colunas
    df_pivot = df_pivot.reset_index()
    
    # Adicionando o DataFrame pivotado à lista
    dataframes_amostras.append(df_pivot)

# --------- --------- --------- --------- --------- Adicionando as concentrações aos dataframes ---------


# --------- --------- --------- --------- --------- Amaranto --------- 

for i in range(2,5):
    dataframes_amostras[i]['[Amaranto]'] = 3

for i in range(5,8):
    dataframes_amostras[i]['[Amaranto]'] = 6

for i in range(11,14):
    dataframes_amostras[i]['[Amaranto]'] = 3

for i in range(14,17):
    dataframes_amostras[i]['[Amaranto]'] = 6

for i in range(20,23):
    dataframes_amostras[i]['[Amaranto]'] = 3

for i in range(23,26):
    dataframes_amostras[i]['[Amaranto]'] = 6


# --------- --------- --------- --------- --------- --------- Sunset Yellow --------- 

concentracoes_sunset_yellow = [3, 6, 0]

# Loop para percorrer os dataframes e associar as concentrações
for i in range(0, len(dataframes_amostras), 3):
    for j in range(3):
        if i + j < len(dataframes_amostras):  # Verifica se o índice não ultrapassa o número de amostras
            dataframes_amostras[i + j]['[Sunset Yellow]'] = concentracoes_sunset_yellow[j]


# --------- --------- --------- --------- --------- --------- Tartrazina --------- 

for i in range(8,17):
    dataframes_amostras[i]['[Tartrazina]'] = 3

for i in range(17,26):
    dataframes_amostras[i]['[Tartrazina]'] = 6


# Concatenando todos os DataFrames para criar um único DataFrame
df_concatenado = pd.concat(dataframes_amostras, ignore_index=True)

# Separando X (comprimentos de onda) e Y (concentrações)
X = df_concatenado.drop(columns=['[Tartrazina]', '[Amaranto]', '[Sunset Yellow]']).values  
Y = df_concatenado[['[Tartrazina]', '[Amaranto]','[Sunset Yellow]']].values  



# Salvando X e Y como arquivos .csv


pd.DataFrame(X).to_csv('X.csv', index=False)
pd.DataFrame(Y, columns=['[Tartrazina]', '[Amaranto]', '[Sunset Yellow]']).to_csv('Y.csv', index=False)

