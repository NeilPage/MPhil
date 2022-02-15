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
Hg0_V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_QAQC_17-18.csv', index_col=0)
Hg0_V4_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V4_Hg0_QAQC_17-18.csv', index_col=0)

Hg0_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_QAQC_18-19.csv', index_col=0)
Hg0_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_QAQC_18-19.csv', index_col=0)
Hg0_V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_QAQC_18-19.csv', index_col=0)
Hg0_V4_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V4_Hg0_QAQC_18-19.csv', index_col=0)

Hg0_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_QAQC_2012.csv', index_col=0)
Hg0_PCAN    = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/PCAN_Hg0_QAQC_2017.csv', index_col=0)

#--------------
# Met
#--------------
Met_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V1_17_underway_60.csv', index_col=0)
Met_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V2_17_underway_60.csv', index_col=0)
Met_V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V3_17_underway_60.csv', index_col=0)
Met_V4_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V4_17_underway_60.csv', index_col=0)

Met_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V1_18_underway_60.csv', index_col=0) 
Met_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V2_18_underway_60.csv', index_col=0)
Met_V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V3_18_underway_60.csv', index_col=0) 
Met_V4_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V4_18_underway_60.csv', index_col=0)

Met_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/ShipTrack/SIPEXII_underway_60.csv', index_col=0) 
Met_PCAN    = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/ShipTrack/PCAN_underway_60.csv', index_col=0) 

#------------------------------------------------------------------------------
# SET THE DATE

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

#--------------
# Met
#--------------
Met_V1_17.index   = (pd.to_datetime(Met_V1_17.index,   dayfirst=True) + timedelta(hours=7))  # Davis timezone is UT+7
Met_V2_17.index   = (pd.to_datetime(Met_V2_17.index,   dayfirst=True) + timedelta(hours=8))  # Casey timezone is UT+8
Met_V3_17.index   = (pd.to_datetime(Met_V3_17.index,   dayfirst=True) + timedelta(hours=5))  # Mawson timezone is UT+5
Met_V4_17.index   = (pd.to_datetime(Met_V4_17.index,   dayfirst=True) + timedelta(hours=11)) # Macquarie Island timezone is UT+11

Met_V1_18.index   = (pd.to_datetime(Met_V1_18.index,   dayfirst=True) + timedelta(hours=7))  # Davis timezone is UT+7
Met_V2_18.index   = (pd.to_datetime(Met_V2_18.index,   dayfirst=True) + timedelta(hours=8))  # Casey timezone is UT+8
Met_V3_18.index   = (pd.to_datetime(Met_V3_18.index,   dayfirst=True) + timedelta(hours=5))  # Mawson timezone is UT+5
Met_V4_18.index   = (pd.to_datetime(Met_V4_18.index,   dayfirst=True) + timedelta(hours=11)) # Macquarie Island timezone is UT+11

Met_SIPEXII.index = (pd.to_datetime(Met_SIPEXII.index, dayfirst=True) + timedelta(hours=8))  # SIPEXII timezone is UT+8
Met_PCAN.index    = (pd.to_datetime(Met_PCAN.index,    dayfirst=True) + timedelta(hours=8))  # PCAN timezone is UT+8

#------------------------------------------------------------------------------
# PASSIVATION ISSUE WITH CELL A ON VOYAGES V3_18 and V4_18 (FILTER DATA)

Filter1   = Hg0_V3_18['Cart'] == "B"
Hg0_V3_18 = Hg0_V3_18[Filter1]

Filter3    = Hg0_V4_18['Cart'] == "B"
Hg0_V4_18  = Hg0_V4_18[Filter3]

#------------------------------------------------------------------------------
# RESAMPLE THE Hg0 AND MET DATASETS TO 1-HOUR TIME RESOLUTION

#--------------
# Hg0
#--------------
Hg0_V1_17   = Hg0_V1_17.resample('60T').mean()
Hg0_V2_17   = Hg0_V2_17.resample('60T').mean()
Hg0_V3_17   = Hg0_V3_17.resample('60T').mean()
Hg0_V4_17   = Hg0_V4_17.resample('60T').mean()

