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
import matplotlib as mpl
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
import mpld3
from mpld3 import plugins, utils

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

#-------------
# Sea Ice
#-------------

SeaIce_V1_17   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20171114.nc', decode_cf=False, engine='netcdf4')
SeaIce_V2_17   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20171221.nc', decode_cf=False, engine='netcdf4')
SeaIce_V3_17M  = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20180201.nc', decode_cf=False, engine='netcdf4')
SeaIce_V3_17D  = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20180127.nc', decode_cf=False, engine='netcdf4')
SeaIce_V4_17   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20180312.nc', decode_cf=False, engine='netcdf4')

SeaIce_V1_18   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20181107.nc', decode_cf=False, engine='netcdf4')
SeaIce_V2_18   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20181215.nc', decode_cf=False, engine='netcdf4')
SeaIce_V3_18M  = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20190130.nc', decode_cf=False, engine='netcdf4')
SeaIce_V3_18D  = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20190126.nc', decode_cf=False, engine='netcdf4')
SeaIce_V4_18   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2018-19/oisst-avhrr-v02r01.20190308.nc', decode_cf=False, engine='netcdf4')

SeaIce_PCAN    = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/Hamburg_ICDC/20170126_median5day.nc', decode_cf=False, engine='netcdf4')
#SeaIce_PCAN    = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2017-18/oisst-avhrr-v02r01.20170126.nc', decode_cf=False, engine='netcdf4') #20170126
SeaIce_SIPEXII = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/OISST_SeaIce/2012/oisst-avhrr-v02r01.20120923.nc', decode_cf=False, engine='netcdf4')

#--------------
# Met
#--------------
Met_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/ShipTrack/SIPEXII_underway_60.csv', index_col=0) 
Met_PCAN    = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/ShipTrack/PCAN_underway_60.csv', index_col=0) 

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

#--------------
# Met
#--------------
Met_SIPEXII.index = (pd.to_datetime(Met_SIPEXII.index, dayfirst=True) + timedelta(hours=8))  # SIPEXII timezone is UT+8
Met_PCAN.index    = (pd.to_datetime(Met_PCAN.index,    dayfirst=True) + timedelta(hours=8))  # PCAN timezone is UT+8

#------------------------------------------------------------------------------
# PASSIVATION ISSUE WITH CELL A ON VOYAGES V3_18M, V3_18D and V4_18 (FILTER DATA)

Filter1    = Hg0_V3_18M['Cart'] == "B"
Hg0_V3_18M = Hg0_V3_18M[Filter1]

Filter2    = Hg0_V3_18D['Cart'] == "B"
Hg0_V3_18D = Hg0_V3_18D[Filter2]

Filter3    = Hg0_V4_18['Cart'] == "B"
Hg0_V4_18  = Hg0_V4_18[Filter3]

#------------------------------------------------------------------------------
# RESAMPLE THE Hg0 DATASETS TO 1-HOUR TIME RESOLUTION

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
# RESAMPLE THE MET DATASETS TO 1-DAY MEANS

#--------------
# Met
#--------------
Met_SIPEXII = Met_SIPEXII.resample('D').mean()
Met_PCAN    = Met_PCAN.resample('D').mean()

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
Mawson           = (Hg0_V3_17M.index >= start_date) & (Hg0_V3_17M.index < end_date)
Hg0_Mawson_V3_17 = Hg0_V3_17M[Mawson]

#-----------------------------
# V3_17 Davis (27-30 Jan 2018 and 19-21 Feb 2018)
#-----------------------------
start_date1   = '2018-01-27'
end_date1     = '2018-01-31'
start_date2   = '2018-02-19'
end_date2     = '2018-02-22'
# Hg0
Davis1          = (Hg0_V3_17D.index >= start_date1) & (Hg0_V3_17D.index < end_date1)
Davis2          = (Hg0_V3_17D.index >= start_date2) & (Hg0_V3_17D.index < end_date2)
Hg0_Davis_1     = Hg0_V3_17D[Davis1]
Hg0_Davis_2     = Hg0_V3_17D[Davis2]
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
Mawson           = (Hg0_V3_18M.index >= start_date) & (Hg0_V3_18M.index < end_date)
Hg0_Mawson_V3_18 = Hg0_V3_18M[Mawson]

#-----------------------------
# V3_18 Davis (26-28 Jan 2019 and 19-20 Feb 2019)
#-----------------------------
start_date1   = '2019-01-26'
end_date1     = '2019-01-29'
start_date2   = '2019-02-19'
end_date2     = '2019-02-21'
# Hg0
Davis1          = (Hg0_V3_18D.index >= start_date1) & (Hg0_V3_18D.index < end_date1)
Davis2          = (Hg0_V3_18D.index >= start_date2) & (Hg0_V3_18D.index < end_date2)
Hg0_Davis_1     = Hg0_V3_18D[Davis1]
Hg0_Davis_2     = Hg0_V3_18D[Davis2]
Hg0_Davis_V3_18 = pd.concat([Hg0_Davis_1,Hg0_Davis_2], axis =0)

#-----------------------------
# V4_18 Macquarie Island (5-25 Mar 2019) (8-22 Mar 2019 on station)
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
# Met
SIPEX           = (Met_SIPEXII.index >= start_date) & (Met_SIPEXII.index < end_date)
Met_SIPEXII_Ice = Met_SIPEXII[SIPEX]

#-----------------------------
# PCAN (26 Jan to 24 Feb 2017)
#-----------------------------
start_date     = '2017-01-26'
end_date       = '2017-02-25'
# Hg0
PCAN         = (Hg0_PCAN.index >= start_date) & (Hg0_PCAN.index < end_date)
Hg0_PCAN_Ice = Hg0_PCAN[PCAN]
# Met
PCAN         = (Met_PCAN.index >= start_date) & (Met_PCAN.index < end_date)
Met_PCAN_Ice = Met_PCAN[PCAN]

#------------------------------------------------------------------------------
# BACK TRAJECTORIES CAMMPCAN (2017-18)

# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/10m/")

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
    filename = 'gdas1nov0010spring' + dateA + '.csv'
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
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V1_17)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
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
    filename = 'gdas1dec0010summer' + dateA + '.csv'
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
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V2_17)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
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
    filename = 'gdas1dec0010summer' + dateA + '.csv'
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
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V2_17)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
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
    filename = 'gdas1jan0010summer' + dateA + '.csv'
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
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V2_17)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
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
    filename = 'gdas1feb0010summer' + dateA + '.csv'
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
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V3_17M)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
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
    filename = 'gdas1jan0010summer' + dateA + '.csv'
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
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V3_17D)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
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
    filename = 'gdas1feb0010summer' + dateA + '.csv'
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
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V3_17D)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)
    
# Combine all the files
Traj_V3_17Db = pd.concat(Traj)

# Append V3_17Da and V3_17Db
Traj_V3_17D = Traj_V3_17Da.append(Traj_V3_17Db)

#-------------
# V4_17
#-------------
start_V4_17   = '2018031211'
end_V4_17     = '2018032111'

start_date    = datetime.strptime(start_V4_17, DATE_FORMAT)
end_date      = datetime.strptime(end_V4_17,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1mar0010autumn' + dateA + '.csv'
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
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=11)) # Macquarie Island timezone is UT+11
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
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V4_17)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V4_17 = pd.concat(Traj)

#------------------------------------------------------------------------------
# BACK TRAJECTORIES CAMMPCAN (2018-19)

# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/10m/")

#-------------
# V1_18
#-------------
start_V1_18   = '2018110707'
end_V1_18     = '2018111607'

start_date    = datetime.strptime(start_V1_18, DATE_FORMAT)
end_date      = datetime.strptime(end_V1_18,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0010spring' + dateA + '.csv'
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
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
        # Percentage time over Land, Ice Ocean
    file['Land_Percentage']   = file['Over_Land']/121
    file['SeaIce_Percentage'] = file['Over_SeaIce']/121
    file['Ocean_Percentage']  = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V1_18)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V1_18 = pd.concat(Traj)

#-------------
# V2_18
#-------------
start_V2_18   = '2018121508'
end_V2_18     = '2018123108'

start_date    = datetime.strptime(start_V2_18, DATE_FORMAT)
end_date      = datetime.strptime(end_V2_18,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1dec0010summer' + dateA + '.csv'
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
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
        # Percentage time over Land, Ice Ocean
    file['Land_Percentage']   = file['Over_Land']/121
    file['SeaIce_Percentage'] = file['Over_SeaIce']/121
    file['Ocean_Percentage']  = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V2_18)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V2_18 = pd.concat(Traj)

#-------------
# V3_18M
#-------------
start_V3_18Ma  = '2019013005'
end_V3_18Ma    = '2019013123'

start_date    = datetime.strptime(start_V3_18Ma, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_18Ma,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0010summer' + dateA + '.csv'
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
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
        # Percentage time over Land, Ice Ocean
    file['Land_Percentage']   = file['Over_Land']/121
    file['SeaIce_Percentage'] = file['Over_SeaIce']/121
    file['Ocean_Percentage']  = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V3_18M)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_18Ma = pd.concat(Traj)

start_V3_18Mb  = '2019020100'
end_V3_18Mb    = '2019021005'

start_date    = datetime.strptime(start_V3_18Mb, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_18Mb,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0010summer' + dateA + '.csv'
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
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
        # Percentage time over Land, Ice Ocean
    file['Land_Percentage']   = file['Over_Land']/121
    file['SeaIce_Percentage'] = file['Over_SeaIce']/121
    file['Ocean_Percentage']  = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V3_18M)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_18Mb = pd.concat(Traj)

# Append V3_18Ma and V3_18Mb
Traj_V3_18M = Traj_V3_18Ma.append(Traj_V3_18Mb)

#-------------
# V3_18D
#-------------
start_V3_18Da = '2019012607'
end_V3_18Da   = '2019012907'

start_date    = datetime.strptime(start_V3_18Da, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_18Da,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0010summer' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

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
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
        # Percentage time over Land, Ice Ocean
    file['Land_Percentage']   = file['Over_Land']/121
    file['SeaIce_Percentage'] = file['Over_SeaIce']/121
    file['Ocean_Percentage']  = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V3_18D)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_18Da = pd.concat(Traj)

start_V3_18Db = '2019021907'
end_V3_18Db   = '2019022107'

start_date    = datetime.strptime(start_V3_18Db, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_18Db,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0010summer' + dateA + '.csv'
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
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
        # Percentage time over Land, Ice Ocean
    file['Land_Percentage']   = file['Over_Land']/121
    file['SeaIce_Percentage'] = file['Over_SeaIce']/121
    file['Ocean_Percentage']  = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V3_18D)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_18Db = pd.concat(Traj)

# Append V3_18Da and V3_18Db
Traj_V3_18D = Traj_V3_18Da.append(Traj_V3_18Db)

#-------------
# V4_18
#-------------
start_V4_18   = '2019030811'
end_V4_18     = '2019032311'

start_date    = datetime.strptime(start_V4_18, DATE_FORMAT)
end_date      = datetime.strptime(end_V4_18,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1mar0010autumn' + dateA + '.csv'
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
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=11)) # Macquarie Island timezone is UT+11
    # Sum the ice contact time (hours)
    file['Over_SeaIce']      = np.sum(file['Traj over Sea Ice?'])
    file['IceContact_100m']  = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    file['IceContact_MLH']   = np.sum(file['Traj over Sea Ice and height < mixed layer top?'])
    # Sum the land contact time (hours)
    file['Over_Land']        = np.sum(file['Traj over Ice Sheet?'])
    file['Land_MLH']         = np.sum(file['Traj over Ice Sheet and height < mixed layer top?'])
    # Calculate if traj over ocean
    file['Traj over Ocean?'] = 1 - (file['Traj over Sea Ice?'] + file['Traj over Ice Sheet?'])
    # Sum the ocean contact time (hours)
    file['Over_Ocean']      = np.sum(file['Traj over Ocean?'])
    # Percentage time over Land, Ice Ocean
    file['Land_Percentage']   = file['Over_Land']/121
    file['SeaIce_Percentage'] = file['Over_SeaIce']/121
    file['Ocean_Percentage']  = file['Over_Ocean']/121
    # Weighting for Traj Age
    file['Weighting']        = (file['Traj Age'].values[::-1] - 1) * -1
    # Weighted Land, Ice and Ocean values
    file['Weighted_Ice']     = np.sum(file['Weighting']*file['Traj over Sea Ice?']/121)
    file['Weighted_Land']    = np.sum(file['Weighting']*file['Traj over Ice Sheet?']/121)
    file['Weighted_Ocean']   = np.sum(file['Weighting']*file['Traj over Ocean?']/121)
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V4_18)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V4_18 = pd.concat(Traj)

#------------------------------------------------------------------------------
#BACK TRAJECTORIES PCAN (2017)

# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/Trajectories/PCAN/")

#-------------
# PCAN
#-------------
start_PCANa    = '2017012608'
end_PCANa      = '2017013123'

start_date    = datetime.strptime(start_PCANa, DATE_FORMAT)
end_date      = datetime.strptime(end_PCANa,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0020summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=11, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2017    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=11)) # Macqurie Island timezone is UT+11
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_PCAN)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_PCANa = pd.concat(Traj)

start_PCANb    = '2017020100'
end_PCANb      = '2017021718'

start_date    = datetime.strptime(start_PCANb, DATE_FORMAT)
end_date      = datetime.strptime(end_PCANb,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0020summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=11, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2017    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=11)) # Macqurie Island timezone is UT+11
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V4_18)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_PCANb = pd.concat(Traj)

start_PCANc    = '2017021723'
end_PCANc      = '2017022523'

start_date    = datetime.strptime(start_PCANc, DATE_FORMAT)
end_date      = datetime.strptime(end_PCANc,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0020summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=11, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2017    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=11)) # Macqurie Island timezone is UT+11
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V4_18)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_PCANc = pd.concat(Traj)
    
# Append PCANa and PCANb
Traj_PCAN = Traj_PCANa.append(Traj_PCANb)
Traj_PCAN = Traj_PCAN.append(Traj_PCANc)

#------------------------------------------------------------------------------
# DROP ROWS WHERE BrO CONCENTRATION IS MISSING

Traj_V1_17  = Traj_V1_17[Traj_V1_17['ng/m3'].notna()]
Traj_V2_17  = Traj_V2_17[Traj_V2_17['ng/m3'].notna()]
Traj_V3_17M = Traj_V3_17M[Traj_V3_17M['ng/m3'].notna()]
Traj_V3_17D = Traj_V3_17D[Traj_V3_17D['ng/m3'].notna()]
Traj_V4_17  = Traj_V4_17[Traj_V4_17['ng/m3'].notna()]

Traj_V1_18  = Traj_V1_18[Traj_V1_18['ng/m3'].notna()]
Traj_V2_18  = Traj_V2_18[Traj_V2_18['ng/m3'].notna()]
Traj_V3_18M = Traj_V3_18M[Traj_V3_18M['ng/m3'].notna()]
Traj_V3_18D = Traj_V3_18D[Traj_V3_18D['ng/m3'].notna()]
Traj_V4_18  = Traj_V4_18[Traj_V4_18['ng/m3'].notna()]

Traj_PCAN   = Traj_PCAN[Traj_PCAN['ng/m3'].notna()]

#------------------------------------------------------------------------------
# SEPERATE TRAJECTORIES INTO LAND, SEA ICE and OCEAN AIR MASSES

#-------------------------------
# By Percentage time spent over (Land, Ice, Ocean)
#-------------------------------
# SeaIce
SeaIce1       = (Traj_V1_17['SeaIce_Percentage']  > Traj_V1_17['Land_Percentage'])  & (Traj_V1_17['SeaIce_Percentage']  > Traj_V1_17['Ocean_Percentage'])
Traj_V1_17SI  = Traj_V1_17[SeaIce1]

SeaIce2       = (Traj_V2_17['SeaIce_Percentage']  > Traj_V2_17['Land_Percentage'])  & (Traj_V2_17['SeaIce_Percentage']  > Traj_V2_17['Ocean_Percentage'])
Traj_V2_17SI  = Traj_V2_17[SeaIce2]

SeaIce3       = (Traj_V3_17M['SeaIce_Percentage'] > Traj_V3_17M['Land_Percentage']) & (Traj_V3_17M['SeaIce_Percentage'] > Traj_V3_17M['Ocean_Percentage'])
Traj_V3_17MSI = Traj_V3_17M[SeaIce3]

SeaIce4       = (Traj_V3_17D['SeaIce_Percentage'] > Traj_V3_17D['Land_Percentage']) & (Traj_V3_17D['SeaIce_Percentage'] > Traj_V3_17D['Ocean_Percentage'])
Traj_V3_17DSI = Traj_V3_17D[SeaIce4]

SeaIce5       = (Traj_V1_18['SeaIce_Percentage']  > Traj_V1_18['Land_Percentage'])  & (Traj_V1_18['SeaIce_Percentage']  > Traj_V1_18['Ocean_Percentage'])
Traj_V1_18SI  = Traj_V1_18[SeaIce5]

SeaIce6       = (Traj_V2_18['SeaIce_Percentage']  > Traj_V2_18['Land_Percentage'])  & (Traj_V2_18['SeaIce_Percentage']  > Traj_V2_18['Ocean_Percentage'])
Traj_V2_18SI  = Traj_V2_18[SeaIce6]

SeaIce7       = (Traj_V3_18M['SeaIce_Percentage'] > Traj_V3_18M['Land_Percentage']) & (Traj_V3_18M['SeaIce_Percentage'] > Traj_V3_18M['Ocean_Percentage'])
Traj_V3_18MSI = Traj_V3_18M[SeaIce7]

SeaIce8       = (Traj_V3_18D['SeaIce_Percentage'] > Traj_V3_18D['Land_Percentage']) & (Traj_V3_18D['SeaIce_Percentage'] > Traj_V3_18D['Ocean_Percentage'])
Traj_V3_18DSI = Traj_V3_18D[SeaIce8]

# Land
Land1        = (Traj_V1_17['Land_Percentage']  > Traj_V1_17['SeaIce_Percentage'])  & (Traj_V1_17['Land_Percentage']  > Traj_V1_17['Ocean_Percentage'])
Traj_V1_17L  = Traj_V1_17[Land1]

Land2        = (Traj_V2_17['Land_Percentage']  > Traj_V2_17['SeaIce_Percentage'])  & (Traj_V2_17['Land_Percentage']  > Traj_V2_17['Ocean_Percentage'])
Traj_V2_17L  = Traj_V2_17[Land2]

Land3        = (Traj_V3_17M['Land_Percentage'] > Traj_V3_17M['SeaIce_Percentage']) & (Traj_V3_17M['Land_Percentage'] > Traj_V3_17M['Ocean_Percentage'])
Traj_V3_17ML = Traj_V3_17M[Land3]

Land4        = (Traj_V3_17D['Land_Percentage'] > Traj_V3_17D['SeaIce_Percentage']) & (Traj_V3_17D['Land_Percentage'] > Traj_V3_17D['Ocean_Percentage'])
Traj_V3_17DL = Traj_V3_17D[Land4]

Land5        = (Traj_V1_18['Land_Percentage']  > Traj_V1_18['SeaIce_Percentage'])  & (Traj_V1_18['Land_Percentage']  > Traj_V1_18['Ocean_Percentage'])
Traj_V1_18L  = Traj_V1_18[Land5]

Land6        = (Traj_V2_18['Land_Percentage']  > Traj_V2_18['SeaIce_Percentage'])  & (Traj_V2_18['Land_Percentage']  > Traj_V2_18['Ocean_Percentage'])
Traj_V2_18L  = Traj_V2_18[Land6]

Land7        = (Traj_V3_18M['Land_Percentage'] > Traj_V3_18M['SeaIce_Percentage']) & (Traj_V3_18M['Land_Percentage'] > Traj_V3_18M['Ocean_Percentage'])
Traj_V3_18ML = Traj_V3_18M[Land7]

Land8        = (Traj_V3_18D['Land_Percentage'] > Traj_V3_18D['SeaIce_Percentage']) & (Traj_V3_18D['Land_Percentage'] > Traj_V3_18D['Ocean_Percentage'])
Traj_V3_18DL = Traj_V3_18D[Land8]

# Ocean
Ocean1       = (Traj_V1_17['Ocean_Percentage']  > Traj_V1_17['SeaIce_Percentage'])  & (Traj_V1_17['Ocean_Percentage']  > Traj_V1_17['Land_Percentage'])
Traj_V1_17O  = Traj_V1_17[Ocean1]

