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
os.chdir("/Users/ncp532/Documents/Data/Trajectories/CAMMPCAN_1718/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'
delta_one_hour = timedelta(hours=1)

#-------------
# V1_17
#-------------
start_V1_17   = '2017111407'
end_V1_17     = '2017112307'

start_date    = datetime.strptime(start_V1_17, DATE_FORMAT)
end_date      = datetime.strptime(end_V1_17,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0010spring' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=12, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2017    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
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
start_V2_17a  = '2017122108'
end_V2_17a    = '2017122308'

start_date    = datetime.strptime(start_V2_17a, DATE_FORMAT)
end_date      = datetime.strptime(end_V2_17a,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1dec0010summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=12, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2017    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=8)) # Casey timezone is UT+8
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V2_17)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V2_17a = pd.concat(Traj)

start_V2_17b  = '2017122608'
end_V2_17b    = '2017123123'

start_date    = datetime.strptime(start_V2_17b, DATE_FORMAT)
end_date      = datetime.strptime(end_V2_17b,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1dec0010summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=12, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2017    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=8)) # Casey timezone is UT+8
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V2_17)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V2_17b = pd.concat(Traj)

start_V2_17c  = '2018010100'
end_V2_17c    = '2018010608'

start_date    = datetime.strptime(start_V2_17c, DATE_FORMAT)
end_date      = datetime.strptime(end_V2_17c,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0010summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=12, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2018    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=8)) # Casey timezone is UT+8
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
start_V3_17M  = '2018020105'
end_V3_17M    = '2018021805'

start_date    = datetime.strptime(start_V3_17M, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_17M,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0010summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=12, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2018    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=5)) # Mawson timezone is UT+5
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
start_V3_17Da = '2018012707'
end_V3_17Da   = '2018013107'

start_date    = datetime.strptime(start_V3_17Da, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_17Da,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1jan0010summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=12, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2018    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
    # Set the Hg0 concentration at the corresponding datetime as a row
    Test = file.join(Hg0_V3_17D)
    file['ng/m3'] = Test.iloc[0]['ng/m3']
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_V3_17Da = pd.concat(Traj)

start_V3_17Db = '2018021907'
end_V3_17Db   = '2018022207'

start_date    = datetime.strptime(start_V3_17Db, DATE_FORMAT)
end_date      = datetime.strptime(end_V3_17Db,   DATE_FORMAT)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1feb0010summer' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=12, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2018    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
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
    filename = 'gdas1mar0010autumn' + dateA
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_fwf(f, sep="\t", lineterminator='\r', skiprows=12, usecols=[3,4,5,6,8,9,10,11])
    file.columns = ['Traj Mon','Traj Day','Traj Hour','Traj Min','Traj Age','Traj Lat','Traj Lon','Traj Height (m)']
    file['Traj Year'] = 2018    
    # Set the datetime as the file index
    file['year']     = file['Traj Year']
    file['month']    = file['Traj Mon']
    file['day']      = file['Traj Day']
    file['hour']     = file['Traj Hour']
    file['minute']   = file['Traj Min']
    file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
    file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=11)) # Macquarie Island timezone is UT+11
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
# BACK TRAJECTORIES SIPEXII (2012)

# Set the location for the working directory
#os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/10m/")

# #-------------
# # SIPEXII
# #-------------
# start_SIPEXII = '2012092308'
# end_SIPEXII   = '2012111208'

# start_date    = datetime.strptime(start_SIPEXII, DATE_FORMAT)
# end_date      = datetime.strptime(end_SIPEXII,   DATE_FORMAT)

# # Save a list of all the file names to the variable all_filenames 
# all_filenames = []
# date = start_date
# while date <= end_date:
#     dateA = date.strftime('%Y%m%d%H')
#     filename = 'gdas1nov0010spring' + dateA + '.csv'
#     date += delta_one_hour
#     all_filenames.append(filename)

# # Set an empty array
# Traj = []

# # Loop over the files in the folder
# for f in all_filenames:
#     # Set the file name
#     file = pd.read_csv(f)
#     # Set the datetime as the file index
#     file['year']     = file['Traj Year']
#     file['month']    = file['Traj Mon']
#     file['day']      = file['Traj Day']
#     file['hour']     = file['Traj Hour']
#     file['minute']   = file['Traj Min']
#     file['DateTime'] = pd.to_datetime(file[['year', 'month', 'day', 'hour', 'minute']])
#     file.index       = (pd.to_datetime(file['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7
#     # Sum the ice contact column below 100m
#     file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
#     # Set the Hg0 concentration at the corresponding datetime as a row
#     #Test = pd.concat([file, Hg0_V3_18D], axis=1, join='inner')
#     Test = file.join(Hg0_SIPEXII)
#     file['ng/m3'] = Test.iloc[0]['ng/m3']
#     # store DataFrame in list
#     Traj.append(file)

# # Combine all the files
# Traj_SIPEXII = pd.concat(Traj)

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
# SEPERATE TRAJECTORIES INTO LAND, SEA ICE and OCEAN AIR MASSES

# #-------------------------------
# # By Weighting (Land, Ice, Ocean)
# #-------------------------------
# # SeaIce
# SeaIce1       = (Traj_V1_18['Weighted_Ice']  > Traj_V1_18['Weighted_Land'])  & (Traj_V1_18['Weighted_Ice']  > Traj_V1_18['Weighted_Ocean'])
# Traj_V1_18SI  = Traj_V1_18[SeaIce1]

# SeaIce2       = (Traj_V2_18['Weighted_Ice']  > Traj_V2_18['Weighted_Land'])  & (Traj_V2_18['Weighted_Ice']  > Traj_V2_18['Weighted_Ocean'])
# Traj_V2_18SI  = Traj_V2_18[SeaIce2]

# SeaIce3       = (Traj_V3_18M['Weighted_Ice'] > Traj_V3_18M['Weighted_Land']) & (Traj_V3_18M['Weighted_Ice'] > Traj_V3_18M['Weighted_Ocean'])
# Traj_V3_18MSI = Traj_V3_18M[SeaIce3]

# SeaIce4       = (Traj_V3_18D['Weighted_Ice'] > Traj_V3_18D['Weighted_Land']) & (Traj_V3_18D['Weighted_Ice'] > Traj_V3_18D['Weighted_Ocean'])
# Traj_V3_18DSI = Traj_V3_18D[SeaIce4]

# # Land
# Land1        = (Traj_V1_18['Weighted_Land']  > Traj_V1_18['Weighted_Ice'])  & (Traj_V1_18['Weighted_Land']  > Traj_V1_18['Weighted_Ocean'])
# Traj_V1_18L  = Traj_V1_18[Land1]

# Land2        = (Traj_V2_18['Weighted_Land']  > Traj_V2_18['Weighted_Ice'])  & (Traj_V2_18['Weighted_Land']  > Traj_V2_18['Weighted_Ocean'])
# Traj_V2_18L  = Traj_V2_18[Land2]

# Land3        = (Traj_V3_18M['Weighted_Land'] > Traj_V3_18M['Weighted_Ice']) & (Traj_V3_18M['Weighted_Land'] > Traj_V3_18M['Weighted_Ocean'])
# Traj_V3_18ML = Traj_V3_18M[Land3]

# Land4        = (Traj_V3_18D['Weighted_Land'] > Traj_V3_18D['Weighted_Ice']) & (Traj_V3_18D['Weighted_Land'] > Traj_V3_18D['Weighted_Ocean'])
# Traj_V3_18DL = Traj_V3_18D[Land4]

# # Ocean
# Ocean1       = (Traj_V1_18['Weighted_Ocean']  > Traj_V1_18['Weighted_Ice'])  & (Traj_V1_18['Weighted_Ocean']  > Traj_V1_18['Weighted_Land'])
# Traj_V1_18O  = Traj_V1_18[Ocean1]

# Ocean2       = (Traj_V2_18['Weighted_Ocean']  > Traj_V2_18['Weighted_Ice'])  & (Traj_V2_18['Weighted_Ocean']  > Traj_V2_18['Weighted_Land'])
# Traj_V2_18O  = Traj_V2_18[Ocean2]

# Ocean3       = (Traj_V3_18M['Weighted_Ocean'] > Traj_V3_18M['Weighted_Ice']) & (Traj_V3_18M['Weighted_Ocean'] > Traj_V3_18M['Weighted_Land'])
# Traj_V3_18MO = Traj_V3_18M[Ocean3]

# Ocean4       = (Traj_V3_18D['Weighted_Ocean'] > Traj_V3_18D['Weighted_Ice']) & (Traj_V3_18D['Weighted_Ocean'] > Traj_V3_18D['Weighted_Land'])
# Traj_V3_18DO = Traj_V3_18D[Ocean4]

#-------------------------------
# By Percentage time spent over (Land, Ice, Ocean)
#-------------------------------
# SeaIce
SeaIce1       = (Traj_V1_18['SeaIce_Percentage']  > Traj_V1_18['Land_Percentage'])  & (Traj_V1_18['SeaIce_Percentage']  > Traj_V1_18['Ocean_Percentage'])
Traj_V1_18SI  = Traj_V1_18[SeaIce1]

SeaIce2       = (Traj_V2_18['SeaIce_Percentage']  > Traj_V2_18['Land_Percentage'])  & (Traj_V2_18['SeaIce_Percentage']  > Traj_V2_18['Ocean_Percentage'])
Traj_V2_18SI  = Traj_V2_18[SeaIce2]

SeaIce3       = (Traj_V3_18M['SeaIce_Percentage'] > Traj_V3_18M['Land_Percentage']) & (Traj_V3_18M['SeaIce_Percentage'] > Traj_V3_18M['Ocean_Percentage'])
Traj_V3_18MSI = Traj_V3_18M[SeaIce3]