Hg0_V1_18   = Hg0_V1_18.resample('60T').mean()
Hg0_V2_18   = Hg0_V2_18.resample('60T').mean()
Hg0_V3_18   = Hg0_V3_18.resample('60T').mean()
Hg0_V4_18   = Hg0_V4_18.resample('60T').mean()

Hg0_SIPEXII = Hg0_SIPEXII.resample('60T').mean()
Hg0_PCAN    = Hg0_PCAN.resample('60T').mean()

#--------------
# Met
#--------------
Met_V1_17   = Met_V1_17.resample('60T').mean()
Met_V2_17   = Met_V2_17.resample('60T').mean()
Met_V3_17   = Met_V3_17.resample('60T').mean()
Met_V4_17   = Met_V4_17.resample('60T').mean()

Met_V1_18   = Met_V1_18.resample('60T').mean()
Met_V2_18   = Met_V2_18.resample('60T').mean()
Met_V3_18   = Met_V3_18.resample('60T').mean()
Met_V4_18   = Met_V4_18.resample('60T').mean()

Met_SIPEXII = Met_SIPEXII.resample('60T').mean()
Met_PCAN    = Met_PCAN.resample('60T').mean()

#------------------------------------------------------------------------------
# COMBINE THE Hg0 AND MET DATAFRAMES

# Combine dataframes
Hg0_V1_17   = pd.concat([Hg0_V1_17,   Met_V1_17],   axis=1, join='inner')
Hg0_V2_17   = pd.concat([Hg0_V2_17,   Met_V2_17],   axis=1, join='inner')
Hg0_V3_17   = pd.concat([Hg0_V3_17,   Met_V3_17],   axis=1, join='inner')
Hg0_V4_17   = pd.concat([Hg0_V4_17,   Met_V4_17],   axis=1, join='inner')

Hg0_V1_18   = pd.concat([Hg0_V1_18,   Met_V1_18],   axis=1, join='inner')
Hg0_V2_18   = pd.concat([Hg0_V2_18,   Met_V2_18],   axis=1, join='inner')
Hg0_V3_18   = pd.concat([Hg0_V3_18,   Met_V3_18],   axis=1, join='inner')
Hg0_V4_18   = pd.concat([Hg0_V4_18,   Met_V4_18],   axis=1, join='inner')

Hg0_SIPEXII = pd.concat([Hg0_SIPEXII, Met_SIPEXII], axis=1, join='inner')
Hg0_PCAN    = pd.concat([Hg0_PCAN,    Met_PCAN],    axis=1, join='inner')

#------------------------------------------------------------------------------
# ROUND THE LATITUDE TO NEAREST DEGREE

Hg0_V1_17['rounded_lat']   = Hg0_V1_17['latitude'].apply(round, ndigits=0)
Hg0_V2_17['rounded_lat']   = Hg0_V2_17['latitude'].apply(round, ndigits=0)
Hg0_V3_17['rounded_lat']   = Hg0_V3_17['latitude'].apply(round, ndigits=0)
Hg0_V4_17['rounded_lat']   = Hg0_V4_17['latitude'].apply(round, ndigits=0)

Hg0_V1_18['rounded_lat']   = Hg0_V1_18['latitude'].apply(round, ndigits=0)
Hg0_V2_18['rounded_lat']   = Hg0_V2_18['latitude'].apply(round, ndigits=0)
Hg0_V3_18['rounded_lat']   = Hg0_V3_18['latitude'].apply(round, ndigits=0)
Hg0_V4_18['rounded_lat']   = Hg0_V4_18['latitude'].apply(round, ndigits=0)

Hg0_SIPEXII['rounded_lat'] = Hg0_SIPEXII['latitude'].apply(round, ndigits=0)
Hg0_PCAN['rounded_lat']    = Hg0_PCAN['latitude'].apply(round, ndigits=0)

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL MEAN

Mean_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').mean()
Mean_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').mean()
Mean_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').mean()
Mean_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').mean()

Mean_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').mean()
Mean_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').mean()
Mean_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').mean()
Mean_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').mean()

Mean_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').mean()
Mean_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').mean()

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL MEDIAN

