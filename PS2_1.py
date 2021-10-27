#!/usr/bin/env python
# coding: utf-8

# In[41]:


# Q1.1

import pandas as pd

# read the earthquake data
eqd = pd.read_csv('earthquakes-2021-10-21_16-20-48_+0800.tsv', sep = '\t')

# compute the total number of deaths
T_deaths = pd.DataFrame(eqd.groupby(['Country']).sum()['Total Deaths'])
print(T_deaths)

# print the top ten countries along with the total number of deaths
print(T_deaths.sort_values('Total Deaths', ascending = False).head(10))

# In[42]:


# Q1.2

# Sort earthquakes with magnitude larger than 6.0
eqd_Mag = eqd[['Year', 'Mag']][eqd['Mag'] >= 6]

# Plot the time series
eqd_Mag.groupby(['Year']).count()['Mag'].plot()


# In[43]:


# Q1.3

# define the function
def CountEq_LargestEq(country, database):
    # extract data of one country
    data_country = database.loc[database['Country'] == country]
    # count the earthquake in this country
    count = data_country['Country'].count()
    # get the date of largest earthquake
    country_max = data_country['Mag'].max()
    date = data_country[['Year', 'Mag']][data_country['Mag'] == country_max]
    return count, date['Year'].values
    
# define ID    
i = 0
# creat a dataframe
header = ['Country', 'Count', 'Date']
ld = pd.DataFrame(columns = ['Country', 'Count', 'Date'])

# apply to all of the reported countries
for s in eqd['Country']:
    ld.loc[str(i)] = [s, CountEq_LargestEq(s, eqd)[0], CountEq_LargestEq(s, eqd)[1]]
    i += 1
    
# delete the duplicates
ld_copy = ld.drop_duplicates(['Country'])  
# report the results in a descending order
ld_order = ld_copy.sort_values("Count", ascending=False)
ld_order.to_excel("Chart 1.xlsx", index=False)