SeaIce4       = (Traj_V3_18D['SeaIce_Percentage'] > Traj_V3_18D['Land_Percentage']) & (Traj_V3_18D['SeaIce_Percentage'] > Traj_V3_18D['Ocean_Percentage'])
Traj_V3_18DSI = Traj_V3_18D[SeaIce4]

# Land
Land1        = (Traj_V1_18['Land_Percentage']  > Traj_V1_18['SeaIce_Percentage'])  & (Traj_V1_18['Land_Percentage']  > Traj_V1_18['Ocean_Percentage'])
Traj_V1_18L  = Traj_V1_18[Land1]

Land2        = (Traj_V2_18['Land_Percentage']  > Traj_V2_18['SeaIce_Percentage'])  & (Traj_V2_18['Land_Percentage']  > Traj_V2_18['Ocean_Percentage'])
Traj_V2_18L  = Traj_V2_18[Land2]

Land3        = (Traj_V3_18M['Land_Percentage'] > Traj_V3_18M['SeaIce_Percentage']) & (Traj_V3_18M['Land_Percentage'] > Traj_V3_18M['Ocean_Percentage'])
Traj_V3_18ML = Traj_V3_18M[Land3]

Land4        = (Traj_V3_18D['Land_Percentage'] > Traj_V3_18D['SeaIce_Percentage']) & (Traj_V3_18D['Land_Percentage'] > Traj_V3_18D['Ocean_Percentage'])
Traj_V3_18DL = Traj_V3_18D[Land4]

# Ocean
Ocean1       = (Traj_V1_18['Ocean_Percentage']  > Traj_V1_18['SeaIce_Percentage'])  & (Traj_V1_18['Ocean_Percentage']  > Traj_V1_18['Land_Percentage'])
Traj_V1_18O  = Traj_V1_18[Ocean1]

Ocean2       = (Traj_V2_18['Ocean_Percentage']  > Traj_V2_18['SeaIce_Percentage'])  & (Traj_V2_18['Ocean_Percentage']  > Traj_V2_18['Land_Percentage'])
Traj_V2_18O  = Traj_V2_18[Ocean2]

Ocean3       = (Traj_V3_18M['Ocean_Percentage'] > Traj_V3_18M['SeaIce_Percentage']) & (Traj_V3_18M['Ocean_Percentage'] > Traj_V3_18M['Land_Percentage'])
Traj_V3_18MO = Traj_V3_18M[Ocean3]

Ocean4       = (Traj_V3_18D['Ocean_Percentage'] > Traj_V3_18D['SeaIce_Percentage']) & (Traj_V3_18D['Ocean_Percentage'] > Traj_V3_18D['Land_Percentage'])
Traj_V3_18DO = Traj_V3_18D[Ocean4]

#------------------------------------------------------------------------------
# GET TRAJECTORIES FOR ONLY TRAJ AGE = 0

# Overall
Filter1         = Traj_V1_18['Traj Age']  == 0.0
Traj_V1_18_B    = Traj_V1_18[Filter1]

Filter1         = Traj_V2_18['Traj Age']  == 0.0
Traj_V2_18_B    = Traj_V2_18[Filter1]

Filter1         = Traj_V3_18M['Traj Age']  == 0.0
Traj_V3_18M_B   = Traj_V3_18M[Filter1]

Filter1         = Traj_V3_18D['Traj Age']  == 0.0
Traj_V3_18D_B   = Traj_V3_18D[Filter1]

# Sea Ice
Filter1         = Traj_V1_18SI['Traj Age']  == 0.0
Traj_V1_18SI_B  = Traj_V1_18SI[Filter1]

Filter1         = Traj_V2_18SI['Traj Age']  == 0.0
Traj_V2_18SI_B  = Traj_V2_18SI[Filter1]

Filter1         = Traj_V3_18MSI['Traj Age']  == 0.0
Traj_V3_18MSI_B = Traj_V3_18MSI[Filter1]

Filter1         = Traj_V3_18DSI['Traj Age']  == 0.0
Traj_V3_18DSI_B = Traj_V3_18DSI[Filter1]

# Land
Filter1         = Traj_V1_18L['Traj Age']  == 0.0
Traj_V1_18L_B   = Traj_V1_18L[Filter1]

Filter1         = Traj_V2_18L['Traj Age']  == 0.0
Traj_V2_18L_B   = Traj_V2_18L[Filter1]

Filter1         = Traj_V3_18ML['Traj Age']  == 0.0
Traj_V3_18ML_B  = Traj_V3_18ML[Filter1]

Filter1         = Traj_V3_18DL['Traj Age']  == 0.0
Traj_V3_18DL_B  = Traj_V3_18DL[Filter1]

# Ocean
Filter1         = Traj_V1_18O['Traj Age']  == 0.0
Traj_V1_18O_B   = Traj_V1_18O[Filter1]

Filter1         = Traj_V2_18O['Traj Age']  == 0.0
Traj_V2_18O_B   = Traj_V2_18O[Filter1]

Filter1         = Traj_V3_18MO['Traj Age']  == 0.0
Traj_V3_18MO_B  = Traj_V3_18MO[Filter1]

Filter1         = Traj_V3_18DO['Traj Age']  == 0.0
Traj_V3_18DO_B  = Traj_V3_18DO[Filter1]

#------------------------------------------------------------------------------
# GET THE CAMMPCAN 2018-19 TOTALS

# Overall
All_1819    = Traj_V1_18_B.append(Traj_V2_18_B)
All_1819    = All_1819.append(Traj_V3_18M_B)
All_1819    = All_1819.append(Traj_V3_18D_B)

# Sea Ice
SeaIce_1819 = Traj_V1_18SI_B.append(Traj_V2_18SI_B)
SeaIce_1819 = SeaIce_1819.append(Traj_V3_18MSI_B)
SeaIce_1819 = SeaIce_1819.append(Traj_V3_18DSI_B)
#SeaIce_1819.to_csv('/Users/ncp532/Desktop/SeaIce_1819.csv')

# Land
Land_1819   = Traj_V1_18L_B.append(Traj_V2_18L_B)
Land_1819   = Land_1819.append(Traj_V3_18ML_B)
Land_1819   = Land_1819.append(Traj_V3_18DL_B)
#Land_1819.to_csv('/Users/ncp532/Desktop/Land_1819.csv')

# Ocean
Ocean_1819  = Traj_V1_18O_B.append(Traj_V2_18O_B)
Ocean_1819  = Ocean_1819.append(Traj_V3_18MO_B)
Ocean_1819  = Ocean_1819.append(Traj_V3_18DO_B)
#Ocean_1819.to_csv('/Users/ncp532/Desktop/Ocean_1819.csv')

#------------------------------------------------------------------------------
# COUNT THE NUMBER OF OBSERVATIONS OVERALL, SEA ICE, LAND OCEAN

# Overall
N_V1_18    = len(Traj_V1_18_B)
N_V2_18    = len(Traj_V2_18_B)
N_V3_18M   = len(Traj_V3_18M_B)
N_V3_18D   = len(Traj_V3_18D_B)

# Sea Ice
N_V1_18SI  = len(Traj_V1_18SI_B)
N_V2_18SI  = len(Traj_V2_18SI_B)
N_V3_18MSI = len(Traj_V3_18MSI_B)
N_V3_18DSI = len(Traj_V3_18DSI_B)

# Land
N_V1_18L   = len(Traj_V1_18L_B)
N_V2_18L   = len(Traj_V2_18L_B)
N_V3_18ML  = len(Traj_V3_18ML_B)
N_V3_18DL  = len(Traj_V3_18DL_B)

# Ocean
N_V1_18O   = len(Traj_V1_18O_B)
N_V2_18O   = len(Traj_V2_18O_B)
N_V3_18MO  = len(Traj_V3_18MO_B)
N_V3_18DO  = len(Traj_V3_18DO_B)

# CAMMPCAN 2018-19
N_All_1819    = len(All_1819)
N_SeaIce_1819 = len(SeaIce_1819)
N_Land_1819   = len(Land_1819)
N_Ocean_1819  = len(Ocean_1819)

#------------------------------------------------------------------------------
# CALCULATE THE MEAN HG0

# Overall
Mean_V1_18    = np.mean(Traj_V1_18_B['ng/m3'])
Mean_V2_18    = np.mean(Traj_V2_18_B['ng/m3'])
Mean_V3_18M   = np.mean(Traj_V3_18M_B['ng/m3'])
Mean_V3_18D   = np.mean(Traj_V3_18D_B['ng/m3'])

# Sea Ice
Mean_V1_18SI  = np.mean(Traj_V1_18SI_B['ng/m3'])
Mean_V2_18SI  = np.mean(Traj_V2_18SI_B['ng/m3'])
Mean_V3_18MSI = np.mean(Traj_V3_18MSI_B['ng/m3'])
Mean_V3_18DSI = np.mean(Traj_V3_18DSI_B['ng/m3'])

# Land
Mean_V1_18L   = np.mean(Traj_V1_18L_B['ng/m3'])
Mean_V2_18L   = np.mean(Traj_V2_18L_B['ng/m3'])
Mean_V3_18ML  = np.mean(Traj_V3_18ML_B['ng/m3'])
Mean_V3_18DL  = np.mean(Traj_V3_18DL_B['ng/m3'])

# Ocean
Mean_V1_18O   = np.mean(Traj_V1_18O_B['ng/m3'])
Mean_V2_18O   = np.mean(Traj_V2_18O_B['ng/m3'])
Mean_V3_18MO  = np.mean(Traj_V3_18MO_B['ng/m3'])
Mean_V3_18DO  = np.mean(Traj_V3_18DO_B['ng/m3'])

