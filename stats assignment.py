import pandas as pd
import matplotlib.pyplot as plt


def read_worldbank_data(filename):
    
    """ Read the data file and transpose it """
    
    # Read the CSV file
    df_ = pd.read_csv(filename, skiprows=4)
    df_ = df_.fillna(0)
    print(df_)
    
    # Transpose the CSV file
    df_transpose = df.T
    print(df_transpose)
    
    
filename = 'stats2.csv'
read_worldbank_data(filename)

df = pd.read_csv(filename, skiprows=4)
df = df.fillna(0)

income = pd.read_csv('income.csv')

#%%
# Merge the income group and indicator data sets
merged_df = pd.merge(df, income, on='Country Name', how='left') 
print(merged_df)

# Describe the dataframe
described_df = df.describe()
print(described_df)

#%%
# Identify the indicators
indicator_names = ['Population, total',
                   'Agricultural land (sq. km)',
                   'CO2 emissions from liquid fuel consumption (kt)',
                   'Energy use (kg of oil equivalent per capita)']

# Identify the countries for each income group
country_names = ['Japan',
                 'Argentina',
                 'India',
                 'Ethiopia']

# Create the filtered dataframe 
df_filtered = df[df['Country Name'].isin(country_names) &
                 df['Indicator Name'].isin(indicator_names)]
print(df_filtered)

#%%
# Seperate the countries by income 
high = df_filtered[df_filtered['Country Name'] == 'Japan']
print('Japan Data:')
print(high)
upper_mid = df_filtered[df_filtered['Country Name'] == 'Argentina']
print('Argentina Data:')
print(upper_mid)
lower_mid = df_filtered[df_filtered['Country Name'] == 'India']
print('India Data:')
print(lower_mid)
low = df_filtered[df_filtered['Country Name'] == 'Ethiopia']
print('Ethiopia Data:')
print(low)

#%%
# Generate the rolling averages
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
rename_dict = {col: indicator_names[i] for i,
               col in enumerate(high_ma_T.columns)}
high_ma_T = high_ma_T.rename(columns=rename_dict)
print(high_ma_T)

upper_mid_ma_T = upper_mid_ma.rename_axis('Year').T
rename_dict = {col: indicator_names[i] for i,
               col in enumerate(upper_mid_ma_T.columns)}
upper_mid_ma_T = upper_mid_ma_T.rename(columns=rename_dict)
print(upper_mid_ma_T)

lower_mid_ma_T = lower_mid_ma.rename_axis('Year').T
rename_dict = {col: indicator_names[i] for i,
               col in enumerate(lower_mid_ma_T.columns)}
lower_mid_ma_T = lower_mid_ma_T.rename(columns=rename_dict)
print(lower_mid_ma_T)

low_ma_T = low_ma.rename_axis('Year').T
rename_dict = {col: indicator_names[i] for i,
               col in enumerate(low_ma_T.columns)}
low_ma_T = low_ma_T.rename(columns=rename_dict)
print(low_ma_T)
#%%
# Specify the start and end years 
start_year = 1971
end_year = 2016

# Print the most recent 20 years and 20 years at the start for each dataframe
# High income
print(f"Data for the most recent 20 years ({end_year-19} to {end_year}):")
high_ma_T_end = high_ma_T.loc[str(end_year-20):str(end_year)]
print(high_ma_T_end)
print("\nData for the 20 years at the start of the data series:")
high_ma_T_start = high_ma_T.loc[str(start_year):str(start_year+20)]
print(high_ma_T_start)
print("\n")

# Upper middle income 
print(f"Data for the most recent 20 years ({end_year-19} to {end_year}):")
upper_mid_ma_T_end = upper_mid_ma_T.loc[str(end_year-20):str(end_year)]
print(upper_mid_ma_T_end)
print("\nData for the 20 years at the start of the data series:")
upper_mid_ma_T_start = upper_mid_ma_T.loc[str(start_year):str(start_year+20)]
print(upper_mid_ma_T_start)
print("\n")

