# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## LIBRARIES ##
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


## DATASET ##
df = pd.read_csv('train.csv')


## EXPLORATORY DATA ANALYSIS ##
# check variables
df.columns

# view sale price
df.SalePrice.describe()
sns.distplot(df.SalePrice)

# check sale price skew
df.SalePrice.skew() # 1.88
df.SalePrice.kurt() # 6.54

# view sale price x categorical variables with 'high' predicted importance
# MSZoning
sns.boxplot(df.MSZoning, df.SalePrice) # moderate relationship
                                       # no housing in agriculture or industrial zones
# Neighborhood
f,ax = plt.subplots(figsize=(12,8))
sns.boxplot(df.Neighborhood, df.SalePrice)
plt.title('Sale Price by Neighborhood', weight='bold', size=20)
plt.xticks(rotation=90) # strong relationship
                        # potential relationship with zoning
                        
# CentralAir
sns.boxplot(df.CentralAir, df.SalePrice) # weak relationship

# view sale price x all numeric variables
# correlation heatmap
plt.subplots(figsize=(12,9))
sns.heatmap(df.corr(), vmax=0.8, square=True) # 5 strongest correlations:
                                              # OverallQual
                                              # GrLivArea
                                              # GarageCars/GarageArea
                                              # TotalBsmtSF
                                              # 1stFlrSF
                                              
# view sale price x top 10 numeric variables
# ordered correlation coeff heatmap
k = 10
cols = df.corr().nlargest(k, 'SalePrice').index
cm = np.corrcoef(df[cols].values.T) # .T = transpose
mask = np.zeros_like(cm)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style('white'):
    f,ax = plt.subplots(figsize=(10,10))
    sns.set(font_scale=1.0)
    sns.heatmap(cm, cmap='Blues', cbar=True, annot=True, square=True, fmt='.1f', annot_kws={'size':12}, 
                yticklabels=cols.values, xticklabels=cols.values, linewidths=1, linecolor='white', mask=mask)
    plt.title('Numerical Features Correlation Map', weight='bold', fontsize=22)
    plt.show()

# check dist of top 5 numeric variables
sns.distplot(df.OverallQual)   
sns.distplot(df.GrLivArea)
sns.distplot(df.GarageCars)
sns.distplot(df.GarageArea)
sns.distplot(df.TotalBsmtSF)
sns.distplot(df['1stFlrSF'])

# check corr in top 5 numeric variables
df[['GarageArea', 'GarageCars']].corr() # 0.88
df[['TotalBsmtSF', '1stFlrSF']].corr() # 0.82
df[['TotRmsAbvGrd', 'GrLivArea']].corr() # 0.83

# view pivot tables of top 10 numeric variables
pd.pivot_table(df, index = '')



## TASKS ##
# create pivot tables
# identify primary variables
# check distribution and outliers