# CAMMPCAN 2018-19
Mean_All_1819    = np.mean(All_1819['ng/m3'])
Mean_SeaIce_1819 = np.mean(SeaIce_1819['ng/m3'])
Mean_Land_1819   = np.mean(Land_1819['ng/m3'])
Mean_Ocean_1819  = np.mean(Ocean_1819['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN HG0

# Overall
Median_V1_18    = np.median(Traj_V1_18_B['ng/m3'])
Median_V2_18    = np.median(Traj_V2_18_B['ng/m3'])
Median_V3_18M   = np.median(Traj_V3_18M_B['ng/m3'])
Median_V3_18D   = np.median(Traj_V3_18D_B['ng/m3'])

# Sea Ice
Median_V1_18SI  = np.median(Traj_V1_18SI_B['ng/m3'])
Median_V2_18SI  = np.median(Traj_V2_18SI_B['ng/m3'])
Median_V3_18MSI = np.median(Traj_V3_18MSI_B['ng/m3'])
Median_V3_18DSI = np.median(Traj_V3_18DSI_B['ng/m3'])

# Land
Median_V1_18L   = np.median(Traj_V1_18L_B['ng/m3'])
Median_V2_18L   = np.median(Traj_V2_18L_B['ng/m3'])
Median_V3_18ML  = np.median(Traj_V3_18ML_B['ng/m3'])
Median_V3_18DL  = np.median(Traj_V3_18DL_B['ng/m3'])

# Ocean
Median_V1_18O   = np.median(Traj_V1_18O_B['ng/m3'])
Median_V2_18O   = np.median(Traj_V2_18O_B['ng/m3'])
Median_V3_18MO  = np.median(Traj_V3_18MO_B['ng/m3'])
Median_V3_18DO  = np.median(Traj_V3_18DO_B['ng/m3'])

# CAMMPCAN 2018-19
Median_All_1819    = np.median(All_1819['ng/m3'])
Median_SeaIce_1819 = np.median(SeaIce_1819['ng/m3'])
Median_Land_1819   = np.median(Land_1819['ng/m3'])
Median_Ocean_1819  = np.median(Ocean_1819['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE ST DEV HG0

# Overall
std_V1_18    = np.std(Traj_V1_18_B['ng/m3'])
std_V2_18    = np.std(Traj_V2_18_B['ng/m3'])
std_V3_18M   = np.std(Traj_V3_18M_B['ng/m3'])
std_V3_18D   = np.std(Traj_V3_18D_B['ng/m3'])

# Sea Ice
std_V1_18SI  = np.std(Traj_V1_18SI_B['ng/m3'])
std_V2_18SI  = np.std(Traj_V2_18SI_B['ng/m3'])
std_V3_18MSI = np.std(Traj_V3_18MSI_B['ng/m3'])
std_V3_18DSI = np.std(Traj_V3_18DSI_B['ng/m3'])

# Land
std_V1_18L   = np.std(Traj_V1_18L_B['ng/m3'])
std_V2_18L   = np.std(Traj_V2_18L_B['ng/m3'])
std_V3_18ML  = np.std(Traj_V3_18ML_B['ng/m3'])
std_V3_18DL  = np.std(Traj_V3_18DL_B['ng/m3'])

# Ocean
std_V1_18O   = np.std(Traj_V1_18O_B['ng/m3'])
std_V2_18O   = np.std(Traj_V2_18O_B['ng/m3'])
std_V3_18MO  = np.std(Traj_V3_18MO_B['ng/m3'])
std_V3_18DO  = np.std(Traj_V3_18DO_B['ng/m3'])

# CAMMPCAN 2018-19
std_All_1819    = np.std(All_1819['ng/m3'])
std_SeaIce_1819 = np.std(SeaIce_1819['ng/m3'])
std_Land_1819   = np.std(Land_1819['ng/m3'])
std_Ocean_1819  = np.std(Ocean_1819['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MAD HG0

# Overall
MAD_V1_18    = stats.median_absolute_deviation(Traj_V1_18_B['ng/m3'])
MAD_V2_18    = stats.median_absolute_deviation(Traj_V2_18_B['ng/m3'])
MAD_V3_18M   = stats.median_absolute_deviation(Traj_V3_18M_B['ng/m3'])
MAD_V3_18D   = stats.median_absolute_deviation(Traj_V3_18D_B['ng/m3'])

# Sea Ice
MAD_V1_18SI  = stats.median_absolute_deviation(Traj_V1_18SI_B['ng/m3'])
MAD_V2_18SI  = stats.median_absolute_deviation(Traj_V2_18SI_B['ng/m3'])
MAD_V3_18MSI = stats.median_absolute_deviation(Traj_V3_18MSI_B['ng/m3'])
MAD_V3_18DSI = stats.median_absolute_deviation(Traj_V3_18DSI_B['ng/m3'])

# Land
MAD_V1_18L   = stats.median_absolute_deviation(Traj_V1_18L_B['ng/m3'])
MAD_V2_18L   = stats.median_absolute_deviation(Traj_V2_18L_B['ng/m3'])
MAD_V3_18ML  = stats.median_absolute_deviation(Traj_V3_18ML_B['ng/m3'])
MAD_V3_18DL  = stats.median_absolute_deviation(Traj_V3_18DL_B['ng/m3'])

# Ocean
MAD_V1_18O   = stats.median_absolute_deviation(Traj_V1_18O_B['ng/m3'])
MAD_V2_18O   = stats.median_absolute_deviation(Traj_V2_18O_B['ng/m3'])
MAD_V3_18MO  = stats.median_absolute_deviation(Traj_V3_18MO_B['ng/m3'])
MAD_V3_18DO  = stats.median_absolute_deviation(Traj_V3_18DO_B['ng/m3'])

# CAMMPCAN 2018-19
MAD_All_1819    = stats.median_absolute_deviation(All_1819['ng/m3'])
MAD_SeaIce_1819 = stats.median_absolute_deviation(SeaIce_1819['ng/m3'])
MAD_Land_1819   = stats.median_absolute_deviation(Land_1819['ng/m3'])
MAD_Ocean_1819  = stats.median_absolute_deviation(Ocean_1819['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MIN HG0

# Overall
Min_V1_18    = np.min(Traj_V1_18_B['ng/m3'])
Min_V2_18    = np.min(Traj_V2_18_B['ng/m3'])
Min_V3_18M   = np.min(Traj_V3_18M_B['ng/m3'])
Min_V3_18D   = np.min(Traj_V3_18D_B['ng/m3'])

# Sea Ice
Min_V1_18SI  = np.min(Traj_V1_18SI_B['ng/m3'])
Min_V2_18SI  = np.min(Traj_V2_18SI_B['ng/m3'])
Min_V3_18MSI = np.min(Traj_V3_18MSI_B['ng/m3'])
Min_V3_18DSI = np.min(Traj_V3_18DSI_B['ng/m3'])

# Land
Min_V1_18L   = np.min(Traj_V1_18L_B['ng/m3'])
Min_V2_18L   = np.min(Traj_V2_18L_B['ng/m3'])
Min_V3_18ML  = np.min(Traj_V3_18ML_B['ng/m3'])
Min_V3_18DL  = np.min(Traj_V3_18DL_B['ng/m3'])

# Ocean
Min_V1_18O   = np.min(Traj_V1_18O_B['ng/m3'])
Min_V2_18O   = np.min(Traj_V2_18O_B['ng/m3'])
Min_V3_18MO  = np.min(Traj_V3_18MO_B['ng/m3'])
Min_V3_18DO  = np.min(Traj_V3_18DO_B['ng/m3'])

# CAMMPCAN 2018-19
Min_All_1819    = np.min(All_1819['ng/m3'])
Min_SeaIce_1819 = np.min(SeaIce_1819['ng/m3'])
Min_Land_1819   = np.min(Land_1819['ng/m3'])
Min_Ocean_1819  = np.min(Ocean_1819['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MAX HG0

# Overall
Max_V1_18    = np.max(Traj_V1_18_B['ng/m3'])
Max_V2_18    = np.max(Traj_V2_18_B['ng/m3'])
Max_V3_18M   = np.max(Traj_V3_18M_B['ng/m3'])
Max_V3_18D   = np.max(Traj_V3_18D_B['ng/m3'])

# Sea Ice
Max_V1_18SI  = np.max(Traj_V1_18SI_B['ng/m3'])
Max_V2_18SI  = np.max(Traj_V2_18SI_B['ng/m3'])
Max_V3_18MSI = np.max(Traj_V3_18MSI_B['ng/m3'])
Max_V3_18DSI = np.max(Traj_V3_18DSI_B['ng/m3'])

# Land
Max_V1_18L   = np.max(Traj_V1_18L_B['ng/m3'])
Max_V2_18L   = np.max(Traj_V2_18L_B['ng/m3'])
Max_V3_18ML  = np.max(Traj_V3_18ML_B['ng/m3'])
Max_V3_18DL  = np.max(Traj_V3_18DL_B['ng/m3'])

# Ocean
Max_V1_18O   = np.max(Traj_V1_18O_B['ng/m3'])
Max_V2_18O   = np.max(Traj_V2_18O_B['ng/m3'])
Max_V3_18MO  = np.max(Traj_V3_18MO_B['ng/m3'])
Max_V3_18DO  = np.max(Traj_V3_18DO_B['ng/m3'])

# CAMMPCAN 2018-19
Max_All_1819    = np.max(All_1819['ng/m3'])
Max_SeaIce_1819 = np.max(SeaIce_1819['ng/m3'])
Max_Land_1819   = np.max(Land_1819['ng/m3'])
Max_Ocean_1819  = np.max(Ocean_1819['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE 5th PERCENTILE HG0

# Overall
P5_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    5)
P5_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    5)
P5_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   5)
P5_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   5)

# Sea Ice
P5_V1_18SI  = np.percentile(Traj_V1_18SI_B['ng/m3'],  5)
P5_V2_18SI  = np.percentile(Traj_V2_18SI_B['ng/m3'],  5)
P5_V3_18MSI = np.percentile(Traj_V3_18MSI_B['ng/m3'], 5)
P5_V3_18DSI = np.percentile(Traj_V3_18DSI_B['ng/m3'], 5)

# Land
P5_V1_18L   = np.percentile(Traj_V1_18L_B['ng/m3'],   5)
P5_V2_18L   = np.percentile(Traj_V2_18L_B['ng/m3'],   5)
P5_V3_18ML  = np.percentile(Traj_V3_18ML_B['ng/m3'],  5)
P5_V3_18DL  = np.percentile(Traj_V3_18DL_B['ng/m3'],  5)

# Ocean
P5_V1_18O   = np.nan #np.percentile(Traj_V1_18O_B['ng/m3'],   5)
P5_V2_18O   = np.percentile(Traj_V2_18O_B['ng/m3'],   5)
P5_V3_18MO  = np.percentile(Traj_V3_18MO_B['ng/m3'],  5)
P5_V3_18DO  = np.percentile(Traj_V3_18DO_B['ng/m3'],  5)

# CAMMPCAN 2018-19
P5_All_1819    = np.percentile(All_1819['ng/m3'],    5)
P5_SeaIce_1819 = np.percentile(SeaIce_1819['ng/m3'], 5)
P5_Land_1819   = np.percentile(Land_1819['ng/m3'],   5)
P5_Ocean_1819  = np.percentile(Ocean_1819['ng/m3'],  5)

#------------------------------------------------------------------------------
# CALCULATE THE 25th PERCENTILE HG0

# Overall
P25_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    25)
P25_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    25)
P25_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   25)
P25_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   25)

# Sea Ice
P25_V1_18SI  = np.percentile(Traj_V1_18SI_B['ng/m3'],  25)
P25_V2_18SI  = np.percentile(Traj_V2_18SI_B['ng/m3'],  25)
P25_V3_18MSI = np.percentile(Traj_V3_18MSI_B['ng/m3'], 25)
P25_V3_18DSI = np.percentile(Traj_V3_18DSI_B['ng/m3'], 25)

# Land
P25_V1_18L   = np.percentile(Traj_V1_18L_B['ng/m3'],   25)
P25_V2_18L   = np.percentile(Traj_V2_18L_B['ng/m3'],   25)
P25_V3_18ML  = np.percentile(Traj_V3_18ML_B['ng/m3'],  25)
P25_V3_18DL  = np.percentile(Traj_V3_18DL_B['ng/m3'],  25)

# Ocean
P25_V1_18O   = np.nan #np.percentile(Traj_V1_18O_B['ng/m3'],   25)
P25_V2_18O   = np.percentile(Traj_V2_18O_B['ng/m3'],   25)
P25_V3_18MO  = np.percentile(Traj_V3_18MO_B['ng/m3'],  25)
P25_V3_18DO  = np.percentile(Traj_V3_18DO_B['ng/m3'],  25)

# CAMMPCAN 2018-19
P25_All_1819    = np.percentile(All_1819['ng/m3'],    25)
P25_SeaIce_1819 = np.percentile(SeaIce_1819['ng/m3'], 25)
P25_Land_1819   = np.percentile(Land_1819['ng/m3'],   25)
P25_Ocean_1819  = np.percentile(Ocean_1819['ng/m3'],  25)

#------------------------------------------------------------------------------
# CALCULATE THE 75th PERCENTILE HG0

# Overall
P75_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    75)
P75_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    75)
P75_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   75)
P75_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   75)

