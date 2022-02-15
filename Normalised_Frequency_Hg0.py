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
from scipy import stats

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
from matplotlib.lines import Line2D
import math

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

#--------------
# Hg0
#--------------
Hg0_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_QAQC_17-18.csv', index_col=0)
Hg0_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_QAQC_17-18.csv', index_col=0)
Hg0_V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_QAQC_17-18.csv', index_col=0)
Hg0_V4_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V4_Hg0_QAQC_17-18.csv', index_col=0)

Hg0_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_QAQC_18-19.csv', index_col=0)
Hg0_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_QAQC_18-19.csv', index_col=0)
Hg0_V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_QAQC_18-19.csv', index_col=0)
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
Hg0_V3_17.index   = pd.to_datetime(Hg0_V3_17.index,   dayfirst=True)
Hg0_V4_17.index   = pd.to_datetime(Hg0_V4_17.index,   dayfirst=True)

Hg0_V1_18.index   = pd.to_datetime(Hg0_V1_18.index,   dayfirst=True)
Hg0_V2_18.index   = pd.to_datetime(Hg0_V2_18.index,   dayfirst=True)
Hg0_V3_18.index   = pd.to_datetime(Hg0_V3_18.index,   dayfirst=True)
Hg0_V4_18.index   = pd.to_datetime(Hg0_V4_18.index,   dayfirst=True)

Hg0_SIPEXII.index = pd.to_datetime(Hg0_SIPEXII.index, dayfirst=True)
Hg0_PCAN.index    = pd.to_datetime(Hg0_PCAN.index,    dayfirst=True)

#------------------------------------------------------------------------------
# PASSIVATION ISSUE WITH CELL A ON VOYAGES V3_18M, V3_18D and V4_18 (FILTER DATA)

Filter1   = Hg0_V3_18['Cart'] == "B"
Hg0_V3_18 = Hg0_V3_18[Filter1]

Filter3   = Hg0_V4_18['Cart'] == "B"
Hg0_V4_18 = Hg0_V4_18[Filter3]

#------------------------------------------------------------------------------
# Filter the datasets for the voyage dates

#-----------------------------
# V1_17 Davis (29 Oct - 3 Dec 2017) (14-22 Nov 2017 on station)
#-----------------------------
start_date = '2017-10-29'
end_date   = '2017-12-04'
# Hg0
Davis      = (Hg0_V1_17.index >= start_date) & (Hg0_V1_17.index < end_date)
Hg0_V1_17  = Hg0_V1_17[Davis]

#-----------------------------
# V2_17 Casey (13 Dec 2017 - 11 Jan 2018) (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018 on station)
#-----------------------------
start_date = '2017-12-13'
end_date   = '2018-01-12'
# Hg0
Casey      = (Hg0_V2_17.index >= start_date) & (Hg0_V2_17.index < end_date)
Hg0_V2_17  = Hg0_V2_17[Casey]

#-----------------------------
# V3_17 Mawson (16 Jan - 6 Mar 2018) (1-17 Feb 2018 on station)
#-----------------------------
start_date = '2018-01-16'
end_date   = '2018-03-07'
# Hg0
Mawson     = (Hg0_V3_17.index >= start_date) & (Hg0_V3_17.index < end_date)
Hg0_V3_17  = Hg0_V3_17[Mawson]

#-----------------------------
# V4_17 Macquarie Island (9-23 Mar 2018) (12-20 Mar 2018 on station)
#-----------------------------
start_date = '2018-03-09'
end_date   = '2018-03-24'
# Hg0
MQIsl      = (Hg0_V4_17.index >= start_date) & (Hg0_V4_17.index < end_date)
Hg0_V4_17  = Hg0_V4_17[MQIsl]

#-----------------------------
# V1_18 Davis (25 Oct - 28 Nov 2018) (7-15 Nov 2018 on station)
#-----------------------------
start_date = '2018-10-25'
end_date   = '2018-11-29'
# Hg0
Davis      = (Hg0_V1_18.index >= start_date) & (Hg0_V1_18.index < end_date)
Hg0_V1_18  = Hg0_V1_18[Davis]

