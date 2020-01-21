# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:13:42 2019

@author: GIGABYTE
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df2 = pd.read_csv('C:/Users/GIGABYTE/Desktop/XXX/xxfiles/april_talabat_2018.csv',
                 encoding='ISO-8859-1', parse_dates=['OrderInTime'], 
                 index_col=['OrderInTime'])

df4 = pd.read_csv('C:/Users/GIGABYTE/Desktop/xxx/xxx/april_talabat_2018.csv',
                 encoding='ISO-8859-1')

df2.head()

df2.plot()

plt.figure(figsize=(15,8))
df2.plot(y='OrderAmt', figsize=(12,8), fontsize=12)

order_monthy = df2.resample('W').mean()

dates = pd.date_range('2014-04-03', '2014-04-10')

# converting ordertime column to datatime

df4['time'] = pd.to_datetime(df4.OrderInTime)
#now new colum is in date time format
df4['day'] = df4.time.dt.day
df4['day'].value_counts()
df4['day'].value_counts().sort_index()
df4['day'].value_counts().sort_index().plot()

mean_orders_april_plot = df4['day'].value_counts().mean()
std_plus = df4['day'].value_counts().std()

plt.figure(figsize=(12,8))
plt.plot(df4['day'].value_counts().sort_index(), '-o')
plt.title('Number of order in April')
plt.xlabel('Days')
plt.ylabel('Orders')
plt.axhline(mean_orders_april_plot, label='Mean orders num = 181', 
            color='green', linestyle='--')
plt.axhline(mean_orders_april_plot + std_plus, 
            label='1 std above the mean = 245', c='red', linestyle='--')
plt.axhline(mean_orders_april_plot - std_plus, 
            label='1 std below the mean = 117', linestyle='--')
plt.legend()


df4['hour'] = df4.time.dt.hour

plt.figure(figsize=(12,5))
plt.plot(df4['hour'].value_counts().sort_index(), '-o')
plt.title('Orders by the Hour April')
plt.xlabel('Hours of the day')
plt.ylabel('Orders Numbers')

plt.hist(df4['hour'].value_counts(normalize=True).sort_index()* 100)

df4['hour'].value_counts(normalize=True).sort_index().plot()

plt.figure(figsize=(12,5))
plt.plot(df4['hour'].value_counts(normalize=True).sort_index(), '-o', c='Red')
plt.title('Percentage of Orders by the Hour April')
plt.xlabel('Hours of the day')
plt.ylabel('% of Orders Numbers')








