import pandas as pd
import matplotlib.pyplot as plt

def read_worldbank_data(filename):
    
    """ Read the data file and transpose it """
    
    # Read the CSV file
    df = pd.read_csv(filename, skiprows=4)
    df = df.fillna(0)
    print(df)
    
    # Transpose the CSV file
    df_transpose = df.T
    print(df_transpose)
    
    
filename = 'stats2.csv'
read_worldbank_data(filename)

df = pd.read_csv(filename, skiprows=4)
df = df.fillna(0)

described_df = df.describe()
print(described_df)

indicator_names = ['Population, total',
                   'Agricultural land (sq. km)',
                   'CO2 emissions from liquid fuel consumption (kt)',
                   'Energy use (kg of oil equivalent per capita)']

country_names = ['Japan',
                 'Argentina',
                 'India',
                 'Ethiopia']

df_filtered = df[df['Country Name'].isin(country_names) & df['Indicator Name'].isin(indicator_names)]
print(df_filtered)

high = df_filtered[df_filtered['Country Name'] == 'Japan']
print(high)
upper_mid = df_filtered[df_filtered['Country Name'] == 'Argentina']
print(upper_mid)
lower_mid = df_filtered[df_filtered['Country Name'] == 'India']
print(lower_mid)
low = df_filtered[df_filtered['Country Name'] == 'Ethiopia']
print(low)


#%%
high_ma = high.rolling(window=5, axis=1).mean()
print(high_ma)
upper_mid_ma = upper_mid.rolling(window=5, axis=1).mean()
print(upper_mid_ma)
lower_mid_ma = lower_mid.rolling(window=5, axis=1).mean()
print(lower_mid_ma)
low_ma = low.rolling(window=5, axis=1).mean()
print(low_ma)

# Transpose the rolling averages
high_ma_T = high_ma.rename_axis('Year').T
rename_dict = {col: indicator_names[i] for i, col in enumerate(high_ma_T.columns)}
high_ma_T = high_ma_T.rename(columns=rename_dict)
print(high_ma_T)

upper_mid_ma_T = upper_mid_ma.rename_axis('Year').T
rename_dict = {col: indicator_names[i] for i, col in enumerate(upper_mid_ma_T.columns)}
upper_mid_ma_T = upper_mid_ma_T.rename(columns=rename_dict)
print(upper_mid_ma_T)

lower_mid_ma_T = lower_mid_ma.rename_axis('Year').T
rename_dict = {col: indicator_names[i] for i, col in enumerate(lower_mid_ma_T.columns)}
lower_mid_ma_T = lower_mid_ma_T.rename(columns=rename_dict)
print(lower_mid_ma_T)

low_ma_T = low_ma.rename_axis('Year').T
rename_dict = {col: indicator_names[i] for i, col in enumerate(low_ma_T.columns)}
low_ma_T = low_ma_T.rename(columns=rename_dict)
print(low_ma_T)
#%%
### 
start_year = 1971
end_year = 2016

# Print the most recent 20 years and the 20 years at the start for each dataframe
print(f"Data for the most recent 20 years ({end_year-19} to {end_year}):")
high_ma_T_end = high_ma_T.loc[str(end_year-20):str(end_year)]
print(high_ma_T_end)
print("\nData for the 20 years at the start of the data series:")
high_ma_T_start = high_ma_T.loc[str(start_year):str(start_year+20)]
print(high_ma_T_start)
print("\n")

print(f"Data for the most recent 20 years ({end_year-19} to {end_year}):")
upper_mid_ma_T_end = upper_mid_ma_T.loc[str(end_year-20):str(end_year)]
print(upper_mid_ma_T_end)
print("\nData for the 20 years at the start of the data series:")
upper_mid_ma_T_start = upper_mid_ma_T.loc[str(start_year):str(start_year+20)]
print(upper_mid_ma_T_start)
print("\n")

print(f"Data for the most recent 20 years ({end_year-19} to {end_year}):")
lower_mid_ma_T_end = lower_mid_ma_T.loc[str(end_year-20):str(end_year)]
print(lower_mid_ma_T_end)
print("\nData for the 20 years at the start of the data series:")
lower_mid_ma_T_start = lower_mid_ma_T.loc[str(start_year):str(start_year+20)]
print(lower_mid_ma_T_start)
print("\n")

print(f"Data for the most recent 20 years ({end_year-19} to {end_year}):")
low_ma_T_end = low_ma_T.loc[str(end_year-20):str(end_year)]
print(low_ma_T_end)
print("\nData for the 20 years at the start of the data series:")
low_ma_T_start = low_ma_T.loc[str(start_year):str(start_year+20)]
print(low_ma_T_start)