#-----------------------------
# V2_18 Casey (6 Dec 2018 - 7 Jan 2019) (15-30 Dec 2018 on station)
#-----------------------------
start_date = '2018-12-06'
end_date   = '2019-01-08'
# Hg0
Casey      = (Hg0_V2_18.index >= start_date) & (Hg0_V2_18.index < end_date)
Hg0_V2_18  = Hg0_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (13 Jan - 1 Mar 2019) (30 Jan - 9 Feb 2019)
#-----------------------------
start_date = '2019-01-13'
end_date   = '2019-03-2'
# Hg0
Mawson     = (Hg0_V3_18.index >= start_date) & (Hg0_V3_18.index < end_date)
Hg0_V3_18  = Hg0_V3_18[Mawson]

#-----------------------------
# V4_17 Macquarie Island (5-25 Mar 2019) (8-22 Mar 2019 on station)
#-----------------------------
start_date = '2019-03-05'
end_date   = '2019-03-26'
# Hg0
MQIsl      = (Hg0_V4_18.index >= start_date) & (Hg0_V4_18.index < end_date)
Hg0_V4_18  = Hg0_V4_18[MQIsl]

#-----------------------------
# SIPEXII (14 Sep to 16 Nov 2012) (23 Sep to 11 Nov 2012 close to Antarctica)
#-----------------------------
start_date  = '2012-09-14'
end_date    = '2012-11-16'
# Hg0
SIPEX       = (Hg0_SIPEXII.index >= start_date) & (Hg0_SIPEXII.index < end_date)
Hg0_SIPEXII = Hg0_SIPEXII[SIPEX]

#-----------------------------
# PCAN (14 Jan to 4 Mar 2017) (26 Jan to 24 Feb 2017 close to Antarctica)
#-----------------------------
start_date = '2017-01-14'
end_date   = '2017-02-25'
# Hg0
PCAN       = (Hg0_PCAN.index >= start_date) & (Hg0_PCAN.index < end_date)
Hg0_PCAN   = Hg0_PCAN[PCAN]

#------------------------------------------------------------------------------
# Filter the datasets for time on station / in sea ice

#-----------------------------
# V1_17 Davis (14-22 Nov 2017)
#-----------------------------
start_date   = '2017-11-14'
end_date     = '2017-11-23'
# Hg0
Davis           = (Hg0_V1_17.index >= start_date) & (Hg0_V1_17.index < end_date)
Hg0_Davis_V1_17 = Hg0_V1_17[Davis]

#-----------------------------
# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
#-----------------------------
start_date1 = '2017-12-21'
end_date1 = '2017-12-23'
start_date2 = '2017-12-26'
end_date2 = '2018-01-6'
# Hg0
Casey1          = (Hg0_V2_17.index >= start_date1) & (Hg0_V2_17.index < end_date1)
Casey2          = (Hg0_V2_17.index >= start_date2) & (Hg0_V2_17.index < end_date2)
Hg0_Casey_1     = Hg0_V2_17[Casey1]
Hg0_Casey_2     = Hg0_V2_17[Casey2]
Hg0_Casey_V2_17 = pd.concat([Hg0_Casey_1,Hg0_Casey_2], axis =0)

#-----------------------------
# V3_17 Mawson (1-17 Feb 2018)
#-----------------------------
start_date    = '2018-02-01'
end_date      = '2018-02-18'
# Hg0
Mawson           = (Hg0_V3_17.index >= start_date) & (Hg0_V3_17.index < end_date)
Hg0_Mawson_V3_17 = Hg0_V3_17[Mawson]

#-----------------------------
# V3_17 Davis (27-30 Jan 2018 and 19-21 Feb 2018)
#-----------------------------
start_date1   = '2018-01-27'
end_date1     = '2018-01-31'
start_date2   = '2018-02-19'
end_date2     = '2018-02-22'
# Hg0
Davis1          = (Hg0_V3_17.index >= start_date1) & (Hg0_V3_17.index < end_date1)
Davis2          = (Hg0_V3_17.index >= start_date2) & (Hg0_V3_17.index < end_date2)
Hg0_Davis_1     = Hg0_V3_17[Davis1]
Hg0_Davis_2     = Hg0_V3_17[Davis2]
Hg0_Davis_V3_17 = pd.concat([Hg0_Davis_1,Hg0_Davis_2], axis =0)