Median_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').median()
Median_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').median()
Median_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').median()
Median_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').median()

Median_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').median()
Median_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').median()
Median_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').median()
Median_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').median()

Median_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').median()
Median_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').median()

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL ST DEV

std_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').std()
std_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').std()
std_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').std()
std_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').std()

std_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').std()
std_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').std()
std_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').std()
std_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').std()

std_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').std()
std_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').std()

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL MEAN

Mean_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').mean()
Mean_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').mean()
Mean_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').mean()
Mean_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').mean()

Mean_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').mean()
Mean_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').mean()
Mean_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').mean()
Mean_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').mean()

Mean_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').mean()
Mean_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').mean()

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL MAX

MAX_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').max()
MAX_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').max()
MAX_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').max()
MAX_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').max()

MAX_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').max()
MAX_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').max()
MAX_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').max()
MAX_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').max()

MAX_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').max()
MAX_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').max()

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL MIN

MIN_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').min()
MIN_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').min()
MIN_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').min()
MIN_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').min()

MIN_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').min()
MIN_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').min()
MIN_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').min()
MIN_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').min()

MIN_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').min()
MIN_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').min()

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL 5th PERCENTILE

P5_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').quantile(q=0.05)
P5_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').quantile(q=0.05)
P5_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').quantile(q=0.05)
P5_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').quantile(q=0.05)

P5_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').quantile(q=0.05)
P5_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').quantile(q=0.05)
P5_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').quantile(q=0.05)
P5_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').quantile(q=0.05)

P5_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').quantile(q=0.05)
P5_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').quantile(q=0.05)

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL 25th PERCENTILE

P25_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').quantile(q=0.25)
P25_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').quantile(q=0.25)
P25_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').quantile(q=0.25)
P25_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').quantile(q=0.25)

P25_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').quantile(q=0.25)
P25_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').quantile(q=0.25)
P25_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').quantile(q=0.25)
P25_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').quantile(q=0.25)

P25_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').quantile(q=0.25)
P25_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').quantile(q=0.25)

#------------------------------------------------------------------------------
# FIND THE LATITUDINAL 75th PERCENTILE

P75_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').quantile(q=0.75)
P75_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').quantile(q=0.75)
P75_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').quantile(q=0.75)
P75_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').quantile(q=0.75)

P75_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').quantile(q=0.75)
P75_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').quantile(q=0.75)
P75_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').quantile(q=0.75)
P75_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').quantile(q=0.75)

P75_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').quantile(q=0.75)
P75_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').quantile(q=0.75)
#------------------------------------------------------------------------------
# FIND THE LATITUDINAL 95th PERCENTILE

P95_Hg0_V1_17   = Hg0_V1_17.groupby('rounded_lat').quantile(q=0.95)
P95_Hg0_V2_17   = Hg0_V2_17.groupby('rounded_lat').quantile(q=0.95)
P95_Hg0_V3_17   = Hg0_V3_17.groupby('rounded_lat').quantile(q=0.95)
P95_Hg0_V4_17   = Hg0_V4_17.groupby('rounded_lat').quantile(q=0.95)

P95_Hg0_V1_18   = Hg0_V1_18.groupby('rounded_lat').quantile(q=0.95)
P95_Hg0_V2_18   = Hg0_V2_18.groupby('rounded_lat').quantile(q=0.95)
P95_Hg0_V3_18   = Hg0_V3_18.groupby('rounded_lat').quantile(q=0.95)
P95_Hg0_V4_18   = Hg0_V4_18.groupby('rounded_lat').quantile(q=0.95)

P95_Hg0_SIPEXII = Hg0_SIPEXII.groupby('rounded_lat').quantile(q=0.95)
P95_Hg0_PCAN    = Hg0_PCAN.groupby('rounded_lat').quantile(q=0.95)

#------------------------------------------------------------------------------
# FIND THE MAX Hg0 CONCENTRATION & LATITUDE

# Hg0
V1_17_MAX   = MAX_Hg0_V1_17['ng/m3'].max()
V2_17_MAX   = MAX_Hg0_V2_17['ng/m3'].max()
V3_17_MAX   = MAX_Hg0_V3_17['ng/m3'].max()
V4_17_MAX   = MAX_Hg0_V4_17['ng/m3'].max()

