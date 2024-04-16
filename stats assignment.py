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

years = [str(year) for year in range(1971, 2016)]

# start = 1961
# end = 2016
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







# CO2_data = df_filtered[df_filtered['Indicator Name'] == 'CO2 emissions (kt)']
# years = [str(year) for year in range(1971, 1991)] 
# values = CO2_data.loc[:, '1971':'1991'].values.tolist()  

# # Plotting the indicator names against their values
# plt.figure(figsize=(10, 6))
# for i, country in enumerate(country_names):
#     plt.plot(years, values[i], marker='o', label=country)

# plt.title('CO2 emission by each country')
# plt.xlabel('Year')
# plt.ylabel('CO2 emissions (kt)')
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True)
# plt.tight_layout()

# # Show plot
# plt.show()


# pop_data = df_filtered[df_filtered['Indicator Name'] == 'Population, total']
# years = [str(year) for year in range(2004, 2024)]
# values = pop_data.loc[:, '2004':].values.tolist()

# # Plotting the indicator names against their values
# plt.figure(figsize=(10, 6))
# for i, country in enumerate(country_names):
#     plt.plot(years, values[i], marker='o', label=country)

# plt.title('Total Population of Countries Over Time')
# plt.xlabel('Year')
# plt.ylabel('Population (Billions)')
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True)
# plt.tight_layout()

# # Show plot
# plt.show()

### DRFATTTT







