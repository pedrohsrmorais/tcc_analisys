import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Função para carregar e escalar os dados
def load_and_scale_data(file_X, file_Y):
    X = pd.read_csv(file_X).values
    Y = pd.read_csv(file_Y).values
    
    scaler_X = StandardScaler()
    scaler_Y = StandardScaler()
    
    X_scaled = scaler_X.fit_transform(X)
    Y_scaled = scaler_Y.fit_transform(Y)
    
    return X_scaled, Y_scaled, scaler_X, scaler_Y

# Carregando e padronizando os dados
X_scaled, Y_scaled, scaler_X, scaler_Y = load_and_scale_data('X.csv', 'Y.csv')

# Dividindo os dados em treino e teste com reprodutibilidade
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y_scaled, test_size=0.2, random_state=42)

# Criando e treinando o modelo Random Forest
rf = RandomForestRegressor(n_estimators=8000, random_state=42)
rf.fit(X_train, Y_train)

# Fazendo previsões
Y_pred_scaled = rf.predict(X_test)
Y_pred = scaler_Y.inverse_transform(Y_pred_scaled)

# Comparando com os valores reais
Y_test_real = scaler_Y.inverse_transform(Y_test)

# Função para exibir as métricas
def evaluate_model(Y_true, Y_pred):
    r2 = r2_score(Y_true, Y_pred)
    mse = mean_squared_error(Y_true, Y_pred)
    mae = mean_absolute_error(Y_true, Y_pred)
    
    print(f"R²: {r2}")
    print(f"MSE (Mean Squared Error): {mse}")
    print(f"MAE (Mean Absolute Error): {mae}")

# Avaliação do modelo
evaluate_model(Y_test_real, Y_pred)