# Sea Ice
P75_V1_18SI  = np.percentile(Traj_V1_18SI_B['ng/m3'],  75)
P75_V2_18SI  = np.percentile(Traj_V2_18SI_B['ng/m3'],  75)
P75_V3_18MSI = np.percentile(Traj_V3_18MSI_B['ng/m3'], 75)
P75_V3_18DSI = np.percentile(Traj_V3_18DSI_B['ng/m3'], 75)

# Land
P75_V1_18L   = np.percentile(Traj_V1_18L_B['ng/m3'],   75)
P75_V2_18L   = np.percentile(Traj_V2_18L_B['ng/m3'],   75)
P75_V3_18ML  = np.percentile(Traj_V3_18ML_B['ng/m3'],  75)
P75_V3_18DL  = np.percentile(Traj_V3_18DL_B['ng/m3'],  75)

# Ocean
P75_V1_18O   = np.nan #np.percentile(Traj_V1_18O_B['ng/m3'],   75)
P75_V2_18O   = np.percentile(Traj_V2_18O_B['ng/m3'],   75)
P75_V3_18MO  = np.percentile(Traj_V3_18MO_B['ng/m3'],  75)
P75_V3_18DO  = np.percentile(Traj_V3_18DO_B['ng/m3'],  75)

# CAMMPCAN 2018-19
P75_All_1819    = np.percentile(All_1819['ng/m3'],    75)
P75_SeaIce_1819 = np.percentile(SeaIce_1819['ng/m3'], 75)
P75_Land_1819   = np.percentile(Land_1819['ng/m3'],   75)
P75_Ocean_1819  = np.percentile(Ocean_1819['ng/m3'],  75)

#------------------------------------------------------------------------------
# CALCULATE THE 95th PERCENTILE HG0

# Overall
P95_V1_18    = np.percentile(Traj_V1_18_B['ng/m3'],    95)
P95_V2_18    = np.percentile(Traj_V2_18_B['ng/m3'],    95)
P95_V3_18M   = np.percentile(Traj_V3_18M_B['ng/m3'],   95)
P95_V3_18D   = np.percentile(Traj_V3_18D_B['ng/m3'],   95)

# Sea Ice
P95_V1_18SI  = np.percentile(Traj_V1_18SI_B['ng/m3'],  95)
P95_V2_18SI  = np.percentile(Traj_V2_18SI_B['ng/m3'],  95)
P95_V3_18MSI = np.percentile(Traj_V3_18MSI_B['ng/m3'], 95)
P95_V3_18DSI = np.percentile(Traj_V3_18DSI_B['ng/m3'], 95)

# Land
P95_V1_18L   = np.percentile(Traj_V1_18L_B['ng/m3'],   95)
P95_V2_18L   = np.percentile(Traj_V2_18L_B['ng/m3'],   95)
P95_V3_18ML  = np.percentile(Traj_V3_18ML_B['ng/m3'],  95)
P95_V3_18DL  = np.percentile(Traj_V3_18DL_B['ng/m3'],  95)

# Ocean
P95_V1_18O   = np.nan #np.percentile(Traj_V1_18O_B['ng/m3'],   95)
P95_V2_18O   = np.percentile(Traj_V2_18O_B['ng/m3'],   95)
P95_V3_18MO  = np.percentile(Traj_V3_18MO_B['ng/m3'],  95)
P95_V3_18DO  = np.percentile(Traj_V3_18DO_B['ng/m3'],  95)

# CAMMPCAN 2018-19
P95_All_1819    = np.percentile(All_1819['ng/m3'],    95)
P95_SeaIce_1819 = np.percentile(SeaIce_1819['ng/m3'], 95)
P95_Land_1819   = np.percentile(Land_1819['ng/m3'],   95)
P95_Ocean_1819  = np.percentile(Ocean_1819['ng/m3'],  95)

#------------------------------------------------------------------------------
# Welches T-Test on Hg0
 
#----------------------
# T-test for the means of 2 indpendent populations
# (Note: unequal sample sizes and/or variance, therefore Welches t-test)
#----------------------

# Land & Sea Ice
WTstat_V1_18_L_SI,  WTpval_V1_18_L_SI  = stats.ttest_ind(Traj_V1_18L_B['ng/m3'],   Traj_V1_18SI_B['ng/m3'],  equal_var = False, nan_policy='omit')
WTstat_V2_18_L_SI,  WTpval_V2_18_L_SI  = stats.ttest_ind(Traj_V2_18L_B['ng/m3'],   Traj_V2_18SI_B['ng/m3'],  equal_var = False, nan_policy='omit')
WTstat_V3_18M_L_SI, WTpval_V3_18M_L_SI = stats.ttest_ind(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MSI_B['ng/m3'], equal_var = False, nan_policy='omit')
WTstat_V3_18D_L_SI, WTpval_V3_18D_L_SI = stats.ttest_ind(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DSI_B['ng/m3'], equal_var = False, nan_policy='omit')
WTstat_1819_L_SI,   WTpval_1819_L_SI   = stats.ttest_ind(Land_1819['ng/m3'],       SeaIce_1819['ng/m3'],     equal_var = False, nan_policy='omit')

# Land & Ocean
WTstat_V1_18_L_O,   WTpval_V1_18_L_O   = stats.ttest_ind(Traj_V1_18L_B['ng/m3'],   Traj_V1_18O_B['ng/m3'],   equal_var = False, nan_policy='omit')
WTstat_V2_18_L_O,   WTpval_V2_18_L_O   = stats.ttest_ind(Traj_V2_18L_B['ng/m3'],   Traj_V2_18O_B['ng/m3'],   equal_var = False, nan_policy='omit')
WTstat_V3_18M_L_O,  WTpval_V3_18M_L_O  = stats.ttest_ind(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MO_B['ng/m3'],  equal_var = False, nan_policy='omit')
WTstat_V3_18D_L_O,  WTpval_V3_18D_L_O  = stats.ttest_ind(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DO_B['ng/m3'],  equal_var = False, nan_policy='omit')
WTstat_1819_L_O,    WTpval_1819_L_O    = stats.ttest_ind(Land_1819['ng/m3'],       Ocean_1819['ng/m3'],      equal_var = False, nan_policy='omit')