Ocean2       = (Traj_V2_17['Ocean_Percentage']  > Traj_V2_17['SeaIce_Percentage'])  & (Traj_V2_17['Ocean_Percentage']  > Traj_V2_17['Land_Percentage'])
Traj_V2_17O  = Traj_V2_17[Ocean2]

Ocean3       = (Traj_V3_17M['Ocean_Percentage'] > Traj_V3_17M['SeaIce_Percentage']) & (Traj_V3_17M['Ocean_Percentage'] > Traj_V3_17M['Land_Percentage'])
Traj_V3_17MO = Traj_V3_17M[Ocean3]

Ocean4       = (Traj_V3_17D['Ocean_Percentage'] > Traj_V3_17D['SeaIce_Percentage']) & (Traj_V3_17D['Ocean_Percentage'] > Traj_V3_17D['Land_Percentage'])
Traj_V3_17DO = Traj_V3_17D[Ocean4]

Ocean5       = (Traj_V1_18['Ocean_Percentage']  > Traj_V1_18['SeaIce_Percentage'])  & (Traj_V1_18['Ocean_Percentage']  > Traj_V1_18['Land_Percentage'])
Traj_V1_18O  = Traj_V1_18[Ocean5]

Ocean6       = (Traj_V2_18['Ocean_Percentage']  > Traj_V2_18['SeaIce_Percentage'])  & (Traj_V2_18['Ocean_Percentage']  > Traj_V2_18['Land_Percentage'])
Traj_V2_18O  = Traj_V2_18[Ocean6]

Ocean7       = (Traj_V3_18M['Ocean_Percentage'] > Traj_V3_18M['SeaIce_Percentage']) & (Traj_V3_18M['Ocean_Percentage'] > Traj_V3_18M['Land_Percentage'])
Traj_V3_18MO = Traj_V3_18M[Ocean7]

Ocean8       = (Traj_V3_18D['Ocean_Percentage'] > Traj_V3_18D['SeaIce_Percentage']) & (Traj_V3_18D['Ocean_Percentage'] > Traj_V3_18D['Land_Percentage'])
Traj_V3_18DO = Traj_V3_18D[Ocean8]

#------------------------------------------------------------------------------
# GET TRAJECTORIES FOR ONLY TRAJ AGE = 0

# CAMMPCAN 2017-18
Filter1         = Traj_V1_17['Traj Age']  == 0.0
Traj_V1_17_B    = Traj_V1_17[Filter1]

Filter1         = Traj_V2_17['Traj Age']  == 0.0
Traj_V2_17_B    = Traj_V2_17[Filter1]

Filter1         = Traj_V3_17M['Traj Age']  == 0.0
Traj_V3_17M_B   = Traj_V3_17M[Filter1]

Filter1         = Traj_V3_17D['Traj Age']  == 0.0
Traj_V3_17D_B   = Traj_V3_17D[Filter1]

Filter1         = Traj_V4_17['Traj Age']  == 0.0
Traj_V4_17_B    = Traj_V4_17[Filter1]

# CAMMPCAN 2018-19
Filter1         = Traj_V1_18['Traj Age']  == 0.0
Traj_V1_18_B    = Traj_V1_18[Filter1]

Filter1         = Traj_V2_18['Traj Age']  == 0.0
Traj_V2_18_B    = Traj_V2_18[Filter1]

Filter1         = Traj_V3_18M['Traj Age']  == 0.0
Traj_V3_18M_B   = Traj_V3_18M[Filter1]

Filter1         = Traj_V3_18D['Traj Age']  == 0.0
Traj_V3_18D_B   = Traj_V3_18D[Filter1]

Filter1         = Traj_V4_18['Traj Age']  == 0.0
Traj_V4_18_B    = Traj_V4_18[Filter1]

# PCAN
Filter1         = Traj_PCAN['Traj Age']  == 0.0
Traj_PCAN_B     = Traj_PCAN[Filter1]

# Sea Ice
Filter1         = Traj_V1_17SI['Traj Age']  == 0.0
Traj_V1_17SI_B  = Traj_V1_17SI[Filter1]

Filter1         = Traj_V2_17SI['Traj Age']  == 0.0
Traj_V2_17SI_B  = Traj_V2_17SI[Filter1]

Filter1         = Traj_V3_17MSI['Traj Age'] == 0.0
Traj_V3_17MSI_B = Traj_V3_17MSI[Filter1]

Filter1         = Traj_V3_17DSI['Traj Age'] == 0.0
Traj_V3_17DSI_B = Traj_V3_17DSI[Filter1]

Filter1         = Traj_V1_18SI['Traj Age']  == 0.0
Traj_V1_18SI_B  = Traj_V1_18SI[Filter1]

Filter1         = Traj_V2_18SI['Traj Age']  == 0.0
Traj_V2_18SI_B  = Traj_V2_18SI[Filter1]

Filter1         = Traj_V3_18MSI['Traj Age'] == 0.0
Traj_V3_18MSI_B = Traj_V3_18MSI[Filter1]

Filter1         = Traj_V3_18DSI['Traj Age'] == 0.0
Traj_V3_18DSI_B = Traj_V3_18DSI[Filter1]

# Land
Filter1         = Traj_V1_17L['Traj Age']  == 0.0
Traj_V1_17L_B   = Traj_V1_17L[Filter1]

Filter1         = Traj_V2_17L['Traj Age']  == 0.0
Traj_V2_17L_B   = Traj_V2_17L[Filter1]

Filter1         = Traj_V3_17ML['Traj Age'] == 0.0
Traj_V3_17ML_B  = Traj_V3_17ML[Filter1]

Filter1         = Traj_V3_17DL['Traj Age'] == 0.0
Traj_V3_17DL_B  = Traj_V3_17DL[Filter1]

Filter1         = Traj_V1_18L['Traj Age']  == 0.0
Traj_V1_18L_B   = Traj_V1_18L[Filter1]

Filter1         = Traj_V2_18L['Traj Age']  == 0.0
Traj_V2_18L_B   = Traj_V2_18L[Filter1]

Filter1         = Traj_V3_18ML['Traj Age'] == 0.0
Traj_V3_18ML_B  = Traj_V3_18ML[Filter1]

Filter1         = Traj_V3_18DL['Traj Age'] == 0.0
Traj_V3_18DL_B  = Traj_V3_18DL[Filter1]

# Ocean
Filter1         = Traj_V1_17O['Traj Age']  == 0.0
Traj_V1_17O_B   = Traj_V1_17O[Filter1]

Filter1         = Traj_V2_17O['Traj Age']  == 0.0
Traj_V2_17O_B   = Traj_V2_17O[Filter1]

Filter1         = Traj_V3_17MO['Traj Age'] == 0.0
Traj_V3_17MO_B  = Traj_V3_17MO[Filter1]

Filter1         = Traj_V3_17DO['Traj Age'] == 0.0
Traj_V3_17DO_B  = Traj_V3_17DO[Filter1]

Filter1         = Traj_V1_18O['Traj Age']  == 0.0
Traj_V1_18O_B   = Traj_V1_18O[Filter1]

Filter1         = Traj_V2_18O['Traj Age']  == 0.0
Traj_V2_18O_B   = Traj_V2_18O[Filter1]

Filter1         = Traj_V3_18MO['Traj Age'] == 0.0
Traj_V3_18MO_B  = Traj_V3_18MO[Filter1]

Filter1         = Traj_V3_18DO['Traj Age'] == 0.0
Traj_V3_18DO_B  = Traj_V3_18DO[Filter1]

#------------------------------------------------------------------------------
# GET THE CAMMPCAN TOTALS

#---------------
# Overall
#---------------
# 2017-18
All_1718 = Traj_V1_17_B.append(Traj_V2_17_B)
All_1718 = All_1718.append(Traj_V3_17M_B)
All_1718 = All_1718.append(Traj_V3_17D_B)
# 2018-19
All_1819 = Traj_V1_18_B.append(Traj_V2_18_B)
All_1819 = All_1819.append(Traj_V3_18M_B)
All_1819 = All_1819.append(Traj_V3_18D_B)
# CAMMPCAN Overall
CAMMPCAN_All = All_1718.append(All_1819)

#---------------
# Sea Ice
#---------------
# 2017-18
SeaIce_1718 = Traj_V1_17SI_B.append(Traj_V2_17SI_B)
SeaIce_1718 = SeaIce_1718.append(Traj_V3_17MSI_B)
SeaIce_1718 = SeaIce_1718.append(Traj_V3_17DSI_B)
# 2018-19
SeaIce_1819 = Traj_V1_18SI_B.append(Traj_V2_18SI_B)
SeaIce_1819 = SeaIce_1819.append(Traj_V3_18MSI_B)
SeaIce_1819 = SeaIce_1819.append(Traj_V3_18DSI_B)
# CAMMPCAN Overall
SeaIce_All  = SeaIce_1718.append(SeaIce_1819)

#---------------
# Land
#---------------
# 2017-18
Land_1718  = Traj_V1_17L_B.append(Traj_V2_17L_B)
Land_1718  = Land_1718.append(Traj_V3_17ML_B)
Land_1718  = Land_1718.append(Traj_V3_17DL_B)
# 2018-19
Land_1819  = Traj_V1_18L_B.append(Traj_V2_18L_B)
Land_1819  = Land_1819.append(Traj_V3_18ML_B)
Land_1819  = Land_1819.append(Traj_V3_18DL_B)
# CAMMPCAN Overall
Land_All   = Land_1718.append(Land_1819)

#---------------
# Ocean
#---------------
# 2017-18
Ocean_1718 = Traj_V1_17O_B.append(Traj_V2_17O_B)
Ocean_1718 = Ocean_1718.append(Traj_V3_17MO_B)
Ocean_1718 = Ocean_1718.append(Traj_V3_17DO_B)
# 2018-19
Ocean_1819 = Traj_V1_18O_B.append(Traj_V2_18O_B)
Ocean_1819 = Ocean_1819.append(Traj_V3_18MO_B)
Ocean_1819 = Ocean_1819.append(Traj_V3_18DO_B)
# CAMMPCAN Overall
Ocean_All  = Ocean_1718.append(Ocean_1819)

#------------------------------------------------------------------------------
# COUNT THE NUMBER OF OBSERVATIONS SEA ICE, LAND OCEAN

# Sea Ice
N_V1_17SI  = len(Traj_V1_17SI_B)
N_V2_17SI  = len(Traj_V2_17SI_B)
N_V3_17MSI = len(Traj_V3_17MSI_B)
N_V3_17DSI = len(Traj_V3_17DSI_B)

N_V1_18SI  = len(Traj_V1_18SI_B)
N_V2_18SI  = len(Traj_V2_18SI_B)
N_V3_18MSI = len(Traj_V3_18MSI_B)
N_V3_18DSI = len(Traj_V3_18DSI_B)

N_SeaIce_1718 = len(SeaIce_1718)
N_SeaIce_1819 = len(SeaIce_1819)
N_SeaIce_All  = len(SeaIce_All)

# Land
N_V1_17L   = len(Traj_V1_17L_B)
N_V2_17L   = len(Traj_V2_17L_B)
N_V3_17ML  = len(Traj_V3_17ML_B)
N_V3_17DL  = len(Traj_V3_17DL_B)

N_V1_18L   = len(Traj_V1_18L_B)
N_V2_18L   = len(Traj_V2_18L_B)
N_V3_18ML  = len(Traj_V3_18ML_B)
N_V3_18DL  = len(Traj_V3_18DL_B)

N_Land_1718   = len(Land_1718)
N_Land_1819   = len(Land_1819)
N_Land_All    = len(Land_All)

# Ocean
N_V1_17O   = len(Traj_V1_17O_B)
N_V2_17O   = len(Traj_V2_17O_B)
N_V3_17MO  = len(Traj_V3_17MO_B)
N_V3_17DO  = len(Traj_V3_17DO_B)

N_V1_18O   = len(Traj_V1_18O_B)
N_V2_18O   = len(Traj_V2_18O_B)
N_V3_18MO  = len(Traj_V3_18MO_B)
N_V3_18DO  = len(Traj_V3_18DO_B)

N_Ocean_1718  = len(Ocean_1718)
N_Ocean_1819  = len(Ocean_1819)
N_Ocean_All   = len(Ocean_All)

#------------------------------------------------------------------------------
# CALCULATE THE MEAN HG0 (SEA ICE, LAND, OCEAN)

# Sea Ice
Mean_V1_17SI  = np.mean(Traj_V1_17SI_B['ng/m3'])
Mean_V2_17SI  = np.mean(Traj_V2_17SI_B['ng/m3'])
Mean_V3_17MSI = np.mean(Traj_V3_17MSI_B['ng/m3'])
Mean_V3_17DSI = np.mean(Traj_V3_17DSI_B['ng/m3'])

Mean_V1_18SI  = np.mean(Traj_V1_18SI_B['ng/m3'])
Mean_V2_18SI  = np.mean(Traj_V2_18SI_B['ng/m3'])
Mean_V3_18MSI = np.mean(Traj_V3_18MSI_B['ng/m3'])
Mean_V3_18DSI = np.mean(Traj_V3_18DSI_B['ng/m3'])

Mean_SeaIce_1718 = np.mean(SeaIce_1718['ng/m3'])
Mean_SeaIce_1819 = np.mean(SeaIce_1819['ng/m3'])
Mean_SeaIce_All  = np.mean(SeaIce_All['ng/m3'])

# Land
Mean_V1_17L   = np.mean(Traj_V1_17L_B['ng/m3'])
Mean_V2_17L   = np.mean(Traj_V2_17L_B['ng/m3'])
Mean_V3_17ML  = np.mean(Traj_V3_17ML_B['ng/m3'])
Mean_V3_17DL  = np.mean(Traj_V3_17DL_B['ng/m3'])

Mean_V1_18L   = np.mean(Traj_V1_18L_B['ng/m3'])
Mean_V2_18L   = np.mean(Traj_V2_18L_B['ng/m3'])
Mean_V3_18ML  = np.mean(Traj_V3_18ML_B['ng/m3'])
Mean_V3_18DL  = np.mean(Traj_V3_18DL_B['ng/m3'])

Mean_Land_1718 = np.mean(Land_1718['ng/m3'])
Mean_Land_1819 = np.mean(Land_1819['ng/m3'])
Mean_Land_All  = np.mean(Land_All['ng/m3'])

# Ocean
Mean_V1_17O   = np.mean(Traj_V1_17O_B['ng/m3'])
Mean_V2_17O   = np.mean(Traj_V2_17O_B['ng/m3'])
Mean_V3_17MO  = np.mean(Traj_V3_17MO_B['ng/m3'])
Mean_V3_17DO  = np.mean(Traj_V3_17DO_B['ng/m3'])

Mean_V1_18O   = np.mean(Traj_V1_18O_B['ng/m3'])
Mean_V2_18O   = np.mean(Traj_V2_18O_B['ng/m3'])
Mean_V3_18MO  = np.mean(Traj_V3_18MO_B['ng/m3'])
Mean_V3_18DO  = np.mean(Traj_V3_18DO_B['ng/m3'])

