import pandas as pd
import plotly_express as px
import dash_bootstrap_components as dbc
from globalization.glb_data_pre_processing import scaled_df, regression_df

regression_button = dbc.Button(
    "Toggle Inflation Regression Line",
    id="reg_button",
    className="me-2",
    n_clicks=0
        ),


plot_scaled_df = px.line(data_frame = scaled_df, x = scaled_df.index, y = scaled_df.columns)

plot_regression_df = px.line(data_frame = regression_df, x = regression_df.index, y = ['scaled_inflation_rate', 'inflation_prediction'])