V1_18_MAX   = MAX_Hg0_V1_18['ng/m3'].max()
V2_18_MAX   = MAX_Hg0_V2_18['ng/m3'].max()
V3_18_MAX   = MAX_Hg0_V3_18['ng/m3'].max()
V4_18_MAX   = MAX_Hg0_V4_18['ng/m3'].max()

SIPEXII_MAX = MAX_Hg0_SIPEXII['ng/m3'].max()
PCAN_MAX    = MAX_Hg0_PCAN['ng/m3'].max()

# Latitude
V1_17_MAX_index   = MAX_Hg0_V1_17['ng/m3'].idxmax()
V2_17_MAX_index   = MAX_Hg0_V2_17['ng/m3'].idxmax()
V3_17_MAX_index   = MAX_Hg0_V3_17['ng/m3'].idxmax()
V4_17_MAX_index   = MAX_Hg0_V4_17['ng/m3'].idxmax()

V1_18_MAX_index   = MAX_Hg0_V1_18['ng/m3'].idxmax()
V2_18_MAX_index   = MAX_Hg0_V2_18['ng/m3'].idxmax()
V3_18_MAX_index   = MAX_Hg0_V3_18['ng/m3'].idxmax()
V4_18_MAX_index   = MAX_Hg0_V4_18['ng/m3'].idxmax()

SIPEXII_MAX_index = MAX_Hg0_SIPEXII['ng/m3'].idxmax()
PCAN_MAX_index    = MAX_Hg0_PCAN['ng/m3'].idxmax()

# #------------------------------------------------------------------------------
# # PLOT THE GRAPH

# fig1 = plt.figure()

# gs = gridspec.GridSpec(nrows=2,
#                        ncols=5, 
#                        figure=fig1, 
#                        width_ratios= [0.5, 0.5, 0.5, 0.5, 0.5],
#                        height_ratios=[0.25, 0.25])

# #-----------------------------
# # Graph 1
# ax1 = plt.subplot(gs[0,0])

# # Plot the variables
# ax1.plot(Hg0_V1_17['ng/m3'], Hg0_V1_17['latitude'], marker='x', markersize = 1.0, ls='None', c='blue', label ='V1 (2017-18)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)
# #ax1.axes.get_xaxis().set_visible(False)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 2
# ax1 = plt.subplot(gs[0,1])

# # Plot the variables
# ax1.plot(Hg0_V2_17['ng/m3'], Hg0_V2_17['latitude'], marker='x', markersize = 1.0, ls='None', c='blue', label ='V2 (2017-18)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 3
# ax1 = plt.subplot(gs[0,2])

# # Plot the variables
# ax1.plot(Hg0_V3_17['ng/m3'], Hg0_V3_17['latitude'], marker='x', markersize = 1.0, ls='None', c='blue', label ='V3 (2017-18)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 4
# ax1 = plt.subplot(gs[0,3])

# # Plot the variables
# ax1.plot(Hg0_V4_17['ng/m3'], Hg0_V4_17['latitude'], marker='x', markersize = 1.0, ls='None', c='blue', label ='V4 (2017-18)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 5
# ax1 = plt.subplot(gs[1,0])

# # Plot the variables
# ax1.plot(Hg0_V1_18['ng/m3'], Hg0_V1_18['latitude'], marker='x', markersize = 1.0, ls='None', c='red', label ='V1 (2018-19)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 6
# ax1 = plt.subplot(gs[1,1])

# # Plot the variables
# ax1.plot(Hg0_V2_18['ng/m3'], Hg0_V2_18['latitude'], marker='x', markersize = 1.0, ls='None', c='red', label ='V2 (2018-19)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# #ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 7
# ax1 = plt.subplot(gs[1,2])

# # Plot the variables
# ax1.plot(Hg0_V3_18['ng/m3'], Hg0_V3_18['latitude'], marker='x', markersize = 1.0, ls='None', c='red', label ='V3 (2018-19)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 8
# ax1 = plt.subplot(gs[1,3])