Mean_Ocean_1718 = np.mean(Ocean_1718['ng/m3'])
Mean_Ocean_1819 = np.mean(Ocean_1819['ng/m3'])
Mean_Ocean_All  = np.mean(Ocean_All['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN HG0  (SEA ICE, LAND, OCEAN)

# Sea Ice
Median_V1_17SI  = np.median(Traj_V1_17SI_B['ng/m3'])
Median_V2_17SI  = np.median(Traj_V2_17SI_B['ng/m3'])
Median_V3_17MSI = np.median(Traj_V3_17MSI_B['ng/m3'])
Median_V3_17DSI = np.median(Traj_V3_17DSI_B['ng/m3'])

Median_V1_18SI  = np.median(Traj_V1_18SI_B['ng/m3'])
Median_V2_18SI  = np.median(Traj_V2_18SI_B['ng/m3'])
Median_V3_18MSI = np.median(Traj_V3_18MSI_B['ng/m3'])
Median_V3_18DSI = np.median(Traj_V3_18DSI_B['ng/m3'])

Median_SeaIce_1718 = np.median(SeaIce_1718['ng/m3'])
Median_SeaIce_1819 = np.median(SeaIce_1819['ng/m3'])
Median_SeaIce_All  = np.median(SeaIce_All['ng/m3'])

# Land
Median_V1_17L   = np.median(Traj_V1_17L_B['ng/m3'])
Median_V2_17L   = np.median(Traj_V2_17L_B['ng/m3'])
Median_V3_17ML  = np.median(Traj_V3_17ML_B['ng/m3'])
Median_V3_17DL  = np.median(Traj_V3_17DL_B['ng/m3'])

Median_V1_18L   = np.median(Traj_V1_18L_B['ng/m3'])
Median_V2_18L   = np.median(Traj_V2_18L_B['ng/m3'])
Median_V3_18ML  = np.median(Traj_V3_18ML_B['ng/m3'])
Median_V3_18DL  = np.median(Traj_V3_18DL_B['ng/m3'])

Median_Land_1718 = np.median(Land_1718['ng/m3'])
Median_Land_1819 = np.median(Land_1819['ng/m3'])
Median_Land_All  = np.median(Land_All['ng/m3'])

# Ocean
Median_V1_17O   = np.median(Traj_V1_17O_B['ng/m3'])
Median_V2_17O   = np.median(Traj_V2_17O_B['ng/m3'])
Median_V3_17MO  = np.median(Traj_V3_17MO_B['ng/m3'])
Median_V3_17DO  = np.median(Traj_V3_17DO_B['ng/m3'])

Median_V1_18O   = np.median(Traj_V1_18O_B['ng/m3'])
Median_V2_18O   = np.median(Traj_V2_18O_B['ng/m3'])
Median_V3_18MO  = np.median(Traj_V3_18MO_B['ng/m3'])
Median_V3_18DO  = np.median(Traj_V3_18DO_B['ng/m3'])

Median_Ocean_1718 = np.median(Ocean_1718['ng/m3'])
Median_Ocean_1819 = np.median(Ocean_1819['ng/m3'])
Median_Ocean_All  = np.median(Ocean_All['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE ST DEV HG0  (SEA ICE, LAND, OCEAN)

# Sea Ice
std_V1_17SI  = np.std(Traj_V1_17SI_B['ng/m3'])
std_V2_17SI  = np.std(Traj_V2_17SI_B['ng/m3'])
std_V3_17MSI = np.std(Traj_V3_17MSI_B['ng/m3'])
std_V3_17DSI = np.std(Traj_V3_17DSI_B['ng/m3'])

std_V1_18SI  = np.std(Traj_V1_18SI_B['ng/m3'])
std_V2_18SI  = np.std(Traj_V2_18SI_B['ng/m3'])
std_V3_18MSI = np.std(Traj_V3_18MSI_B['ng/m3'])
std_V3_18DSI = np.std(Traj_V3_18DSI_B['ng/m3'])

std_SeaIce_1718 = np.std(SeaIce_1718['ng/m3'])
std_SeaIce_1819 = np.std(SeaIce_1819['ng/m3'])
std_SeaIce_All  = np.std(SeaIce_All['ng/m3'])

# Land
std_V1_17L   = np.std(Traj_V1_17L_B['ng/m3'])
std_V2_17L   = np.std(Traj_V2_17L_B['ng/m3'])
std_V3_17ML  = np.std(Traj_V3_17ML_B['ng/m3'])
std_V3_17DL  = np.std(Traj_V3_17DL_B['ng/m3'])

std_V1_18L   = np.std(Traj_V1_18L_B['ng/m3'])
std_V2_18L   = np.std(Traj_V2_18L_B['ng/m3'])
std_V3_18ML  = np.std(Traj_V3_18ML_B['ng/m3'])
std_V3_18DL  = np.std(Traj_V3_18DL_B['ng/m3'])

std_Land_1718 = np.std(Land_1718['ng/m3'])
std_Land_1819 = np.std(Land_1819['ng/m3'])
std_Land_All  = np.std(Land_All['ng/m3'])

# Ocean
std_V1_17O   = np.std(Traj_V1_17O_B['ng/m3'])
std_V2_17O   = np.std(Traj_V2_17O_B['ng/m3'])
std_V3_17MO  = np.std(Traj_V3_17MO_B['ng/m3'])
std_V3_17DO  = np.std(Traj_V3_17DO_B['ng/m3'])

std_V1_18O   = np.std(Traj_V1_18O_B['ng/m3'])
std_V2_18O   = np.std(Traj_V2_18O_B['ng/m3'])
std_V3_18MO  = np.std(Traj_V3_18MO_B['ng/m3'])
std_V3_18DO  = np.std(Traj_V3_18DO_B['ng/m3'])

std_Ocean_1718 = np.std(Ocean_1718['ng/m3'])
std_Ocean_1819 = np.std(Ocean_1819['ng/m3'])
std_Ocean_All  = np.std(Ocean_All['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MAD HG0  (SEA ICE, LAND, OCEAN)

# Sea Ice
MAD_V1_17SI  = stats.median_absolute_deviation(Traj_V1_17SI_B['ng/m3'])
MAD_V2_17SI  = stats.median_absolute_deviation(Traj_V2_17SI_B['ng/m3'])
MAD_V3_17MSI = stats.median_absolute_deviation(Traj_V3_17MSI_B['ng/m3'])
MAD_V3_17DSI = stats.median_absolute_deviation(Traj_V3_17DSI_B['ng/m3'])

MAD_V1_18SI  = stats.median_absolute_deviation(Traj_V1_18SI_B['ng/m3'])
MAD_V2_18SI  = stats.median_absolute_deviation(Traj_V2_18SI_B['ng/m3'])
MAD_V3_18MSI = stats.median_absolute_deviation(Traj_V3_18MSI_B['ng/m3'])
MAD_V3_18DSI = stats.median_absolute_deviation(Traj_V3_18DSI_B['ng/m3'])

MAD_SeaIce_1718 = stats.median_absolute_deviation(SeaIce_1718['ng/m3'])
MAD_SeaIce_1819 = stats.median_absolute_deviation(SeaIce_1819['ng/m3'])
MAD_SeaIce_All  = stats.median_absolute_deviation(SeaIce_All['ng/m3'])

# Land
MAD_V1_17L   = stats.median_absolute_deviation(Traj_V1_17L_B['ng/m3'])
MAD_V2_17L   = stats.median_absolute_deviation(Traj_V2_17L_B['ng/m3'])
MAD_V3_17ML  = stats.median_absolute_deviation(Traj_V3_17ML_B['ng/m3'])
MAD_V3_17DL  = stats.median_absolute_deviation(Traj_V3_17DL_B['ng/m3'])

MAD_V1_18L   = stats.median_absolute_deviation(Traj_V1_18L_B['ng/m3'])
MAD_V2_18L   = stats.median_absolute_deviation(Traj_V2_18L_B['ng/m3'])
MAD_V3_18ML  = stats.median_absolute_deviation(Traj_V3_18ML_B['ng/m3'])
MAD_V3_18DL  = stats.median_absolute_deviation(Traj_V3_18DL_B['ng/m3'])

MAD_Land_1718   = stats.median_absolute_deviation(Land_1718['ng/m3'])
MAD_Land_1819   = stats.median_absolute_deviation(Land_1819['ng/m3'])
MAD_Land_All    = stats.median_absolute_deviation(Land_All['ng/m3'])

# Ocean
MAD_V1_17O   = stats.median_absolute_deviation(Traj_V1_17O_B['ng/m3'])
MAD_V2_17O   = stats.median_absolute_deviation(Traj_V2_17O_B['ng/m3'])
MAD_V3_17MO  = stats.median_absolute_deviation(Traj_V3_17MO_B['ng/m3'])
MAD_V3_17DO  = stats.median_absolute_deviation(Traj_V3_17DO_B['ng/m3'])

MAD_V1_18O   = stats.median_absolute_deviation(Traj_V1_18O_B['ng/m3'])
MAD_V2_18O   = stats.median_absolute_deviation(Traj_V2_18O_B['ng/m3'])
MAD_V3_18MO  = stats.median_absolute_deviation(Traj_V3_18MO_B['ng/m3'])
MAD_V3_18DO  = stats.median_absolute_deviation(Traj_V3_18DO_B['ng/m3'])

MAD_Ocean_1718  = stats.median_absolute_deviation(Ocean_1718['ng/m3'])
MAD_Ocean_1819  = stats.median_absolute_deviation(Ocean_1819['ng/m3'])
MAD_Ocean_All   = stats.median_absolute_deviation(Ocean_All['ng/m3'])

#------------------------------------------------------------------------------
# Welches T-Test on Hg0
 
#----------------------
# T-test for the means of 2 indpendent populations
# (Note: unequal sample sizes and/or variance, therefore Welches t-test)
#----------------------

# Continental & Sea Ice
WT_stat_V1_17_L_SI,  WT_pval_V1_17_L_SI  = stats.ttest_ind(Traj_V1_17L_B['ng/m3'],   Traj_V1_17SI_B['ng/m3'],  equal_var = False)
WT_stat_V2_17_L_SI,  WT_pval_V2_17_L_SI  = stats.ttest_ind(Traj_V2_17L_B['ng/m3'],   Traj_V2_17SI_B['ng/m3'],  equal_var = False)
WT_stat_V3_17M_L_SI, WT_pval_V3_17M_L_SI = stats.ttest_ind(Traj_V3_17ML_B['ng/m3'],  Traj_V3_17MSI_B['ng/m3'], equal_var = False)
WT_stat_V3_17D_L_SI, WT_pval_V3_17D_L_SI = stats.ttest_ind(Traj_V3_17DL_B['ng/m3'],  Traj_V3_17DSI_B['ng/m3'], equal_var = False)

WT_stat_V1_18_L_SI,  WT_pval_V1_18_L_SI  = stats.ttest_ind(Traj_V1_18L_B['ng/m3'],   Traj_V1_18SI_B['ng/m3'],  equal_var = False)
WT_stat_V2_18_L_SI,  WT_pval_V2_18_L_SI  = stats.ttest_ind(Traj_V2_18L_B['ng/m3'],   Traj_V2_18SI_B['ng/m3'],  equal_var = False)
WT_stat_V3_18M_L_SI, WT_pval_V3_18M_L_SI = stats.ttest_ind(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MSI_B['ng/m3'], equal_var = False)
WT_stat_V3_18D_L_SI, WT_pval_V3_18D_L_SI = stats.ttest_ind(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DSI_B['ng/m3'], equal_var = False)

WT_stat_1718_L_SI,   WT_pval_1718_L_SI   = stats.ttest_ind(Land_1718['ng/m3'],       SeaIce_1718['ng/m3'],     equal_var = False)
WT_stat_1819_L_SI,   WT_pval_1819_L_SI   = stats.ttest_ind(Land_1819['ng/m3'],       SeaIce_1819['ng/m3'],     equal_var = False)
WT_stat_All_L_SI,    WT_pval_All_L_SI    = stats.ttest_ind(Land_All['ng/m3'],        SeaIce_All['ng/m3'],      equal_var = False)

# Continental & Ocean
WT_stat_V1_17_L_O,   WT_pval_V1_17_L_O   = stats.ttest_ind(Traj_V1_17L_B['ng/m3'],   Traj_V1_17O_B['ng/m3'],   equal_var = False)
WT_stat_V2_17_L_O,   WT_pval_V2_17_L_O   = stats.ttest_ind(Traj_V2_17L_B['ng/m3'],   Traj_V2_17O_B['ng/m3'],   equal_var = False)
WT_stat_V3_17M_L_O,  WT_pval_V3_17M_L_O  = stats.ttest_ind(Traj_V3_17ML_B['ng/m3'],  Traj_V3_17MO_B['ng/m3'],  equal_var = False)
WT_stat_V3_17D_L_O,  WT_pval_V3_17D_L_O  = stats.ttest_ind(Traj_V3_17DL_B['ng/m3'],  Traj_V3_17DO_B['ng/m3'],  equal_var = False)

WT_stat_V1_18_L_O,   WT_pval_V1_18_L_O   = stats.ttest_ind(Traj_V1_18L_B['ng/m3'],   Traj_V1_18O_B['ng/m3'],   equal_var = False)
WT_stat_V2_18_L_O,   WT_pval_V2_18_L_O   = stats.ttest_ind(Traj_V2_18L_B['ng/m3'],   Traj_V2_18O_B['ng/m3'],   equal_var = False)
WT_stat_V3_18M_L_O,  WT_pval_V3_18M_L_O  = stats.ttest_ind(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MO_B['ng/m3'],  equal_var = False)
WT_stat_V3_18D_L_O,  WT_pval_V3_18D_L_O  = stats.ttest_ind(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DO_B['ng/m3'],  equal_var = False)

WT_stat_1718_L_O,    WT_pval_1718_L_O    = stats.ttest_ind(Land_1718['ng/m3'],       Ocean_1718['ng/m3'],      equal_var = False)
WT_stat_1819_L_O,    WT_pval_1819_L_O    = stats.ttest_ind(Land_1819['ng/m3'],       Ocean_1819['ng/m3'],      equal_var = False)
WT_stat_All_L_O,     WT_pval_All_L_O     = stats.ttest_ind(Land_All['ng/m3'],        Ocean_All['ng/m3'],       equal_var = False)

# Sea Ice & Ocean
WT_stat_V1_17_SI_O,  WT_pval_V1_17_SI_O  = stats.ttest_ind(Traj_V1_17SI_B['ng/m3'],  Traj_V1_17O_B['ng/m3'],   equal_var = False)
WT_stat_V2_17_SI_O,  WT_pval_V2_17_SI_O  = stats.ttest_ind(Traj_V2_17SI_B['ng/m3'],  Traj_V2_17O_B['ng/m3'],   equal_var = False)
WT_stat_V3_17M_SI_O, WT_pval_V3_17M_SI_O = stats.ttest_ind(Traj_V3_17MSI_B['ng/m3'], Traj_V3_17MO_B['ng/m3'],  equal_var = False)
WT_stat_V3_17D_SI_O, WT_pval_V3_17D_SI_O = stats.ttest_ind(Traj_V3_17DSI_B['ng/m3'], Traj_V3_17DO_B['ng/m3'],  equal_var = False)

WT_stat_V1_18_SI_O,  WT_pval_V1_18_SI_O  = stats.ttest_ind(Traj_V1_18SI_B['ng/m3'],  Traj_V1_18O_B['ng/m3'],   equal_var = False)
WT_stat_V2_18_SI_O,  WT_pval_V2_18_SI_O  = stats.ttest_ind(Traj_V2_18SI_B['ng/m3'],  Traj_V2_18O_B['ng/m3'],   equal_var = False)
WT_stat_V3_18M_SI_O, WT_pval_V3_18M_SI_O = stats.ttest_ind(Traj_V3_18MSI_B['ng/m3'], Traj_V3_18MO_B['ng/m3'],  equal_var = False)
WT_stat_V3_18D_SI_O, WT_pval_V3_18D_SI_O = stats.ttest_ind(Traj_V3_18DSI_B['ng/m3'], Traj_V3_18DO_B['ng/m3'],  equal_var = False)

WT_stat_1718_SI_O,   WT_pval_1718_SI_O   = stats.ttest_ind(SeaIce_1718['ng/m3'],     Ocean_1718['ng/m3'],      equal_var = False)
WT_stat_1819_SI_O,   WT_pval_1819_SI_O   = stats.ttest_ind(SeaIce_1819['ng/m3'],     Ocean_1819['ng/m3'],      equal_var = False)
WT_stat_All_SI_O,    WT_pval_All_SI_O    = stats.ttest_ind(SeaIce_All['ng/m3'],      Ocean_All['ng/m3'],       equal_var = False)

#------------------------------------------------------------------------------
# KS-Test on BrO (Kolmogorov-Smirnov Test)

# Interannual variability (2017-18 to 2018-19)
#KS_stat_1,       KS_pval_1       = stats.ks_2samp(BrO_V1_17_D,               BrO_V1_18_D,             alternative='two-sided', mode='auto')

# Continental & Sea Ice
KS_stat_V1_17_L_SI,  KS_pval_V1_17_L_SI  = stats.ks_2samp(Traj_V1_17L_B['ng/m3'],   Traj_V1_17SI_B['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V2_17_L_SI,  KS_pval_V2_17_L_SI  = stats.ks_2samp(Traj_V2_17L_B['ng/m3'],   Traj_V2_17SI_B['ng/m3'],  alternative='two-sided', mode='auto')
#KS_stat_V3_17M_L_SI, KS_pval_V3_17M_L_SI = stats.ks_2samp(Traj_V3_17ML_B['ng/m3'],  Traj_V3_17MSI_B['ng/m3'], alternative='two-sided', mode='auto')
KS_stat_V3_17D_L_SI, KS_pval_V3_17D_L_SI = stats.ks_2samp(Traj_V3_17DL_B['ng/m3'],  Traj_V3_17DSI_B['ng/m3'], alternative='two-sided', mode='auto')

KS_stat_V1_18_L_SI,  KS_pval_V1_18_L_SI  = stats.ks_2samp(Traj_V1_18L_B['ng/m3'],   Traj_V1_18SI_B['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V2_18_L_SI,  KS_pval_V2_18_L_SI  = stats.ks_2samp(Traj_V2_18L_B['ng/m3'],   Traj_V2_18SI_B['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V3_18M_L_SI, KS_pval_V3_18M_L_SI = stats.ks_2samp(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MSI_B['ng/m3'], alternative='two-sided', mode='auto')
KS_stat_V3_18D_L_SI, KS_pval_V3_18D_L_SI = stats.ks_2samp(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DSI_B['ng/m3'], alternative='two-sided', mode='auto')

KS_stat_1718_L_SI,   KS_pval_1718_L_SI   = stats.ks_2samp(Land_1718['ng/m3'],       SeaIce_1718['ng/m3'],     alternative='two-sided', mode='auto')
KS_stat_1819_L_SI,   KS_pval_1819_L_SI   = stats.ks_2samp(Land_1819['ng/m3'],       SeaIce_1819['ng/m3'],     alternative='two-sided', mode='auto')
KS_stat_All_L_SI,    KS_pval_All_L_SI    = stats.ks_2samp(Land_All['ng/m3'],        SeaIce_All['ng/m3'],      alternative='two-sided', mode='auto')

# Continental & Ocean
#KS_stat_V1_17_L_O,   KS_pval_V1_17_L_O   = stats.ks_2samp(Traj_V1_17L_B['ng/m3'],   Traj_V1_17O_B['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V2_17_L_O,   KS_pval_V2_17_L_O   = stats.ks_2samp(Traj_V2_17L_B['ng/m3'],   Traj_V2_17O_B['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_17M_L_O,  KS_pval_V3_17M_L_O  = stats.ks_2samp(Traj_V3_17ML_B['ng/m3'],  Traj_V3_17MO_B['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V3_17D_L_O,  KS_pval_V3_17D_L_O  = stats.ks_2samp(Traj_V3_17DL_B['ng/m3'],  Traj_V3_17DO_B['ng/m3'],  alternative='two-sided', mode='auto')

#KS_stat_V1_18_L_O,   KS_pval_V1_18_L_O   = stats.ks_2samp(Traj_V1_18L_B['ng/m3'],   Traj_V1_18O_B['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V2_18_L_O,   KS_pval_V2_18_L_O   = stats.ks_2samp(Traj_V2_18L_B['ng/m3'],   Traj_V2_18O_B['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_18M_L_O,  KS_pval_V3_18M_L_O  = stats.ks_2samp(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MO_B['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V3_18D_L_O,  KS_pval_V3_18D_L_O  = stats.ks_2samp(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DO_B['ng/m3'],  alternative='two-sided', mode='auto')

KS_stat_1718_L_O,    KS_pval_1718_L_O    = stats.ks_2samp(Land_1718['ng/m3'],       Ocean_1718['ng/m3'],      alternative='two-sided', mode='auto')
KS_stat_1819_L_O,    KS_pval_1819_L_O    = stats.ks_2samp(Land_1819['ng/m3'],       Ocean_1819['ng/m3'],      alternative='two-sided', mode='auto')
KS_stat_All_L_O,     KS_pval_All_L_O     = stats.ks_2samp(Land_All['ng/m3'],        Ocean_All['ng/m3'],       alternative='two-sided', mode='auto')

# Sea Ice & Ocean
#KS_stat_V1_17_SI_O,  KS_pval_V1_17_SI_O  = stats.ks_2samp(Traj_V1_17SI_B['ng/m3'],  Traj_V1_17O_B['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V2_17_SI_O,  KS_pval_V2_17_SI_O  = stats.ks_2samp(Traj_V2_17SI_B['ng/m3'],  Traj_V2_17O_B['ng/m3'],   alternative='two-sided', mode='auto')
#KS_stat_V3_17M_SI_O, KS_pval_V3_17M_SI_O = stats.ks_2samp(Traj_V3_17MSI_B['ng/m3'], Traj_V3_17MO_B['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V3_17D_SI_O, KS_pval_V3_17D_SI_O = stats.ks_2samp(Traj_V3_17DSI_B['ng/m3'], Traj_V3_17DO_B['ng/m3'],  alternative='two-sided', mode='auto')

#KS_stat_V1_18_SI_O,  KS_pval_V1_18_SI_O  = stats.ks_2samp(Traj_V1_18SI_B['ng/m3'],  Traj_V1_18O_B['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V2_18_SI_O,  KS_pval_V2_18_SI_O  = stats.ks_2samp(Traj_V2_18SI_B['ng/m3'],  Traj_V2_18O_B['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_18M_SI_O, KS_pval_V3_18M_SI_O = stats.ks_2samp(Traj_V3_18MSI_B['ng/m3'], Traj_V3_18MO_B['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V3_18D_SI_O, KS_pval_V3_18D_SI_O = stats.ks_2samp(Traj_V3_18DSI_B['ng/m3'], Traj_V3_18DO_B['ng/m3'],  alternative='two-sided', mode='auto')

KS_stat_1718_SI_O,   KS_pval_1718_SI_O   = stats.ks_2samp(SeaIce_1718['ng/m3'],     Ocean_1718['ng/m3'],      alternative='two-sided', mode='auto')
KS_stat_1819_SI_O,   KS_pval_1819_SI_O   = stats.ks_2samp(SeaIce_1819['ng/m3'],     Ocean_1819['ng/m3'],      alternative='two-sided', mode='auto')
KS_stat_All_SI_O,    KS_pval_All_SI_O    = stats.ks_2samp(SeaIce_All['ng/m3'],      Ocean_All['ng/m3'],       alternative='two-sided', mode='auto')

#------------------------------------------------------------------------------
#BUILD DATAFRAME FOR THE STATISTICAL RESULTS (SEA ICE, LAND, OCEAN)

# Build a pandas dataframe (Seasonal Met)
dfHg_AirMass = {'N':      [N_V1_17SI,          N_V2_17SI,          N_V3_17MSI,       N_V3_17DSI,      N_SeaIce_1718,
                           N_V1_18SI,          N_V2_18SI,          N_V3_18MSI,       N_V3_18DSI,      N_SeaIce_1819,      N_SeaIce_All,
                           N_V1_17L,           N_V2_17L,           N_V3_17ML,        N_V3_17DL,       N_Land_1718,
                           N_V1_18L,           N_V2_18L,           N_V3_18ML,        N_V3_18DL,       N_Land_1819,        N_Land_All,
                           N_V1_17O,           N_V2_17O,           N_V3_17MO,        N_V3_17DO,       N_Ocean_1718,
                           N_V1_18O,           N_V2_18O,           N_V3_18MO,        N_V3_18DO,       N_Ocean_1819,       N_Ocean_All],
                'Mean':   [Mean_V1_17SI,       Mean_V2_17SI,       Mean_V3_17MSI,    Mean_V3_17DSI,   Mean_SeaIce_1718,
                           Mean_V1_18SI,       Mean_V2_18SI,       Mean_V3_18MSI,    Mean_V3_18DSI,   Mean_SeaIce_1819,   Mean_SeaIce_All,
                           Mean_V1_17L,        Mean_V2_17L,        Mean_V3_17ML,     Mean_V3_17DL,    Mean_Land_1718,
                           Mean_V1_18L,        Mean_V2_18L,        Mean_V3_18ML,     Mean_V3_18DL,    Mean_Land_1819,     Mean_Land_All,
                           Mean_V1_17O,        Mean_V2_17O,        Mean_V3_17MO,     Mean_V3_17DO,    Mean_Ocean_1718,
                           Mean_V1_18O,        Mean_V2_18O,        Mean_V3_18MO,     Mean_V3_18DO,    Mean_Ocean_1819,    Mean_Ocean_All],
                'StDev':  [std_V1_17SI,        std_V2_17SI,        std_V3_17MSI,     std_V3_17DSI,    std_SeaIce_1718,
                           std_V1_18SI,        std_V2_18SI,        std_V3_18MSI,     std_V3_18DSI,    std_SeaIce_1819,    std_SeaIce_All,
                           std_V1_17L,         std_V2_17L,         std_V3_17ML,      std_V3_17DL,     std_Land_1718,
                           std_V1_18L,         std_V2_18L,         std_V3_18ML,      std_V3_18DL,     std_Land_1819,      std_Land_All,
                           std_V1_17O,         std_V2_17O,         std_V3_17MO,      std_V3_17DO,     std_Ocean_1718,
                           std_V1_18O,         std_V2_18O,         std_V3_18MO,      std_V3_18DO,     std_Ocean_1819,     std_Ocean_All],
                'Median': [Median_V1_17SI,     Median_V2_17SI,     Median_V3_17MSI,  Median_V3_17DSI, Median_SeaIce_1718,
                           Median_V1_18SI,     Median_V2_18SI,     Median_V3_18MSI,  Median_V3_18DSI, Median_SeaIce_1819, Median_SeaIce_All,
                           Median_V1_17L,      Median_V2_17L,      Median_V3_17ML,   Median_V3_17DL,  Median_Land_1718,
                           Median_V1_18L,      Median_V2_18L,      Median_V3_18ML,   Median_V3_18DL,  Median_Land_1819,   Median_Land_All,
                           Median_V1_17O,      Median_V2_17O,      Median_V3_17MO,   Median_V3_17DO,  Median_Ocean_1718,
                           Median_V1_18O,      Median_V2_18O,      Median_V3_18MO,   Median_V3_18DO,  Median_Ocean_1819,  Median_Ocean_All],
                'MAD':    [MAD_V1_17SI,        MAD_V2_17SI,        MAD_V3_17MSI,     MAD_V3_17DSI,    MAD_SeaIce_1718,
                           MAD_V1_18SI,        MAD_V2_18SI,        MAD_V3_18MSI,     MAD_V3_18DSI,    MAD_SeaIce_1819,    MAD_SeaIce_All,
                           MAD_V1_17L,         MAD_V2_17L,         MAD_V3_17ML,      MAD_V3_17DL,     MAD_Land_1718,
                           MAD_V1_18L,         MAD_V2_18L,         MAD_V3_18ML,      MAD_V3_18DL,     MAD_Land_1819,      MAD_Land_All,
                           MAD_V1_17O,         MAD_V2_17O,         MAD_V3_17MO,      MAD_V3_17DO,     MAD_Ocean_1718,
                           MAD_V1_18O,         MAD_V2_18O,         MAD_V3_18MO,      MAD_V3_18DO,     MAD_Ocean_1819,     MAD_Ocean_All]}
dfHg_AirMass_SI_LAND = pd.DataFrame(dfHg_AirMass, columns = ['N','Mean','StDev','Median','MAD'], index = ['SI_V1_17','SI_V2_17','SI_V3M_17','SI_V3D_17','SI_1718','SI_V1_18','SI_V2_18','SI_V3M_18','SI_V3D_18','SI_1819','SI_All',
                                                                                                          'L_V1_17', 'L_V2_17', 'L_V3M_17', 'L_V3D_17', 'L_1718', 'L_V1_18', 'L_V2_18', 'L_V3M_18', 'L_V3D_18', 'L_1819', 'L_All',
                                                                                                          'O_V1_17', 'O_V2_17', 'O_V3M_17', 'O_V3D_17', 'O_1718', 'O_V1_18', 'O_V2_18', 'O_V3M_18', 'O_V3D_18', 'O_1819', 'O_All'])
dfHg_AirMass_SI_LAND.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_AirMass_SI_LAND.csv')

# Build a pandas dataframe (Voyage Hg0)
dfHg_StatTest = {'Welches (stat)': [WT_stat_V1_17_L_SI, WT_stat_V2_17_L_SI, WT_stat_V3_17M_L_SI, WT_stat_V3_17D_L_SI, WT_stat_1718_L_SI,
                                    WT_stat_V1_18_L_SI, WT_stat_V2_18_L_SI, WT_stat_V3_18M_L_SI, WT_stat_V3_18D_L_SI, WT_stat_1819_L_SI, WT_stat_All_L_SI,
                                    WT_stat_V1_17_L_O,  WT_stat_V2_17_L_O,  WT_stat_V3_17M_L_O,  WT_stat_V3_17D_L_O,  WT_stat_1718_L_O,
                                    WT_stat_V1_18_L_O,  WT_stat_V2_18_L_O,  WT_stat_V3_18M_L_O,  WT_stat_V3_18D_L_O,  WT_stat_1819_L_O,  WT_stat_All_L_O,
                                    WT_stat_V1_17_SI_O, WT_stat_V2_17_SI_O, WT_stat_V3_17M_SI_O, WT_stat_V3_17D_SI_O, WT_stat_1718_SI_O,
                                    WT_stat_V1_18_SI_O, WT_stat_V2_18_SI_O, WT_stat_V3_18M_SI_O, WT_stat_V3_18D_SI_O, WT_stat_1819_SI_O, WT_stat_All_SI_O],
                 'Welches (pval)': [WT_pval_V1_17_L_SI, WT_pval_V2_17_L_SI, WT_pval_V3_17M_L_SI, WT_pval_V3_17D_L_SI, WT_pval_1718_L_SI, 
                                    WT_pval_V1_18_L_SI, WT_pval_V2_18_L_SI, WT_pval_V3_18M_L_SI, WT_pval_V3_18D_L_SI, WT_pval_1819_L_SI, WT_pval_All_L_SI,
                                    WT_pval_V1_17_L_O,  WT_pval_V2_17_L_O,  WT_pval_V3_17M_L_O,  WT_pval_V3_17D_L_O,  WT_pval_1718_L_O, 
                                    WT_pval_V1_18_L_O,  WT_pval_V2_18_L_O,  WT_pval_V3_18M_L_O,  WT_pval_V3_18D_L_O,  WT_pval_1819_L_O,  WT_pval_All_L_O,
                                    WT_pval_V1_17_SI_O, WT_pval_V2_17_SI_O, WT_pval_V3_17M_SI_O, WT_pval_V3_17D_SI_O, WT_pval_1718_SI_O, 
                                    WT_pval_V1_18_SI_O, WT_pval_V2_18_SI_O, WT_pval_V3_18M_SI_O, WT_pval_V3_18D_SI_O, WT_pval_1819_SI_O, WT_pval_All_SI_O],
                 'KS-Test (stat)': [KS_stat_V1_17_L_SI, KS_stat_V2_17_L_SI, np.nan,              KS_stat_V3_17D_L_SI, KS_stat_1718_L_SI,
                                    KS_stat_V1_18_L_SI, KS_stat_V2_18_L_SI, KS_stat_V3_18M_L_SI, KS_stat_V3_18D_L_SI, KS_stat_1819_L_SI, KS_stat_All_L_SI,
                                    np.nan,             KS_stat_V2_17_L_O,  KS_stat_V3_17M_L_O,  KS_stat_V3_17D_L_O,  KS_stat_1718_L_O,
                                    np.nan,             KS_stat_V2_18_L_O,  KS_stat_V3_18M_L_O,  KS_stat_V3_18D_L_O,  KS_stat_1819_L_O,  KS_stat_All_L_O,
                                    np.nan,             KS_stat_V2_17_SI_O, np.nan,              KS_stat_V3_17D_SI_O, KS_stat_1718_SI_O,
                                    np.nan,             KS_stat_V2_18_SI_O, KS_stat_V3_18M_SI_O, KS_stat_V3_18D_SI_O, KS_stat_1819_SI_O, KS_stat_All_SI_O],
                 'KS-Test (pval)': [KS_pval_V1_17_L_SI, KS_pval_V2_17_L_SI, np.nan,              KS_pval_V3_17D_L_SI, KS_pval_1718_L_SI, 
                                    KS_pval_V1_18_L_SI, KS_pval_V2_18_L_SI, KS_pval_V3_18M_L_SI, KS_pval_V3_18D_L_SI, KS_pval_1819_L_SI, KS_pval_All_L_SI,
                                    np.nan,             KS_pval_V2_17_L_O,  KS_pval_V3_17M_L_O,  KS_pval_V3_17D_L_O,  KS_pval_1718_L_O, 
                                    np.nan,             KS_pval_V2_18_L_O,  KS_pval_V3_18M_L_O,  KS_pval_V3_18D_L_O,  KS_pval_1819_L_O,  KS_pval_All_L_O,
                                    np.nan,             KS_pval_V2_17_SI_O, np.nan,              KS_pval_V3_17D_SI_O, KS_pval_1718_SI_O, 
                                    np.nan,             KS_pval_V2_18_SI_O, KS_pval_V3_18M_SI_O, KS_pval_V3_18D_SI_O, KS_pval_1819_SI_O, KS_pval_All_SI_O]}
dfHg_StatTest = pd.DataFrame(dfHg_StatTest, columns = ['Welches (stat)','Welches (pval)','KS-Test (stat)','KS-Test (pval)'],
                          index = ['L_SI_V1_17','L_SI_V2_17','L_SI_V3_17M','L_SI_V3_17D','L_SI_1718',
                                   'L_SI_V1_18','L_SI_V2_18','L_SI_V3_18M','L_SI_V3_17D','L_SI_1819','L_SI_All',
                                   'L_O_V1_17','L_O_V2_17','L_O_V3_17M','L_O_V3_17D','L_O_1718',
                                   'L_O_V1_18','L_O_V2_18','L_O_V3_18M','L_O_V3_17D','L_O_1819','L_O_All',
                                   'O_SI_V1_17','O_SI_V2_17','O_SI_V3_17M','O_SI_V3_17D','O_SI_1718',
                                   'O_SI_V1_18','O_SI_V2_18','O_SI_V3_18M','O_SI_V3_17D','O_SI_1819','O_SI_All'])
dfHg_StatTest.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_StatTest_SeaIceOpenWater.csv')

#------------------------------------------------------------------------------
# CALCULATE THE 5th PERCENTILE Hg0

P5_V1_17    = np.percentile(Traj_V1_17_B['ng/m3'],    5)
P5_V2_17    = np.percentile(Traj_V2_17_B['ng/m3'],    5)
P5_V3_17M   = np.percentile(Traj_V3_17M_B['ng/m3'],   5)
P5_V3_17D   = np.percentile(Traj_V3_17D_B['ng/m3'],   5)
P5_V4_17    = np.percentile(Traj_V4_17_B['ng/m3'],    5)

P5_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    5)
P5_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    5)
P5_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   5)
P5_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   5)
P5_V4_18    = np.percentile(Traj_V4_18_B['ng/m3'],    5)

P5_PCAN     = np.percentile(Traj_PCAN_B['ng/m3'],     5)

P5_1718     = np.percentile(All_1718['ng/m3'],        5)
P5_1819     = np.percentile(All_1819['ng/m3'],        5)
P5_CAMMPCAN = np.percentile(CAMMPCAN_All['ng/m3'],    5)

#------------------------------------------------------------------------------
# CALCULATE THE 95th PERCENTILE Hg0

P95_V1_17    = np.percentile(Traj_V1_17_B['ng/m3'],    95)
P95_V2_17    = np.percentile(Traj_V2_17_B['ng/m3'],    95)
P95_V3_17M   = np.percentile(Traj_V3_17M_B['ng/m3'],   95)
P95_V3_17D   = np.percentile(Traj_V3_17D_B['ng/m3'],   95)
P95_V4_17    = np.percentile(Traj_V4_17_B['ng/m3'],    95)

P95_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    95)
P95_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    95)
P95_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   95)
P95_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   95)
P95_V4_18    = np.percentile(Traj_V4_18_B['ng/m3'],    95)

P95_PCAN     = np.percentile(Traj_PCAN_B['ng/m3'],     95)

P95_1718     = np.percentile(All_1718['ng/m3'],        95)
P95_1819     = np.percentile(All_1819['ng/m3'],        95)
P95_CAMMPCAN = np.percentile(CAMMPCAN_All['ng/m3'],    95)

#------------------------------------------------------------------------------
# CALCULATE THE 10th PERCENTILE BrO

P10_V1_17    = np.percentile(Traj_V1_17_B['ng/m3'],    10)
P10_V2_17    = np.percentile(Traj_V2_17_B['ng/m3'],    10)
P10_V3_17M   = np.percentile(Traj_V3_17M_B['ng/m3'],   10)
P10_V3_17D   = np.percentile(Traj_V3_17D_B['ng/m3'],   10)
P10_V4_17    = np.percentile(Traj_V4_17_B['ng/m3'],    10)

P10_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    10)
P10_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    10)
P10_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   10)
P10_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   10)
P10_V4_18    = np.percentile(Traj_V4_18_B['ng/m3'],    10)

