# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:43:10 2021

@author: serha
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('upwork_example_data.csv')

data['DATE'] = pd.to_datetime(data.DATE)
data['CLASS'] = data['CLASS'].astype('category')
data['CLASS'] = data['CLASS'].cat.codes


#Plot heatmap of feature correlation
plt.figure(figsize = (15,10))
sns.heatmap(data.corr())


#data.to_csv('result_data.csv',index=False)