# # Plot the variables
# ax1.plot(Hg0_V4_18['ng/m3'], Hg0_V4_18['latitude'], marker='x', markersize = 1.0, ls='None', c='red', label ='V4 (2018-19)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 9
# ax1 = plt.subplot(gs[0,4])

# # Plot the variables
# ax1.plot(Hg0_SIPEXII['ng/m3'], Hg0_SIPEXII['latitude'], marker='x', markersize = 1.0, ls='None', c='green', label ='SIPEXII (2012)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# #-----------------------------
# # Graph 10
# ax1 = plt.subplot(gs[1,4])

# # Plot the variables
# ax1.plot(Hg0_PCAN['ng/m3'], Hg0_PCAN['latitude'], marker='x', markersize = 1.0, ls='None', c='orange', label ='PCAN (2017)')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# #Plot the legend and title
# #plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)



# #------------------------------------------------------------------------------
# # PLOT THE GRAPH

# fig3 = plt.figure()

# gs = gridspec.GridSpec(nrows=2,
#                        ncols=5, 
#                        figure=fig3, 
#                        width_ratios= [0.5, 0.5, 0.5, 0.5, 0.5],
#                        height_ratios=[0.25, 0.25])

# #-----------------------------
# # Graph 1
# ax1 = plt.subplot(gs[0,0])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_V1_17['ng/m3'], Median_Hg0_V1_17['latitude'],   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=std_Hg0_V1_17['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_V1_17.index, MIN_Hg0_V1_17['ng/m3'], MAX_Hg0_V1_17['ng/m3'], facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(V1_17_MAX, V1_17_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)
# #ax1.axes.get_xaxis().set_visible(False)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(V1_17_MAX))+' ng/m$^3$'], loc='upper right', title='V1 (2017-18)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 2
# ax1 = plt.subplot(gs[0,1])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_V2_17['ng/m3'], Median_Hg0_V2_17['latitude'],   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=std_Hg0_V2_17['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_V2_17.index, MIN_Hg0_V2_17['ng/m3'], MAX_Hg0_V2_17['ng/m3'], facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(V2_17_MAX, V2_17_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(V2_17_MAX))+' ng/m$^3$'], loc='upper right', title='V2 (2017-18)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 3
# ax1 = plt.subplot(gs[0,2])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_V3_17['ng/m3'], Median_Hg0_V3_17['latitude'],   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=std_Hg0_V3_17['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_V3_17.index, MIN_Hg0_V3_17['ng/m3'], MAX_Hg0_V3_17['ng/m3'], facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(V3_17_MAX, V3_17_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(V3_17_MAX))+' ng/m$^3$'], loc='upper right', title='V3 (2017-18)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 4
# ax1 = plt.subplot(gs[0,3])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_V4_17['ng/m3'], Median_Hg0_V4_17['latitude'],   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=std_Hg0_V4_17['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_V4_17.index, MIN_Hg0_V4_17['ng/m3'], MAX_Hg0_V4_17['ng/m3'], facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(V4_17_MAX, V4_17_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(V4_17_MAX))+' ng/m$^3$'], loc='upper right', title='V4 (2017-18)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 5
# ax1 = plt.subplot(gs[1,0])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_V1_18['ng/m3'], Median_Hg0_V1_18['latitude'],   marker='o', c='red',  markersize = 3.0, ls='-', xerr=std_Hg0_V1_17['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_V1_18.index, MIN_Hg0_V1_18['ng/m3'], MAX_Hg0_V1_18['ng/m3'], facecolor='red', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(V1_18_MAX, V1_18_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(V1_18_MAX))+' ng/m$^3$'], loc='upper right', title='V1 (2018-19)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 6
# ax1 = plt.subplot(gs[1,1])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_V2_18['ng/m3'], Median_Hg0_V2_18['latitude'],   marker='o', c='red',  markersize = 3.0, ls='-', xerr=std_Hg0_V2_18['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_V2_18.index, MIN_Hg0_V2_18['ng/m3'], MAX_Hg0_V2_18['ng/m3'], facecolor='red', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(V2_18_MAX, V2_18_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(V2_18_MAX))+' ng/m$^3$'], loc='upper right', title='V2 (2018-19)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 7
# ax1 = plt.subplot(gs[1,2])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_V3_18['ng/m3'], Median_Hg0_V3_18['latitude'],   marker='o', c='red',  markersize = 3.0, ls='-', xerr=std_Hg0_V3_18['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_V3_18.index, MIN_Hg0_V3_18['ng/m3'], MAX_Hg0_V3_18['ng/m3'], facecolor='red', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(V3_18_MAX, V3_18_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(V3_18_MAX))+' ng/m$^3$'], loc='upper right', title='V3 (2018-19)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 8
# ax1 = plt.subplot(gs[1,3])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_V4_18['ng/m3'], Median_Hg0_V4_18['latitude'],   marker='o', c='red',  markersize = 3.0, ls='-', xerr=std_Hg0_V4_18['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_V4_18.index, MIN_Hg0_V4_18['ng/m3'], MAX_Hg0_V4_18['ng/m3'], facecolor='red', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(V4_18_MAX, V4_18_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(V4_18_MAX))+' ng/m$^3$'], loc='upper right', title='V4 (2018-19)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 9
# ax1 = plt.subplot(gs[0,4])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_SIPEXII['ng/m3'], Median_Hg0_SIPEXII['latitude'],   marker='o', c='green',  markersize = 3.0, ls='-', xerr=std_Hg0_SIPEXII['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_SIPEXII.index, MIN_Hg0_SIPEXII['ng/m3'], MAX_Hg0_SIPEXII['ng/m3'], facecolor='green', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(SIPEXII_MAX, SIPEXII_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# #ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(SIPEXII_MAX))+' ng/m$^3$'], loc='upper left', title='SIPEXII (2012)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