#-----------------------------
# V4_17 Macquarie Island (9-23 Mar 2018) (12-20 Mar 2018 on station)
#-----------------------------
start_date   = '2018-03-12'
end_date     = '2018-03-21'
# Hg0
MQIsl           = (Hg0_V4_17.index >= start_date) & (Hg0_V4_17.index < end_date)
Hg0_MQIsl_V4_17 = Hg0_V4_17[MQIsl]

#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
#-----------------------------
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# Hg0
Davis           = (Hg0_V1_18.index >= start_date) & (Hg0_V1_18.index < end_date)
Hg0_Davis_V1_18 = Hg0_V1_18[Davis]

#-----------------------------
# V2_18 Casey (15-30 Dec 2018)
#-----------------------------
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# Hg0
Casey           = (Hg0_V2_18.index >= start_date) & (Hg0_V2_18.index < end_date)
Hg0_Casey_V2_18 = Hg0_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#-----------------------------
start_date    = '2019-01-30'
end_date      = '2019-02-10'
# Hg0
Mawson           = (Hg0_V3_18.index >= start_date) & (Hg0_V3_18.index < end_date)
Hg0_Mawson_V3_18 = Hg0_V3_18[Mawson]

#-----------------------------
# V3_18 Davis (26-28 Jan 2019 and 19-20 Feb 2019)
#-----------------------------
start_date1   = '2019-01-26'
end_date1     = '2019-01-29'
start_date2   = '2019-02-19'
end_date2     = '2019-02-21'
# Hg0
Davis1          = (Hg0_V3_18.index >= start_date1) & (Hg0_V3_18.index < end_date1)
Davis2          = (Hg0_V3_18.index >= start_date2) & (Hg0_V3_18.index < end_date2)
Hg0_Davis_1     = Hg0_V3_18[Davis1]
Hg0_Davis_2     = Hg0_V3_18[Davis2]
Hg0_Davis_V3_18 = pd.concat([Hg0_Davis_1,Hg0_Davis_2], axis =0)

#-----------------------------
# V4_17 Macquarie Island (5-25 Mar 2019) (8-22 Mar 2019 on station)
#-----------------------------
start_date   = '2019-03-08'
end_date     = '2019-03-23'
# Hg0
MQIsl           = (Hg0_V4_18.index >= start_date) & (Hg0_V4_18.index < end_date)
Hg0_MQIsl_V4_18 = Hg0_V4_18[MQIsl]

#-----------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
#-----------------------------
start_date     = '2012-09-23'
end_date       = '2012-11-12'
# Hg0
SIPEX           = (Hg0_SIPEXII.index >= start_date) & (Hg0_SIPEXII.index < end_date)
Hg0_SIPEXII_Ice = Hg0_SIPEXII[SIPEX]

#-----------------------------
# PCAN (26 Jan to 24 Feb 2017)
#-----------------------------
start_date     = '2017-01-26'
end_date       = '2017-02-25'
# Hg0
PCAN         = (Hg0_PCAN.index >= start_date) & (Hg0_PCAN.index < end_date)
Hg0_PCAN_Ice = Hg0_PCAN[PCAN]

#------------------------------------------------------------------------------
# Combine the datasets for Mawson and Davis during V3

# Hg0_V3
Hg0_V3_17_Ice = Hg0_Davis_V3_17.append(Hg0_Mawson_V3_17)
Hg0_V3_18_Ice = Hg0_Davis_V3_18.append(Hg0_Mawson_V3_18)

#------------------------------------------------------------------------------
# Filter the datasets for time in open water

