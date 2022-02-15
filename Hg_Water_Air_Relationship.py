#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:09:27 2020

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
from scipy import signal, stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

SIPEXII_Air = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_QAQC_2012.csv')
SIPEXII_H2O = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Ocean/SIPEXII_Ocean_HgT.csv')

#------------------------------------------------------------------------------
# Set the date

SIPEXII_Air['DateTime'] = pd.to_datetime(SIPEXII_Air['DateTime'], dayfirst=True)

#------------------------------------------------------------------------------
# Filter the datasets for each Ice Station

#-----------------------------------
# Ice Station 0 (-62.50 S, 121.50 E)
# (23/09/2012 08:00:00)
#-----------------------------------
start_time = '2012-09-23 00:00:00'
end_time   = '2012-09-23 23:59:00'
zero = (SIPEXII_Air['DateTime'] >= start_time) & (SIPEXII_Air['DateTime'] < end_time)
IceS0 = SIPEXII_Air[zero]

#-----------------------------------
# Ice Station 2 (-62.50 S, 121.50 E)
# (26/09/2012 12:45:00) (29/09/2012 16:30:00)
#-----------------------------------
start_time = '2012-09-26 00:00:00'
end_time   = '2012-09-29 23:59:00'
two = (SIPEXII_Air['DateTime'] >= start_time) & (SIPEXII_Air['DateTime'] < end_time)
IceS2 = SIPEXII_Air[two]

#-----------------------------------
# Ice Station 4 (-62.50 S, 121.50 E)
# (07/10/2012 18:00:00) (09/10/2012 09:30:00)
#-----------------------------------
start_time = '2012-10-07 00:00:00'
end_time   = '2012-10-09 23:59:00'
four = (SIPEXII_Air['DateTime'] >= start_time) & (SIPEXII_Air['DateTime'] < end_time)
IceS4 = SIPEXII_Air[four]

#-----------------------------------
# Ice Station 6 (-62.50 S, 121.50 E)
# (13/10/2012 09:00:00) (14/10/2012 17:00:00)
#-----------------------------------
start_time = '2012-10-13 00:00:00'
end_time   = '2012-10-14 23:59:00'
six = (SIPEXII_Air['DateTime'] >= start_time) & (SIPEXII_Air['DateTime'] < end_time)
IceS6 = SIPEXII_Air[six]

#-----------------------------------
# Ice Station 7 (-62.50 S, 121.50 E)
# (20/10/2012 09:00:00) (24/10/2012 06:00:00)
#-----------------------------------
start_time = '2012-10-20 00:00:00'
end_time   = '2012-10-23 23:59:00'
seven = (SIPEXII_Air['DateTime'] >= start_time) & (SIPEXII_Air['DateTime'] < end_time)
IceS7 = SIPEXII_Air[seven]

#-----------------------------------
# Ice Station 8 (-62.50 S, 121.50 E)
# (29/10/2012 09:00:00) (04/11/2012 16:00:00)
#-----------------------------------
start_time = '2012-10-29 00:00:00'
end_time   = '2012-10-29 23:59:00'
eight = (SIPEXII_Air['DateTime'] >= start_time) & (SIPEXII_Air['DateTime'] < end_time)
IceS8 = SIPEXII_Air[eight]

#-----------------------------------
# ALL ICE STATIONS
#-----------------------------------
SIPEXII = np.concatenate((IceS0['ng/m3'], IceS2['ng/m3'], IceS4['ng/m3'], IceS6['ng/m3'], IceS7['ng/m3'], IceS8['ng/m3']), axis = None)

#------------------------------------------------------------------------------
# CALCULATE THE MEAN HG0

IceS0_Mean   = np.mean(IceS0['ng/m3'])
IceS2_Mean   = np.mean(IceS2['ng/m3'])
IceS4_Mean   = np.mean(IceS4['ng/m3'])
IceS6_Mean   = np.mean(IceS6['ng/m3'])
IceS7_Mean   = np.mean(IceS7['ng/m3'])
IceS8_Mean   = np.mean(IceS8['ng/m3'])
SIPEXII_Mean = np.mean(SIPEXII)

#------------------------------------------------------------------------------
# CALCULATE THE HG0 STANDARD DEVIATION

IceS0_std   = np.std(IceS0['ng/m3'])
IceS2_std   = np.std(IceS2['ng/m3'])
IceS4_std   = np.std(IceS4['ng/m3'])
IceS6_std   = np.std(IceS6['ng/m3'])
IceS7_std   = np.std(IceS7['ng/m3'])
IceS8_std   = np.std(IceS8['ng/m3'])
SIPEXII_std = np.std(SIPEXII)

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN HG0