# #-----------------------------
# # Graph 10
# ax1 = plt.subplot(gs[1,4])

# # Plot Hg0 latitudinal profile
# Line_Med = ax1.errorbar(Median_Hg0_PCAN['ng/m3'], Median_Hg0_PCAN['latitude'],   marker='o', c='orange',  markersize = 3.0, ls='-', xerr=std_Hg0_PCAN['ng/m3'], capsize=2)
# Line_Ran = ax1.fill_betweenx(MIN_Hg0_PCAN.index, MIN_Hg0_PCAN['ng/m3'], MAX_Hg0_PCAN['ng/m3'], facecolor='orange', alpha=0.3, interpolate=False) # fill the distribution
# Star_Max = ax1.scatter(PCAN_MAX, PCAN_MAX_index, c ='black', marker='*')

# # Format x-axis
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.xaxis.label.set_color('black')
# ax1.tick_params(axis='x', which='both', colors='black')
# ax1.set_xlim(0,2.0)

# # Format y-axis
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax1.yaxis.label.set_color('black')
# ax1.tick_params(axis='y', which='both', colors='black')
# ax1.set_ylim(-70,-39)

# # Plot the axis labels
# ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
# #ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

# # adjust the axis labels and ticks
# legend = ax1.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max Hg$^0$:'+str("%5.2f"%(PCAN_MAX))+' ng/m$^3$'], loc='upper right', title='PCAN (2017)', fontsize=10)
# legend.get_frame().set_facecolor('grey')
# legend.get_frame().set_alpha(0.9)
# legend.get_title().set_fontsize(12)

#------------------------------------------------------------------------------
# PLOT THE GRAPH

fig2 = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=5, 
                       figure=fig2, 
                       width_ratios= [0.5, 0.5, 0.5, 0.5, 0.5],
                       height_ratios=[0.25, 0.25])

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_V1_17['ng/m3'], MIN_Hg0_V1_17.index, marker='None', ls='-', c='black', label ='V1 (2017-18)')

