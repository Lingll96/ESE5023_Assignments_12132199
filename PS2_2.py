#!/usr/bin/env python
# coding: utf-8

# In[46]:


# Q2

import pandas as pd

all_data = pd.read_csv('2281305.csv')
Wind_data = all_data[['DATE', 'WND']]
Wind_data


# In[47]:


# Separate the parameters
# direction angle, direction quality code, type code, speed rate, speed quality code
Wind_data['ANGLE'] = Wind_data['WND'].map(lambda x:x.split(',')[0])
Wind_data['DQC'] = Wind_data['WND'].map(lambda x:x.split(',')[1])
Wind_data['TC'] = Wind_data['WND'].map(lambda x:x.split(',')[2])
Wind_data['SR'] = Wind_data['WND'].map(lambda x:x.split(',')[3])
Wind_data['SQC'] = Wind_data['WND'].map(lambda x:x.split(',')[4])
Wind_data = Wind_data.drop(columns = 'WND')

# Get the year, month
Wind_data['Year'] = Wind_data['DATE'].map(lambda x:x.split('-')[0])
Wind_data['Month'] = Wind_data['DATE'].map(lambda x:x.split('-')[1])
Wind_data['YM'] = Wind_data['Year'].astype('str') + '-' + Wind_data['Month'].astype('str') + '-01'

Wind_data


# In[48]:


# Delete the missed data
Wind_data['SR'] = pd.to_numeric(Wind_data['SR'])
Wind_data = Wind_data.drop(Wind_data[Wind_data['SR'] > 900].index)
Wind_data


# In[51]:


# Plot
Wind_data = pd.DataFrame(Wind_data.groupby(['YM']).mean()['SR'])
Wind_data['SR'].plot()

