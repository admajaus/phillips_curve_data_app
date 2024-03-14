import dash_bootstrap_components as dbc
from dash import html, dcc
from phillips_curve.pc_ui_components import dropdown_corr_pc, dropdown_corr_bar_pc
from style import card_style, card_header_style, dropdown_style
from globalization.glb_ui_components import regression_button, plot_scaled_df
from globalization.glb_text import summary

phillips_curve_analysis = dbc.Container([
    dbc.Row([
        html.H3("Phillips Curve Analysis")
    ], style = {'marginTop':'30px'}),

    dbc.Row(html.H5('Testing the Strength of the Inverse Relationship Between Inflation and Employment Rates in the U.S')),

    html.Br(),

    dbc.Card([
        dbc.CardHeader(
            'Evaluating the Phillips Curve in the U.S. for Short vs. Long-Term Impact: An Interval-Based Correlation Analysis (1948-2016)',
            style = card_header_style
        ),

        dbc.CardBody([
            dbc.Row([
            html.P('This analysis segments the period of 1948-2016 into intervals of varying lengths to assess the short-term vs. long-term impact of the Phillips curve.'),
            html.P('Please select an interval length (years):')
            ]),

            dbc.Row([
                dbc.Col(dropdown_corr_pc,  style = dropdown_style)
            ]),

            dbc.Row([

                dbc.Col(
                    dbc.Card(
                        id = 'insert_corr_data_table',
                        style = card_style
                    ),
                    width = 6
                ),
                dbc.Col(
                    dbc.Card(
                        dcc.Graph(id = 'pc_corr_histogram'),
                        style = card_style
                    ),
                    width = 6
                )
            ]),
        ])
]),
    dbc.Card([

        dbc.CardHeader(
            "The Diminishing Influence of the Phillips Curve Over Time: An Interval-Based Analysis of Correlation",
            style = card_header_style
        ),

        dbc.CardBody([
            html.P("This chart evaluates the Phillips Curve's robustness across different time segments, examining whether its influence remains consistent throughout the period (1948 -2016) analyzed."),
            html.P('Please select an interval length (years):'),

            dbc.Row([
                dbc.Col(dropdown_corr_bar_pc, style = dropdown_style)
            ]),

            dbc.Row([

                dbc.Col(
                    dbc.Card(
                        dcc.Graph(id='pc_corr_bar'),
                        style = card_style
                    )
                )
            ]),
        ]),
    ]),
    html.Br(),

    dbc.Card([
        dbc.CardHeader('Inflation Dynamics: The Interplay of Globalization and Unemployment', style = card_header_style),
        dbc.CardBody([

            html.P('Click the button below to explore the impact of unemployment and globalization (KOF Globalization Index) on inflation using regression analysis. The data is scaled using z-score normalization.'),

            dbc.Row([dbc.Col(regression_button)]),

            dbc.Row([

                dbc.Col(
                    dcc.Graph(
                    id = 'global_scaled_plot',
                    figure = plot_scaled_df
                    )
                )
            ])
        ])
    ]),
    html.Br(),
    dbc.Card(
        [
            dbc.CardHeader(
                "Economic Trends and Policy Implications: Beyond the Phillips Curve",
                style=card_header_style
            ),
            dbc.CardBody(
                [summary],
            )
        ],
        style={'border': '2px double black', 'height': '675px', 'marginBottom':'30 px'}
    )
])