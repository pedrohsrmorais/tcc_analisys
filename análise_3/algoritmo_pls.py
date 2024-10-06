import pandas as pd
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Carregando X e Y de arquivos .csv
X = pd.read_csv('X.csv').values
Y = pd.read_csv('Y.csv').values

# Dividindo os dados em treino e teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Criando e treinando o modelo PLS
pls = PLSRegression(n_components=2)
pls.fit(X_train, Y_train)

# Fazendo previsões
Y_pred = pls.predict(X_test)

# Cálculo das métricas
r2 = r2_score(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
mae = mean_absolute_error(Y_test, Y_pred)

# Exibindo os resultados
print(f"R²: {r2}")
print(f"MSE (Mean Squared Error): {mse}")
print(f"MAE (Mean Absolute Error): {mae}")
