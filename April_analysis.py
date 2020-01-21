# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df.head()

df.isnull().sum()
df['CustName'].nunique()

#plot areas
plt.figure(figsize=(20,9))
plt.title('Order Count by Area')
sns.countplot(df['AreaName'].sort_values())
plt.xticks(rotation=90)

#average orders
plt.figure(figsize=(15,8))
sns.distplot(df['OrderAmt'])

repeat_cust = (
        df['OrderAmt']
        .groupby(df['CustName'])
        )

area_orders = (
        df
        .groupby(df['AreaName'])
        )


plt.figure(figsize=(15,8))
sns.barplot(x='AreaName', y='OrderAmt',  data=df)
plt.xticks(rotation='90')

df_area = df.groupby('AreaName')['OrderAmt'].sum().sort_values()

sns.barplot(df.groupby('AreaName')['OrderAmt'].sum().sort_values())

sns.distplot(df_area)

df_area_mean = df.groupby('AreaName')['OrderAmt'].mean().sort_values()
df_area_mean_2 = df.groupby('AreaName')['OrderAmt'].mean().iloc[::-1].index


plt.figure(figsize=(15,8))
plt.grid()
plt.title('Average of order amount all area April 2018')
sns.distplot(df_area_mean)

plt.figure(figsize=(20,20))
sns.boxplot(y='AreaName', x='OrderAmt', data=df.sort_values(by='OrderAmt'), order=df_area_mean_2)
plt.xticks(rotation='90')
#sns.despine(trim=True, left=True)
plt.grid()
plt.title('Average order Amounts by Area April 2018')

plt.figure(figsize=(8,20))
sns.boxplot(y='AreaName', x='OrderAmt', 
            data=less_tha_10kd.sort_values(by='OrderAmt'), 
            order=df_area_mean_2)
plt.xticks(rotation='90')
#sns.despine(trim=True, left=True)
plt.grid()
plt.title('Average order Amounts by Area April 2018 less than 10k order')

median = df['OrderAmt'].median()
percentage25 = np.percentile(df['OrderAmt'], 25)
percentage75 = np.percentile(df['OrderAmt'], 75)

means_by_area = (
        df['OrderAmt']
        .groupby(df['AreaName'])
        .mean()
        .rename('mean_orders')
        .reset_index()
        )

plt.figure(figsize=(18,8))
sns.barplot(x='AreaName', y='mean_orders', data=means_by_area.sort_values(by='mean_orders'))
plt.title('Mean orders by Area')
plt.xticks(rotation=90)
plt.axhline(median, color='black', label='Median of all order', linestyle='dashed')
plt.legend()

plt.figure(figsize=(18,15))
sns.swarmplot(less_tha_10kd['AreaName'],less_tha_10kd['OrderAmt'].sort_values(by='OrderAmt'), 
              hue=less_tha_10kd['PaymentMode'], size=4)
plt.title('Order  plot Cash/CC/Knet')
plt.xticks(rotation=90)
plt.axhline(median, color='black', label='Median of all order', linestyle='dashed')
plt.axhline(percentage75, color='green', label='75% of all order', linestyle='dashed')
plt.axhline(percentage25, color='blue', label='25% of all order', linestyle='dashed')
plt.legend()

plt.figure(figsize=(18,15))
plt.xticks(rotation=90)
sns.swarmplot(less_tha_10kd['AreaName'], less_tha_10kd['OrderAmt'],
              hue=less_tha_10kd['BranchName'], size=4)
plt.title('Hue by Branches by Orders')


less_tha_10kd = df[df['OrderAmt'] < 10]


above_below = lambda x : 'above_mean'if x > 5 else 'below_mean'
df['above_or_below'] = df['OrderAmt'].apply(above_below)

plt.figure(figsize=(18,15))
sns.countplot(x='AreaName', data=df, order=df['AreaName'].value_counts(ascending=True))
plt.xticks(rotation=90)

    

#plot by area by counts horizontal
plt.figure(figsize=(18,15))
df['AreaName'].value_counts().plot(kind="barh")
plt.title('Count of orders by Areas')
plt.xlabel('Areas')
plt.grid()
plt.show()

orders_by_branches = (
        df['OrderAmt']
        .groupby(df['BranchName'])
        .sum(ascending=True)
        .rename('Sum_of_branches')
        .reset_index()
        )

#sns.set(style="whitegrid")
plt.figure(figsize=(18,8))
sns.barplot(x='BranchName', y='Sum_of_branches', data=orders_by_branches.sort_values(by='Sum_of_branches'))
plt.title('Sum of Branches by Amount KD')
plt.xticks(rotation=90)
plt.grid()

plt.figure(figsize=(18,15))
df['BranchName'].value_counts().plot(kind="barh")
plt.title('Count of orders by Branches')
plt.xlabel('Order numbers')
plt.grid()
plt.show()


df['BranchName'].value_counts()







