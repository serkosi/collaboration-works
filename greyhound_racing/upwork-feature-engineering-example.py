#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('upwork_example_data.csv')
data['DATE'] = pd.to_datetime(data.DATE)


# In[4]:


data['CLASS'] = data['CLASS'].astype('category')
data['CLASS'] = data['CLASS'].cat.codes


# In[5]:


data['FT3'] = data.groupby('NAME')['TIME'].transform(lambda x: x.rolling(3).min().shift())
data['FT12'] = data.groupby('NAME')['TIME'].transform(lambda x: x.rolling(12).min().shift())


# In[6]:


data['AB3'] = data.groupby('NAME')['BREAK'].transform(lambda x: x.rolling(3).mean().shift())
data['AB12'] = data.groupby('NAME')['BREAK'].transform(lambda x: x.rolling(12).mean().shift())


# In[7]:


data['AF3'] = data.groupby('NAME')['FINISH'].transform(lambda x: x.rolling(3).mean().shift())
data['AF12'] = data.groupby('NAME')['FINISH'].transform(lambda x: x.rolling(12).mean().shift())


# In[8]:


data['T3'] = data.groupby('NAME')['TIME'].transform(lambda x: x.rolling(3).mean().shift())
data['T12'] = data.groupby('NAME')['TIME'].transform(lambda x: x.rolling(12).mean().shift())


# In[9]:


data['AG3'] = data.groupby('NAME')['CLASS'].transform(lambda x:x.rolling(3).mean().shift())
data['AG12'] = data.groupby('NAME')['CLASS'].transform(lambda x:x.rolling(12).mean().shift())


# In[10]:


data['PLACED'] = np.where(data['FINISH'] <= 3, 1, 0)
data['WIN'] = np.where(data['FINISH'] == 1, 1, 0)

data['Placings'] = (data.groupby('NAME')['PLACED'].apply(lambda x: x.shift().expanding().sum()))
data['Wins'] = (data.groupby('NAME')['WIN'].apply(lambda x: x.shift().expanding().sum()))

data['STARTS'] = (data.groupby('NAME')['FINISH'].apply(lambda x: x.shift().expanding().count())).astype('int')

data['WinP'] = (data['Wins'] / data['STARTS']).round(2)

data['PlaceP'] = (data['Placings'] / data['STARTS']).round(2)

# data = data.dropna()
# data.sort_values('DATE', inplace = True)


# In[11]:

# Average position at turn-1 in last three races and last twelve races
data['AT-one3'] = data.groupby('NAME')['TURN1'].transform(lambda x: x.rolling(3).mean().shift())
data['AT-one12'] = data.groupby('NAME')['TURN1'].transform(lambda x: x.rolling(12).mean().shift())


# In[12]:

# Average position at turn-2 in last three races and last twelve races
data['AT-two3'] = data.groupby('NAME')['TURN2'].transform(lambda x: x.rolling(3).mean().shift())
data['AT-two12'] = data.groupby('NAME')['TURN2'].transform(lambda x: x.rolling(12).mean().shift())
