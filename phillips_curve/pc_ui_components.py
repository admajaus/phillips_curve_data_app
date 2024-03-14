from dash import dash_table
from dash import dcc
from pc_data_pre_processing import corr_df_dict, interval_periods
from style import table_header_style, cell_style

# Create a dropdown to allow user to select period
dropdown_corr_pc = dcc.Dropdown(
    id ='pc_corr_dropdown',
    value = interval_periods[0],
    options = interval_periods
)

# Create data_tables for each set of intervals
corr_table_dict = {}

for period, corr_df in corr_df_dict.items():
    corr_df_copy = corr_df.copy()
    corr_df_copy['interval'] = corr_df_copy['interval'].apply(
        lambda x: f"{x.left.strftime('%Y')} to {x.right.strftime('%Y')}")

    corr_table = dash_table.DataTable(
        corr_df_copy.to_dict('records'),
        style_table = {'overflowX': 'auto', 'overflowY': 'scroll', 'maxHeight' : '450px'},
        style_cell = cell_style,
        style_header = table_header_style

    )

    corr_table_dict[period] = corr_table

# Create a dropdown to allow user to select period for the corr coef bar chart
dropdown_corr_bar_pc = dcc.Dropdown(
    id ='pc_corr_dropdown_bar',
    value = interval_periods[0],
    options = interval_periods
)

histo_corr_df_dict = {}
for period, corr_df in corr_df_dict.items():
    corr_df_copy2 = corr_df.copy()
    copy3 = corr_df_copy2.copy()
    copy3['interval'] = copy3['interval'].apply(lambda x: x.left.strftime('%Y-%m-%d'))
    histo_corr_df_dict[period] = copy3


##Test
#print(corr_table_dict[5])
# print(histo_corr_df_dict)