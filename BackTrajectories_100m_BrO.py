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
from scipy import stats
import math

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
import cmocean
import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

#--------------
# BrO
#--------------
BrO_V1_17   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv', index_col=0)       # BrO V1 (2017/18)
BrO_V2_17   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv', index_col=0)       # BrO V2 (2017/18)
BrO_V3_17   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv', index_col=0)       # BrO V3 (2017/18)

BrO_V1_18   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv', index_col=0)       # BrO V1 (2018/19)
BrO_V2_18   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv', index_col=0)       # BrO V2 (2018/19)
BrO_V3_18   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv', index_col=0)       # BrO V3 (2018/19)

BrO_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv', index_col=0) # BrO SIPEXII (2012)

#-------------
# Sea Ice
#-------------

SeaIce_V1_17   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20171114.nc', decode_cf=False, engine='netcdf4')
SeaIce_V2_17   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20171221.nc', decode_cf=False, engine='netcdf4')
SeaIce_V3_17M  = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20180201.nc', decode_cf=False, engine='netcdf4')
SeaIce_V3_17D  = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20180127.nc', decode_cf=False, engine='netcdf4')

SeaIce_V1_18   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20181107.nc', decode_cf=False, engine='netcdf4')
SeaIce_V2_18   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20181215.nc', decode_cf=False, engine='netcdf4')
SeaIce_V3_18M  = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20190130.nc', decode_cf=False, engine='netcdf4')
SeaIce_V3_18D  = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20190126.nc', decode_cf=False, engine='netcdf4')

SeaIce_SIPEXII = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2012/oisst-avhrr-v02r01.20120923.nc', decode_cf=False, engine='netcdf4')
SeaIce_PCAN    = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/Hamburg_ICDC/20170126_median5day.nc', decode_cf=False, engine='netcdf4')

#------------------------------------------------------------------------------
# FILTER THE BrO DATA FOR RELATIVE ERROR 

#--------------
# BrO
#--------------
# Calculate the Relative Error (>=0.6)
Filter1_BrO = BrO_V1_17['err_surf_vmr'] / BrO_V1_17['surf_vmr(ppmv)']
Filter2_BrO = BrO_V2_17['err_surf_vmr'] / BrO_V2_17['surf_vmr(ppmv)']
Filter3_BrO = BrO_V3_17['err_surf_vmr'] / BrO_V3_17['surf_vmr(ppmv)']

Filter4_BrO = BrO_V1_18['err_surf_vmr'] / BrO_V1_18['surf_vmr(ppmv)']
Filter5_BrO = BrO_V2_18['err_surf_vmr'] / BrO_V2_18['surf_vmr(ppmv)']
Filter6_BrO = BrO_V3_18['err_surf_vmr'] / BrO_V3_18['surf_vmr(ppmv)']

Filter7_BrO = BrO_SIPEXII['err_surf_vmr'] / BrO_SIPEXII['surf_vmr(ppmv)']

# Apply the filter
V1_17F      = Filter1_BrO < 0.6
BrO_V1_17   = BrO_V1_17[V1_17F]

V2_17F      = Filter2_BrO < 0.6
BrO_V2_17   = BrO_V2_17[V2_17F]

V3_17F      = Filter3_BrO < 0.6
BrO_V3_17   = BrO_V3_17[V3_17F]

V1_18F      = Filter4_BrO < 0.6
BrO_V1_18   = BrO_V1_18[V1_18F]

V2_18F      = Filter5_BrO < 0.6
BrO_V2_18   = BrO_V2_18[V2_18F]

V3_18F      = Filter6_BrO < 0.6
BrO_V3_18   = BrO_V3_18[V3_18F]

SIPEXIIF    = Filter7_BrO < 0.6
BrO_SIPEXII = BrO_SIPEXII[SIPEXIIF]

# Slit V3 into Mawson and Davis
BrO_V3_17M = BrO_V3_17
BrO_V3_17D = BrO_V3_17

BrO_V3_18M = BrO_V3_18
BrO_V3_18D = BrO_V3_18

#------------------------------------------------------------------------------
# Set the date

