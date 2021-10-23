#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Q3.1

import pandas as pd

# read
rice_export_raw_data = pd.read_csv('Rice_China_export_Quantity.csv')
rice_ex_data = rice_export_raw_data[['Year', 'Partner Countries', 'Value', 'Unit']]

rice_ex_data = rice_ex_data.dropna()
rice_ex_data


# In[37]:


# Q3.2

# Time series of the annual exportation
rice_ex_data.groupby(['Year']).sum()['Value'].plot()


# In[38]:


# Q3.3

# 1. The ten countries with the largest export volumes
pd.DataFrame(rice_ex_data.groupby(['Partner Countries']).sum()['Value']).sort_values('Value', ascending = False).head(10)


# In[39]:


# 2. The ten countries with the largest import volumes
rice_import_raw_data = pd.read_csv('Rice_China_import_Quantity.csv')
rice_im_data = rice_import_raw_data[['Year', 'Partner Countries', 'Value', 'Unit']]
rice_im_data


# In[40]:


pd.DataFrame(rice_im_data.groupby(['Partner Countries']).sum()['Value']).sort_values('Value', ascending = False).head(10)


# In[41]:


# 3. The countries count in both list
pd.DataFrame(rice_ex_data.groupby(['Partner Countries']).sum()['Value']).sort_values('Value', ascending = False).head(10).merge(pd.DataFrame(rice_im_data.groupby(['Partner Countries']).sum()['Value']).sort_values('Value', ascending = False).head(10), on = 'Partner Countries').count()


# In[42]:


# 4. Annual net exportation

annual_ex = pd.DataFrame(rice_ex_data.groupby(['Year']).sum()['Value'])
annual_im = pd.DataFrame(rice_im_data.groupby(['Year']).sum()['Value'])
annual_net = annual_ex.merge(annual_im, on = 'Year')
annual_net['Net_exportation'] = annual_net['Value_x'] - annual_net['Value_y']
annual_net


# In[43]:


# 5. Plot the annual net exportation, compare with exportation and 

annual_net[['Net_exportation', 'Value_x' , 'Value_y']].plot()

