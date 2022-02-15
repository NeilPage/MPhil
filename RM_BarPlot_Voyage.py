#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:14:04 2019

@author: ncp532
"""


# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
from windrose import WindroseAxes

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd
from scipy import stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# PCAN and CAMMPCAN
DF1 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_RM_Voyage.csv')
DF2 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_RM_Deployment.csv')

#------------------------------------------------------------------------------
# Reactive Hg concentrations

# CAMMPCAN (2017-18)
V1_17 = DF1['RM_Conc'][1]
V2_17 = DF1['RM_Conc'][2]
V3_17 = DF1['RM_Conc'][3]
V4_17 = DF1['RM_Conc'][4]

# CAMMPCAN (2018-19)
V1_18 = DF1['RM_Conc'][5]
V2_18 = DF1['RM_Conc'][6]
V3_18 = DF1['RM_Conc'][7]
V4_18 = DF1['RM_Conc'][8]

# PCAN (2017)
PCAN = DF1['RM_Conc'][0]

#------------------------------------------------------------------------------
# Standard devition

# CAMMPCAN (2017-18)
STD1 = DF1['StDev'][1]
STD2 = DF1['StDev'][2]
STD3 = DF1['StDev'][3]
STD4 = DF1['StDev'][4]

# CAMMPCAN (2018-19)
STD5 = DF1['StDev'][5]
STD6 = DF1['StDev'][6]
STD7 = DF1['StDev'][7]
STD8 = DF1['StDev'][8]

# PCAN (2017)
STD9 = DF1['StDev'][0]

#------------------------------------------------------------------------------
# Build a dataframe for the Hg0 Bar Graph

# Graph 3: RM data set-up
RM1 = [V1_17, V2_17, V3_17]
RM2 = [V2_18, V3_18, V4_18]
RM3 = [PCAN]

# Graph 3: STD data set-up
St_Dev1 = [STD1, STD2, STD3]
St_Dev2 = [STD6, STD7, STD8]
St_Dev3 = [STD9]

#------------------------------------------------------------------------------
# PLOT THE GRAPH

# Graph 1
fig1, ax1 = plt.subplots()

# Set the positions for each of the datasets
p1 = [1,2,3]
p2 = [2.3,3.3,4.3]
p3 = 5

# Configurations for the datasets
bar_width = 0.3
opacity = 0.8

# Plot the data
rects1 = ax1.bar(p1, RM1, bar_width, alpha=opacity, color='b', ec='black', label='CAMMPCAN (2017-18)', yerr=St_Dev1, capsize=5)
rects2 = ax1.bar(p2, RM2, bar_width, alpha=opacity, color='r', ec='black', label='CAMMPCAN (2018-19)', yerr=St_Dev2, capsize=5)
rects3 = ax1.bar(p3, RM3, bar_width, alpha=opacity, color='g', ec='black', label='PCAN (2017)',    yerr=St_Dev3, capsize=5)
rects4 = ax1.bar(4, 0.5, bar_width, alpha=opacity, color='b', ec='black')
rects5 = ax1.bar(1.3, 0.5, bar_width, alpha=opacity, color='r', ec='black')


# Label the data values

for i, v in enumerate(RM1):
    ax1.text(i-0.05 + 1,v/RM1[i]+5,RM1[i],fontsize=12,color='black',fontweight='bold')

for i, v in enumerate(RM2):
    ax1.text(i-0.05 + 2.3,v/RM2[i]+5,RM2[i],fontsize=12,color='black',fontweight='bold')

for i, v in enumerate(RM3):
    ax1.text(i-0.05 + 5,v/RM3[i]+5,RM3[i],fontsize=12,color='black',fontweight='bold')

# Set up ticks for X and Y axis
plt.xticks([1.15,2.15,3.15,4.15,5],['V1','V2','V3','V4','PCAN'])
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(10))

# Axis labels, title and legend
ax1.set_ylabel('RM (pg/m$^3$)', fontsize=16, labelpad=15)
ax1.set_xlabel('Voyage', fontsize=16, labelpad=15)
ax1.set_title('RM concentrations observed during PCAN and CAMMPCAN 2017-19',fontsize=20,y=1.02)
ax1.legend(loc='upper left',title='Season',fontsize=12)

plt.show()