P10_PCAN     = np.percentile(Traj_PCAN['ng/m3'],       10)

P10_1718     = np.percentile(All_1718['ng/m3'],        10)
P10_1819     = np.percentile(All_1819['ng/m3'],        10)
P10_CAMMPCAN = np.percentile(CAMMPCAN_All['ng/m3'],    10)

#------------------------------------------------------------------------------
# CALCULATE THE 90th PERCENTILE BrO

P90_V1_17    = np.percentile(Traj_V1_17_B['ng/m3'],    90)
P90_V2_17    = np.percentile(Traj_V2_17_B['ng/m3'],    90)
P90_V3_17M   = np.percentile(Traj_V3_17M_B['ng/m3'],   90)
P90_V3_17D   = np.percentile(Traj_V3_17D_B['ng/m3'],   90)
P90_V4_17    = np.percentile(Traj_V4_17_B['ng/m3'],    90)

P90_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    90)
P90_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    90)
P90_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   90)
P90_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   90)
P90_V4_18    = np.percentile(Traj_V4_18_B['ng/m3'],    90)

P90_PCAN     = np.percentile(Traj_PCAN_B['ng/m3'],     90)

P90_1718     = np.percentile(All_1718['ng/m3'],        90)
P90_1819     = np.percentile(All_1819['ng/m3'],        90)
P90_CAMMPCAN = np.percentile(CAMMPCAN_All['ng/m3'],    90)

#------------------------------------------------------------------------------
# CALCULATE THE 25th PERCENTILE Hg0

P25_V1_17    = np.percentile(Traj_V1_17_B['ng/m3'],    25)
P25_V2_17    = np.percentile(Traj_V2_17_B['ng/m3'],    25)
P25_V3_17M   = np.percentile(Traj_V3_17M_B['ng/m3'],   25)
P25_V3_17D   = np.percentile(Traj_V3_17D_B['ng/m3'],   25)
P25_V4_17    = np.percentile(Traj_V4_17_B['ng/m3'],    25)

P25_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    25)
P25_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    25)
P25_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   25)
P25_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   25)
P25_V4_18    = np.percentile(Traj_V4_18_B['ng/m3'],    25)

P25_PCAN     = np.percentile(Traj_PCAN_B['ng/m3'],     25)

P25_1718     = np.percentile(All_1718['ng/m3'],        25)
P25_1819     = np.percentile(All_1819['ng/m3'],        25)
P25_CAMMPCAN = np.percentile(CAMMPCAN_All['ng/m3'],    25)

#------------------------------------------------------------------------------
# CALCULATE THE 75th PERCENTILE Hg0

P75_V1_17    = np.percentile(Traj_V1_17_B['ng/m3'],    75)
P75_V2_17    = np.percentile(Traj_V2_17_B['ng/m3'],    75)
P75_V3_17M   = np.percentile(Traj_V3_17M_B['ng/m3'],   75)
P75_V3_17D   = np.percentile(Traj_V3_17D_B['ng/m3'],   75)
P75_V4_17    = np.percentile(Traj_V4_17_B['ng/m3'],    75)

P75_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    75)
P75_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    75)
P75_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   75)
P75_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   75)
P75_V4_18    = np.percentile(Traj_V4_18_B['ng/m3'],    75)

P75_PCAN     = np.percentile(Traj_PCAN_B['ng/m3'],     75)

P75_1718     = np.percentile(All_1718['ng/m3'],        75)
P75_1819     = np.percentile(All_1819['ng/m3'],        75)
P75_CAMMPCAN = np.percentile(CAMMPCAN_All['ng/m3'],    75)

#------------------------------------------------------------------------------
# CALCULATE THE 45th PERCENTILE Hg0

P45_V1_17    = np.percentile(Traj_V1_17_B['ng/m3'],    45)
P45_V2_17    = np.percentile(Traj_V2_17_B['ng/m3'],    45)
P45_V3_17M   = np.percentile(Traj_V3_17M_B['ng/m3'],   45)
P45_V3_17D   = np.percentile(Traj_V3_17D_B['ng/m3'],   45)
P45_V4_17    = np.percentile(Traj_V4_17_B['ng/m3'],    45)

P45_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    45)
P45_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    45)
P45_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   45)
P45_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   45)
P45_V4_18    = np.percentile(Traj_V4_18_B['ng/m3'],    45)

P45_PCAN     = np.percentile(Traj_PCAN_B['ng/m3'],     45)

P45_1718     = np.percentile(All_1718['ng/m3'],        45)
P45_1819     = np.percentile(All_1819['ng/m3'],        45)
P45_CAMMPCAN = np.percentile(CAMMPCAN_All['ng/m3'],    45)

#------------------------------------------------------------------------------
# CALCULATE THE 55th PERCENTILE Hg0

P55_V1_17    = np.percentile(Traj_V1_17_B['ng/m3'],    55)
P55_V2_17    = np.percentile(Traj_V2_17_B['ng/m3'],    55)
P55_V3_17M   = np.percentile(Traj_V3_17M_B['ng/m3'],   55)
P55_V3_17D   = np.percentile(Traj_V3_17D_B['ng/m3'],   55)
P55_V4_17    = np.percentile(Traj_V4_17_B['ng/m3'],    55)

P55_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    55)
P55_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    55)
P55_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   55)
P55_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   55)
P55_V4_18    = np.percentile(Traj_V4_18_B['ng/m3'],    55)

P55_PCAN     = np.percentile(Traj_PCAN_B['ng/m3'],     55)

P55_1718     = np.percentile(All_1718['ng/m3'],        55)
P55_1819     = np.percentile(All_1819['ng/m3'],        55)
P55_CAMMPCAN = np.percentile(CAMMPCAN_All['ng/m3'],    55)

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN BrO

Median_V1_17    = np.median(Traj_V1_17_B['ng/m3'])
Median_V2_17    = np.median(Traj_V2_17_B['ng/m3'])
Median_V3_17M   = np.median(Traj_V3_17M_B['ng/m3'])
Median_V3_17D   = np.median(Traj_V3_17D_B['ng/m3'])
Median_V4_17    = np.median(Traj_V4_17_B['ng/m3'])

Median_V1_18    = np.median(Traj_V1_18_B['ng/m3'])
Median_V2_18    = np.median(Traj_V2_18_B['ng/m3'])
Median_V3_18M   = np.median(Traj_V3_18M_B['ng/m3'])
Median_V3_18D   = np.median(Traj_V3_18D_B['ng/m3'])
Median_V4_18    = np.median(Traj_V4_18_B['ng/m3'])

Median_PCAN     = np.median(Traj_PCAN_B['ng/m3'])