# Plot the percentiles
ax1.plot(MIN_Hg0_V1_17['ng/m3'], MIN_Hg0_V1_17.index, ls='-', c='blue',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_V1_17['ng/m3'], MAX_Hg0_V1_17.index, ls='-', c='blue',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_V1_17.index, P25_Hg0_V1_17['ng/m3'], P75_Hg0_V1_17['ng/m3'], facecolor='blue', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(V1_17_MAX, V1_17_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.50, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)
#ax1.axes.get_xaxis().set_visible(False)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(V1_17_MAX))+' ng/m$^3$'], loc='upper right', title='V1 (2017-18)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[0,1])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_V2_17['ng/m3'], MIN_Hg0_V2_17.index, marker='None', ls='-', c='black', label ='V2 (2017-18)')

# Plot the percentiles
ax1.plot(MIN_Hg0_V2_17['ng/m3'], MIN_Hg0_V2_17.index, ls='-', c='blue',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_V2_17['ng/m3'], MAX_Hg0_V2_17.index, ls='-', c='blue',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_V2_17.index, P25_Hg0_V2_17['ng/m3'], P75_Hg0_V2_17['ng/m3'], facecolor='blue', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(V2_17_MAX, V2_17_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.57, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(V2_17_MAX))+' ng/m$^3$'], loc='upper right', title='V2 (2017-18)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[0,2])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_V3_17['ng/m3'], MIN_Hg0_V3_17.index, marker='None', ls='-', c='black', label ='V3 (2017-18)')

# Plot the percentiles
ax1.plot(MIN_Hg0_V3_17['ng/m3'], MIN_Hg0_V3_17.index, ls='-', c='blue',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_V3_17['ng/m3'], MAX_Hg0_V3_17.index, ls='-', c='blue',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_V3_17.index, P25_Hg0_V3_17['ng/m3'], P75_Hg0_V3_17['ng/m3'], facecolor='blue', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(V3_17_MAX, V3_17_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.49, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(V3_17_MAX))+' ng/m$^3$'], loc='upper right', title='V3 (2017-18)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 4
ax1 = plt.subplot(gs[0,3])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_V4_17['ng/m3'], MIN_Hg0_V4_17.index, marker='None', ls='-', c='black', label ='V4 (2017-18)')

# Plot the percentiles
ax1.plot(MIN_Hg0_V4_17['ng/m3'], MIN_Hg0_V4_17.index, ls='-', c='blue',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_V4_17['ng/m3'], MAX_Hg0_V4_17.index, ls='-', c='blue',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_V4_17.index, P25_Hg0_V4_17['ng/m3'], P75_Hg0_V4_17['ng/m3'], facecolor='blue', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(V4_17_MAX, V4_17_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.36, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(V4_17_MAX))+' ng/m$^3$'], loc='upper right', title='V4 (2017-18)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 5
ax1 = plt.subplot(gs[1,0])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_V1_18['ng/m3'], MIN_Hg0_V1_18.index, marker='None', ls='-', c='black', label ='V1 (2018-19)')

# Plot the percentiles
ax1.plot(MIN_Hg0_V1_18['ng/m3'], MIN_Hg0_V1_18.index, ls='-', c='red',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_V1_18['ng/m3'], MAX_Hg0_V1_18.index, ls='-', c='red',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_V1_18.index, P25_Hg0_V1_18['ng/m3'], P75_Hg0_V1_18['ng/m3'], facecolor='red', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(V1_18_MAX, V1_18_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.74, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(V1_18_MAX))+' ng/m$^3$'], loc='upper right', title='V1 (2018-19)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 6
ax1 = plt.subplot(gs[1,1])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_V2_18['ng/m3'], MIN_Hg0_V2_18.index, marker='None', ls='-', c='black', label ='V2 (2018-19)')

# Plot the percentiles
ax1.plot(MIN_Hg0_V2_18['ng/m3'], MIN_Hg0_V2_18.index, ls='-', c='red',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_V2_18['ng/m3'], MAX_Hg0_V2_18.index, ls='-', c='red',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_V2_18.index, P25_Hg0_V2_18['ng/m3'], P75_Hg0_V2_18['ng/m3'], facecolor='red', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(V2_18_MAX, V2_18_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.69, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(V2_18_MAX))+' ng/m$^3$'], loc='upper right', bbox_to_anchor=(0.992, 0.7), title='V2 (2018-19)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 7
ax1 = plt.subplot(gs[1,2])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_V3_18['ng/m3'], MIN_Hg0_V3_18.index, marker='None', ls='-', c='black', label ='V3 (2018-19)')

