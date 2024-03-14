import dash_bootstrap_components as dbc
from dash import Dash
from layout import phillips_curve_analysis
from phillips_curve import pc_callbacks
from globalization import glb_callbacks

app = Dash(__name__, suppress_callback_exceptions=True)

server = app.server

app.layout = dbc.Container([phillips_curve_analysis])

if __name__ == '__main__':
    app.run_server(debug = False)