import pandas as pd
import numpy as np

# Lendo os arquivos XLS
dataframe = pd.read_excel('./teste.xlsx', sheet_name='Plan1')

print("DataFrame original:")
print(dataframe)

# Indentificando linhas com 3 valores negativos e excluindo elas
linhas_com_3_negativos = dataframe[dataframe.lt(0).sum(axis=1) == 3]

df_filtrado = dataframe.drop(linhas_com_3_negativos.index)

# Substituindo todos os valores negativos restantes por 0
df_filtrado[df_filtrado < 0] = 0

print("\nDataFrame filtrado (sem linhas com 3 valores negativos e sem negativos):")
print(df_filtrado)

# Função para adicionar ou subtrair uma porcentagem aleatória de 0 a 20%
def alterar_valores(dataframe, porcentagem_max=0.2):
    return dataframe.applymap(lambda x: x * (1 + np.random.uniform(-porcentagem_max, porcentagem_max)))

# Alterando os valores do DataFrame filtrado (não o original)
df_alterado = alterar_valores(df_filtrado)

print("\nDataFrame alterado:")
print(df_alterado)

# Seperando os diferentes espectros
df_amaranto = df_alterado[['onda','Amaranto']]
df_yellow = df_alterado[['Sunset Yellow']]
df_tartrazina = df_alterado[['tartrazina']]






# Verificando a 
#posto = np.linalg.matrix_rank(df_amaranto)
#num_colunas = df_amaranto.shape[1]
#if posto == num_colunas:
#    print("As colunas são linearmente independentes.")
#else:
#    print("As colunas não são linearmente independentes.")


# Salvando X e Y como arquivos .csv
# pd.DataFrame(X).to_csv('X.csv', index=False)
# pd.DataFrame(Y, columns=['[A]', '[B]']).to_csv('Y.csv', index=False)