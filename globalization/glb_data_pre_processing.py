from sklearn.linear_model import LinearRegression
import pandas as pd

scaled_df = pd.read_pickle('clean_dataframes/scaled_global_df.pkl')

# set inflation_rate and KOFGI as the independent variables
X_ur_kofgi = scaled_df[['scaled_unemployment_rate', 'scaled_KOFGI']]
y_inf = scaled_df['scaled_inflation_rate']

# Fit the model for inflation
model_inflation = LinearRegression().fit(X_ur_kofgi, y_inf)

# Create a regression line using the model
inflation_prediction = model_inflation.predict(X_ur_kofgi)

regression_df = scaled_df.copy()
regression_df['inflation_prediction'] = inflation_prediction
