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
Met_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V1_17_underway_60.csv', index_col=0)
Met_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V2_17_underway_60.csv', index_col=0)
Met_V3_17M  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V3_17_underway_60.csv', index_col=0)
Met_V3_17D  = Met_V3_17M
Met_V4_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V4_17_underway_60.csv', index_col=0)

Met_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V1_18_underway_60.csv', index_col=0) 
Met_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V2_18_underway_60.csv', index_col=0)
Met_V3_18M  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V3_18_underway_60.csv', index_col=0) 
Met_V3_18D  = Met_V3_18M
Met_V4_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V4_18_underway_60.csv', index_col=0)

Met_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/ShipTrack/SIPEXII_underway_60.csv', index_col=0) 
Met_PCAN    = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/ShipTrack/PCAN_underway_60.csv', index_col=0) 

#--------------
# Sea Ice
#--------------
#SI_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V1_17_BrO.csv',  index_col=0)
#SI_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V2_17_BrO.csv',  index_col=0)
SI_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv', index_col=0)
SI_V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv', index_col=0)
SI_V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V3_17M_BrO.csv', index_col=0)

#SI_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V1_18_BrO.csv',  index_col=0)
#SI_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V2_18_BrO.csv',  index_col=0)
SI_V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv', index_col=0)
SI_V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv', index_col=0)
SI_V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V3_18M_BrO.csv', index_col=0)

SI_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv', index_col=0)

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
Met_V1_17.index   = (pd.to_datetime(Met_V1_17.index,   dayfirst=True) + timedelta(hours=7))  # Davis timezone is UT+7
Met_V2_17.index   = (pd.to_datetime(Met_V2_17.index,   dayfirst=True) + timedelta(hours=8))  # Casey timezone is UT+8
Met_V3_17M.index  = (pd.to_datetime(Met_V3_17M.index,  dayfirst=True) + timedelta(hours=5))  # Mawson timezone is UT+5
Met_V3_17D.index  = (pd.to_datetime(Met_V3_17D.index,  dayfirst=True) + timedelta(hours=7))  # Davis timezone is UT+7
Met_V4_17.index   = (pd.to_datetime(Met_V4_17.index,   dayfirst=True) + timedelta(hours=11)) # Macquarie Island timezone is UT+11

Met_V1_18.index   = (pd.to_datetime(Met_V1_18.index,   dayfirst=True) + timedelta(hours=7))  # Davis timezone is UT+7
Met_V2_18.index   = (pd.to_datetime(Met_V2_18.index,   dayfirst=True) + timedelta(hours=8))  # Casey timezone is UT+8
Met_V3_18M.index  = (pd.to_datetime(Met_V3_18M.index,  dayfirst=True) + timedelta(hours=5))  # Mawson timezone is UT+5
Met_V3_18D.index  = (pd.to_datetime(Met_V3_18D.index,  dayfirst=True) + timedelta(hours=7))  # Davis timezone is UT+7
Met_V4_18.index   = (pd.to_datetime(Met_V4_18.index,   dayfirst=True) + timedelta(hours=11)) # Macquarie Island timezone is UT+11

Met_SIPEXII.index = (pd.to_datetime(Met_SIPEXII.index, dayfirst=True) + timedelta(hours=8))  # SIPEXII timezone is UT+8
Met_PCAN.index    = (pd.to_datetime(Met_PCAN.index,    dayfirst=True) + timedelta(hours=8))  # PCAN timezone is UT+8

#--------------
# Sea Ice
#--------------
SI_V1_17.index   = (pd.to_datetime(SI_V1_17.index,   dayfirst=True)) # Davis timezone is UT+7
SI_V2_17.index   = (pd.to_datetime(SI_V2_17.index,   dayfirst=True)) # Casey timezone is UT+8
SI_V3_17.index   = (pd.to_datetime(SI_V3_17.index,   dayfirst=True)) # Mawson timezone is UT+5

SI_V1_18.index   = (pd.to_datetime(SI_V1_18.index,   dayfirst=True)) # Davis timezone is UT+7
SI_V2_18.index   = (pd.to_datetime(SI_V2_18.index,   dayfirst=True)) # Casey timezone is UT+8
SI_V3_18.index   = (pd.to_datetime(SI_V3_18.index,   dayfirst=True)) # Mawson timezone is UT+5

SI_SIPEXII.index = (pd.to_datetime(SI_SIPEXII.index, dayfirst=True)) # SIPEXII timezone is UT+8

#------------------------------------------------------------------------------
# PASSIVATION ISSUE WITH CELL A ON VOYAGES V3_18M, V3_18D and V4_18 (FILTER DATA)

Filter1    = Hg0_V3_18M['Cart'] == "B"
Hg0_V3_18M = Hg0_V3_18M[Filter1]

Filter2    = Hg0_V3_18D['Cart'] == "B"
Hg0_V3_18D = Hg0_V3_18D[Filter2]

Filter3    = Hg0_V4_18['Cart'] == "B"
Hg0_V4_18  = Hg0_V4_18[Filter3]

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
# Met
Davis      = (Met_V1_17.index >= start_date) & (Met_V1_17.index < end_date)
Met_V1_17  = Met_V1_17[Davis]

#-----------------------------
# V2_17 Casey (13 Dec 2017 - 11 Jan 2018) (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018 on station)
#-----------------------------
start_date = '2017-12-13'
end_date   = '2018-01-12'
# Hg0
Casey      = (Hg0_V2_17.index >= start_date) & (Hg0_V2_17.index < end_date)
Hg0_V2_17  = Hg0_V2_17[Casey]
# Met
Casey      = (Met_V2_17.index >= start_date) & (Met_V2_17.index < end_date)
Met_V2_17  = Met_V2_17[Casey]

#-----------------------------
# V3_17 Mawson (16 Jan - 6 Mar 2018) (1-17 Feb 2018 on station)
#-----------------------------
start_date = '2018-01-16'
end_date   = '2018-03-07'
# Hg0
Mawson     = (Hg0_V3_17M.index >= start_date) & (Hg0_V3_17M.index < end_date)
Hg0_V3_17M = Hg0_V3_17M[Mawson]
# Met
Mawson     = (Met_V3_17M.index >= start_date) & (Met_V3_17M.index < end_date)
Met_V3_17M = Met_V3_17M[Mawson]

#-----------------------------
# V3_17 Davis (16 Jan - 6 Mar 2018) (27-30 Jan 2018 and 19-21 Feb 2018 on station)
#-----------------------------
start_date = '2018-01-16'
end_date   = '2018-03-07'
# Hg0
Mawson     = (Hg0_V3_17D.index >= start_date) & (Hg0_V3_17D.index < end_date)
Hg0_V3_17D = Hg0_V3_17D[Mawson]
# Met
Mawson     = (Met_V3_17D.index >= start_date) & (Met_V3_17D.index < end_date)
Met_V3_17D = Met_V3_17D[Mawson]

#-----------------------------
# V4_17 Macquarie Island (9-23 Mar 2018) (12-20 Mar 2018 on station)
#-----------------------------
start_date = '2018-03-09'
end_date   = '2018-03-24'
# Hg0
MQIsl      = (Hg0_V4_17.index >= start_date) & (Hg0_V4_17.index < end_date)
Hg0_V4_17  = Hg0_V4_17[MQIsl]
# Met
MQIsl      = (Met_V4_17.index >= start_date) & (Met_V4_17.index < end_date)
Met_V4_17  = Met_V4_17[MQIsl]

#-----------------------------
# V1_18 Davis (25 Oct - 28 Nov 2018) (7-15 Nov 2018 on station)
#-----------------------------
start_date = '2018-10-25'
end_date   = '2018-11-29'
# Hg0
Davis      = (Hg0_V1_18.index >= start_date) & (Hg0_V1_18.index < end_date)
Hg0_V1_18  = Hg0_V1_18[Davis]
# Met
Davis      = (Met_V1_18.index >= start_date) & (Met_V1_18.index < end_date)
Met_V1_18  = Met_V1_18[Davis]

#-----------------------------
# V2_18 Casey (6 Dec 2018 - 7 Jan 2019) (15-30 Dec 2018 on station)
#-----------------------------
start_date = '2018-12-06'
end_date   = '2019-01-08'
# Hg0
Casey      = (Hg0_V2_18.index >= start_date) & (Hg0_V2_18.index < end_date)
Hg0_V2_18  = Hg0_V2_18[Casey]
# Met
Casey      = (Met_V2_18.index >= start_date) & (Met_V2_18.index < end_date)
Met_V2_18  = Met_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (13 Jan - 1 Mar 2019) (30 Jan - 9 Feb 2019)
#-----------------------------
start_date = '2019-01-13'
end_date   = '2019-03-02'
# Hg0
Mawson     = (Hg0_V3_18M.index >= start_date) & (Hg0_V3_18M.index < end_date)
Hg0_V3_18M = Hg0_V3_18M[Mawson]
# Met
Mawson     = (Met_V3_18M.index >= start_date) & (Met_V3_18M.index < end_date)
Met_V3_18M = Met_V3_18M[Mawson]

#-----------------------------
# V3_18 Davis (13 Jan - 1 Mar 2019) (26-28 Jan 2019 and 19-20 Feb 2019 on station)
#-----------------------------
start_date = '2019-01-13'
end_date   = '2019-03-02'
# Hg0
Mawson     = (Hg0_V3_18D.index >= start_date) & (Hg0_V3_18D.index < end_date)
Hg0_V3_18D = Hg0_V3_18D[Mawson]
# Met
Mawson     = (Met_V3_18D.index >= start_date) & (Met_V3_18D.index < end_date)
Met_V3_18D = Met_V3_18D[Mawson]

#-----------------------------
# V4_17 Macquarie Island (5-25 Mar 2019) (8-22 Mar 2019 on station)
#-----------------------------
start_date = '2019-03-05'
end_date   = '2019-03-26'
# Hg0
MQIsl      = (Hg0_V4_18.index >= start_date) & (Hg0_V4_18.index < end_date)
Hg0_V4_18  = Hg0_V4_18[MQIsl]
# Met
MQIsl      = (Met_V4_18.index >= start_date) & (Met_V4_18.index < end_date)
Met_V4_18  = Met_V4_18[MQIsl]

#-----------------------------
# SIPEXII (14 Sep to 16 Nov 2012) (23 Sep to 11 Nov 2012 close to Antarctica)
#-----------------------------
start_date  = '2012-09-14'
end_date    = '2012-11-16'
# Hg0
SIPEX       = (Hg0_SIPEXII.index >= start_date) & (Hg0_SIPEXII.index < end_date)
Hg0_SIPEXII = Hg0_SIPEXII[SIPEX]
# Met
SIPEX       = (Met_SIPEXII.index >= start_date) & (Met_SIPEXII.index < end_date)
Met_SIPEXII = Met_SIPEXII[SIPEX]

#-----------------------------
# PCAN (14 Jan to 4 Mar 2017) (26 Jan to 24 Feb 2017 close to Antarctica)
#-----------------------------
start_date = '2017-01-14'
end_date   = '2017-02-25'
# Hg0
PCAN       = (Hg0_PCAN.index >= start_date) & (Hg0_PCAN.index < end_date)
Hg0_PCAN   = Hg0_PCAN[PCAN]
# Met
PCAN       = (Met_PCAN.index >= start_date) & (Met_PCAN.index < end_date)
Met_PCAN   = Met_PCAN[PCAN]

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
# Met
Davis           = (Met_V1_17.index >= start_date) & (Met_V1_17.index < end_date)
Met_Davis_V1_17 = Met_V1_17[Davis]

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
# Met
Casey1          = (Met_V2_17.index >= start_date1) & (Met_V2_17.index < end_date1)
Casey2          = (Met_V2_17.index >= start_date2) & (Met_V2_17.index < end_date2)
Met_Casey_1     = Met_V2_17[Casey1]
Met_Casey_2     = Met_V2_17[Casey2]
Met_Casey_V2_17 = pd.concat([Met_Casey_1,Met_Casey_2], axis =0)

#-----------------------------
# V3_17 Mawson (1-17 Feb 2018)
#-----------------------------
start_date    = '2018-02-01'
end_date      = '2018-02-18'
# Hg0
Mawson           = (Hg0_V3_17M.index >= start_date) & (Hg0_V3_17M.index < end_date)
Hg0_Mawson_V3_17 = Hg0_V3_17M[Mawson]
# Met
Mawson           = (Met_V3_17M.index >= start_date) & (Met_V3_17M.index < end_date)
Met_Mawson_V3_17 = Met_V3_17M[Mawson]

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
# Met
Davis1          = (Met_V3_17D.index >= start_date1) & (Met_V3_17D.index < end_date1)
Davis2          = (Met_V3_17D.index >= start_date2) & (Met_V3_17D.index < end_date2)
Met_Davis_1     = Met_V3_17D[Davis1]
Met_Davis_2     = Met_V3_17D[Davis2]
Met_Davis_V3_17 = pd.concat([Met_Davis_1,Met_Davis_2], axis =0)

#-----------------------------
# V4_17 Macquarie Island (9-23 Mar 2018) (12-20 Mar 2018 on station)
#-----------------------------
start_date   = '2018-03-12'
end_date     = '2018-03-21'
# Hg0
MQIsl           = (Hg0_V4_17.index >= start_date) & (Hg0_V4_17.index < end_date)
Hg0_MQIsl_V4_17 = Hg0_V4_17[MQIsl]
# Met
MQIsl           = (Met_V4_17.index >= start_date) & (Met_V4_17.index < end_date)
Met_MQIsl_V4_17 = Met_V4_17[MQIsl]

#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
#-----------------------------
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# Hg0
Davis           = (Hg0_V1_18.index >= start_date) & (Hg0_V1_18.index < end_date)
Hg0_Davis_V1_18 = Hg0_V1_18[Davis]
# Met
Davis           = (Met_V1_18.index >= start_date) & (Met_V1_18.index < end_date)
Met_Davis_V1_18 = Met_V1_18[Davis]

#-----------------------------
# V2_18 Casey (15-30 Dec 2018)
#-----------------------------
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# Hg0
Casey           = (Hg0_V2_18.index >= start_date) & (Hg0_V2_18.index < end_date)
Hg0_Casey_V2_18 = Hg0_V2_18[Casey]
# Met
Casey           = (Met_V2_18.index >= start_date) & (Met_V2_18.index < end_date)
Met_Casey_V2_18 = Met_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#-----------------------------
start_date    = '2019-01-30'
end_date      = '2019-02-10'
# Hg0
Mawson           = (Hg0_V3_18M.index >= start_date) & (Hg0_V3_18M.index < end_date)
Hg0_Mawson_V3_18 = Hg0_V3_18M[Mawson]
# Met
Mawson           = (Met_V3_18M.index >= start_date) & (Met_V3_18M.index < end_date)
Met_Mawson_V3_18 = Met_V3_18M[Mawson]

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
# Met
Davis1          = (Met_V3_18D.index >= start_date1) & (Met_V3_18D.index < end_date1)
Davis2          = (Met_V3_18D.index >= start_date2) & (Met_V3_18D.index < end_date2)
Met_Davis_1     = Met_V3_18D[Davis1]
Met_Davis_2     = Met_V3_18D[Davis2]
Met_Davis_V3_18 = pd.concat([Met_Davis_1,Met_Davis_2], axis =0)

#-----------------------------
# V4_17 Macquarie Island (5-25 Mar 2019) (8-22 Mar 2019 on station)
#-----------------------------
start_date   = '2019-03-08'
end_date     = '2019-03-23'
# Hg0
MQIsl           = (Hg0_V4_18.index >= start_date) & (Hg0_V4_18.index < end_date)
Hg0_MQIsl_V4_18 = Hg0_V4_18[MQIsl]
# Met
MQIsl           = (Met_V4_18.index >= start_date) & (Met_V4_18.index < end_date)
Met_MQIsl_V4_18 = Met_V4_18[MQIsl]

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
# Combine the datasets for Mawson and Davis during V3

# Hg0_V3
Hg0_V3_17_Ice = Hg0_Davis_V3_17.append(Hg0_Mawson_V3_17)
Hg0_V3_18_Ice = Hg0_Davis_V3_18.append(Hg0_Mawson_V3_18)

#------------------------------------------------------------------------------
# Filter the datasets for time in open water

