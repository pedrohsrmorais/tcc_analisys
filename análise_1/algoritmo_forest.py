import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Carregando X e Y de arquivos .csv
X = pd.read_csv('X.csv').values
Y = pd.read_csv('Y.csv').values

# Padronizando os dados (opcional, mas recomendável)
scaler_X = StandardScaler()
X_scaled = scaler_X.fit_transform(X)

scaler_Y = StandardScaler()
Y_scaled = scaler_Y.fit_transform(Y)

# Dividindo os dados em treino e teste
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y_scaled, test_size=0.5)

# Criando e treinando o modelo Random Forest
rf = RandomForestRegressor(n_estimators=2000)
rf.fit(X_train, Y_train)

# Fazendo previsões
Y_pred_scaled = rf.predict(X_test)
Y_pred = scaler_Y.inverse_transform(Y_pred_scaled)

# Comparando com os valores reais
Y_test_real = scaler_Y.inverse_transform(Y_test)

# Cálculo das métricas
r2 = r2_score(Y_test_real, Y_pred)
mse = mean_squared_error(Y_test_real, Y_pred)
mae = mean_absolute_error(Y_test_real, Y_pred)

# Exibindo os resultados
print(f"R²: {r2}")
print(f"MSE (Mean Squared Error): {mse}")
print(f"MAE (Mean Absolute Error): {mae}")
