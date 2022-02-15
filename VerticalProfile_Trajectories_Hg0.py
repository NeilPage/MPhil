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

start_V3_18Mb  = '2019020101'
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
# PLOT THE GRAPH (Hg0 concentration & HYSPLIT back trajectory)

fig1 = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=4, 
                       figure=fig1, 
                       width_ratios= [0.5, 0.5, 0.5, 0.5],
                       height_ratios=[0.5, 0.5])

#-----------------------------
# Graph 1
ax = plt.subplot(gs[0,0]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V1_17['Traj Age'], Traj_V1_17['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V1_17['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V1_17['Traj Age'][0], Traj_V1_17['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V1 (Davis)", y=1.1, fontsize=15)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "a.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "        CAMMPCAN (2017-18)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 2
ax = plt.subplot(gs[0,1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V2_17['Traj Age'], Traj_V2_17['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V2_17['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V2_17['Traj Age'][0], Traj_V2_17['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V2 (Casey)", y=1.1, fontsize=15)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "b.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 3
ax = plt.subplot(gs[0,2]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V3_17M['Traj Age'], Traj_V3_17M['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V3_17M['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V3_17M['Traj Age'][0], Traj_V3_17M['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V3 (Mawson)", y=1.1, fontsize=15)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "c.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 4
ax = plt.subplot(gs[0,3]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V3_17D['Traj Age'], Traj_V3_17D['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V3_17D['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V3_17D['Traj Age'][0], Traj_V3_17D['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V3 (Davis)", y=1.1, fontsize=15)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "d.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 5
ax = plt.subplot(gs[1,0]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V1_18['Traj Age'], Traj_V1_18['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V1_18['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V1_18['Traj Age'][0], Traj_V1_18['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
#clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "e.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "        CAMMPCAN (2018-19)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 6
ax = plt.subplot(gs[1,1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V2_18['Traj Age'], Traj_V2_18['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V2_18['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V2_18['Traj Age'][0], Traj_V2_18['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
#clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "f.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 7
ax = plt.subplot(gs[1,2]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V3_18M['Traj Age'], Traj_V3_18M['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V3_18M['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V3_18M['Traj Age'][0], Traj_V3_18M['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
#clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "g.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-----------------------------
# Graph 8
ax = plt.subplot(gs[1,3]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.5,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V3_18D['Traj Age'], Traj_V3_18D['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V3_18D['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V3_18D['Traj Age'][0], Traj_V3_18D['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
#clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "h.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# Add a colorbar for the figure
fig1.subplots_adjust(right=0.9)
cbar_ax = fig1.add_axes([0.93, 0.15, 0.025, 0.7])
#cb = fig.colorbar(cs, cax=cbar_ax, ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.08, shrink=.995) # Sea ice concentration
#cb.set_label('Sea ice cover (%)') # Sea ice concentration
cb = fig1.colorbar(cs1, cax=cbar_ax, ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0], pad = 0.08, shrink=.995) # Hg0 concentration
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
ax = plt.subplot(gs[0,0]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.1,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V4_17['Traj Age'], Traj_V4_17['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V4_17['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V4_17['Traj Age'][0], Traj_V4_17['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("V4 (Macquarie Island)", y=1.1, fontsize=15)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "a.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "        CAMMPCAN (2017-18)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 2
ax = plt.subplot(gs[1,0]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.1,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_V4_18['Traj Age'], Traj_V4_18['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_V4_18['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_V4_18['Traj Age'][0], Traj_V4_18['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# # PLOT TITLE, AXIS LABEL & LEGEND TITLE
# plt.title("V4 (Macquarie Island)", y=1.1, fontsize=15)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "b.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "        CAMMPCAN (2018-19)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 3
ax = plt.subplot(gs[0,1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.viridis
norm = BoundaryNorm(np.arange(0,1.1,0.1), cmap.N) # Hg0 concentration

cs1 = ax.scatter(Traj_PCAN['Traj Age'], Traj_PCAN['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_PCAN['ng/m3'], label='Traj Height (m)')
ax.plot(Traj_PCAN['Traj Age'][0], Traj_PCAN['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("PCAN (2017)", y=1.1, fontsize=15)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='white', alpha=0.75)
ax.text(0.025, 0.925, "c.", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# #-----------------------------
# # Graph 4
# ax = plt.subplot(gs[1,1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# # SET UP THE PLOT
# ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
# ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
# ax.coastlines()

# # PLOT THE DATA (SEA ICE CONCENTRATION) 
# seaice_data_E1_2a = np.ma.masked_where(seaice_data_E1_2a==0,seaice_data_E1_2a)
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
cb = fig2.colorbar(cs1, cax=cbar_ax, ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0], pad = 0.08, shrink=.995) # Hg0 concentration
cb.set_label('Hg$^0$ (ng/m$^3$)') # Hg$^0$ (ng/m$^3$)