# Sea Ice & Ocean
WTstat_V1_18_SI_O,  WTpval_V1_18_SI_O  = stats.ttest_ind(Traj_V1_18SI_B['ng/m3'],  Traj_V1_18O_B['ng/m3'],   equal_var = False, nan_policy='omit')
WTstat_V2_18_SI_O,  WTpval_V2_18_SI_O  = stats.ttest_ind(Traj_V2_18SI_B['ng/m3'],  Traj_V2_18O_B['ng/m3'],   equal_var = False, nan_policy='omit')
WTstat_V3_18M_SI_O, WTpval_V3_18M_SI_O = stats.ttest_ind(Traj_V3_18MSI_B['ng/m3'], Traj_V3_18MO_B['ng/m3'],  equal_var = False, nan_policy='omit')
WTstat_V3_18D_SI_O, WTpval_V3_18D_SI_O = stats.ttest_ind(Traj_V3_18DSI_B['ng/m3'], Traj_V3_18DO_B['ng/m3'],  equal_var = False, nan_policy='omit')
WTstat_1819_SI_O,   WTpval_1819_SI_O   = stats.ttest_ind(SeaIce_1819['ng/m3'],     Ocean_1819['ng/m3'],      equal_var = False, nan_policy='omit')

#------------------------------------------------------------------------------
# KS-Test on BrO (Kolmogorov-Smirnov Test)

# Land & Sea Ice
KSstat_V1_18_L_SI,  KSpval_V1_18_L_SI  = stats.ks_2samp(Traj_V1_18L_B['ng/m3'],   Traj_V1_18SI_B['ng/m3'],  alternative='two-sided', mode='auto')
KSstat_V2_18_L_SI,  KSpval_V2_18_L_SI  = stats.ks_2samp(Traj_V2_18L_B['ng/m3'],   Traj_V2_18SI_B['ng/m3'],  alternative='two-sided', mode='auto')
KSstat_V3_18M_L_SI, KSpval_V3_18M_L_SI = stats.ks_2samp(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MSI_B['ng/m3'], alternative='two-sided', mode='auto')
KSstat_V3_18D_L_SI, KSpval_V3_18D_L_SI = stats.ks_2samp(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DSI_B['ng/m3'], alternative='two-sided', mode='auto')
KSstat_1819_L_SI,   KSpval_1819_L_SI   = stats.ks_2samp(Land_1819['ng/m3'],       SeaIce_1819['ng/m3'],   alternative='two-sided', mode='auto')

# Land & Ocean
KSstat_V1_18_L_O,   KSpval_V1_18_L_O   = np.nan, np.nan #stats.ks_2samp(Traj_V1_18L_B['ng/m3'],   Traj_V1_18O_B['ng/m3'],   alternative='two-sided', mode='auto')
KSstat_V2_18_L_O,   KSpval_V2_18_L_O   = stats.ks_2samp(Traj_V2_18L_B['ng/m3'],   Traj_V2_18O_B['ng/m3'],   alternative='two-sided', mode='auto')
KSstat_V3_18M_L_O,  KSpval_V3_18M_L_O  = stats.ks_2samp(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MO_B['ng/m3'],  alternative='two-sided', mode='auto')
KSstat_V3_18D_L_O,  KSpval_V3_18D_L_O  = stats.ks_2samp(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DO_B['ng/m3'],  alternative='two-sided', mode='auto')
KSstat_1819_L_O,    KSpval_1819_L_O    = stats.ks_2samp(Land_1819['ng/m3'],       Ocean_1819['ng/m3'],      alternative='two-sided', mode='auto')

# Sea Ice & Ocean
KSstat_V1_18_SI_O,  KSpval_V1_18_SI_O  = np.nan, np.nan #stats.ks_2samp(Traj_V1_18SI_B['ng/m3'],  Traj_V1_18O_B['ng/m3'],   alternative='two-sided', mode='auto')
KSstat_V2_18_SI_O,  KSpval_V2_18_SI_O  = stats.ks_2samp(Traj_V2_18SI_B['ng/m3'],  Traj_V2_18O_B['ng/m3'],   alternative='two-sided', mode='auto')
KSstat_V3_18M_SI_O, KSpval_V3_18M_SI_O = stats.ks_2samp(Traj_V3_18MSI_B['ng/m3'], Traj_V3_18MO_B['ng/m3'],  alternative='two-sided', mode='auto')
KSstat_V3_18D_SI_O, KSpval_V3_18D_SI_O = stats.ks_2samp(Traj_V3_18DSI_B['ng/m3'], Traj_V3_18DO_B['ng/m3'],  alternative='two-sided', mode='auto')
KSstat_1819_SI_O,   KSpval_1819_SI_O   = stats.ks_2samp(SeaIce_1819['ng/m3'],     Ocean_1819['ng/m3'],      alternative='two-sided', mode='auto')

#------------------------------------------------------------------------------
# MW (Mann-Whitney) U-Test on BrO

# Land & Sea Ice
MWstat_V1_18_L_SI,  MWpval_V1_18_L_SI  = stats.mannwhitneyu(Traj_V1_18L_B['ng/m3'],   Traj_V1_18SI_B['ng/m3'],  alternative='two-sided')
MWstat_V2_18_L_SI,  MWpval_V2_18_L_SI  = stats.mannwhitneyu(Traj_V2_18L_B['ng/m3'],   Traj_V2_18SI_B['ng/m3'],  alternative='two-sided')
MWstat_V3_18M_L_SI, MWpval_V3_18M_L_SI = stats.mannwhitneyu(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MSI_B['ng/m3'], alternative='two-sided')
MWstat_V3_18D_L_SI, MWpval_V3_18D_L_SI = stats.mannwhitneyu(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DSI_B['ng/m3'], alternative='two-sided')
MWstat_1819_L_SI,   MWpval_1819_L_SI   = stats.mannwhitneyu(Land_1819['ng/m3'],       SeaIce_1819['ng/m3'],     alternative='two-sided')

# Land & Ocean
MWstat_V1_18_L_O,   MWpval_V1_18_L_O   = stats.mannwhitneyu(Traj_V1_18L_B['ng/m3'],   Traj_V1_18O_B['ng/m3'],   alternative='two-sided')
MWstat_V2_18_L_O,   MWpval_V2_18_L_O   = stats.mannwhitneyu(Traj_V2_18L_B['ng/m3'],   Traj_V2_18O_B['ng/m3'],   alternative='two-sided')
MWstat_V3_18M_L_O,  MWpval_V3_18M_L_O  = stats.mannwhitneyu(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MO_B['ng/m3'],  alternative='two-sided')
MWstat_V3_18D_L_O,  MWpval_V3_18D_L_O  = stats.mannwhitneyu(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DO_B['ng/m3'],  alternative='two-sided')
MWstat_1819_L_O,    MWpval_1819_L_O    = stats.mannwhitneyu(Land_1819['ng/m3'],       Ocean_1819['ng/m3'],      alternative='two-sided')

# Sea Ice & Ocean
MWstat_V1_18_SI_O,  MWpval_V1_18_SI_O  = stats.mannwhitneyu(Traj_V1_18SI_B['ng/m3'],  Traj_V1_18O_B['ng/m3'],   alternative='two-sided')
MWstat_V2_18_SI_O,  MWpval_V2_18_SI_O  = stats.mannwhitneyu(Traj_V2_18SI_B['ng/m3'],  Traj_V2_18O_B['ng/m3'],   alternative='two-sided')
MWstat_V3_18M_SI_O, MWpval_V3_18M_SI_O = stats.mannwhitneyu(Traj_V3_18MSI_B['ng/m3'], Traj_V3_18MO_B['ng/m3'],  alternative='two-sided')
MWstat_V3_18D_SI_O, MWpval_V3_18D_SI_O = stats.mannwhitneyu(Traj_V3_18DSI_B['ng/m3'], Traj_V3_18DO_B['ng/m3'],  alternative='two-sided')
MWstat_1819_SI_O,   MWpval_1819_SI_O   = stats.mannwhitneyu(SeaIce_1819['ng/m3'],     Ocean_1819['ng/m3'],      alternative='two-sided')

#------------------------------------------------------------------------------
# KW (Kruskal-Wallis) H-Test on BrO

# Land & Sea Ice
KWstat_V1_18_L_SI,  KWpval_V1_18_L_SI  = stats.kruskal(Traj_V1_18L_B['ng/m3'],   Traj_V1_18SI_B['ng/m3'])
KWstat_V2_18_L_SI,  KWpval_V2_18_L_SI  = stats.kruskal(Traj_V2_18L_B['ng/m3'],   Traj_V2_18SI_B['ng/m3'])
KWstat_V3_18M_L_SI, KWpval_V3_18M_L_SI = stats.kruskal(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MSI_B['ng/m3'])
KWstat_V3_18D_L_SI, KWpval_V3_18D_L_SI = stats.kruskal(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DSI_B['ng/m3'])
KWstat_1819_L_SI,   KWpval_1819_L_SI   = stats.kruskal(Land_1819['ng/m3'],       SeaIce_1819['ng/m3'])

# Land & Ocean
KWstat_V1_18_L_O,   KWpval_V1_18_L_O   = stats.kruskal(Traj_V1_18L_B['ng/m3'],   Traj_V1_18O_B['ng/m3'])
KWstat_V2_18_L_O,   KWpval_V2_18_L_O   = stats.kruskal(Traj_V2_18L_B['ng/m3'],   Traj_V2_18O_B['ng/m3'])
KWstat_V3_18M_L_O,  KWpval_V3_18M_L_O  = stats.kruskal(Traj_V3_18ML_B['ng/m3'],  Traj_V3_18MO_B['ng/m3'])
KWstat_V3_18D_L_O,  KWpval_V3_18D_L_O  = stats.kruskal(Traj_V3_18DL_B['ng/m3'],  Traj_V3_18DO_B['ng/m3'])
KWstat_1819_L_O,    KWpval_1819_L_O    = stats.kruskal(Land_1819['ng/m3'],       Ocean_1819['ng/m3'])

