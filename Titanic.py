# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:25:16 2019

@author: Lenovo
"""

import pandas as pd

titanic = pd.read_csv("titanic.csv")
titanic.head(10)

# replace null value in 'embarked' column with 'S'
values = {'embarked' : 'S'}
titanic.fillna(values, inplace = True)
    
    # check the column again
titanic['embarked'].isnull().sum()

# fill the NA data in 'age'
    # use age mean as replacement value
titanic['age'].isnull().sum()

    # count the age mean
Mage = titanic['age'].mean()
print(Mage)

import math as mt
Mage = mt.ceil(Mage)

    # replace the NA
titanic['age'].fillna(30, inplace=True)

# Lifeboat data in 'boat' column
titanic['boat'].isnull().sum()

    # fill with 'None' string
titanic['boat'].fillna('None', inplace = True)

# Cabin number
titanic['cabin'].fillna('Unknown', inplace = True)

# 'home.dest'
titanic['home.dest'].fillna('Unkown', inplace = True)

# Write to csv
titanic.to_csv(r"C:\Users\Lenovo\Documents\Python Scripts\Spyder\Numpy&Pandas\titanic_clean.csv")