Median_1718     = np.median(All_1718['ng/m3'])
Median_1819     = np.median(All_1819['ng/m3'])
Median_CAMMPCAN = np.median(CAMMPCAN_All['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MAD BrO

MAD_V1_17    = stats.median_absolute_deviation(Traj_V1_17_B['ng/m3'])
MAD_V2_17    = stats.median_absolute_deviation(Traj_V2_17_B['ng/m3'])
MAD_V3_17M   = stats.median_absolute_deviation(Traj_V3_17M_B['ng/m3'])
MAD_V3_17D   = stats.median_absolute_deviation(Traj_V3_17D_B['ng/m3'])
MAD_V4_17    = stats.median_absolute_deviation(Traj_V4_17_B['ng/m3'])

MAD_V1_18    = stats.median_absolute_deviation(Traj_V1_18_B['ng/m3'])
MAD_V2_18    = stats.median_absolute_deviation(Traj_V2_18_B['ng/m3'])
MAD_V3_18M   = stats.median_absolute_deviation(Traj_V3_18M_B['ng/m3'])
MAD_V3_18D   = stats.median_absolute_deviation(Traj_V3_18D_B['ng/m3'])
MAD_V4_18    = stats.median_absolute_deviation(Traj_V4_18_B['ng/m3'])

MAD_PCAN     = stats.median_absolute_deviation(Traj_PCAN_B['ng/m3'])

MAD_1718     = stats.median_absolute_deviation(All_1718['ng/m3'])
MAD_1819     = stats.median_absolute_deviation(All_1819['ng/m3'])
MAD_CAMMPCAN = stats.median_absolute_deviation(CAMMPCAN_All['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN - MAD BrO

Med_M_MAD_V1_17    = Median_V1_17    - MAD_V1_17
Med_M_MAD_V2_17    = Median_V2_17    - MAD_V2_17
Med_M_MAD_V3_17M   = Median_V3_17M   - MAD_V3_17M
Med_M_MAD_V3_17D   = Median_V3_17D   - MAD_V3_17D
Med_M_MAD_V4_17    = Median_V4_17    - MAD_V4_17

Med_M_MAD_V1_18    = Median_V1_18    - MAD_V1_18
Med_M_MAD_V2_18    = Median_V2_18    - MAD_V2_18
Med_M_MAD_V3_18M   = Median_V3_18M   - MAD_V3_18M
Med_M_MAD_V3_18D   = Median_V3_18D   - MAD_V3_18D
Med_M_MAD_V4_18    = Median_V4_18    - MAD_V4_18

Med_M_MAD_PCAN     = Median_PCAN     - MAD_PCAN

Med_M_MAD_1718     = Median_1718     - MAD_1718
Med_M_MAD_1819     = Median_1819     - MAD_1819
Med_M_MAD_CAMMPCAN = Median_CAMMPCAN - MAD_CAMMPCAN

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN + MAD BrO

Med_P_MAD_V1_17    = Median_V1_17    + MAD_V1_17
Med_P_MAD_V2_17    = Median_V2_17    + MAD_V2_17
Med_P_MAD_V3_17M   = Median_V3_17M   + MAD_V3_17M
Med_P_MAD_V3_17D   = Median_V3_17D   + MAD_V3_17D
Med_P_MAD_V4_17    = Median_V4_17    + MAD_V4_17

Med_P_MAD_V1_18    = Median_V1_18    + MAD_V1_18
Med_P_MAD_V2_18    = Median_V2_18    + MAD_V2_18
Med_P_MAD_V3_18M   = Median_V3_18M   + MAD_V3_18M
Med_P_MAD_V3_18D   = Median_V3_18D   + MAD_V3_18D
Med_P_MAD_V4_18    = Median_V4_18    + MAD_V4_18

Med_P_MAD_PCAN     = Median_PCAN     + MAD_PCAN

Med_P_MAD_1718     = Median_1718     + MAD_1718
Med_P_MAD_1819     = Median_1819     + MAD_1819
Med_P_MAD_CAMMPCAN = Median_CAMMPCAN + MAD_CAMMPCAN

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO <= 5th PERCENTILE

# CAMMPCAN 2017-18
P5_1           = Traj_V1_17['ng/m3']  <= P5_V1_17
Traj_V1_17_P5  = Traj_V1_17[P5_1]

P5_2           = Traj_V2_17['ng/m3']  <= P5_V2_17
Traj_V2_17_P5  = Traj_V2_17[P5_2]

P5_3           = Traj_V3_17M['ng/m3'] <= P5_V3_17M
Traj_V3_17M_P5 = Traj_V3_17M[P5_3]

P5_4           = Traj_V3_17D['ng/m3'] <= P5_V3_17D
Traj_V3_17D_P5 = Traj_V3_17D[P5_4]

P5_5           = Traj_V4_17['ng/m3']  <= P5_V4_17
Traj_V4_17_P5  = Traj_V4_17[P5_5]

# CAMMPCAN 2018-19
P5_6           = Traj_V1_18['ng/m3']  <= P5_V1_18
Traj_V1_18_P5  = Traj_V1_18[P5_6]

P5_7           = Traj_V2_18['ng/m3']  <= P5_V2_18
Traj_V2_18_P5  = Traj_V2_18[P5_7]

P5_8           = Traj_V3_18M['ng/m3'] <= P5_V3_18M
Traj_V3_18M_P5 = Traj_V3_18M[P5_8]

P5_9           = Traj_V3_18D['ng/m3'] <= P5_V3_18D
Traj_V3_18D_P5 = Traj_V3_18D[P5_9]

P5_10          = Traj_V4_18['ng/m3']  <= P5_V4_18
Traj_V4_18_P5  = Traj_V4_18[P5_10]

# PCAN
P5_11          = Traj_PCAN['ng/m3']   <= P5_PCAN
Traj_PCAN_P5   = Traj_PCAN[P5_11]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO <= 10th PERCENTILE

# CAMMPCAN 2017-18
P10_1           = Traj_V1_17['ng/m3']  <= P10_V1_17
Traj_V1_17_P10  = Traj_V1_17[P10_1]

P10_2           = Traj_V2_17['ng/m3']  <= P10_V2_17
Traj_V2_17_P10  = Traj_V2_17[P10_2]

P10_3           = Traj_V3_17M['ng/m3'] <= P10_V3_17M
Traj_V3_17M_P10 = Traj_V3_17M[P10_3]

P10_4           = Traj_V3_17D['ng/m3'] <= P10_V3_17D
Traj_V3_17D_P10 = Traj_V3_17D[P10_4]

P10_5           = Traj_V4_17['ng/m3']  <= P10_V4_17
Traj_V4_17_P10  = Traj_V4_17[P10_5]

# CAMMPCAN 2018-19
P10_6           = Traj_V1_18['ng/m3']  <= P10_V1_18
Traj_V1_18_P10  = Traj_V1_18[P10_6]

P10_7           = Traj_V2_18['ng/m3']  <= P10_V2_18
Traj_V2_18_P10  = Traj_V2_18[P10_7]

P10_8           = Traj_V3_18M['ng/m3'] <= P10_V3_18M
Traj_V3_18M_P10 = Traj_V3_18M[P10_8]

P10_9           = Traj_V3_18D['ng/m3'] <= P10_V3_18D
Traj_V3_18D_P10 = Traj_V3_18D[P10_9]

P10_10          = Traj_V4_18['ng/m3']  <= P10_V4_18
Traj_V4_18_P10  = Traj_V4_18[P10_10]

# PCAN
P10_11          = Traj_PCAN['ng/m3']   <= P10_PCAN
Traj_PCAN_P10   = Traj_PCAN[P10_11]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO >= 25th PERCENTILE

# CAMMPCAN 2017-18
P25_1           = Traj_V1_17['ng/m3']  <= P25_V1_17
Traj_V1_17_P25  = Traj_V1_17[P25_1]

P25_2           = Traj_V2_17['ng/m3']  <= P25_V2_17
Traj_V2_17_P25  = Traj_V2_17[P25_2]

P25_3           = Traj_V3_17M['ng/m3'] <= P25_V3_17M
Traj_V3_17M_P25 = Traj_V3_17M[P25_3]

P25_4           = Traj_V3_17D['ng/m3'] <= P25_V3_17D
Traj_V3_17D_P25 = Traj_V3_17D[P25_4]

P25_5           = Traj_V4_17['ng/m3']  <= P25_V4_17
Traj_V4_17_P25  = Traj_V4_17[P25_5]

# CAMMPCAN 2018-19
P25_6           = Traj_V1_18['ng/m3']  <= P25_V1_18
Traj_V1_18_P25  = Traj_V1_18[P25_6]

P25_7           = Traj_V2_18['ng/m3']  <= P25_V2_18
Traj_V2_18_P25  = Traj_V2_18[P25_7]

P25_8           = Traj_V3_18M['ng/m3'] <= P25_V3_18M
Traj_V3_18M_P25 = Traj_V3_18M[P25_8]

P25_9           = Traj_V3_18D['ng/m3'] <= P25_V3_18D
Traj_V3_18D_P25 = Traj_V3_18D[P25_9]

P25_10          = Traj_V4_18['ng/m3']  <= P25_V4_18
Traj_V4_18_P25  = Traj_V4_18[P25_10]

# PCAN
P25_11          = Traj_PCAN['ng/m3']   <= P25_PCAN
Traj_PCAN_P25   = Traj_PCAN[P25_11]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO >= 75th PERCENTILE

# CAMMPCAN 2017-18
P75_1           = Traj_V1_17['ng/m3']  >= P75_V1_17
Traj_V1_17_P75  = Traj_V1_17[P75_1]

P75_2           = Traj_V2_17['ng/m3']  >= P75_V2_17
Traj_V2_17_P75  = Traj_V2_17[P75_2]

P75_3           = Traj_V3_17M['ng/m3'] >= P75_V3_17M
Traj_V3_17M_P75 = Traj_V3_17M[P75_3]

P75_4           = Traj_V3_17D['ng/m3'] >= P75_V3_17D
Traj_V3_17D_P75 = Traj_V3_17D[P75_4]

P75_5           = Traj_V4_17['ng/m3']  >= P75_V4_17
Traj_V4_17_P75  = Traj_V4_17[P75_5]

# CAMMPCAN 2018-19
P75_6           = Traj_V1_18['ng/m3']  >= P75_V1_18
Traj_V1_18_P75  = Traj_V1_18[P75_6]

P75_7           = Traj_V2_18['ng/m3']  >= P75_V2_18
Traj_V2_18_P75  = Traj_V2_18[P75_7]

P75_8           = Traj_V3_18M['ng/m3'] >= P75_V3_18M
Traj_V3_18M_P75 = Traj_V3_18M[P75_8]

P75_9           = Traj_V3_18D['ng/m3'] >= P75_V3_18D
Traj_V3_18D_P75 = Traj_V3_18D[P75_9]

P75_10          = Traj_V4_18['ng/m3']  >= P75_V4_18
Traj_V4_18_P75  = Traj_V4_18[P75_10]

# PCAN
P75_11          = Traj_PCAN['ng/m3']   >= P75_PCAN
Traj_PCAN_P75   = Traj_PCAN[P75_11]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO >= 90th PERCENTILE

# CAMMPCAN 2017-18
P90_1           = Traj_V1_17['ng/m3']  >= P90_V1_17
Traj_V1_17_P90  = Traj_V1_17[P90_1]

P90_2           = Traj_V2_17['ng/m3']  >= P90_V2_17
Traj_V2_17_P90  = Traj_V2_17[P90_2]

P90_3           = Traj_V3_17M['ng/m3'] >= P90_V3_17M
Traj_V3_17M_P90 = Traj_V3_17M[P90_3]

P90_4           = Traj_V3_17D['ng/m3'] >= P90_V3_17D
Traj_V3_17D_P90 = Traj_V3_17D[P90_4]

P90_5           = Traj_V4_17['ng/m3']  >= P90_V4_17
Traj_V4_17_P90  = Traj_V4_17[P90_5]

# CAMMPCAN 2018-19
P90_6           = Traj_V1_18['ng/m3']  >= P90_V1_18
Traj_V1_18_P90  = Traj_V1_18[P90_6]

P90_7           = Traj_V2_18['ng/m3']  >= P90_V2_18
Traj_V2_18_P90  = Traj_V2_18[P90_7]

P90_8           = Traj_V3_18M['ng/m3'] >= P90_V3_18M
Traj_V3_18M_P90 = Traj_V3_18M[P90_8]

P90_9           = Traj_V3_18D['ng/m3'] >= P90_V3_18D
Traj_V3_18D_P90 = Traj_V3_18D[P90_9]

P90_10          = Traj_V4_18['ng/m3']  >= P90_V4_18
Traj_V4_18_P90  = Traj_V4_18[P90_10]

# PCAN
P90_11          = Traj_PCAN['ng/m3']   >= P90_PCAN
Traj_PCAN_P90   = Traj_PCAN[P90_11]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO >= 95th PERCENTILE

# CAMMPCAN 2017-18
P95_1           = Traj_V1_17['ng/m3']  >= P95_V1_17
Traj_V1_17_P95  = Traj_V1_17[P95_1]

P95_2           = Traj_V2_17['ng/m3']  >= P95_V2_17
Traj_V2_17_P95  = Traj_V2_17[P95_2]

P95_3           = Traj_V3_17M['ng/m3'] >= P95_V3_17M
Traj_V3_17M_P95 = Traj_V3_17M[P95_3]

P95_4           = Traj_V3_17D['ng/m3'] >= P95_V3_17D
Traj_V3_17D_P95 = Traj_V3_17D[P95_4]

P95_5           = Traj_V4_17['ng/m3']  >= P95_V4_17
Traj_V4_17_P95  = Traj_V4_17[P95_5]

# CAMMPCAN 2018-19
P95_6           = Traj_V1_18['ng/m3']  >= P95_V1_18
Traj_V1_18_P95  = Traj_V1_18[P95_6]

P95_7           = Traj_V2_18['ng/m3']  >= P95_V2_18
Traj_V2_18_P95  = Traj_V2_18[P95_7]

P95_8           = Traj_V3_18M['ng/m3'] >= P95_V3_18M
Traj_V3_18M_P95 = Traj_V3_18M[P95_8]

P95_9           = Traj_V3_18D['ng/m3'] >= P95_V3_18D
Traj_V3_18D_P95 = Traj_V3_18D[P95_9]

P95_10          = Traj_V4_18['ng/m3']  >= P95_V4_18
Traj_V4_18_P95  = Traj_V4_18[P95_10]

# PCAN
P95_11          = Traj_PCAN['ng/m3']   >= P95_PCAN
Traj_PCAN_P95   = Traj_PCAN[P95_11]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO MEDIAN (>= 45th percentile & <= 55th percentile)

# CAMMPCAN 2017-18
Median_1        = (Traj_V1_17['ng/m3']  >= P45_V1_17)  & (Traj_V1_17['ng/m3']  <= P55_V1_17)
Traj_V1_17_Med  = Traj_V1_17[Median_1]

Median_2        = (Traj_V2_17['ng/m3']  >= P45_V2_17)  & (Traj_V2_17['ng/m3']  <= P55_V2_17)
Traj_V2_17_Med  = Traj_V2_17[Median_2]

Median_3        = (Traj_V3_17M['ng/m3'] >= P45_V3_17M) & (Traj_V3_17M['ng/m3'] <= P55_V3_17M)
Traj_V3_17M_Med = Traj_V3_17M[Median_3]

Median_4        = (Traj_V3_17D['ng/m3'] >= P45_V3_17D) & (Traj_V3_17D['ng/m3'] <= P55_V3_17D)
Traj_V3_17D_Med = Traj_V3_17D[Median_4]

Median_5        = (Traj_V4_17['ng/m3']  >= P45_V4_17)  & (Traj_V4_17['ng/m3']  <= P55_V4_17)
Traj_V4_17_Med  = Traj_V4_17[Median_5]

# CAMMPCAN 2018-19
Median_6        = (Traj_V1_18['ng/m3']  >= P45_V1_18)  & (Traj_V1_18['ng/m3']  <= P55_V1_18)
Traj_V1_18_Med  = Traj_V1_18[Median_6]

Median_7        = (Traj_V2_18['ng/m3']  >= P45_V2_18)  & (Traj_V2_18['ng/m3']  <= P55_V2_18)
Traj_V2_18_Med  = Traj_V2_18[Median_7]

Median_8        = (Traj_V3_18M['ng/m3'] >= P45_V3_18M) & (Traj_V3_18M['ng/m3'] <= P55_V3_18M)
Traj_V3_18M_Med = Traj_V3_18M[Median_8]

Median_9        = (Traj_V3_18D['ng/m3'] >= P45_V3_18D) & (Traj_V3_18D['ng/m3'] <= P55_V3_18D)
Traj_V3_18D_Med = Traj_V3_18D[Median_9]

Median_10       = (Traj_V4_18['ng/m3']  >= P45_V4_18)  & (Traj_V4_18['ng/m3']  <= P55_V4_18)
Traj_V4_18_Med  = Traj_V4_18[Median_10]

# PCAN
Median_11       = (Traj_PCAN['ng/m3']   >= P45_PCAN)   & (Traj_PCAN['ng/m3']   <= P55_PCAN)
Traj_PCAN_Med   = Traj_PCAN[Median_11]

#------------------------------------------------------------------------------
# FILTER TRAJ FOR WHEN BrO IS WITHIN THE IQR

# CAMMPCAN 2017-18
IQR_1        = (Traj_V1_17['ng/m3']  >= Med_M_MAD_V1_17)  & (Traj_V1_17['ng/m3']  <= Med_P_MAD_V1_17)
Traj_V1_17_IQR  = Traj_V1_17[IQR_1]

IQR_2        = (Traj_V2_17['ng/m3']  >= Med_M_MAD_V2_17)  & (Traj_V2_17['ng/m3']  <= Med_P_MAD_V2_17)
Traj_V2_17_IQR  = Traj_V2_17[IQR_2]

IQR_3        = (Traj_V3_17M['ng/m3'] >= Med_M_MAD_V3_17M) & (Traj_V3_17M['ng/m3'] <= Med_P_MAD_V3_17M)
Traj_V3_17M_IQR = Traj_V3_17M[IQR_3]

IQR_4        = (Traj_V3_17D['ng/m3'] >= Med_M_MAD_V3_17D) & (Traj_V3_17D['ng/m3'] <= Med_P_MAD_V3_17D)
Traj_V3_17D_IQR = Traj_V3_17D[IQR_4]

IQR_5        = (Traj_V4_17['ng/m3']  >= Med_M_MAD_V4_17)  & (Traj_V4_17['ng/m3']  <= Med_P_MAD_V4_17)
Traj_V4_17_IQR  = Traj_V4_17[IQR_5]

# CAMMPCAN 2018-19
IQR_6        = (Traj_V1_18['ng/m3']  >= Med_M_MAD_V1_18)  & (Traj_V1_18['ng/m3']  <= Med_P_MAD_V1_18)
Traj_V1_18_IQR  = Traj_V1_18[IQR_6]

IQR_7        = (Traj_V2_18['ng/m3']  >= Med_M_MAD_V2_18)  & (Traj_V2_18['ng/m3']  <= Med_P_MAD_V2_18)
Traj_V2_18_IQR  = Traj_V2_18[IQR_7]

IQR_8        = (Traj_V3_18M['ng/m3'] >= Med_M_MAD_V3_18M) & (Traj_V3_18M['ng/m3'] <= Med_P_MAD_V3_18M)
Traj_V3_18M_IQR = Traj_V3_18M[IQR_8]

IQR_9        = (Traj_V3_18D['ng/m3'] >= Med_M_MAD_V3_18D) & (Traj_V3_18D['ng/m3'] <= Med_P_MAD_V3_18D)
Traj_V3_18D_IQR = Traj_V3_18D[IQR_9]

IQR_10       = (Traj_V4_18['ng/m3']  >= Med_M_MAD_V4_18)  & (Traj_V4_18['ng/m3']  <= Med_P_MAD_V4_18)
Traj_V4_18_IQR  = Traj_V4_18[IQR_10]

# PCAN
IQR_11       = (Traj_PCAN['ng/m3']   >= Med_M_MAD_PCAN)   & (Traj_PCAN['ng/m3'] <= Med_P_MAD_PCAN)
Traj_PCAN_IQR   = Traj_PCAN[IQR_11]

#------------------------------------------------------------------------------
# GET TRAJECTORIES FOR ONLY TRAJ AGE = 0

#--------------
# P5
#--------------
# CAMMPCAN 2017-18
Filter1          = Traj_V1_17_P5['Traj Age']  == 0.0
Traj_V1_17_P5_B  = Traj_V1_17_P5[Filter1]

Filter1          = Traj_V2_17_P5['Traj Age']  == 0.0
Traj_V2_17_P5_B  = Traj_V2_17_P5[Filter1]

Filter1          = Traj_V3_17M_P5['Traj Age'] == 0.0
Traj_V3_17M_P5_B = Traj_V3_17M_P5[Filter1]

Filter1          = Traj_V3_17D_P5['Traj Age'] == 0.0
Traj_V3_17D_P5_B = Traj_V3_17D_P5[Filter1]

Filter1          = Traj_V4_17_P5['Traj Age']  == 0.0
Traj_V4_17_P5_B  = Traj_V4_17_P5[Filter1]

# CAMMPCAN 2018-19
Filter1          = Traj_V1_18_P5['Traj Age']  == 0.0
Traj_V1_18_P5_B  = Traj_V1_18_P5[Filter1]

Filter1          = Traj_V2_18_P5['Traj Age']  == 0.0
Traj_V2_18_P5_B  = Traj_V2_18_P5[Filter1]

Filter1          = Traj_V3_18M_P5['Traj Age'] == 0.0
Traj_V3_18M_P5_B = Traj_V3_18M_P5[Filter1]

Filter1          = Traj_V3_18D_P5['Traj Age'] == 0.0
Traj_V3_18D_P5_B = Traj_V3_18D_P5[Filter1]

Filter1          = Traj_V4_18_P5['Traj Age']  == 0.0
Traj_V4_18_P5_B  = Traj_V4_18_P5[Filter1]

# PCAN
Filter1          = Traj_PCAN_P5['Traj Age']   == 0.0
Traj_PCAN_P5_B   = Traj_PCAN_P5[Filter1]

#--------------
# P10
#--------------
# CAMMPCAN 2017-18
Filter1           = Traj_V1_17_P10['Traj Age']  == 0.0
Traj_V1_17_P10_B  = Traj_V1_17_P10[Filter1]

Filter1           = Traj_V2_17_P10['Traj Age']  == 0.0
Traj_V2_17_P10_B  = Traj_V2_17_P10[Filter1]

Filter1           = Traj_V3_17M_P10['Traj Age'] == 0.0
Traj_V3_17M_P10_B = Traj_V3_17M_P10[Filter1]

Filter1           = Traj_V3_17D_P10['Traj Age'] == 0.0
Traj_V3_17D_P10_B = Traj_V3_17D_P10[Filter1]

Filter1           = Traj_V4_17_P10['Traj Age']  == 0.0
Traj_V4_17_P10_B  = Traj_V4_17_P10[Filter1]

# CAMMPCAN 2018-19
Filter1           = Traj_V1_18_P10['Traj Age']  == 0.0
Traj_V1_18_P10_B  = Traj_V1_18_P10[Filter1]

Filter1           = Traj_V2_18_P10['Traj Age']  == 0.0
Traj_V2_18_P10_B  = Traj_V2_18_P10[Filter1]

Filter1           = Traj_V3_18M_P10['Traj Age'] == 0.0
Traj_V3_18M_P10_B = Traj_V3_18M_P10[Filter1]

Filter1           = Traj_V3_18D_P10['Traj Age'] == 0.0
Traj_V3_18D_P10_B = Traj_V3_18D_P10[Filter1]

Filter1           = Traj_V4_18_P10['Traj Age']  == 0.0
Traj_V4_18_P10_B  = Traj_V4_18_P10[Filter1]

# PCAN
Filter1           = Traj_PCAN_P10['Traj Age']   == 0.0
Traj_PCAN_P10_B   = Traj_PCAN_P10[Filter1]

#--------------
# P25
#--------------
# CAMMPCAN 2017-18
Filter1           = Traj_V1_17_P25['Traj Age']  == 0.0
Traj_V1_17_P25_B  = Traj_V1_17_P25[Filter1]

Filter1           = Traj_V2_17_P25['Traj Age']  == 0.0
Traj_V2_17_P25_B  = Traj_V2_17_P25[Filter1]

Filter1           = Traj_V3_17M_P25['Traj Age'] == 0.0
Traj_V3_17M_P25_B = Traj_V3_17M_P25[Filter1]

Filter1           = Traj_V3_17D_P25['Traj Age'] == 0.0
Traj_V3_17D_P25_B = Traj_V3_17D_P25[Filter1]

Filter1           = Traj_V4_17_P25['Traj Age']  == 0.0
Traj_V4_17_P25_B  = Traj_V4_17_P25[Filter1]

# CAMMPCAN 2018-19
Filter1           = Traj_V1_18_P25['Traj Age']  == 0.0
Traj_V1_18_P25_B  = Traj_V1_18_P25[Filter1]

Filter1           = Traj_V2_18_P25['Traj Age']  == 0.0
Traj_V2_18_P25_B  = Traj_V2_18_P25[Filter1]

Filter1           = Traj_V3_18M_P25['Traj Age'] == 0.0
Traj_V3_18M_P25_B = Traj_V3_18M_P25[Filter1]

Filter1           = Traj_V3_18D_P25['Traj Age'] == 0.0
Traj_V3_18D_P25_B = Traj_V3_18D_P25[Filter1]

Filter1           = Traj_V4_18_P25['Traj Age']  == 0.0
Traj_V4_18_P25_B  = Traj_V4_18_P25[Filter1]

# PCAN
Filter1           = Traj_PCAN_P25['Traj Age']   == 0.0
Traj_PCAN_P25_B   = Traj_PCAN_P25[Filter1]

#--------------
# P75
#--------------
# CAMMPCAN 2017-18
Filter1           = Traj_V1_17_P75['Traj Age']  == 0.0
Traj_V1_17_P75_B  = Traj_V1_17_P75[Filter1]

Filter1           = Traj_V2_17_P75['Traj Age']  == 0.0
Traj_V2_17_P75_B  = Traj_V2_17_P75[Filter1]

Filter1           = Traj_V3_17M_P75['Traj Age'] == 0.0
Traj_V3_17M_P75_B = Traj_V3_17M_P75[Filter1]

Filter1           = Traj_V3_17D_P75['Traj Age'] == 0.0
Traj_V3_17D_P75_B = Traj_V3_17D_P75[Filter1]

Filter1           = Traj_V4_17_P75['Traj Age']  == 0.0
Traj_V4_17_P75_B  = Traj_V4_17_P75[Filter1]

# CAMMPCAN 2018-19
Filter1           = Traj_V1_18_P75['Traj Age']  == 0.0
Traj_V1_18_P75_B  = Traj_V1_18_P75[Filter1]

Filter1           = Traj_V2_18_P75['Traj Age']  == 0.0
Traj_V2_18_P75_B  = Traj_V2_18_P75[Filter1]

Filter1           = Traj_V3_18M_P75['Traj Age'] == 0.0
Traj_V3_18M_P75_B = Traj_V3_18M_P75[Filter1]

Filter1           = Traj_V3_18D_P75['Traj Age'] == 0.0
Traj_V3_18D_P75_B = Traj_V3_18D_P75[Filter1]

Filter1           = Traj_V4_18_P75['Traj Age']  == 0.0
Traj_V4_18_P75_B  = Traj_V4_18_P75[Filter1]

# PCAN
Filter1           = Traj_PCAN_P75['Traj Age']   == 0.0
Traj_PCAN_P75_B   = Traj_PCAN_P75[Filter1]

#--------------
# P90
#--------------
# CAMMPCAN 2017-18
Filter1           = Traj_V1_17_P90['Traj Age']  == 0.0
Traj_V1_17_P90_B  = Traj_V1_17_P90[Filter1]

Filter1           = Traj_V2_17_P90['Traj Age']  == 0.0
Traj_V2_17_P90_B  = Traj_V2_17_P90[Filter1]

Filter1           = Traj_V3_17M_P90['Traj Age'] == 0.0
Traj_V3_17M_P90_B = Traj_V3_17M_P90[Filter1]

Filter1           = Traj_V3_17D_P90['Traj Age'] == 0.0
Traj_V3_17D_P90_B = Traj_V3_17D_P90[Filter1]

Filter1           = Traj_V4_17_P90['Traj Age']  == 0.0
Traj_V4_17_P90_B  = Traj_V4_17_P90[Filter1]

# CAMMPCAN 2018-19
Filter1           = Traj_V1_18_P90['Traj Age']  == 0.0
Traj_V1_18_P90_B  = Traj_V1_18_P90[Filter1]

Filter1           = Traj_V2_18_P90['Traj Age']  == 0.0
Traj_V2_18_P90_B  = Traj_V2_18_P90[Filter1]

Filter1           = Traj_V3_18M_P90['Traj Age'] == 0.0
Traj_V3_18M_P90_B = Traj_V3_18M_P90[Filter1]

Filter1           = Traj_V3_18D_P90['Traj Age'] == 0.0
Traj_V3_18D_P90_B = Traj_V3_18D_P90[Filter1]

Filter1           = Traj_V4_18_P90['Traj Age']  == 0.0
Traj_V4_18_P90_B  = Traj_V4_18_P90[Filter1]

# PCAN
Filter1           = Traj_PCAN_P90['Traj Age']   == 0.0
Traj_PCAN_P90_B   = Traj_PCAN_P90[Filter1]

#--------------
# P95
#--------------
# CAMMPCAN 2017-18
Filter1           = Traj_V1_17_P95['Traj Age']  == 0.0
Traj_V1_17_P95_B  = Traj_V1_17_P95[Filter1]

Filter1           = Traj_V2_17_P95['Traj Age']  == 0.0
Traj_V2_17_P95_B  = Traj_V2_17_P95[Filter1]

Filter1           = Traj_V3_17M_P95['Traj Age'] == 0.0
Traj_V3_17M_P95_B = Traj_V3_17M_P95[Filter1]

Filter1           = Traj_V3_17D_P95['Traj Age'] == 0.0
Traj_V3_17D_P95_B = Traj_V3_17D_P95[Filter1]

Filter1           = Traj_V4_17_P95['Traj Age']  == 0.0
Traj_V4_17_P95_B  = Traj_V4_17_P95[Filter1]

# CAMMPCAN 2018-19
Filter1           = Traj_V1_18_P95['Traj Age']  == 0.0
Traj_V1_18_P95_B  = Traj_V1_18_P95[Filter1]

Filter1           = Traj_V2_18_P95['Traj Age']  == 0.0
Traj_V2_18_P95_B  = Traj_V2_18_P95[Filter1]

Filter1           = Traj_V3_18M_P95['Traj Age'] == 0.0
Traj_V3_18M_P95_B = Traj_V3_18M_P95[Filter1]

Filter1           = Traj_V3_18D_P95['Traj Age'] == 0.0
Traj_V3_18D_P95_B = Traj_V3_18D_P95[Filter1]

Filter1           = Traj_V4_18_P95['Traj Age']  == 0.0
Traj_V4_18_P95_B  = Traj_V4_18_P95[Filter1]

# PCAN
Filter1           = Traj_PCAN_P95['Traj Age']   == 0.0
Traj_PCAN_P95_B   = Traj_PCAN_P95[Filter1]

#--------------
# Median
#--------------
# CAMMPCAN 2017-18
Filter1           = Traj_V1_17_Med['Traj Age']  == 0.0
Traj_V1_17_Med_B  = Traj_V1_17_Med[Filter1]

Filter1           = Traj_V2_17_Med['Traj Age']  == 0.0
Traj_V2_17_Med_B  = Traj_V2_17_Med[Filter1]

Filter1           = Traj_V3_17M_Med['Traj Age'] == 0.0
Traj_V3_17M_Med_B = Traj_V3_17M_Med[Filter1]

Filter1           = Traj_V3_17D_Med['Traj Age'] == 0.0
Traj_V3_17D_Med_B = Traj_V3_17D_Med[Filter1]

Filter1           = Traj_V4_17_Med['Traj Age']  == 0.0
Traj_V4_17_Med_B  = Traj_V4_17_Med[Filter1]

# CAMMPCAN 2018-19
Filter1           = Traj_V1_18_Med['Traj Age']  == 0.0
Traj_V1_18_Med_B  = Traj_V1_18_Med[Filter1]

Filter1           = Traj_V2_18_Med['Traj Age']  == 0.0
Traj_V2_18_Med_B  = Traj_V2_18_Med[Filter1]

Filter1           = Traj_V3_18M_Med['Traj Age'] == 0.0
Traj_V3_18M_Med_B = Traj_V3_18M_Med[Filter1]

Filter1           = Traj_V3_18D_Med['Traj Age'] == 0.0
Traj_V3_18D_Med_B = Traj_V3_18D_Med[Filter1]

Filter1           = Traj_V4_18_Med['Traj Age']  == 0.0
Traj_V4_18_Med_B  = Traj_V4_18_Med[Filter1]

# PCAN
Filter1           = Traj_PCAN_Med['Traj Age']   == 0.0
Traj_PCAN_Med_B   = Traj_PCAN_Med[Filter1]

#--------------
# IQR
#--------------
# CAMMPCAN 2017-18
Filter1           = Traj_V1_17_IQR['Traj Age']  == 0.0
Traj_V1_17_IQR_B  = Traj_V1_17_IQR[Filter1]

Filter1           = Traj_V2_17_IQR['Traj Age']  == 0.0
Traj_V2_17_IQR_B  = Traj_V2_17_IQR[Filter1]

Filter1           = Traj_V3_17M_IQR['Traj Age'] == 0.0
Traj_V3_17M_IQR_B = Traj_V3_17M_IQR[Filter1]

Filter1           = Traj_V3_17D_IQR['Traj Age'] == 0.0
Traj_V3_17D_IQR_B = Traj_V3_17D_IQR[Filter1]

Filter1           = Traj_V4_17_IQR['Traj Age']  == 0.0
Traj_V4_17_IQR_B  = Traj_V4_17_IQR[Filter1]

# CAMMPCAN 2018-19
Filter1           = Traj_V1_18_IQR['Traj Age']  == 0.0
Traj_V1_18_IQR_B  = Traj_V1_18_IQR[Filter1]

Filter1           = Traj_V2_18_IQR['Traj Age']  == 0.0
Traj_V2_18_IQR_B  = Traj_V2_18_IQR[Filter1]

Filter1           = Traj_V3_18M_IQR['Traj Age'] == 0.0
Traj_V3_18M_IQR_B = Traj_V3_18M_IQR[Filter1]

Filter1           = Traj_V3_18D_IQR['Traj Age'] == 0.0
Traj_V3_18D_IQR_B = Traj_V3_18D_IQR[Filter1]

Filter1           = Traj_V4_18_IQR['Traj Age']  == 0.0
Traj_V4_18_IQR_B  = Traj_V4_18_IQR[Filter1]

# PCAN
Filter1           = Traj_PCAN_IQR['Traj Age']   == 0.0
Traj_PCAN_IQR_B   = Traj_PCAN_IQR[Filter1]

#------------------------------------------------------------------------------
# COUNT THE NUMBER OF OBSERVATIONS All, P5, P95, Median

# All
N_V1_17    = len(Traj_V1_17_B)
N_V2_17    = len(Traj_V2_17_B)
N_V3_17M   = len(Traj_V3_17M_B)
N_V3_17D   = len(Traj_V3_17D_B)
N_V4_17    = len(Traj_V4_17_B)

N_V1_18    = len(Traj_V1_18_B)
N_V2_18    = len(Traj_V2_18_B)
N_V3_18M   = len(Traj_V3_18M_B)
N_V3_18D   = len(Traj_V3_18D_B)
N_V4_18    = len(Traj_V4_18_B)

N_PCAN     = len(Traj_PCAN_B)

N_1718     = len(All_1718)
N_1819     = len(All_1819)
N_CAMMPCAN = len(CAMMPCAN_All)

# P5
N_V1_17_P5    = len(Traj_V1_17_P5_B)
N_V2_17_P5    = len(Traj_V2_17_P5_B)
N_V3_17M_P5   = len(Traj_V3_17M_P5_B)
N_V3_17D_P5   = len(Traj_V3_17D_P5_B)
N_V4_17_P5    = len(Traj_V4_17_P5_B)

N_V1_18_P5    = len(Traj_V1_18_P5_B)
N_V2_18_P5    = len(Traj_V2_18_P5_B)
N_V3_18M_P5   = len(Traj_V3_18M_P5_B)
N_V3_18D_P5   = len(Traj_V3_18D_P5_B)
N_V4_18_P5    = len(Traj_V4_18_P5_B)

N_PCAN_P5     = len(Traj_PCAN_P5_B)

# P10
N_V1_17_P10    = len(Traj_V1_17_P10_B)
N_V2_17_P10    = len(Traj_V2_17_P10_B)
N_V3_17M_P10   = len(Traj_V3_17M_P10_B)
N_V3_17D_P10   = len(Traj_V3_17D_P10_B)
N_V4_17_P10    = len(Traj_V4_17_P10_B)

N_V1_18_P10    = len(Traj_V1_18_P10_B)
N_V2_18_P10    = len(Traj_V2_18_P10_B)
N_V3_18M_P10   = len(Traj_V3_18M_P10_B)
N_V3_18D_P10   = len(Traj_V3_18D_P10_B)
N_V4_18_P10    = len(Traj_V4_18_P10_B)

N_PCAN_P10     = len(Traj_PCAN_P10_B)

# P25
N_V1_17_P25    = len(Traj_V1_17_P25_B)
N_V2_17_P25    = len(Traj_V2_17_P25_B)
N_V3_17M_P25   = len(Traj_V3_17M_P25_B)
N_V3_17D_P25   = len(Traj_V3_17D_P25_B)
N_V4_17_P25    = len(Traj_V4_17_P25_B)

N_V1_18_P25    = len(Traj_V1_18_P25_B)
N_V2_18_P25    = len(Traj_V2_18_P25_B)
N_V3_18M_P25   = len(Traj_V3_18M_P25_B)
N_V3_18D_P25   = len(Traj_V3_18D_P25_B)
N_V4_18_P25    = len(Traj_V4_18_P25_B)

N_PCAN_P25     = len(Traj_PCAN_P25_B)

# P75
N_V1_17_P75    = len(Traj_V1_17_P75_B)
N_V2_17_P75    = len(Traj_V2_17_P75_B)
N_V3_17M_P75   = len(Traj_V3_17M_P75_B)
N_V3_17D_P75   = len(Traj_V3_17D_P75_B)
N_V4_17_P75    = len(Traj_V4_17_P75_B)

N_V1_18_P75    = len(Traj_V1_18_P75_B)
N_V2_18_P75    = len(Traj_V2_18_P75_B)
N_V3_18M_P75   = len(Traj_V3_18M_P75_B)
N_V3_18D_P75   = len(Traj_V3_18D_P75_B)
N_V4_18_P75    = len(Traj_V4_18_P75_B)

N_PCAN_P75     = len(Traj_PCAN_P75_B)

# P90
N_V1_17_P90   = len(Traj_V1_17_P90_B)
N_V2_17_P90   = len(Traj_V2_17_P90_B)
N_V3_17M_P90  = len(Traj_V3_17M_P90_B)
N_V3_17D_P90  = len(Traj_V3_17D_P90_B)
N_V4_17_P90   = len(Traj_V4_17_P90_B)

N_V1_18_P90   = len(Traj_V1_18_P90_B)
N_V2_18_P90   = len(Traj_V2_18_P90_B)
N_V3_18M_P90  = len(Traj_V3_18M_P90_B)
N_V3_18D_P90  = len(Traj_V3_18D_P90_B)
N_V4_18_P90   = len(Traj_V4_18_P90_B)

N_PCAN_P90    = len(Traj_PCAN_P90_B)

# P95
N_V1_17_P95   = len(Traj_V1_17_P95_B)
N_V2_17_P95   = len(Traj_V2_17_P95_B)
N_V3_17M_P95  = len(Traj_V3_17M_P95_B)
N_V3_17D_P95  = len(Traj_V3_17D_P95_B)
N_V4_17_P95   = len(Traj_V4_17_P95_B)

N_V1_18_P95   = len(Traj_V1_18_P95_B)
N_V2_18_P95   = len(Traj_V2_18_P95_B)
N_V3_18M_P95  = len(Traj_V3_18M_P95_B)
N_V3_18D_P95  = len(Traj_V3_18D_P95_B)
N_V4_18_P95   = len(Traj_V4_18_P95_B)

N_PCAN_P95    = len(Traj_PCAN_P95_B)

# Median
N_V1_17_Med   = len(Traj_V1_17_Med_B)
N_V2_17_Med   = len(Traj_V2_17_Med_B)
N_V3_17M_Med  = len(Traj_V3_17M_Med_B)
N_V3_17D_Med  = len(Traj_V3_17D_Med_B)
N_V4_17_Med   = len(Traj_V4_17_Med_B)

N_V1_18_Med   = len(Traj_V1_18_Med_B)
N_V2_18_Med   = len(Traj_V2_18_Med_B)
N_V3_18M_Med  = len(Traj_V3_18M_Med_B)
N_V3_18D_Med  = len(Traj_V3_18D_Med_B)
N_V4_18_Med   = len(Traj_V4_18_Med_B)

N_PCAN_Med    = len(Traj_PCAN_Med_B)

# IQR
N_V1_17_IQR   = len(Traj_V1_17_IQR_B)
N_V2_17_IQR   = len(Traj_V2_17_IQR_B)
N_V3_17M_IQR  = len(Traj_V3_17M_IQR_B)
N_V3_17D_IQR  = len(Traj_V3_17D_IQR_B)
N_V4_17_IQR   = len(Traj_V4_17_IQR_B)

N_V1_18_IQR   = len(Traj_V1_18_IQR_B)
N_V2_18_IQR   = len(Traj_V2_18_IQR_B)
N_V3_18M_IQR  = len(Traj_V3_18M_IQR_B)
N_V3_18D_IQR  = len(Traj_V3_18D_IQR_B)
N_V4_18_IQR   = len(Traj_V4_18_IQR_B)

N_PCAN_IQR    = len(Traj_PCAN_IQR_B)

#------------------------------------------------------------------------------
# CALCULATE THE MEAN HG0

# Overall
Mean_V1_17    = np.mean(Traj_V1_17_B['ng/m3'])
Mean_V2_17    = np.mean(Traj_V2_17_B['ng/m3'])
Mean_V3_17M   = np.mean(Traj_V3_17M_B['ng/m3'])
Mean_V3_17D   = np.mean(Traj_V3_17D_B['ng/m3'])
Mean_V4_17    = np.mean(Traj_V4_17_B['ng/m3'])

Mean_V1_18    = np.mean(Traj_V1_18_B['ng/m3'])
Mean_V2_18    = np.mean(Traj_V2_18_B['ng/m3'])
Mean_V3_18M   = np.mean(Traj_V3_18M_B['ng/m3'])
Mean_V3_18D   = np.mean(Traj_V3_18D_B['ng/m3'])
Mean_V4_18    = np.mean(Traj_V4_18_B['ng/m3'])

Mean_PCAN     = np.mean(Traj_PCAN_B['ng/m3'])

Mean_1718     = np.mean(All_1718['ng/m3'])
Mean_1819     = np.mean(All_1819['ng/m3'])
Mean_CAMMPCAN = np.mean(CAMMPCAN_All['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE ST DEV HG0

# Overall
std_V1_17    = np.std(Traj_V1_17_B['ng/m3'])
std_V2_17    = np.std(Traj_V2_17_B['ng/m3'])
std_V3_17M   = np.std(Traj_V3_17M_B['ng/m3'])
std_V3_17D   = np.std(Traj_V3_17D_B['ng/m3'])
std_V4_17    = np.std(Traj_V4_17_B['ng/m3'])

std_V1_18    = np.std(Traj_V1_18_B['ng/m3'])
std_V2_18    = np.std(Traj_V2_18_B['ng/m3'])
std_V3_18M   = np.std(Traj_V3_18M_B['ng/m3'])
std_V3_18D   = np.std(Traj_V3_18D_B['ng/m3'])
std_V4_18    = np.std(Traj_V4_18_B['ng/m3'])

std_PCAN     = np.std(Traj_PCAN_B['ng/m3'])

std_1718     = np.std(All_1718['ng/m3'])
std_1819     = np.std(All_1819['ng/m3'])
std_CAMMPCAN = np.std(CAMMPCAN_All['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MIN HG0

# Overall
Min_V1_17    = np.min(Traj_V1_17_B['ng/m3'])
Min_V2_17    = np.min(Traj_V2_17_B['ng/m3'])
Min_V3_17M   = np.min(Traj_V3_17M_B['ng/m3'])
Min_V3_17D   = np.min(Traj_V3_17D_B['ng/m3'])
Min_V4_17    = np.min(Traj_V4_17_B['ng/m3'])

Min_V1_18    = np.min(Traj_V1_18_B['ng/m3'])
Min_V2_18    = np.min(Traj_V2_18_B['ng/m3'])
Min_V3_18M   = np.min(Traj_V3_18M_B['ng/m3'])
Min_V3_18D   = np.min(Traj_V3_18D_B['ng/m3'])
Min_V4_18    = np.min(Traj_V4_18_B['ng/m3'])

Min_PCAN     = np.min(Traj_PCAN_B['ng/m3'])

Min_1718     = np.min(All_1718['ng/m3'])
Min_1819     = np.min(All_1819['ng/m3'])
Min_CAMMPCAN = np.min(CAMMPCAN_All['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MAX HG0

# Overall
Max_V1_17    = np.max(Traj_V1_17_B['ng/m3'])
Max_V2_17    = np.max(Traj_V2_17_B['ng/m3'])
Max_V3_17M   = np.max(Traj_V3_17M_B['ng/m3'])
Max_V3_17D   = np.max(Traj_V3_17D_B['ng/m3'])
Max_V4_17    = np.max(Traj_V4_17_B['ng/m3'])

Max_V1_18    = np.max(Traj_V1_18_B['ng/m3'])
Max_V2_18    = np.max(Traj_V2_18_B['ng/m3'])
Max_V3_18M   = np.max(Traj_V3_18M_B['ng/m3'])
Max_V3_18D   = np.max(Traj_V3_18D_B['ng/m3'])
Max_V4_18    = np.max(Traj_V4_18_B['ng/m3'])

Max_PCAN     = np.max(Traj_PCAN_B['ng/m3'])

Max_1718     = np.max(All_1718['ng/m3'])
Max_1819     = np.max(All_1819['ng/m3'])
Max_CAMMPCAN = np.max(CAMMPCAN_All['ng/m3'])

#------------------------------------------------------------------------------
#BUILD DATAFRAME FOR THE STATISTICAL RESULTS (Percentiles)

# Build a pandas dataframe (Seasonal Met)
dfHg_AirMass = {'N':        [N_1718,           N_1819,           N_CAMMPCAN,         N_PCAN,
                              N_V1_17,          N_V2_17,          N_V3_17M,           N_V3_17D,          N_V4_17,
                              N_V1_18,          N_V2_18,          N_V3_18M,           N_V3_18D,          N_V4_18],
                'Mean':     [Mean_1718,        Mean_1819,        Mean_CAMMPCAN,      Mean_PCAN,
                              Mean_V1_17,       Mean_V2_17,       Mean_V3_17M,        Mean_V3_17D,       Mean_V4_17,
                              Mean_V1_18,       Mean_V2_18,       Mean_V3_18M,        Mean_V3_18D,       Mean_V4_18],
                'StDev':    [std_1718,         std_1819,         std_CAMMPCAN,       std_PCAN,
                              std_V1_17,        std_V2_17,        std_V3_17M,         std_V3_17D,        std_V4_17,
                              std_V1_18,        std_V2_18,        std_V3_18M,         std_V3_18D,        std_V4_18],
                'Median':   [Median_1718,      Median_1819,      Median_CAMMPCAN,    Median_PCAN,
                              Median_V1_17,     Median_V2_17,     Median_V3_17M,      Median_V3_17D,     Median_V4_17,
                              Median_V1_18,     Median_V2_18,     Median_V3_18M,      Median_V3_18D,     Median_V4_18],
                'MAD':      [MAD_1718,         MAD_1819,         MAD_CAMMPCAN,       MAD_PCAN,
                              MAD_V1_17,        MAD_V2_17,        MAD_V3_17M,         MAD_V3_17D,        MAD_V4_17,
                              MAD_V1_18,        MAD_V2_18,        MAD_V3_18M,         MAD_V3_18D,        MAD_V4_18],
                'Med_M_MAD':[Med_M_MAD_1718,   Med_M_MAD_1819,   Med_M_MAD_CAMMPCAN, Med_M_MAD_PCAN,
                              Med_M_MAD_V1_17,  Med_M_MAD_V2_17,  Med_M_MAD_V3_17M,    Med_M_MAD_V3_17D, Med_M_MAD_V4_17,
                              Med_M_MAD_V1_18,  Med_M_MAD_V2_18,  Med_M_MAD_V3_18M,    Med_M_MAD_V3_18D, Med_M_MAD_V4_18],
                'Med_P_MAD':[Med_P_MAD_1718,   Med_P_MAD_1819,   Med_P_MAD_CAMMPCAN, Med_P_MAD_PCAN,
                              Med_P_MAD_V1_17,  Med_P_MAD_V2_17,  Med_P_MAD_V3_17M,    Med_P_MAD_V3_17D, Med_P_MAD_V4_17,
                              Med_P_MAD_V1_18,  Med_P_MAD_V2_18,  Med_P_MAD_V3_18M,    Med_P_MAD_V3_18D, Med_P_MAD_V4_18],
                'P5':       [P5_1718,          P5_1819,          P5_CAMMPCAN,        P5_PCAN,
                              P5_V1_17,         P5_V2_17,         P5_V3_17M,          P5_V3_17D,         P5_V4_17,
                              P5_V1_18,         P5_V2_18,         P5_V3_18M,          P5_V3_18D,         P5_V4_18],
                'P10':      [P10_1718,         P10_1819,         P10_CAMMPCAN,       P10_PCAN,
                              P10_V1_17,        P10_V2_17,        P10_V3_17M,         P10_V3_17D,        P10_V4_17,
                              P10_V1_18,        P10_V2_18,        P10_V3_18M,         P10_V3_18D,        P10_V4_18],
                'P25':      [P25_1718,         P25_1819,         P25_CAMMPCAN,       P25_PCAN,
                              P25_V1_17,        P25_V2_17,        P25_V3_17M,         P25_V3_17D,        P25_V4_17,
                              P25_V1_18,        P25_V2_18,        P25_V3_18M,         P25_V3_18D,        P25_V4_18],
                'P75':      [P75_1718,         P75_1819,         P75_CAMMPCAN,       P75_PCAN,
                              P75_V1_17,        P75_V2_17,        P75_V3_17M,         P75_V3_17D,        P75_V4_17,
                              P75_V1_18,        P75_V2_18,        P75_V3_18M,         P75_V3_18D,        P75_V4_18],
                'P90':      [P90_1718,         P90_1819,         P90_CAMMPCAN,       P90_PCAN,
                              P90_V1_17,        P90_V2_17,        P90_V3_17M,         P90_V3_17D,        P90_V4_17,
                              P90_V1_18,        P90_V2_18,        P90_V3_18M,         P90_V3_18D,        P90_V4_18],
                'P95':      [P95_1718,         P95_1819,         P95_CAMMPCAN,       P95_PCAN,
                              P95_V1_17,        P95_V2_17,        P95_V3_17M,         P95_V3_17D,        P95_V4_17,
                              P95_V1_18,        P95_V2_18,        P95_V3_18M,         P95_V3_18D,        P95_V4_18],
                'Min':      [Min_1718,         Min_1819,         Min_CAMMPCAN,       Min_PCAN,
                              Min_V1_17,        Min_V2_17,        Min_V3_17M,         Min_V3_17D,        Min_V4_17,
                              Min_V1_18,        Min_V2_18,        Min_V3_18M,         Min_V3_18D,        Min_V4_18],
                'Max':      [Max_1718,         Max_1819,         Max_CAMMPCAN,       Max_PCAN,
                              Max_V1_17,        Max_V2_17,        Max_V3_17M,         Max_V3_17D,        Max_V4_17,
                              Max_V1_18,        Max_V2_18,        Max_V3_18M,         Max_V3_18D,        Max_V4_18]}
dfHg_AirMass = pd.DataFrame(dfHg_AirMass, columns = ['N','Mean','StDev','Median','MAD','Med_M_MAD','Med_P_MAD','P5','P10','P25','P75','P90','P95','Min','Max'],
                            index = ['All_1718','All_1819','All_CAMMPCAN','PCAN',
                                     'V1_17','V2_17','V3_17M','V3_17D','V4_17',
                                     'V1_18','V2_18','V3_18M','V3_18D','V4_18'])
dfHg_AirMass.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_Stats_Percentiles.csv')

#------------------------------------------------------------------------------
# VARIABLES FOR PLOTTING SEA ICE COVER

# Sea ice
seaice_data_V1_17  = SeaIce_V1_17.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V2_17  = SeaIce_V2_17.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V3_17M = SeaIce_V3_17M.variables['ice'][0,0,:,:]   # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V3_17D = SeaIce_V3_17D.variables['ice'][0,0,:,:]   # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V4_17  = SeaIce_V4_17.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)

seaice_data_V1_18  = SeaIce_V1_18.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V2_18  = SeaIce_V2_18.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V3_18M = SeaIce_V3_18M.variables['ice'][0,0,:,:]   # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V3_18D = SeaIce_V3_18D.variables['ice'][0,0,:,:]   # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_V4_18  = SeaIce_V4_18.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)

seaice_data_SIPEXII = SeaIce_SIPEXII.variables['ice'][0,0,:,:] # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)
seaice_data_PCAN    = SeaIce_PCAN.variables['sea_ice_area_fraction'][0,:,:]    # Sea Ice concentration (time,y,x)(1,1,632,664)
#seaice_data_PCAN    = SeaIce_PCAN.variables['ice'][0,0,:,:]    # Sea Ice concentration (time,lev,y,x)(1,1,720,1440)

land_PCAN = SeaIce_PCAN.variables['land'][0,:,:] 

# Latitudes
lats_V1_17   = SeaIce_V1_17.lat
lats_V2_17   = SeaIce_V2_17.lat
lats_V3_17M  = SeaIce_V3_17M.lat
lats_V3_17D  = SeaIce_V3_17D.lat
lats_V4_17   = SeaIce_V4_17.lat

lats_V1_18   = SeaIce_V1_18.lat
lats_V2_18   = SeaIce_V2_18.lat
lats_V3_18M  = SeaIce_V3_18M.lat
lats_V3_18D  = SeaIce_V3_18D.lat
lats_V4_18   = SeaIce_V4_18.lat

lats_SIPEXII = SeaIce_SIPEXII.lat
lats_PCAN    = SeaIce_PCAN.latitude
#lats_PCAN    = SeaIce_PCAN.lat

# Longitudes
lons_V1_17   = SeaIce_V1_17.lon
lons_V2_17   = SeaIce_V2_17.lon
lons_V3_17M  = SeaIce_V3_17M.lon
lons_V3_17D  = SeaIce_V3_17D.lon
lons_V4_17   = SeaIce_V4_17.lon

lons_V1_18   = SeaIce_V1_18.lon
lons_V2_18   = SeaIce_V2_18.lon
lons_V3_18M  = SeaIce_V3_18M.lon
lons_V3_18D  = SeaIce_V3_18D.lon
lons_V4_18   = SeaIce_V4_18.lon

lons_SIPEXII = SeaIce_SIPEXII.lon
lons_PCAN    = SeaIce_PCAN.longitude
#lons_PCAN    = SeaIce_PCAN.lon

# The data are defined in lat/lon coordinate system, so PlateCarree()
# is the appropriate coordinate system:
data_crs = ccrs.PlateCarree()

#------------------------------------------------------------------------------
# SORT TRAJECTORIES BY Hg0 CONCENTRATION (LOW TO HIGH)

# All
Traj_V1_17  = Traj_V1_17.sort_values(by=['ng/m3'],  ascending=True)
Traj_V2_17  = Traj_V2_17.sort_values(by=['ng/m3'],  ascending=True)
Traj_V3_17M = Traj_V3_17M.sort_values(by=['ng/m3'], ascending=True)
Traj_V3_17D = Traj_V3_17D.sort_values(by=['ng/m3'], ascending=True)
Traj_V4_17  = Traj_V4_17.sort_values(by=['ng/m3'],  ascending=True)

Traj_V1_18  = Traj_V1_18.sort_values(by=['ng/m3'],  ascending=True)
Traj_V2_18  = Traj_V2_18.sort_values(by=['ng/m3'],  ascending=True)
Traj_V3_18M = Traj_V3_18M.sort_values(by=['ng/m3'], ascending=True)
Traj_V3_18D = Traj_V3_18D.sort_values(by=['ng/m3'], ascending=True)
Traj_V4_18  = Traj_V4_18.sort_values(by=['ng/m3'],  ascending=True)

Traj_PCAN   = Traj_PCAN.sort_values(by=['ng/m3'],   ascending=True)

# P10
Traj_V1_17_P10  = Traj_V1_17_P10.sort_values(by=['ng/m3'],  ascending=True)
Traj_V2_17_P10  = Traj_V2_17_P10.sort_values(by=['ng/m3'],  ascending=True)
Traj_V3_17M_P10 = Traj_V3_17M_P10.sort_values(by=['ng/m3'], ascending=True)
Traj_V3_17D_P10 = Traj_V3_17D_P10.sort_values(by=['ng/m3'], ascending=True)
Traj_V4_17_P10  = Traj_V4_17_P10.sort_values(by=['ng/m3'],  ascending=True)

Traj_V1_18_P10  = Traj_V1_18_P10.sort_values(by=['ng/m3'],  ascending=True)
Traj_V2_18_P10  = Traj_V2_18_P10.sort_values(by=['ng/m3'],  ascending=True)
Traj_V3_18M_P10 = Traj_V3_18M_P10.sort_values(by=['ng/m3'], ascending=True)
Traj_V3_18D_P10 = Traj_V3_18D_P10.sort_values(by=['ng/m3'], ascending=True)
Traj_V4_18_P10  = Traj_V4_18_P10.sort_values(by=['ng/m3'],  ascending=True)

Traj_PCAN_P10   = Traj_PCAN_P10.sort_values(by=['ng/m3'],   ascending=True)

# IQR
Traj_V1_17_IQR  = Traj_V1_17_IQR.sort_values(by=['ng/m3'],  ascending=True)
Traj_V2_17_IQR  = Traj_V2_17_IQR.sort_values(by=['ng/m3'],  ascending=True)
Traj_V3_17M_IQR = Traj_V3_17M_IQR.sort_values(by=['ng/m3'], ascending=True)
Traj_V3_17D_IQR = Traj_V3_17D_IQR.sort_values(by=['ng/m3'], ascending=True)
Traj_V4_17_IQR  = Traj_V4_17_IQR.sort_values(by=['ng/m3'],  ascending=True)

Traj_V1_18_IQR  = Traj_V1_18_IQR.sort_values(by=['ng/m3'],  ascending=True)
Traj_V2_18_IQR  = Traj_V2_18_IQR.sort_values(by=['ng/m3'],  ascending=True)
Traj_V3_18M_IQR = Traj_V3_18M_IQR.sort_values(by=['ng/m3'], ascending=True)
Traj_V3_18D_IQR = Traj_V3_18D_IQR.sort_values(by=['ng/m3'], ascending=True)
Traj_V4_18_IQR  = Traj_V4_18_IQR.sort_values(by=['ng/m3'],  ascending=True)

Traj_PCAN_IQR   = Traj_PCAN_IQR.sort_values(by=['ng/m3'],   ascending=True)

# P90
Traj_V1_17_P90  = Traj_V1_17_P90.sort_values(by=['ng/m3'],  ascending=True)
Traj_V2_17_P90  = Traj_V2_17_P90.sort_values(by=['ng/m3'],  ascending=True)
Traj_V3_17M_P90 = Traj_V3_17M_P90.sort_values(by=['ng/m3'], ascending=True)
Traj_V3_17D_P90 = Traj_V3_17D_P90.sort_values(by=['ng/m3'], ascending=True)
Traj_V4_17_P90  = Traj_V4_17_P90.sort_values(by=['ng/m3'],  ascending=True)

Traj_V1_18_P90  = Traj_V1_18_P90.sort_values(by=['ng/m3'],  ascending=True)
Traj_V2_18_P90  = Traj_V2_18_P90.sort_values(by=['ng/m3'],  ascending=True)
Traj_V3_18M_P90 = Traj_V3_18M_P90.sort_values(by=['ng/m3'], ascending=True)
Traj_V3_18D_P90 = Traj_V3_18D_P90.sort_values(by=['ng/m3'], ascending=True)
Traj_V4_18_P90  = Traj_V4_18_P90.sort_values(by=['ng/m3'],  ascending=True)

Traj_PCAN_P90   = Traj_PCAN_P90.sort_values(by=['ng/m3'],   ascending=True)

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
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V1_17['IceContact_100m'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17['ng/m3'], label='Traj Height (m)')

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
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_17['Traj Lon'], Traj_V2_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V2_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V2_17['Traj Lon'], Traj_V2_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17['ng/m3'], label='Traj Height (m)')

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
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17M['Traj Lon'], Traj_V3_17M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_17M['Traj Lon'], Traj_V3_17M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M['ng/m3'], label='Traj Height (m)')

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
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17D['Traj Lon'], Traj_V3_17D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_17D['Traj Lon'], Traj_V3_17D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D['ng/m3'], label='Traj Height (m)')

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
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V1_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V1_18['Traj Lon'], Traj_V1_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18['ng/m3'], label='Traj Height (m)')

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
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_17['Traj Lon'], Traj_V2_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V2_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V2_18['Traj Lon'], Traj_V2_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18['ng/m3'], label='Traj Height (m)')

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
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17M['Traj Lon'], Traj_V3_17M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18M['Traj Lon'], Traj_V3_18M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M['ng/m3'], label='Traj Height (m)')

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
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17D['Traj Lon'], Traj_V3_17D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18D['Traj Lon'], Traj_V3_18D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D['ng/m3'], label='Traj Height (m)')

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
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$')

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_17_P5['Traj Lon'], Traj_V1_17_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_P5['Traj Height (m)'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_17_P10['Traj Lon'], Traj_V1_17_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_P10['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_17_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_17_P5['Traj Lon'], Traj_V2_17_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_P5['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V2_17_P10['Traj Lon'], Traj_V2_17_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_P10['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_17_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration


#ax.scatter(Traj_V3_17M_P5['Traj Lon'], Traj_V3_17M_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M_P5['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V3_17M_P10['Traj Lon'], Traj_V3_17M_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M_P10['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17M_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17D_P5['Traj Lon'], Traj_V3_17D_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D_P5['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V3_17D_P10['Traj Lon'], Traj_V3_17D_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D_P10['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17D_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_17_Med['Traj Lon'], Traj_V1_17_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_Med['Traj Height (m)'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_17_Med['Traj Lon'], Traj_V1_17_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_Med['ng/m3'], label='Traj Height (m)')
#cs2 = ax.scatter(Traj_V1_17_IQR['Traj Lon'], Traj_V1_17_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_IQR['ng/m3'], label='Traj Height (m)')

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
#ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_17_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_17_Med+1)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V2_17_Med['Traj Lon'], Traj_V2_17_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_Med['ng/m3'], label='Traj Height (m)')
#ax.scatter(Traj_V2_17_IQR['Traj Lon'], Traj_V2_17_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_IQR['ng/m3'], label='Traj Height (m)')

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
#ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_17_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration


ax.scatter(Traj_V3_17M_Med['Traj Lon'], Traj_V3_17M_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M_Med['ng/m3'], label='Traj Height (m)')
#ax.scatter(Traj_V3_17M_IQR['Traj Lon'], Traj_V3_17M_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M_IQR['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17M_Med+1)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
#ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17M_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_17D_Med['Traj Lon'], Traj_V3_17D_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D_Med['ng/m3'], label='Traj Height (m)')
#ax.scatter(Traj_V3_17D_IQR['Traj Lon'], Traj_V3_17D_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D_IQR['ng/m3'], label='Traj Height (m)')

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
#ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17D_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_17_P95['Traj Lon'], Traj_V1_17_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_P95['Traj Height (m)'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_17_P90['Traj Lon'], Traj_V1_17_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17_P90['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_17_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_17_P95['Traj Lon'], Traj_V2_17_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_P95['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V2_17_P90['Traj Lon'], Traj_V2_17_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_17_P90['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_17_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17M_P95['Traj Lon'], Traj_V3_17M_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17M_P95['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V3_17M_P90['Traj Lon'], Traj_V3_17M_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17M_P90['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17M_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_17D_P95['Traj Lon'], Traj_V3_17D_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_17D_P95['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V3_17D_P90['Traj Lon'], Traj_V3_17D_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_17D_P90['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_17D_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "l", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$')
# cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,500,1000,1500,2000,2500,3000,3500,4000], pad = 0.08, shrink=.995) # Hg0 concentration
# cb.set_label('Height (MSL)') # Hg$^0$ (ng/m$^3$)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_18_P5['Traj Lon'], Traj_V1_18_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P5['Traj Height (m)'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_18_P10['Traj Lon'], Traj_V1_18_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P10['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_18_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_18_P5['Traj Lon'], Traj_V2_18_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P5['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V2_18_P10['Traj Lon'], Traj_V2_18_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P10['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_18_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_18M_P5['Traj Lon'], Traj_V3_18M_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M_P5['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V3_18M_P10['Traj Lon'], Traj_V3_18M_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M_P10['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18M_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_18D_P5['Traj Lon'], Traj_V3_18D_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18D_P5['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V3_18D_P10['Traj Lon'], Traj_V3_18D_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D_P10['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18D_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs2 = ax.scatter(Traj_V1_18_Med['Traj Lon'], Traj_V1_18_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_Med['ng/m3'], label='Traj Height (m)')
#cs2 = ax.scatter(Traj_V1_18_IQR['Traj Lon'], Traj_V1_18_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_IQR['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_18_Med+1)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
#ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_18_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V2_18_Med['Traj Lon'], Traj_V2_18_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_Med['ng/m3'], label='Traj Height (m)')
#ax.scatter(Traj_V2_18_IQR['Traj Lon'], Traj_V2_18_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_IQR['ng/m3'], label='Traj Height (m)')

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
#ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_18_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_18M_Med['Traj Lon'], Traj_V3_18M_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M_Med['ng/m3'], label='Traj Height (m)')
#ax.scatter(Traj_V3_18M_IQR['Traj Lon'], Traj_V3_18M_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M_IQR['ng/m3'], label='Traj Height (m)')

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
#ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18M_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

ax.scatter(Traj_V3_18D_Med['Traj Lon'], Traj_V3_18D_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D_Med['ng/m3'], label='Traj Height (m)')
#ax.scatter(Traj_V3_18D_IQR['Traj Lon'], Traj_V3_18D_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D_IQR['ng/m3'], label='Traj Height (m)')

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
#ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18D_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_18_P95['Traj Lon'], Traj_V1_18_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P95['Traj Height (m)'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_18_P90['Traj Lon'], Traj_V1_18_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P90['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V1_18_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_18_P95['Traj Lon'], Traj_V2_18_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P95['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V2_18_P90['Traj Lon'], Traj_V2_18_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P90['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V2_18_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration


#ax.scatter(Traj_V3_18M_P95['Traj Lon'], Traj_V3_18M_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M_P95['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V3_18M_P90['Traj Lon'], Traj_V3_18M_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18M_P90['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18M_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_18D_P95['Traj Lon'], Traj_V3_18D_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18D_P95['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V3_18D_P90['Traj Lon'], Traj_V3_18D_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18D_P90['ng/m3'], label='Traj Height (m)')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V3_18D_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "l", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$')
# cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,500,1000,1500,2000,2500,3000,3500,4000], pad = 0.08, shrink=.995) # Hg0 concentration
# cb.set_label('Height (MSL)') # Hg$^0$ (ng/m$^3$)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (Hg0 concentration & HYSPLIT back trajectory)

fig1 = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=2, 
                       figure=fig1, 
                       width_ratios= [0.5, 0.5],
                       height_ratios=[0.5, 0.5])

#-----------------------------
# Graph 1
ax = plt.subplot(gs[0,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -25.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V4_17 = np.ma.masked_where(seaice_data_V4_17==-999,seaice_data_V4_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V4_17, lats_V4_17, seaice_data_V4_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V4_17['Traj Lon'], Traj_V4_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V4_17['IceContact_100m'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V4_17['Traj Lon'], Traj_V4_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_17['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
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
plt.title("V4 (Macquarie Island)", y=1.1, fontsize=15)
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
ax.text(-0.35, 0.5, "       CAMMPCAN (2017-18)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "a", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V4_17)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 2
ax = plt.subplot(gs[1,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -25.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V4_18 = np.ma.masked_where(seaice_data_V4_18==-999,seaice_data_V4_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V4_18, lats_V4_18, seaice_data_V4_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V4_18['Traj Lon'], Traj_V4_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V4_18['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V4_18['Traj Lon'], Traj_V4_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_18['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
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
#plt.title("V4 (2018-19)", y=1.05, fontsize=15)
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
ax.text(-0.35, 0.5, "        CAMMPCAN (2018-19)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "b", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V4_18)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 3
ax = plt.subplot(gs[0,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_PCAN = np.ma.masked_where(seaice_data_PCAN==0,seaice_data_PCAN)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_PCAN, lats_PCAN, seaice_data_PCAN, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))



#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_PCAN['Traj Lon'], Traj_PCAN['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_PCAN['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_PCAN['Traj Lon'], Traj_PCAN['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_PCAN['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')
ax.plot(np.mean(Met_PCAN_Ice['longitude']), np.mean(Met_PCAN_Ice['latitude']), transform=data_crs, color='k', marker='*')
#ax.scatter(Met_PCAN_Ice['longitude'], Met_PCAN_Ice['latitude'], transform=data_crs, color='k', marker='*', s=15.0)

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')
ax.text(Met_PCAN_Ice['longitude'][0] + 3,  Met_PCAN_Ice['latitude'][0]  - 2, 'PCAN',  transform=data_crs, horizontalalignment='right')

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
plt.title("PCAN (2017)", y=1.1, fontsize=15)
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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(-0.35, 0.5, "        PCAN (2017)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)
# Text box in upper left

props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "c", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_PCAN)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$')
# cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,500,1000,1500,2000,2500,3000,3500,4000], pad = 0.08, shrink=.995) # Hg0 concentration
# cb.set_label('Height (MSL)') # Hg$^0$ (ng/m$^3$)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN V4 & PCAN)

fig1 = plt.figure()

gs = gridspec.GridSpec(nrows=3,
                       ncols=3, 
                       figure=fig1, 
                       width_ratios= [0.5, 0.5, 0.5],
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
seaice_data_V4_17 = np.ma.masked_where(seaice_data_V4_17==-999,seaice_data_V4_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V4_17, lats_V4_17, seaice_data_V4_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,0.95,0.05), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_18_P5['Traj Lon'], Traj_V1_18_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P5['Traj Height (m)'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V4_17_P10['Traj Lon'], Traj_V4_17_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_17_P10['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
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
plt.title("V4 2017-18\n(Macquarie Island)", y=1.1, fontsize=15)
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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V4_17_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
seaice_data_V4_18 = np.ma.masked_where(seaice_data_V4_18==-999,seaice_data_V2_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V4_18, lats_V4_18, seaice_data_V4_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,0.95,0.05), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_18_P5['Traj Lon'], Traj_V2_18_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P5['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V4_18_P10['Traj Lon'], Traj_V4_18_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_18_P10['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
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
plt.title("V4 2018-19\n(Macquarie Island)", y=1.1, fontsize=15)
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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V4_18_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
seaice_data_PCAN = np.ma.masked_where(seaice_data_PCAN==-999,seaice_data_PCAN)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_PCAN, lats_PCAN, seaice_data_PCAN, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,0.95,0.05), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_18M_P5['Traj Lon'], Traj_V3_18M_P5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M_P5['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_PCAN_P10['Traj Lon'], Traj_PCAN_P10['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_PCAN_P10['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')
ax.plot(np.mean(Met_PCAN_Ice['longitude']), np.mean(Met_PCAN_Ice['latitude']), transform=data_crs, color='k', marker='*')
ax.text(Met_PCAN_Ice['longitude'][0] + 3,  Met_PCAN_Ice['latitude'][0]  - 2, 'PCAN',  transform=data_crs, horizontalalignment='right')

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
plt.title("PCAN (2017)", y=1.1, fontsize=15)
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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_PCAN_P10)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "c", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 4

ax = plt.subplot(gs[1,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V4_17 = np.ma.masked_where(seaice_data_V4_17==-999,seaice_data_V4_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V4_17, lats_V4_17, seaice_data_V4_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,0.95,0.05), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_18_Med['Traj Lon'], Traj_V1_18_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_Med['Traj Height (m)'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V4_17_IQR['Traj Lon'], Traj_V4_17_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_17_IQR['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V4_17_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "d", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 5
ax = plt.subplot(gs[1,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)
ax.set_facecolor('lightgrey')

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V4_18 = np.ma.masked_where(seaice_data_V4_18==-999,seaice_data_V4_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V4_18, lats_V4_18, seaice_data_V4_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,0.95,0.05), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_18_Med['Traj Lon'], Traj_V2_18_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_Med['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V4_18_IQR['Traj Lon'], Traj_V4_18_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_18_IQR['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V4_18_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "e", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 6
ax = plt.subplot(gs[1,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_PCAN = np.ma.masked_where(seaice_data_PCAN==-999,seaice_data_PCAN)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_PCAN, lats_PCAN, seaice_data_PCAN, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,0.95,0.05), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_18M_Med['Traj Lon'], Traj_V3_18M_Med['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M_Med['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_PCAN_IQR['Traj Lon'], Traj_PCAN_IQR['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_PCAN_IQR['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')
ax.plot(np.mean(Met_PCAN_Ice['longitude']), np.mean(Met_PCAN_Ice['latitude']), transform=data_crs, color='k', marker='*')
ax.text(Met_PCAN_Ice['longitude'][0] + 3,  Met_PCAN_Ice['latitude'][0]  - 2, 'PCAN',  transform=data_crs, horizontalalignment='right')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_PCAN_IQR)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 7
ax = plt.subplot(gs[2,0], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V4_17 = np.ma.masked_where(seaice_data_V4_17==-999,seaice_data_V4_17)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V4_17, lats_V4_17, seaice_data_V4_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,0.95,0.05), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_18_P95['Traj Lon'], Traj_V1_18_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18_P95['Traj Height (m)'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V4_17_P90['Traj Lon'], Traj_V4_17_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_17_P90['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V4_17_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 8
ax = plt.subplot(gs[2,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)
ax.set_facecolor('lightgrey')

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_V4_18 = np.ma.masked_where(seaice_data_V4_18==-999,seaice_data_V4_18)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_V4_18, lats_V4_18, seaice_data_V4_18, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,0.95,0.05), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_18_P95['Traj Lon'], Traj_V2_18_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18_P95['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_V4_18_P90['Traj Lon'], Traj_V4_18_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_18_P90['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_V4_18_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "h", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 9
ax = plt.subplot(gs[2,2], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -35.0, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()
ax.set_facecolor('lightgrey')

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_PCAN = np.ma.masked_where(seaice_data_PCAN==-999,seaice_data_PCAN)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_PCAN, lats_PCAN, seaice_data_PCAN, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# PLOT LAND
land_PCAN = np.ma.masked_where(land_PCAN==0,land_PCAN)
cmap=cmocean.cm.ice_r
ax.pcolormesh(lons_PCAN, lats_PCAN, land_PCAN,transform=data_crs,cmap=cmap)

#cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.viridis
#cmap = plt.cm.autumn_r

#norm = BoundaryNorm(np.arange(0,4200,200), cmap.N) # Traj altitude (m)
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,.95,0.05), cmap.N) # Hg0 concentration


#ax.scatter(Traj_V3_18M_P95['Traj Lon'], Traj_V3_18M_P95['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M_P95['Traj Height (m)'], label='Traj Height (m)')
ax.scatter(Traj_PCAN_P90['Traj Lon'], Traj_PCAN_P90['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_PCAN_P90['ng/m3'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
#ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
#ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
#ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
#ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
#ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')
ax.plot(np.mean(Met_PCAN_Ice['longitude']), np.mean(Met_PCAN_Ice['latitude']), transform=data_crs, color='k', marker='*')
ax.text(Met_PCAN_Ice['longitude'][0] + 3,  Met_PCAN_Ice['latitude'][0]  - 2, 'PCAN',  transform=data_crs, horizontalalignment='right')

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
ax.text(0.04, 0.125, "n: " +str("%6.0f"%(N_PCAN_P90)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.04, 0.955, "i", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$')
# cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,500,1000,1500,2000,2500,3000,3500,4000], pad = 0.08, shrink=.995) # Hg0 concentration
# cb.set_label('Height (MSL)') # Hg$^0$ (ng/m$^3$)


#------------------------------------------------------------------------------
# PLOT PIE CHART OF AIR MASSES FOR EACH STATION
fig = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=4, 
                       figure=fig, 
                       width_ratios= [0.25, 0.25, 0.25, 0.25],
                       height_ratios=[0.5, 0.5])

#-----------------------------
# Graph 1 (V1 2017-18)
ax1 = plt.subplot(gs[0,0])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental'#, 'Oceanic'
sizes = [N_V1_17SI, N_V1_17L]#, N_V1_18O]
colors = ['red','springgreen']#,'deepskyblue']
explode = (0.1, 0)#, 0.1)  # make sea ice and oceanic air masses stand out

ax1.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('V1 (Davis)', fontsize=15, y=1.1)

#-----------------------------
# Graph 2 (V2 2017-18)
ax2 = plt.subplot(gs[0,1])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V2_17SI, N_V2_17L, N_V2_17O]
colors = ['red','springgreen','deepskyblue']
explode = (0.1, 0, 0.1)  # make sea ice and oceanic air masses stand out

ax2.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('V2 (Casey)', fontsize=15, y=1.1)

#-----------------------------
# Graph 3 (V3 Mawson 2017-18)
ax3 = plt.subplot(gs[0,2])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V3_17MSI, N_V3_17ML, N_V3_17MO]
colors = ['red','springgreen','deepskyblue']
explode = (0.1, 0, 0.1)  # make sea ice and oceanic air masses stand out

w,l,p = ax3.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.25, shadow=False, startangle=270)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

pctdists = [1.6, 0.8, 0.8]

for t,d in zip(p, pctdists):
    xi,yi = t.get_position()
    ri = np.sqrt(xi**2+yi**2)
    phi = np.arctan2(yi,xi)
    x = d*ri*np.cos(phi)
    y = d*ri*np.sin(phi)
    t.set_position((x,y))
    
plt.title('V3 (Mawson)', fontsize=15, y=1.1)

#-----------------------------
# Graph 4 (V3 Davis 2017-18)
ax4 = plt.subplot(gs[0,3])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V3_17DSI, N_V3_17DL, N_V3_17DO]
colors = ['red','springgreen','deepskyblue']
explode = (0.1, 0, 0.1)  # make sea ice and oceanic air masses stand out

ax4.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('V3 (Davis)', fontsize=15, y=1.1)

#-----------------------------
# Graph 5 (V1 2018-19)
ax5 = plt.subplot(gs[1,0])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental'#, 'Oceanic'
sizes = [N_V1_18SI, N_V1_18L]#, N_V1_18O]
colors = ['red','springgreen']#,'deepskyblue']
explode = (0.1, 0)#, 0.1)  # make sea ice and oceanic air masses stand out

ax5.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.title('V1 (Davis)', fontsize=15, y=1.1)

#-----------------------------
# Graph 6 (V2 2018-19)
ax6 = plt.subplot(gs[1,1])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V2_18SI, N_V2_18L, N_V2_18O]
colors = ['red','springgreen','deepskyblue']
explode = (0.1, 0, 0.1)  # make sea ice and oceanic air masses stand out

ax6.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax6.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.title('V2 (Casey)', fontsize=15, y=1.1)

#-----------------------------
# Graph 7 (V3 Mawson 2018-19)
ax7 = plt.subplot(gs[1,2])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V3_18MSI, N_V3_18ML, N_V3_18MO]
colors = ['red','springgreen','deepskyblue']
explode = (0.1, 0, 0.1)  # make sea ice and oceanic air masses stand out

w,l,p = ax7.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax7.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

pctdists = [0.9, 0.8, 0.7]

for t,d in zip(p, pctdists):
    xi,yi = t.get_position()
    ri = np.sqrt(xi**2+yi**2)
    phi = np.arctan2(yi,xi)
    x = d*ri*np.cos(phi)
    y = d*ri*np.sin(phi)
    t.set_position((x,y))

#plt.title('V3 (Mawson)', fontsize=15, y=1.1)

#-----------------------------
# Graph 8 (V3 Davis 2018-19)
ax8 = plt.subplot(gs[1,3])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V3_18DSI, N_V3_18DL, N_V3_18DO]
colors = ['red','springgreen','deepskyblue']
explode = (0.1, 0, 0.1)  # make sea ice and oceanic air masses stand out

w,l,p = ax8.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax8.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

pctdists = [0.9, 0.8, 0.7]

for t,d in zip(p, pctdists):
    xi,yi = t.get_position()
    ri = np.sqrt(xi**2+yi**2)
    phi = np.arctan2(yi,xi)
    x = d*ri*np.cos(phi)
    y = d*ri*np.sin(phi)
    t.set_position((x,y))
    
#plt.title('V3 (Davis)', fontsize=15, y=1.1)
