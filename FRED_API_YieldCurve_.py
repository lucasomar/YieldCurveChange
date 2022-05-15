# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 08:02:28 2021

@author: Lucas
"""

from fredapi import Fred
fred = Fred(api_key='')
import pandas as pd
import matplotlib.pyplot as plt


# Dias para analizar
dia1 = '2022-05-09'
dia2 = '2022-05-12'

# Yield Curve
yield_curve_tickers = ['DGS1','DGS2','DGS5','DGS7','DGS10','DGS20','DGS30']
yield_curve = []
last_week_yield_curve = []

for i in yield_curve_tickers:
    data = fred.get_series(i)
    data_lw = data.tail(7)
    last_week_yield_curve.append(data_lw)

tabla_lw = pd.DataFrame(last_week_yield_curve, index=['DGS1','DGS2','DGS5','DGS7','DGS10','DGS20','DGS30'])


plt.style.use('dark_background')
plt.figure(figsize=(15,8))
ax = plt.gca()
tabla_lw.plot(kind='line',y=dia1,ax=ax)
tabla_lw.plot(kind='line',y=dia2,ax=ax)
plt.ylabel('Yield %')
plt.xlabel('Yield curve')
plt.show()


