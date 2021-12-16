#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:16:19 2021

@author: marieledbetter
"""

import pandas as pd

import matplotlib.pyplot as plt



df= pd.read_csv('/Users/marieledbetter/Downloads/FoodEnvironmentAtlas.csv')
df.sort_values(by=['County'], inplace=True, ascending=True)
df.plot.bar(x="County", y=None,);
plt.xlabel('US Counties')
plt.ylabel('Household food insecurity %, three-year average')
plt.title('Food Insecurity in US Counties Similar in Population')
plt.show() 