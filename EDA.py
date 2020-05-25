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

## DATASET ##
df = pd.read_csv('train.csv')

## EXPLORE ##
# check variables
df.columns

# view sale price
df.SalePrice.describe()
sns.distplot(df.SalePrice)

# check sale price skew
df.SalePrice.skew() # 1.88
df.SalePrice.kurt() # 6.54

# view sale price x variables with 'high' predicted importance
# OverallQual
sns.boxplot(df.OverallQual, df.SalePrice) # strong relationship
# OverallCond
sns.boxplot(df.OverallCond, df.SalePrice) # weak relationship
# YearBuilt
f, ax = plt.subplots(figsize=(16,8))
f = sns.boxplot(x=df.YearBuilt, y=df.SalePrice) # moderate relationship
f.axis(ymin=0, ymax=800000)
plt.xticks(rotation=90)
# GrLivArea
sns.scatterplot(df.GrLivArea, df.SalePrice) # strong relationship
# LotArea
sns.scatterplot(df.LotArea, df.SalePrice) # strong relationship

# view sale price x other variables of interest
# MSZoning
sns.boxplot(df.MSZoning, df.SalePrice) # moderate relationship
                                       # no housing in agriculture or industrial zones
# Neighborhood
sns.boxplot(df.Neighborhood, df.SalePrice) # strong relationship
                                           # potential relationship with zoning
# CentralAir
sns.boxplot(df.CentralAir, df.SalePrice) # weak relationship
# GarageArea
sns.scatterplot(df.GarageArea, df.SalePrice) # strong relationship
# YrSold
sns.boxplot(df.YrSold, df.SalePrice) # no relationship

# view sale price x all variables
# correlation heatmap
plt.subplots(figsize=(12,9))
sns.heatmap(df.corr(), vmax=0.8, square=True) # 5 strongest correlations:
                                              # OverallQual
                                              # GrLivArea
                                              # GarageCars/GarageArea
                                              # TotalBsmtSF
                                              # 1stFlrSF
                                              
# view sale price x top 10 variables
# ordered correlation coeff heatmap
k = 10
cols = df.corr().nlargest(k, 'SalePrice').index
cm = np.corrcoef(df[cols].values.T) # .T = transpose
sns.set(font_scale=1.0)
sns.heatmap(cm, cmap='Blues_r', cbar=True, annot=True, square=True, fmt='.1f', annot_kws={'size':9}, 
            yticklabels=cols.values, xticklabels=cols.values, linewidths=1)

# test validity of top 10 variables
sns.distplot(df.OverallQual)
sns.distplot(df.GrLivArea)
sns.distplot(df.GarageCars)
sns.distplot(df.GarageArea)
sns.distplot(df.TotalBsmtSF)
sns.distplot(df['1stFlrSF'])

## TASKS ##
# deal with NAs
# 