# Sea Ice & Ocean
KWstat_V1_18_SI_O,  KWpval_V1_18_SI_O  = stats.kruskal(Traj_V1_18SI_B['ng/m3'],  Traj_V1_18O_B['ng/m3'])
KWstat_V2_18_SI_O,  KWpval_V2_18_SI_O  = stats.kruskal(Traj_V2_18SI_B['ng/m3'],  Traj_V2_18O_B['ng/m3'])
KWstat_V3_18M_SI_O, KWpval_V3_18M_SI_O = stats.kruskal(Traj_V3_18MSI_B['ng/m3'], Traj_V3_18MO_B['ng/m3'])
KWstat_V3_18D_SI_O, KWpval_V3_18D_SI_O = stats.kruskal(Traj_V3_18DSI_B['ng/m3'], Traj_V3_18DO_B['ng/m3'])
KWstat_1819_SI_O,   KWpval_1819_SI_O   = stats.kruskal(SeaIce_1819['ng/m3'],     Ocean_1819['ng/m3'])

#------------------------------------------------------------------------------
#BUILD DATAFRAME FOR THE STATISTICAL RESULTS (AIR MASS)

# Build a pandas dataframe (Seasonal Met)
dfHg_AirMass = {'N':      [N_All_1819,         N_SeaIce_1819,      N_Land_1819,      N_Ocean_1819,
                           N_V1_18,            N_V2_18,            N_V3_18M,         N_V3_18D,
                           N_V1_18SI,          N_V2_18SI,          N_V3_18MSI,       N_V3_18DSI,
                           N_V1_18L,           N_V2_18L,           N_V3_18ML,        N_V3_18DL,
                           N_V1_18O,           N_V2_18O,           N_V3_18MO,        N_V3_18DO],
                'Mean':   [Mean_All_1819,      Mean_SeaIce_1819,   Mean_Land_1819,   Mean_Ocean_1819,
                           Mean_V1_18,         Mean_V2_18,         Mean_V3_18M,      Mean_V3_18D,
                           Mean_V1_18SI,       Mean_V2_18SI,       Mean_V3_18MSI,    Mean_V3_18D,
                           Mean_V1_18L,        Mean_V2_18L,        Mean_V3_18ML,     Mean_V3_18D,
                           Mean_V1_18O,        Mean_V2_18O,        Mean_V3_18MO,     Mean_V3_18D],
                'StDev':  [std_All_1819,       std_SeaIce_1819,    std_Land_1819,    std_Ocean_1819,
                           std_V1_18,          std_V2_18,          std_V3_18M,       std_V3_18D,
                           std_V1_18SI,        std_V2_18SI,        std_V3_18MSI,     std_V3_18DSI,
                           std_V1_18L,         std_V2_18L,         std_V3_18ML,      std_V3_18DL,
                           std_V1_18O,         std_V2_18O,         std_V3_18MO,      std_V3_18DO],
                'Median': [   Median_All_1819, Median_SeaIce_1819, Median_Land_1819, Median_Ocean_1819,
                           Median_V1_18,       Median_V2_18,       Median_V3_18M,    Median_V3_18D,
                           Median_V1_18SI,     Median_V2_18SI,     Median_V3_18MSI,  Median_V3_18DSI,
                           Median_V1_18L,      Median_V2_18L,      Median_V3_18ML,   Median_V3_18DL,
                           Median_V1_18O,      Median_V2_18O,      Median_V3_18MO,   Median_V3_18DO],
                'MAD':    [MAD_All_1819,       MAD_SeaIce_1819,    MAD_Land_1819,    MAD_Ocean_1819,
                           MAD_V1_18,          MAD_V2_18,          MAD_V3_18M,       MAD_V3_18D,
                           MAD_V1_18SI,        MAD_V2_18SI,        MAD_V3_18MSI,     MAD_V3_18DSI,
                           MAD_V1_18L,         MAD_V2_18L,         MAD_V3_18ML,      MAD_V3_18DL,
                           MAD_V1_18O,         MAD_V2_18O,         MAD_V3_18MO,      MAD_V3_18DO],
                'P5':     [P5_All_1819,        P5_SeaIce_1819,     P5_Land_1819,     P5_Ocean_1819,
                           P5_V1_18,           P5_V2_18,           P5_V3_18M,        P5_V3_18D,
                           P5_V1_18SI,         P5_V2_18SI,         P5_V3_18MSI,      P5_V3_18DSI,
                           P5_V1_18L,          P5_V2_18L,          P5_V3_18ML,       P5_V3_18DL,
                           P5_V1_18O,          P5_V2_18O,          P5_V3_18MO,       P5_V3_18DO],
                'P25':    [P25_All_1819,       P25_SeaIce_1819,    P25_Land_1819,    P25_Ocean_1819,
                           P25_V1_18,          P25_V2_18,          P25_V3_18M,       P25_V3_18D,
                           P25_V1_18SI,        P25_V2_18SI,        P25_V3_18MSI,     P25_V3_18DSI,
                           P25_V1_18L,         P25_V2_18L,         P25_V3_18ML,      P25_V3_18DL,
                           P25_V1_18O,         P25_V2_18O,         P25_V3_18MO,      P25_V3_18DO],
                'P75':    [P75_All_1819,       P75_SeaIce_1819,    P75_Land_1819,    P75_Ocean_1819,
                           P75_V1_18,          P75_V2_18,          P75_V3_18M,       P75_V3_18D,
                           P75_V1_18SI,        P75_V2_18SI,        P75_V3_18MSI,     P75_V3_18DSI,
                           P75_V1_18L,         P75_V2_18L,         P75_V3_18ML,      P75_V3_18DL,
                           P75_V1_18O,         P75_V2_18O,         P75_V3_18MO,      P75_V3_18DO],
                'P95':    [P95_All_1819,       P95_SeaIce_1819,    P95_Land_1819,    P95_Ocean_1819,
                           P95_V1_18,          P95_V2_18,          P95_V3_18M,       P95_V3_18D,
                           P95_V1_18SI,        P95_V2_18SI,        P95_V3_18MSI,     P95_V3_18DSI,
                           P95_V1_18L,         P95_V2_18L,         P95_V3_18ML,      P95_V3_18DL,
                           P95_V1_18O,         P95_V2_18O,         P95_V3_18MO,      P95_V3_18DO]}
dfHg_AirMass = pd.DataFrame(dfHg_AirMass, columns = ['N','Mean','StDev','Median','MAD','P5','P25','P75','P95'], index = ['All_1819','SI_1819','L_1819','O_1819','V1_18_All','V2_18_All','V3_18M_All','V3_18D_All','V1_18_SI','V2_18_SI','V3_18M_SI','V3_18D_SI','V1_18_L','V2_18_L','V3_18M_L','V3_18D_L','V1_18_O','V2_18_O','V3_18M_O','V3_18D_O'])
dfHg_AirMass.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_AirMass.csv')

# Build a pandas dataframe (Hg0 variability ice vs open water)
dfHg_AirMass_Stat = {'WT_Pval':[WTpval_V1_18_L_SI, WTpval_V2_18_L_SI, WTpval_V3_18M_L_SI, WTpval_V3_18D_L_SI, WTpval_1819_L_SI,
                                WTpval_V1_18_L_O,  WTpval_V2_18_L_O,  WTpval_V3_18M_L_O,  WTpval_V3_18D_L_O,  WTpval_1819_L_O,
                                WTpval_V1_18_SI_O, WTpval_V2_18_SI_O, WTpval_V3_18M_SI_O, WTpval_V3_18D_SI_O, WTpval_1819_SI_O],
                     'KS_Pval':[WTpval_V1_18_L_SI, WTpval_V2_18_L_SI, WTpval_V3_18M_L_SI, WTpval_V3_18D_L_SI, KSpval_1819_L_SI,
                                WTpval_V1_18_L_O,  WTpval_V2_18_L_O,  WTpval_V3_18M_L_O,  WTpval_V3_18D_L_O,  KSpval_1819_L_O,
                                WTpval_V1_18_SI_O, WTpval_V2_18_SI_O, WTpval_V3_18M_SI_O, WTpval_V3_18D_SI_O, KSpval_1819_SI_O],
                     'MW_Pval':[WTpval_V1_18_L_SI, WTpval_V2_18_L_SI, WTpval_V3_18M_L_SI, WTpval_V3_18D_L_SI, MWpval_1819_L_SI,
                                WTpval_V1_18_L_O,  WTpval_V2_18_L_O,  WTpval_V3_18M_L_O,  WTpval_V3_18D_L_O,  MWpval_1819_L_O,
                                WTpval_V1_18_SI_O, WTpval_V2_18_SI_O, WTpval_V3_18M_SI_O, WTpval_V3_18D_SI_O, MWpval_1819_SI_O],
                     'KW_Pval':[WTpval_V1_18_L_SI, WTpval_V2_18_L_SI, WTpval_V3_18M_L_SI, WTpval_V3_18D_L_SI, KWpval_1819_L_SI,
                                WTpval_V1_18_L_O,  WTpval_V2_18_L_O,  WTpval_V3_18M_L_O,  WTpval_V3_18D_L_O,  KWpval_1819_L_O,
                                WTpval_V1_18_SI_O, WTpval_V2_18_SI_O, WTpval_V3_18M_SI_O, WTpval_V3_18D_SI_O, KWpval_1819_SI_O],
                     'WT_stat':[WTstat_V1_18_L_SI, WTstat_V2_18_L_SI, WTstat_V3_18M_L_SI, WTstat_V3_18D_L_SI, WTstat_1819_L_SI,
                                WTstat_V1_18_L_O,  WTstat_V2_18_L_O,  WTstat_V3_18M_L_O,  WTstat_V3_18D_L_O,  WTstat_1819_L_O,
                                WTstat_V1_18_SI_O, WTstat_V2_18_SI_O, WTstat_V3_18M_SI_O, WTstat_V3_18D_SI_O, WTstat_1819_SI_O],
                     'KS_stat':[WTstat_V1_18_L_SI, WTstat_V2_18_L_SI, WTstat_V3_18M_L_SI, WTstat_V3_18D_L_SI, KSstat_1819_L_SI,
                                WTstat_V1_18_L_O,  WTstat_V2_18_L_O,  WTstat_V3_18M_L_O,  WTstat_V3_18D_L_O,  KSstat_1819_L_O,
                                WTstat_V1_18_SI_O, WTstat_V2_18_SI_O, WTstat_V3_18M_SI_O, WTstat_V3_18D_SI_O, KSstat_1819_SI_O],
                     'MW_stat':[WTstat_V1_18_L_SI, WTstat_V2_18_L_SI, WTstat_V3_18M_L_SI, WTstat_V3_18D_L_SI, MWstat_1819_L_SI,
                                WTstat_V1_18_L_O,  WTstat_V2_18_L_O,  WTstat_V3_18M_L_O,  WTstat_V3_18D_L_O,  MWstat_1819_L_O,
                                WTstat_V1_18_SI_O, WTstat_V2_18_SI_O, WTstat_V3_18M_SI_O, WTstat_V3_18D_SI_O, MWstat_1819_SI_O],
                     'KW_stat':[WTstat_V1_18_L_SI, WTstat_V2_18_L_SI, WTstat_V3_18M_L_SI, WTstat_V3_18D_L_SI, KWstat_1819_L_SI,
                                WTstat_V1_18_L_O,  WTstat_V2_18_L_O,  WTstat_V3_18M_L_O,  WTstat_V3_18D_L_O,  KWstat_1819_L_O,
                                WTstat_V1_18_SI_O, WTstat_V2_18_SI_O, WTstat_V3_18M_SI_O, WTstat_V3_18D_SI_O, KWstat_1819_SI_O]}
