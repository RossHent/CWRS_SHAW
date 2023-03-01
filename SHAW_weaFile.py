#!/usr/bin/env python
# coding: utf-8

# In[3]:


# -*- coding: utf-8 -*-
"""
Created on May 25, 2022

author: Ross Henteleff
"""
get_ipython().run_line_magic('reset', '-f')
import os
import pandas as pd
import numpy as np
import glob

#%% Importing & joining hourly data from CSVs

path_hr = r"C:\Users\uOttawa\Desktop\DAL\SHAW\runs\Inputs\Trial001\wea\rawData\hourly"

os.chdir(path_hr)

all_files_hr = glob.glob(os.path.join(path_hr,"*.csv"))

df_hr = pd.concat((pd.read_csv(f) for f in all_files_hr), ignore_index=True)

#%% Calculating daily averages of hourly data

df_hr2day = df_hr.groupby(np.arange(len(df_hr))//24).mean()

df_hr2day['Wind Spd (m/s)'] =  df_hr2day['Wind Spd (km/h)'] / 3.6

#%% Importing & joining daily data from CSVs

path_day = r"C:\Users\uOttawa\Desktop\DAL\SHAW\runs\Inputs\Trial001\wea\rawData\daily"

os.chdir(path_day)

all_files_day = glob.glob(os.path.join(path_day,"*.csv"))

df_day = pd.concat((pd.read_csv(f) for f in all_files_day), ignore_index=True)

#%% Importing daily solar data

path_solar = r"C:\Users\uOttawa\Desktop\DAL\SHAW\runs\Inputs\Trial001\wea\rawData\solar"

os.chdir(path_solar)

all_files_solar = glob.glob(os.path.join(path_solar,"*.csv"))

df_solar = pd.concat((pd.read_csv(f) for f in all_files_solar), ignore_index=True)

#%% Joining data together

wea = pd.DataFrame()

wea[1] = df_solar['DOY']
wea[2] = df_solar['YEAR']
wea[3] = df_day['Max Temp (°C)']
wea[4] = df_day['Min Temp (°C)']
wea[5] = df_day['Min Temp (°C)']
wea[6] = df_hr2day['Wind Spd (m/s)']
wea[7] = df_day['Total Precip (mm)']
wea[8] = df_solar['ALLSKY_SFC_SW_DWN']

path_wea = r"C:\Users\uOttawa\Desktop\DAL\SHAW\runs\Inputs\Trial001\wea"

os.chdir(path_wea)

wea.to_csv('Trial001.csv', sep='\t', index=False, header=False)


# In[ ]:





# In[ ]:




