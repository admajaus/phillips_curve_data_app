from dash import dash_table,Input, Output, callback
import plotly_express as px
from phillips_curve.pc_ui_components import corr_table_dict, corr_df_dict, histo_corr_df_dict

# Renders correlation table and histogram based on period selected from the dropdown
@callback(
    Output('insert_corr_data_table', 'children'),
    Output('pc_corr_histogram', 'figure'),
    Input('pc_corr_dropdown', 'value')
)

def return_table_histogram(period_choice):
    return (corr_table_dict[period_choice],
            px.histogram(data_frame = corr_df_dict[period_choice], y = 'Phillips_Curve_Correlation_Strength')
            )


# Renders correlation bar chart based on period selected from dropdown
@callback(
    Output('pc_corr_bar', 'figure'),
    Input('pc_corr_dropdown_bar', 'value')
)

def return_corr_bar_chart(period_choice):

    return px.bar(
        data_frame = histo_corr_df_dict[period_choice].sort_values(by = 'interval'),
        x = 'interval',
        y='corr_coeff',
        color = 'Phillips_Curve_Correlation_Strength',
        color_discrete_map={'Strong': 'green', 'Weak': 'gray', 'Contradictory': 'red'})