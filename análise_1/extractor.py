import pandas as pd
import numpy as np


# Lendo os arquivos XLS
dataframe_amostra_1 = pd.read_excel('./amostra1.xls', sheet_name='Plan1')
dataframe_amostra_2 = pd.read_excel('./amostra2.xls', sheet_name='Plan1')
dataframe_amostra_3 = pd.read_excel('./amostra3.xls', sheet_name='Plan1')
dataframe_amostra_4 = pd.read_excel('./amostra4.xls', sheet_name='Plan1')
dataframe_amostra_5 = pd.read_excel('./amostra5.xls', sheet_name='Plan1')
dataframe_amostra_6 = pd.read_excel('./amostra6.xls', sheet_name='Plan1')

# Atribuição das colunas de concentração (Variando de 10 mg/L até 0 mg/L)
dataframe_amostra_1[['[A]', '[B]']] = [10, 0]
dataframe_amostra_2[['[A]', '[B]']] = [8, 2]
dataframe_amostra_3[['[A]', '[B]']] = [6, 4]
dataframe_amostra_4[['[A]', '[B]']] = [4, 6]
dataframe_amostra_5[['[A]', '[B]']] = [2, 8]
dataframe_amostra_6[['[A]', '[B]']] = [0, 10]

# Concatenando os dataframes de amostra
dataframes = [dataframe_amostra_1, dataframe_amostra_2, dataframe_amostra_3, dataframe_amostra_4, dataframe_amostra_5, dataframe_amostra_6]
df = pd.concat(dataframes)

# Ajustando valores de absorção e nm
df[' Abs'] = df[' Abs'].str.replace(',', '.').astype(float)
df['nm'] = df['nm'].str.replace(',', '.').astype(float)

# Fazendo o pivot para colocar comprimentos de onda como colunas
df_pivot = df.pivot(index=['[A]', '[B]'], columns='nm', values=' Abs')

# Resetando o índice para retornar as concentrações de A e B como colunas
df_pivot = df_pivot.reset_index()

# Separando em fatores independentes (preditoras) e dependentes (resposta)
X = df_pivot.drop(columns=['[A]', '[B]']).values  
Y = df_pivot[['[A]', '[B]']].values  


print("440:")
print(df_pivot[440.0])
print("420:")
print(df_pivot[420.0])
print("400:")
print(df_pivot[400.0])


# Salvando X e Y como arquivos .csv
# pd.DataFrame(X).to_csv('X.csv', index=False)
# pd.DataFrame(Y, columns=['[A]', '[B]']).to_csv('Y.csv', index=False)
