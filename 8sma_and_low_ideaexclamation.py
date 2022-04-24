#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
import pathlib 
yf.pdr_override()


# In[2]:


ES = pd.read_csv("~/Desktop/market data/CHRIS-CME_ES1.csv", index_col = "Date",
                parse_dates=True, na_values=['nan'])


# In[3]:


es_close = pd.DataFrame(ES.Close)


# In[4]:


es_close['MA_8'] = es_close.Close.rolling(9).mean().shift()


# In[5]:


plt.figure(figsize=(15,10))
plt.grid(True)
plt.plot(es_close['Close'],label='ES')
plt.plot(es_close['MA_8'], label='MA 8 day')
plt.legend(loc=2)


# In[6]:


ES = pd.DataFrame(ES)


# In[7]:


ES['Signal'] = (ES['Low'] <= ES['Low'].shift(1)) & (ES['Volume'] < ES['Volume'].shift(1)) & (ES['Close'] < es_close['MA_8']) & (ES['Close'].shift(1) < es_close['MA_8'].shift(1))
ES['Returns'] = ES['Close'].shift(-1) - ES['Open'].shift(-1)
ES['Results']  = ES['Signal'] * ES['Returns']
plt.figure(figsize=(15,10))
plt.grid(True)
ES['Results'].cumsum().plot()
print(ES['Results'])


# In[8]:


plt.figure(figsize=(15,10))
plt.grid(True)
plt.plot(es_close['MA_8'], label='MA 8 day')
plt.plot(ES['Results'].cumsum())
plt.legend(loc=2)