# Plot the percentiles
ax1.plot(MIN_Hg0_V3_18['ng/m3'], MIN_Hg0_V3_18.index, ls='-', c='red',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_V3_18['ng/m3'], MAX_Hg0_V3_18.index, ls='-', c='red',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_V3_18.index, P25_Hg0_V3_18['ng/m3'], P75_Hg0_V3_18['ng/m3'], facecolor='red', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(V3_18_MAX, V3_18_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.60, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(V3_18_MAX))+' ng/m$^3$'], loc='upper right', title='V3 (2018-19)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 8
ax1 = plt.subplot(gs[1,3])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_V4_18['ng/m3'], MIN_Hg0_V4_18.index, marker='None', ls='-', c='black', label ='V4 (2018-19)')

# Plot the percentiles
ax1.plot(MIN_Hg0_V4_18['ng/m3'], MIN_Hg0_V4_18.index, ls='-', c='red',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_V4_18['ng/m3'], MAX_Hg0_V4_18.index, ls='-', c='red',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_V4_18.index, P25_Hg0_V4_18['ng/m3'], P75_Hg0_V4_18['ng/m3'], facecolor='red', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(V4_18_MAX, V4_18_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.52, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(V4_18_MAX))+' ng/m$^3$'], loc='upper right', title='V4 (2018-19)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 9
ax1 = plt.subplot(gs[0,4])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_SIPEXII['ng/m3'], MIN_Hg0_SIPEXII.index, marker='None', ls='-', c='black', label ='SIPEXII (2012)')

# Plot the percentiles
ax1.plot(MIN_Hg0_SIPEXII['ng/m3'], MIN_Hg0_SIPEXII.index, ls='-', c='green',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_SIPEXII['ng/m3'], MAX_Hg0_SIPEXII.index, ls='-', c='green',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_SIPEXII.index, P25_Hg0_SIPEXII['ng/m3'], P75_Hg0_SIPEXII['ng/m3'], facecolor='green', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(SIPEXII_MAX, SIPEXII_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(1.07, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
#ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(SIPEXII_MAX))+' ng/m$^3$'], loc='upper left', title='SIPEXII (2012)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)

#-----------------------------
# Graph 10
ax1 = plt.subplot(gs[1,4])

# Plot the median
Line_Med = ax1.plot(Median_Hg0_PCAN['ng/m3'], MIN_Hg0_PCAN.index, marker='None', ls='-', c='black', label ='PCAN (2017)')

# Plot the percentiles
ax1.plot(MIN_Hg0_PCAN['ng/m3'], MIN_Hg0_PCAN.index, ls='-', c='orange',  linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(MAX_Hg0_PCAN['ng/m3'], MAX_Hg0_PCAN.index, ls='-', c='orange',  linewidth=1, alpha=0.5, label='_nolegend_')
Line_Ran = ax1.fill_betweenx(P25_Hg0_PCAN.index, P25_Hg0_PCAN['ng/m3'], P75_Hg0_PCAN['ng/m3'], facecolor='orange', alpha=0.7) # fill the distribution
Star_Max = ax1.scatter(PCAN_MAX, PCAN_MAX_index, c ='black', marker='*')

# Plot vertical line for median Hg0
ax1.axvline(0.56, linewidth=1.0, color='k', ls='--')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.xaxis.label.set_color('black')
ax1.tick_params(axis='x', which='both', colors='black')
ax1.set_xlim(0,2.0)

# Format y-axis
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.label.set_color('black')
ax1.tick_params(axis='y', which='both', colors='black')
ax1.set_ylim(-70,-39)

# Plot the axis labels
ax1.set_xlabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_ylabel('Latitude ($^\circ$S)', fontsize=12, labelpad=-0.1)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
legend = ax1.legend([Star_Max], [str("%5.2f"%(PCAN_MAX))+' ng/m$^3$'], loc='upper right', title='PCAN (2017)', fontsize=10)
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)
legend.get_title().set_fontsize(10)