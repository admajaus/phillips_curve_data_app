from dash import Input, Output, callback
import plotly_express as px
from globalization.glb_data_pre_processing import inflation_prediction
from globalization.glb_ui_components import plot_scaled_df, plot_regression_df

@callback(
    Output('global_scaled_plot', "figure"),
    Input("reg_button", "n_clicks")
)
def on_button_click(n):
    if (n is None) | (n % 2 == 0):
        return plot_scaled_df

    else:
        return plot_regression_df