dfHg_AirMass_Stat = pd.DataFrame(dfHg_AirMass_Stat, columns = ['WT_Pval','KS_Pval','MW_Pval','KW_Pval','WT_stat','KS_stat','MW_stat','KW_stat'], index = ['V1_18_L_SI','V2_18_L_SI','V3_18M_L_SI','V3_18D_L_SI','1819_L_SI','V1_18_L_O','V2_18_L_O','V3_18M_L_O','V3_18D_L_O','1819_L_O','V1_18_SI_O','V2_18_SI_O','V3_18M_SI_O','V3_18D_SI_O','1819_SI_O'])
dfHg_AirMass_Stat.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_AirMass_Stat.csv')

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
cs2 = ax.pcolormesh(lons_V1_17, lats_V1_17, seaice_data_V1_17, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
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
ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17['ng/m3'], label='Traj Height (m)')

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
ax.text(-0.35, 0.5, "        Land        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V1_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17['ng/m3'], label='Traj Height (m)')

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
ax.text(-0.35, 0.5, "        Continental        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 6
ax = plt.subplot(gs[1,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V1_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V1_17['Traj Lon'], Traj_V1_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_17['ng/m3'], label='Traj Height (m)')

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
ax.text(-0.35, 0.5, "        Ocean        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 10
ax = plt.subplot(gs[2,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
#cb = fig.colorbar(cs, cax=cbar_ax, ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.08, shrink=.995) # Sea ice concentration
#cb.set_label('Sea ice cover (%)') # Sea ice concentration
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$)') # Hg$^0$ (ng/m$^3$)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_18['Traj Lon'], Traj_V1_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18['IceContact_100m'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_18L['Traj Lon'], Traj_V1_18L['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18L['ng/m3'], label='Traj Height (m)')

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
ax.text(-0.35, 0.5, "        Continental        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V1_18L)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_18['Traj Lon'], Traj_V2_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V2_18L['Traj Lon'], Traj_V2_18L['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18L['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V2_18L)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration


#ax.scatter(Traj_V3_18M['Traj Lon'], Traj_V3_18M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18ML['Traj Lon'], Traj_V3_18ML['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18ML['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V3_18ML)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_18D['Traj Lon'], Traj_V3_18D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18D['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18DL['Traj Lon'], Traj_V3_18DL['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18DL['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V3_18DL)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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

#cs2 = ax.scatter(Traj_V1_18['Traj Lon'], Traj_V1_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18['IceContact_100m'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_18SI['Traj Lon'], Traj_V1_18SI['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18SI['ng/m3'], label='Traj Height (m)')

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
ax.text(-0.35, 0.5, "        Sea Ice        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V1_18SI)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_18['Traj Lon'], Traj_V2_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V2_18SI['Traj Lon'], Traj_V2_18SI['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18SI['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V2_18SI)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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


#ax.scatter(Traj_V3_18M['Traj Lon'], Traj_V3_18M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18MSI['Traj Lon'], Traj_V3_18MSI['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18MSI['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V3_18MSI)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_18D['Traj Lon'], Traj_V3_18D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18D['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18DSI['Traj Lon'], Traj_V3_18DSI['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18DSI['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V3_18DSI)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#cs2 = ax.scatter(Traj_V1_18['Traj Lon'], Traj_V1_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18['IceContact_100m'], label='Traj Height (m)')
cs2 = ax.scatter(Traj_V1_18O['Traj Lon'], Traj_V1_18O['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V1_18O['ng/m3'], label='Traj Height (m)')

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
ax.text(-0.35, 0.5, "        Ocean        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V1_18O)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V2_18['Traj Lon'], Traj_V2_18['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V2_18O['Traj Lon'], Traj_V2_18O['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V2_18O['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V2_18O)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration


#ax.scatter(Traj_V3_18M['Traj Lon'], Traj_V3_18M['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18M['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18MO['Traj Lon'], Traj_V3_18MO['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18MO['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V3_18MO)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

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
#norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V3_18D['Traj Lon'], Traj_V3_18D['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V3_18D['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V3_18DO['Traj Lon'], Traj_V3_18DO['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V3_18DO['ng/m3'], label='Traj Height (m)')

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
ax.text(0.025, 0.925, "n: " +str("%6.0f"%(N_V3_18DO)), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
#cb = fig.colorbar(cs, cax=cbar_ax, ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.08, shrink=.995) # Sea ice concentration
#cb.set_label('Sea ice cover (%)') # Sea ice concentration
cb = fig1.colorbar(cs2, cax=cbar_ax, ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$)') # Hg$^0$ (ng/m$^3$)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (Hg0 concentration & HYSPLIT back trajectory)

fig2 = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=2, 
                       figure=fig2, 
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
norm = BoundaryNorm(np.arange(0,1.1,0.1), cmap.N) # Hg0 concentration

#ax.scatter(Traj_V4_17['Traj Lon'], Traj_V4_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_V4_17['IceContact_100m'], label='Traj Height (m)')
ax.scatter(Traj_V4_17['Traj Lon'], Traj_V4_17['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_V4_17['ng/m3'], label='Traj Height (m)')

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
norm = BoundaryNorm(np.arange(0,1.1,0.1), cmap.N) # Hg0 concentration

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
norm = BoundaryNorm(np.arange(0,1.1,0.1), cmap.N) # Hg0 concentration

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

# #-----------------------------
# # Graph 4
# ax = plt.subplot(gs[1,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# # SET UP THE PLOT
# ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
# ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
# ax.coastlines()

# # PLOT THE DATA (SEA ICE CONCENTRATION) 
# seaice_data_E1_2a = np.ma.masked_where(seaice_data_E1_2a==-999,seaice_data_E1_2a)
# #cmap=cm.get_cmap('viridis')
# cmap=cmocean.cm.ice
# cmap.set_bad(color='lightgrey')
# cs = ax.pcolormesh(lons_E1_2a, lats_E1_2a, seaice_data_E1_2a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
# #cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

# #cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# # PLOT THE BACK TRAJECTORIES
# cmap = plt.cm.autumn_r
# #norm = BoundaryNorm(np.arange(0,90,10), cmap.N) # Sea ice contact
# norm = BoundaryNorm(np.arange(0,2,0.2), cmap.N) # Hg0 concentration

# #ax.scatter(Traj_SIPEXII['Traj Lon'], Traj_SIPEXII['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_SIPEXII['IceContact_100m'], label='Traj Height (m)')
# ax.scatter(Traj_SIPEXII['Traj Lon'], Traj_SIPEXII['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=0.3, norm=norm, c=Traj_SIPEXII['ng/m3'], label='Traj Height (m)')

# # PLOT THE AAD STATIONS (Lon, Lat)
# Davis_lon,   Davis_lat   = -68.5766, 77.9674
# Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
# Casey_lon,   Casey_lat   = -66.2818, 110.5276
# MacIsl_lon,  MacIsl_lat  = -54.2959, 158.5609
# SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# # Plot the station markers
# ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
# ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
# ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
# ax.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='*')
# #ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# # Plot the marker labels
# ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
# ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
# ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
# ax.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
# #ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# # PLOT THE MAP GRIDLINES
# gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
#                   linewidth=1, color='black', alpha=0.5, linestyle='-')
# #gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
# #gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
# gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
# gl.ylocator   = ticker.FixedLocator([-60,-90])
# gl.xformatter = LONGITUDE_FORMATTER
# gl.yformatter = LATITUDE_FORMATTER

# # PLOT TITLE, AXIS LABEL & LEGEND TITLE
# #plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
# #cb.set_label('Concentration (%)')#, rotation=90)

# # ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
# #          rotation='vertical', rotation_mode='anchor',
# #          transform=ax.transAxes)

# # ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
# #          rotation='horizontal', rotation_mode='anchor',
# #          transform=ax.transAxes)

# # adjust the axis labels and ticks
# ax.xaxis.labelpad = 30
# ax.yaxis.labelpad = 30
# ax.tick_params(labelsize=10)

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(-0.35, 0.5, "        SIPEXII (2012)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-------------------------------------
# Add a colorbar for the figure
fig2.subplots_adjust(right=0.65)
cbar_ax = fig2.add_axes([0.68, 0.15, 0.025, 0.7])
#cb = fig.colorbar(cs, cax=cbar_ax, ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.08, shrink=.995) # Sea ice concentration
#cb.set_label('Sea ice cover (%)') # Sea ice concentration
cb = fig2.colorbar(cs2, cax=cbar_ax, ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$)') # Hg$^0$ (ng/m$^3$)

#------------------------------------------------------------------------------
# PLOT HISTOGRAMS OF NORMALISED FREQUENCY Hg0

fig = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=2, 
                       figure=fig, 
                       width_ratios= [0.5, 0.5],
                       height_ratios=[0.5, 0.5])

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])

w = 0.01
n1 = math.ceil((Max_V1_18SI - Min_V1_18SI)/w)
n2 = math.ceil((Max_V1_18L  - Min_V1_18L)/w)
#n3 = math.ceil((Max_V1_18O  - Min_V1_18O)/w)

# Plot the variables
plt.hist(Traj_V1_18SI_B['ng/m3'], density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Sea ice')
plt.hist(Traj_V1_18L_B['ng/m3'],  density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='Continental')
#plt.hist(Traj_V1_18O_B['ng/m3'],  density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='Oceanic')

# Plot the mean Hg
point1 = [Traj_V1_18SI_B['ng/m3'].max(),  0]
point2 = [Traj_V1_18SI_B['ng/m3'].max(),  0.2]
point3 = [Traj_V1_18L_B['ng/m3'].max(),   0]
point4 = [Traj_V1_18L_B['ng/m3'].max(),   0.2]
# point5 = [Traj_V1_18O_B['ng/m3'].max(),   0]
# point6 = [Traj_V1_18O_B['ng/m3'].max(),   0.2]

x_SI  = [point1[0], point2[0]]
y_SI  = [point1[1], point2[1]]
x_L   = [point3[0], point4[0]]
y_L   = [point3[1], point4[1]]
# x_O   = [point5[0], point6[0]]
# y_O   = [point5[1], point6[1]]

plt.plot(x_SI, y_SI, c ='red')
plt.plot(x_L,  y_L,  c ='green')
# plt.plot(x_O,  y_O,  c ='blue')

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
legend = ax1.legend(loc='upper right', title='V1 (Davis)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[0,1])

w = 0.01
n1 = math.ceil((Max_V2_18SI - Min_V2_18SI)/w)
n2 = math.ceil((Max_V2_18L  - Min_V2_18L)/w)
n3 = math.ceil((Max_V2_18O  - Min_V2_18O)/w)

# Plot the variables
plt.hist(Traj_V2_18SI_B['ng/m3'], density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Sea ice')
plt.hist(Traj_V2_18L_B['ng/m3'],  density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='Continental')
plt.hist(Traj_V2_18O_B['ng/m3'],  density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='Oceanic')

# Plot the mean Hg
point1 = [Traj_V2_18SI_B['ng/m3'].max(),  0]
point2 = [Traj_V2_18SI_B['ng/m3'].max(),  0.2]
point3 = [Traj_V2_18L_B['ng/m3'].max(),   0]
point4 = [Traj_V2_18L_B['ng/m3'].max(),   0.2]
point5 = [Traj_V2_18O_B['ng/m3'].max(),   0]
point6 = [Traj_V2_18O_B['ng/m3'].max(),   0.2]

x_SI  = [point1[0], point2[0]]
y_SI  = [point1[1], point2[1]]
x_L   = [point3[0], point4[0]]
y_L   = [point3[1], point4[1]]
x_O   = [point5[0], point6[0]]
y_O   = [point5[1], point6[1]]

plt.plot(x_SI, y_SI, c ='red')
plt.plot(x_L,  y_L,  c ='green')
plt.plot(x_O,  y_O,  c ='blue')

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
legend = ax1.legend(loc='upper right', title='V2 (Casey)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[1,0])

w = 0.01
#n1 = math.ceil((Max_V3_18MSI - Min_V3_18MSI)/w)
n2 = math.ceil((Max_V3_18ML  - Min_V3_18ML)/w)
n3 = math.ceil((Max_V3_18MO  - Min_V3_18MO)/w)

# Plot the variables
#plt.hist(Traj_V3_18MSI_B['ng/m3'], density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Sea ice')
plt.hist(Traj_V3_18ML_B['ng/m3'],  density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='Continental')
plt.hist(Traj_V3_18MO_B['ng/m3'],  density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='Oceanic')

# Plot the mean Hg
#point1 = [Traj_V3_18MSI_B['ng/m3'].max(),  0]
#point2 = [Traj_V3_18MSI_B['ng/m3'].max(),  0.2]
point3 = [Traj_V3_18ML_B['ng/m3'].max(),   0]
point4 = [Traj_V3_18ML_B['ng/m3'].max(),   0.2]
point5 = [Traj_V3_18MO_B['ng/m3'].max(),   0]
point6 = [Traj_V3_18MO_B['ng/m3'].max(),   0.2]

#x_SI  = [point1[0], point2[0]]
#y_SI  = [point1[1], point2[1]]
x_L   = [point3[0], point4[0]]
y_L   = [point3[1], point4[1]]
x_O   = [point5[0], point6[0]]
y_O   = [point5[1], point6[1]]

plt.plot(x_SI, y_SI, c ='red')
plt.plot(x_L,  y_L,  c ='green')
plt.plot(x_O,  y_O,  c ='blue')

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
legend = ax1.legend(loc='upper right', title='V3 (Mawson)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 4
ax1 = plt.subplot(gs[1,1])

w = 0.01
n1 = math.ceil((Max_V3_18DSI - Min_V3_18DSI)/w)
n2 = math.ceil((Max_V3_18DL  - Min_V3_18DL)/w)
n3 = math.ceil((Max_V3_18DO  - Min_V3_18DO)/w)

# Plot the variables
plt.hist(Traj_V3_18DSI_B['ng/m3'], density=True, bins=n1, histtype='step', edgecolor = 'blue',  lw = 2.0, label='Sea ice')
plt.hist(Traj_V3_18DL_B['ng/m3'],  density=True, bins=n2, histtype='step', edgecolor = 'red',   lw = 2.0, label='Continental')
plt.hist(Traj_V3_18DO_B['ng/m3'],  density=True, bins=n3, histtype='step', edgecolor = 'green', lw = 2.0, label='Oceanic')

# Plot the mean Hg
point1 = [Traj_V3_18DSI_B['ng/m3'].max(),  0]
point2 = [Traj_V3_18DSI_B['ng/m3'].max(),  0.2]
point3 = [Traj_V3_18DL_B['ng/m3'].max(),   0]
point4 = [Traj_V3_18DL_B['ng/m3'].max(),   0.2]
point5 = [Traj_V3_18DO_B['ng/m3'].max(),   0]
point6 = [Traj_V3_18DO_B['ng/m3'].max(),   0.2]

x_SI  = [point1[0], point2[0]]
y_SI  = [point1[1], point2[1]]
x_L   = [point3[0], point4[0]]
y_L   = [point3[1], point4[1]]
x_O   = [point5[0], point6[0]]
y_O   = [point5[1], point6[1]]

plt.plot(x_SI, y_SI, c ='red')
plt.plot(x_L,  y_L,  c ='green')
plt.plot(x_O,  y_O,  c ='blue')

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
legend = ax1.legend(loc='upper right', title='V3 (Mawson)')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.99)

#------------------------------------------------------------------------------
# PLOT PIE CHART OF AIR MASSES FOR EACH STATION

fig = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=2, 
                       figure=fig, 
                       width_ratios= [0.5, 0.5],
                       height_ratios=[0.5, 0.5])

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental'#, 'Oceanic'
sizes = [N_V1_18SI, N_V1_18L]#, N_V1_18O]
colors = ['red','springgreen']#,'deepskyblue']
explode = (0.1, 0)#, 0.1)  # make sea ice and oceanic air masses stand out

ax1.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('V1 (Davis)', fontsize=15, y=1.1)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[0,1])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V2_18SI, N_V2_18L, N_V2_18O]
colors = ['red','springgreen','deepskyblue']
explode = (0.1, 0, 0.1)  # make sea ice and oceanic air masses stand out

ax1.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('V2 (Casey)', fontsize=15, y=1.1)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[1,0])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V3_18MSI, N_V3_18ML, N_V3_18MO]
colors = ['red','springgreen','deepskyblue']
explode = (0.4, 0, 0.1)  # make sea ice and oceanic air masses stand out

ax1.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('V3 (Mawson)', fontsize=15, y=1.1)

#-----------------------------
# Graph 4
ax1 = plt.subplot(gs[1,1])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sea Ice', 'Continental', 'Oceanic'
sizes = [N_V3_18DSI, N_V3_18DL, N_V3_18DO]
colors = ['red','springgreen','deepskyblue']
explode = (0.4, 0, 0.1)  # make sea ice and oceanic air masses stand out

ax1.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.2, shadow=False, startangle=270)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('V3 (Davis)', fontsize=15, y=1.1)