IceS0_Median   = np.median(IceS0['ng/m3'])
IceS2_Median   = np.median(IceS2['ng/m3'])
IceS4_Median   = np.median(IceS4['ng/m3'])
IceS6_Median   = np.median(IceS6['ng/m3'])
IceS7_Median   = np.median(IceS7['ng/m3'])
IceS8_Median   = np.median(IceS8['ng/m3'])
SIPEXII_Median = np.median(SIPEXII)

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN ABSOLUTE DEVIATION HG0

IceS0_MAD   = stats.median_absolute_deviation(IceS0['ng/m3'])
IceS2_MAD   = stats.median_absolute_deviation(IceS2['ng/m3'])
IceS4_MAD   = stats.median_absolute_deviation(IceS4['ng/m3'])
IceS6_MAD   = stats.median_absolute_deviation(IceS6['ng/m3'])
IceS7_MAD   = stats.median_absolute_deviation(IceS7['ng/m3'])
IceS8_MAD   = stats.median_absolute_deviation(IceS8['ng/m3'])
SIPEXII_MAD = stats.median_absolute_deviation(SIPEXII)

#------------------------------------------------------------------------------
# BUILD A DATAFRAME FOR THE BOXPLOT

Air          = [IceS0_Mean,IceS2_Mean,IceS4_Mean,IceS6_Mean,IceS7_Mean,IceS8_Mean,SIPEXII_Mean]
Air          = np.round(Air, 2)
Snow         = SIPEXII_H2O['Snow'][0:7]
SeaIce       = SIPEXII_H2O['Sea_Ice'][0:7]
Brine        = SIPEXII_H2O['Brine'][0:7]
SeaWaterDeep = SIPEXII_H2O['SeaWater_Deep'][0:7]
SeaWaterUI   = SIPEXII_H2O['SeaWater_UnderIce'][0:7]
X = np.arange(7)

#------------------------------------------------------------------------------
# PLOT THE GRAPH

fig = plt.figure()

gs = gridspec.GridSpec(nrows=1,
                       ncols=1, 
                       figure=fig, 
                       width_ratios= [1],
                       height_ratios=[1],
                       hspace=0.0)

#-----------------------------

ax1 = plt.subplot(gs[0])
ax2 = ax1.twinx()
# Configurations for the datasets
bar_width = 0.15
opacity = 0.8

# Plot the data
rects1 = ax1.bar(X- 0.15, Air, bar_width, alpha=opacity, color='blue', ec='black', label='Air (ng/m$^3$)')
rects2 = ax2.bar(X, Snow, bar_width, alpha=opacity, color='red', ec='black', label='Snow (pmol/L)')
rects3 = ax2.bar(X+ 0.15, SeaIce, bar_width, alpha=opacity, color='green', ec='black', label='Sea Ice (pmol/L)')
rects4 = ax2.bar(X+ 0.3, Brine, bar_width, alpha=opacity, color='yellow', ec='black', label='Brine (pmol/L)')
rects5 = ax2.bar(X+ 0.45, SeaWaterDeep, bar_width, alpha=opacity, color='purple', ec='black', label='Sea Water Deep (pmol/L)')
rects6 = ax2.bar(X+ 0.6, SeaWaterUI, bar_width, alpha=opacity, color='grey', ec='black', label='Sea Water Under Ice (pmol/L)')

# Label the data values
#for i, v in enumerate(Air):
#    ax1.text(i-0.175 ,v/Air[i]-0.1,Air[i],fontsize=10,color='black',fontweight='bold')

def autolabel1(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax1.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def autolabel2(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax2.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel1(rects1)
autolabel2(rects2)
autolabel2(rects3)
autolabel2(rects4)
autolabel2(rects5)
autolabel2(rects6)

# Set up ticks for X and Y axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.02))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax1.set_ylim(0.9,1.15)

ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))

# Axis labels, title and legend
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=16, labelpad=15)
ax2.set_ylabel('Total Hg (pmol/L)', fontsize=16, labelpad=15)
ax1.set_xlabel('Ice Station (no:)', fontsize=16, labelpad=15)
fig.legend(loc='upper left', bbox_to_anchor=(0.125, 0.875), fontsize=16)
plt.title('Mercury concentrations at each ice station', fontsize=25, y=1.01)
plt.xticks([0,1,2,3,4,5,6],['0','2','4','6','7','8','Mean'])

plt.show()