# Hg0_OW
Hg0_PCAN_OW    = Hg0_PCAN.merge(Hg0_PCAN_Ice,        how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_SIPEXII_OW = Hg0_SIPEXII.merge(Hg0_SIPEXII_Ice,  how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V1_17_OW   = Hg0_V1_17.merge(Hg0_Davis_V1_17,    how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V2_17_OW   = Hg0_V2_17.merge(Hg0_Casey_V2_17,    how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17_OW   = Hg0_V3_17.merge(Hg0_Mawson_V3_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17_OW   = Hg0_V3_17_OW.drop(['_merge'], axis=1)
Hg0_V3_17_OW   = Hg0_V3_17_OW.merge(Hg0_Davis_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V4_17_OW   = Hg0_V4_17.merge(Hg0_MQIsl_V4_17,    how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V1_18_OW   = Hg0_V1_18.merge(Hg0_Davis_V1_18,    how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V2_18_OW   = Hg0_V2_18.merge(Hg0_Casey_V2_18,    how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18_OW   = Hg0_V3_18.merge(Hg0_Mawson_V3_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18_OW   = Hg0_V3_18_OW.drop(['_merge'], axis=1)
Hg0_V3_18_OW   = Hg0_V3_18_OW.merge(Hg0_Davis_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V4_18_OW   = Hg0_V4_18.merge(Hg0_MQIsl_V4_18,    how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

#------------------------------------------------------------------------------
# CALCULATE THE MEAN HG0

# Whole voyage
SIPEXII_Mean = np.mean(Hg0_SIPEXII['ng/m3'])
PCAN_Mean    = np.mean(Hg0_PCAN['ng/m3'])

V1_17_Mean   = np.mean(Hg0_V1_17['ng/m3'])
V2_17_Mean   = np.mean(Hg0_V2_17['ng/m3'])
V3_17_Mean   = np.mean(Hg0_V3_17['ng/m3'])
V4_17_Mean   = np.mean(Hg0_V4_17['ng/m3'])

V1_18_Mean   = np.mean(Hg0_V1_18['ng/m3'])
V2_18_Mean   = np.mean(Hg0_V2_18['ng/m3'])
V3_18M_Mean  = np.mean(Hg0_V3_18['ng/m3'])
V4_18_Mean   = np.mean(Hg0_V4_18['ng/m3'])

# On station/Sea ice
SIPEXII_Mean_S = np.mean(Hg0_SIPEXII_Ice['ng/m3'])
PCAN_Mean_S    = np.mean(Hg0_PCAN_Ice['ng/m3'])

V1_17_Mean_S   = np.mean(Hg0_Davis_V1_17['ng/m3'])
V2_17_Mean_S   = np.mean(Hg0_Casey_V2_17['ng/m3'])
V3_17_Mean_S   = np.mean(Hg0_V3_17_Ice['ng/m3'])
V4_17_Mean_S   = np.mean(Hg0_MQIsl_V4_17['ng/m3'])

V1_18_Mean_S   = np.mean(Hg0_Davis_V1_18['ng/m3'])
V2_18_Mean_S   = np.mean(Hg0_Casey_V2_18['ng/m3'])
V3_18_Mean_S   = np.mean(Hg0_V3_18_Ice['ng/m3'])
V4_18_Mean_S   = np.mean(Hg0_MQIsl_V4_18['ng/m3'])

# Open water
SIPEXII_Mean_OW = np.mean(Hg0_SIPEXII_OW['ng/m3'])
PCAN_Mean_OW    = np.mean(Hg0_PCAN_OW['ng/m3'])

V1_17_Mean_OW   = np.mean(Hg0_V1_17_OW['ng/m3'])
V2_17_Mean_OW   = np.mean(Hg0_V2_17_OW['ng/m3'])
V3_17_Mean_OW   = np.mean(Hg0_V3_17_OW['ng/m3'])
V4_17_Mean_OW   = np.mean(Hg0_V4_17_OW['ng/m3'])

V1_18_Mean_OW   = np.mean(Hg0_V1_18_OW['ng/m3'])
V2_18_Mean_OW   = np.mean(Hg0_V2_18_OW['ng/m3'])
V3_18_Mean_OW   = np.mean(Hg0_V3_18_OW['ng/m3'])
V4_18_Mean_OW   = np.mean(Hg0_V4_18_OW['ng/m3'])

#------------------------------------------------------------------------------
# PLOT HISTOGRAMS OF NORMALISED FREQUENCY Hg0

fig = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=3, 
                       figure=fig, 
                       width_ratios= [0.25, 0.25, 0.25],
                       height_ratios=[0.3, 0.3])

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])

w = 0.01
n1 = math.ceil((Hg0_V1_17['ng/m3'].max()       - Hg0_V1_17['ng/m3'].min())/w)
n2 = math.ceil((Hg0_Davis_V1_17['ng/m3'].max() - Hg0_Davis_V1_17['ng/m3'].min())/w)
n3 = math.ceil((Hg0_V1_17_OW['ng/m3'].max()    - Hg0_V1_17_OW['ng/m3'].min())/w)

# Plot the variables
#plt.hist(Hg0_V1_17['ng/m3'],       density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
plt.hist(Hg0_Davis_V1_17['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
plt.hist(Hg0_V1_17_OW['ng/m3'],    density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# Plot the mean Hg
point1 = [V1_17_Mean_S,  0]
point2 = [V1_17_Mean_S,  0.2]
point3 = [V1_17_Mean_OW, 0]
point4 = [V1_17_Mean_OW, 0.2]

x_S  = [point1[0], point2[0]]
y_S  = [point1[1], point2[1]]
x_OW = [point3[0], point4[0]]
y_OW = [point3[1], point4[1]]

plt.plot(x_S,  y_S,  c ='red')
plt.plot(x_OW, y_OW, c ='green')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_xlim(0,1.3)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax1.set_ylim(-0.1,6.5)

# Plot the axis labels
ax1.set_ylabel('Normalised Frequency', fontsize=12)
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper right', title='V1 (2017-18)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[0,1])

w = 0.01
n1 = math.ceil((Hg0_V2_17['ng/m3'].max()       - Hg0_V2_17['ng/m3'].min())/w)
n2 = math.ceil((Hg0_Casey_V2_17['ng/m3'].max() - Hg0_Casey_V2_17['ng/m3'].min())/w)
n3 = math.ceil((Hg0_V2_17_OW['ng/m3'].max()    - Hg0_V2_17_OW['ng/m3'].min())/w)

# Plot the variables
#plt.hist(Hg0_V2_17['ng/m3'],       density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
plt.hist(Hg0_Casey_V2_17['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
plt.hist(Hg0_V2_17_OW['ng/m3'],    density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# Plot the mean Hg
point1 = [V2_17_Mean_S,  0]
point2 = [V2_17_Mean_S,  0.2]
point3 = [V2_17_Mean_OW, 0]
point4 = [V2_17_Mean_OW, 0.2]

x_S  = [point1[0], point2[0]]
y_S  = [point1[1], point2[1]]
x_OW = [point3[0], point4[0]]
y_OW = [point3[1], point4[1]]

plt.plot(x_S,  y_S,  c ='red')
plt.plot(x_OW, y_OW, c ='green')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_xlim(0,1.1)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax1.set_ylim(-0.1,6.5)

# Plot the axis labels
#ax1.set_ylabel('Normalised Frequency', fontsize=12)
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper right', title='V2 (2017-18)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[0,2])

w = 0.01
n1 = math.ceil((Hg0_V3_17['ng/m3'].max()     - Hg0_V3_17['ng/m3'].min())/w)
n2 = math.ceil((Hg0_V3_17_Ice['ng/m3'].max() - Hg0_V3_17_Ice['ng/m3'].min())/w)
n3 = math.ceil((Hg0_V3_17_OW['ng/m3'].max()  - Hg0_V3_17_OW['ng/m3'].min())/w)

# Plot the variables
#plt.hist(Hg0_V3_17['ng/m3'],     density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
plt.hist(Hg0_V3_17_Ice['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
plt.hist(Hg0_V3_17_OW['ng/m3'],  density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# Plot the mean Hg
point1 = [V3_17_Mean_S,  0]
point2 = [V3_17_Mean_S,  0.2]
point3 = [V3_17_Mean_OW, 0]
point4 = [V3_17_Mean_OW, 0.2]

x_S  = [point1[0], point2[0]]
y_S  = [point1[1], point2[1]]
x_OW = [point3[0], point4[0]]
y_OW = [point3[1], point4[1]]

plt.plot(x_S,  y_S,  c ='red')
plt.plot(x_OW, y_OW, c ='green')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_xlim(0,2.0)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax1.set_ylim(-0.1,6.5)

# Plot the axis labels
#ax1.set_ylabel('Normalised Frequency', fontsize=12)
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper right', title='V3 (2017-18)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 4
# ax1 = plt.subplot(gs[0,3])

# w = 0.01
# n1 = math.ceil((Hg0_V4_17['ng/m3'].max()       - Hg0_V4_17['ng/m3'].min())/w)
# n2 = math.ceil((Hg0_MQIsl_V4_17['ng/m3'].max() - Hg0_MQIsl_V4_17['ng/m3'].min())/w)
# n3 = math.ceil((Hg0_V4_17_OW['ng/m3'].max()    - Hg0_V4_17_OW['ng/m3'].min())/w)

# # Plot the variables
# #plt.hist(Hg0_V4_17['ng/m3'],       density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
# plt.hist(Hg0_MQIsl_V4_17['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
# plt.hist(Hg0_V4_17_OW['ng/m3'],    density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# # Plot the mean Hg
# point1 = [V4_17_Mean_S,  0]
# point2 = [V4_17_Mean_S,  0.2]
# point3 = [V4_17_Mean_OW, 0]
# point4 = [V4_17_Mean_OW, 0.2]

# x_S  = [point1[0], point2[0]]
# y_S  = [point1[1], point2[1]]
# x_OW = [point3[0], point4[0]]
# y_OW = [point3[1], point4[1]]

# plt.plot(x_S,  y_S,  c ='red')
# plt.plot(x_OW, y_OW, c ='green')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.set_xlim(0,1.0)

# # Format y-axis 1
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax1.set_ylim(-0.1,6.5)

# # Plot the axis labels
# #ax1.set_ylabel('Normalised Frequency', fontsize=12)
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

# #Plot the legend and title
# #plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper right', title='V4 (2017-18)')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 5
ax1 = plt.subplot(gs[1,0])

w = 0.01
n1 = math.ceil((Hg0_V1_18['ng/m3'].max()       - Hg0_V1_18['ng/m3'].min())/w)
n2 = math.ceil((Hg0_Davis_V1_18['ng/m3'].max() - Hg0_Davis_V1_18['ng/m3'].min())/w)
n3 = math.ceil((Hg0_V1_18_OW['ng/m3'].max()    - Hg0_V1_18_OW['ng/m3'].min())/w)

# Plot the variables
#plt.hist(Hg0_V1_18['ng/m3'],       density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
plt.hist(Hg0_Davis_V1_18['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
plt.hist(Hg0_V1_18_OW['ng/m3'],    density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# Plot the mean Hg
point1 = [V1_18_Mean_S,  0]
point2 = [V1_18_Mean_S,  0.2]
point3 = [V1_18_Mean_OW, 0]
point4 = [V1_18_Mean_OW, 0.2]

x_S  = [point1[0], point2[0]]
y_S  = [point1[1], point2[1]]
x_OW = [point3[0], point4[0]]
y_OW = [point3[1], point4[1]]

plt.plot(x_S,  y_S,  c ='red')
plt.plot(x_OW, y_OW, c ='green')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_xlim(0,2.7)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax1.set_ylim(-0.1,6.5)

# Plot the axis labels
ax1.set_ylabel('Normalised Frequency', fontsize=12)
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper right', title='V1 (2018-19)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 6
ax1 = plt.subplot(gs[1,1])

w = 0.01
n1 = math.ceil((Hg0_V2_18['ng/m3'].max()       - Hg0_V2_18['ng/m3'].min())/w)
n2 = math.ceil((Hg0_Casey_V2_18['ng/m3'].max() - Hg0_Casey_V2_18['ng/m3'].min())/w)
n3 = math.ceil((Hg0_V2_18_OW['ng/m3'].max()    - Hg0_V2_18_OW['ng/m3'].min())/w)

# Plot the variables
#plt.hist(Hg0_V2_18['ng/m3'],       density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
plt.hist(Hg0_Casey_V2_18['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
plt.hist(Hg0_V2_18_OW['ng/m3'],    density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# Plot the mean Hg
point1 = [V2_18_Mean_S,  0]
point2 = [V2_18_Mean_S,  0.2]
point3 = [V2_18_Mean_OW, 0]
point4 = [V2_18_Mean_OW, 0.2]

x_S  = [point1[0], point2[0]]
y_S  = [point1[1], point2[1]]
x_OW = [point3[0], point4[0]]
y_OW = [point3[1], point4[1]]

plt.plot(x_S,  y_S,  c ='red')
plt.plot(x_OW, y_OW, c ='green')
# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_xlim(0,3.0)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax1.set_ylim(-0.1,6.5)

# Plot the axis labels
#ax1.set_ylabel('Normalised Frequency', fontsize=12)
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper right', title='V2 (2018-19)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 7
ax1 = plt.subplot(gs[1,2])

w = 0.01
n1 = math.ceil((Hg0_V3_18['ng/m3'].max()     - Hg0_V3_18['ng/m3'].min())/w)
n2 = math.ceil((Hg0_V3_18_Ice['ng/m3'].max() - Hg0_V3_18_Ice['ng/m3'].min())/w)
n3 = math.ceil((Hg0_V3_18_OW['ng/m3'].max()  - Hg0_V3_18_OW['ng/m3'].min())/w)

# Plot the variables
#plt.hist(Hg0_V3_18['ng/m3'],     density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
plt.hist(Hg0_V3_18_Ice['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
plt.hist(Hg0_V3_18_OW['ng/m3'],  density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# Plot the mean Hg
point1 = [V3_18_Mean_S,  0]
point2 = [V3_18_Mean_S,  0.2]
point3 = [V3_18_Mean_OW, 0]
point4 = [V3_18_Mean_OW, 0.2]

x_S  = [point1[0], point2[0]]
y_S  = [point1[1], point2[1]]
x_OW = [point3[0], point4[0]]
y_OW = [point3[1], point4[1]]

plt.plot(x_S,  y_S,  c ='red')
plt.plot(x_OW, y_OW, c ='green')
# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_xlim(0,1.8)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax1.set_ylim(-0.1,6.5)

# Plot the axis labels
#ax1.set_ylabel('Normalised Frequency', fontsize=12)
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
legend = ax1.legend(loc='upper right', title='V3 (2018-19)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 8
# ax1 = plt.subplot(gs[1,3])

# w = 0.01
# n1 = math.ceil((Hg0_V4_18['ng/m3'].max()       - Hg0_V4_18['ng/m3'].min())/w)
# n2 = math.ceil((Hg0_MQIsl_V4_18['ng/m3'].max() - Hg0_MQIsl_V4_18['ng/m3'].min())/w)
# n3 = math.ceil((Hg0_V4_18_OW['ng/m3'].max()    - Hg0_V4_18_OW['ng/m3'].min())/w)

# # Plot the variables
# #plt.hist(Hg0_V4_18['ng/m3'],       density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
# plt.hist(Hg0_MQIsl_V4_18['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
# plt.hist(Hg0_V4_18_OW['ng/m3'],    density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# # Plot the mean Hg
# point1 = [V4_18_Mean_S,  0]
# point2 = [V4_18_Mean_S,  0.2]
# point3 = [V4_18_Mean_OW, 0]
# point4 = [V4_18_Mean_OW, 0.2]

# x_S  = [point1[0], point2[0]]
# y_S  = [point1[1], point2[1]]
# x_OW = [point3[0], point4[0]]
# y_OW = [point3[1], point4[1]]

# plt.plot(x_S,  y_S,  c ='red')
# plt.plot(x_OW, y_OW, c ='green')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.set_xlim(0,2.0)

# # Format y-axis 1
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax1.set_ylim(-0.1,6.5)

# # Plot the axis labels
# #ax1.set_ylabel('Normalised Frequency', fontsize=12)
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

# #Plot the legend and title
# #plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper right', title='V4 (2018-19)')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 9
# ax1 = plt.subplot(gs[2,0])

# w = 0.01
# n1 = math.ceil((Hg0_SIPEXII['ng/m3'].max()     - Hg0_SIPEXII['ng/m3'].min())/w)
# n2 = math.ceil((Hg0_SIPEXII_Ice['ng/m3'].max() - Hg0_SIPEXII_Ice['ng/m3'].min())/w)
# n3 = math.ceil((Hg0_SIPEXII_OW['ng/m3'].max()  - Hg0_SIPEXII_OW['ng/m3'].min())/w)

# # Plot the variables
# #plt.hist(Hg0_SIPEXII['ng/m3'],     density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
# plt.hist(Hg0_SIPEXII_Ice['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
# plt.hist(Hg0_SIPEXII_OW['ng/m3'],  density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# # Plot the mean Hg
# point1 = [SIPEXII_Mean_S,  0]
# point2 = [SIPEXII_Mean_S,  0.2]
# point3 = [SIPEXII_Mean_OW, 0]
# point4 = [SIPEXII_Mean_OW, 0.2]

# x_S  = [point1[0], point2[0]]
# y_S  = [point1[1], point2[1]]
# x_OW = [point3[0], point4[0]]
# y_OW = [point3[1], point4[1]]

# plt.plot(x_S,  y_S,  c ='red')
# plt.plot(x_OW, y_OW, c ='green')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.set_xlim(0,3.5)

# # Format y-axis 1
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax1.set_ylim(-0.1,6.5)

# # Plot the axis labels
# ax1.set_ylabel('Normalised Frequency', fontsize=12)
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

# #Plot the legend and title
# #plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper right', title='SIPEXII (2012)')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 10
# ax1 = plt.subplot(gs[2,2])

# w = 0.01
# n1 = math.ceil((Hg0_PCAN['ng/m3'].max()     - Hg0_PCAN['ng/m3'].min())/w)
# n2 = math.ceil((Hg0_PCAN_Ice['ng/m3'].max() - Hg0_PCAN_Ice['ng/m3'].min())/w)
# n3 = math.ceil((Hg0_PCAN_OW['ng/m3'].max()  - Hg0_PCAN_OW['ng/m3'].min())/w)

# # Plot the variables
# #plt.hist(Hg0_PCAN['ng/m3'],     density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Whole Voyage')
# plt.hist(Hg0_PCAN_Ice['ng/m3'], density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='_nolegend_')
# plt.hist(Hg0_PCAN_OW['ng/m3'],  density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='_nolegend_')

# # Plot the mean Hg
# point1 = [PCAN_Mean_S,  0]
# point2 = [PCAN_Mean_S,  0.2]
# point3 = [PCAN_Mean_OW, 0]
# point4 = [PCAN_Mean_OW, 0.2]

# x_S  = [point1[0], point2[0]]
# y_S  = [point1[1], point2[1]]
# x_OW = [point3[0], point4[0]]
# y_OW = [point3[1], point4[1]]

# plt.plot(x_S,  y_S,  c ='red')
# plt.plot(x_OW, y_OW, c ='green')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.set_xlim(0,1.2)

# # Format y-axis 1
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax1.set_ylim(-0.1,6.5)

# # Plot the axis labels
# ax1.set_ylabel('Normalised Frequency', fontsize=12)
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)

# #Plot the legend and title
# #plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper right', title='PCAN (2017)')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Custom Legend
custom_lines = [Line2D([0], [0], color='red',   lw=4),
                Line2D([0], [0], color='green', lw=4)]
fig.legend(custom_lines, ['Sea Ice', 'Open Ocean'], loc='upper left', bbox_to_anchor=(0.775, 0.275))