#--------------
# BrO
#--------------
BrO_V1_17.index   = (pd.to_datetime(BrO_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_17.index   = (pd.to_datetime(BrO_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_17M.index  = (pd.to_datetime(BrO_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_17D.index  = (pd.to_datetime(BrO_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_V1_18.index   = (pd.to_datetime(BrO_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_18.index   = (pd.to_datetime(BrO_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_18M.index  = (pd.to_datetime(BrO_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_18D.index  = (pd.to_datetime(BrO_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_SIPEXII.index = (pd.to_datetime(BrO_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#------------------------------------------------------------------------------
# RESAMPLE THE BrO DATASETS TO 1-HOUR TIME RESOLUTION

#--------------
# BrO
#--------------
BrO_V1_17   = BrO_V1_17.resample('60T').mean()
BrO_V2_17   = BrO_V2_17.resample('60T').mean()
BrO_V3_17M  = BrO_V3_17M.resample('60T').mean()
BrO_V3_17D  = BrO_V3_17D.resample('60T').mean()

BrO_V1_18   = BrO_V1_18.resample('60T').mean()
BrO_V2_18   = BrO_V2_18.resample('60T').mean()
BrO_V3_18M  = BrO_V3_18M.resample('60T').mean()
BrO_V3_18D  = BrO_V3_18D.resample('60T').mean()

BrO_SIPEXII = BrO_SIPEXII.resample('60T').mean()

#------------------------------------------------------------------------------
# BACK TRAJECTORIES CAMMPCAN (2017-18)

# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'
delta_one_hour = timedelta(hours=1)

#-------------
# V1_17
#-------------
# Set the start/end dates
start_V1_17a   = '2017111407'
end_V1_17a     = '2017112307'

start_date    = datetime.strptime(start_V1_17a, DATE_FORMAT)
end_date      = datetime.strptime(end_V1_17a,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V1_17)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V1_17 = pd.concat(Traj)

#-------------
# V2_17
#-------------
# Set the start/end dates   
start_V2_17a  = '2017122108'
end_V2_17a    = '2017122308'

start_date    = datetime.strptime(start_V2_17a, DATE_FORMAT)
end_date      = datetime.strptime(end_V2_17a,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1dec0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=8)) # Casey timezone is UT+8
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V2_17)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V2_17a = pd.concat(Traj)

# Set the start/end dates   
start_V2_17b  = '2017122608'
end_V2_17b    = '2017123123'

start_date    = datetime.strptime(start_V2_17b, DATE_FORMAT)
end_date      = datetime.strptime(end_V2_17b,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1dec0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=8)) # Casey timezone is UT+8
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V2_17)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V2_17b = pd.concat(Traj)

# Set the start/end dates   
start_V2_17c  = '2018010100'
end_V2_17c    = '2018010608'

start_date    = datetime.strptime(start_V2_17c, DATE_FORMAT)
end_date      = datetime.strptime(end_V2_17c,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=8)) # Casey timezone is UT+8
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V2_17)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V2_17c = pd.concat(Traj)

# Append V2_17a, V2_17b and V2_17c
Traj_V2_17 = Traj_V2_17a.append(Traj_V2_17b)
Traj_V2_17 = Traj_V2_17.append(Traj_V2_17c)

#-------------
# V3_17M
#-------------
# Set the start/end dates   
start_V3_17Ma  = '2018020105'
end_V3_17Ma    = '2018021805'

start_date    = datetime.strptime(start_V3_17Ma, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_17Ma,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=5)) # Mawson timezone is UT+5
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V3_17M)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)
    
# Combine all the files
Traj_V3_17M = pd.concat(Traj)

#-------------
# V3_17D
#-------------
# Set the start/end dates   
start_V3_17Da = '2018012707'
end_V3_17Da   = '2018013107'

start_date    = datetime.strptime(start_V3_17Da, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_17Da,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V3_17D)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)
    
# Combine all the files
Traj_V3_17Da = pd.concat(Traj)

# Set the start/end dates   
start_V3_17Db = '2018021907'
end_V3_17Db   = '2018022207'

start_date    = datetime.strptime(start_V3_17Db, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_17Db,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V3_17D)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)
    
# Combine all the files
Traj_V3_17Db = pd.concat(Traj)

# Append V3_17Da and V3_17Db
Traj_V3_17D = Traj_V3_17Da.append(Traj_V3_17Db)

#------------------------------------------------------------------------------
# BACK TRAJECTORIES CAMMPCAN (2018-19)

# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

#-------------
# V1_18
#-------------
# Set the start/end dates   
start_V1_18   = '2018110707'
end_V1_18     = '2018111607'

start_date    = datetime.strptime(start_V1_18, DATE_FORMAT)
end_date      = datetime.strptime(end_V1_18,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V1_18)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V1_18 = pd.concat(Traj)

#-------------
# V2_18
#-------------
# Set the start/end dates   
start_V2_18   = '2018121508'
end_V2_18     = '2018123108'

start_date    = datetime.strptime(start_V2_18, DATE_FORMAT)
end_date      = datetime.strptime(end_V2_18,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1dec0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=8)) # Casey timezone is UT+7
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V2_18)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V2_18 = pd.concat(Traj)

#-------------
# V3_18M
#-------------
# Set the start/end dates   
start_V3_18Ma  = '2019013005'
end_V3_18Ma    = '2019013123'

start_date    = datetime.strptime(start_V3_18Ma, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_18Ma,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=5)) # Mawson timezone is UT+5
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V3_18M)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_18Ma = pd.concat(Traj)

# Set the start/end dates   
start_V3_18Mb  = '2019020100'
end_V3_18Mb    = '2019021005'

start_date    = datetime.strptime(start_V3_18Mb, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_18Mb,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=5)) # Mawson timezone is UT+5
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V3_18M)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_18Mb = pd.concat(Traj)

# Append V3_18Ma and V3_18Mb
Traj_V3_18M = Traj_V3_18Ma.append(Traj_V3_18Mb)

#-------------
# V3_18D
#-------------
# Set the start/end dates   
start_V3_18Da = '2019012607'
end_V3_18Da   = '2019012907'

start_date    = datetime.strptime(start_V3_18Da, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_18Da,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V3_18D)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_18Da = pd.concat(Traj)

# Set the start/end dates   
start_V3_18Db = '2019021907'
end_V3_18Db   = '2019022107'

start_date    = datetime.strptime(start_V3_18Db, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_18Db,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0100summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Ice contact time (hours) * sea ice concentration (%)
    file['ContactIcePerc']   = np.sum(file['Traj over Sea Ice?']*file['Sea Ice Conc (0-1)'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice, Ocean
    file['Land_Percentage']    = file['Over_Land']/121
    file['SeaIce_Percentage']  = file['Over_SeaIce']/121
    file['Ice100m_Percentage'] = file['IceContact_100m']/121
    file['IceMLH_Percentage']  = file['IceContact_MLH']/121
    file['Ocean_Percentage']   = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Ice100m'] = np.sum(file['Weighting']*file['Traj over Sea Ice and height < 100 m?']/121)
    file['Weighted_IceMLH']  = np.sum(file['Weighting']*file['Traj over Sea Ice and height < mixed layer top?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the BrO concentration at the corresponding datetime as a row
    Test = file.join(BrO_V3_18D)
    file['surf_vmr(ppmv)'] = Test.iloc[0]['surf_vmr(ppmv)']*1e6
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_18Db = pd.concat(Traj)

# Append V3_18Da and V3_18Db
Traj_V3_18D = Traj_V3_18Da.append(Traj_V3_18Db)

#------------------------------------------------------------------------------
# DROP ROWS WHERE BrO CONCENTRATION IS MISSING

Traj_V1_17  = Traj_V1_17[Traj_V1_17['surf_vmr(ppmv)'].notna()]
Traj_V2_17  = Traj_V2_17[Traj_V2_17['surf_vmr(ppmv)'].notna()]
Traj_V3_17M = Traj_V3_17M[Traj_V3_17M['surf_vmr(ppmv)'].notna()]
Traj_V3_17D = Traj_V3_17D[Traj_V3_17D['surf_vmr(ppmv)'].notna()]

Traj_V1_18  = Traj_V1_18[Traj_V1_18['surf_vmr(ppmv)'].notna()]
Traj_V2_18  = Traj_V2_18[Traj_V2_18['surf_vmr(ppmv)'].notna()]
Traj_V3_18M = Traj_V3_18M[Traj_V3_18M['surf_vmr(ppmv)'].notna()]
Traj_V3_18D = Traj_V3_18D[Traj_V3_18D['surf_vmr(ppmv)'].notna()]

#------------------------------------------------------------------------------
# GET TRAJECTORIES FOR ONLY TRAJ AGE = 0

# Overall
Filter1         = Traj_V1_17['Traj Age']  == 0.0
Traj_V1_17_B    = Traj_V1_17[Filter1]

Filter1         = Traj_V2_17['Traj Age']  == 0.0
Traj_V2_17_B    = Traj_V2_17[Filter1]

Filter1         = Traj_V3_17M['Traj Age']  == 0.0
Traj_V3_17M_B   = Traj_V3_17M[Filter1]

Filter1         = Traj_V3_17D['Traj Age']  == 0.0
Traj_V3_17D_B   = Traj_V3_17D[Filter1]

Filter1         = Traj_V1_18['Traj Age']  == 0.0
Traj_V1_18_B    = Traj_V1_18[Filter1]

Filter1         = Traj_V2_18['Traj Age']  == 0.0
Traj_V2_18_B    = Traj_V2_18[Filter1]

Filter1         = Traj_V3_18M['Traj Age']  == 0.0
Traj_V3_18M_B   = Traj_V3_18M[Filter1]

Filter1         = Traj_V3_18D['Traj Age']  == 0.0
Traj_V3_18D_B   = Traj_V3_18D[Filter1]

# #------------------------------------------------------------------------------
# # CALCULATE THE 5th PERCENTILE BrO

# P5_V1_17    = np.percentile(Traj_V1_17_B['surf_vmr(ppmv)'],    5)
# P5_V2_17    = np.percentile(Traj_V2_17_B['surf_vmr(ppmv)'],    5)
# P5_V3_17M   = np.percentile(Traj_V3_17M_B['surf_vmr(ppmv)'],   5)
# P5_V3_17D   = np.percentile(Traj_V3_17D_B['surf_vmr(ppmv)'],   5)

# P5_V1_18    = np.percentile(Traj_V1_18_B['surf_vmr(ppmv)'],    5)
# P5_V2_18    = np.percentile(Traj_V2_18_B['surf_vmr(ppmv)'],    5)
# P5_V3_18M   = np.percentile(Traj_V3_18M_B['surf_vmr(ppmv)'],   5)
# P5_V3_18D   = np.percentile(Traj_V3_18D_B['surf_vmr(ppmv)'],   5)

# #------------------------------------------------------------------------------
# # CALCULATE THE 95th PERCENTILE BrO

# P95_V1_17    = np.percentile(Traj_V1_17_B['surf_vmr(ppmv)'],    95)
# P95_V2_17    = np.percentile(Traj_V2_17_B['surf_vmr(ppmv)'],    95)
# P95_V3_17M   = np.percentile(Traj_V3_17M_B['surf_vmr(ppmv)'],   95)
# P95_V3_17D   = np.percentile(Traj_V3_17D_B['surf_vmr(ppmv)'],   95)

# P95_V1_18    = np.percentile(Traj_V1_18_B['surf_vmr(ppmv)'],    95)
# P95_V2_18    = np.percentile(Traj_V2_18_B['surf_vmr(ppmv)'],    95)
# P95_V3_18M   = np.percentile(Traj_V3_18M_B['surf_vmr(ppmv)'],   95)
# P95_V3_18D   = np.percentile(Traj_V3_18D_B['surf_vmr(ppmv)'],   95)

#------------------------------------------------------------------------------
# CALCULATE THE 10th PERCENTILE BrO

P5_V1_17    = np.percentile(Traj_V1_17_B['surf_vmr(ppmv)'],    10)
P5_V2_17    = np.percentile(Traj_V2_17_B['surf_vmr(ppmv)'],    10)
P5_V3_17M   = np.percentile(Traj_V3_17M_B['surf_vmr(ppmv)'],   10)
P5_V3_17D   = np.percentile(Traj_V3_17D_B['surf_vmr(ppmv)'],   10)

P5_V1_18    = np.percentile(Traj_V1_18_B['surf_vmr(ppmv)'],    10)
P5_V2_18    = np.percentile(Traj_V2_18_B['surf_vmr(ppmv)'],    10)
P5_V3_18M   = np.percentile(Traj_V3_18M_B['surf_vmr(ppmv)'],   10)
P5_V3_18D   = np.percentile(Traj_V3_18D_B['surf_vmr(ppmv)'],   10)

#------------------------------------------------------------------------------
# CALCULATE THE 90th PERCENTILE BrO

P95_V1_17    = np.percentile(Traj_V1_17_B['surf_vmr(ppmv)'],    90)
P95_V2_17    = np.percentile(Traj_V2_17_B['surf_vmr(ppmv)'],    90)
P95_V3_17M   = np.percentile(Traj_V3_17M_B['surf_vmr(ppmv)'],   90)
P95_V3_17D   = np.percentile(Traj_V3_17D_B['surf_vmr(ppmv)'],   90)

P95_V1_18    = np.percentile(Traj_V1_18_B['surf_vmr(ppmv)'],    90)
P95_V2_18    = np.percentile(Traj_V2_18_B['surf_vmr(ppmv)'],    90)
P95_V3_18M   = np.percentile(Traj_V3_18M_B['surf_vmr(ppmv)'],   90)
P95_V3_18D   = np.percentile(Traj_V3_18D_B['surf_vmr(ppmv)'],   90)

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN BrO

Median_V1_17    = np.median(Traj_V1_17_B['surf_vmr(ppmv)'])
Median_V2_17    = np.median(Traj_V2_17_B['surf_vmr(ppmv)'])
Median_V3_17M   = np.median(Traj_V3_17M_B['surf_vmr(ppmv)'])
Median_V3_17D   = np.median(Traj_V3_17D_B['surf_vmr(ppmv)'])

Median_V1_18    = np.median(Traj_V1_18_B['surf_vmr(ppmv)'])
Median_V2_18    = np.median(Traj_V2_18_B['surf_vmr(ppmv)'])
Median_V3_18M   = np.median(Traj_V3_18M_B['surf_vmr(ppmv)'])
Median_V3_18D   = np.median(Traj_V3_18D_B['surf_vmr(ppmv)'])

#------------------------------------------------------------------------------
# CALCULATE THE MAD BrO

MAD_V1_17    = stats.median_absolute_deviation(Traj_V1_17_B['surf_vmr(ppmv)'])
MAD_V2_17    = stats.median_absolute_deviation(Traj_V2_17_B['surf_vmr(ppmv)'])
MAD_V3_17M   = stats.median_absolute_deviation(Traj_V3_17M_B['surf_vmr(ppmv)'])
MAD_V3_17D   = stats.median_absolute_deviation(Traj_V3_17D_B['surf_vmr(ppmv)'])

MAD_V1_18    = stats.median_absolute_deviation(Traj_V1_18_B['surf_vmr(ppmv)'])
MAD_V2_18    = stats.median_absolute_deviation(Traj_V2_18_B['surf_vmr(ppmv)'])
MAD_V3_18M   = stats.median_absolute_deviation(Traj_V3_18M_B['surf_vmr(ppmv)'])
MAD_V3_18D   = stats.median_absolute_deviation(Traj_V3_18D_B['surf_vmr(ppmv)'])

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN - MAD BrO

Med_M_MAD_V1_17  = Median_V1_17  - MAD_V1_17
Med_M_MAD_V2_17  = Median_V2_17  - MAD_V2_17
Med_M_MAD_V3_17M = Median_V3_17M - MAD_V3_17M
Med_M_MAD_V3_17D = Median_V3_17D - MAD_V3_17D

Med_M_MAD_V1_18  = Median_V1_18  - MAD_V1_18
Med_M_MAD_V2_18  = Median_V2_18  - MAD_V2_18
Med_M_MAD_V3_18M = Median_V3_18M - MAD_V3_18M
Med_M_MAD_V3_18D = Median_V3_18D - MAD_V3_18D

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN + MAD BrO

Med_P_MAD_V1_17  = Median_V1_17  + MAD_V1_17
Med_P_MAD_V2_17  = Median_V2_17  + MAD_V2_17
Med_P_MAD_V3_17M = Median_V3_17M + MAD_V3_17M
Med_P_MAD_V3_17D = Median_V3_17D + MAD_V3_17D

Med_P_MAD_V1_18  = Median_V1_18  + MAD_V1_18
Med_P_MAD_V2_18  = Median_V2_18  + MAD_V2_18
Med_P_MAD_V3_18M = Median_V3_18M + MAD_V3_18M
Med_P_MAD_V3_18D = Median_V3_18D + MAD_V3_18D

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO <= 5th PERCENTILE

P5_1           = Traj_V1_17['surf_vmr(ppmv)']  <= P5_V1_17
Traj_V1_17_P5  = Traj_V1_17[P5_1]

P5_2           = Traj_V2_17['surf_vmr(ppmv)']  <= P5_V2_17
Traj_V2_17_P5  = Traj_V2_17[P5_2]

P5_3           = Traj_V3_17M['surf_vmr(ppmv)'] <= P5_V3_17M
Traj_V3_17M_P5 = Traj_V3_17M[P5_3]

P5_4           = Traj_V3_17D['surf_vmr(ppmv)'] <= P5_V3_17D
Traj_V3_17D_P5 = Traj_V3_17D[P5_4]

P5_5           = Traj_V1_18['surf_vmr(ppmv)']  <= P5_V1_18
Traj_V1_18_P5  = Traj_V1_18[P5_5]

P5_6           = Traj_V2_18['surf_vmr(ppmv)']  <= P5_V2_18
Traj_V2_18_P5  = Traj_V2_18[P5_6]

P5_7           = Traj_V3_18M['surf_vmr(ppmv)'] <= P5_V3_18M
Traj_V3_18M_P5 = Traj_V3_18M[P5_7]

P5_8           = Traj_V3_18D['surf_vmr(ppmv)'] <= P5_V3_18D
Traj_V3_18D_P5 = Traj_V3_18D[P5_8]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO >= 95th PERCENTILE

P95_1           = Traj_V1_17['surf_vmr(ppmv)']  >= P95_V1_17
Traj_V1_17_P95  = Traj_V1_17[P95_1]

P95_2           = Traj_V2_17['surf_vmr(ppmv)']  >= P95_V2_17
Traj_V2_17_P95  = Traj_V2_17[P95_2]

P95_3           = Traj_V3_17M['surf_vmr(ppmv)'] >= P95_V3_17M
Traj_V3_17M_P95 = Traj_V3_17M[P95_3]

P95_4           = Traj_V3_17D['surf_vmr(ppmv)'] >= P95_V3_17D
Traj_V3_17D_P95 = Traj_V3_17D[P95_4]

P95_5           = Traj_V1_18['surf_vmr(ppmv)']  >= P95_V1_18
Traj_V1_18_P95  = Traj_V1_18[P95_5]

P95_6           = Traj_V2_18['surf_vmr(ppmv)']  >= P95_V2_18
Traj_V2_18_P95  = Traj_V2_18[P95_6]

P95_7           = Traj_V3_18M['surf_vmr(ppmv)'] >= P95_V3_18M
Traj_V3_18M_P95 = Traj_V3_18M[P95_7]

P95_8           = Traj_V3_18D['surf_vmr(ppmv)'] >= P95_V3_18D
Traj_V3_18D_P95 = Traj_V3_18D[P95_8]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO MEDIAN +/- MAD

Median_1        = (Traj_V1_17['surf_vmr(ppmv)']  >= Med_M_MAD_V1_17)  & (Traj_V1_17['surf_vmr(ppmv)']  <= Med_P_MAD_V1_17)
Traj_V1_17_Med  = Traj_V1_17[Median_1]

Median_2        = (Traj_V2_17['surf_vmr(ppmv)']  >= Med_M_MAD_V2_17)  & (Traj_V2_17['surf_vmr(ppmv)']  <= Med_P_MAD_V2_17)
Traj_V2_17_Med  = Traj_V2_17[Median_2]

Median_3        = (Traj_V3_17M['surf_vmr(ppmv)'] >= Med_M_MAD_V3_17M) & (Traj_V3_17M['surf_vmr(ppmv)'] <= Med_P_MAD_V3_17M)
Traj_V3_17M_Med = Traj_V3_17M[Median_3]

Median_4        = (Traj_V3_17D['surf_vmr(ppmv)'] >= Med_M_MAD_V3_17D) & (Traj_V3_17D['surf_vmr(ppmv)'] <= Med_P_MAD_V3_17D)
Traj_V3_17D_Med = Traj_V3_17D[Median_4]

Median_5        = (Traj_V1_18['surf_vmr(ppmv)']  >= Med_M_MAD_V1_18)  & (Traj_V1_18['surf_vmr(ppmv)']  <= Med_P_MAD_V1_18)
Traj_V1_18_Med  = Traj_V1_18[Median_5]

Median_6        = (Traj_V2_18['surf_vmr(ppmv)']  >= Med_M_MAD_V2_18)  & (Traj_V2_18['surf_vmr(ppmv)']  <= Med_P_MAD_V2_18)
Traj_V2_18_Med  = Traj_V2_18[Median_6]

Median_7        = (Traj_V3_18M['surf_vmr(ppmv)'] >= Med_M_MAD_V3_18M) & (Traj_V3_18M['surf_vmr(ppmv)'] <= Med_P_MAD_V3_18M)
Traj_V3_18M_Med = Traj_V3_18M[Median_7]

Median_8        = (Traj_V3_18D['surf_vmr(ppmv)'] >= Med_M_MAD_V3_18D) & (Traj_V3_18D['surf_vmr(ppmv)'] <= Med_P_MAD_V3_18D)
Traj_V3_18D_Med = Traj_V3_18D[Median_8]

#------------------------------------------------------------------------------
# GET TRAJECTORIES FOR ONLY TRAJ AGE = 0

#--------------
# P5
#--------------
Filter1          = Traj_V1_17_P5['Traj Age']  == 0.0
Traj_V1_17_P5_B  = Traj_V1_17_P5[Filter1]

Filter1          = Traj_V2_17_P5['Traj Age']  == 0.0
Traj_V2_17_P5_B  = Traj_V2_17_P5[Filter1]

Filter1          = Traj_V3_17M_P5['Traj Age'] == 0.0
Traj_V3_17M_P5_B = Traj_V3_17M_P5[Filter1]

Filter1          = Traj_V3_17D_P5['Traj Age'] == 0.0
Traj_V3_17D_P5_B = Traj_V3_17D_P5[Filter1]

Filter1          = Traj_V1_18_P5['Traj Age']  == 0.0
Traj_V1_18_P5_B  = Traj_V1_18_P5[Filter1]

Filter1          = Traj_V2_18_P5['Traj Age']  == 0.0
Traj_V2_18_P5_B  = Traj_V2_18_P5[Filter1]

Filter1          = Traj_V3_18M_P5['Traj Age'] == 0.0
Traj_V3_18M_P5_B = Traj_V3_18M_P5[Filter1]

Filter1          = Traj_V3_18D_P5['Traj Age'] == 0.0
Traj_V3_18D_P5_B = Traj_V3_18D_P5[Filter1]

#--------------
# P95
#--------------
Filter1           = Traj_V1_17_P95['Traj Age']  == 0.0
Traj_V1_17_P95_B  = Traj_V1_17_P95[Filter1]

Filter1           = Traj_V2_17_P95['Traj Age']  == 0.0
Traj_V2_17_P95_B  = Traj_V2_17_P95[Filter1]

Filter1           = Traj_V3_17M_P95['Traj Age'] == 0.0
Traj_V3_17M_P95_B = Traj_V3_17M_P95[Filter1]

Filter1           = Traj_V3_17D_P95['Traj Age'] == 0.0
Traj_V3_17D_P95_B = Traj_V3_17D_P95[Filter1]

Filter1           = Traj_V1_18_P95['Traj Age']  == 0.0
Traj_V1_18_P95_B  = Traj_V1_18_P95[Filter1]

Filter1           = Traj_V2_18_P95['Traj Age']  == 0.0
Traj_V2_18_P95_B  = Traj_V2_18_P95[Filter1]

Filter1           = Traj_V3_18M_P95['Traj Age'] == 0.0
Traj_V3_18M_P95_B = Traj_V3_18M_P95[Filter1]

Filter1           = Traj_V3_18D_P95['Traj Age'] == 0.0
Traj_V3_18D_P95_B = Traj_V3_18D_P95[Filter1]

#--------------
# Median
#--------------
Filter1           = Traj_V1_17_Med['Traj Age']  == 0.0
Traj_V1_17_Med_B  = Traj_V1_17_Med[Filter1]

Filter1           = Traj_V2_17_Med['Traj Age']  == 0.0
Traj_V2_17_Med_B  = Traj_V2_17_Med[Filter1]

Filter1           = Traj_V3_17M_Med['Traj Age'] == 0.0
Traj_V3_17M_Med_B = Traj_V3_17M_Med[Filter1]

Filter1           = Traj_V3_17D_Med['Traj Age'] == 0.0
Traj_V3_17D_Med_B = Traj_V3_17D_Med[Filter1]

Filter1           = Traj_V1_18_Med['Traj Age']  == 0.0
Traj_V1_18_Med_B  = Traj_V1_18_Med[Filter1]

Filter1           = Traj_V2_18_Med['Traj Age']  == 0.0
Traj_V2_18_Med_B  = Traj_V2_18_Med[Filter1]

Filter1           = Traj_V3_18M_Med['Traj Age'] == 0.0
Traj_V3_18M_Med_B = Traj_V3_18M_Med[Filter1]

Filter1           = Traj_V3_18D_Med['Traj Age'] == 0.0
Traj_V3_18D_Med_B = Traj_V3_18D_Med[Filter1]

#------------------------------------------------------------------------------
# COUNT THE NUMBER OF OBSERVATIONS All, P5, P95, Median

# All
N_V1_17    = len(Traj_V1_17_B)
N_V2_17    = len(Traj_V2_17_B)
N_V3_17M   = len(Traj_V3_17M_B)
N_V3_17D   = len(Traj_V3_17D_B)

N_V1_18    = len(Traj_V1_18_B)
N_V2_18    = len(Traj_V2_18_B)
N_V3_18M   = len(Traj_V3_18M_B)
N_V3_18D   = len(Traj_V3_18D_B)

# P5
N_V1_17_P5    = len(Traj_V1_17_P5_B)
N_V2_17_P5    = len(Traj_V2_17_P5_B)
N_V3_17M_P5   = len(Traj_V3_17M_P5_B)
N_V3_17D_P5   = len(Traj_V3_17D_P5_B)

N_V1_18_P5    = len(Traj_V1_18_P5_B)
N_V2_18_P5    = len(Traj_V2_18_P5_B)
N_V3_18M_P5   = len(Traj_V3_18M_P5_B)
N_V3_18D_P5   = len(Traj_V3_18D_P5_B)

# P95
N_V1_17_P95   = len(Traj_V1_17_P95_B)
N_V2_17_P95   = len(Traj_V2_17_P95_B)
N_V3_17M_P95  = len(Traj_V3_17M_P95_B)
N_V3_17D_P95  = len(Traj_V3_17D_P95_B)

N_V1_18_P95   = len(Traj_V1_18_P95_B)
N_V2_18_P95   = len(Traj_V2_18_P95_B)
N_V3_18M_P95  = len(Traj_V3_18M_P95_B)
N_V3_18D_P95  = len(Traj_V3_18D_P95_B)

# Median
N_V1_17_Med   = len(Traj_V1_17_Med_B)
N_V2_17_Med   = len(Traj_V2_17_Med_B)
N_V3_17M_Med  = len(Traj_V3_17M_Med_B)
N_V3_17D_Med  = len(Traj_V3_17D_Med_B)

N_V1_18_Med   = len(Traj_V1_18_Med_B)
N_V2_18_Med   = len(Traj_V2_18_Med_B)
N_V3_18M_Med  = len(Traj_V3_18M_Med_B)
N_V3_18D_Med  = len(Traj_V3_18D_Med_B)

# #------------------------------------------------------------------------------
# # Welches T-Test on BrO
 
# #----------------------
# # T-test for the means of 2 indpendent populations
# # (Note: unequal sample sizes and/or variance, therefore Welches t-test)
# #----------------------

# # Land & Sea Ice
# WTstat_V1_18_L_SI,  WTpval_V1_18_L_SI  = stats.ttest_ind(Traj_V1_18L_B['surf_vmr(ppmv)'],   Traj_V1_18SI_B['surf_vmr(ppmv)'],  equal_var = False, nan_policy='omit')
# WTstat_V2_18_L_SI,  WTpval_V2_18_L_SI  = stats.ttest_ind(Traj_V2_18L_B['surf_vmr(ppmv)'],   Traj_V2_18SI_B['surf_vmr(ppmv)'],  equal_var = False, nan_policy='omit')
# WTstat_V3_18M_L_SI, WTpval_V3_18M_L_SI = stats.ttest_ind(Traj_V3_18ML_B['surf_vmr(ppmv)'],  Traj_V3_18MSI_B['surf_vmr(ppmv)'], equal_var = False, nan_policy='omit')
# WTstat_V3_18D_L_SI, WTpval_V3_18D_L_SI = stats.ttest_ind(Traj_V3_18DL_B['surf_vmr(ppmv)'],  Traj_V3_18DSI_B['surf_vmr(ppmv)'], equal_var = False, nan_policy='omit')
# WTstat_1819_L_SI,   WTpval_1819_L_SI   = stats.ttest_ind(Land_1819['surf_vmr(ppmv)'],       SeaIce_1819['surf_vmr(ppmv)'],     equal_var = False, nan_policy='omit')

# # Land & Ocean
# WTstat_V1_18_L_O,   WTpval_V1_18_L_O   = stats.ttest_ind(Traj_V1_18L_B['surf_vmr(ppmv)'],   Traj_V1_18O_B['surf_vmr(ppmv)'],   equal_var = False, nan_policy='omit')
# WTstat_V2_18_L_O,   WTpval_V2_18_L_O   = stats.ttest_ind(Traj_V2_18L_B['surf_vmr(ppmv)'],   Traj_V2_18O_B['surf_vmr(ppmv)'],   equal_var = False, nan_policy='omit')
# WTstat_V3_18M_L_O,  WTpval_V3_18M_L_O  = stats.ttest_ind(Traj_V3_18ML_B['surf_vmr(ppmv)'],  Traj_V3_18MO_B['surf_vmr(ppmv)'],  equal_var = False, nan_policy='omit')
# WTstat_V3_18D_L_O,  WTpval_V3_18D_L_O  = stats.ttest_ind(Traj_V3_18DL_B['surf_vmr(ppmv)'],  Traj_V3_18DO_B['surf_vmr(ppmv)'],  equal_var = False, nan_policy='omit')
# WTstat_1819_L_O,    WTpval_1819_L_O    = stats.ttest_ind(Land_1819['surf_vmr(ppmv)'],       Ocean_1819['surf_vmr(ppmv)'],      equal_var = False, nan_policy='omit')

# # Sea Ice & Ocean
# WTstat_V1_18_SI_O,  WTpval_V1_18_SI_O  = stats.ttest_ind(Traj_V1_18SI_B['surf_vmr(ppmv)'],  Traj_V1_18O_B['surf_vmr(ppmv)'],   equal_var = False, nan_policy='omit')
# WTstat_V2_18_SI_O,  WTpval_V2_18_SI_O  = stats.ttest_ind(Traj_V2_18SI_B['surf_vmr(ppmv)'],  Traj_V2_18O_B['surf_vmr(ppmv)'],   equal_var = False, nan_policy='omit')
# WTstat_V3_18M_SI_O, WTpval_V3_18M_SI_O = stats.ttest_ind(Traj_V3_18MSI_B['surf_vmr(ppmv)'], Traj_V3_18MO_B['surf_vmr(ppmv)'],  equal_var = False, nan_policy='omit')
# WTstat_V3_18D_SI_O, WTpval_V3_18D_SI_O = stats.ttest_ind(Traj_V3_18DSI_B['surf_vmr(ppmv)'], Traj_V3_18DO_B[surf_vmr(ppmv)'],  equal_var = False, nan_policy='omit')
# WTstat_1819_SI_O,   WTpval_1819_SI_O   = stats.ttest_ind(SeaIce_1819['surf_vmr(ppmv)'],     Ocean_1819['surf_vmr(ppmv)'],      equal_var = False, nan_policy='omit')

# #------------------------------------------------------------------------------
# # KS-Test on BrO (Kolmogorov-Smirnov Test)

# # Land & Sea Ice
# KSstat_V1_18_L_SI,  KSpval_V1_18_L_SI  = stats.ks_2samp(Traj_V1_18L_B['surf_vmr(ppmv)'],   Traj_V1_18SI_B['surf_vmr(ppmv)'],  alternative='two-sided', mode='auto')
# KSstat_V2_18_L_SI,  KSpval_V2_18_L_SI  = stats.ks_2samp(Traj_V2_18L_B['surf_vmr(ppmv)'],   Traj_V2_18SI_B['surf_vmr(ppmv)'],  alternative='two-sided', mode='auto')
# KSstat_V3_18M_L_SI, KSpval_V3_18M_L_SI = stats.ks_2samp(Traj_V3_18ML_B['surf_vmr(ppmv)'],  Traj_V3_18MSI_B['surf_vmr(ppmv)'], alternative='two-sided', mode='auto')
# KSstat_V3_18D_L_SI, KSpval_V3_18D_L_SI = stats.ks_2samp(Traj_V3_18DL_B['surf_vmr(ppmv)'],  Traj_V3_18DSI_B['surf_vmr(ppmv)'], alternative='two-sided', mode='auto')
# KSstat_1819_L_SI,   KSpval_1819_L_SI   = stats.ks_2samp(Land_1819['surf_vmr(ppmv)'],       SeaIce_1819['surf_vmr(ppmv)'],   alternative='two-sided', mode='auto')

# # Land & Ocean
# KSstat_V1_18_L_O,   KSpval_V1_18_L_O   = np.nan, np.nan #stats.ks_2samp(Traj_V1_18L_B['surf_vmr(ppmv)'],   Traj_V1_18O_B['surf_vmr(ppmv)'],   alternative='two-sided', mode='auto')
# KSstat_V2_18_L_O,   KSpval_V2_18_L_O   = stats.ks_2samp(Traj_V2_18L_B['surf_vmr(ppmv)'],   Traj_V2_18O_B['surf_vmr(ppmv)'],   alternative='two-sided', mode='auto')
# KSstat_V3_18M_L_O,  KSpval_V3_18M_L_O  = stats.ks_2samp(Traj_V3_18ML_B['surf_vmr(ppmv)'],  Traj_V3_18MO_B['surf_vmr(ppmv)'],  alternative='two-sided', mode='auto')
# KSstat_V3_18D_L_O,  KSpval_V3_18D_L_O  = stats.ks_2samp(Traj_V3_18DL_B['surf_vmr(ppmv)'],  Traj_V3_18DO_B['surf_vmr(ppmv)'],  alternative='two-sided', mode='auto')
# KSstat_1819_L_O,    KSpval_1819_L_O    = stats.ks_2samp(Land_1819['surf_vmr(ppmv)'],       Ocean_1819['surf_vmr(ppmv)'],      alternative='two-sided', mode='auto')

# # Sea Ice & Ocean
# KSstat_V1_18_SI_O,  KSpval_V1_18_SI_O  = np.nan, np.nan #stats.ks_2samp(Traj_V1_18SI_B['surf_vmr(ppmv)'],  Traj_V1_18O_B['surf_vmr(ppmv)'],   alternative='two-sided', mode='auto')
# KSstat_V2_18_SI_O,  KSpval_V2_18_SI_O  = stats.ks_2samp(Traj_V2_18SI_B['surf_vmr(ppmv)'],  Traj_V2_18O_B['surf_vmr(ppmv)'],   alternative='two-sided', mode='auto')
# KSstat_V3_18M_SI_O, KSpval_V3_18M_SI_O = stats.ks_2samp(Traj_V3_18MSI_B['surf_vmr(ppmv)'], Traj_V3_18MO_B['surf_vmr(ppmv)'],  alternative='two-sided', mode='auto')
# KSstat_V3_18D_SI_O, KSpval_V3_18D_SI_O = stats.ks_2samp(Traj_V3_18DSI_B['surf_vmr(ppmv)'], Traj_V3_18DO_B['surf_vmr(ppmv)'],  alternative='two-sided', mode='auto')
# KSstat_1819_SI_O,   KSpval_1819_SI_O   = stats.ks_2samp(SeaIce_1819['surf_vmr(ppmv)'],     Ocean_1819['surf_vmr(ppmv)'],      alternative='two-sided', mode='auto')

#------------------------------------------------------------------------------
# VARIABLES FOR PLOTTING SEA ICE COVER

# Sea ice
seaice_data_V1_17  = SeaIce_V1_17.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V2_17  = SeaIce_V2_17.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V3_17M = SeaIce_V3_17M.variables['ice'][0,0,:,:]   # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V3_17D = SeaIce_V3_17D.variables['ice'][0,0,:,:]   # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)

seaice_data_V1_18  = SeaIce_V1_18.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V2_18  = SeaIce_V2_18.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V3_18M = SeaIce_V3_18M.variables['ice'][0,0,:,:]   # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V3_18D = SeaIce_V3_18D.variables['ice'][0,0,:,:]   # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)

seaice_data_SIPEXII = SeaIce_SIPEXII.variables['ice'][0,0,:,:] # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_PCAN    = SeaIce_PCAN.variables['sea_ice_area_fraction'][0,:,:]    # Sea Ice concentration (time,y,x)(1,1,632,664)

land_PCAN = SeaIce_PCAN.variables['land'][0,:,:] 

# Latitudes
lats_V1_17   = SeaIce_V1_17.lat
lats_V2_17   = SeaIce_V2_17.lat
lats_V3_17M  = SeaIce_V3_17M.lat
lats_V3_17D  = SeaIce_V3_17D.lat

lats_V1_18   = SeaIce_V1_18.lat
lats_V2_18   = SeaIce_V2_18.lat
lats_V3_18M  = SeaIce_V3_18M.lat
lats_V3_18D  = SeaIce_V3_18D.lat

lats_SIPEXII = SeaIce_SIPEXII.lat
lats_PCAN    = SeaIce_PCAN.latitude

# Longitudes
lons_V1_17   = SeaIce_V1_17.lon
lons_V2_17   = SeaIce_V2_17.lon
lons_V3_17M  = SeaIce_V3_17M.lon
lons_V3_17D  = SeaIce_V3_17D.lon

lons_V1_18   = SeaIce_V1_18.lon
lons_V2_18   = SeaIce_V2_18.lon
lons_V3_18M  = SeaIce_V3_18M.lon
lons_V3_18D  = SeaIce_V3_18D.lon

lons_SIPEXII = SeaIce_SIPEXII.lon
lons_PCAN    = SeaIce_PCAN.longitude

# The data are defined in lat/lon coordinate system, so PlateCarree()
# is the appropriate coordinate system:
data_crs = ccrs.PlateCarree()

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN 2017-18 & 2018-19)
fig1 = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=4, 
                       figure=fig1, 
                       width_ratios= [0.5, 0.5, 0.5, 0.5],
                       height_ratios=[0.5, 0.5])

#-----------------------------
# Graph 1
ax = plt.subplot(gs[0,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V1_17 = np.ma.masked_where(seaice_data_V1_17==-999,seaice_data_V1_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V1_17, lats_V1_17, seaice_data_V1_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,7.5,0.5), cmap.N) # BrO concentration

#ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V1_17['IceContact_100m'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V1 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Label for CAMMPCAN (2017-18)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "    CAMMPCAN (2017-18)    ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.955, "a", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box for no of observations
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.095, "n: " +str("%6.0f"%(N_V1_17)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 2
ax = plt.subplot(gs[0,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V2_17 = np.ma.masked_where(seaice_data_V2_17==-999,seaice_data_V2_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V2_17, lats_V2_17, seaice_data_V2_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,7.5,0.5), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_17['Traj Lon'], Traj_V2_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V2_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V2_17['Traj Lon'], Traj_V2_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V2 (Casey)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.955, "b", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box for no of observations
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.095, "n: " +str("%6.0f"%(N_V2_17)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 3
ax = plt.subplot(gs[0,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_17M = np.ma.masked_where(seaice_data_V3_17M==-999,seaice_data_V3_17M)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_17M, lats_V3_17M, seaice_data_V3_17M, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,7.5,0.5), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17M['Traj Lon'], Traj_V3_17M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_17M['Traj Lon'], Traj_V3_17M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V3 (Mawson)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.955, "c", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box for no of observations
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.095, "n: " +str("%6.0f"%(N_V3_17M)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 4
ax = plt.subplot(gs[0,3], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_17D = np.ma.masked_where(seaice_data_V3_17D==-999,seaice_data_V3_17D)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_17D, lats_V3_17D, seaice_data_V3_17D, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,7.5,0.5), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17D['Traj Lon'], Traj_V3_17D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_17D['Traj Lon'], Traj_V3_17D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V3 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.955, "d", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box for no of observations
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.095, "n: " +str("%6.0f"%(N_V3_17D)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 5
ax = plt.subplot(gs[1,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V1_18 = np.ma.masked_where(seaice_data_V1_18==-999,seaice_data_V1_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V1_18, lats_V1_18, seaice_data_V1_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,7.5,0.5), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V1_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V1_18['Traj Lon'], Traj_V1_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V1 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Label for CAMMPCAN (2018-19)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "    CAMMPCAN (2018-19)    ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.955, "e", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box for no of observations
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.095, "n: " +str("%6.0f"%(N_V1_18)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 6
ax = plt.subplot(gs[1,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V2_18 = np.ma.masked_where(seaice_data_V2_18==-999,seaice_data_V2_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V2_18, lats_V2_18, seaice_data_V2_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,7.5,0.5), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_17['Traj Lon'], Traj_V2_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V2_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V2_18['Traj Lon'], Traj_V2_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V2 (Casey)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.955, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box for no of observations
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.095, "n: " +str("%6.0f"%(N_V2_18)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 7
ax = plt.subplot(gs[1,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_18M = np.ma.masked_where(seaice_data_V3_18M==-999,seaice_data_V3_18M)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_18M, lats_V3_18M, seaice_data_V3_18M, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,7.5,0.5), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17M['Traj Lon'], Traj_V3_17M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18M['Traj Lon'], Traj_V3_18M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Mawson)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.955, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box for no of observations
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.095, "n: " +str("%6.0f"%(N_V3_18M)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 8
ax = plt.subplot(gs[1,3], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_18D = np.ma.masked_where(seaice_data_V3_18D==-999,seaice_data_V3_17D)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_18D, lats_V3_18D, seaice_data_V3_18D, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,7.5,0.5), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17D['Traj Lon'], Traj_V3_17D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18D['Traj Lon'], Traj_V3_18D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.955, "h", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box for no of observations
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.035, 0.095, "n: " +str("%6.0f"%(N_V3_18D)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,1.0,2.0,3.0,4.0,5.0,6.0,7.0], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('BrO (pptv)') # Hg$^0$ (ng/m$^3$)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN 2017-18)

fig1 = plt.figure()

gs = gridspec.GridSpec(nrows=3,
                       ncols=4, 
                       figure=fig1, 
                       width_ratios= [0.5, 0.5, 0.5, 0.5],
                       height_ratios=[0.5, 0.5, 0.5])

#-----------------------------
# Graph 1
ax = plt.subplot(gs[0,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V1_17 = np.ma.masked_where(seaice_data_V1_17==-999,seaice_data_V1_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V1_17, lats_V1_17, seaice_data_V1_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

cs2 = ax.scatter(Traj_V1_17_P5['Traj Lon'], Traj_V1_17_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_P5['Traj Height (m)'], label='Traj Height (m)')
#cs2 = ax.scatter(Traj_V1_17_P5['Traj Lon'], Traj_V1_17_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_P5['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V1 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box for label
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "       10$^t$$^h$ percentile       ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_17_P5)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "a", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 2
ax = plt.subplot(gs[0,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)
ax.set_facecolor('lightgrey')

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V2_17 = np.ma.masked_where(seaice_data_V2_17==-999,seaice_data_V2_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V2_17, lats_V2_17, seaice_data_V2_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V2_17_P5['Traj Lon'], Traj_V2_17_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_P5['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V2_17_P5['Traj Lon'], Traj_V2_17_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_P5['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V2 (Casey)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_17_P5)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "b", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 3
ax = plt.subplot(gs[0,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_17M = np.ma.masked_where(seaice_data_V3_17M==-999,seaice_data_V3_17M)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_17M, lats_V3_17M, seaice_data_V3_17M, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration


ax.scatter(Traj_V3_17M_P5['Traj Lon'], Traj_V3_17M_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M_P5['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_17M_P5['Traj Lon'], Traj_V3_17M_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M_P5['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V3 (Mawson)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17M_P5)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "c", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 4
ax = plt.subplot(gs[0,3], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_17D = np.ma.masked_where(seaice_data_V3_17D==-999,seaice_data_V3_17D)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_17D, lats_V3_17D, seaice_data_V3_17D, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_17D_P5['Traj Lon'], Traj_V3_17D_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D_P5['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_17D_P5['Traj Lon'], Traj_V3_17D_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D_P5['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V3 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17D_P5)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "d", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 5
ax = plt.subplot(gs[1,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V1_17 = np.ma.masked_where(seaice_data_V1_17==-999,seaice_data_V1_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V1_17, lats_V1_17, seaice_data_V1_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

cs2 = ax.scatter(Traj_V1_17_Med['Traj Lon'], Traj_V1_17_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_Med['Traj Height (m)'], label='Traj Height (m)')
#cs2 = ax.scatter(Traj_V1_17_Med['Traj Lon'], Traj_V1_17_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_Med['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V1 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "            Median           ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_17_Med)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "e", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 6
ax = plt.subplot(gs[1,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)
ax.set_facecolor('lightgrey')

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V2_17 = np.ma.masked_where(seaice_data_V2_17==-999,seaice_data_V2_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V2_17, lats_V2_17, seaice_data_V2_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V2_17_Med['Traj Lon'], Traj_V2_17_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_Med['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V2_17_Med['Traj Lon'], Traj_V2_17_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_Med['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V2 (Casey)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_17_Med)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 7
ax = plt.subplot(gs[1,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_17M = np.ma.masked_where(seaice_data_V3_17M==-999,seaice_data_V3_17M)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_17M, lats_V3_17M, seaice_data_V3_17M, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration


ax.scatter(Traj_V3_17M_Med['Traj Lon'], Traj_V3_17M_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M_Med['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_17M_Med['Traj Lon'], Traj_V3_17M_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M_Med['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Mawson)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17M_Med)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 8
ax = plt.subplot(gs[1,3], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_17D = np.ma.masked_where(seaice_data_V3_17D==-999,seaice_data_V3_17D)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_17D, lats_V3_17D, seaice_data_V3_17D, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_17D_Med['Traj Lon'], Traj_V3_17D_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D_Med['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_17D_Med['Traj Lon'], Traj_V3_17D_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D_Med['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17D_Med)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "h", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 9
ax = plt.subplot(gs[2,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V1_17 = np.ma.masked_where(seaice_data_V1_17==-999,seaice_data_V1_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V1_17, lats_V1_17, seaice_data_V1_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

cs2 = ax.scatter(Traj_V1_17_P95['Traj Lon'], Traj_V1_17_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_P95['Traj Height (m)'], label='Traj Height (m)')
#cs2 = ax.scatter(Traj_V1_17_P95['Traj Lon'], Traj_V1_17_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_P95['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V1 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "       90$^t$$^h$ percentile       ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_17_P95)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "i", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 10
ax = plt.subplot(gs[2,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)
ax.set_facecolor('lightgrey')

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V2_17 = np.ma.masked_where(seaice_data_V2_17==-999,seaice_data_V2_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V2_17, lats_V2_17, seaice_data_V2_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V2_17_P95['Traj Lon'], Traj_V2_17_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_P95['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V2_17_P95['Traj Lon'], Traj_V2_17_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_P95['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V2 (Casey)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_17_P95)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "j", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 11
ax = plt.subplot(gs[2,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_17M = np.ma.masked_where(seaice_data_V3_17M==-999,seaice_data_V3_17M)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_17M, lats_V3_17M, seaice_data_V3_17M, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_17M_P95['Traj Lon'], Traj_V3_17M_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M_P95['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_17M_P95['Traj Lon'], Traj_V3_17M_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M_P95['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Mawson)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17M_P95)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "k", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 12
ax = plt.subplot(gs[2,3], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_17D = np.ma.masked_where(seaice_data_V3_17D==-999,seaice_data_V3_17D)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_17D, lats_V3_17D, seaice_data_V3_17D, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_17D_P95['Traj Lon'], Traj_V3_17D_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D_P95['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_17D_P95['Traj Lon'], Traj_V3_17D_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D_P95['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17D_P95)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "l", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
# cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,1.0,2.0,3.0,4.0,5.0,6.0,7.0], pad = 0.08, shrink=.995) # Hg0 concentration
# cb.set_label('BrO (pptv)') # Hg$^0$ (ng/m$^3$)
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,500,1000,1500,2000,2500,3000,3500,4000], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Height (MSL)') # Hg$^0$ (ng/m$^3$)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN 2018-19)

fig1 = plt.figure()

gs = gridspec.GridSpec(nrows=3,
                       ncols=4, 
                       figure=fig1, 
                       width_ratios= [0.5, 0.5, 0.5, 0.5],
                       height_ratios=[0.5, 0.5, 0.5])

#-----------------------------
# Graph 1
ax = plt.subplot(gs[0,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V1_18 = np.ma.masked_where(seaice_data_V1_18==-999,seaice_data_V1_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V1_18, lats_V1_18, seaice_data_V1_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

cs2 = ax.scatter(Traj_V1_18_P5['Traj Lon'], Traj_V1_18_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P5['Traj Height (m)'], label='Traj Height (m)')
#cs2 = ax.scatter(Traj_V1_18_P5['Traj Lon'], Traj_V1_18_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P5['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V1 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "       10$^t$$^h$ percentile       ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_18_P5)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "a", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 2
ax = plt.subplot(gs[0,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)
ax.set_facecolor('lightgrey')

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V2_18 = np.ma.masked_where(seaice_data_V2_18==-999,seaice_data_V2_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V2_18, lats_V2_18, seaice_data_V2_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V2_18_P5['Traj Lon'], Traj_V2_18_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P5['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V2_18_P5['Traj Lon'], Traj_V2_18_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P5['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V2 (Casey)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_18_P5)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "b", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 3
ax = plt.subplot(gs[0,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_18M = np.ma.masked_where(seaice_data_V3_18M==-999,seaice_data_V3_18M)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_18M, lats_V3_18M, seaice_data_V3_18M, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_18M_P5['Traj Lon'], Traj_V3_18M_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M_P5['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_18M_P5['Traj Lon'], Traj_V3_18M_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M_P5['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V3 (Mawson)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18M_P5)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "c", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 4
ax = plt.subplot(gs[0,3], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_18D = np.ma.masked_where(seaice_data_V3_18D==-999,seaice_data_V3_18D)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_18D, lats_V3_18D, seaice_data_V3_18D, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_18D_P5['Traj Lon'], Traj_V3_18D_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18D_P5['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_18D_P5['Traj Lon'], Traj_V3_18D_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D_P5['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V3 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18D_P5)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "d", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 5
ax = plt.subplot(gs[1,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V1_18 = np.ma.masked_where(seaice_data_V1_18==-999,seaice_data_V1_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V1_18, lats_V1_18, seaice_data_V1_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

cs2 = ax.scatter(Traj_V1_18_Med['Traj Lon'], Traj_V1_18_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_Med['Traj Height (m)'], label='Traj Height (m)')
#cs2 = ax.scatter(Traj_V1_18_Med['Traj Lon'], Traj_V1_18_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_Med['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V1 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "            Median           ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_18_Med)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "e", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 6
ax = plt.subplot(gs[1,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)
ax.set_facecolor('lightgrey')

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V2_18 = np.ma.masked_where(seaice_data_V2_18==-999,seaice_data_V2_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V2_18, lats_V2_18, seaice_data_V2_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V2_18_Med['Traj Lon'], Traj_V2_18_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_Med['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V2_18_Med['Traj Lon'], Traj_V2_18_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_Med['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V2 (Casey)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_18_Med)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 7
ax = plt.subplot(gs[1,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_18M = np.ma.masked_where(seaice_data_V3_18M==-999,seaice_data_V3_18M)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_18M, lats_V3_18M, seaice_data_V3_18M, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_18M_Med['Traj Lon'], Traj_V3_18M_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M_Med['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_18M_Med['Traj Lon'], Traj_V3_18M_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M_Med['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Mawson)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18M_Med)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 8
ax = plt.subplot(gs[1,3], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_18D = np.ma.masked_where(seaice_data_V3_18D==-999,seaice_data_V3_18D)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_18D, lats_V3_18D, seaice_data_V3_18D, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_18D_Med['Traj Lon'], Traj_V3_18D_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18D_Med['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_18D_Med['Traj Lon'], Traj_V3_18D_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D_Med['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18D_Med)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "h", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 9
ax = plt.subplot(gs[2,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V1_18 = np.ma.masked_where(seaice_data_V1_18==-999,seaice_data_V1_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V1_18, lats_V1_18, seaice_data_V1_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

cs2 = ax.scatter(Traj_V1_18_P95['Traj Lon'], Traj_V1_18_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P95['Traj Height (m)'], label='Traj Height (m)')
#cs2 = ax.scatter(Traj_V1_18_P95['Traj Lon'], Traj_V1_18_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P95['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V1 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "       90$^t$$^h$ percentile       ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_18_P95)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "i", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 10
ax = plt.subplot(gs[2,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)
ax.set_facecolor('lightgrey')

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V2_18 = np.ma.masked_where(seaice_data_V2_18==-999,seaice_data_V2_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V2_18, lats_V2_18, seaice_data_V2_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V2_18_P95['Traj Lon'], Traj_V2_18_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P95['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V2_18_P95['Traj Lon'], Traj_V2_18_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P95['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V2 (Casey)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_18_P95)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "j", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 11
ax = plt.subplot(gs[2,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_18M = np.ma.masked_where(seaice_data_V3_18M==-999,seaice_data_V3_18M)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_18M, lats_V3_18M, seaice_data_V3_18M, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration


ax.scatter(Traj_V3_18M_P95['Traj Lon'], Traj_V3_18M_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M_P95['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_18M_P95['Traj Lon'], Traj_V3_18M_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M_P95['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Mawson)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18M_P95)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "k", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 12
ax = plt.subplot(gs[2,3], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V3_18D = np.ma.masked_where(seaice_data_V3_18D==-999,seaice_data_V3_18D)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V3_18D, lats_V3_18D, seaice_data_V3_18D, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
#cmap = plt.cm.viridis
cmap = plt.cm.autumn_r

norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
#norm = BoundaryNorm(np.arange(0,7.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_18D_P95['Traj Lon'], Traj_V3_18D_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18D_P95['Traj Height (m)'], label='Traj Height (m)')
#ax.scatter(Traj_V3_18D_P95['Traj Lon'], Traj_V3_18D_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D_P95['surf_vmr(ppmv)'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("V3 (Davis)", y=1.1, fontsize=15)
#cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18D_P95)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "l", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
#cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,1.0,2.0,3.0,4.0,5.0,6.0,7.0], pad = 0.08, shrink=.995) # Hg0 concentration
#cb.set_label('BrO (pptv)') # Hg$^0$ (ng/m$^3$)
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,500,1000,1500,2000,2500,3000,3500,4000], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Height (MSL)') # Hg$^0$ (ng/m$^3$)