# Hg0
Hg0_PCAN_OW     = Hg0_PCAN.merge(Hg0_PCAN_Ice,       how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_SIPEXII_OW  = Hg0_SIPEXII.merge(Hg0_SIPEXII_Ice, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V1_17_OW    = Hg0_V1_17.merge(Hg0_Davis_V1_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V2_17_OW    = Hg0_V2_17.merge(Hg0_Casey_V2_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V3_17D_OW   = Hg0_V3_17M.merge(Hg0_Mawson_V3_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17D_OW   = Hg0_V3_17D_OW.drop(['_merge'], axis=1)
Hg0_V3_17D_OW   = Hg0_V3_17D_OW.merge(Hg0_Davis_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V3_17M_OW   = Hg0_V3_17M.merge(Hg0_Mawson_V3_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17M_OW   = Hg0_V3_17M_OW.drop(['_merge'], axis=1)
Hg0_V3_17M_OW   = Hg0_V3_17M_OW.merge(Hg0_Davis_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V3_17_OW    = Hg0_V3_17M.merge(Hg0_Mawson_V3_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17_OW    = Hg0_V3_17_OW.drop(['_merge'], axis=1)
Hg0_V3_17_OW    = Hg0_V3_17_OW.merge(Hg0_Davis_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V4_17_OW    = Hg0_V4_17.merge(Hg0_MQIsl_V4_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V1_18_OW    = Hg0_V1_18.merge(Hg0_Davis_V1_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V2_18_OW    = Hg0_V2_18.merge(Hg0_Casey_V2_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V3_18D_OW   = Hg0_V3_18M.merge(Hg0_Mawson_V3_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18D_OW   = Hg0_V3_18D_OW.drop(['_merge'], axis=1)
Hg0_V3_18D_OW   = Hg0_V3_18D_OW.merge(Hg0_Davis_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V3_18M_OW   = Hg0_V3_18M.merge(Hg0_Mawson_V3_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18M_OW   = Hg0_V3_18M_OW.drop(['_merge'], axis=1)
Hg0_V3_18M_OW   = Hg0_V3_18M_OW.merge(Hg0_Davis_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V3_18_OW    = Hg0_V3_18M.merge(Hg0_Mawson_V3_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18_OW    = Hg0_V3_18_OW.drop(['_merge'], axis=1)
Hg0_V3_18_OW    = Hg0_V3_18_OW.merge(Hg0_Davis_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V4_18_OW    = Hg0_V4_18.merge(Hg0_MQIsl_V4_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

# Met
Met_PCAN_OW     = Met_PCAN.merge(Met_PCAN_Ice,       how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_SIPEXII_OW  = Met_SIPEXII.merge(Met_SIPEXII_Ice, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V1_17_OW    = Met_V1_17.merge(Met_Davis_V1_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_V2_17_OW    = Met_V2_17.merge(Met_Casey_V2_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V3_17M_OW   = Met_V3_17M.merge(Met_Mawson_V3_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_V3_17M_OW   = Met_V3_17M_OW.drop(['_merge'], axis=1)
Met_V3_17M_OW   = Met_V3_17M_OW.merge(Met_Davis_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V3_17_OW    = Met_V3_17M.merge(Met_Mawson_V3_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_V3_17_OW    = Met_V3_17_OW.drop(['_merge'], axis=1)
Met_V3_17_OW    = Met_V3_17_OW.merge(Met_Davis_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V3_17_OW    = Met_V3_17M.merge(Met_Mawson_V3_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_V3_17_OW    = Met_V3_17_OW.drop(['_merge'], axis=1)
Met_V3_17_OW    = Met_V3_17_OW.merge(Met_Davis_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V4_17_OW    = Met_V4_17.merge(Met_MQIsl_V4_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V1_18_OW    = Met_V1_18.merge(Met_Davis_V1_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_V2_18_OW    = Met_V2_18.merge(Met_Casey_V2_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V3_18D_OW   = Met_V3_18M.merge(Met_Mawson_V3_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_V3_18D_OW   = Met_V3_18D_OW.drop(['_merge'], axis=1)
Met_V3_18D_OW   = Met_V3_18D_OW.merge(Met_Davis_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V3_18M_OW   = Met_V3_18M.merge(Met_Mawson_V3_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_V3_18M_OW   = Met_V3_18M_OW.drop(['_merge'], axis=1)
Met_V3_18M_OW   = Met_V3_18M_OW.merge(Met_Davis_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V3_18_OW    = Met_V3_18M.merge(Met_Mawson_V3_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Met_V3_18_OW    = Met_V3_18_OW.drop(['_merge'], axis=1)
Met_V3_18_OW    = Met_V3_18_OW.merge(Met_Davis_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Met_V4_18_OW    = Met_V4_18.merge(Met_MQIsl_V4_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

#------------------------------------------------------------------------------
# CALCULATE THE DAILY MEAN

#--------------
# Hg0
#--------------
DMean_SIPEXII = Hg0_SIPEXII.resample('D').mean()
DMean_PCAN    = Hg0_PCAN.resample('D').mean()

DMean_V1_17   = Hg0_V1_17.resample('D').mean()
DMean_V2_17   = Hg0_V2_17.resample('D').mean()
DMean_V3_17M  = Hg0_V3_17M.resample('D').mean()
DMean_V4_17   = Hg0_V4_17.resample('D').mean()

DMean_V1_18   = Hg0_V1_18.resample('D').mean()
DMean_V2_18   = Hg0_V2_18.resample('D').mean()
DMean_V3_18M  = Hg0_V3_18M.resample('D').mean()
DMean_V4_18   = Hg0_V4_18.resample('D').mean()

#--------------
# Met
#--------------
Met_V1_17_DM   = Met_V1_17.resample('D').mean()
Met_V2_17_DM   = Met_V2_17.resample('D').mean()
Met_V3_17_DM   = Met_V3_17M.resample('D').mean()
Met_V4_17_DM   = Met_V4_17.resample('D').mean()

Met_V1_18_DM   = Met_V1_18.resample('D').mean()
Met_V2_18_DM   = Met_V2_18.resample('D').mean()
Met_V3_18_DM   = Met_V3_18M.resample('D').mean()
Met_V4_18_DM   = Met_V4_18.resample('D').mean()

Met_SIPEXII_DM = Met_SIPEXII.resample('D').mean()
Met_PCAN_DM    = Met_PCAN.resample('D').mean()

# SeaIce Daily Means
SI_V1_17_DM = SI_V1_17.resample('D').mean()
SI_V2_17_DM = SI_V2_17.resample('D').mean()
SI_V3_17_DM = SI_V3_17.resample('D').mean()

SI_V1_18_DM = SI_V1_18.resample('D').mean()
SI_V2_18_DM = SI_V2_18.resample('D').mean()
SI_V3_18_DM = SI_V3_18.resample('D').mean()

SI_SIPEXII_DM = SI_SIPEXII.resample('D').mean()

#------------------------------------------------------------------------------
# CALCULATE THE DAILY MEDIAN

DMedian_SIPEXII = Hg0_SIPEXII.resample('D').median()
DMedian_PCAN    = Hg0_PCAN.resample('D').median()

DMedian_V1_17   = Hg0_V1_17.resample('D').median()
DMedian_V2_17   = Hg0_V2_17.resample('D').median()
DMedian_V3_17M  = Hg0_V3_17M.resample('D').median()
DMedian_V4_17   = Hg0_V4_17.resample('D').median()

DMedian_V1_18   = Hg0_V1_18.resample('D').median()
DMedian_V2_18   = Hg0_V2_18.resample('D').median()
DMedian_V3_18M  = Hg0_V3_18M.resample('D').median()
DMedian_V4_18   = Hg0_V4_18.resample('D').median()

#------------------------------------------------------------------------------
# CALCULATE THE DAILY ST DEV

DSTD_SIPEXII = Hg0_SIPEXII.resample('D').std()
DSTD_PCAN    = Hg0_PCAN.resample('D').std()

DSTD_V1_17   = Hg0_V1_17.resample('D').std()
DSTD_V2_17   = Hg0_V2_17.resample('D').std()
DSTD_V3_17M  = Hg0_V3_17M.resample('D').std()
DSTD_V4_17   = Hg0_V4_17.resample('D').std()

DSTD_V1_18   = Hg0_V1_18.resample('D').std()
DSTD_V2_18   = Hg0_V2_18.resample('D').std()
DSTD_V3_18M  = Hg0_V3_18M.resample('D').std()
DSTD_V4_18   = Hg0_V4_18.resample('D').std()

#------------------------------------------------------------------------------
# CALCULATE THE DAILY 5TH PERCENTILE

D5P_SIPEXII = Hg0_SIPEXII.resample('D').quantile(q=0.05)
D5P_PCAN    = Hg0_PCAN.resample('D').quantile(q=0.05)

D5P_V1_17   = Hg0_V1_17.resample('D').quantile(q=0.05)
D5P_V2_17   = Hg0_V2_17.resample('D').quantile(q=0.05)
D5P_V3_17M  = Hg0_V3_17M.resample('D').quantile(q=0.05)
D5P_V4_17   = Hg0_V4_17.resample('D').quantile(q=0.05)

D5P_V1_18   = Hg0_V1_18.resample('D').quantile(q=0.05)
D5P_V2_18   = Hg0_V2_18.resample('D').quantile(q=0.05)
D5P_V3_18M  = Hg0_V3_18M.resample('D').quantile(q=0.05)
D5P_V4_18   = Hg0_V4_18.resample('D').quantile(q=0.05)

#------------------------------------------------------------------------------
# CALCULATE THE DAILY 25TH PERCENTILE

D25P_SIPEXII = Hg0_SIPEXII.resample('D').quantile(q=0.25)
D25P_PCAN    = Hg0_PCAN.resample('D').quantile(q=0.25)

D25P_V1_17   = Hg0_V1_17.resample('D').quantile(q=0.25)
D25P_V2_17   = Hg0_V2_17.resample('D').quantile(q=0.25)
D25P_V3_17M  = Hg0_V3_17M.resample('D').quantile(q=0.25)
D25P_V4_17   = Hg0_V4_17.resample('D').quantile(q=0.25)

D25P_V1_18   = Hg0_V1_18.resample('D').quantile(q=0.25)
D25P_V2_18   = Hg0_V2_18.resample('D').quantile(q=0.25)
D25P_V3_18M  = Hg0_V3_18M.resample('D').quantile(q=0.25)
D25P_V4_18   = Hg0_V4_18.resample('D').quantile(q=0.25)

#------------------------------------------------------------------------------
# CALCULATE THE DAILY 75TH PERCENTILE

D75P_SIPEXII = Hg0_SIPEXII.resample('D').quantile(q=0.75)
D75P_PCAN    = Hg0_PCAN.resample('D').quantile(q=0.75)

D75P_V1_17   = Hg0_V1_17.resample('D').quantile(q=0.75)
D75P_V2_17   = Hg0_V2_17.resample('D').quantile(q=0.75)
D75P_V3_17M  = Hg0_V3_17M.resample('D').quantile(q=0.75)
D75P_V4_17   = Hg0_V4_17.resample('D').quantile(q=0.75)

D75P_V1_18   = Hg0_V1_18.resample('D').quantile(q=0.75)
D75P_V2_18   = Hg0_V2_18.resample('D').quantile(q=0.75)
D75P_V3_18M  = Hg0_V3_18M.resample('D').quantile(q=0.75)
D75P_V4_18   = Hg0_V4_18.resample('D').quantile(q=0.75)

#------------------------------------------------------------------------------
# CALCULATE THE DAILY 95TH PERCENTILE

D95P_SIPEXII = Hg0_SIPEXII.resample('D').quantile(q=0.95)
D95P_PCAN    = Hg0_PCAN.resample('D').quantile(q=0.95)

D95P_V1_17   = Hg0_V1_17.resample('D').quantile(q=0.95)
D95P_V2_17   = Hg0_V2_17.resample('D').quantile(q=0.95)
D95P_V3_17M  = Hg0_V3_17M.resample('D').quantile(q=0.95)
D95P_V4_17   = Hg0_V4_17.resample('D').quantile(q=0.95)

D95P_V1_18   = Hg0_V1_18.resample('D').quantile(q=0.95)
D95P_V2_18   = Hg0_V2_18.resample('D').quantile(q=0.95)
D95P_V3_18M  = Hg0_V3_18M.resample('D').quantile(q=0.95)
D95P_V4_18   = Hg0_V4_18.resample('D').quantile(q=0.95)

#------------------------------------------------------------------------------
# CALCULATE THE DAILY MAD

# DMAD_SIPEXII = Hg0_SIPEXII['ng/m3'].resample('D').mad(axis = 1,  skipna = True)
# DMAD_PCAN    = Hg0_PCAN['ng/m3'].resample('D').mad(axis = 1,     skipna = True)

# DMAD_V1_17   = Hg0_V1_17['ng/m3'].resample('D').mad(axis = 1,  skipna = True)
# DMAD_V2_17   = Hg0_V2_17['ng/m3'].resample('D').mad(axis = 1,  skipna = True)
# DMAD_V3_17M  = Hg0_V3_17M['ng/m3'].resample('D').mad(axis = 1, skipna = True)
# DMAD_V4_17   = Hg0_V4_17['ng/m3'].resample('D').mad(axis = 1,  skipna = True)

# DMAD_V1_18   = Hg0_V1_18['ng/m3'].resample('D').mad(axis = 1,  skipna = True)
# DMAD_V2_18   = Hg0_V2_18['ng/m3'].resample('D').mad(axis = 1,  skipna = True)
# DMAD_V3_18M  = Hg0_V3_18M['ng/m3'].resample('D').mad(axis = 1, skipna = True)
# DMAD_V4_18   = Hg0_V4_18['ng/m3'].resample('D').mad(axis = 1,  skipna = True)

#------------------------------------------------------------------------------
# GET THE SEASONAL VALUES

#--------------
# Hg0
#--------------
# Whole voyage
LateSpring_All  = np.concatenate((Hg0_V1_17['ng/m3'],  Hg0_V1_18['ng/m3']), axis = None) 
EarlySummer_All = np.concatenate((Hg0_V2_17['ng/m3'],  Hg0_V2_18['ng/m3']), axis = None) 
LateSummer_All  = np.concatenate((Hg0_V3_17M['ng/m3'], Hg0_V3_18M['ng/m3']), axis = None) 
Summer_All      = np.concatenate((Hg0_V2_17['ng/m3'],  Hg0_V2_18['ng/m3'], Hg0_V3_17M['ng/m3'], Hg0_V3_18M['ng/m3']), axis = None) 
Autumn_All      = np.concatenate((Hg0_V4_17['ng/m3'],  Hg0_V4_18['ng/m3']), axis = None) 

# Over sea ice
LateSpring_SI   = np.concatenate((Hg0_Davis_V1_17['ng/m3'],  Hg0_Davis_V1_18['ng/m3']), axis = None) 
EarlySummer_SI  = np.concatenate((Hg0_Casey_V2_17['ng/m3'],  Hg0_Casey_V2_18['ng/m3']), axis = None) 
LateSummer_SI   = np.concatenate((Hg0_Mawson_V3_17['ng/m3'], Hg0_Davis_V3_17['ng/m3'], Hg0_Mawson_V3_18['ng/m3'], Hg0_Davis_V3_18['ng/m3']), axis = None) 
Summer_SI       = np.concatenate((Hg0_Casey_V2_17['ng/m3'],  Hg0_Casey_V2_18['ng/m3'], Hg0_Mawson_V3_17['ng/m3'], Hg0_Davis_V3_17['ng/m3'], Hg0_Mawson_V3_18['ng/m3'], Hg0_Davis_V3_18['ng/m3']), axis = None) 
Autumn_SI       = np.concatenate((Hg0_MQIsl_V4_17['ng/m3'],  Hg0_MQIsl_V4_18['ng/m3']), axis = None) 

# Open water
LateSpring_OW   = np.concatenate((Hg0_V1_17_OW['ng/m3'],  Hg0_V1_18_OW['ng/m3']), axis = None) 
EarlySummer_OW  = np.concatenate((Hg0_V2_17_OW['ng/m3'],  Hg0_V2_18_OW['ng/m3']), axis = None) 
LateSummer_OW   = np.concatenate((Hg0_V3_17M_OW['ng/m3'], Hg0_V3_18M_OW['ng/m3']), axis = None) 
Summer_OW       = np.concatenate((Hg0_V2_17_OW['ng/m3'],  Hg0_V2_18_OW['ng/m3'], Hg0_V3_17M_OW['ng/m3'], Hg0_V3_18M_OW['ng/m3']), axis = None) 
Autumn_OW       = np.concatenate((Hg0_V4_17_OW['ng/m3'],  Hg0_V4_18_OW['ng/m3']), axis = None) 

#--------------
# Water temperature
#--------------
# Whole voyage
LateSpring_WT_All  = np.concatenate((Met_V1_17['temp_sea_wtr_degc'],  Met_V1_18['temp_sea_wtr_degc']), axis = None) 
EarlySummer_WT_All = np.concatenate((Met_V2_17['temp_sea_wtr_degc'],  Met_V2_18['temp_sea_wtr_degc']), axis = None) 
LateSummer_WT_All  = np.concatenate((Met_V3_17M['temp_sea_wtr_degc'], Met_V3_18M['temp_sea_wtr_degc']), axis = None) 
Summer_WT_All      = np.concatenate((Met_V2_17['temp_sea_wtr_degc'],  Met_V2_18['temp_sea_wtr_degc'], Met_V3_17M['temp_sea_wtr_degc'], Met_V3_18M['temp_sea_wtr_degc']), axis = None) 
Autumn_WT_All      = np.concatenate((Met_V4_17['temp_sea_wtr_degc'],  Met_V4_18['temp_sea_wtr_degc']), axis = None) 

# Over sea ice
LateSpring_WT_SI   = np.concatenate((Met_Davis_V1_17['temp_sea_wtr_degc'],  Met_Davis_V1_18['temp_sea_wtr_degc']), axis = None) 
EarlySummer_WT_SI  = np.concatenate((Met_Casey_V2_17['temp_sea_wtr_degc'],  Met_Casey_V2_18['temp_sea_wtr_degc']), axis = None) 
LateSummer_WT_SI   = np.concatenate((Met_Mawson_V3_17['temp_sea_wtr_degc'], Met_Davis_V3_17['temp_sea_wtr_degc'], Met_Mawson_V3_18['temp_sea_wtr_degc'], Met_Davis_V3_18['temp_sea_wtr_degc']), axis = None) 
Summer_WT_SI       = np.concatenate((Met_Casey_V2_17['temp_sea_wtr_degc'],  Met_Casey_V2_18['temp_sea_wtr_degc'], Met_Mawson_V3_17['temp_sea_wtr_degc'], Met_Davis_V3_17['temp_sea_wtr_degc'], Met_Mawson_V3_18['temp_sea_wtr_degc'], Met_Davis_V3_18['temp_sea_wtr_degc']), axis = None) 
Autumn_WT_SI       = np.concatenate((Met_MQIsl_V4_17['temp_sea_wtr_degc'],  Met_MQIsl_V4_18['temp_sea_wtr_degc']), axis = None) 

# Open water
LateSpring_WT_OW   = np.concatenate((Met_V1_17_OW['temp_sea_wtr_degc'],  Met_V1_18_OW['temp_sea_wtr_degc']), axis = None) 
EarlySummer_WT_OW  = np.concatenate((Met_V2_17_OW['temp_sea_wtr_degc'],  Met_V2_18_OW['temp_sea_wtr_degc']), axis = None) 
LateSummer_WT_OW   = np.concatenate((Met_V3_17M_OW['temp_sea_wtr_degc'], Met_V3_18M_OW['temp_sea_wtr_degc']), axis = None) 
Summer_WT_OW       = np.concatenate((Met_V2_17_OW['temp_sea_wtr_degc'],  Met_V2_18_OW['temp_sea_wtr_degc'], Met_V3_17M_OW['temp_sea_wtr_degc'], Met_V3_18M_OW['temp_sea_wtr_degc']), axis = None) 
Autumn_WT_OW       = np.concatenate((Met_V4_17_OW['temp_sea_wtr_degc'],  Met_V4_18_OW['temp_sea_wtr_degc']), axis = None) 

#--------------
# Air temperature
#--------------
# Whole voyage
LateSpring_ATP_All  = np.concatenate((Met_V1_17['temp_air_port_degc'],    Met_V1_18['temp_air_port_degc']), axis = None)
LateSpring_ATS_All  = np.concatenate((Met_V1_17['temp_air_strbrd_degc'],  Met_V1_18['temp_air_strbrd_degc']), axis = None)
LateSpring_AT_All   = (LateSpring_ATP_All + LateSpring_ATS_All) / 2
EarlySummer_ATP_All = np.concatenate((Met_V2_17['temp_air_port_degc'],    Met_V2_18['temp_air_port_degc']), axis = None)
EarlySummer_ATS_All = np.concatenate((Met_V2_17['temp_air_strbrd_degc'],  Met_V2_18['temp_air_strbrd_degc']), axis = None)
EarlySummer_AT_All  = (EarlySummer_ATP_All + EarlySummer_ATS_All) / 2
LateSummer_ATP_All  = np.concatenate((Met_V3_17M['temp_air_port_degc'],   Met_V3_18M['temp_air_port_degc']), axis = None)
LateSummer_ATS_All  = np.concatenate((Met_V3_17M['temp_air_strbrd_degc'], Met_V3_18M['temp_air_strbrd_degc']), axis = None)
LateSummer_AT_All   = (LateSummer_ATP_All + LateSummer_ATS_All) / 2
Summer_ATP_All      = np.concatenate((Met_V2_17['temp_air_port_degc'],    Met_V2_18['temp_air_port_degc'],   Met_V3_17M['temp_air_port_degc'],   Met_V3_18M['temp_air_port_degc']), axis = None)
Summer_ATS_All      = np.concatenate((Met_V2_17['temp_air_strbrd_degc'],  Met_V2_18['temp_air_strbrd_degc'], Met_V3_17M['temp_air_strbrd_degc'], Met_V3_18M['temp_air_strbrd_degc']), axis = None)
Summer_AT_All       = (Summer_ATP_All + Summer_ATS_All) / 2
Autumn_ATP_All      = np.concatenate((Met_V4_17['temp_air_port_degc'],    Met_V4_18['temp_air_port_degc']), axis = None)
Autumn_ATS_All      = np.concatenate((Met_V4_17['temp_air_strbrd_degc'],  Met_V4_18['temp_air_strbrd_degc']), axis = None)
Autumn_AT_All       = (Autumn_ATP_All + Autumn_ATS_All) / 2

# Over sea ice
LateSpring_ATP_SI   = np.concatenate((Met_Davis_V1_17['temp_air_port_degc'],    Met_Davis_V1_18['temp_air_port_degc']), axis = None)
LateSpring_ATS_SI   = np.concatenate((Met_Davis_V1_17['temp_air_strbrd_degc'],  Met_Davis_V1_18['temp_air_strbrd_degc']), axis = None)
LateSpring_AT_SI    = (LateSpring_ATP_SI + LateSpring_ATS_SI) / 2
EarlySummer_ATP_SI  = np.concatenate((Met_Casey_V2_17['temp_air_port_degc'],    Met_Casey_V2_18['temp_air_port_degc']), axis = None)
EarlySummer_ATS_SI  = np.concatenate((Met_Casey_V2_17['temp_air_strbrd_degc'],  Met_Casey_V2_18['temp_air_strbrd_degc']), axis = None)
EarlySummer_AT_SI   = (EarlySummer_ATP_SI + EarlySummer_ATS_SI) / 2
LateSummer_ATP_SI   = np.concatenate((Met_Mawson_V3_17['temp_air_port_degc'],   Met_Davis_V3_17['temp_air_port_degc'],   Met_Mawson_V3_18['temp_air_port_degc'],   Met_Davis_V3_18['temp_air_port_degc']), axis = None)
LateSummer_ATS_SI   = np.concatenate((Met_Mawson_V3_17['temp_air_strbrd_degc'], Met_Davis_V3_17['temp_air_strbrd_degc'], Met_Mawson_V3_18['temp_air_strbrd_degc'], Met_Davis_V3_18['temp_air_strbrd_degc']), axis = None)
LateSummer_AT_SI    = (LateSummer_ATP_SI + LateSummer_ATS_SI) / 2
Summer_ATP_SI       = np.concatenate((Met_Casey_V2_17['temp_air_port_degc'],    Met_Casey_V2_18['temp_air_port_degc'],   Met_Mawson_V3_17['temp_air_port_degc'],   Met_Davis_V3_17['temp_air_port_degc'],   Met_Mawson_V3_18['temp_air_port_degc'],   Met_Davis_V3_18['temp_air_port_degc']), axis = None)
Summer_ATS_SI       = np.concatenate((Met_Casey_V2_17['temp_air_strbrd_degc'],  Met_Casey_V2_18['temp_air_strbrd_degc'], Met_Mawson_V3_17['temp_air_strbrd_degc'], Met_Davis_V3_17['temp_air_strbrd_degc'], Met_Mawson_V3_18['temp_air_strbrd_degc'], Met_Davis_V3_18['temp_air_strbrd_degc']), axis = None)
Summer_AT_SI        = (Summer_ATP_SI + Summer_ATS_SI) / 2
Autumn_ATP_SI       = np.concatenate((Met_MQIsl_V4_17['temp_air_port_degc'],    Met_MQIsl_V4_18['temp_air_port_degc']), axis = None)
Autumn_ATS_SI       = np.concatenate((Met_MQIsl_V4_17['temp_air_strbrd_degc'],  Met_MQIsl_V4_18['temp_air_strbrd_degc']), axis = None)
Autumn_AT_SI        = (Autumn_ATP_SI + Autumn_ATS_SI) / 2

# Open water
LateSpring_ATP_OW   = np.concatenate((Met_V1_17_OW['temp_air_port_degc'],    Met_V1_18_OW['temp_air_port_degc']), axis = None)
LateSpring_ATS_OW   = np.concatenate((Met_V1_17_OW['temp_air_strbrd_degc'],  Met_V1_18_OW['temp_air_strbrd_degc']), axis = None)
LateSpring_AT_OW    = (LateSpring_ATP_OW + LateSpring_ATS_OW) / 2
EarlySummer_ATP_OW  = np.concatenate((Met_V2_17_OW['temp_air_port_degc'],    Met_V2_18_OW['temp_air_port_degc']), axis = None)
EarlySummer_ATS_OW  = np.concatenate((Met_V2_17_OW['temp_air_strbrd_degc'],  Met_V2_18_OW['temp_air_strbrd_degc']), axis = None)
EarlySummer_AT_OW   = (EarlySummer_ATP_OW + EarlySummer_ATS_OW) / 2
LateSummer_ATP_OW   = np.concatenate((Met_V3_17M_OW['temp_air_port_degc'],   Met_V3_18M_OW['temp_air_port_degc']), axis = None)
LateSummer_ATS_OW   = np.concatenate((Met_V3_17M_OW['temp_air_strbrd_degc'], Met_V3_18M_OW['temp_air_strbrd_degc']), axis = None)
LateSummer_AT_OW    = (LateSummer_ATP_OW + LateSummer_ATS_OW) / 2
Summer_ATP_OW       = np.concatenate((Met_V2_17_OW['temp_air_port_degc'],    Met_V2_18_OW['temp_air_port_degc'],   Met_V3_17M_OW['temp_air_port_degc'],   Met_V3_18M_OW['temp_air_port_degc']), axis = None)
Summer_ATS_OW       = np.concatenate((Met_V2_17_OW['temp_air_strbrd_degc'],  Met_V2_18_OW['temp_air_strbrd_degc'], Met_V3_17M_OW['temp_air_strbrd_degc'], Met_V3_18M_OW['temp_air_strbrd_degc']), axis = None)
Summer_AT_OW        = (Summer_ATP_OW + Summer_ATS_OW) / 2
Autumn_ATP_OW       = np.concatenate((Met_V4_17_OW['temp_air_port_degc'],    Met_V4_18_OW['temp_air_port_degc']), axis = None)
Autumn_ATS_OW       = np.concatenate((Met_V4_17_OW['temp_air_strbrd_degc'],  Met_V4_18_OW['temp_air_strbrd_degc']), axis = None)
Autumn_AT_OW        = (Autumn_ATP_OW + Autumn_ATS_OW) / 2

#--------------
# Wind speed
#--------------
# Whole voyage
LateSpring_WSP_All  = np.concatenate((Met_V1_17['wnd_spd_port_corr_knot'],    Met_V1_18['wnd_spd_port_corr_knot']), axis = None)
LateSpring_WSS_All  = np.concatenate((Met_V1_17['wnd_spd_strbrd_corr_knot'],  Met_V1_18['wnd_spd_strbrd_corr_knot']), axis = None)
LateSpring_WS_All   = (LateSpring_WSP_All + LateSpring_WSS_All) / 2
EarlySummer_WSP_All = np.concatenate((Met_V2_17['wnd_spd_port_corr_knot'],    Met_V2_18['wnd_spd_port_corr_knot']), axis = None)
EarlySummer_WSS_All = np.concatenate((Met_V2_17['wnd_spd_strbrd_corr_knot'],  Met_V2_18['wnd_spd_strbrd_corr_knot']), axis = None)
EarlySummer_WS_All  = (EarlySummer_WSP_All + EarlySummer_WSS_All) / 2
LateSummer_WSP_All  = np.concatenate((Met_V3_17M['wnd_spd_port_corr_knot'],   Met_V3_18M['wnd_spd_port_corr_knot']), axis = None)
LateSummer_WSS_All  = np.concatenate((Met_V3_17M['wnd_spd_strbrd_corr_knot'], Met_V3_18M['wnd_spd_strbrd_corr_knot']), axis = None)
LateSummer_WS_All   = (LateSummer_WSP_All + LateSummer_WSS_All) / 2
Summer_WSP_All      = np.concatenate((Met_V2_17['wnd_spd_port_corr_knot'],    Met_V2_18['wnd_spd_port_corr_knot'],   Met_V3_17M['wnd_spd_port_corr_knot'],   Met_V3_18M['wnd_spd_port_corr_knot']), axis = None)
Summer_WSS_All      = np.concatenate((Met_V2_17['wnd_spd_strbrd_corr_knot'],  Met_V2_18['wnd_spd_strbrd_corr_knot'], Met_V3_17M['wnd_spd_strbrd_corr_knot'], Met_V3_18M['wnd_spd_strbrd_corr_knot']), axis = None)
Summer_WS_All       = (Summer_WSP_All + Summer_WSS_All) / 2
Autumn_WSP_All      = np.concatenate((Met_V4_17['wnd_spd_port_corr_knot'],    Met_V4_18['wnd_spd_port_corr_knot']), axis = None)
Autumn_WSS_All      = np.concatenate((Met_V4_17['wnd_spd_strbrd_corr_knot'],  Met_V4_18['wnd_spd_strbrd_corr_knot']), axis = None)
Autumn_WS_All       = (Autumn_WSP_All + Autumn_WSS_All) / 2

# Over sea ice
LateSpring_WSP_SI   = np.concatenate((Met_Davis_V1_17['wnd_spd_port_corr_knot'],    Met_Davis_V1_18['wnd_spd_port_corr_knot']), axis = None)
LateSpring_WSS_SI   = np.concatenate((Met_Davis_V1_17['wnd_spd_strbrd_corr_knot'],  Met_Davis_V1_18['wnd_spd_strbrd_corr_knot']), axis = None)
LateSpring_WS_SI    = (LateSpring_WSP_SI + LateSpring_WSS_SI) / 2
EarlySummer_WSP_SI  = np.concatenate((Met_Casey_V2_17['wnd_spd_port_corr_knot'],    Met_Casey_V2_18['wnd_spd_port_corr_knot']), axis = None)
EarlySummer_WSS_SI  = np.concatenate((Met_Casey_V2_17['wnd_spd_strbrd_corr_knot'],  Met_Casey_V2_18['wnd_spd_strbrd_corr_knot']), axis = None)
EarlySummer_WS_SI   = (EarlySummer_WSP_SI + EarlySummer_WSS_SI) / 2
LateSummer_WSP_SI   = np.concatenate((Met_Mawson_V3_17['wnd_spd_port_corr_knot'],   Met_Davis_V3_17['wnd_spd_port_corr_knot'],   Met_Mawson_V3_18['wnd_spd_port_corr_knot'],   Met_Davis_V3_18['wnd_spd_port_corr_knot']), axis = None)
LateSummer_WSS_SI   = np.concatenate((Met_Mawson_V3_17['wnd_spd_strbrd_corr_knot'], Met_Davis_V3_17['wnd_spd_strbrd_corr_knot'], Met_Mawson_V3_18['wnd_spd_strbrd_corr_knot'], Met_Davis_V3_18['wnd_spd_strbrd_corr_knot']), axis = None)
LateSummer_WS_SI    = (LateSummer_WSP_SI + LateSummer_WSS_SI) / 2
Summer_WSP_SI       = np.concatenate((Met_Casey_V2_17['wnd_spd_port_corr_knot'],    Met_Casey_V2_18['wnd_spd_port_corr_knot'],   Met_Mawson_V3_17['wnd_spd_port_corr_knot'],   Met_Davis_V3_17['wnd_spd_port_corr_knot'],   Met_Mawson_V3_18['wnd_spd_port_corr_knot'],   Met_Davis_V3_18['wnd_spd_port_corr_knot']), axis = None)
Summer_WSS_SI       = np.concatenate((Met_Casey_V2_17['wnd_spd_strbrd_corr_knot'],  Met_Casey_V2_18['wnd_spd_strbrd_corr_knot'], Met_Mawson_V3_17['wnd_spd_strbrd_corr_knot'], Met_Davis_V3_17['wnd_spd_strbrd_corr_knot'], Met_Mawson_V3_18['wnd_spd_strbrd_corr_knot'], Met_Davis_V3_18['wnd_spd_strbrd_corr_knot']), axis = None)
Summer_WS_SI        = (Summer_WSP_SI + Summer_WSS_SI) / 2
Autumn_WSP_SI       = np.concatenate((Met_MQIsl_V4_17['wnd_spd_port_corr_knot'],    Met_MQIsl_V4_18['wnd_spd_port_corr_knot']), axis = None)
Autumn_WSS_SI       = np.concatenate((Met_MQIsl_V4_17['wnd_spd_strbrd_corr_knot'],  Met_MQIsl_V4_18['wnd_spd_strbrd_corr_knot']), axis = None)
Autumn_WS_SI        = (Autumn_WSP_SI + Autumn_WSS_SI) / 2

# Open water
LateSpring_WSP_OW   = np.concatenate((Met_V1_17_OW['wnd_spd_port_corr_knot'],    Met_V1_18_OW['wnd_spd_port_corr_knot']), axis = None)
LateSpring_WSS_OW   = np.concatenate((Met_V1_17_OW['wnd_spd_port_corr_knot'],  Met_V1_18_OW['wnd_spd_strbrd_corr_knot']), axis = None)
LateSpring_WS_OW    = (LateSpring_WSP_OW + LateSpring_WSS_OW) / 2
EarlySummer_WSP_OW  = np.concatenate((Met_V2_17_OW['wnd_spd_port_corr_knot'],    Met_V2_18_OW['wnd_spd_port_corr_knot']), axis = None)
EarlySummer_WSS_OW  = np.concatenate((Met_V2_17_OW['wnd_spd_strbrd_corr_knot'],  Met_V2_18_OW['wnd_spd_strbrd_corr_knot']), axis = None)
EarlySummer_WS_OW   = (EarlySummer_WSP_OW + EarlySummer_WSS_OW) / 2
LateSummer_WSP_OW   = np.concatenate((Met_V3_17M_OW['wnd_spd_port_corr_knot'],   Met_V3_18M_OW['wnd_spd_port_corr_knot']), axis = None)
LateSummer_WSS_OW   = np.concatenate((Met_V3_17M_OW['wnd_spd_strbrd_corr_knot'], Met_V3_18M_OW['wnd_spd_strbrd_corr_knot']), axis = None)
LateSummer_WS_OW    = (LateSummer_WSP_OW + LateSummer_WSS_OW) / 2
Summer_WSP_OW       = np.concatenate((Met_V2_17_OW['wnd_spd_port_corr_knot'],    Met_V2_18_OW['wnd_spd_port_corr_knot'],   Met_V3_17M_OW['wnd_spd_port_corr_knot'],   Met_V3_18M_OW['wnd_spd_port_corr_knot']), axis = None)
Summer_WSS_OW       = np.concatenate((Met_V2_17_OW['wnd_spd_strbrd_corr_knot'],  Met_V2_18_OW['wnd_spd_strbrd_corr_knot'], Met_V3_17M_OW['wnd_spd_strbrd_corr_knot'], Met_V3_18M_OW['wnd_spd_strbrd_corr_knot']), axis = None)
Summer_WS_OW        = (Summer_WSP_OW + Summer_WSS_OW) / 2
Autumn_WSP_OW       = np.concatenate((Met_V4_17_OW['wnd_spd_port_corr_knot'],    Met_V4_18_OW['wnd_spd_port_corr_knot']), axis = None)
Autumn_WSS_OW       = np.concatenate((Met_V4_17_OW['wnd_spd_strbrd_corr_knot'],  Met_V4_18_OW['wnd_spd_strbrd_corr_knot']), axis = None)
Autumn_WS_OW        = (Autumn_WSP_OW + Autumn_WSS_OW) / 2

#--------------
# Solar radiation
#--------------
# Whole voyage
LateSpring_SRP_All  = np.concatenate((Met_V1_17['rad_slr_port_wperm2'],    Met_V1_18['rad_slr_port_wperm2']), axis = None)
LateSpring_SRS_All  = np.concatenate((Met_V1_17['rad_slr_strbrd_wperm2'],  Met_V1_18['rad_slr_strbrd_wperm2']), axis = None)
LateSpring_SR_All   = (LateSpring_SRP_All + LateSpring_SRS_All) / 2
EarlySummer_SRP_All = np.concatenate((Met_V2_17['rad_slr_port_wperm2'],    Met_V2_18['rad_slr_port_wperm2']), axis = None)
EarlySummer_SRS_All = np.concatenate((Met_V2_17['rad_slr_strbrd_wperm2'],  Met_V2_18['rad_slr_strbrd_wperm2']), axis = None)
EarlySummer_SR_All  = (EarlySummer_SRP_All + EarlySummer_SRS_All) / 2
LateSummer_SRP_All  = np.concatenate((Met_V3_17M['rad_slr_port_wperm2'],   Met_V3_18M['rad_slr_port_wperm2']), axis = None)
LateSummer_SRS_All  = np.concatenate((Met_V3_17M['rad_slr_strbrd_wperm2'], Met_V3_18M['rad_slr_strbrd_wperm2']), axis = None)
LateSummer_SR_All   = (LateSummer_SRP_All + LateSummer_SRS_All) / 2
Summer_SRP_All      = np.concatenate((Met_V2_17['rad_slr_port_wperm2'],    Met_V2_18['rad_slr_port_wperm2'],   Met_V3_17M['rad_slr_port_wperm2'],   Met_V3_18M['rad_slr_port_wperm2']), axis = None)
Summer_SRS_All      = np.concatenate((Met_V2_17['rad_slr_strbrd_wperm2'],  Met_V2_18['rad_slr_strbrd_wperm2'], Met_V3_17M['rad_slr_strbrd_wperm2'], Met_V3_18M['rad_slr_strbrd_wperm2']), axis = None)
Summer_SR_All       = (Summer_SRP_All + Summer_SRS_All) / 2
Autumn_SRP_All      = np.concatenate((Met_V4_17['rad_slr_port_wperm2'],    Met_V4_18['rad_slr_port_wperm2']), axis = None)
Autumn_SRS_All      = np.concatenate((Met_V4_17['rad_slr_strbrd_wperm2'],  Met_V4_18['rad_slr_strbrd_wperm2']), axis = None)
Autumn_SR_All       = (Autumn_SRP_All + Autumn_SRS_All) / 2

# Over sea ice
LateSpring_SRP_SI   = np.concatenate((Met_Davis_V1_17['rad_slr_port_wperm2'],    Met_Davis_V1_18['rad_slr_port_wperm2']), axis = None)
LateSpring_SRS_SI   = np.concatenate((Met_Davis_V1_17['rad_slr_strbrd_wperm2'],  Met_Davis_V1_18['rad_slr_strbrd_wperm2']), axis = None)
LateSpring_SR_SI    = (LateSpring_SRP_SI + LateSpring_SRS_SI) / 2
EarlySummer_SRP_SI  = np.concatenate((Met_Casey_V2_17['rad_slr_port_wperm2'],    Met_Casey_V2_18['rad_slr_port_wperm2']), axis = None)
EarlySummer_SRS_SI  = np.concatenate((Met_Casey_V2_17['rad_slr_strbrd_wperm2'],  Met_Casey_V2_18['rad_slr_strbrd_wperm2']), axis = None)
EarlySummer_SR_SI   = (EarlySummer_SRP_SI + EarlySummer_SRS_SI) / 2
LateSummer_SRP_SI   = np.concatenate((Met_Mawson_V3_17['rad_slr_port_wperm2'],   Met_Davis_V3_17['rad_slr_port_wperm2'],   Met_Mawson_V3_18['rad_slr_port_wperm2'],   Met_Davis_V3_18['rad_slr_port_wperm2']), axis = None)
LateSummer_SRS_SI   = np.concatenate((Met_Mawson_V3_17['rad_slr_strbrd_wperm2'], Met_Davis_V3_17['rad_slr_strbrd_wperm2'], Met_Mawson_V3_18['rad_slr_strbrd_wperm2'], Met_Davis_V3_18['rad_slr_strbrd_wperm2']), axis = None)
LateSummer_SR_SI    = (LateSummer_SRP_SI + LateSummer_SRS_SI) / 2
Summer_SRP_SI       = np.concatenate((Met_Casey_V2_17['rad_slr_port_wperm2'],    Met_Casey_V2_18['rad_slr_port_wperm2'],   Met_Mawson_V3_17['rad_slr_port_wperm2'],   Met_Davis_V3_17['rad_slr_port_wperm2'],   Met_Mawson_V3_18['rad_slr_port_wperm2'],   Met_Davis_V3_18['rad_slr_port_wperm2']), axis = None)
Summer_SRS_SI       = np.concatenate((Met_Casey_V2_17['rad_slr_strbrd_wperm2'],  Met_Casey_V2_18['rad_slr_strbrd_wperm2'], Met_Mawson_V3_17['rad_slr_strbrd_wperm2'], Met_Davis_V3_17['rad_slr_strbrd_wperm2'], Met_Mawson_V3_18['rad_slr_strbrd_wperm2'], Met_Davis_V3_18['rad_slr_strbrd_wperm2']), axis = None)
Summer_SR_SI        = (Summer_SRP_SI + Summer_SRS_SI) / 2
Autumn_SRP_SI       = np.concatenate((Met_MQIsl_V4_17['rad_slr_port_wperm2'],    Met_MQIsl_V4_18['rad_slr_port_wperm2']), axis = None)
Autumn_SRS_SI       = np.concatenate((Met_MQIsl_V4_17['rad_slr_strbrd_wperm2'],  Met_MQIsl_V4_18['rad_slr_strbrd_wperm2']), axis = None)
Autumn_SR_SI        = (Autumn_SRP_SI + Autumn_SRS_SI) / 2

# Open water
LateSpring_SRP_OW   = np.concatenate((Met_V1_17_OW['rad_slr_port_wperm2'],    Met_V1_18_OW['rad_slr_port_wperm2']), axis = None)
LateSpring_SRS_OW   = np.concatenate((Met_V1_17_OW['rad_slr_strbrd_wperm2'],  Met_V1_18_OW['rad_slr_strbrd_wperm2']), axis = None)
LateSpring_SR_OW    = (LateSpring_SRP_OW + LateSpring_SRS_OW) / 2
EarlySummer_SRP_OW  = np.concatenate((Met_V2_17_OW['rad_slr_port_wperm2'],    Met_V2_18_OW['rad_slr_port_wperm2']), axis = None)
EarlySummer_SRS_OW  = np.concatenate((Met_V2_17_OW['rad_slr_strbrd_wperm2'],  Met_V2_18_OW['rad_slr_strbrd_wperm2']), axis = None)
EarlySummer_SR_OW   = (EarlySummer_SRP_OW + EarlySummer_SRS_OW) / 2
LateSummer_SRP_OW   = np.concatenate((Met_V3_17M_OW['rad_slr_port_wperm2'],   Met_V3_18M_OW['rad_slr_port_wperm2']), axis = None)
LateSummer_SRS_OW   = np.concatenate((Met_V3_17M_OW['rad_slr_strbrd_wperm2'], Met_V3_18M_OW['rad_slr_strbrd_wperm2']), axis = None)
LateSummer_SR_OW    = (LateSummer_SRP_OW + LateSummer_SRS_OW) / 2
Summer_SRP_OW       = np.concatenate((Met_V2_17_OW['rad_slr_port_wperm2'],    Met_V2_18_OW['rad_slr_port_wperm2'],   Met_V3_17M_OW['rad_slr_port_wperm2'],   Met_V3_18M_OW['rad_slr_port_wperm2']), axis = None)
Summer_SRS_OW       = np.concatenate((Met_V2_17_OW['rad_slr_strbrd_wperm2'],  Met_V2_18_OW['rad_slr_strbrd_wperm2'], Met_V3_17M_OW['rad_slr_strbrd_wperm2'], Met_V3_18M_OW['rad_slr_strbrd_wperm2']), axis = None)
Summer_SR_OW        = (Summer_SRP_OW + Summer_SRS_OW) / 2
Autumn_SRP_OW       = np.concatenate((Met_V4_17_OW['rad_slr_port_wperm2'],    Met_V4_18_OW['rad_slr_port_wperm2']), axis = None)
Autumn_SRS_OW       = np.concatenate((Met_V4_17_OW['rad_slr_strbrd_wperm2'],  Met_V4_18_OW['rad_slr_strbrd_wperm2']), axis = None)
Autumn_SR_OW        = (Autumn_SRP_OW + Autumn_SRS_OW) / 2

#------------------------------------------------------------------------------
# CALCULATE THE MEAN WEATHER PARAMETERS

#--------------
# Water temperature
#--------------
LateSpring_Mean_WT_All  = np.nanmean(LateSpring_WT_All)
EarlySummer_Mean_WT_All = np.nanmean(EarlySummer_WT_All)
LateSummer_Mean_WT_All  = np.nanmean(LateSummer_WT_All)
Summer_Mean_WT_All      = np.nanmean(Summer_WT_All)
Autumn_Mean_WT_All      = np.nanmean(Autumn_WT_All)

LateSpring_Mean_WT_SI   = np.nanmean(LateSpring_WT_SI)
EarlySummer_Mean_WT_SI  = np.nanmean(EarlySummer_WT_SI)
LateSummer_Mean_WT_SI   = np.nanmean(LateSummer_WT_SI)
Summer_Mean_WT_SI       = np.nanmean(Summer_WT_SI)
Autumn_Mean_WT_SI       = np.nanmean(Autumn_WT_SI)

LateSpring_Mean_WT_OW   = np.nanmean(LateSpring_WT_OW)
EarlySummer_Mean_WT_OW  = np.nanmean(EarlySummer_WT_OW)
LateSummer_Mean_WT_OW   = np.nanmean(LateSummer_WT_OW)
Summer_Mean_WT_OW       = np.nanmean(Summer_WT_OW)
Autumn_Mean_WT_OW       = np.nanmean(Autumn_WT_OW)

#--------------
# Air temperature
#--------------
LateSpring_Mean_AT_All  = np.nanmean(LateSpring_AT_All)
EarlySummer_Mean_AT_All = np.nanmean(EarlySummer_AT_All)
LateSummer_Mean_AT_All  = np.nanmean(LateSummer_AT_All)
Summer_Mean_AT_All      = np.nanmean(Summer_AT_All)
Autumn_Mean_AT_All      = np.nanmean(Autumn_AT_All)

LateSpring_Mean_AT_SI   = np.nanmean(LateSpring_AT_SI)
EarlySummer_Mean_AT_SI  = np.nanmean(EarlySummer_AT_SI)
LateSummer_Mean_AT_SI   = np.nanmean(LateSummer_AT_SI)
Summer_Mean_AT_SI       = np.nanmean(Summer_AT_SI)
Autumn_Mean_AT_SI       = np.nanmean(Autumn_AT_SI)

LateSpring_Mean_AT_OW   = np.nanmean(LateSpring_AT_OW)
EarlySummer_Mean_AT_OW  = np.nanmean(EarlySummer_AT_OW)
LateSummer_Mean_AT_OW   = np.nanmean(LateSummer_AT_OW)
Summer_Mean_AT_OW       = np.nanmean(Summer_AT_OW)
Autumn_Mean_AT_OW       = np.nanmean(Autumn_AT_OW)

#--------------
# Wind speed
#--------------
LateSpring_Mean_WS_All  = np.nanmean(LateSpring_WS_All)
EarlySummer_Mean_WS_All = np.nanmean(EarlySummer_WS_All)
LateSummer_Mean_WS_All  = np.nanmean(LateSummer_WS_All)
Summer_Mean_WS_All      = np.nanmean(Summer_WS_All)
Autumn_Mean_WS_All      = np.nanmean(Autumn_WS_All)

LateSpring_Mean_WS_SI   = np.nanmean(LateSpring_WS_SI)
EarlySummer_Mean_WS_SI  = np.nanmean(EarlySummer_WS_SI)
LateSummer_Mean_WS_SI   = np.nanmean(LateSummer_WS_SI)
Summer_Mean_WS_SI       = np.nanmean(Summer_WS_SI)
Autumn_Mean_WS_SI       = np.nanmean(Autumn_WS_SI)

LateSpring_Mean_WS_OW   = np.nanmean(LateSpring_WS_OW)
EarlySummer_Mean_WS_OW  = np.nanmean(EarlySummer_WS_OW)
LateSummer_Mean_WS_OW   = np.nanmean(LateSummer_WS_OW)
Summer_Mean_WS_OW       = np.nanmean(Summer_WS_OW)
Autumn_Mean_WS_OW       = np.nanmean(Autumn_WS_OW)

#--------------
# Solar radiation
#--------------
LateSpring_Mean_SR_All  = np.nanmean(LateSpring_SR_All)
EarlySummer_Mean_SR_All = np.nanmean(EarlySummer_SR_All)
LateSummer_Mean_SR_All  = np.nanmean(LateSummer_SR_All)
Summer_Mean_SR_All      = np.nanmean(Summer_SR_All)
Autumn_Mean_SR_All      = np.nanmean(Autumn_SR_All)

LateSpring_Mean_SR_SI   = np.nanmean(LateSpring_SR_SI)
EarlySummer_Mean_SR_SI  = np.nanmean(EarlySummer_SR_SI)
LateSummer_Mean_SR_SI   = np.nanmean(LateSummer_SR_SI)
Summer_Mean_SR_SI       = np.nanmean(Summer_SR_SI)
Autumn_Mean_SR_SI       = np.nanmean(Autumn_SR_SI)

LateSpring_Mean_SR_OW   = np.nanmean(LateSpring_SR_OW)
EarlySummer_Mean_SR_OW  = np.nanmean(EarlySummer_SR_OW)
LateSummer_Mean_SR_OW   = np.nanmean(LateSummer_SR_OW)
Summer_Mean_SR_OW       = np.nanmean(Summer_SR_OW)
Autumn_Mean_SR_OW       = np.nanmean(Autumn_SR_OW)

#------------------------------------------------------------------------------
# CALCULATE THE STANDARD DEVIATION WEATHER PARAMETERS

#--------------
# Water temperature
#--------------
LateSpring_std_WT_All  = np.nanstd(LateSpring_WT_All)
EarlySummer_std_WT_All = np.nanstd(EarlySummer_WT_All)
LateSummer_std_WT_All  = np.nanstd(LateSummer_WT_All)
Summer_std_WT_All      = np.nanstd(Summer_WT_All)
Autumn_std_WT_All      = np.nanstd(Autumn_WT_All)

LateSpring_std_WT_SI   = np.nanstd(LateSpring_WT_SI)
EarlySummer_std_WT_SI  = np.nanstd(EarlySummer_WT_SI)
LateSummer_std_WT_SI   = np.nanstd(LateSummer_WT_SI)
Summer_std_WT_SI       = np.nanstd(Summer_WT_SI)
Autumn_std_WT_SI       = np.nanstd(Autumn_WT_SI)

LateSpring_std_WT_OW   = np.nanstd(LateSpring_WT_OW)
EarlySummer_std_WT_OW  = np.nanstd(EarlySummer_WT_OW)
LateSummer_std_WT_OW   = np.nanstd(LateSummer_WT_OW)
Summer_std_WT_OW       = np.nanstd(Summer_WT_OW)
Autumn_std_WT_OW       = np.nanstd(Autumn_WT_OW)

#--------------
# Air temperature
#--------------
LateSpring_std_AT_All  = np.nanstd(LateSpring_AT_All)
EarlySummer_std_AT_All = np.nanstd(EarlySummer_AT_All)
LateSummer_std_AT_All  = np.nanstd(LateSummer_AT_All)
Summer_std_AT_All      = np.nanstd(Summer_AT_All)
Autumn_std_AT_All      = np.nanstd(Autumn_AT_All)

LateSpring_std_AT_SI   = np.nanstd(LateSpring_AT_SI)
EarlySummer_std_AT_SI  = np.nanstd(EarlySummer_AT_SI)
LateSummer_std_AT_SI   = np.nanstd(LateSummer_AT_SI)
Summer_std_AT_SI       = np.nanstd(Summer_AT_SI)
Autumn_std_AT_SI       = np.nanstd(Autumn_AT_SI)

LateSpring_std_AT_OW   = np.nanstd(LateSpring_AT_OW)
EarlySummer_std_AT_OW  = np.nanstd(EarlySummer_AT_OW)
LateSummer_std_AT_OW   = np.nanstd(LateSummer_AT_OW)
Summer_std_AT_OW       = np.nanstd(Summer_AT_OW)
Autumn_std_AT_OW       = np.nanstd(Autumn_AT_OW)

#--------------
# Wind speed
#--------------
LateSpring_std_WS_All  = np.nanstd(LateSpring_WS_All)
EarlySummer_std_WS_All = np.nanstd(EarlySummer_WS_All)
LateSummer_std_WS_All  = np.nanstd(LateSummer_WS_All)
Summer_std_WS_All      = np.nanstd(Summer_WS_All)
Autumn_std_WS_All      = np.nanstd(Autumn_WS_All)

LateSpring_std_WS_SI   = np.nanstd(LateSpring_WS_SI)
EarlySummer_std_WS_SI  = np.nanstd(EarlySummer_WS_SI)
LateSummer_std_WS_SI   = np.nanstd(LateSummer_WS_SI)
Summer_std_WS_SI       = np.nanstd(Summer_WS_SI)
Autumn_std_WS_SI       = np.nanstd(Autumn_WS_SI)

LateSpring_std_WS_OW   = np.nanstd(LateSpring_WS_OW)
EarlySummer_std_WS_OW  = np.nanstd(EarlySummer_WS_OW)
LateSummer_std_WS_OW   = np.nanstd(LateSummer_WS_OW)
Summer_std_WS_OW       = np.nanstd(Summer_WS_OW)
Autumn_std_WS_OW       = np.nanstd(Autumn_WS_OW)

#--------------
# Solar radiation
#--------------
LateSpring_std_SR_All  = np.nanstd(LateSpring_SR_All)
EarlySummer_std_SR_All = np.nanstd(EarlySummer_SR_All)
LateSummer_std_SR_All  = np.nanstd(LateSummer_SR_All)
Summer_std_SR_All      = np.nanstd(Summer_SR_All)
Autumn_std_SR_All      = np.nanstd(Autumn_SR_All)

LateSpring_std_SR_SI   = np.nanstd(LateSpring_SR_SI)
EarlySummer_std_SR_SI  = np.nanstd(EarlySummer_SR_SI)
LateSummer_std_SR_SI   = np.nanstd(LateSummer_SR_SI)
Summer_std_SR_SI       = np.nanstd(Summer_SR_SI)
Autumn_std_SR_SI       = np.nanstd(Autumn_SR_SI)

LateSpring_std_SR_OW   = np.nanstd(LateSpring_SR_OW)
EarlySummer_std_SR_OW  = np.nanstd(EarlySummer_SR_OW)
LateSummer_std_SR_OW   = np.nanstd(LateSummer_SR_OW)
Summer_std_SR_OW       = np.nanstd(Summer_SR_OW)
Autumn_std_SR_OW       = np.nanstd(Autumn_SR_OW)

#------------------------------------------------------------------------------
# COUNT THE NUMBER OF OBSERVATIONS OVERALL, EACH SEASON & VOYAGE

# Whole voyage
N_SIPEXII_All = len(Hg0_SIPEXII)
N_PCAN_All    = len(Hg0_PCAN)

N_V1_17_All   = len(Hg0_V1_17)
N_V2_17_All   = len(Hg0_V2_17)
N_V3_17_All   = len(Hg0_V3_17M)
N_V3_17M_All  = len(Hg0_V3_17M)
N_V3_17D_All  = len(Hg0_V3_17D)
N_V4_17_All   = len(Hg0_V4_17)

N_V1_18_All   = len(Hg0_V1_18)
N_V2_18_All   = len(Hg0_V2_18)
N_V3_18_All   = len(Hg0_V3_18M)
N_V3_18M_All  = len(Hg0_V3_18M)
N_V3_18D_All  = len(Hg0_V3_18D)
N_V4_18_All   = len(Hg0_V4_18)

# On station/Sea ice
N_SIPEXII_S = len(Hg0_SIPEXII_Ice)
N_PCAN_S    = len(Hg0_PCAN_Ice)

N_V1_17_S   = len(Hg0_Davis_V1_17)
N_V2_17_S   = len(Hg0_Casey_V2_17)
N_V3_17_S   = len(Hg0_V3_17_Ice)
N_V3_17M_S  = len(Hg0_Mawson_V3_17)
N_V3_17D_S  = len(Hg0_Davis_V3_17)
N_V4_17_S   = len(Hg0_MQIsl_V4_17)

N_V1_18_S   = len(Hg0_Davis_V1_18)
N_V2_18_S   = len(Hg0_Casey_V2_18)
N_V3_18_S   = len(Hg0_V3_18_Ice)
N_V3_18M_S  = len(Hg0_Mawson_V3_18)
N_V3_18D_S  = len(Hg0_Davis_V3_18)
N_V4_18_S   = len(Hg0_MQIsl_V4_18)

# Open water
N_SIPEXII_OW = len(Hg0_SIPEXII_OW)
N_PCAN_OW    = len(Hg0_PCAN_OW)

N_V1_17_OW   = len(Hg0_V1_17_OW)
N_V2_17_OW   = len(Hg0_V2_17_OW)
N_V3_17_OW   = len(Hg0_V3_17_OW)
N_V3_17M_OW  = len(Hg0_V3_17M_OW)
N_V3_17D_OW  = len(Hg0_V3_17D_OW)
N_V4_17_OW   = len(Hg0_V4_17_OW)

N_V1_18_OW   = len(Hg0_V1_18_OW)
N_V2_18_OW   = len(Hg0_V2_18_OW)
N_V3_18_OW   = len(Hg0_V3_18_OW)
N_V3_18M_OW  = len(Hg0_V3_18M_OW)
N_V3_18D_OW  = len(Hg0_V3_18D_OW)
N_V4_18_OW   = len(Hg0_V4_18_OW)

#------------------------------------------------------------------------------
# CALCULATE THE MEAN HG0

# Whole voyage
SIPEXII_Mean_All = np.mean(Hg0_SIPEXII['ng/m3'])
PCAN_Mean_All    = np.mean(Hg0_PCAN['ng/m3'])

V1_17_Mean_All   = np.mean(Hg0_V1_17['ng/m3'])
V2_17_Mean_All   = np.mean(Hg0_V2_17['ng/m3'])
V3_17_Mean_All   = np.mean(Hg0_V3_17M['ng/m3'])
V3_17M_Mean_All  = np.mean(Hg0_V3_17M['ng/m3'])
V3_17D_Mean_All  = np.mean(Hg0_V3_17D['ng/m3'])
V4_17_Mean_All   = np.mean(Hg0_V4_17['ng/m3'])

V1_18_Mean_All   = np.mean(Hg0_V1_18['ng/m3'])
V2_18_Mean_All   = np.mean(Hg0_V2_18['ng/m3'])
V3_18_Mean_All   = np.mean(Hg0_V3_18M['ng/m3'])
V3_18M_Mean_All  = np.mean(Hg0_V3_18M['ng/m3'])
V3_18D_Mean_All  = np.mean(Hg0_V3_18D['ng/m3'])
V4_18_Mean_All   = np.mean(Hg0_V4_18['ng/m3'])

# On station/Sea ice
SIPEXII_Mean_S = np.mean(Hg0_SIPEXII_Ice['ng/m3'])
PCAN_Mean_S    = np.mean(Hg0_PCAN_Ice['ng/m3'])

V1_17_Mean_S   = np.mean(Hg0_Davis_V1_17['ng/m3'])
V2_17_Mean_S   = np.mean(Hg0_Casey_V2_17['ng/m3'])
V3_17_Mean_S   = np.mean(Hg0_V3_17_Ice['ng/m3'])
V3_17M_Mean_S  = np.mean(Hg0_Mawson_V3_17['ng/m3'])
V3_17D_Mean_S  = np.mean(Hg0_Davis_V3_17['ng/m3'])
V4_17_Mean_S   = np.mean(Hg0_MQIsl_V4_17['ng/m3'])

V1_18_Mean_S   = np.mean(Hg0_Davis_V1_18['ng/m3'])
V2_18_Mean_S   = np.mean(Hg0_Casey_V2_18['ng/m3'])
V3_18_Mean_S   = np.mean(Hg0_V3_18_Ice['ng/m3'])
V3_18M_Mean_S  = np.mean(Hg0_Mawson_V3_18['ng/m3'])
V3_18D_Mean_S  = np.mean(Hg0_Davis_V3_18['ng/m3'])
V4_18_Mean_S   = np.mean(Hg0_MQIsl_V4_18['ng/m3'])

# Open water
SIPEXII_Mean_OW = np.mean(Hg0_SIPEXII_OW['ng/m3'])
PCAN_Mean_OW    = np.mean(Hg0_PCAN_OW['ng/m3'])

V1_17_Mean_OW   = np.mean(Hg0_V1_17_OW['ng/m3'])
V2_17_Mean_OW   = np.mean(Hg0_V2_17_OW['ng/m3'])
V3_17_Mean_OW   = np.mean(Hg0_V3_17_OW['ng/m3'])
V3_17M_Mean_OW  = np.mean(Hg0_V3_17M_OW['ng/m3'])
V3_17D_Mean_OW  = np.mean(Hg0_V3_17D_OW['ng/m3'])
V4_17_Mean_OW   = np.mean(Hg0_V4_17_OW['ng/m3'])

V1_18_Mean_OW   = np.mean(Hg0_V1_18_OW['ng/m3'])
V2_18_Mean_OW   = np.mean(Hg0_V2_18_OW['ng/m3'])
V3_18_Mean_OW   = np.mean(Hg0_V3_18_OW['ng/m3'])
V3_18M_Mean_OW  = np.mean(Hg0_V3_18M_OW['ng/m3'])
V3_18D_Mean_OW  = np.mean(Hg0_V3_18D_OW['ng/m3'])
V4_18_Mean_OW   = np.mean(Hg0_V4_18_OW['ng/m3'])

# Seasonal values
LateSpring_Mean_All  = np.mean(LateSpring_All)
EarlySummer_Mean_All = np.mean(EarlySummer_All)
LateSummer_Mean_All  = np.mean(LateSummer_All)
Summer_Mean_All      = np.mean(Summer_All)
Autumn_Mean_All      = np.mean(Autumn_All)

LateSpring_Mean_SI   = np.mean(LateSpring_SI)
EarlySummer_Mean_SI  = np.mean(EarlySummer_SI)
LateSummer_Mean_SI   = np.mean(LateSummer_SI)
Summer_Mean_SI       = np.mean(Summer_SI)
Autumn_Mean_SI       = np.mean(Autumn_SI)

LateSpring_Mean_OW   = np.mean(LateSpring_OW)
EarlySummer_Mean_OW  = np.mean(EarlySummer_OW)
LateSummer_Mean_OW   = np.mean(LateSummer_OW)
Summer_Mean_OW       = np.mean(Summer_OW)
Autumn_Mean_OW       = np.mean(Autumn_OW)

#------------------------------------------------------------------------------
# CALCULATE THE HG0 STANDARD DEVIATION

# Whole voyage
SIPEXII_std_All = np.std(Hg0_SIPEXII['ng/m3'])
PCAN_std_All    = np.std(Hg0_PCAN['ng/m3'])

V1_17_std_All   = np.std(Hg0_V1_17['ng/m3'])
V2_17_std_All   = np.std(Hg0_V2_17['ng/m3'])
V3_17_std_All   = np.std(Hg0_V3_17M['ng/m3'])
V3_17M_std_All  = np.std(Hg0_V3_17M['ng/m3'])
V3_17D_std_All  = np.std(Hg0_V3_17D['ng/m3'])
V4_17_std_All   = np.std(Hg0_V4_17['ng/m3'])

V1_18_std_All   = np.std(Hg0_V1_18['ng/m3'])
V2_18_std_All   = np.std(Hg0_V2_18['ng/m3'])
V3_18_std_All   = np.std(Hg0_V3_18M['ng/m3'])
V3_18M_std_All  = np.std(Hg0_V3_18M['ng/m3'])
V3_18D_std_All  = np.std(Hg0_V3_18D['ng/m3'])
V4_18_std_All   = np.std(Hg0_V4_18['ng/m3'])

# On station/Sea ice
SIPEXII_std_S = np.std(Hg0_SIPEXII_Ice['ng/m3'])
PCAN_std_S    = np.std(Hg0_PCAN_Ice['ng/m3'])

V1_17_std_S   = np.std(Hg0_Davis_V1_17['ng/m3'])
V2_17_std_S   = np.std(Hg0_Casey_V2_17['ng/m3'])
V3_17_std_S   = np.std(Hg0_V3_17_Ice['ng/m3'])
V3_17M_std_S  = np.std(Hg0_Mawson_V3_17['ng/m3'])
V3_17D_std_S  = np.std(Hg0_Davis_V3_17['ng/m3'])
V4_17_std_S   = np.std(Hg0_MQIsl_V4_17['ng/m3'])

V1_18_std_S   = np.std(Hg0_Davis_V1_18['ng/m3'])
V2_18_std_S   = np.std(Hg0_Casey_V2_18['ng/m3'])
V3_18_std_S   = np.std(Hg0_V3_18_Ice['ng/m3'])
V3_18M_std_S  = np.std(Hg0_Mawson_V3_18['ng/m3'])
V3_18D_std_S  = np.std(Hg0_Davis_V3_18['ng/m3'])
V4_18_std_S   = np.std(Hg0_MQIsl_V4_18['ng/m3'])

# Open water
SIPEXII_std_OW = np.std(Hg0_SIPEXII_OW['ng/m3'])
PCAN_std_OW    = np.std(Hg0_PCAN_OW['ng/m3'])

V1_17_std_OW   = np.std(Hg0_V1_17_OW['ng/m3'])
V2_17_std_OW   = np.std(Hg0_V2_17_OW['ng/m3'])
V3_17_std_OW   = np.mean(Hg0_V3_17_OW['ng/m3'])
V3_17M_std_OW  = np.std(Hg0_V3_17M_OW['ng/m3'])
V3_17D_std_OW  = np.std(Hg0_V3_17D_OW['ng/m3'])
V4_17_std_OW   = np.std(Hg0_V4_17_OW['ng/m3'])

V1_18_std_OW   = np.std(Hg0_V1_18_OW['ng/m3'])
V2_18_std_OW   = np.std(Hg0_V2_18_OW['ng/m3'])
V3_18_std_OW   = np.mean(Hg0_V3_18_OW['ng/m3'])
V3_18M_std_OW  = np.std(Hg0_V3_18M_OW['ng/m3'])
V3_18D_std_OW  = np.std(Hg0_V3_18D_OW['ng/m3'])
V4_18_std_OW   = np.std(Hg0_V4_18_OW['ng/m3'])

# Seasonal values
LateSpring_std_All  = np.std(LateSpring_All)
EarlySummer_std_All = np.std(EarlySummer_All)
LateSummer_std_All  = np.std(LateSummer_All)
Summer_std_All      = np.std(Summer_All)
Autumn_std_All      = np.std(Autumn_All)

LateSpring_std_SI   = np.std(LateSpring_SI)
EarlySummer_std_SI  = np.std(EarlySummer_SI)
LateSummer_std_SI   = np.std(LateSummer_SI)
Summer_std_SI       = np.std(Summer_SI)
Autumn_std_SI       = np.std(Autumn_SI)

LateSpring_std_OW   = np.std(LateSpring_OW)
EarlySummer_std_OW  = np.std(EarlySummer_OW)
LateSummer_std_OW   = np.std(LateSummer_OW)
Summer_std_OW       = np.std(Summer_OW)
Autumn_std_OW       = np.std(Autumn_OW)

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN HG0

# Whole voyage
SIPEXII_Median_All = np.median(Hg0_SIPEXII['ng/m3'])
PCAN_Median_All    = np.median(Hg0_PCAN['ng/m3'])

V1_17_Median_All   = np.median(Hg0_V1_17['ng/m3'])
V2_17_Median_All   = np.median(Hg0_V2_17['ng/m3'])
V3_17_Median_All   = np.mean(Hg0_V3_17M['ng/m3'])
V3_17M_Median_All  = np.median(Hg0_V3_17M['ng/m3'])
V3_17D_Median_All  = np.median(Hg0_V3_17D['ng/m3'])
V4_17_Median_All   = np.median(Hg0_V4_17['ng/m3'])

V1_18_Median_All   = np.median(Hg0_V1_18['ng/m3'])
V2_18_Median_All   = np.median(Hg0_V2_18['ng/m3'])
V3_18_Median_All   = np.mean(Hg0_V3_18M['ng/m3'])
V3_18M_Median_All  = np.median(Hg0_V3_18M['ng/m3'])
V3_18D_Median_All  = np.median(Hg0_V3_18D['ng/m3'])
V4_18_Median_All   = np.median(Hg0_V4_18['ng/m3'])

# On station/Sea ice
SIPEXII_Median_S = np.median(Hg0_SIPEXII_Ice['ng/m3'])
PCAN_Median_S    = np.median(Hg0_PCAN_Ice['ng/m3'])

V1_17_Median_S   = np.median(Hg0_Davis_V1_17['ng/m3'])
V2_17_Median_S   = np.median(Hg0_Casey_V2_17['ng/m3'])
V3_17_Median_S   = np.median(Hg0_V3_17_Ice['ng/m3'])
V3_17M_Median_S  = np.median(Hg0_Mawson_V3_17['ng/m3'])
V3_17D_Median_S  = np.median(Hg0_Davis_V3_17['ng/m3'])
V4_17_Median_S   = np.median(Hg0_MQIsl_V4_17['ng/m3'])

V1_18_Median_S   = np.median(Hg0_Davis_V1_18['ng/m3'])
V2_18_Median_S   = np.median(Hg0_Casey_V2_18['ng/m3'])
V3_18_Median_S   = np.median(Hg0_V3_18_Ice['ng/m3'])
V3_18M_Median_S  = np.median(Hg0_Mawson_V3_18['ng/m3'])
V3_18D_Median_S  = np.median(Hg0_Davis_V3_18['ng/m3'])
V4_18_Median_S   = np.median(Hg0_MQIsl_V4_18['ng/m3'])

# Open water
SIPEXII_Median_OW = np.median(Hg0_SIPEXII_OW['ng/m3'])
PCAN_Median_OW    = np.median(Hg0_PCAN_OW['ng/m3'])

V1_17_Median_OW   = np.median(Hg0_V1_17_OW['ng/m3'])
V2_17_Median_OW   = np.median(Hg0_V2_17_OW['ng/m3'])
V3_17_Median_OW   = np.median(Hg0_V3_17_OW['ng/m3'])
V3_17M_Median_OW  = np.median(Hg0_V3_17M_OW['ng/m3'])
V3_17D_Median_OW  = np.median(Hg0_V3_17D_OW['ng/m3'])
V4_17_Median_OW   = np.median(Hg0_V4_17_OW['ng/m3'])

V1_18_Median_OW   = np.median(Hg0_V1_18_OW['ng/m3'])
V2_18_Median_OW   = np.median(Hg0_V2_18_OW['ng/m3'])
V3_18_Median_OW   = np.median(Hg0_V3_18_OW['ng/m3'])
V3_18M_Median_OW  = np.median(Hg0_V3_18M_OW['ng/m3'])
V3_18D_Median_OW  = np.median(Hg0_V3_18D_OW['ng/m3'])
V4_18_Median_OW   = np.median(Hg0_V4_18_OW['ng/m3'])

# Seasonal values
LateSpring_Median_All  = np.median(LateSpring_All)
EarlySummer_Median_All = np.median(EarlySummer_All)
LateSummer_Median_All  = np.median(LateSummer_All)
Summer_Median_All      = np.median(Summer_All)
Autumn_Median_All      = np.median(Autumn_All)

LateSpring_Median_SI   = np.median(LateSpring_SI)
EarlySummer_Median_SI  = np.median(EarlySummer_SI)
LateSummer_Median_SI   = np.median(LateSummer_SI)
Summer_Median_SI       = np.median(Summer_SI)
Autumn_Median_SI       = np.median(Autumn_SI)

LateSpring_Median_OW   = np.median(LateSpring_OW)
EarlySummer_Median_OW  = np.median(EarlySummer_OW)
LateSummer_Median_OW   = np.median(LateSummer_OW)
Summer_Median_OW       = np.median(Summer_OW)
Autumn_Median_OW       = np.median(Autumn_OW)

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN ABSOLUTE DEVIATION HG0

# Whole voyage
SIPEXII_MAD_All = stats.median_absolute_deviation(Hg0_SIPEXII['ng/m3'])
PCAN_MAD_All    = stats.median_absolute_deviation(Hg0_PCAN['ng/m3'])

V1_17_MAD_All   = stats.median_absolute_deviation(Hg0_V1_17['ng/m3'])
V2_17_MAD_All   = stats.median_absolute_deviation(Hg0_V2_17['ng/m3'])
V3_17_MAD_All   = stats.median_absolute_deviation(Hg0_V3_17M['ng/m3'])
V3_17M_MAD_All  = stats.median_absolute_deviation(Hg0_V3_17M['ng/m3'])
V3_17D_MAD_All  = stats.median_absolute_deviation(Hg0_V3_17D['ng/m3'])
V4_17_MAD_All   = stats.median_absolute_deviation(Hg0_V4_17['ng/m3'])

V1_18_MAD_All   = stats.median_absolute_deviation(Hg0_V1_18['ng/m3'])
V2_18_MAD_All   = stats.median_absolute_deviation(Hg0_V2_18['ng/m3'])
V3_18_MAD_All   = stats.median_absolute_deviation(Hg0_V3_18M['ng/m3'])
V3_18M_MAD_All  = stats.median_absolute_deviation(Hg0_V3_18M['ng/m3'])
V3_18D_MAD_All  = stats.median_absolute_deviation(Hg0_V3_18D['ng/m3'])
V4_18_MAD_All   = stats.median_absolute_deviation(Hg0_V4_18['ng/m3'])

# On station/Sea ice
SIPEXII_MAD_S = stats.median_absolute_deviation(Hg0_SIPEXII_Ice['ng/m3'])
PCAN_MAD_S    = stats.median_absolute_deviation(Hg0_PCAN_Ice['ng/m3'])

V1_17_MAD_S   = stats.median_absolute_deviation(Hg0_Davis_V1_17['ng/m3'])
V2_17_MAD_S   = stats.median_absolute_deviation(Hg0_Casey_V2_17['ng/m3'])
V3_17_MAD_S   = stats.median_absolute_deviation(Hg0_V3_17_Ice['ng/m3'])
V3_17M_MAD_S  = stats.median_absolute_deviation(Hg0_Mawson_V3_17['ng/m3'])
V3_17D_MAD_S  = stats.median_absolute_deviation(Hg0_Davis_V3_17['ng/m3'])
V4_17_MAD_S   = stats.median_absolute_deviation(Hg0_MQIsl_V4_17['ng/m3'])

V1_18_MAD_S   = stats.median_absolute_deviation(Hg0_Davis_V1_18['ng/m3'])
V2_18_MAD_S   = stats.median_absolute_deviation(Hg0_Casey_V2_18['ng/m3'])
V3_18_MAD_S   = stats.median_absolute_deviation(Hg0_V3_18_Ice['ng/m3'])
V3_18M_MAD_S  = stats.median_absolute_deviation(Hg0_Mawson_V3_18['ng/m3'])
V3_18D_MAD_S  = stats.median_absolute_deviation(Hg0_Davis_V3_18['ng/m3'])
V4_18_MAD_S   = stats.median_absolute_deviation(Hg0_MQIsl_V4_18['ng/m3'])

# Open ocean
SIPEXII_MAD_OW  = stats.median_absolute_deviation(Hg0_SIPEXII_OW['ng/m3'])
PCAN_MAD_OW     = stats.median_absolute_deviation(Hg0_PCAN_OW['ng/m3'])

V1_17_MAD_OW    = stats.median_absolute_deviation(Hg0_V1_17_OW['ng/m3'])
V2_17_MAD_OW    = stats.median_absolute_deviation(Hg0_V2_17_OW['ng/m3'])
V3_17_MAD_OW    = stats.median_absolute_deviation(Hg0_V3_17_OW['ng/m3'])
V3_17M_MAD_OW   = stats.median_absolute_deviation(Hg0_V3_17M_OW['ng/m3'])
V3_17D_MAD_OW   = stats.median_absolute_deviation(Hg0_V3_17D_OW['ng/m3'])
V4_17_MAD_OW    = stats.median_absolute_deviation(Hg0_V4_17_OW['ng/m3'])

V1_18_MAD_OW    = stats.median_absolute_deviation(Hg0_V1_18_OW['ng/m3'])
V2_18_MAD_OW    = stats.median_absolute_deviation(Hg0_V2_18_OW['ng/m3'])
V3_18_MAD_OW    = stats.median_absolute_deviation(Hg0_V3_18_OW['ng/m3'])
V3_18M_MAD_OW   = stats.median_absolute_deviation(Hg0_V3_18M_OW['ng/m3'])
V3_18D_MAD_OW   = stats.median_absolute_deviation(Hg0_V3_18D_OW['ng/m3'])
V4_18_MAD_OW    = stats.median_absolute_deviation(Hg0_V4_18_OW['ng/m3'])

# Seasonal values
LateSpring_MAD_All  = stats.median_absolute_deviation(LateSpring_All)
EarlySummer_MAD_All = stats.median_absolute_deviation(EarlySummer_All)
LateSummer_MAD_All  = stats.median_absolute_deviation(LateSummer_All)
Summer_MAD_All      = stats.median_absolute_deviation(Summer_All)
Autumn_MAD_All      = stats.median_absolute_deviation(Autumn_All)

LateSpring_MAD_SI   = stats.median_absolute_deviation(LateSpring_SI)
EarlySummer_MAD_SI  = stats.median_absolute_deviation(EarlySummer_SI)
LateSummer_MAD_SI   = stats.median_absolute_deviation(LateSummer_SI)
Summer_MAD_SI       = stats.median_absolute_deviation(Summer_SI)
Autumn_MAD_SI       = stats.median_absolute_deviation(Autumn_SI)

LateSpring_MAD_OW   = stats.median_absolute_deviation(LateSpring_OW)
EarlySummer_MAD_OW  = stats.median_absolute_deviation(EarlySummer_OW)
LateSummer_MAD_OW   = stats.median_absolute_deviation(LateSummer_OW)
Summer_MAD_OW       = stats.median_absolute_deviation(Summer_OW)
Autumn_MAD_OW       = stats.median_absolute_deviation(Autumn_OW)

#------------------------------------------------------------------------------
# CALCULATE THE INTERQUARTILE RANGE HG0

# Whole voyage
SIPEXII_IQR_All = stats.iqr(Hg0_SIPEXII['ng/m3'])
PCAN_IQR_All    = stats.iqr(Hg0_PCAN['ng/m3'])

V1_17_IQR_All   = stats.iqr(Hg0_V1_17['ng/m3'])
V2_17_IQR_All   = stats.iqr(Hg0_V2_17['ng/m3'])
V3_17_IQR_All   = stats.iqr(Hg0_V3_17M['ng/m3'])
V3_17M_IQR_All  = stats.iqr(Hg0_V3_17M['ng/m3'])
V3_17D_IQR_All  = stats.iqr(Hg0_V3_17D['ng/m3'])
V4_17_IQR_All   = stats.iqr(Hg0_V4_17['ng/m3'])

V1_18_IQR_All   = stats.iqr(Hg0_V1_18['ng/m3'])
V2_18_IQR_All   = stats.iqr(Hg0_V2_18['ng/m3'])
V3_18_IQR_All   = stats.iqr(Hg0_V3_18M['ng/m3'])
V3_18M_IQR_All  = stats.iqr(Hg0_V3_18M['ng/m3'])
V3_18D_IQR_All  = stats.iqr(Hg0_V3_18D['ng/m3'])
V4_18_IQR_All   = stats.iqr(Hg0_V4_18['ng/m3'])

# On station/Sea ice
SIPEXII_IQR_S = stats.iqr(Hg0_SIPEXII_Ice['ng/m3'])
PCAN_IQR_S    = stats.iqr(Hg0_PCAN_Ice['ng/m3'])

V1_17_IQR_S   = stats.iqr(Hg0_Davis_V1_17['ng/m3'])
V2_17_IQR_S   = stats.iqr(Hg0_Casey_V2_17['ng/m3'])
V3_17_IQR_S   = stats.iqr(Hg0_V3_17_Ice['ng/m3'])
V3_17M_IQR_S  = stats.iqr(Hg0_Mawson_V3_17['ng/m3'])
V3_17D_IQR_S  = stats.iqr(Hg0_Davis_V3_17['ng/m3'])
V4_17_IQR_S   = stats.iqr(Hg0_MQIsl_V4_17['ng/m3'])

V1_18_IQR_S   = stats.iqr(Hg0_Davis_V1_18['ng/m3'])
V2_18_IQR_S   = stats.iqr(Hg0_Casey_V2_18['ng/m3'])
V3_18_IQR_S   = stats.iqr(Hg0_V3_18_Ice['ng/m3'])
V3_18M_IQR_S  = stats.iqr(Hg0_Mawson_V3_18['ng/m3'])
V3_18D_IQR_S  = stats.iqr(Hg0_Davis_V3_18['ng/m3'])
V4_18_IQR_S   = stats.iqr(Hg0_MQIsl_V4_18['ng/m3'])

# Open ocean
SIPEXII_IQR_OW = stats.iqr(Hg0_SIPEXII_OW['ng/m3'])
PCAN_IQR_OW    = stats.iqr(Hg0_PCAN_OW['ng/m3'])

V1_17_IQR_OW   = stats.iqr(Hg0_V1_17_OW['ng/m3'])
V2_17_IQR_OW   = stats.iqr(Hg0_V2_17_OW['ng/m3'])
V3_17_IQR_OW   = stats.iqr(Hg0_V3_17_OW['ng/m3'])
V3_17M_IQR_OW  = stats.iqr(Hg0_V3_17M_OW['ng/m3'])
V3_17D_IQR_OW  = stats.iqr(Hg0_V3_17D_OW['ng/m3'])
V4_17_IQR_OW   = stats.iqr(Hg0_V4_17_OW['ng/m3'])

V1_18_IQR_OW   = stats.iqr(Hg0_V1_18_OW['ng/m3'])
V2_18_IQR_OW   = stats.iqr(Hg0_V2_18_OW['ng/m3'])
V3_18_IQR_OW   = stats.iqr(Hg0_V3_18_OW['ng/m3'])
V3_18M_IQR_OW  = stats.iqr(Hg0_V3_18M_OW['ng/m3'])
V3_18D_IQR_OW  = stats.iqr(Hg0_V3_18D_OW['ng/m3'])
V4_18_IQR_OW   = stats.iqr(Hg0_V4_18_OW['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE 5th PERCENTILE HG0

# Whole voyage
SIPEXII_5P_All = np.percentile(Hg0_SIPEXII['ng/m3'], 5)
PCAN_5P_All    = np.percentile(Hg0_PCAN['ng/m3'],    5)

V1_17_5P_All   = np.percentile(Hg0_V1_17['ng/m3'],   5)
V2_17_5P_All   = np.percentile(Hg0_V2_17['ng/m3'],   5)
V3_17_5P_All   = np.percentile(Hg0_V3_17M['ng/m3'],  5)
V3_17M_5P_All  = np.percentile(Hg0_V3_17M['ng/m3'],  5)
V3_17D_5P_All  = np.percentile(Hg0_V3_17D['ng/m3'],  5)
V4_17_5P_All   = np.percentile(Hg0_V4_17['ng/m3'],   5)

V1_18_5P_All   = np.percentile(Hg0_V1_18['ng/m3'],   5)
V2_18_5P_All   = np.percentile(Hg0_V2_18['ng/m3'],   5)
V3_18_5P_All   = np.percentile(Hg0_V3_18M['ng/m3'],  5)
V3_18M_5P_All  = np.percentile(Hg0_V3_18M['ng/m3'],  5)
V3_18D_5P_All  = np.percentile(Hg0_V3_18D['ng/m3'],  5)
V4_18_5P_All   = np.percentile(Hg0_V4_18['ng/m3'],   5)

# On station/Sea ice
SIPEXII_5P_S = np.percentile(Hg0_SIPEXII_Ice['ng/m3'],  5)
PCAN_5P_S    = np.percentile(Hg0_PCAN_Ice['ng/m3'],     5)

V1_17_5P_S   = np.percentile(Hg0_Davis_V1_17['ng/m3'],  5)
V2_17_5P_S   = np.percentile(Hg0_Casey_V2_17['ng/m3'],  5)
V3_17_5P_S   = np.percentile(Hg0_V3_17_Ice['ng/m3'],    5)
V3_17M_5P_S  = np.percentile(Hg0_Mawson_V3_17['ng/m3'], 5)
V3_17D_5P_S  = np.percentile(Hg0_Davis_V3_17['ng/m3'],  5)
V4_17_5P_S   = np.percentile(Hg0_MQIsl_V4_17['ng/m3'],  5)

V1_18_5P_S   = np.percentile(Hg0_Davis_V1_18['ng/m3'],  5)
V2_18_5P_S   = np.percentile(Hg0_Casey_V2_18['ng/m3'],  5)
V3_18_5P_S   = np.percentile(Hg0_V3_18_Ice['ng/m3'],    5)
V3_18M_5P_S  = np.percentile(Hg0_Mawson_V3_18['ng/m3'], 5)
V3_18D_5P_S  = np.percentile(Hg0_Davis_V3_18['ng/m3'],  5)
V4_18_5P_S   = np.percentile(Hg0_MQIsl_V4_18['ng/m3'],  5)

# Open water
SIPEXII_5P_OW = np.percentile(Hg0_SIPEXII_OW['ng/m3'],5)
PCAN_5P_OW    = np.percentile(Hg0_PCAN_OW['ng/m3'],   5)

V1_17_5P_OW   = np.percentile(Hg0_V1_17_OW['ng/m3'],  5)
V2_17_5P_OW   = np.percentile(Hg0_V2_17_OW['ng/m3'],  5)
V3_17_5P_OW   = np.percentile(Hg0_V3_17_OW['ng/m3'],  5)
V3_17M_5P_OW  = np.percentile(Hg0_V3_17M_OW['ng/m3'], 5)
V3_17D_5P_OW  = np.percentile(Hg0_V3_17D_OW['ng/m3'], 5)
V4_17_5P_OW   = np.percentile(Hg0_V4_17_OW['ng/m3'],  5)

V1_18_5P_OW   = np.percentile(Hg0_V1_18_OW['ng/m3'],  5)
V2_18_5P_OW   = np.percentile(Hg0_V2_18_OW['ng/m3'],  5)
V3_18_5P_OW   = np.percentile(Hg0_V3_18_OW['ng/m3'],  5)
V3_18M_5P_OW  = np.percentile(Hg0_V3_18M_OW['ng/m3'], 5)
V3_18D_5P_OW  = np.percentile(Hg0_V3_18D_OW['ng/m3'], 5)
V4_18_5P_OW   = np.percentile(Hg0_V4_18_OW['ng/m3'],  5)

#------------------------------------------------------------------------------
# CALCULATE THE 25th PERCENTILE HG0

# Whole voyage
SIPEXII_25P_All = np.percentile(Hg0_SIPEXII['ng/m3'], 25)
PCAN_25P_All    = np.percentile(Hg0_PCAN['ng/m3'],    25)

V1_17_25P_All   = np.percentile(Hg0_V1_17['ng/m3'],   25)
V2_17_25P_All   = np.percentile(Hg0_V2_17['ng/m3'],   25)
V3_17_25P_All   = np.percentile(Hg0_V3_17M['ng/m3'],  25)
V3_17M_25P_All  = np.percentile(Hg0_V3_17M['ng/m3'],  25)
V3_17D_25P_All  = np.percentile(Hg0_V3_17D['ng/m3'],  25)
V4_17_25P_All   = np.percentile(Hg0_V4_17['ng/m3'],   25)

V1_18_25P_All   = np.percentile(Hg0_V1_18['ng/m3'],   25)
V2_18_25P_All   = np.percentile(Hg0_V2_18['ng/m3'],   25)
V3_18_25P_All   = np.percentile(Hg0_V3_18M['ng/m3'],  25)
V3_18M_25P_All  = np.percentile(Hg0_V3_18M['ng/m3'],  25)
V3_18D_25P_All  = np.percentile(Hg0_V3_18D['ng/m3'],  25)
V4_18_25P_All   = np.percentile(Hg0_V4_18['ng/m3'],   25)

# On station/Sea ice
SIPEXII_25P_S = np.percentile(Hg0_SIPEXII_Ice['ng/m3'],  25)
PCAN_25P_S    = np.percentile(Hg0_PCAN_Ice['ng/m3'],     25)

V1_17_25P_S   = np.percentile(Hg0_Davis_V1_17['ng/m3'],  25)
V2_17_25P_S   = np.percentile(Hg0_Casey_V2_17['ng/m3'],  25)
V3_17_25P_S   = np.percentile(Hg0_V3_17_Ice['ng/m3'],    25)
V3_17M_25P_S  = np.percentile(Hg0_Mawson_V3_17['ng/m3'], 25)
V3_17D_25P_S  = np.percentile(Hg0_Davis_V3_17['ng/m3'],  25)
V4_17_25P_S   = np.percentile(Hg0_MQIsl_V4_17['ng/m3'],  25)

V1_18_25P_S   = np.percentile(Hg0_Davis_V1_18['ng/m3'],  25)
V2_18_25P_S   = np.percentile(Hg0_Casey_V2_18['ng/m3'],  25)
V3_18_25P_S   = np.percentile(Hg0_V3_18_Ice['ng/m3'],    25)
V3_18M_25P_S  = np.percentile(Hg0_Mawson_V3_18['ng/m3'], 25)
V3_18D_25P_S  = np.percentile(Hg0_Davis_V3_18['ng/m3'],  25)
V4_18_25P_S   = np.percentile(Hg0_MQIsl_V4_18['ng/m3'],  25)

# Open water
SIPEXII_25P_OW = np.percentile(Hg0_SIPEXII_OW['ng/m3'],25)
PCAN_25P_OW    = np.percentile(Hg0_PCAN_OW['ng/m3'],   25)

V1_17_25P_OW   = np.percentile(Hg0_V1_17_OW['ng/m3'],  25)
V2_17_25P_OW   = np.percentile(Hg0_V2_17_OW['ng/m3'],  25)
V3_17_25P_OW   = np.percentile(Hg0_V3_17_OW['ng/m3'],    25)
V3_17M_25P_OW  = np.percentile(Hg0_V3_17M_OW['ng/m3'], 25)
V3_17D_25P_OW  = np.percentile(Hg0_V3_17D_OW['ng/m3'], 25)
V4_17_25P_OW   = np.percentile(Hg0_V4_17_OW['ng/m3'],  25)

V1_18_25P_OW   = np.percentile(Hg0_V1_18_OW['ng/m3'],  25)
V2_18_25P_OW   = np.percentile(Hg0_V2_18_OW['ng/m3'],  25)
V3_18_25P_OW   = np.percentile(Hg0_V3_18_OW['ng/m3'],    25)
V3_18M_25P_OW  = np.percentile(Hg0_V3_18M_OW['ng/m3'], 25)
V3_18D_25P_OW  = np.percentile(Hg0_V3_18D_OW['ng/m3'], 25)
V4_18_25P_OW   = np.percentile(Hg0_V4_18_OW['ng/m3'],  25)

#------------------------------------------------------------------------------
# CALCULATE THE 75th PERCENTILE HG0

# Whole voyage
SIPEXII_75P_All = np.percentile(Hg0_SIPEXII['ng/m3'], 75)
PCAN_75P_All    = np.percentile(Hg0_PCAN['ng/m3'],    75)

V1_17_75P_All   = np.percentile(Hg0_V1_17['ng/m3'],   75)
V2_17_75P_All   = np.percentile(Hg0_V2_17['ng/m3'],   75)
V3_17_75P_All   = np.percentile(Hg0_V3_17M['ng/m3'],  75)
V3_17M_75P_All  = np.percentile(Hg0_V3_17M['ng/m3'],  75)
V3_17D_75P_All  = np.percentile(Hg0_V3_17D['ng/m3'],  75)
V4_17_75P_All   = np.percentile(Hg0_V4_17['ng/m3'],   75)

V1_18_75P_All   = np.percentile(Hg0_V1_18['ng/m3'],   75)
V2_18_75P_All   = np.percentile(Hg0_V2_18['ng/m3'],   75)
V3_18_75P_All   = np.percentile(Hg0_V3_18M['ng/m3'],  75)
V3_18M_75P_All  = np.percentile(Hg0_V3_18M['ng/m3'],  75)
V3_18D_75P_All  = np.percentile(Hg0_V3_18D['ng/m3'],  75)
V4_18_75P_All   = np.percentile(Hg0_V4_18['ng/m3'],   75)

# On station/Sea ice
SIPEXII_75P_S = np.percentile(Hg0_SIPEXII_Ice['ng/m3'],  75)
PCAN_75P_S    = np.percentile(Hg0_PCAN_Ice['ng/m3'],     75)

V1_17_75P_S   = np.percentile(Hg0_Davis_V1_17['ng/m3'],  75)
V2_17_75P_S   = np.percentile(Hg0_Casey_V2_17['ng/m3'],  75)
V3_17_75P_S   = np.percentile(Hg0_V3_17_Ice['ng/m3'],    75)
V3_17M_75P_S  = np.percentile(Hg0_Mawson_V3_17['ng/m3'], 75)
V3_17D_75P_S  = np.percentile(Hg0_Davis_V3_17['ng/m3'],  75)
V4_17_75P_S   = np.percentile(Hg0_MQIsl_V4_17['ng/m3'],  75)

V1_18_75P_S   = np.percentile(Hg0_Davis_V1_18['ng/m3'],  75)
V2_18_75P_S   = np.percentile(Hg0_Casey_V2_18['ng/m3'],  75)
V3_18_75P_S   = np.percentile(Hg0_V3_18_Ice['ng/m3'],    75)
V3_18M_75P_S  = np.percentile(Hg0_Mawson_V3_18['ng/m3'], 75)
V3_18D_75P_S  = np.percentile(Hg0_Davis_V3_18['ng/m3'],  75)
V4_18_75P_S   = np.percentile(Hg0_MQIsl_V4_18['ng/m3'],  75)

# Open water
SIPEXII_75P_OW = np.percentile(Hg0_SIPEXII_OW['ng/m3'],75)
PCAN_75P_OW    = np.percentile(Hg0_PCAN_OW['ng/m3'],   75)

V1_17_75P_OW   = np.percentile(Hg0_V1_17_OW['ng/m3'],  75)
V2_17_75P_OW   = np.percentile(Hg0_V2_17_OW['ng/m3'],  75)
V3_17_75P_OW   = np.percentile(Hg0_V3_17_OW['ng/m3'],  75)
V3_17M_75P_OW  = np.percentile(Hg0_V3_17M_OW['ng/m3'], 75)
V3_17D_75P_OW  = np.percentile(Hg0_V3_17D_OW['ng/m3'], 75)
V4_17_75P_OW   = np.percentile(Hg0_V4_17_OW['ng/m3'],  75)

V1_18_75P_OW   = np.percentile(Hg0_V1_18_OW['ng/m3'],  75)
V2_18_75P_OW   = np.percentile(Hg0_V2_18_OW['ng/m3'],  75)
V3_18_75P_OW   = np.percentile(Hg0_V3_18_OW['ng/m3'],  75)
V3_18M_75P_OW  = np.percentile(Hg0_V3_18M_OW['ng/m3'], 75)
V3_18D_75P_OW  = np.percentile(Hg0_V3_18D_OW['ng/m3'], 75)
V4_18_75P_OW   = np.percentile(Hg0_V4_18_OW['ng/m3'],  75)

#------------------------------------------------------------------------------
# CALCULATE THE 95th PERCENTILE HG0

# Whole voyage
SIPEXII_95P_All = np.percentile(Hg0_SIPEXII['ng/m3'], 95)
PCAN_95P_All    = np.percentile(Hg0_PCAN['ng/m3'],    95)

V1_17_95P_All   = np.percentile(Hg0_V1_17['ng/m3'],   95)
V2_17_95P_All   = np.percentile(Hg0_V2_17['ng/m3'],   95)
V3_17_95P_All   = np.percentile(Hg0_V3_17M['ng/m3'],  95)
V3_17M_95P_All  = np.percentile(Hg0_V3_17M['ng/m3'],  95)
V3_17D_95P_All  = np.percentile(Hg0_V3_17D['ng/m3'],  95)
V4_17_95P_All   = np.percentile(Hg0_V4_17['ng/m3'],   95)

V1_18_95P_All   = np.percentile(Hg0_V1_18['ng/m3'],   95)
V2_18_95P_All   = np.percentile(Hg0_V2_18['ng/m3'],   95)
V3_18_95P_All   = np.percentile(Hg0_V3_18M['ng/m3'],  95)
V3_18M_95P_All  = np.percentile(Hg0_V3_18M['ng/m3'],  95)
V3_18D_95P_All  = np.percentile(Hg0_V3_18D['ng/m3'],  95)
V4_18_95P_All   = np.percentile(Hg0_V4_18['ng/m3'],   95)

# On station/Sea ice
SIPEXII_95P_S = np.percentile(Hg0_SIPEXII_Ice['ng/m3'],  95)
PCAN_95P_S    = np.percentile(Hg0_PCAN_Ice['ng/m3'],     95)

V1_17_95P_S   = np.percentile(Hg0_Davis_V1_17['ng/m3'],  95)
V2_17_95P_S   = np.percentile(Hg0_Casey_V2_17['ng/m3'],  95)
V3_17_95P_S   = np.percentile(Hg0_V3_17_Ice['ng/m3'],    95)
V3_17M_95P_S  = np.percentile(Hg0_Mawson_V3_17['ng/m3'], 95)
V3_17D_95P_S  = np.percentile(Hg0_Davis_V3_17['ng/m3'],  95)
V4_17_95P_S   = np.percentile(Hg0_MQIsl_V4_17['ng/m3'],  95)

V1_18_95P_S   = np.percentile(Hg0_Davis_V1_18['ng/m3'],  95)
V2_18_95P_S   = np.percentile(Hg0_Casey_V2_18['ng/m3'],  95)
V3_18_95P_S   = np.percentile(Hg0_V3_18_Ice['ng/m3'],    95)
V3_18M_95P_S  = np.percentile(Hg0_Mawson_V3_18['ng/m3'], 95)
V3_18D_95P_S  = np.percentile(Hg0_Davis_V3_18['ng/m3'],  95)
V4_18_95P_S   = np.percentile(Hg0_MQIsl_V4_18['ng/m3'],  95)

# Open water
SIPEXII_95P_OW = np.percentile(Hg0_SIPEXII_OW['ng/m3'],95)
PCAN_95P_OW    = np.percentile(Hg0_PCAN_OW['ng/m3'],   95)

V1_17_95P_OW   = np.percentile(Hg0_V1_17_OW['ng/m3'],  95)
V2_17_95P_OW   = np.percentile(Hg0_V2_17_OW['ng/m3'],  95)
V3_17_95P_OW   = np.percentile(Hg0_V3_17_OW['ng/m3'],  95)
V3_17M_95P_OW  = np.percentile(Hg0_V3_17M_OW['ng/m3'], 95)
V3_17D_95P_OW  = np.percentile(Hg0_V3_17D_OW['ng/m3'], 95)
V4_17_95P_OW   = np.percentile(Hg0_V4_17_OW['ng/m3'],  95)

V1_18_95P_OW   = np.percentile(Hg0_V1_18_OW['ng/m3'],  95)
V2_18_95P_OW   = np.percentile(Hg0_V2_18_OW['ng/m3'],  95)
V3_18_95P_OW   = np.percentile(Hg0_V3_18_OW['ng/m3'],  95)
V3_18M_95P_OW  = np.percentile(Hg0_V3_18M_OW['ng/m3'], 95)
V3_18D_95P_OW  = np.percentile(Hg0_V3_18D_OW['ng/m3'], 95)
V4_18_95P_OW   = np.percentile(Hg0_V4_18_OW['ng/m3'],  95)

#------------------------------------------------------------------------------
# CALCULATE THE MINIMUM HG0

# Whole voyage
SIPEXII_MIN_All = np.min(Hg0_SIPEXII['ng/m3'])
PCAN_MIN_All    = np.min(Hg0_PCAN['ng/m3'])

V1_17_MIN_All   = np.min(Hg0_V1_17['ng/m3'])
V2_17_MIN_All   = np.min(Hg0_V2_17['ng/m3'])
V3_17_MIN_All   = np.min(Hg0_V3_17M['ng/m3'])
V3_17M_MIN_All  = np.min(Hg0_V3_17M['ng/m3'])
V3_17D_MIN_All  = np.min(Hg0_V3_17D['ng/m3'])
V4_17_MIN_All   = np.min(Hg0_V4_17['ng/m3'])

V1_18_MIN_All   = np.min(Hg0_V1_18['ng/m3'])
V2_18_MIN_All   = np.min(Hg0_V2_18['ng/m3'])
V3_18_MIN_All   = np.min(Hg0_V3_18M['ng/m3'])
V3_18M_MIN_All  = np.min(Hg0_V3_18M['ng/m3'])
V3_18D_MIN_All  = np.min(Hg0_V3_18D['ng/m3'])
V4_18_MIN_All   = np.min(Hg0_V4_18['ng/m3'])

# On station/Sea ice
SIPEXII_MIN_S = np.min(Hg0_SIPEXII_Ice['ng/m3'])
PCAN_MIN_S    = np.min(Hg0_PCAN_Ice['ng/m3'])

V1_17_MIN_S   = np.min(Hg0_Davis_V1_17['ng/m3'])
V2_17_MIN_S   = np.min(Hg0_Casey_V2_17['ng/m3'])
V3_17_MIN_S   = np.min(Hg0_V3_17_Ice['ng/m3'])
V3_17M_MIN_S  = np.min(Hg0_Mawson_V3_17['ng/m3'])
V3_17D_MIN_S  = np.min(Hg0_Davis_V3_17['ng/m3'])
V4_17_MIN_S   = np.min(Hg0_MQIsl_V4_17['ng/m3'])

V1_18_MIN_S   = np.min(Hg0_Davis_V1_18['ng/m3'])
V2_18_MIN_S   = np.min(Hg0_Casey_V2_18['ng/m3'])
V3_18_MIN_S   = np.min(Hg0_V3_18_Ice['ng/m3'])
V3_18M_MIN_S  = np.min(Hg0_Mawson_V3_18['ng/m3'])
V3_18D_MIN_S  = np.min(Hg0_Davis_V3_18['ng/m3'])
V4_18_MIN_S   = np.min(Hg0_MQIsl_V4_18['ng/m3'])

# Open water
SIPEXII_MIN_OW = np.min(Hg0_SIPEXII_OW['ng/m3'])
PCAN_MIN_OW    = np.min(Hg0_PCAN_OW['ng/m3'])

V1_17_MIN_OW   = np.min(Hg0_V1_17_OW['ng/m3'])
V2_17_MIN_OW   = np.min(Hg0_V2_17_OW['ng/m3'])
V3_17_MIN_OW   = np.min(Hg0_V3_17_OW['ng/m3'])
V3_17M_MIN_OW  = np.min(Hg0_V3_17M_OW['ng/m3'])
V3_17D_MIN_OW  = np.min(Hg0_V3_17D_OW['ng/m3'])
V4_17_MIN_OW   = np.min(Hg0_V4_17_OW['ng/m3'])

V1_18_MIN_OW   = np.min(Hg0_V1_18_OW['ng/m3'])
V2_18_MIN_OW   = np.min(Hg0_V2_18_OW['ng/m3'])
V3_18_MIN_OW   = np.min(Hg0_V3_18_OW['ng/m3'])
V3_18M_MIN_OW  = np.min(Hg0_V3_18M_OW['ng/m3'])
V3_18D_MIN_OW  = np.min(Hg0_V3_18D_OW['ng/m3'])
V4_18_MIN_OW   = np.min(Hg0_V4_18_OW['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MAXIMUM HG0

# Whole voyage
SIPEXII_MAX_All = np.max(Hg0_SIPEXII['ng/m3'])
PCAN_MAX_All    = np.max(Hg0_PCAN['ng/m3'])

V1_17_MAX_All   = np.max(Hg0_V1_17['ng/m3'])
V2_17_MAX_All   = np.max(Hg0_V2_17['ng/m3'])
V3_17_MAX_All   = np.max(Hg0_V3_17M['ng/m3'])
V3_17M_MAX_All  = np.max(Hg0_V3_17M['ng/m3'])
V3_17D_MAX_All  = np.max(Hg0_V3_17D['ng/m3'])
V4_17_MAX_All   = np.max(Hg0_V4_17['ng/m3'])

V1_18_MAX_All   = np.max(Hg0_V1_18['ng/m3'])
V2_18_MAX_All   = np.max(Hg0_V2_18['ng/m3'])
V3_18_MAX_All   = np.max(Hg0_V3_17M['ng/m3'])
V3_18M_MAX_All  = np.max(Hg0_V3_18M['ng/m3'])
V3_18D_MAX_All  = np.max(Hg0_V3_18D['ng/m3'])
V4_18_MAX_All   = np.max(Hg0_V4_18['ng/m3'])

# On station/Sea ice
SIPEXII_MAX_S = np.max(Hg0_SIPEXII_Ice['ng/m3'])
PCAN_MAX_S    = np.max(Hg0_PCAN_Ice['ng/m3'])

V1_17_MAX_S   = np.max(Hg0_Davis_V1_17['ng/m3'])
V2_17_MAX_S   = np.max(Hg0_Casey_V2_17['ng/m3'])
V3_17_MAX_S   = np.max(Hg0_V3_17_Ice['ng/m3'])
V3_17M_MAX_S  = np.max(Hg0_Mawson_V3_17['ng/m3'])
V3_17D_MAX_S  = np.max(Hg0_Davis_V3_17['ng/m3'])
V4_17_MAX_S   = np.max(Hg0_MQIsl_V4_17['ng/m3'])

V1_18_MAX_S   = np.max(Hg0_Davis_V1_18['ng/m3'])
V2_18_MAX_S   = np.max(Hg0_Casey_V2_18['ng/m3'])
V3_18_MAX_S   = np.max(Hg0_V3_18_Ice['ng/m3'])
V3_18M_MAX_S  = np.max(Hg0_Mawson_V3_18['ng/m3'])
V3_18D_MAX_S  = np.max(Hg0_Davis_V3_18['ng/m3'])
V4_18_MAX_S   = np.max(Hg0_MQIsl_V4_18['ng/m3'])

# Open water
SIPEXII_MAX_OW = np.max(Hg0_SIPEXII_OW['ng/m3'])
PCAN_MAX_OW    = np.max(Hg0_PCAN_OW['ng/m3'])

V1_17_MAX_OW   = np.max(Hg0_V1_17_OW['ng/m3'])
V2_17_MAX_OW   = np.max(Hg0_V2_17_OW['ng/m3'])
V3_17_MAX_OW   = np.max(Hg0_V3_17_OW['ng/m3'])
V3_17M_MAX_OW  = np.max(Hg0_V3_17M_OW['ng/m3'])
V3_17D_MAX_OW  = np.max(Hg0_V3_17D_OW['ng/m3'])
V4_17_MAX_OW   = np.max(Hg0_V4_17_OW['ng/m3'])

V1_18_MAX_OW   = np.max(Hg0_V1_18_OW['ng/m3'])
V2_18_MAX_OW   = np.max(Hg0_V2_18_OW['ng/m3'])
V3_18_MAX_OW   = np.max(Hg0_V3_18_OW['ng/m3'])
V3_18M_MAX_OW  = np.max(Hg0_V3_18M_OW['ng/m3'])
V3_18D_MAX_OW  = np.max(Hg0_V3_18D_OW['ng/m3'])
V4_18_MAX_OW   = np.max(Hg0_V4_18_OW['ng/m3'])

#------------------------------------------------------------------------------
# Welches T-Test on Hg0
 
#----------------------
# T-test for the means of 2 indpendent populations
# (Note: unequal sample sizes and/or variance, therefore Welches t-test)
#----------------------

# Between On station/Sea ice & Open water
WT_stat_SIPEXII, WT_pval_SIPEXII = stats.ttest_ind(Hg0_SIPEXII_Ice['ng/m3'],  Hg0_SIPEXII_OW['ng/m3'], equal_var = False)
WT_stat_PCAN,    WT_pval_PCAN    = stats.ttest_ind(Hg0_PCAN_Ice['ng/m3'],     Hg0_PCAN_OW['ng/m3'],    equal_var = False)

WT_stat_V1_17,   WT_pval_V1_17   = stats.ttest_ind(Hg0_Davis_V1_17['ng/m3'],  Hg0_V1_17_OW['ng/m3'],   equal_var = False)
WT_stat_V2_17,   WT_pval_V2_17   = stats.ttest_ind(Hg0_Casey_V2_17['ng/m3'],  Hg0_V2_17_OW['ng/m3'],   equal_var = False)
WT_stat_V3_17,   WT_pval_V3_17   = stats.ttest_ind(Hg0_V3_17_Ice['ng/m3'],    Hg0_V3_17_OW['ng/m3'],   equal_var = False)
WT_stat_V3_17M,  WT_pval_V3_17M  = stats.ttest_ind(Hg0_Mawson_V3_17['ng/m3'], Hg0_V3_17M_OW['ng/m3'],  equal_var = False)
WT_stat_V3_17D,  WT_pval_V3_17D  = stats.ttest_ind(Hg0_Davis_V3_17['ng/m3'],  Hg0_V3_17D_OW['ng/m3'],  equal_var = False)
WT_stat_V4_17,   WT_pval_V4_17   = stats.ttest_ind(Hg0_MQIsl_V4_17['ng/m3'],  Hg0_V4_17_OW['ng/m3'],   equal_var = False)

WT_stat_V1_18,   WT_pval_V1_18   = stats.ttest_ind(Hg0_Davis_V1_18['ng/m3'],  Hg0_V1_18_OW['ng/m3'],   equal_var = False)
WT_stat_V2_18,   WT_pval_V2_18   = stats.ttest_ind(Hg0_Casey_V2_18['ng/m3'],  Hg0_V2_18_OW['ng/m3'],   equal_var = False)
WT_stat_V3_18,   WT_pval_V3_18   = stats.ttest_ind(Hg0_V3_18_Ice['ng/m3'],    Hg0_V3_18_OW['ng/m3'],   equal_var = False)
WT_stat_V3_18M,  WT_pval_V3_18M  = stats.ttest_ind(Hg0_Mawson_V3_18['ng/m3'], Hg0_V3_18M_OW['ng/m3'],  equal_var = False)
WT_stat_V3_18D,  WT_pval_V3_18D  = stats.ttest_ind(Hg0_Davis_V3_18['ng/m3'],  Hg0_V3_18D_OW['ng/m3'],  equal_var = False)
WT_stat_V4_18,   WT_pval_V4_18   = stats.ttest_ind(Hg0_MQIsl_V4_18['ng/m3'],  Hg0_V4_18_OW['ng/m3'],   equal_var = False)

#------------------------------------------------------------------------------
# KS-Test on BrO (Kolmogorov-Smirnov Test)

# Interannual variability (2017-18 to 2018-19)
#KS_stat_1,       KS_pval_1       = stats.ks_2samp(BrO_V1_17_D,               BrO_V1_18_D,             alternative='two-sided', mode='auto')

# Between On station/Sea ice & Open water
KS_stat_SIPEXII, KS_pval_SIPEXII = stats.ks_2samp(Hg0_SIPEXII_Ice['ng/m3'],  Hg0_SIPEXII_OW['ng/m3'], alternative='two-sided', mode='auto')
KS_stat_PCAN,    KS_pval_PCAN    = stats.ks_2samp(Hg0_PCAN_Ice['ng/m3'],     Hg0_PCAN_OW['ng/m3'],    alternative='two-sided', mode='auto')

KS_stat_V1_17,   KS_pval_V1_17   = stats.ks_2samp(Hg0_Davis_V1_17['ng/m3'],  Hg0_V1_17_OW['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V2_17,   KS_pval_V2_17   = stats.ks_2samp(Hg0_Casey_V2_17['ng/m3'],  Hg0_V2_17_OW['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_17,   KS_pval_V3_17   = stats.ks_2samp(Hg0_V3_17_Ice['ng/m3'],    Hg0_V3_17_OW['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_17M,  KS_pval_V3_17M  = stats.ks_2samp(Hg0_Mawson_V3_17['ng/m3'], Hg0_V3_17M_OW['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V3_17D,  KS_pval_V3_17D  = stats.ks_2samp(Hg0_Davis_V3_17['ng/m3'],  Hg0_V3_17D_OW['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V4_17,   KS_pval_V4_17   = stats.ks_2samp(Hg0_MQIsl_V4_17['ng/m3'],  Hg0_V4_17_OW['ng/m3'],   alternative='two-sided', mode='auto')

KS_stat_V1_18,   KS_pval_V1_18   = stats.ks_2samp(Hg0_Davis_V1_18['ng/m3'],  Hg0_V1_18_OW['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V2_18,   KS_pval_V2_18   = stats.ks_2samp(Hg0_Casey_V2_18['ng/m3'],  Hg0_V2_18_OW['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_18,   KS_pval_V3_18   = stats.ks_2samp(Hg0_V3_18_Ice['ng/m3'],    Hg0_V3_18_OW['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_18M,  KS_pval_V3_18M  = stats.ks_2samp(Hg0_Mawson_V3_18['ng/m3'], Hg0_V3_18M_OW['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V3_18D,  KS_pval_V3_18D  = stats.ks_2samp(Hg0_Davis_V3_18['ng/m3'],  Hg0_V3_18D_OW['ng/m3'],  alternative='two-sided', mode='auto')
KS_stat_V4_18,   KS_pval_V4_18   = stats.ks_2samp(Hg0_MQIsl_V4_18['ng/m3'],  Hg0_V4_18_OW['ng/m3'],   alternative='two-sided', mode='auto')

#------------------------------------------------------------------------------
# MW (Mann-Whitney) U-Test on BrO

# Interannual variability (2017-18 to 2018-19)
#MW_stat_1,       MW_pval_1       = stats.mannwhitneyu(BrO_V1_17_D,               BrO_V1_18_D,            alternative='two-sided')

# Between On station/Sea ice & Open water
MW_stat_SIPEXII, MW_pval_SIPEXII = stats.mannwhitneyu(Hg0_SIPEXII_Ice['ng/m3'],  Hg0_SIPEXII_OW['ng/m3'], alternative='two-sided')
MW_stat_PCAN,    MW_pval_PCAN    = stats.mannwhitneyu(Hg0_PCAN_Ice['ng/m3'],     Hg0_PCAN_OW['ng/m3'],    alternative='two-sided')

MW_stat_V1_17,   MW_pval_V1_17   = stats.mannwhitneyu(Hg0_Davis_V1_17['ng/m3'],  Hg0_V1_17_OW['ng/m3'],   alternative='two-sided')
MW_stat_V2_17,   MW_pval_V2_17   = stats.mannwhitneyu(Hg0_Casey_V2_17['ng/m3'],  Hg0_V2_17_OW['ng/m3'],   alternative='two-sided')
MW_stat_V3_17,   MW_pval_V3_17   = stats.mannwhitneyu(Hg0_V3_17_Ice['ng/m3'],    Hg0_V3_17_OW['ng/m3'],   alternative='two-sided')
MW_stat_V3_17M,  MW_pval_V3_17M  = stats.mannwhitneyu(Hg0_Mawson_V3_17['ng/m3'], Hg0_V3_17M_OW['ng/m3'],  alternative='two-sided')
MW_stat_V3_17D,  MW_pval_V3_17D  = stats.mannwhitneyu(Hg0_Davis_V3_17['ng/m3'],  Hg0_V3_17D_OW['ng/m3'],  alternative='two-sided')
MW_stat_V4_17,   MW_pval_V4_17   = stats.mannwhitneyu(Hg0_MQIsl_V4_17['ng/m3'],  Hg0_V4_17_OW['ng/m3'],   alternative='two-sided')

MW_stat_V1_18,   MW_pval_V1_18   = stats.mannwhitneyu(Hg0_Davis_V1_18['ng/m3'],  Hg0_V1_18_OW['ng/m3'],   alternative='two-sided')
MW_stat_V2_18,   MW_pval_V2_18   = stats.mannwhitneyu(Hg0_Casey_V2_18['ng/m3'],  Hg0_V2_18_OW['ng/m3'],   alternative='two-sided')
MW_stat_V3_18,   MW_pval_V3_18   = stats.mannwhitneyu(Hg0_V3_18_Ice['ng/m3'],    Hg0_V3_18_OW['ng/m3'],   alternative='two-sided')
MW_stat_V3_18M,  MW_pval_V3_18M  = stats.mannwhitneyu(Hg0_Mawson_V3_18['ng/m3'], Hg0_V3_18M_OW['ng/m3'],  alternative='two-sided')
MW_stat_V3_18D,  MW_pval_V3_18D  = stats.mannwhitneyu(Hg0_Davis_V3_18['ng/m3'],  Hg0_V3_18D_OW['ng/m3'],  alternative='two-sided')
MW_stat_V4_18,   MW_pval_V4_18   = stats.mannwhitneyu(Hg0_MQIsl_V4_18['ng/m3'],  Hg0_V4_18_OW['ng/m3'],   alternative='two-sided')

#------------------------------------------------------------------------------
# KW (Kruskal-Wallis) H-Test on BrO

# Interannual variability (2017-18 to 2018-19)
#KW_stat_1,       KW_pval_1       = stats.kruskal(BrO_V1_17_D,               BrO_V1_18_D)

# Between On station/Sea ice & Open water
KW_stat_SIPEXII, KW_pval_SIPEXII = stats.kruskal(Hg0_SIPEXII_Ice['ng/m3'],  Hg0_SIPEXII_OW['ng/m3'])
KW_stat_PCAN,    KW_pval_PCAN    = stats.kruskal(Hg0_PCAN_Ice['ng/m3'],     Hg0_PCAN_OW['ng/m3'])

KW_stat_V1_17,   KW_pval_V1_17   = stats.kruskal(Hg0_Davis_V1_17['ng/m3'],  Hg0_V1_17_OW['ng/m3'])
KW_stat_V2_17,   KW_pval_V2_17   = stats.kruskal(Hg0_Casey_V2_17['ng/m3'],  Hg0_V2_17_OW['ng/m3'])
KW_stat_V3_17,   KW_pval_V3_17   = stats.kruskal(Hg0_V3_17_Ice['ng/m3'],    Hg0_V3_17_OW['ng/m3'])
KW_stat_V3_17M,  KW_pval_V3_17M  = stats.kruskal(Hg0_Mawson_V3_17['ng/m3'], Hg0_V3_17M_OW['ng/m3'])
KW_stat_V3_17D,  KW_pval_V3_17D  = stats.kruskal(Hg0_Davis_V3_17['ng/m3'],  Hg0_V3_17D_OW['ng/m3'])
KW_stat_V4_17,   KW_pval_V4_17   = stats.kruskal(Hg0_MQIsl_V4_17['ng/m3'],  Hg0_V4_17_OW['ng/m3'])

KW_stat_V1_18,   KW_pval_V1_18   = stats.kruskal(Hg0_Davis_V1_18['ng/m3'],  Hg0_V1_18_OW['ng/m3'])
KW_stat_V2_18,   KW_pval_V2_18   = stats.kruskal(Hg0_Casey_V2_18['ng/m3'],  Hg0_V2_18_OW['ng/m3'])
KW_stat_V3_18,   KW_pval_V3_18   = stats.kruskal(Hg0_V3_18_Ice['ng/m3'],    Hg0_V3_18_OW['ng/m3'])
KW_stat_V3_18M,  KW_pval_V3_18M  = stats.kruskal(Hg0_Mawson_V3_18['ng/m3'], Hg0_V3_18M_OW['ng/m3'])
KW_stat_V3_18D,  KW_pval_V3_18D  = stats.kruskal(Hg0_Davis_V3_18['ng/m3'],  Hg0_V3_18D_OW['ng/m3'])
KW_stat_V4_18,   KW_pval_V4_18   = stats.kruskal(Hg0_MQIsl_V4_18['ng/m3'],  Hg0_V4_18_OW['ng/m3'])

#------------------------------------------------------------------------------
#BUILD DATAFRAME FOR THE STATISTICAL RESULTS (VOYAGE)

# Build a pandas dataframe (Voyage Hg0)
dfHg_Stats = {'No_All':     [N_SIPEXII_All,      N_PCAN_All,      N_V1_17_All,      N_V2_17_All,      N_V3_17_All,      N_V3_17M_All,      N_V3_17D_All,      N_V4_17_All,      N_V1_18_All,      N_V2_18_All,      N_V3_18_All,      N_V3_18M_All,      N_V3_18D_All,      N_V4_18_All],
              'No_S':       [N_SIPEXII_S,        N_PCAN_S,        N_V1_17_S,        N_V2_17_S,        N_V3_17_S,        N_V3_17M_S,        N_V3_17D_S,        N_V4_17_S,        N_V1_18_S,        N_V2_18_S,        N_V3_18_S,        N_V3_18M_S,        N_V3_18D_S,        N_V4_18_S],
              'No_OW':      [N_SIPEXII_OW,       N_PCAN_OW,       N_V1_17_OW,       N_V2_17_OW,       N_V3_17_OW,       N_V3_17M_OW,       N_V3_17D_OW,       N_V4_17_OW,       N_V1_18_OW,       N_V2_18_OW,       N_V3_18_OW,       N_V3_18M_OW,       N_V3_18D_OW,       N_V4_18_OW],
              'Mean_All':   [SIPEXII_Mean_All,   PCAN_Mean_All,   V1_17_Mean_All,   V2_17_Mean_All,   V3_17_Mean_All,   V3_17M_Mean_All,   V3_17D_Mean_All,   V4_17_Mean_All,   V1_18_Mean_All,   V2_18_Mean_All,   V3_18_Mean_All,   V3_18M_Mean_All,   V3_18D_Mean_All,   V4_18_Mean_All],
              'Mean_S':     [SIPEXII_Mean_S,     PCAN_Mean_S,     V1_17_Mean_S,     V2_17_Mean_S,     V3_17_Mean_S,     V3_17M_Mean_S,     V3_17D_Mean_S,     V4_17_Mean_S,     V1_18_Mean_S,     V2_18_Mean_S,     V3_18_Mean_S,     V3_18M_Mean_S,     V3_18D_Mean_S,     V4_18_Mean_S],
              'Mean_OW':    [SIPEXII_Mean_OW,    PCAN_Mean_OW,    V1_17_Mean_OW,    V2_17_Mean_OW,    V3_17_Mean_OW,    V3_17M_Mean_OW,    V3_17D_Mean_OW,    V4_17_Mean_OW,    V1_18_Mean_OW,    V2_18_Mean_OW,    V3_18_Mean_OW,    V3_18M_Mean_OW,    V3_18D_Mean_OW,    V4_18_Mean_OW],
              'StDev_All':  [SIPEXII_std_All,    PCAN_std_All,    V1_17_std_All,    V2_17_std_All,    V3_17_std_All,    V3_17M_std_All,    V3_17D_std_All,    V4_17_std_All,    V1_18_std_All,    V2_18_std_All,    V3_18_std_All,    V3_18M_std_All,    V3_18D_std_All,    V4_18_std_All],
              'StDev_S':    [SIPEXII_std_S,      PCAN_std_S,      V1_17_std_S,      V2_17_std_S,      V3_17_std_S,      V3_17M_std_S,      V3_17D_std_S,      V4_17_std_S,      V1_18_std_S,      V2_18_std_S,      V3_18_std_S,      V3_18M_std_S,      V3_18D_std_S,      V4_18_std_S],
              'StDev_OW':   [SIPEXII_std_OW,     PCAN_std_OW,     V1_17_std_OW,     V2_17_std_OW,     V3_17_std_OW,     V3_17M_std_OW,     V3_17D_std_OW,     V4_17_std_OW,     V1_18_std_OW,     V2_18_std_OW,     V3_18_std_OW,     V3_18M_std_OW,     V3_18D_std_OW,     V4_18_std_OW],
              'Median_All': [SIPEXII_Median_All, PCAN_Median_All, V1_17_Median_All, V2_17_Median_All, V3_17_Median_All, V3_17M_Median_All, V3_17D_Median_All, V4_17_Median_All, V1_18_Median_All, V2_18_Median_All, V3_18_Median_All, V3_18M_Median_All, V3_18D_Median_All, V4_18_Median_All],
              'Median_S':   [SIPEXII_Median_S,   PCAN_Median_S,   V1_17_Median_S,   V2_17_Median_S,   V3_17_Median_S,   V3_17M_Median_S,   V3_17D_Median_S,   V4_17_Median_S,   V1_18_Median_S,   V2_18_Median_S,   V3_18_Median_S,   V3_18M_Median_S,   V3_18D_Median_S,   V4_18_Median_S],
              'Median_OW':  [SIPEXII_Median_OW,  PCAN_Median_OW,  V1_17_Median_OW,  V2_17_Median_OW,  V3_17_Median_OW,  V3_17M_Median_OW,  V3_17D_Median_OW,  V4_17_Median_OW,  V1_18_Median_OW,  V2_18_Median_OW,  V3_18_Median_OW,  V3_18M_Median_OW,  V3_18D_Median_OW,  V4_18_Median_OW],
              'MAD_All':    [SIPEXII_MAD_All,    PCAN_MAD_All,    V1_17_MAD_All,    V2_17_MAD_All,    V3_17_MAD_All,    V3_17M_MAD_All,    V3_17D_MAD_All,    V4_17_MAD_All,    V1_18_MAD_All,    V2_18_MAD_All,    V3_18_MAD_All,    V3_18M_MAD_All,    V3_18D_MAD_All,    V4_18_MAD_All],
              'MAD_S':      [SIPEXII_MAD_S,      PCAN_MAD_S,      V1_17_MAD_S,      V2_17_MAD_S,      V3_17_MAD_S,      V3_17M_MAD_S,      V3_17D_MAD_S,      V4_17_MAD_S,      V1_18_MAD_S,      V2_18_MAD_S,      V3_18_MAD_S,      V3_18M_MAD_S,      V3_18D_MAD_S,      V4_18_MAD_S],
              'MAD_OW':     [SIPEXII_MAD_OW,     PCAN_MAD_OW,     V1_17_MAD_OW,     V2_17_MAD_OW,     V3_17_MAD_OW,     V3_17M_MAD_OW,     V3_17D_MAD_OW,     V4_17_MAD_OW,     V1_18_MAD_OW,     V2_18_MAD_OW,     V3_18_MAD_OW,     V3_18M_MAD_OW,     V3_18D_MAD_OW,     V4_18_MAD_OW],
              'MIN_All':    [SIPEXII_MIN_All,    PCAN_MIN_All,    V1_17_MIN_All,    V2_17_MIN_All,    V3_17_MIN_All,    V3_17M_MIN_All,    V3_17D_MIN_All,    V4_17_MIN_All,    V1_18_MIN_All,    V2_18_MIN_All,    V3_18_MIN_All,    V3_18M_MIN_All,    V3_18D_MIN_All,    V4_18_MIN_All],
              'MIN_S':      [SIPEXII_MIN_S,      PCAN_MIN_S,      V1_17_MIN_S,      V2_17_MIN_S,      V3_17_MIN_S,      V3_17M_MIN_S,      V3_17D_MIN_S,      V4_17_MIN_S,      V1_18_MIN_S,      V2_18_MIN_S,      V3_18_MIN_S,      V3_18M_MIN_S,      V3_18D_MIN_S,      V4_18_MIN_S],
              'MIN_OW':     [SIPEXII_MIN_OW,     PCAN_MIN_OW,     V1_17_MIN_OW,     V2_17_MIN_OW,     V3_17_MIN_OW,     V3_17M_MIN_OW,     V3_17D_MIN_OW,     V4_17_MIN_OW,     V1_18_MIN_OW,     V2_18_MIN_OW,     V3_18_MIN_OW,     V3_18M_MIN_OW,     V3_18D_MIN_OW,     V4_18_MIN_OW],
              'MAX_All':    [SIPEXII_MAX_All,    PCAN_MAX_All,    V1_17_MAX_All,    V2_17_MAX_All,    V3_17_MAX_All,    V3_17M_MAX_All,    V3_17D_MAX_All,    V4_17_MAX_All,    V1_18_MAX_All,    V2_18_MAX_All,    V3_18_MAX_All,    V3_18M_MAX_All,    V3_18D_MAX_All,    V4_18_MAX_All],
              'MAX_S':      [SIPEXII_MAX_S,      PCAN_MAX_S,      V1_17_MAX_S,      V2_17_MAX_S,      V3_17_MAX_S,      V3_17M_MAX_S,      V3_17D_MAX_S,      V4_17_MAX_S,      V1_18_MAX_S,      V2_18_MAX_S,      V3_18_MAX_S,      V3_18M_MAX_S,      V3_18D_MAX_S,      V4_18_MAX_S],
              'MAX_OW':     [SIPEXII_MAX_OW,     PCAN_MAX_OW,     V1_17_MAX_OW,     V2_17_MAX_OW,     V3_17_MAX_OW,     V3_17M_MAX_OW,     V3_17D_MAX_OW,     V4_17_MAX_OW,     V1_18_MAX_OW,     V2_18_MAX_OW,     V3_18_MAX_OW,     V3_18M_MAX_OW,     V3_18D_MAX_OW,     V4_18_MAX_OW],
              '5P_All':     [SIPEXII_5P_All,     PCAN_5P_All,     V1_17_5P_All,     V2_17_5P_All,     V3_17_5P_All,     V3_17M_5P_All,     V3_17D_5P_All,     V4_17_5P_All,     V1_18_5P_All,     V2_18_5P_All,     V3_18_5P_All,     V3_18M_5P_All,     V3_18D_5P_All,     V4_18_5P_All],
              '5P_S':       [SIPEXII_5P_S,       PCAN_5P_S,       V1_17_5P_S,       V2_17_5P_S,       V3_17_5P_S,       V3_17M_5P_S,       V3_17D_5P_S,       V4_17_5P_S,       V1_18_5P_S,       V2_18_5P_S,       V3_18_5P_S,       V3_18M_5P_S,       V3_18D_5P_S,       V4_18_5P_S],
              '5P_OW':      [SIPEXII_5P_OW,      PCAN_5P_OW,      V1_17_5P_OW,      V2_17_5P_OW,      V3_17_5P_OW,      V3_17M_5P_OW,      V3_17D_5P_OW,      V4_17_5P_OW,      V1_18_5P_OW,      V2_18_5P_OW,      V3_18_5P_OW,      V3_18M_5P_OW,      V3_18D_5P_OW,      V4_18_5P_OW],
              '25P_All':    [SIPEXII_25P_All,    PCAN_25P_All,    V1_17_25P_All,    V2_17_25P_All,    V3_17_25P_All,    V3_17M_25P_All,    V3_17D_25P_All,    V4_17_25P_All,    V1_18_25P_All,    V2_18_25P_All,    V3_18_25P_All,    V3_18M_25P_All,    V3_18D_25P_All,    V4_18_25P_All],
              '25P_S':      [SIPEXII_25P_S,      PCAN_25P_S,      V1_17_25P_S,      V2_17_25P_S,      V3_17_25P_S,      V3_17M_25P_S,      V3_17D_25P_S,      V4_17_25P_S,      V1_18_25P_S,      V2_18_25P_S,      V3_18_25P_S,      V3_18M_25P_S,      V3_18D_25P_S,      V4_18_25P_S],
              '25P_OW':     [SIPEXII_25P_OW,     PCAN_25P_OW,     V1_17_25P_OW,     V2_17_25P_OW,     V3_17_25P_OW,     V3_17M_25P_OW,     V3_17D_25P_OW,     V4_17_25P_OW,     V1_18_25P_OW,     V2_18_25P_OW,     V3_18_25P_OW,     V3_18M_25P_OW,     V3_18D_25P_OW,     V4_18_25P_OW],
              '75P_All':    [SIPEXII_75P_All,    PCAN_75P_All,    V1_17_75P_All,    V2_17_75P_All,    V3_17_75P_All,    V3_17M_75P_All,    V3_17D_75P_All,    V4_17_75P_All,    V1_18_75P_All,    V2_18_75P_All,    V3_18_75P_All,    V3_18M_75P_All,    V3_18D_75P_All,    V4_18_75P_All],
              '75P_S':      [SIPEXII_75P_S,      PCAN_75P_S,      V1_17_75P_S,      V2_17_75P_S,      V3_17_75P_S,      V3_17M_75P_S,      V3_17D_75P_S,      V4_17_75P_S,      V1_18_75P_S,      V2_18_75P_S,      V3_18_75P_S,      V3_18M_75P_S,      V3_18D_75P_S,      V4_18_75P_S],
              '75P_OW':     [SIPEXII_75P_OW,     PCAN_75P_OW,     V1_17_75P_OW,     V2_17_75P_OW,     V3_17_75P_OW,     V3_17M_75P_OW,     V3_17D_75P_OW,     V4_17_75P_OW,     V1_18_75P_OW,     V2_18_75P_OW,     V3_18_75P_OW,     V3_18M_75P_OW,     V3_18D_75P_OW,     V4_18_75P_OW],
              '95P_All':    [SIPEXII_95P_All,    PCAN_95P_All,    V1_17_95P_All,    V2_17_95P_All,    V3_17_95P_All,    V3_17M_95P_All,    V3_17D_95P_All,    V4_17_95P_All,    V1_18_95P_All,    V2_18_95P_All,    V3_18_95P_All,    V3_18M_95P_All,    V3_18D_95P_All,    V4_18_95P_All],
              '95P_S':      [SIPEXII_95P_S,      PCAN_95P_S,      V1_17_95P_S,      V2_17_95P_S,      V3_17_95P_S,      V3_17M_95P_S,      V3_17D_95P_S,      V4_17_95P_S,      V1_18_95P_S,      V2_18_95P_S,      V3_18_95P_S,      V3_18M_95P_S,      V3_18D_95P_S,      V4_18_95P_S],
              '95P_OW':     [SIPEXII_95P_OW,     PCAN_95P_OW,     V1_17_95P_OW,     V2_17_95P_OW,     V3_17_95P_OW,     V3_17M_95P_OW,     V3_17D_95P_OW,     V4_17_95P_OW,     V1_18_95P_OW,     V2_18_95P_OW,     V3_18_95P_OW,     V3_18M_95P_OW,     V3_18D_95P_OW,     V4_18_95P_OW],
              'IQR_All':    [SIPEXII_IQR_All,    PCAN_IQR_All,    V1_17_IQR_All,    V2_17_IQR_All,    V3_17_IQR_All,    V3_17M_IQR_All,    V3_17D_IQR_All,    V4_17_IQR_All,    V1_18_IQR_All,    V2_18_IQR_All,    V3_18_IQR_All,    V3_18M_IQR_All,    V3_18D_IQR_All,    V4_18_IQR_All],
              'IQR_S':      [SIPEXII_IQR_S,      PCAN_IQR_S,      V1_17_IQR_S,      V2_17_IQR_S,      V3_17_IQR_S,      V3_17M_IQR_S,      V3_17D_IQR_S,      V4_17_IQR_S,      V1_18_IQR_S,      V2_18_IQR_S,      V3_18_IQR_S,      V3_18M_IQR_S,      V3_18D_IQR_S,      V4_18_IQR_S],
              'IQR_OW':     [SIPEXII_IQR_OW,     PCAN_IQR_OW,     V1_17_IQR_OW,     V2_17_IQR_OW,     V3_17_IQR_OW,     V3_17M_IQR_OW,     V3_17D_IQR_OW,     V4_17_IQR_OW,     V1_18_IQR_OW,     V2_18_IQR_OW,     V3_18_IQR_OW,     V3_18M_IQR_OW,     V3_18D_IQR_OW,     V4_18_IQR_OW]}
dfHg_Stats = pd.DataFrame(dfHg_Stats, columns = ['No_All','No_S','No_OW','Mean_All','Mean_S','Mean_OW','StDev_All','StDev_S','StDev_OW','Median_All','Median_S','Median_OW','MAD_All','MAD_S','MAD_OW','MIN_All','MIN_S','MIN_OW','MAX_All','MAX_S','MAX_OW','5P_All','5P_S','5P_OW','25P_All','25P_S','25P_OW','75P_All','75P_S','75P_OW','95P_All','95P_S','95P_OW','IQR_All','IQR_S','IQR_OW'],index = ['SIPEXII','PCAN','V1_17','V2_17','V3_17','V3_17M','V3_17D','V4_17','V1_18','V2_18','V3_18','V3_18M','V3_18D','V4_18'])
#dfHg_Stats = dfHg_Stats.T
dfHg_Stats.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_Stats.csv')

# Build a pandas dataframe (Seasonal Met)
dfHg_Met = {'Mean_WT':  [LateSpring_Mean_WT_All, EarlySummer_Mean_WT_All, LateSummer_Mean_WT_All, Summer_Mean_WT_All, Autumn_Mean_WT_All, LateSpring_Mean_WT_SI, EarlySummer_Mean_WT_SI, LateSummer_Mean_WT_SI, Summer_Mean_WT_SI, Autumn_Mean_WT_SI, LateSpring_Mean_WT_OW, EarlySummer_Mean_WT_OW, LateSummer_Mean_WT_OW, Summer_Mean_WT_OW, Autumn_Mean_WT_OW],
            'StDev_WT': [LateSpring_std_WT_All,  EarlySummer_std_WT_All,  LateSummer_std_WT_All,  Summer_std_WT_All,  Autumn_std_WT_All,  LateSpring_std_WT_SI,  EarlySummer_std_WT_SI,  LateSummer_std_WT_SI,  Summer_std_WT_SI,  Autumn_std_WT_SI,  LateSpring_std_WT_OW,  EarlySummer_std_WT_OW,  LateSummer_std_WT_OW,  Summer_std_WT_OW,  Autumn_std_WT_OW],
            'Mean_AT':  [LateSpring_Mean_AT_All, EarlySummer_Mean_AT_All, LateSummer_Mean_AT_All, Summer_Mean_AT_All, Autumn_Mean_AT_All, LateSpring_Mean_AT_SI, EarlySummer_Mean_AT_SI, LateSummer_Mean_AT_SI, Summer_Mean_AT_SI, Autumn_Mean_AT_SI, LateSpring_Mean_AT_OW, EarlySummer_Mean_AT_OW, LateSummer_Mean_AT_OW, Summer_Mean_AT_OW, Autumn_Mean_AT_OW],
            'StDev_AT': [LateSpring_std_AT_All,  EarlySummer_std_AT_All,  LateSummer_std_AT_All,  Summer_std_AT_All,  Autumn_std_AT_All,  LateSpring_std_AT_SI,  EarlySummer_std_AT_SI,  LateSummer_std_AT_SI,  Summer_std_AT_SI,  Autumn_std_AT_SI,  LateSpring_std_AT_OW,  EarlySummer_std_AT_OW,  LateSummer_std_AT_OW,  Summer_std_AT_OW,  Autumn_std_AT_OW],
            'Mean_WS':  [LateSpring_Mean_WS_All, EarlySummer_Mean_WS_All, LateSummer_Mean_WS_All, Summer_Mean_WS_All, Autumn_Mean_WS_All, LateSpring_Mean_WS_SI, EarlySummer_Mean_WS_SI, LateSummer_Mean_WS_SI, Summer_Mean_WS_SI, Autumn_Mean_WS_SI, LateSpring_Mean_WS_OW, EarlySummer_Mean_WS_OW, LateSummer_Mean_WS_OW, Summer_Mean_WS_OW, Autumn_Mean_WS_OW],
            'StDev_WS': [LateSpring_std_WS_All,  EarlySummer_std_WS_All,  LateSummer_std_WS_All,  Summer_std_WS_All,  Autumn_std_WS_All,  LateSpring_std_WS_SI,  EarlySummer_std_WS_SI,  LateSummer_std_WS_SI,  Summer_std_WS_SI,  Autumn_std_WS_SI,  LateSpring_std_WS_OW,  EarlySummer_std_WS_OW,  LateSummer_std_WS_OW,  Summer_std_WS_OW,  Autumn_std_WS_OW],
            'Mean_SR':  [LateSpring_Mean_SR_All, EarlySummer_Mean_SR_All, LateSummer_Mean_SR_All, Summer_Mean_SR_All, Autumn_Mean_SR_All, LateSpring_Mean_SR_SI, EarlySummer_Mean_SR_SI, LateSummer_Mean_SR_SI, Summer_Mean_SR_SI, Autumn_Mean_SR_SI, LateSpring_Mean_SR_OW, EarlySummer_Mean_SR_OW, LateSummer_Mean_SR_OW, Summer_Mean_SR_OW, Autumn_Mean_SR_OW],
            'StDev_SR': [LateSpring_std_SR_All,  EarlySummer_std_SR_All,  LateSummer_std_SR_All,  Summer_std_SR_All,  Autumn_std_SR_All,  LateSpring_std_SR_SI,  EarlySummer_std_SR_SI,  LateSummer_std_SR_SI,  Summer_std_SR_SI,  Autumn_std_SR_SI,  LateSpring_std_SR_OW,  EarlySummer_std_SR_OW,  LateSummer_std_SR_OW,  Summer_std_SR_OW,  Autumn_std_SR_OW]}
dfHg_Met = pd.DataFrame(dfHg_Met, columns = ['Mean_WT','StDev_WT','Mean_AT','StDev_AT','Mean_WS','StDev_WS','Mean_SR','StDev_SR'], index = ['LateSpring_All','EarlySummer_All','LateSummer_All','Summer_All','Autumn_All','LateSpring_SI','EarlySummer_SI','LateSummer_SI','Summer_SI','Autumn_SI','LateSpring_OW','EarlySummer_OW','LateSummer_OW','Summer_OW','Autumn_OW'])
dfHg_Met.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_Met.csv')

# Build a pandas dataframe (Hg0 variability ice vs open water)
dfHg_Varia = {'Welches (stat)':   [WT_stat_SIPEXII, WT_stat_PCAN, WT_stat_V1_17, WT_stat_V2_17, WT_stat_V3_17, WT_stat_V3_17M, WT_stat_V3_17D, WT_stat_V4_18, WT_stat_V1_18, WT_stat_V2_18, WT_stat_V3_18, WT_stat_V3_18M, WT_stat_V3_18D, WT_stat_V4_18],
              'Welches (pval)':   [WT_pval_SIPEXII, WT_pval_PCAN, WT_pval_V1_17, WT_pval_V2_17, WT_pval_V3_17, WT_pval_V3_17M, WT_pval_V3_17D, WT_pval_V4_18, WT_pval_V1_18, WT_pval_V2_18, WT_pval_V3_18, WT_pval_V3_18M, WT_pval_V3_18D, WT_pval_V4_18],
              'KS-Test (stat)':   [KS_stat_SIPEXII, KS_stat_PCAN, KS_stat_V1_17, KS_stat_V2_17, KS_stat_V3_17, KS_stat_V3_17M, KS_stat_V3_17D, KS_stat_V4_18, KS_stat_V1_18, KS_stat_V2_18, KS_stat_V3_18, KS_stat_V3_18M, KS_stat_V3_18D, KS_stat_V4_18],
              'KS-Test (pval)':   [KS_pval_SIPEXII, KS_pval_PCAN, KS_pval_V1_17, KS_pval_V2_17, KS_pval_V3_17, KS_pval_V3_17M, KS_pval_V3_17D, KS_pval_V4_18, KS_pval_V1_18, KS_pval_V2_18, KS_pval_V3_18, KS_pval_V3_18M, KS_pval_V3_18D, KS_pval_V4_18],
              'MW U-Test (stat)': [MW_stat_SIPEXII, MW_stat_PCAN, MW_stat_V1_17, MW_stat_V2_17, MW_stat_V3_17, MW_stat_V3_17M, MW_stat_V3_17D, MW_stat_V4_18, MW_stat_V1_18, MW_stat_V2_18, MW_stat_V3_18, MW_stat_V3_18M, MW_stat_V3_18D, MW_stat_V4_18],
              'MW U-Test (pval)': [MW_pval_SIPEXII, MW_pval_PCAN, MW_pval_V1_17, MW_pval_V2_17, MW_pval_V3_17, MW_pval_V3_17M, MW_pval_V3_17D, MW_pval_V4_18, MW_pval_V1_18, MW_pval_V2_18, MW_pval_V3_18, MW_pval_V3_18M, MW_pval_V3_18D, MW_pval_V4_18],
              'KW H-Test (stat)': [KW_stat_SIPEXII, KW_stat_PCAN, KW_stat_V1_17, KW_stat_V2_17, KW_stat_V3_17, KW_stat_V3_17M, KW_stat_V3_17D, KW_stat_V4_18, KW_stat_V1_18, KW_stat_V2_18, KW_stat_V3_18, KW_stat_V3_18M, KW_stat_V3_18D, KW_stat_V4_18],
              'KW H-Test (pval)': [KW_pval_SIPEXII, KW_pval_PCAN, KW_pval_V1_17, KW_pval_V2_17, KW_pval_V3_17, KW_pval_V3_17M, KW_pval_V3_17D, KW_pval_V4_18, KW_pval_V1_18, KW_pval_V2_18, KW_pval_V3_18, KW_pval_V3_18M, KW_pval_V3_18D, KW_pval_V4_18]}
dfHg_Varia = pd.DataFrame(dfHg_Varia, columns = ['Welches (stat)','Welches (pval)','KS-Test (stat)','KS-Test (pval)','MW U-Test (stat)','MW U-Test (pval)','KW H-Test (stat)','KW H-Test (pval)'], index = ['SIPEXII','PCAN','V1_17','V2_17','V3_17','V3_17M','V3_17D','V4_17','V1_18','V2_18','V3_18','V3_18M','V3_18D','V4_18'])
dfHg_Varia.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_Variability.csv')

#------------------------------------------------------------------------------
#BUILD DATAFRAME FOR THE STATISTICAL RESULTS (SEASONAL)

# Build a pandas dataframe (Seasonal Hg0)
dfHgSeasonal = {'Mean_All':   [LateSpring_Mean_All,   EarlySummer_Mean_All,   LateSummer_Mean_All,   Summer_Mean_All,   Autumn_Mean_All],
                'Mean_SI':    [LateSpring_Mean_SI,    EarlySummer_Mean_SI,    LateSummer_Mean_SI,    Summer_Mean_SI,    Autumn_Mean_SI],
                'Mean_OW':    [LateSpring_Mean_OW,    EarlySummer_Mean_OW,    LateSummer_Mean_OW,    Summer_Mean_OW,    Autumn_Mean_OW],
                'StDev_All':  [LateSpring_std_All,    EarlySummer_std_All,    LateSummer_std_All,    Summer_std_All,    Autumn_std_All],
                'StDev_SI':   [LateSpring_std_SI,     EarlySummer_std_SI,     LateSummer_std_SI,     Summer_std_SI,     Autumn_std_SI],
                'StDev_OW':   [LateSpring_std_OW,     EarlySummer_std_OW,     LateSummer_std_OW,     Summer_std_OW,     Autumn_std_OW],
                'Median_All': [LateSpring_Median_All, EarlySummer_Median_All, LateSummer_Median_All, Summer_Median_All, Autumn_Median_All],
                'Median_SI':  [LateSpring_Median_SI,  EarlySummer_Median_SI,  LateSummer_Median_SI,  Summer_Median_SI,  Autumn_Median_SI],
                'Median_OW':  [LateSpring_Median_OW,  EarlySummer_Median_OW,  LateSummer_Median_OW,  Summer_Median_OW,  Autumn_Median_OW],
                'MAD_All':    [LateSpring_MAD_All,    EarlySummer_MAD_All,    LateSummer_MAD_All,    Summer_MAD_All,    Autumn_MAD_All],
                'MAD_SI':     [LateSpring_MAD_SI,     EarlySummer_MAD_SI,     LateSummer_MAD_SI,     Summer_MAD_SI,     Autumn_MAD_SI],
                'MAD_OW':     [LateSpring_MAD_OW,     EarlySummer_MAD_OW,     LateSummer_MAD_OW,     Summer_MAD_OW,     Autumn_MAD_OW]}
dfHgSeasonal = pd.DataFrame(dfHgSeasonal, columns = ['Mean_All','Mean_SI','Mean_OW','StDev_All','StDev_SI','StDev_OW','Median_All','Median_SI','Median_OW','MAD_All','MAD_SI','MAD_OW'],index = ['LateSpring','EarlySummer','LateSummer','Summer','Autumn'])
dfHgSeasonal.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/HgSeasonal.csv')

# Build a pandas dataframe (Seasonal Met)
dfWeatherParameters = {'Mean_WT':  [LateSpring_Mean_WT_All, EarlySummer_Mean_WT_All, LateSummer_Mean_WT_All, Summer_Mean_WT_All, Autumn_Mean_WT_All, LateSpring_Mean_WT_SI, EarlySummer_Mean_WT_SI, LateSummer_Mean_WT_SI, Summer_Mean_WT_SI, Autumn_Mean_WT_SI, LateSpring_Mean_WT_OW, EarlySummer_Mean_WT_OW, LateSummer_Mean_WT_OW, Summer_Mean_WT_OW, Autumn_Mean_WT_OW],
                       'StDev_WT': [LateSpring_std_WT_All,  EarlySummer_std_WT_All,  LateSummer_std_WT_All,  Summer_std_WT_All,  Autumn_std_WT_All,  LateSpring_std_WT_SI,  EarlySummer_std_WT_SI,  LateSummer_std_WT_SI,  Summer_std_WT_SI,  Autumn_std_WT_SI,  LateSpring_std_WT_OW,  EarlySummer_std_WT_OW,  LateSummer_std_WT_OW,  Summer_std_WT_OW,  Autumn_std_WT_OW],
                       'Mean_AT':  [LateSpring_Mean_AT_All, EarlySummer_Mean_AT_All, LateSummer_Mean_AT_All, Summer_Mean_AT_All, Autumn_Mean_AT_All, LateSpring_Mean_AT_SI, EarlySummer_Mean_AT_SI, LateSummer_Mean_AT_SI, Summer_Mean_AT_SI, Autumn_Mean_AT_SI, LateSpring_Mean_AT_OW, EarlySummer_Mean_AT_OW, LateSummer_Mean_AT_OW, Summer_Mean_AT_OW, Autumn_Mean_AT_OW],
                       'StDev_AT': [LateSpring_std_AT_All,  EarlySummer_std_AT_All,  LateSummer_std_AT_All,  Summer_std_AT_All,  Autumn_std_AT_All,  LateSpring_std_AT_SI,  EarlySummer_std_AT_SI,  LateSummer_std_AT_SI,  Summer_std_AT_SI,  Autumn_std_AT_SI,  LateSpring_std_AT_OW,  EarlySummer_std_AT_OW,  LateSummer_std_AT_OW,  Summer_std_AT_OW,  Autumn_std_AT_OW],
                       'Mean_WS':  [LateSpring_Mean_WS_All, EarlySummer_Mean_WS_All, LateSummer_Mean_WS_All, Summer_Mean_WS_All, Autumn_Mean_WS_All, LateSpring_Mean_WS_SI, EarlySummer_Mean_WS_SI, LateSummer_Mean_WS_SI, Summer_Mean_WS_SI, Autumn_Mean_WS_SI, LateSpring_Mean_WS_OW, EarlySummer_Mean_WS_OW, LateSummer_Mean_WS_OW, Summer_Mean_WS_OW, Autumn_Mean_WS_OW],
                       'StDev_WS': [LateSpring_std_WS_All,  EarlySummer_std_WS_All,  LateSummer_std_WS_All,  Summer_std_WS_All,  Autumn_std_WS_All,  LateSpring_std_WS_SI,  EarlySummer_std_WS_SI,  LateSummer_std_WS_SI,  Summer_std_WS_SI,  Autumn_std_WS_SI,  LateSpring_std_WS_OW,  EarlySummer_std_WS_OW,  LateSummer_std_WS_OW,  Summer_std_WS_OW,  Autumn_std_WS_OW],
                       'Mean_SR':  [LateSpring_Mean_SR_All, EarlySummer_Mean_SR_All, LateSummer_Mean_SR_All, Summer_Mean_SR_All, Autumn_Mean_SR_All, LateSpring_Mean_SR_SI, EarlySummer_Mean_SR_SI, LateSummer_Mean_SR_SI, Summer_Mean_SR_SI, Autumn_Mean_SR_SI, LateSpring_Mean_SR_OW, EarlySummer_Mean_SR_OW, LateSummer_Mean_SR_OW, Summer_Mean_SR_OW, Autumn_Mean_SR_OW],
                       'StDev_SR': [LateSpring_std_SR_All,  EarlySummer_std_SR_All,  LateSummer_std_SR_All,  Summer_std_SR_All,  Autumn_std_SR_All,  LateSpring_std_SR_SI,  EarlySummer_std_SR_SI,  LateSummer_std_SR_SI,  Summer_std_SR_SI,  Autumn_std_SR_SI,  LateSpring_std_SR_OW,  EarlySummer_std_SR_OW,  LateSummer_std_SR_OW,  Summer_std_SR_OW,  Autumn_std_SR_OW]}
dfWeatherParameters = pd.DataFrame(dfWeatherParameters, columns = ['Mean_WT','StDev_WT','Mean_AT','StDev_AT','Mean_WS','StDev_WS','Mean_SR','StDev_SR'], index = ['LateSpring_All','EarlySummer_All','LateSummer_All','Summer_All','Autumn_All','LateSpring_SI','EarlySummer_SI','LateSummer_SI','Summer_SI','Autumn_SI','LateSpring_OW','EarlySummer_OW','LateSummer_OW','Summer_OW','Autumn_OW'])
dfWeatherParameters.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/WeatherParameters.csv')

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()

gs = gridspec.GridSpec(nrows=3,
                       ncols=4, 
                       figure=fig, 
                       width_ratios= [0.25, 0.25, 0.25, 0.25],
                       height_ratios=[0.3, 0.3, 0.3],
                       hspace=0.5)

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
#ax3.spines["right"].set_position(("axes", 1.22))
ax3.spines["left"].set_color('blue')

# Shade time on station
arrive1 = datetime(2017,11,14) # Arrive Davis (V1 17)
depart1 = datetime(2017,11,21) # Depart Davis (V1 17)
ax1.axvspan(arrive1, depart1, color='lawngreen', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.75, "Davis", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(DMedian_V1_17.index, DMedian_V1_17['ng/m3'], marker='None', ls='-', c='black', label ="V1 (2017-18)\n median: "+str("%5.2f"%(V1_17_Median_All))+" $\pm$ "+str("%5.2f"%(V1_17_MAD_All))+" ng/m$^3$")
ax2.plot(Met_V1_17_DM.index, Met_V1_17_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_V1_17_DM.index, SI_V1_17_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_V1_17.index,  D5P_V1_17['ng/m3'],  'b-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_V1_17.index, D95P_V1_17['ng/m3'], 'b-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_V1_17.index, D25P_V1_17['ng/m3'], D75P_V1_17['ng/m3'], facecolor='blue', alpha=0.7) # fill the distribution

# UL1 = DMedian_V1_17['ng/m3'] + DSTD_V1_17['ng/m3'] # find the upper limit
# LL1 = DMedian_V1_17['ng/m3'] - DSTD_V1_17['ng/m3'] # find the lower limit

# ax1.plot(DMedian_V1_17.index, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_V1_17.index, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_V1_17.index, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('blue')
ax1.tick_params(axis='y', which='both', colors='blue')
ax1.set_ylim(0,2)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V1 (Davis)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# Label for CAMMPCAN (2017-18)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax1.text(-0.35, 0.5, " CAMMPCAN (2017-18) ", transform=ax1.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[0,1])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
#ax3.spines["right"].set_position(("axes", 1.22))

# Shade time on station
arrive1 = datetime(2017,12,21) # Arrive Casey (V2 17)
depart1 = datetime(2017,12,22) # Depart Casey (V2 17)
arrive2 = datetime(2017,12,24) # Arrive Casey (V2 17)
depart2 = datetime(2018,1,6)   # Depart Casey (V2 17)
ax1.axvspan(arrive1, depart1, color='pink', alpha=0.4, lw=0) # dark shade
ax1.axvspan(arrive2, depart2, color='pink', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.75, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive2 + (depart2 - arrive2)/3, 1.75, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
#ax1.plot(DMean_V2_17.index, DMean_V2_17['ng/m3'], marker='o', ls='--', c='blue', label ="Mean: "+str("%5.2f"%(V2_17_Mean))+" $\pm$ "+str("%5.2f"%(V2_17_std)))
ax1.plot(DMedian_V2_17.index, DMedian_V2_17['ng/m3'], marker='None', ls='-', c='black', label ="V2 (2017-18)\n median: "+str("%5.2f"%(V2_17_Median_All))+" $\pm$ "+str("%5.2f"%(V2_17_MAD_All))+" ng/m$^3$")
ax2.plot(Met_V2_17_DM.index, Met_V2_17_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_V2_17_DM.index, SI_V2_17_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_V2_17.index,  D5P_V2_17['ng/m3'],  'b-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_V2_17.index, D95P_V2_17['ng/m3'], 'b-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_V2_17.index, D25P_V2_17['ng/m3'], D75P_V2_17['ng/m3'], facecolor='blue', alpha=0.7) # fill the distribution

# UL2 = DMedian_V2_17['ng/m3'] + DSTD_V2_17['ng/m3'] # find the upper limit
# LL2 = DMedian_V2_17['ng/m3'] - DSTD_V2_17['ng/m3']# find the lower limit

# ax1.plot(DMedian_V2_17.index, UL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_V2_17.index, LL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_V2_17.index, UL2, LL2, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('blue')
ax1.tick_params(axis='y', which='both', colors='blue')
ax1.set_ylim(0,2)
ax1.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)


# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V2 (Casey)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[0,2])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
#ax3.spines["right"].set_position(("axes", 1.22))

# Shade time on station
arrive1 = datetime(2018,2,1)  # Arrive Mawson (V3 17)
depart1 = datetime(2018,2,18) # Depart Mawson (V3 17)
arrive2 = datetime(2018,1,27) # Arrive Davis (V3 17)
depart2 = datetime(2018,1,30) # Depart Davis (V3 17)
arrive3 = datetime(2018,2,19) # Arrive Davis (V3 17)
depart3 = datetime(2018,2,21) # Depart Davis (V3 17)
ax1.axvspan(arrive1, depart1, color='orange',    alpha=0.4, lw=0) # dark shade
ax1.axvspan(arrive2, depart2, color='lawngreen', alpha=0.4, lw=0)  # dark shade
ax1.axvspan(arrive3, depart3, color='lawngreen', alpha=0.4, lw=0)  # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.75, "Mawson", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive2 + (depart2 - arrive2)/2, 1.75, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive3 + (datetime(2018,2,23) - arrive3)/2, 1.75, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(DMedian_V3_17M.index, DMedian_V3_17M['ng/m3'], marker='None', ls='-', c='black', label ="V3 (2017-18)\n median: "+str("%5.2f"%(V3_17M_Median_All))+" $\pm$ "+str("%5.2f"%(V3_17M_MAD_All))+" ng/m$^3$")
#ax1.plot(DMedian_V3_17M.index, DMedian_V3_17M['ng/m3'], marker='o', ls='--', c='blue', label ="V3 (2017-18)\n median (Mawson): "+str("%5.2f"%(V3_17M_Median_All))+" $\pm$ "+str("%5.2f"%(V3_17M_MAD_All))+" ng/m$^3$\n median (Davis):     "+str("%5.2f"%(V3_17D_Median_All))+" $\pm$ "+str("%5.2f"%(V3_17D_MAD_All))+" ng/m$^3$")
ax2.plot(Met_V3_17_DM.index, Met_V3_17_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_V3_17_DM.index, SI_V3_17_DM['Sea Ice Conc (0-1)']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_V3_17M.index,  D5P_V3_17M['ng/m3'],  'b-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_V3_17M.index, D95P_V3_17M['ng/m3'], 'b-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_V3_17M.index, D25P_V3_17M['ng/m3'], D75P_V3_17M['ng/m3'], facecolor='blue', alpha=0.7) # fill the distribution

# UL3 = DMedian_V3_17M['ng/m3'] + DSTD_V3_17M['ng/m3'] # find the upper limit
# LL3 = DMedian_V3_17M['ng/m3'] - DSTD_V3_17M['ng/m3'] # find the lower limit

# ax1.plot(DMedian_V3_17M.index, UL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_V3_17M.index, LL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_V3_17M.index, UL3, LL3, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('blue')
ax1.tick_params(axis='y', which='both', colors='blue')
ax1.set_ylim(0,2)
ax1.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V3 (Mawson & Davis)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 4
ax1 = plt.subplot(gs[0,3])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax2.spines["right"].set_color('magenta')
ax3.spines["right"].set_position(("axes", 1.22))
ax3.spines["right"].set_color('grey')

# Shade time on station
arrive1 = datetime(2018,3,13) # Arrive Maquarie Island (V4 17)
depart1 = datetime(2018,3,22) # Depart Maquarie Island (V4 17)
ax1.axvspan(arrive1, depart1, color='slateblue', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.75, "Maquarie Island", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
#ax1.plot(DMean_V4_17.index, DMean_V4_17['ng/m3'], marker='o', ls='--', c='blue', label ="Mean: "+str("%5.2f"%(V4_17_Mean))+" $\pm$ "+str("%5.2f"%(V4_17_std)))
ax1.plot(DMedian_V4_17.index, DMedian_V4_17['ng/m3'], marker='None', ls='-', c='black', label ="V4 (2017-18)\n median: "+str("%5.2f"%(V4_17_Median_All))+" $\pm$ "+str("%5.2f"%(V4_17_MAD_All))+" ng/m$^3$")
ax2.plot(Met_V4_17_DM.index, Met_V4_17_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_V3_17_DM.index, SI_V3_17_DM['Sea Ice Conc (0-1)']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_V4_17.index,  D5P_V4_17['ng/m3'],  'b-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_V4_17.index, D95P_V4_17['ng/m3'], 'b-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_V4_17.index, D25P_V4_17['ng/m3'], D75P_V4_17['ng/m3'], facecolor='blue', alpha=0.7) # fill the distribution

# UL4 = DMedian_V4_17['ng/m3'] + DSTD_V4_17['ng/m3'] # find the upper limit
# LL4 = DMedian_V4_17['ng/m3'] - DSTD_V4_17['ng/m3'] # find the lower limit

# ax1.plot(DMedian_V4_17.index, UL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_V4_17.index, LL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_V4_17.index, UL4, LL4, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2018,3,8),datetime(2018,3,24)) # all dates

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('blue')
ax1.tick_params(axis='y', which='both', colors='blue')
ax1.set_ylim(0,2)
ax1.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
#ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
#ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V4 (Macquarie Island)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 5
ax1 = plt.subplot(gs[1,0])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
#ax3.spines["right"].set_position(("axes", 1.22))
ax3.spines["left"].set_color('red')

# Shade time on station
arrive1 = datetime(2018,11,7)  # Arrive Davis (V1 18)
depart1 = datetime(2018,11,15) # Depart Davis (V1 18)
ax1.axvspan(arrive1, depart1, color='lawngreen', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.75, "Davis", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
#ax1.plot(DMean_V1_18_avg.index, DMean_V1_18['ng/m3'], marker='o', ls='--', c='red', label ="Mean: "+str("%5.2f"%(V1_18_Mean))+" $\pm$ "+str("%5.2f"%(V1_18_std)))
ax1.plot(DMedian_V1_18.index, DMedian_V1_18['ng/m3'], marker='None', ls='-', c='black', label ="V1 (2018-19)\n median: "+str("%5.2f"%(V1_18_Median_All))+" $\pm$ "+str("%5.2f"%(V1_18_MAD_All))+" ng/m$^3$")
ax2.plot(Met_V1_18_DM.index, Met_V1_18_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_V1_18_DM.index, SI_V1_18_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_V1_18.index,  D5P_V1_18['ng/m3'],  'r-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_V1_18.index, D95P_V1_18['ng/m3'], 'r-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_V1_18.index, D25P_V1_18['ng/m3'], D75P_V1_18['ng/m3'], facecolor='red', alpha=0.7) # fill the distribution

# UL5 = DMedian_V1_18['ng/m3'] + DSTD_V1_18['ng/m3'] # find the upper limit
# LL5 = DMedian_V1_18['ng/m3'] - DSTD_V1_18['ng/m3'] # find the lower limit

# ax1.plot(DMedian_V1_18.index, UL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_V1_18.index, LL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_V1_18.index, UL5, LL5, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', which='both', colors='red')
ax1.set_ylim(0,2)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
#plt.title('V1 (2018-19)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# Label for CAMMPCAN (2018-19)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax1.text(-0.35, 0.5, " CAMMPCAN (2018-19) ", transform=ax1.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 6
ax1 = plt.subplot(gs[1,1])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
#ax3.spines["right"].set_position(("axes", 1.22))

# Shade time on station
arrive1 = datetime(2018,12,14) # Arrive Casey (V2 18)
depart1 = datetime(2018,12,28) # Depart Casey (V2 18)
ax1.axvspan(arrive1, depart1, color='pink', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.75, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
#ax1.plot(DMean_V2_18_avg.index, DMean_V2_18['ng/m3'], marker='o', ls='--', c='red', label ="Mean: "+str("%5.2f"%(V2_18_Mean))+" $\pm$ "+str("%5.2f"%(V2_18_std)))
ax1.plot(DMedian_V2_18.index, DMedian_V2_18['ng/m3'], marker='None', ls='-', c='black', label ="V2 (2018-19)\n median: "+str("%5.2f"%(V2_18_Median_All))+" $\pm$ "+str("%5.2f"%(V2_18_MAD_All))+" ng/m$^3$")
ax2.plot(Met_V2_18_DM.index, Met_V2_18_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_V2_18_DM.index, SI_V2_18_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_V2_18.index,  D5P_V2_18['ng/m3'],  'r-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_V2_18.index, D95P_V2_18['ng/m3'], 'r-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_V2_18.index, D25P_V2_18['ng/m3'], D75P_V2_18['ng/m3'], facecolor='red', alpha=0.7) # fill the distribution

# UL6 = DMedian_V2_18['ng/m3'] + DSTD_V2_18['ng/m3'] # find the upper limit
# LL6 = DMedian_V2_18['ng/m3'] - DSTD_V2_18['ng/m3'] # find the lower limit

# ax1.plot(DMedian_V2_18.index, UL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_V2_18.index, LL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_V2_18.index, UL6, LL6, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', which='both', colors='red')
ax1.set_ylim(0,2)
ax1.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
#plt.title('V2 (2018-19)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 7
ax1 = plt.subplot(gs[1,2])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
#ax3.spines["right"].set_position(("axes", 1.22))

# Shade time on station
arrive1 = datetime(2019,1,29) # Arrive Mawson (V3 18)
depart1 = datetime(2019,2,9) # Depart Mawson (V3 18)
arrive2 = datetime(2019,1,25) # Arrive Davis (V3 18)
depart2 = datetime(2019,1,27) # Depart Davis (V3 18)
arrive3 = datetime(2019,2,17) # Arrive Davis (V3 18)
depart3 = datetime(2019,2,19) # Depart Davis (V3 18)
ax1.axvspan(arrive1, depart1, color='orange',    alpha=0.4, lw=0) # dark shade
ax1.axvspan(arrive2, depart2, color='lawngreen', alpha=0.4, lw=0) # dark shade
ax1.axvspan(arrive3, depart3, color='lawngreen', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (datetime(2019,2,11) - arrive1)/2, 1.75, "Mawson", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(datetime(2019,1,24), 1.75, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive3 + (depart3 - arrive3)/2, 1.75, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax1.plot(DMedian_V3_18M.index, DMedian_V3_18M['ng/m3'], marker='None', ls='-', c='black', label ="V3 (2018-19)\n median: "+str("%5.2f"%(V3_18M_Median_All))+" $\pm$ "+str("%5.2f"%(V3_18M_MAD_All))+" ng/m$^3$")
#ax1.plot(DMedian_V3_18M.index, DMedian_V3_18M['ng/m3'], marker='o', ls='--', c='red', label ="V3 (2018-19)\n median (Mawson): "+str("%5.2f"%(V3_18M_Median_All))+" $\pm$ "+str("%5.2f"%(V3_18M_MAD_All))+" ng/m$^3$\n median (Davis):     "+str("%5.2f"%(V3_18D_Median_All))+" $\pm$ "+str("%5.2f"%(V3_18D_MAD_All))+" ng/m$^3$")
ax2.plot(Met_V3_18_DM.index, Met_V3_18_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_V3_18_DM.index, SI_V3_18_DM['Sea Ice Conc (0-1)']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_V3_18M.index,  D5P_V3_18M['ng/m3'],  'r-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_V3_18M.index, D95P_V3_18M['ng/m3'], 'r-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_V3_18M.index, D25P_V3_18M['ng/m3'], D75P_V3_18M['ng/m3'], facecolor='red', alpha=0.7) # fill the distribution

# UL7 = DMedian_V3_18M['ng/m3'] + DSTD_V3_18M['ng/m3'] # find the upper limit
# LL7 = DMedian_V3_18M['ng/m3'] - DSTD_V3_18M['ng/m3'] # find the lower limit

# ax1.plot(DMedian_V3_18M.index, UL7, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_V3_18M.index, LL7, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_V3_18M.index, UL7, LL7, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', which='both', colors='red')
ax1.set_ylim(0,2)
ax1.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
#plt.title('V3 (2018-19)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 8
ax1 = plt.subplot(gs[1,3])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax2.spines["right"].set_color('magenta')
ax3.spines["right"].set_position(("axes", 1.22))
ax3.spines["right"].set_color('grey')

# Shade time on station
arrive1 = datetime(2019,3,9)  # Arrive Maquarie Island (V4 18)
depart1 = datetime(2019,3,22) # Depart Maquarie Island (V4 18)
ax1.axvspan(arrive1, depart1, color='slateblue', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.85, "Maquarie Island", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
#ax1.plot(Mean_V4_18.index, DMean_V4_18['ng/m3'], marker='o', ls='--', c='red', label ="Mean: "+str("%5.2f"%(V4_18_Mean))+" $\pm$ "+str("%5.2f"%(V4_18_std)))
ax1.plot(DMedian_V4_18.index, DMedian_V4_18['ng/m3'], marker='None', ls='-', c='black', label ="V4 (2018-19)\n median: "+str("%5.2f"%(V4_18_Median_All))+" $\pm$ "+str("%5.2f"%(V4_18_MAD_All))+" ng/m$^3$")
ax2.plot(Met_V4_18_DM.index, Met_V4_18_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_V3_18_DM.index, SI_V3_18_DM['Sea Ice Conc (0-1)']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_V4_18.index,  D5P_V4_18['ng/m3'],  'r-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_V4_18.index, D95P_V4_18['ng/m3'], 'r-', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_V4_18.index, D25P_V4_18['ng/m3'], D75P_V4_18['ng/m3'], facecolor='red', alpha=0.7) # fill the distribution

# UL8 = DMedian_V4_18['ng/m3'] + DSTD_V4_18['ng/m3'] # find the upper limit
# LL8 = DMedian_V4_18['ng/m3'] - DSTD_V4_18['ng/m3'] # find the lower limit

# ax1.plot(DMedian_V4_18.index, UL8, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_V4_18.index, LL8, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_V4_18.index, UL8, LL8, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2019,3,4),datetime(2019,3,26)) # all dates

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', which='both', colors='red')
ax1.set_ylim(0,2)
ax1.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
#ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
#plt.title('V4 (2018-19)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 9
ax1 = plt.subplot(gs[2,0])
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax2.spines["right"].set_color('magenta')
ax3.spines["right"].set_position(("axes", 1.22))
ax3.spines["right"].set_color('grey')
ax3.spines["left"].set_color('green')

# Plot the variables
#ax1.plot(DMean_SIPEXII.index, DMean_SIPEXII['ng/m3'], marker='o', ls='--', c='green', label ="Mean: "+str("%5.2f"%(SIPEXII_Mean))+" $\pm$ "+str("%5.2f"%(SIPEXII_std)))
ax1.plot(DMedian_SIPEXII.index, DMedian_SIPEXII['ng/m3'], marker='None', ls='-', c='black', label ="SIPEXII (2012)\n median: "+str("%5.2f"%(SIPEXII_Median_All))+" $\pm$ "+str("%5.2f"%(SIPEXII_MAD_All))+" ng/m$^3$")
ax2.plot(Met_SIPEXII_DM.index, Met_SIPEXII_DM['latitude'], ls='--', c='magenta', label ='Latitude')
ax3.plot(SI_SIPEXII_DM.index, SI_SIPEXII_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the percentiles
ax1.plot(D5P_SIPEXII.index,  D5P_SIPEXII['ng/m3'],  ls='-', c='green', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_SIPEXII.index, D95P_SIPEXII['ng/m3'], ls='-', c='green', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_SIPEXII.index, D25P_SIPEXII['ng/m3'], D75P_SIPEXII['ng/m3'], facecolor='green', alpha=0.7) # fill the distribution

# UL9 = DMedian_SIPEXII['ng/m3'] + DSTD_SIPEXII['ng/m3'] # find the upper limit
# LL9 = DMedian_SIPEXII['ng/m3'] - DSTD_SIPEXII['ng/m3'] # find the lower limit

# ax1.plot(DMedian_SIPEXII.index, UL9, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_SIPEXII.index, LL9, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_SIPEXII.index, UL9, LL9, facecolor='green', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=10)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('green')
ax1.tick_params(axis='y', which='both', colors='green')
ax1.set_ylim(0,2)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
#ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,140)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
#plt.title('SIPEXII (2012)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# Label for SIPEXII (2012)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax1.text(-0.35, 0.5, "       SIPEXII (2012)       ", transform=ax1.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 10
ax1 = plt.subplot(gs[2,2])
ax2 = ax1.twinx()
ax2.spines["left"].set_color('orange')
ax2.spines["right"].set_color('magenta')

# Plot the variables
#ax1.plot(DMean_PCAN.index, DMean_PCAN['ng/m3'], marker='o', ls='--', c='orange', label ="Mean: "+str("%5.2f"%(PCAN_Mean))+" $\pm$ "+str("%5.2f"%(PCAN_std)))
ax1.plot(DMedian_PCAN.index, DMedian_PCAN['ng/m3'], marker='None', ls='-', c='black', label ="PCAN (2017)\n median: "+str("%5.2f"%(PCAN_Median_All))+" $\pm$ "+str("%5.2f"%(PCAN_MAD_All))+" ng/m$^3$")
ax2.plot(Met_PCAN_DM.index, Met_PCAN_DM['latitude'], ls='--', c='magenta', label ='Latitude')

# Plot the percentiles
ax1.plot(D5P_PCAN.index,  D5P_PCAN['ng/m3'],  ls='-', c='orange', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.plot(D95P_PCAN.index, D95P_PCAN['ng/m3'], ls='-', c='orange', linewidth=1, alpha=0.5, label='_nolegend_')
ax1.fill_between(D25P_PCAN.index, D25P_PCAN['ng/m3'], D75P_PCAN['ng/m3'], facecolor='orange', alpha=0.7) # fill the distribution

# UL10 = DMedian_PCAN['ng/m3'] + DSTD_PCAN['ng/m3'] # find the upper limit
# LL10 = DMedian_PCAN['ng/m3'] - DSTD_PCAN['ng/m3'] # find the lower limit

# ax1.plot(DMedian_PCAN.index, UL10, ls='-', c='orange', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# ax1.plot(DMedian_PCAN.index, LL10, ls='-', c='orange', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# ax1.fill_between(DMedian_PCAN.index, UL10, LL10, facecolor='orange', alpha=0.3) # fill the distribution

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.label.set_color('orange')
ax1.tick_params(axis='y', which='both', colors='orange')
ax1.set_ylim(0,2)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('magenta')
ax2.tick_params(axis='y', which='both', colors='magenta')
ax2.set_ylim(-69,-42)
#ax2.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)

#Plot the legend and title
#plt.title('PCAN (2017)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# Label for SIPEXII (2012)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax1.text(-0.35, 0.5, "        PCAN (2012)        ", transform=ax1.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Custom Legend
custom_lines = [Line2D([0], [0], color='blue',  lw=4),
                Line2D([0], [0], color='red',   lw=4),
                Line2D([0], [0], color='green', lw=4),
                Line2D([0], [0], color='orange', lw=4),
                Line2D([0], [0], color='magenta', lw=4),
                Line2D([0], [0], color='grey',  lw=4)]
fig.legend(custom_lines, ['Hg$^0$ (CAMMPCAN 2017-18)', 'Hg$^0$ (CAMMPCAN 2018-19)', 'Hg$^0$ (SIPEXII)', 'Hg$^0$ (PCAN)', 'Latitude ($^\circ$S)','Sea Ice Concentration (%)'], loc='upper left', bbox_to_anchor=(0.775, 0.275))