# Lower middle income
print(f"Data for the most recent 20 years ({end_year-19} to {end_year}):")
lower_mid_ma_T_end = lower_mid_ma_T.loc[str(end_year-20):str(end_year)]
print(lower_mid_ma_T_end)
print("\nData for the 20 years at the start of the data series:")
lower_mid_ma_T_start = lower_mid_ma_T.loc[str(start_year):str(start_year+20)]
print(lower_mid_ma_T_start)
print("\n")

# Low income 
print(f"Data for the most recent 20 years ({end_year-19} to {end_year}):")
low_ma_T_end = low_ma_T.loc[str(end_year-20):str(end_year)]
print(low_ma_T_end)
print("\nData for the 20 years at the start of the data series:")
low_ma_T_start = low_ma_T.loc[str(start_year):str(start_year+20)]
print(low_ma_T_start)
#%%
# Summing up the 'Energy use' column for each income group

# High income
high_ma_T_end_sum = high_ma_T_end['Energy use (kg of oil equivalent per capita)'].sum()
print(f"Sum of energy use in high income countries for the most recent 20 years: {high_ma_T_end_sum}")

high_ma_T_start_sum = high_ma_T_start['Energy use (kg of oil equivalent per capita)'].sum()
print(f"Sum of energy use in high income countries for the 20 years at the start of the data series: {high_ma_T_start_sum}")

# Upper middle income
upper_mid_ma_T_end_sum = upper_mid_ma_T_end['Energy use (kg of oil equivalent per capita)'].sum()
print(f"Sum of energy use in upper middle income countries for the most recent 20 years: {upper_mid_ma_T_end_sum}")

upper_mid_ma_T_start_sum = upper_mid_ma_T_start['Energy use (kg of oil equivalent per capita)'].sum()
print(f"Sum of energy use in upper middle income countries for the 20 years at the start of the data series: {upper_mid_ma_T_start_sum}")

# Lower middle income
lower_mid_ma_T_end_sum = lower_mid_ma_T_end['Energy use (kg of oil equivalent per capita)'].sum()
print(f"Sum of energy use in lower middle income countries for the most recent 20 years: {lower_mid_ma_T_end_sum}")

lower_mid_ma_T_start_sum = lower_mid_ma_T_start['Energy use (kg of oil equivalent per capita)'].sum()
print(f"Sum of energy use in lower middle income countries for the 20 years at the start of the data series: {lower_mid_ma_T_start_sum}")

# Low income
low_ma_T_end_sum = low_ma_T_end['Energy use (kg of oil equivalent per capita)'].sum()
print(f"Sum of energy use in low income countries for the most recent 20 years: {low_ma_T_end_sum}")

low_ma_T_start_sum = low_ma_T_start['Energy use (kg of oil equivalent per capita)'].sum()
print(f"Sum of energy use in low income countries for the 20 years at the start of the data series: {low_ma_T_start_sum}")

#%%
### POPULATION COMPARISON 
# Population in earliest 20 years of Dataseries (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_start['Population, total'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_start['Population, total'],
         label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_start['Population, total'],
         label='India (lower middle income)')
plt.plot(low_ma_T_start['Population, total'], label='Ethiopia (low income)')
plt.title('Total Population of Countries from 1971 to 1991')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.xticks(rotation=45)
plt.legend(frameon=False)
plt.grid(True)
plt.tight_layout()
plt.savefig('pop_start.png')
# Show plot
plt.show()

# Population in recent 20 years of Dataseries (1996 to 2016)
plt.figure()
plt.plot(high_ma_T_end['Population, total'], label='Japan (high income)')
plt.plot(upper_mid_ma_T_end['Population, total'],
         label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_end['Population, total'],
         label='India (lower middle income)')
