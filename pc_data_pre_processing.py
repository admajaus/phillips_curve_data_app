import pandas as pd
import numpy as np

# CONVERT CSV TO DATAFRAME-------------------------------
resample = pd.DataFrame(
    pd.read_pickle('clean_dataframes/resample.pkl')
)

# define options for interval length
interval_periods = [4,8,12,16]

# create data-time intervals for each period in interval_periods

interval_df_dict = {}
bin_dict = {}

for period in interval_periods:

    # establish starting and ending bin edges
    start_year = resample.index.year.min()
    end_year = resample.index.year.max()

    # create bins from start year to end year, with bin length equaling the period defined in interval_periods
    dt_bins = pd.date_range(start=f'{start_year}', end=f'{end_year + period}', freq=f'{period}YS')

    # copy resample dataframe to reset resample from alteration in binning below
    resample_copy = resample.copy()

    # Bin the data into intervals defined in dt_bins; do not include right bin edge in interval
    resample_copy['dt_interval'] = pd.cut(resample_copy.index, bins=dt_bins, right=False)

    # Save this binned dataframe into a dict as the value and the period as the key
    interval_df_dict[period] = resample_copy

    # Save the bins for each period into a dictionary
    bin_dict[period] = dt_bins

corr_dict = {}
corr_df_dict = {}

corr_bins = [-1.0, -0.30, 0, 1]
corr_bin_labels = ['Strong', 'Weak', 'Contradictory']


for period, df in interval_df_dict.items():
    bins = df['dt_interval'].unique()

    for bin in bins:
        corr = df[df['dt_interval'] == bin][['inflation_rate', 'unemployment_rate']].corr().iloc[0,1]

        corr_dict[bin] = round(corr,2)

    correlation = pd.DataFrame(data=corr_dict.items(), index=range(len(corr_dict)), columns=['interval', 'corr_coeff'])

    correlation['Phillips_Curve_Correlation_Strength'] = pd.cut(
        x=correlation['corr_coeff'],
        bins=corr_bins,
        labels=corr_bin_labels,
        right=False)

    # adjust the data type of PCCS from categorical to string, otherwise if a categorey is absent from a subset, the bar chart won't work
    correlation['Phillips_Curve_Correlation_Strength'] = correlation['Phillips_Curve_Correlation_Strength'].astype(
        'str').replace('nan', np.nan)

    corr_df_dict[period] = correlation
    corr_dict = {}

# # Tests
# print(corr_df_dict[10])

