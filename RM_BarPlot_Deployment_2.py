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
import matplotlib.gridspec as gridspec
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# REACTIVE MERCURY
DF1 = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_RM_Deployment.csv')
DF2 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_17_18_RM_Deployment.csv')
DF3 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_18_19_RM_Deployment.csv')

#------------------------------------------------------------------------------
# Set the date

#-------------
# DF1
dattim1 = np.array(DF1['Date'])

#CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(dattim1)):
    date1.append(datetime.strptime(dattim1[i],'%d/%m/%Y')) # midday data 

#-------------
# DF2
dattim2 = np.array(DF2['Date'])

#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y')) # midday data 

#-------------
# DF3
dattim3 = np.array(DF3['Date'])

#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y')) # midday data 
    
#------------------------------------------------------------------------------
# PLOT THE GRAPH

fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax1 = plt.subplot(311) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.05))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax1.set_zorder(ax2.get_zorder()+1)
ax1.patch.set_visible(False)

# Plot the RM and Error
ax1.plot(date1, DF1['RM_Conc'], marker=None, c='green', markersize = 3.0, ls='-', label ='PCAN (2017)')
UL = DF1['RM_Conc'] + DF1['RM_StDev'] # find the upper limit
LL = DF1['RM_Conc'] - DF1['RM_StDev'] # find the lower limit
ax1.plot(date1, UL, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax1.plot(date1, LL, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax1.fill_between(date1, UL, LL, facecolor='green', alpha=0.3) # fill the distribution

# Plot the Wind Speed
ax2.scatter(date1, DF1['WindSpeed_(m/s)'], marker='x', c='black')

# Plot the Precipitation
ax3.scatter(date1, DF1['Rainfall_(mm)'], marker='x', c='orange')

## Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
##xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
##ax.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
##ax2.axes.get_xaxis().set_visible(False)
#plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('green')
ax1.tick_params(axis='y', which='both', colors='green')
#ax1.set_ylim(0.25,0.65) # On Station

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.set_ylim(0.25,0.65) # On Station

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
#ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax1.set_ylabel('RM (pg/m$^3$)', fontsize=15)
ax2.set_ylabel('Wind Speed (m/s)', fontsize=15)
ax3.set_ylabel('Precipitation (mm/day)', fontsize=15)
ax1.set_xlabel('Date', fontsize=15)

#Plot the legend and title
ax1.set_title('PCAN (2017)', fontsize=15, y=1.02)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 2
ax1 = plt.subplot(312) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.05))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax1.set_zorder(ax2.get_zorder()+1)
ax1.patch.set_visible(False)

# Plot the RM and Error
ax1.plot(date2, DF2['RM_Conc'], marker=None, c='blue', markersize = 3.0, ls='-', label ='CAMMPCAN (2017-18)')
UL = DF2['RM_Conc'] + DF2['RM_StDev'] # find the upper limit
LL = DF2['RM_Conc'] - DF2['RM_StDev'] # find the lower limit
ax1.plot(date2, UL, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax1.plot(date2, LL, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax1.fill_between(date2, UL, LL, facecolor='blue', alpha=0.3) # fill the distribution

# Plot the Wind Speed
ax2.scatter(date2, DF2['WindSpeed_(m/s)'], marker='x', c='black')

# Plot the Precipitation
ax3.scatter(date2, DF2['Rainfall_(mm)'], marker='x', c='orange')

## Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
##xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
##ax.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
##ax2.axes.get_xaxis().set_visible(False)
#plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax1.yaxis.label.set_color('blue')
ax1.tick_params(axis='y', which='both', colors='blue')
#ax1.set_ylim(0.25,0.65) # On Station

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.set_ylim(0.25,0.65) # On Station

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
#ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax1.set_ylabel('RM (pg/m$^3$)', fontsize=15)
ax2.set_ylabel('Wind Speed (m/s)', fontsize=15)
ax3.set_ylabel('Precipitation (mm/day)', fontsize=15)
ax1.set_xlabel('Date', fontsize=15)

#Plot the legend and title
ax1.set_title('CAMMPCAN (2017-18)', fontsize=15, y=1.02)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 3
ax1 = plt.subplot(313) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.05))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax1.set_zorder(ax2.get_zorder()+1)
ax1.patch.set_visible(False)

# Plot the RM and Error
ax1.plot(date3, DF3['RM_Conc'], marker=None, c='red', markersize = 3.0, ls='-', label ='CAMMPCAN (2018-19)')
UL = DF3['RM_Conc'] + DF3['RM_StDev'] # find the upper limit
LL = DF3['RM_Conc'] - DF3['RM_StDev'] # find the lower limit
ax1.plot(date3, UL, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax1.plot(date3, LL, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax1.fill_between(date3, UL, LL, facecolor='red', alpha=0.3) # fill the distribution

# Plot the Wind Speed
ax2.scatter(date3, DF3['WindSpeed_(m/s)'], marker='x', c='black', label ='Wind Speed (m/s)')

# Plot the Precipitation
ax3.scatter(date3, DF3['Rainfall_(mm)'], marker='x', c='orange', label ='Precipitation (mm/day)')

## Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
##xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
##ax.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
##ax2.axes.get_xaxis().set_visible(False)
#plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', which='both', colors='red')
#ax1.set_ylim(0.25,0.65) # On Station

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.set_ylim(0.25,0.65) # On Station

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
#ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax1.set_ylabel('RM (pg/m$^3$)', fontsize=15)
ax2.set_ylabel('Wind Speed (m/s)', fontsize=15)
ax3.set_ylabel('Precipitation (mm/day)', fontsize=15)
ax1.set_xlabel('Date', fontsize=15)

#Plot the legend and title
ax1.set_title('CAMMPCAN (2018-19)', fontsize=15, y=1.02)
fig.legend(loc='upper left', bbox_to_anchor=(0.02, 0.89), title='Season',fontsize=12)
#fig.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()