#%%
### POPULATION COMPARISON 
# Population in earliest 20 years of Dataseries (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_start['Population, total'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_start['Population, total'], label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_start['Population, total'], label='India (lower middle income)')
plt.plot(low_ma_T_start['Population, total'], label='Ethiopia (low income)')
plt.title('Total Population of Countries from 1971 to 1991')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.xticks(rotation=45)
plt.legend(frameon=False)
plt.grid(True)
plt.tight_layout()
# Show plot
plt.show()

# Population in recent 20 years of Dataseries (1996 to 2016)
plt.figure()
plt.plot(high_ma_T_end['Population, total'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_end['Population, total'], label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_end['Population, total'], label='India (lower middle income)')
plt.plot(low_ma_T_end['Population, total'], label='Ethiopia (low income)')
plt.title('Total Population of Countries from 1996 to 2016')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.xticks(rotation=45)
plt.legend(frameon=False)
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()

#%%
### AGRICULTURAL LAND COMPARISON
# Agricultural land in earliest 20 years (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_start['Agricultural land (sq. km)'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_start['Agricultural land (sq. km)'], label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_start['Agricultural land (sq. km)'], label='India (lower middle income)')
plt.plot(low_ma_T_start['Agricultural land (sq. km)'], label='Ethiopia (low income)')
plt.title('Agricultural land of Countries from 1971 to 1991')
plt.xlabel('Year')
plt.ylabel('Agricultural land (sq. km)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
# Show plot
plt.show()

# Agricultural land in recent 20 years (1996 to 2016)
plt.figure()
plt.plot(high_ma_T_end['Agricultural land (sq. km)'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_end['Agricultural land (sq. km)'], label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_end['Agricultural land (sq. km)'], label='India (lower middle income)')
plt.plot(low_ma_T_end['Agricultural land (sq. km)'], label='Ethiopia (low income)')
plt.title('Agricultural land of Countries from 1996 to 2016')
plt.xlabel('Year')
plt.ylabel('Agricultural land (sq. km)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
# Show plot
plt.show()

#%%
### CO2 EMISSION FROM LIQUID FUEL COMPARISON
# CO2 emission in earliest 20 years of Dataseries (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_start['CO2 emissions from liquid fuel consumption (kt)'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_start['CO2 emissions from liquid fuel consumption (kt)'], label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_start['CO2 emissions from liquid fuel consumption (kt)'], label='India (lower middle income)')
plt.plot(low_ma_T_start['CO2 emissions from liquid fuel consumption (kt)'], label='Ethiopia (low income)')
plt.title('Agricultural land of Countries from 1971 to 1991')
plt.xlabel('Year')
plt.ylabel('CO2 emission (kt)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
# Show plot
plt.show()

# CO2 emission in recent 20 years of Dataseries (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_end['CO2 emissions from liquid fuel consumption (kt)'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_end['CO2 emissions from liquid fuel consumption (kt)'], label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_end['CO2 emissions from liquid fuel consumption (kt)'], label='India (lower middle income)')
plt.plot(low_ma_T_end['CO2 emissions from liquid fuel consumption (kt)'], label='Ethiopia (low income)')
plt.title('CO2 Emission from liquid fuel of Countries from 1996 to 2016')
plt.xlabel('Year')
plt.ylabel('CO2 emission (kt)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
# Show plot
plt.show()

#%%
### ENERGY USE FROM OIL COMPARISON
# Energy use in earliest 20 years of Dataseries (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_start['Energy use (kg of oil equivalent per capita)'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_start['Energy use (kg of oil equivalent per capita)'], label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_start['Energy use (kg of oil equivalent per capita)'], label='India (lower middle income)')
plt.plot(low_ma_T_start['Energy use (kg of oil equivalent per capita)'], label='Ethiopia (low income)')
plt.title('Energy use (oil in kg) of Countries from 1971 to 1991')
plt.xlabel('Year')
plt.ylabel('Energy use (kg of oil equivalent per capita)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
# Show plot
plt.show()

# Energy use in recent 20 years of Dataseries (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_end['Energy use (kg of oil equivalent per capita)'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_end['Energy use (kg of oil equivalent per capita)'], label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_end['Energy use (kg of oil equivalent per capita)'], label='India (lower middle income)')
plt.plot(low_ma_T_end['Energy use (kg of oil equivalent per capita)'], label='Ethiopia (low income)')
plt.title('Energy use (oil in kg) of Countries from 1996 to 2016')
plt.xlabel('Year')
plt.ylabel('Energy use (kg of oil equivalent per capita)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
# Show plot
plt.show()


























