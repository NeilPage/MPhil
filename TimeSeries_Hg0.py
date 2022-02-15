#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:51:48 2020

@author: ncp532
"""

# FILE SYSTEM PACKAGES
from netCDF4 import Dataset,MFDataset				# function used to open multiple netcdf files
import xarray as xr

# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

# DATA HANDLING PACKAGES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

# DRAWING PACKAGES
import cartopy.crs as ccrs
from matplotlib import cm                   # imports the colormap function from matplotlib
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt             
import matplotlib.dates as mdates            
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

#--------------
# Hg0
#--------------
Hg0_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_QAQC_17-18.csv', index_col=0)
Hg0_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_QAQC_17-18.csv', index_col=0)
Hg0_V3_17M  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_QAQC_17-18.csv', index_col=0)
Hg0_V3_17D  = Hg0_V3_17M
Hg0_V4_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V4_Hg0_QAQC_17-18.csv', index_col=0)

Hg0_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_QAQC_18-19.csv', index_col=0)
Hg0_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_QAQC_18-19.csv', index_col=0)
Hg0_V3_18M  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_QAQC_18-19.csv', index_col=0)
Hg0_V3_18D  = Hg0_V3_18M
Hg0_V4_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V4_Hg0_QAQC_18-19.csv', index_col=0)

Hg0_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_QAQC_2012.csv', index_col=0)
Hg0_PCAN    = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/PCAN_Hg0_QAQC_2017.csv', index_col=0)

#------------------------------------------------------------------------------
# Set the date

#--------------
# Hg0
#--------------
Hg0_V1_17.index   = pd.to_datetime(Hg0_V1_17.index,   dayfirst=True)
Hg0_V2_17.index   = pd.to_datetime(Hg0_V2_17.index,   dayfirst=True)
Hg0_V3_17M.index  = pd.to_datetime(Hg0_V3_17M.index,  dayfirst=True)
Hg0_V3_17D.index  = (pd.to_datetime(Hg0_V3_17D.index, dayfirst=True) - timedelta(hours=1))
Hg0_V4_17.index   = pd.to_datetime(Hg0_V4_17.index,   dayfirst=True)

Hg0_V1_18.index   = pd.to_datetime(Hg0_V1_18.index,   dayfirst=True)
Hg0_V2_18.index   = pd.to_datetime(Hg0_V2_18.index,   dayfirst=True)
Hg0_V3_18M.index  = pd.to_datetime(Hg0_V3_18M.index,  dayfirst=True)
Hg0_V3_18D.index  = (pd.to_datetime(Hg0_V3_18D.index, dayfirst=True) - timedelta(hours=1))
Hg0_V4_18.index   = pd.to_datetime(Hg0_V4_18.index,   dayfirst=True)

Hg0_SIPEXII.index = pd.to_datetime(Hg0_SIPEXII.index, dayfirst=True)
Hg0_PCAN.index    = pd.to_datetime(Hg0_PCAN.index,    dayfirst=True)

#------------------------------------------------------------------------------
# PASSIVATION ISSUE WITH CELL A ON VOYAGES V3_18M, V3_18D and V4_18 (FILTER DATA)

Filter1    = Hg0_V3_18M['Cart'] == "B"
Hg0_V3_18M = Hg0_V3_18M[Filter1]

Filter2    = Hg0_V3_18D['Cart'] == "B"
Hg0_V3_18D = Hg0_V3_18D[Filter2]

Filter3    = Hg0_V4_18['Cart'] == "B"
Hg0_V4_18  = Hg0_V4_18[Filter3]

#------------------------------------------------------------------------------
# RESAMPLE THE Hg0 AND MET DATASETS TO 1-HOUR TIME RESOLUTION

#--------------
# Hg0
#--------------
Hg0_V1_17   = Hg0_V1_17.resample('60T').mean()
Hg0_V2_17   = Hg0_V2_17.resample('60T').mean()
Hg0_V3_17M  = Hg0_V3_17M.resample('60T').mean()
Hg0_V3_17D  = Hg0_V3_17D.resample('60T').mean()
Hg0_V4_17   = Hg0_V4_17.resample('60T').mean()

Hg0_V1_18   = Hg0_V1_18.resample('60T').mean()
Hg0_V2_18   = Hg0_V2_18.resample('60T').mean()
Hg0_V3_18M  = Hg0_V3_18M.resample('60T').mean()
Hg0_V3_18D  = Hg0_V3_18D.resample('60T').mean()
Hg0_V4_18   = Hg0_V4_18.resample('60T').mean()

Hg0_SIPEXII = Hg0_SIPEXII.resample('60T').mean()
Hg0_PCAN    = Hg0_PCAN.resample('60T').mean()

#------------------------------------------------------------------------------
# PLOT THE GRAPH

fig = plt.figure()

gs = gridspec.GridSpec(nrows=5,
                       ncols=2, 
                       figure=fig, 
                       width_ratios= [0.5,0.5],
                       height_ratios=[0.25, 0.25, 0.25, 0.25, 0.25])

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])

# Shade time on station
arrive1 = datetime(2017,11,14) # Arrive Davis (V1 17)
depart1 = datetime(2017,11,23) # Depart Davis (V1 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Davis", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_V1_17.index, Hg0_V1_17['ng/m3'], marker='x', markersize = 1.0, ls='None', c='blue', label ='V1 (2017-18)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[1,0])

# Shade time on station
arrive1 = datetime(2017,12,21) # Arrive Casey (V2 17)
depart1 = datetime(2017,12,23) # Depart Casey (V2 17)
arrive2 = datetime(2017,12,26) # Arrive Casey (V2 17)
depart2 = datetime(2018,1,6)   # Depart Casey (V2 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive2 + (depart2 - arrive2)/2, 1.85, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_V2_17.index, Hg0_V2_17['ng/m3'], marker='x', markersize = 1.0, ls='None', c='blue', label ='V2 (2017-18)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[2,0])

# Shade time on station
arrive1 = datetime(2018,2,1)  # Arrive Mawson (V3 17)
depart1 = datetime(2018,2,18) # Depart Mawson (V3 17)
arrive2 = datetime(2018,1,27) # Arrive Davis (V3 17)
depart2 = datetime(2018,1,31) # Depart Davis (V3 17)
arrive3 = datetime(2018,2,19) # Arrive Davis (V3 17)
depart3 = datetime(2018,2,22) # Depart Davis (V3 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Mawson", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive2 + (depart2 - arrive2)/2, 1.85, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive3 + (depart3 - arrive3)/2, 1.85, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_V3_17M.index, Hg0_V3_17M['ng/m3'], marker='x', markersize = 1.0, ls='None', c='blue', label ='V3 (2017-18)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 4
ax1 = plt.subplot(gs[3,0])

# Shade time on station
arrive1 = datetime(2018,3,12) # Arrive Maquarie Island (V4 17)
depart1 = datetime(2018,3,21) # Depart Maquarie Island (V4 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Maquarie Island", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_V4_17.index, Hg0_V4_17['ng/m3'], marker='x', markersize = 1.0, ls='None', c='blue', label ='V4 (2017-18)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=4)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 5
ax1 = plt.subplot(gs[0,1])

# Shade time on station
arrive1 = datetime(2018,11,7)  # Arrive Davis (V1 18)
depart1 = datetime(2018,11,16) # Depart Davis (V1 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Davis", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_V1_18.index, Hg0_V1_18['ng/m3'], marker='x', markersize = 1.0, ls='None', c='red', label ='V1 (2018-19)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)
ax1.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 6
ax1 = plt.subplot(gs[1,1])

# Shade time on station
arrive1 = datetime(2018,12,15) # Arrive Casey (V2 18)
depart1 = datetime(2018,12,31) # Depart Casey (V2 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_V2_18.index, Hg0_V2_18['ng/m3'], marker='x', markersize = 1.0, ls='None', c='red', label ='V2 (2018-19)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)
ax1.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 7
ax1 = plt.subplot(gs[2,1])

# Shade time on station
arrive1 = datetime(2019,1,30) # Arrive Mawson (V3 18)
depart1 = datetime(2019,2,10) # Depart Mawson (V3 18)
arrive2 = datetime(2019,1,26) # Arrive Davis (V3 18)
depart2 = datetime(2019,1,29) # Depart Davis (V3 18)
arrive3 = datetime(2019,2,19) # Arrive Davis (V3 18)
depart3 = datetime(2019,2,21) # Depart Davis (V3 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Mawson", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive2 + (depart2 - arrive2)/2, 1.85, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive3 + (depart3 - arrive3)/2, 1.85, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_V3_18M.index, Hg0_V3_18M['ng/m3'], marker='x', markersize = 1.0, ls='None', c='red', label ='V3 (2018-19)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)
ax1.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 8
ax1 = plt.subplot(gs[3,1])

# Shade time on station
arrive1 = datetime(2019,3,8)  # Arrive Maquarie Island (V4 18)
depart1 = datetime(2019,3,23) # Depart Maquarie Island (V4 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Maquarie Island", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_V4_18.index, Hg0_V4_18['ng/m3'], marker='x', markersize = 1.0, ls='None', c='red', label ='V4 (2018-19)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)
ax1.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 9
ax1 = plt.subplot(gs[4,0])

# Shade time on station
arrive1 = datetime(2012,9,23)  # Arrive Sea Ice (2012)
depart1 = datetime(2012,11,12) # Depart Sea Ice (2012)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
ax1.plot(Hg0_SIPEXII.index, Hg0_SIPEXII['ng/m3'], marker='x', markersize = 1.0, ls='None', c='green', label ='SIPEXII (2012)')

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Within sea Ice", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 10
ax1 = plt.subplot(gs[4,1])

# Shade time on station
arrive1 = datetime(2017,1,26) # Arrive close to Antarctica (2017)
depart1 = datetime(2017,2,25) # Depart close to Antarctica (2017)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Close to Antarctica", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(Hg0_PCAN.index, Hg0_PCAN['ng/m3'], marker='x', markersize = 1.0, ls='None', c='orange', label ='PCAN (2017)')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=45)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-0.1,2.0)
ax1.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