plt.plot(low_ma_T_end['Population, total'], label='Ethiopia (low income)')
plt.title('Total Population of Countries from 1996 to 2016')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.xticks(rotation=45)
plt.legend(frameon=False)
plt.grid(True)
plt.tight_layout()
plt.savefig('pop_end.png')
# Show plot
plt.show()

#%%
### AGRICULTURAL LAND COMPARISON
# Agricultural land in earliest 20 years (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_start['Agricultural land (sq. km)'],
         label='Japan (high income)')
plt.plot(upper_mid_ma_T_start['Agricultural land (sq. km)'],
         label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_start['Agricultural land (sq. km)'],
         label='India (lower middle income)')
plt.plot(low_ma_T_start['Agricultural land (sq. km)'],
         label='Ethiopia (low income)')
plt.title('Agricultural land of Countries from 1971 to 1991')
plt.xlabel('Year')
plt.ylabel('Agricultural land (sq. km)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
plt.savefig('agriculture_start.png')
# Show plot
plt.show()

# Agricultural land in recent 20 years (1996 to 2016)
plt.figure()
plt.plot(high_ma_T_end['Agricultural land (sq. km)'],
         label='Japan (high income)')
plt.plot(upper_mid_ma_T_end['Agricultural land (sq. km)'],
         label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_end['Agricultural land (sq. km)'],
         label='India (lower middle income)')
plt.plot(low_ma_T_end['Agricultural land (sq. km)'],
         label='Ethiopia (low income)')
plt.title('Agricultural land of Countries from 1996 to 2016')
plt.xlabel('Year')
plt.ylabel('Agricultural land (sq. km)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
plt.savefig('agriculture_end.png')
# Show plot
plt.show()

#%%
### CO2 EMISSION FROM LIQUID FUEL COMPARISON
# CO2 emission in earliest 20 years of Dataseries (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_start['CO2 emissions from liquid fuel consumption (kt)'],
         label='Japan (high income)')
plt.plot(upper_mid_ma_T_start
         ['CO2 emissions from liquid fuel consumption (kt)'],
         label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_start
         ['CO2 emissions from liquid fuel consumption (kt)'],
         label='India (lower middle income)')
plt.plot(low_ma_T_start['CO2 emissions from liquid fuel consumption (kt)'],
         label='Ethiopia (low income)')
plt.title('CO2 Emission from liquid fuel of Countries from 1971 to 1991')
plt.xlabel('Year')
plt.ylabel('CO2 emission (kt)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
plt.savefig('CO2_start.png')
# Show plot
plt.show()

# CO2 emission in recent 20 years of Dataseries (1971 to 1991)
plt.figure()
plt.plot(high_ma_T_end['CO2 emissions from liquid fuel consumption (kt)'],
         label='Japan (high income)')
plt.plot(upper_mid_ma_T_end['CO2 emissions from liquid fuel consumption (kt)'],
         label='Argentina (upper middle income)')
plt.plot(lower_mid_ma_T_end['CO2 emissions from liquid fuel consumption (kt)'],
         label='India (lower middle income)')
plt.plot(low_ma_T_end['CO2 emissions from liquid fuel consumption (kt)'],
         label='Ethiopia (low income)')
plt.title('CO2 Emission from liquid fuel of Countries from 1996 to 2016')
plt.xlabel('Year')
plt.ylabel('CO2 emission (kt)')
plt.xticks(rotation=45)
plt.legend(fontsize='small', loc='upper right', frameon=False)
plt.grid(True)
plt.tight_layout()
plt.savefig('CO2_end.png')
# Show plot
plt.show()

#%%
### TOTAL ENERGY USE FROM OIL COMPARISON 
# Name the countries and there energy use from the start and end of data
countries = ['Japan (high income)', 'Argentina (upper mid income)', 'India (lower mid income)', 'Ethiopia (low income)']
energy_use_recent = [1084238.0, 26743294.0, 37861982.0, 6991184.0]
energy_use_start = [1306618.0, 26764322.0, 37800146.0, 12305754.0]

# Create bar chart
plt.figure(figsize=(8, 6))
bar_width = 0.35
index = range(len(countries))

plt.bar(countries, energy_use_recent, label='Most Recent 20 Years', color = 'lime')
plt.bar(countries, energy_use_start, label='20 Years at Start', color = 'navy', alpha = 0.5)

plt.xlabel('Country', fontsize=16)
plt.ylabel('Energy Use (kg of oil equivalent per capita)', fontsize=14)
plt.title('Total Energy Use from Oil by Country in 20 years', fontsize=18)
plt.xticks(rotation=20, fontsize=14)
plt.yticks(fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot as image
plt.savefig('energy_comparison.png')

# Show plot
plt.show()

#%%
### CORRELATION BETWEEN CO2 EMISSIONS AND POPULATION

def calculate_correlations(start_df, end_df):
    # Calculate correlations between CO2 emissions and Population for different income groups
    corr_start_pop = start_df['CO2 emissions from liquid fuel consumption (kt)'].corr(start_df['Population, total'])
    corr_end_pop = end_df['CO2 emissions from liquid fuel consumption (kt)'].corr(end_df['Population, total'])
    
    return corr_start_pop, corr_end_pop

# Calculate correlations for high income countries
corr_start_rich_pop, corr_end_rich_pop = calculate_correlations(high_ma_T_start, high_ma_T_end)
print("Correlation in high income country at start of data:", corr_start_rich_pop)
print("Correlation in high income country at end of data:", corr_end_rich_pop)

# Calculate correlations for upper middle income countries
corr_start_upper_pop, corr_end_upper_pop = calculate_correlations(upper_mid_ma_T_start, upper_mid_ma_T_end)
print("Correlation in upper middle income country at start of data:", corr_start_upper_pop)
print("Correlation in upper middle income country at end of data:", corr_end_upper_pop)

# Calculate correlations for lower middle income countries
corr_start_lower_pop, corr_end_lower_pop = calculate_correlations(lower_mid_ma_T_start, lower_mid_ma_T_end)
print("Correlation in lower middle income country at start of data:", corr_start_lower_pop)
print("Correlation in lower middle income country at end of data:", corr_end_lower_pop)

# Calculate correlations for low income countries
corr_start_low_pop, corr_end_low_pop = calculate_correlations(low_ma_T_start, low_ma_T_end)
print("Correlation in low income country at start of data:", corr_start_low_pop)
print("Correlation in low income country at end of data:", corr_end_low_pop)


#%% 
### CORRELATION BETWEEN CO2 EMISSIONS AND AGRICULTURAL LAND

def calculate_correlations_agricultural(start_df, end_df):
    # Calculate correlations between CO2 emissions and Agricultural land for different income groups
    corr_start_ag = start_df['CO2 emissions from liquid fuel consumption (kt)'].corr(start_df['Agricultural land (sq. km)'])
    corr_end_ag = end_df['CO2 emissions from liquid fuel consumption (kt)'].corr(end_df['Agricultural land (sq. km)'])
    
    return corr_start_ag, corr_end_ag

# Calculate correlations for high income countries
corr_start_rich_ag, corr_end_rich_ag = calculate_correlations_agricultural(high_ma_T_start, high_ma_T_end)
print("Correlation in high income country at start of data:", corr_start_rich_ag)
print("Correlation in high income country at end of data:", corr_end_rich_ag)

# Calculate correlations for upper middle income countries
corr_start_upper_ag, corr_end_upper_ag = calculate_correlations_agricultural(upper_mid_ma_T_start, upper_mid_ma_T_end)
print("Correlation in upper middle income country at start of data:", corr_start_upper_ag)
print("Correlation in upper middle income country at end of data:", corr_end_upper_ag)

# Calculate correlations for lower middle income countries
corr_start_lower_ag, corr_end_lower_ag = calculate_correlations_agricultural(lower_mid_ma_T_start, lower_mid_ma_T_end)
print("Correlation in lower middle income country at start of data:", corr_start_lower_ag)
print("Correlation in lower middle income country at end of data:", corr_end_lower_ag)

# Calculate correlations for low income countries
corr_start_low_ag, corr_end_low_ag = calculate_correlations_agricultural(low_ma_T_start, low_ma_T_end)
print("Correlation in low income country at start of data:", corr_start_low_ag)
print("Correlation in low income country at end of data:", corr_end_low_ag)

#%% 
### CORRELATION BETWEEN CO2 EMISSIONS AND ENERGY USE

def calculate_correlations_energy(start_df, end_df):
    # Calculate correlations between CO2 emissions and Energy use for different income groups
    corr_start_en = start_df['CO2 emissions from liquid fuel consumption (kt)'].corr(start_df['Energy use (kg of oil equivalent per capita)'])
    corr_end_en = end_df['CO2 emissions from liquid fuel consumption (kt)'].corr(end_df['Energy use (kg of oil equivalent per capita)'])
    
    return corr_start_en, corr_end_en

# Calculate correlations for high income countries
corr_start_rich_en, corr_end_rich_en = calculate_correlations_energy(high_ma_T_start, high_ma_T_end)
print("Correlation in high income country at start of data:", corr_start_rich_en)
print("Correlation in high income country at end of data:", corr_end_rich_en)

# Calculate correlations for upper middle income countries
corr_start_upper_en, corr_end_upper_en = calculate_correlations_energy(upper_mid_ma_T_start, upper_mid_ma_T_end)
print("Correlation in upper middle income country at start of data:", corr_start_upper_en)
print("Correlation in upper middle income country at end of data:", corr_end_upper_en)

# Calculate correlations for lower middle income countries
corr_start_lower_en, corr_end_lower_en = calculate_correlations_energy(lower_mid_ma_T_start, lower_mid_ma_T_end)
print("Correlation in lower middle income country at start of data:", corr_start_lower_en)
print("Correlation in lower middle income country at end of data:", corr_end_lower_en)

# Calculate correlations for low income countries
corr_start_low_en, corr_end_low_en = calculate_correlations_energy(low_ma_T_start, low_ma_T_end)
print("Correlation in low income country at start of data:", corr_start_low_en)
print("Correlation in low income country at end of data:", corr_end_low_en)

#%%
### SCATTER PLOT FOR CO2 EMISSION AND TOTAL POPULATION
# Create a scatter plot for correlations at the start of data
plt.figure(figsize=(10, 6))
plt.scatter(['Japan(High Income)', 'Argentina(Upper Mid Income)', 'India(Lower Mid Income)', 'Ethiopia(Low Income)'], 
            [corr_start_rich_pop, corr_start_upper_pop, corr_start_lower_pop, corr_start_low_pop], 
            color='blue', label='Start of Data')
plt.xlabel('Income Group', fontsize=16)
plt.ylabel('Correlation Coefficient', fontsize=16)
plt.xticks(fontsize=14, rotation=10)
plt.yticks(fontsize=14)
plt.title('Correlation between CO2 Emissions and Population at Start of Data', fontsize=16)
plt.ylim(-1, 1)
plt.axhline(y=0, color='gray', linestyle='--') 
plt.legend()
plt.savefig('pop_corr_start.png')
plt.show()

# Create a scatter plot for correlations at the end of data
plt.figure(figsize=(10, 6))
plt.scatter(['Japan(High Income)', 'Argentina(Upper Mid Income)', 'India(Lower Mid Income)', 'Ethiopia(Low Income)'], 
            [corr_end_rich_pop, corr_end_upper_pop, corr_end_lower_pop, corr_end_low_pop], 
            color='green', label='End of Data')
plt.xlabel('Income Group', fontsize=16)
plt.ylabel('Correlation Coefficient', fontsize=16)
plt.xticks(fontsize=14, rotation=10)
plt.yticks(fontsize=14)
plt.title('Correlation between CO2 Emissions and Population at End of Data', fontsize=16)
plt.ylim(-1, 1)
plt.axhline(y=0, color='gray', linestyle='--')
plt.legend()
plt.savefig('pop_corr_end.png')

plt.show()
#%%
### SCATTER PLOT FOR CO2 EMISSION AND AGRICULTURAL LAND
# Create a scatter plot for correlations at the start of data
plt.figure(figsize=(10, 6))
plt.scatter(['Japan(High Income)', 'Argentina(Upper Mid Income)', 'India(Lower Mid Income)', 'Ethiopia(Low Income)'], 
            [corr_start_rich_ag, corr_start_upper_ag, corr_start_lower_ag, corr_start_low_ag], 
            color='blue', label='Start of Data')
plt.xlabel('Income Group', fontsize=16)
plt.ylabel('Correlation Coefficient', fontsize=16)
plt.xticks(fontsize=14, rotation=10)
plt.yticks(fontsize=14)
plt.title('Correlation between CO2 Emissions and Agricultural Land at Start of Data', fontsize=16)
plt.ylim(-1, 1) 
plt.axhline(y=0, color='gray', linestyle='--')
plt.legend()
plt.savefig('ag_corr_start.png')
plt.show()

# Create a scatter plot for correlations at the end of data
plt.figure(figsize=(10, 6))
plt.scatter(['Japan(High Income)', 'Argentina(Upper Mid Income)', 'India(Lower Mid Income)', 'Ethiopia(Low Income)'], 
            [corr_end_rich_ag, corr_end_upper_ag, corr_end_lower_ag, corr_end_low_ag], 
            color='green', label='End of Data')
plt.xlabel('Income Group', fontsize=16)
plt.ylabel('Correlation Coefficient', fontsize=16)
plt.xticks(fontsize=14, rotation=10)
plt.yticks(fontsize=14)
plt.title('Correlation between CO2 Emissions and Agricultural Land at End of Data', fontsize=16)
plt.ylim(-1, 1) 
plt.axhline(y=0, color='gray', linestyle='--')
plt.legend()
plt.savefig('ag_corr_end.png')
plt.show()
#%%
### SCATTER PLOT FOR CO2 EMISSION AND ENERGY USE 
# Create a scatter plot for correlations at the start of data
plt.figure(figsize=(10, 6))
plt.scatter(['Japan(High Income)', 'Argentina(Upper Mid Income)', 'India(Lower Mid Income)', 'Ethiopia(Low Income)'],  
            [corr_start_rich_en, corr_start_upper_en, corr_start_lower_en, corr_start_low_en], 
            color='blue', label='Start of Data')
plt.xlabel('Income Group', fontsize=16)
plt.ylabel('Correlation Coefficient', fontsize=16)
plt.xticks(fontsize=14, rotation=10)
plt.yticks(fontsize=14)
plt.title('Correlation between CO2 Emissions and Energy Use at Start of Data'
          , fontsize=16)
plt.ylim(-1, 1)
plt.axhline(y=0, color='gray', linestyle='--') 
plt.legend()
plt.savefig('en_corr_start.png')
plt.show()

# Create a scatter plot for correlations at the end of data
plt.figure(figsize=(10, 6))
plt.scatter(['Japan(High Income)', 'Argentina(Upper Mid Income)', 'India(Lower Mid Income)', 'Ethiopia(Low Income)'], 
            [corr_end_rich_en, corr_end_upper_en, corr_end_lower_en, corr_end_low_en], 
            color='green', label='End of Data')
plt.xlabel('Income Group', fontsize=16)
plt.ylabel('Correlation Coefficient', fontsize=16)
plt.xticks(fontsize=14, rotation=10)
plt.yticks(fontsize=14)
plt.title('Correlation between CO2 Emissions and Energy Use at End of Data'
          , fontsize=16)
plt.ylim(-1, 1)  
plt.axhline(y=0, color='gray', linestyle='--')  
plt.legend()
plt.savefig('en_corr_end.png')
plt.show()













