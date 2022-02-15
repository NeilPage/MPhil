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

#---------
# BrO
#---------
BrO_V1_17  = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv',index_col=0)       # BrO V1 (2017/18)
BrO_V2_17  = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv',index_col=0)       # BrO V2 (2017/18)
BrO_V3_17M = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv',index_col=0)       # BrO V3 (2017/18)
BrO_V3_17D = BrO_V3_17M

BrO_V1_18  = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv',index_col=0)       # BrO V1 (2018/19)
BrO_V2_18  = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv',index_col=0)       # BrO V2 (2018/19)
BrO_V3_18M = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv',index_col=0)       # BrO V3 (2018/19)
BrO_V3_18D = BrO_V3_18M

BrO_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv',index_col=0) # BrO SIPEXII (2012)

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
SI_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv', index_col=0)
SI_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv', index_col=0)
SI_V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_17_M_SeaIce.csv', index_col=0)

SI_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv', index_col=0)
SI_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv', index_col=0)
SI_V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_18_M_SeaIce.csv', index_col=0)
SI_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv', index_col=0)

#--------------
# O3
#--------------
O3_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv', index_col=0)
O3_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V2_O3_1min.csv', index_col=0)
O3_V3_17M  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V3_O3_1min.csv', index_col=0)
O3_V3_17D  = O3_V3_17M
O3_V4_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V4_O3_1min.csv', index_col=0)

O3_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V1_O3_1min.csv', index_col=0)
O3_V1_18.rename(columns={'O3':'O3_(ppb)'},inplace=True) # rename the column from 'O3' to 'O3_(ppb)'
O3_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V2_O3_1min.csv', index_col=0)
O3_V2_18.rename(columns={'O3':'O3_(ppb)'},inplace=True) # rename the column from 'O3' to 'O3_(ppb)'
O3_V2_18   = O3_V2_18.loc[~O3_V2_18.index.duplicated(keep='first')] # remove duplicate values from the .csv file
O3_V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V3_O3_1min.csv', index_col=0)
O3_V3_18.rename(columns={'O3':'O3_(ppb)'},inplace=True) # rename the column from 'O3' to 'O3_(ppb)'
O3_V3_18M  = O3_V3_18.loc[~O3_V3_18.index.duplicated(keep='first')] # remove duplicate values from the .csv file
O3_V3_18D  = O3_V3_18M
O3_V4_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V4_O3_1min.csv', index_col=0)
O3_V4_18.rename(columns={'O3':'O3_(ppb)'},inplace=True) # rename the column from 'O3' to 'O3_(ppb)'
O3_V4_18   = O3_V4_18.loc[~O3_V4_18.index.duplicated(keep='first')] # remove duplicate values from the .csv file

O3_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_O3/SIPEXII_O3_QAQC.csv', index_col=0)
O3_SIPEXII = O3_SIPEXII.loc[~O3_SIPEXII.index.duplicated(keep='first')] # remove duplicate values from the .csv file

#------------------------------------------------------------------------------
# FILTER THE BrO DATA FOR RELATIVE ERROR 

#----------------
# BrO (Retrieval)
#----------------
# Calculate the Relative Error (>=0.6)
Filter1_BrO = BrO_V1_17['err_surf_vmr']  / BrO_V1_17['surf_vmr(ppmv)']
Filter2_BrO = BrO_V2_17['err_surf_vmr']  / BrO_V2_17['surf_vmr(ppmv)']
Filter3_BrO = BrO_V3_17M['err_surf_vmr'] / BrO_V3_17M['surf_vmr(ppmv)']
Filter4_BrO = BrO_V3_17D['err_surf_vmr'] / BrO_V3_17D['surf_vmr(ppmv)']

Filter5_BrO = BrO_V1_18['err_surf_vmr']  / BrO_V1_18['surf_vmr(ppmv)']
Filter6_BrO = BrO_V2_18['err_surf_vmr']  / BrO_V2_18['surf_vmr(ppmv)']
Filter7_BrO = BrO_V3_18M['err_surf_vmr'] / BrO_V3_18M['surf_vmr(ppmv)']
Filter8_BrO = BrO_V3_18D['err_surf_vmr'] / BrO_V3_18D['surf_vmr(ppmv)']

Filter9_BrO = BrO_SIPEXII['err_surf_vmr'] / BrO_SIPEXII['surf_vmr(ppmv)']

# Apply the filter
V1_17F      = Filter1_BrO < 0.6
BrO_V1_17   = BrO_V1_17[V1_17F]

V2_17F      = Filter2_BrO < 0.6
BrO_V2_17   = BrO_V2_17[V2_17F]

V3_17MF     = Filter3_BrO < 0.6
BrO_V3_17M  = BrO_V3_17M[V3_17MF]

V3_17DF     = Filter4_BrO < 0.6
BrO_V3_17D  = BrO_V3_17D[V3_17DF]

V1_18F      = Filter5_BrO < 0.6
BrO_V1_18   = BrO_V1_18[V1_18F]

V2_18F      = Filter6_BrO < 0.6
BrO_V2_18   = BrO_V2_18[V2_18F]

V3_18MF     = Filter7_BrO < 0.6
BrO_V3_18M  = BrO_V3_18M[V3_18MF]

V3_18DF     = Filter8_BrO < 0.6
BrO_V3_18D  = BrO_V3_18D[V3_18DF]

SIPEXIIF    = Filter9_BrO < 0.6
BrO_SIPEXII = BrO_SIPEXII[SIPEXIIF]

#------------------------------------------------------------------------------
# Set the date

#--------------
# Hg0
#--------------
Hg0_V1_17.index   = pd.to_datetime(Hg0_V1_17.index,   dayfirst=True)
Hg0_V2_17.index   = pd.to_datetime(Hg0_V2_17.index,   dayfirst=True)
Hg0_V3_17M.index  = pd.to_datetime(Hg0_V3_17M.index,  dayfirst=True)
Hg0_V3_17D.index  = (pd.to_datetime(Hg0_V3_17D.index, dayfirst=True) + timedelta(hours=2))
Hg0_V4_17.index   = pd.to_datetime(Hg0_V4_17.index,   dayfirst=True)

Hg0_V1_18.index   = pd.to_datetime(Hg0_V1_18.index,   dayfirst=True)
Hg0_V2_18.index   = pd.to_datetime(Hg0_V2_18.index,   dayfirst=True)
Hg0_V3_18M.index  = pd.to_datetime(Hg0_V3_18M.index,  dayfirst=True)
Hg0_V3_18D.index  = (pd.to_datetime(Hg0_V3_18D.index, dayfirst=True) + timedelta(hours=2))
Hg0_V4_18.index   = pd.to_datetime(Hg0_V4_18.index,   dayfirst=True)

Hg0_SIPEXII.index = pd.to_datetime(Hg0_SIPEXII.index, dayfirst=True)
Hg0_PCAN.index    = pd.to_datetime(Hg0_PCAN.index,    dayfirst=True)

#---------
# BrO
#---------
BrO_V1_17.index   = (pd.to_datetime(BrO_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_17.index   = (pd.to_datetime(BrO_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_17M.index  = (pd.to_datetime(BrO_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_17D.index  = (pd.to_datetime(BrO_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_V1_18.index   = (pd.to_datetime(BrO_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_18.index   = (pd.to_datetime(BrO_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_18M.index  = (pd.to_datetime(BrO_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_18D.index  = (pd.to_datetime(BrO_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_SIPEXII.index = (pd.to_datetime(BrO_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

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
SI_V1_17.index  = (pd.to_datetime(SI_V1_17.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SI_V2_17.index  = (pd.to_datetime(SI_V2_17.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SI_V3_17.index  = (pd.to_datetime(SI_V3_17.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

SI_V1_18.index  = (pd.to_datetime(SI_V1_18.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SI_V2_18.index  = (pd.to_datetime(SI_V2_18.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SI_V3_18.index  = (pd.to_datetime(SI_V3_18.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

SI_SIPEXII.index = (pd.to_datetime(SI_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#--------------
# O3
#--------------
O3_V1_17.index   = (pd.to_datetime(O3_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
O3_V2_17.index   = (pd.to_datetime(O3_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
O3_V3_17M.index  = (pd.to_datetime(O3_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
O3_V3_17D.index  = (pd.to_datetime(O3_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
O3_V4_17.index   = (pd.to_datetime(O3_V4_17.index,   dayfirst=True) + timedelta(hours=11)) # Macquarie Island is UT+11

O3_V1_18.index   = (pd.to_datetime(O3_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
O3_V2_18.index   = (pd.to_datetime(O3_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
O3_V3_18M.index  = (pd.to_datetime(O3_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
O3_V3_18D.index  = (pd.to_datetime(O3_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
O3_V4_18.index   = (pd.to_datetime(O3_V4_18.index,   dayfirst=True) + timedelta(hours=11)) # Macquarie Island is UT+11
                    
O3_SIPEXII.index = (pd.to_datetime(O3_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#------------------------------------------------------------------------------
# FIX UP PCAN O3

O3_PCAN = Met_PCAN

# Replace erroneous values with nan
O3_PCAN['Ozone1 (ppb)'] = O3_PCAN['Ozone1 (ppb)'].replace(-999.9,  np.nan)
O3_PCAN['Ozone2 (ppb)'] = O3_PCAN['Ozone2 (ppb)'].replace(-999.9,  np.nan)

# Calculate O3 average for PCAN
O3_PCAN['O3_(ppb)'] =  O3_PCAN[['Ozone1 (ppb)', 'Ozone2 (ppb)']].mean(axis=1)  

#------------------------------------------------------------------------------
# CLEAN UP THE O3 DATA (REMOVE ERRONEOUS DATA)

# O3 (positive values only)
filter1   = O3_V1_17['O3_(ppb)']  >= 0
O3_V1_17  = O3_V1_17[filter1]

filter1   = O3_V2_17['O3_(ppb)']  >= 0
O3_V2_17  = O3_V2_17[filter1]

filter1   = O3_V3_17M['O3_(ppb)'] >= 0
O3_V3_17M = O3_V3_17M[filter1]

filter1   = O3_V3_17D['O3_(ppb)'] >= 0
O3_V3_17D = O3_V3_17D[filter1]

filter1   = O3_V4_17['O3_(ppb)']  >= 0
O3_V4_17  = O3_V4_17[filter1]

filter1  = O3_PCAN['O3_(ppb)'] >= 0
O3_PCAN  = O3_PCAN[filter1]

# O3 (get rid of stupidly high values)
filter2   = O3_V1_17['O3_(ppb)']  <= 50
O3_V1_17  = O3_V1_17[filter2]

filter2   = O3_V2_17['O3_(ppb)']  <= 50
O3_V2_17  = O3_V2_17[filter2]

filter2   = O3_V3_17M['O3_(ppb)'] <= 50
O3_V3_17M = O3_V3_17M[filter2]

filter2   = O3_V3_17D['O3_(ppb)'] <= 50
O3_V3_17D = O3_V3_17D[filter2]

filter2   = O3_V4_17['O3_(ppb)']  <= 50
O3_V4_17  = O3_V4_17[filter2]

filter2   = O3_PCAN['O3_(ppb)']   <= 50
O3_PCAN   = O3_PCAN[filter2]

#------------------------------------------------------------------------------
# OZONE SCREEN

# Set the filter
F_O3_V1_17   = O3_V1_17['O3_(ppb)']
F_O3_V2_17   = O3_V2_17['O3_(ppb)']
F_O3_V3_17M  = O3_V3_17M['O3_(ppb)']
F_O3_V3_17D  = O3_V3_17D['O3_(ppb)']
F_O3_V4_17   = O3_V4_17['O3_(ppb)']

F_O3_V1_18   = O3_V1_18['O3_(ppb)']
F_O3_V2_18   = O3_V2_18['O3_(ppb)']
F_O3_V3_18M  = O3_V3_18M['O3_(ppb)']
F_O3_V3_18D  = O3_V3_18D['O3_(ppb)']
F_O3_V4_18   = O3_V4_18['O3_(ppb)']

F_O3_PCAN    = O3_PCAN['O3_(ppb)']
F_O3_SIPEXII = O3_SIPEXII['O3_(ppb)']

# Apply the filter (Remove values when O3 <2 ppb)
OzoneF_V1_17   = F_O3_V1_17   > 2
O3_V1_17       = O3_V1_17[OzoneF_V1_17]

OzoneF_V2_17   = F_O3_V2_17   > 2
O3_V2_17       = O3_V2_17[OzoneF_V2_17]

OzoneF_V3_17M  = F_O3_V3_17M  > 2
O3_V3_17M      = O3_V3_17M[OzoneF_V3_17M]

OzoneF_V3_17D  = F_O3_V3_17D  > 2
O3_V3_17D      = O3_V3_17D[OzoneF_V3_17D]

OzoneF_V4_17   = F_O3_V4_17  > 2
O3_V4_17       = O3_V4_17[OzoneF_V4_17]

OzoneF_V1_18   = F_O3_V1_18   > 2
O3_V1_18       = O3_V1_18[OzoneF_V1_18]

OzoneF_V2_18   = F_O3_V2_18   > 2
O3_V2_18       = O3_V2_18[OzoneF_V2_18]

OzoneF_V3_18M  = F_O3_V3_18M  > 2
O3_V3_18M      = O3_V3_18M[OzoneF_V3_18M]

OzoneF_V3_18D  = F_O3_V3_18D  > 2
O3_V3_18D      = O3_V3_18D[OzoneF_V3_18D]

OzoneF_V4_18   = F_O3_V4_18  > 2
O3_V4_18       = O3_V4_18[OzoneF_V4_18]

OzoneF_PCAN    = F_O3_PCAN > 2
O3_PCAN        = O3_PCAN[OzoneF_PCAN]

OzoneF_SIPEXII = F_O3_SIPEXII > 2
O3_SIPEXII     = O3_SIPEXII[OzoneF_SIPEXII]

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
# BrO
Davis      = (BrO_V1_17.index >= start_date) & (BrO_V1_17.index < end_date)
BrO_V1_17  = BrO_V1_17[Davis]
# Met
Davis      = (Met_V1_17.index >= start_date) & (Met_V1_17.index < end_date)
Met_V1_17  = Met_V1_17[Davis]
# O3
Davis      = (O3_V1_17.index >= start_date)  & (O3_V1_17.index < end_date)
O3_V1_17   = O3_V1_17[Davis]

#-----------------------------
# V2_17 Casey (13 Dec 2017 - 11 Jan 2018) (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018 on station)
#-----------------------------
start_date = '2017-12-13'
end_date   = '2018-01-12'
# Hg0
Casey      = (Hg0_V2_17.index >= start_date) & (Hg0_V2_17.index < end_date)
Hg0_V2_17  = Hg0_V2_17[Casey]
# BrO
Casey      = (BrO_V2_17.index >= start_date) & (BrO_V2_17.index < end_date)
BrO_V2_17  = BrO_V2_17[Casey]
# Met
Casey      = (Met_V2_17.index >= start_date) & (Met_V2_17.index < end_date)
Met_V2_17  = Met_V2_17[Casey]
# O3
Casey      = (O3_V2_17.index >= start_date)  & (O3_V2_17.index < end_date)
O3_V2_17   = O3_V2_17[Casey]

#-----------------------------
# V3_17 Mawson (16 Jan - 6 Mar 2018) (1-17 Feb 2018 on station)
#-----------------------------
start_date = '2018-01-16'
end_date   = '2018-03-07'
# Hg0
Mawson     = (Hg0_V3_17M.index >= start_date) & (Hg0_V3_17M.index < end_date)
Hg0_V3_17M = Hg0_V3_17M[Mawson]
# BrO
Mawson     = (BrO_V3_17M.index >= start_date) & (BrO_V3_17M.index < end_date)
BrO_V3_17M = BrO_V3_17M[Mawson]
# Met
Mawson     = (Met_V3_17M.index >= start_date) & (Met_V3_17M.index < end_date)
Met_V3_17M = Met_V3_17M[Mawson]
# O3
Mawson     = (O3_V3_17M.index >= start_date)  & (O3_V3_17M.index < end_date)
O3_V3_17M  = O3_V3_17M[Mawson]

#-----------------------------
# V3_17 Davis (16 Jan - 6 Mar 2018) (27-30 Jan 2018 and 19-21 Feb 2018 on station)
#-----------------------------
start_date = '2018-01-16'
end_date   = '2018-03-07'
# Hg0
Mawson     = (Hg0_V3_17D.index >= start_date) & (Hg0_V3_17D.index < end_date)
Hg0_V3_17D = Hg0_V3_17D[Mawson]
# BrO
Mawson     = (BrO_V3_17D.index >= start_date) & (BrO_V3_17D.index < end_date)
BrO_V3_17D = BrO_V3_17D[Mawson]
# Met
Mawson     = (Met_V3_17D.index >= start_date) & (Met_V3_17D.index < end_date)
Met_V3_17D = Met_V3_17D[Mawson]
# O3
Mawson     = (O3_V3_17D.index >= start_date)  & (O3_V3_17D.index < end_date)
O3_V3_17D  = O3_V3_17D[Mawson]

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
# O3
MQIsl      = (O3_V4_17.index >= start_date)  & (O3_V4_17.index < end_date)
O3_V4_17   = O3_V4_17[MQIsl]

#-----------------------------
# V1_18 Davis (25 Oct - 28 Nov 2018) (7-15 Nov 2018 on station)
#-----------------------------
start_date = '2018-10-25'
end_date   = '2018-11-29'
# Hg0
Davis      = (Hg0_V1_18.index >= start_date) & (Hg0_V1_18.index < end_date)
Hg0_V1_18  = Hg0_V1_18[Davis]
# BrO
Davis      = (BrO_V1_18.index >= start_date) & (BrO_V1_18.index < end_date)
BrO_V1_18  = BrO_V1_18[Davis]
# Met
Davis      = (Met_V1_18.index >= start_date) & (Met_V1_18.index < end_date)
Met_V1_18  = Met_V1_18[Davis]
# O3
Davis      = (O3_V1_18.index >= start_date)  & (O3_V1_18.index < end_date)
O3_V1_18   = O3_V1_18[Davis]

#-----------------------------
# V2_18 Casey (6 Dec 2018 - 7 Jan 2019) (15-30 Dec 2018 on station)
#-----------------------------
start_date = '2018-12-06'
end_date   = '2019-01-08'
# Hg0
Casey      = (Hg0_V2_18.index >= start_date) & (Hg0_V2_18.index < end_date)
Hg0_V2_18  = Hg0_V2_18[Casey]
# BrO
Casey      = (BrO_V2_18.index >= start_date) & (BrO_V2_18.index < end_date)
BrO_V2_18  = BrO_V2_18[Casey]
# Met
Casey      = (Met_V2_18.index >= start_date) & (Met_V2_18.index < end_date)
Met_V2_18  = Met_V2_18[Casey]
# O3
Casey      = (O3_V2_18.index >= start_date)  & (O3_V2_18.index < end_date)
O3_V2_18   = O3_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (13 Jan - 1 Mar 2019) (30 Jan - 9 Feb 2019)
#-----------------------------
start_date = '2019-01-13'
end_date   = '2019-03-2'
# Hg0
Mawson     = (Hg0_V3_18M.index >= start_date) & (Hg0_V3_18M.index < end_date)
Hg0_V3_18M = Hg0_V3_18M[Mawson]
# BrO
Mawson     = (BrO_V3_18M.index >= start_date) & (BrO_V3_18M.index < end_date)
BrO_V3_18M = BrO_V3_18M[Mawson]
# Met
Mawson     = (Met_V3_18M.index >= start_date) & (Met_V3_18M.index < end_date)
Met_V3_18M = Met_V3_18M[Mawson]
# O3
Mawson     = (O3_V3_18M.index >= start_date)  & (O3_V3_18M.index < end_date)
O3_V3_18M  = O3_V3_18M[Mawson]

#-----------------------------
# V3_18 Davis (13 Jan - 1 Mar 2019) (26-28 Jan 2019 and 19-20 Feb 2019 on station)
#-----------------------------
start_date = '2019-01-13'
end_date   = '2019-03-2'
# Hg0
Mawson     = (Hg0_V3_18D.index >= start_date) & (Hg0_V3_18D.index < end_date)
Hg0_V3_18D = Hg0_V3_18D[Mawson]
# BrO
Mawson     = (BrO_V3_18D.index >= start_date) & (BrO_V3_18D.index < end_date)
BrO_V3_18D = BrO_V3_18D[Mawson]
# Met
Mawson     = (Met_V3_18D.index >= start_date) & (Met_V3_18D.index < end_date)
Met_V3_18D = Met_V3_18D[Mawson]
# O3
Mawson     = (O3_V3_18D.index >= start_date)  & (O3_V3_18D.index < end_date)
O3_V3_18D  = O3_V3_18D[Mawson]

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
# O3
MQIsl      = (O3_V4_18.index >= start_date)  & (O3_V4_18.index < end_date)
O3_V4_18   = O3_V4_18[MQIsl]

#-----------------------------
# SIPEXII (14 Sep to 16 Nov 2012) (23 Sep to 11 Nov 2012 close to Antarctica)
#-----------------------------
start_date  = '2012-09-14'
end_date    = '2012-11-16'
# Hg0
SIPEX       = (Hg0_SIPEXII.index >= start_date) & (Hg0_SIPEXII.index < end_date)
Hg0_SIPEXII = Hg0_SIPEXII[SIPEX]
# BrO
SIPEX       = (BrO_SIPEXII.index >= start_date) & (BrO_SIPEXII.index < end_date)
BrO_SIPEXII = BrO_SIPEXII[SIPEX]
# Met
SIPEX       = (Met_SIPEXII.index >= start_date) & (Met_SIPEXII.index < end_date)
Met_SIPEXII = Met_SIPEXII[SIPEX]
# O3
SIPEX       = (O3_SIPEXII.index >= start_date)  & (O3_SIPEXII.index < end_date)
O3_SIPEXII  = O3_SIPEXII[SIPEX]

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
# # O3
PCAN       = (O3_PCAN.index >= start_date) & (O3_PCAN.index < end_date)
O3_PCAN    = O3_PCAN[PCAN]

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
# BrO
Davis           = (BrO_V1_17.index >= start_date) & (BrO_V1_17.index < end_date)
BrO_Davis_V1_17 = BrO_V1_17[Davis]
# Met
Davis           = (Met_V1_17.index >= start_date) & (Met_V1_17.index < end_date)
Met_Davis_V1_17 = Met_V1_17[Davis]
# O3
Davis           = (O3_V1_17.index >= start_date)  & (O3_V1_17.index < end_date)
O3_Davis_V1_17  = O3_V1_17[Davis]

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
# BrO
Casey1          = (BrO_V2_17.index >= start_date1) & (BrO_V2_17.index < end_date1)
Casey2          = (BrO_V2_17.index >= start_date2) & (BrO_V2_17.index < end_date2)
BrO_Casey_1     = BrO_V2_17[Casey1]
BrO_Casey_2     = BrO_V2_17[Casey2]
BrO_Casey_V2_17 = pd.concat([BrO_Casey_1,BrO_Casey_2], axis =0)
# Met
Casey1          = (Met_V2_17.index >= start_date1) & (Met_V2_17.index < end_date1)
Casey2          = (Met_V2_17.index >= start_date2) & (Met_V2_17.index < end_date2)
Met_Casey_1     = Met_V2_17[Casey1]
Met_Casey_2     = Met_V2_17[Casey2]
Met_Casey_V2_17 = pd.concat([Met_Casey_1,Met_Casey_2], axis =0)
# O3
Casey1          = (O3_V2_17.index >= start_date1) & (O3_V2_17.index < end_date1)
Casey2          = (O3_V2_17.index >= start_date2) & (O3_V2_17.index < end_date2)
O3_Casey_1      = O3_V2_17[Casey1]
O3_Casey_2      = O3_V2_17[Casey2]
O3_Casey_V2_17  = pd.concat([O3_Casey_1,O3_Casey_2], axis =0)

#-----------------------------
# V3_17 Mawson (1-17 Feb 2018)
#-----------------------------
start_date    = '2018-02-01'
end_date      = '2018-02-18'
# Hg0
Mawson           = (Hg0_V3_17M.index >= start_date) & (Hg0_V3_17M.index < end_date)
Hg0_Mawson_V3_17 = Hg0_V3_17M[Mawson]
# BrO
Mawson           = (BrO_V3_17M.index >= start_date) & (BrO_V3_17M.index < end_date)
BrO_Mawson_V3_17 = BrO_V3_17M[Mawson]
# Met
Mawson           = (Met_V3_17M.index >= start_date) & (Met_V3_17M.index < end_date)
Met_Mawson_V3_17 = Met_V3_17M[Mawson]
# O3
Mawson           = (O3_V3_17M.index >= start_date)  & (O3_V3_17M.index < end_date)
O3_Mawson_V3_17  = O3_V3_17M[Mawson]

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
# BrO
Davis1          = (BrO_V3_17D.index >= start_date1) & (BrO_V3_17D.index < end_date1)
Davis2          = (BrO_V3_17D.index >= start_date2) & (BrO_V3_17D.index < end_date2)
BrO_Davis_1     = BrO_V3_17D[Davis1]
BrO_Davis_2     = BrO_V3_17D[Davis2]
BrO_Davis_V3_17 = pd.concat([BrO_Davis_1,BrO_Davis_2], axis =0)
# Met
Davis1          = (Met_V3_17D.index >= start_date1) & (Met_V3_17D.index < end_date1)
Davis2          = (Met_V3_17D.index >= start_date2) & (Met_V3_17D.index < end_date2)
Met_Davis_1     = Met_V3_17D[Davis1]
Met_Davis_2     = Met_V3_17D[Davis2]
Met_Davis_V3_17 = pd.concat([Met_Davis_1,Met_Davis_2], axis =0)
# O3
Davis1          = (O3_V3_17D.index >= start_date1) & (O3_V3_17D.index < end_date1)
Davis2          = (O3_V3_17D.index >= start_date2) & (O3_V3_17D.index < end_date2)
O3_Davis_1      = O3_V3_17D[Davis1]
O3_Davis_2      = O3_V3_17D[Davis2]
O3_Davis_V3_17  = pd.concat([O3_Davis_1,O3_Davis_2], axis =0)

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
# O3
MQIsl           = (O3_V4_17.index >= start_date)  & (O3_V4_17.index < end_date)
O3_MQIsl_V4_17  = O3_V4_17[MQIsl]

#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
#-----------------------------
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# Hg0
Davis           = (Hg0_V1_18.index >= start_date) & (Hg0_V1_18.index < end_date)
Hg0_Davis_V1_18 = Hg0_V1_18[Davis]
# BrO
Davis           = (BrO_V1_18.index >= start_date) & (BrO_V1_18.index < end_date)
BrO_Davis_V1_18 = BrO_V1_18[Davis]
# Met
Davis           = (Met_V1_18.index >= start_date) & (Met_V1_18.index < end_date)
Met_Davis_V1_18 = Met_V1_18[Davis]
# O3
Davis           = (O3_V1_18.index >= start_date)  & (O3_V1_18.index < end_date)
O3_Davis_V1_18  = O3_V1_18[Davis]

#-----------------------------
# V2_18 Casey (15-30 Dec 2018)
#-----------------------------
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# Hg0
Casey           = (Hg0_V2_18.index >= start_date) & (Hg0_V2_18.index < end_date)
Hg0_Casey_V2_18 = Hg0_V2_18[Casey]
# BrO
Casey           = (BrO_V2_18.index >= start_date) & (BrO_V2_18.index < end_date)
BrO_Casey_V2_18 = BrO_V2_18[Casey]
# Met
Casey           = (Met_V2_18.index >= start_date) & (Met_V2_18.index < end_date)
Met_Casey_V2_18 = Met_V2_18[Casey]
# O3
Casey           = (O3_V2_18.index >= start_date)  & (O3_V2_18.index < end_date)
O3_Casey_V2_18  = O3_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#-----------------------------
start_date    = '2019-01-30'
end_date      = '2019-02-10'
# Hg0
Mawson           = (Hg0_V3_18M.index >= start_date) & (Hg0_V3_18M.index < end_date)
Hg0_Mawson_V3_18 = Hg0_V3_18M[Mawson]
# BrO
Mawson           = (BrO_V3_18M.index >= start_date) & (BrO_V3_18M.index < end_date)
BrO_Mawson_V3_18 = BrO_V3_18M[Mawson]
# Met
Mawson           = (Met_V3_18M.index >= start_date) & (Met_V3_18M.index < end_date)
Met_Mawson_V3_18 = Met_V3_18M[Mawson]
# O3
Mawson           = (O3_V3_18M.index >= start_date)  & (O3_V3_18M.index < end_date)
O3_Mawson_V3_18  = O3_V3_18M[Mawson]

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
# BrO
Davis1          = (BrO_V3_18D.index >= start_date1) & (BrO_V3_18D.index < end_date1)
Davis2          = (BrO_V3_18D.index >= start_date2) & (BrO_V3_18D.index < end_date2)
BrO_Davis_1     = BrO_V3_18D[Davis1]
BrO_Davis_2     = BrO_V3_18D[Davis2]
BrO_Davis_V3_18 = pd.concat([BrO_Davis_1,BrO_Davis_2], axis =0)
# Met
Davis1          = (Met_V3_18D.index >= start_date1) & (Met_V3_18D.index < end_date1)
Davis2          = (Met_V3_18D.index >= start_date2) & (Met_V3_18D.index < end_date2)
Met_Davis_1     = Met_V3_18D[Davis1]
Met_Davis_2     = Met_V3_18D[Davis2]
Met_Davis_V3_18 = pd.concat([Met_Davis_1,Met_Davis_2], axis =0)
# O3
Davis1          = (O3_V3_18D.index >= start_date1) & (O3_V3_18D.index < end_date1)
Davis2          = (O3_V3_18D.index >= start_date2) & (O3_V3_18D.index < end_date2)
O3_Davis_1      = O3_V3_18D[Davis1]
O3_Davis_2      = O3_V3_18D[Davis2]
O3_Davis_V3_18  = pd.concat([O3_Davis_1,O3_Davis_2], axis =0)

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
# O3
MQIsl           = (O3_V4_18.index >= start_date)  & (O3_V4_18.index < end_date)
O3_MQIsl_V4_18  = O3_V4_18[MQIsl]

#-----------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
#-----------------------------
start_date      = '2012-09-23'
end_date        = '2012-11-12'
# Hg0
SIPEX           = (Hg0_SIPEXII.index >= start_date) & (Hg0_SIPEXII.index < end_date)
Hg0_SIPEXII_Ice = Hg0_SIPEXII[SIPEX]
# BrO
SIPEX           = (BrO_SIPEXII.index >= start_date) & (BrO_SIPEXII.index < end_date)
BrO_SIPEXII_Ice = BrO_SIPEXII[SIPEX]
# Met
SIPEX           = (Met_SIPEXII.index >= start_date) & (Met_SIPEXII.index < end_date)
Met_SIPEXII_Ice = Met_SIPEXII[SIPEX]
# O3
SIPEX           = (O3_SIPEXII.index >= start_date)  & (O3_SIPEXII.index < end_date)
O3_SIPEXII_Ice  = O3_SIPEXII[SIPEX]

#-----------------------------
# PCAN (26 Jan to 24 Feb 2017)
#-----------------------------
start_date     = '2017-01-26'
end_date       = '2017-02-25'
# Hg0
PCAN           = (Hg0_PCAN.index >= start_date) & (Hg0_PCAN.index < end_date)
Hg0_PCAN_Ice   = Hg0_PCAN[PCAN]
# Met
PCAN           = (Met_PCAN.index >= start_date) & (Met_PCAN.index < end_date)
Met_PCAN_Ice   = Met_PCAN[PCAN]
# O3
PCAN           = (O3_PCAN.index >= start_date) & (O3_PCAN.index < end_date)
O3_PCAN_Ice    = O3_PCAN[PCAN]

#------------------------------------------------------------------------------
# RESAMPLE TO HOURLY RESOLUTION

#--------------
# Hg0
#--------------
Hg0_SIPEXII_HM = Hg0_SIPEXII.resample('H').mean()
Hg0_PCAN_HM    = Hg0_PCAN.resample('H').mean()

Hg0_V1_17_HM   = Hg0_V1_17.resample('H').mean()
Hg0_V2_17_HM   = Hg0_V2_17.resample('H').mean()
Hg0_V3_17M_HM  = Hg0_V3_17M.resample('H').mean()
Hg0_V3_17D_HM  = Hg0_V3_17D.resample('H').mean()
Hg0_V4_17_HM   = Hg0_V4_17.resample('H').mean()

Hg0_V1_18_HM   = Hg0_V1_18.resample('H').mean()
Hg0_V2_18_HM   = Hg0_V2_18.resample('H').mean()
Hg0_V3_18M_HM  = Hg0_V3_18M.resample('H').mean()
Hg0_V3_18D_HM  = Hg0_V3_18D.resample('H').mean()
Hg0_V4_18_HM   = Hg0_V4_18.resample('H').mean()

#--------------
# BrO
#--------------
BrO_SIPEXII_HM = BrO_SIPEXII.resample('H').mean()
#BrO_PCAN_HM    = BrO_PCAN.resample('H').mean()

BrO_V1_17_HM   = BrO_V1_17.resample('H').mean()
BrO_V2_17_HM   = BrO_V2_17.resample('H').mean()
BrO_V3_17M_HM  = BrO_V3_17M.resample('H').mean()
BrO_V3_17D_HM  = BrO_V3_17D.resample('H').mean()
#BrO_V4_17_HM   = BrO_V4_17.resample('H').mean()

BrO_V1_18_HM   = BrO_V1_18.resample('H').mean()
BrO_V2_18_HM   = BrO_V2_18.resample('H').mean()
BrO_V3_18M_HM  = BrO_V3_18M.resample('H').mean()
BrO_V3_18D_HM  = BrO_V3_18D.resample('H').mean()
#BrO_V4_18_HM   = BrO_V4_18.resample('H').mean()

#--------------
# Met
#--------------
Met_SIPEXII_HM = Met_SIPEXII.resample('H').mean()
Met_PCAN_HM    = Met_PCAN.resample('H').mean()

Met_V1_17_HM   = Met_V1_17.resample('H').mean()
Met_V2_17_HM   = Met_V2_17.resample('H').mean()
Met_V3_17M_HM  = Met_V3_17M.resample('H').mean()
Met_V3_17D_HM  = Met_V3_17D.resample('H').mean()
Met_V4_17_HM   = Met_V4_17.resample('H').mean()

Met_V1_18_HM   = Met_V1_18.resample('H').mean()
Met_V2_18_HM   = Met_V2_18.resample('H').mean()
Met_V3_18M_HM  = Met_V3_18M.resample('H').mean()
Met_V3_18D_HM  = Met_V3_18D.resample('H').mean()
Met_V4_18_HM   = Met_V4_18.resample('H').mean()

#--------------
# O3
#--------------
O3_SIPEXII_HM = O3_SIPEXII.resample('H').mean()
O3_PCAN_HM    = O3_PCAN.resample('H').mean()

O3_V1_17_HM   = O3_V1_17.resample('H').mean()
O3_V2_17_HM   = O3_V2_17.resample('H').mean()
O3_V3_17M_HM  = O3_V3_17M.resample('H').mean()
O3_V3_17D_HM  = O3_V3_17D.resample('H').mean()
O3_V4_17_HM   = O3_V4_17.resample('H').mean()

O3_V1_18_HM   = O3_V1_18.resample('H').mean()
O3_V2_18_HM   = O3_V2_18.resample('H').mean()
O3_V3_18M_HM  = O3_V3_18M.resample('H').mean()
O3_V3_18D_HM  = O3_V3_18D.resample('H').mean()
O3_V4_18_HM   = O3_V4_18.resample('H').mean()

#--------------
# SeaIce
#--------------
SI_SIPEXII_HM = SI_SIPEXII.resample('H').mean()

SI_V1_17_HM   = SI_V1_17.resample('H').mean()
SI_V2_17_HM   = SI_V2_17.resample('H').mean()
SI_V3_17_HM   = SI_V3_17.resample('H').mean()

SI_V1_18_HM   = SI_V1_18.resample('H').mean()
SI_V2_18_HM   = SI_V2_18.resample('H').mean()
SI_V3_18_HM   = SI_V3_18.resample('H').mean()

#------------------------------------------------------------------------------
# CALCULATE RELATIVE HUMIDITY AVERAGE (Port/Strbrd)

Met_V1_17_HM['RH_Avg']   = Met_V1_17_HM[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V1_17
Met_V2_17_HM['RH_Avg']   = Met_V2_17_HM[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V2_17
Met_V3_17M_HM['RH_Avg']  = Met_V3_17M_HM[['rel_humidity_strbrd_percent',  'rel_humidity_port_percent']].mean(axis=1)  # V3_17
Met_V3_17D_HM['RH_Avg']  = Met_V3_17D_HM[['rel_humidity_strbrd_percent',  'rel_humidity_port_percent']].mean(axis=1)  # V3_17
Met_V4_17_HM['RH_Avg']   = Met_V4_17_HM[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V4_17

Met_V1_18_HM['RH_Avg']   = Met_V1_18_HM[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V1_18
Met_V2_18_HM['RH_Avg']   = Met_V2_18_HM[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V2_18
Met_V3_18M_HM['RH_Avg']  = Met_V3_18M_HM[['rel_humidity_strbrd_percent',  'rel_humidity_port_percent']].mean(axis=1)  # V3_18
Met_V3_18D_HM['RH_Avg']  = Met_V3_18D_HM[['rel_humidity_strbrd_percent',  'rel_humidity_port_percent']].mean(axis=1)  # V3_18
Met_V4_18_HM['RH_Avg']   = Met_V4_18_HM[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V4_18

Met_PCAN_HM['RH_Avg']    = Met_PCAN_HM[['Starboard Humidity (%)',         'Port Humidity (%)']].mean(axis=1)          # PCAN
Met_SIPEXII_HM['RH_Avg'] = Met_SIPEXII_HM[['rel_humidity_strbrd_percent', 'rel_humidity_port_percent']].mean(axis=1)  # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE TEMPERATURE AVERAGE (Port/Strbrd)

Met_V1_17_HM['Temp_Avg']   = Met_V1_17_HM[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V1_17
Met_V2_17_HM['Temp_Avg']   = Met_V2_17_HM[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V2_17
Met_V3_17M_HM['Temp_Avg']  = Met_V3_17M_HM[['temp_air_strbrd_degc',           'temp_air_port_degc']].mean(axis=1)  # V3_17
Met_V3_17D_HM['Temp_Avg']  = Met_V3_17D_HM[['temp_air_strbrd_degc',           'temp_air_port_degc']].mean(axis=1)  # V3_17
Met_V4_17_HM['Temp_Avg']   = Met_V4_17_HM[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V4_17

Met_V1_18_HM['Temp_Avg']   = Met_V1_18_HM[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V1_18
Met_V2_18_HM['Temp_Avg']   = Met_V2_18_HM[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V2_18
Met_V3_18M_HM['Temp_Avg']  = Met_V3_18M_HM[['temp_air_strbrd_degc',           'temp_air_port_degc']].mean(axis=1)  # V3_18
Met_V3_18D_HM['Temp_Avg']  = Met_V3_18D_HM[['temp_air_strbrd_degc',           'temp_air_port_degc']].mean(axis=1)  # V3_18
Met_V4_18_HM['Temp_Avg']   = Met_V4_18_HM[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V4_18

Met_PCAN_HM['Temp_Avg']    = Met_PCAN_HM[['Starboard Air Temperature (degC)', 'Port Air Temperature (degC)']].mean(axis=1) # PCAN
Met_SIPEXII_HM['Temp_Avg'] = Met_SIPEXII_HM[['temp_air_strbrd_degc',          'temp_air_port_degc']].mean(axis=1)  # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE SOLAR RADIATION (Port/Strbrd)

Met_V1_17_HM['SolRad_Avg']   = Met_V1_17_HM[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V1_17
Met_V2_17_HM['SolRad_Avg']   = Met_V2_17_HM[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V2_17
Met_V3_17M_HM['SolRad_Avg']  = Met_V3_17M_HM[['rad_slr_strbrd_wperm2',      'rad_slr_port_wperm2']].mean(axis=1)  # V3_17
Met_V3_17D_HM['SolRad_Avg']  = Met_V3_17D_HM[['rad_slr_strbrd_wperm2',      'rad_slr_port_wperm2']].mean(axis=1)  # V3_17
Met_V4_17_HM['SolRad_Avg']   = Met_V4_17_HM[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V4_17

Met_V1_18_HM['SolRad_Avg']   = Met_V1_18_HM[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V1_18
Met_V2_18_HM['SolRad_Avg']   = Met_V2_18_HM[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V2_18
Met_V3_18M_HM['SolRad_Avg']  = Met_V3_18M_HM[['rad_slr_strbrd_wperm2',      'rad_slr_port_wperm2']].mean(axis=1)  # V3_18
Met_V3_18D_HM['SolRad_Avg']  = Met_V3_18D_HM[['rad_slr_strbrd_wperm2',      'rad_slr_port_wperm2']].mean(axis=1)  # V3_18
Met_V4_18_HM['SolRad_Avg']   = Met_V4_18_HM[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V4_18

Met_PCAN_HM['SolRad_Avg']    = Met_PCAN_HM[['Starboard Radiometer (W/m^2)', 'Port Radiometer (W/m^2)']].mean(axis=1) # PCAN
Met_SIPEXII_HM['SolRad_Avg'] = Met_SIPEXII_HM[['rad_slr_strbrd_wperm2',     'rad_slr_port_wperm2']].mean(axis=1)  # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE WIND SPEED (Port/Strbrd)

Met_V1_17_HM['WS_Avg']   = Met_V1_17_HM[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V1_17
Met_V2_17_HM['WS_Avg']   = Met_V2_17_HM[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V2_17
Met_V3_17M_HM['WS_Avg']  = Met_V3_17M_HM[['wnd_spd_strbrd_corr_knot',       'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V3_17
Met_V3_17D_HM['WS_Avg']  = Met_V3_17D_HM[['wnd_spd_strbrd_corr_knot',       'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V3_17
Met_V4_17_HM['WS_Avg']   = Met_V4_17_HM[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V4_17

Met_V1_18_HM['WS_Avg']   = Met_V1_18_HM[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V1_18
Met_V2_18_HM['WS_Avg']   = Met_V2_18_HM[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V2_18
Met_V3_18M_HM['WS_Avg']  = Met_V3_18M_HM[['wnd_spd_strbrd_corr_knot',       'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V3_18
Met_V3_18D_HM['WS_Avg']  = Met_V3_18D_HM[['wnd_spd_strbrd_corr_knot',       'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V3_18
Met_V4_18_HM['WS_Avg']   = Met_V4_18_HM[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V4_18

Met_PCAN_HM['WS_Avg']    = Met_PCAN_HM[['Starboard True Wind Speed (knot)', 'Port True Wind Speed (knot)']].mean(axis=1) * 0.514444444 # PCAN
Met_SIPEXII_HM['WS_Avg'] = Met_SIPEXII_HM[['wnd_spd_strbrd_corr_knot',      'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # SIPEXII

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN 2017-18)
fig = plt.figure()

gs = gridspec.GridSpec(nrows=4,
                       ncols=3, 
                       figure=fig, 
                       width_ratios= [0.33, 0.33, 0.33],
                       height_ratios=[0.25, 0.25, 0.25, 0.25])

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2017,11,14) # Arrive Davis (V1 17)
depart1 = datetime(2017,11,23) # Depart Davis (V1 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.05, "Davis", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_V1_17_HM.index, Hg0_V1_17_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="V1 (2017-18)", zorder=2)
ax1.plot(Hg0_V1_17_HM.index,    Hg0_V1_17_HM['ng/m3'],    marker='o',    markersize=1.0,   ls='--',  c='black',   label ="V1 (2017-18)", zorder=2)
ax2.plot(Met_V1_17_HM.index,    Met_V1_17_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.50, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,10,30,0,1,),datetime(2017,12,2,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.1) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["right"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('V1 (2017-18)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[0,1])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2017,12,21) # Arrive Casey (V2 17)
depart1 = datetime(2017,12,23) # Depart Casey (V2 17)
arrive2 = datetime(2017,12,26) # Arrive Casey (V2 17)
depart2 = datetime(2018,1,6)   # Depart Casey (V2 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.05, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive2 + (depart2 - arrive2)/2, 1.05, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_V2_17_HM.index, Hg0_V2_17_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="V2 (2017-18)", zorder=2)
ax1.plot(Hg0_V2_17_HM.index,    Hg0_V2_17_HM['ng/m3'],    marker='o',    markersize=1.0,   ls='--',  c='black',   label ="V2 (2017-18)", zorder=2)
ax2.plot(Met_V2_17_HM.index,    Met_V2_17_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.57, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,12,13,0,1,),datetime(2018,1,11,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.1) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["left"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('V2 (2017-18)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[0,2])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2018,2,1)  # Arrive Mawson (V3 17)
depart1 = datetime(2018,2,18) # Depart Mawson (V3 17)
arrive2 = datetime(2018,1,27) # Arrive Davis (V3 17)
depart2 = datetime(2018,1,31) # Depart Davis (V3 17)
arrive3 = datetime(2018,2,19) # Arrive Davis (V3 17)
depart3 = datetime(2018,2,22) # Depart Davis (V3 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.05, "Mawson", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive2 + (depart2 - arrive2)/2, 1.05, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive3 + (depart3 - arrive3)/2, 1.05, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_V3_17M_HM.index, Hg0_V3_17M_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="V3M (2017-18)", zorder=2)
ax1.plot(Hg0_V3_17M_HM.index,    Hg0_V3_17M_HM['ng/m3'],    marker='o',    markersize=1.0,   ls='--',  c='black',   label ="V1 (2017-18)", zorder=2)
ax2.plot(Met_V3_17M_HM.index,    Met_V3_17M_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.49, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,1,19,0,1,),datetime(2018,3,4,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.1) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["left"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('V3 (2017-18)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 4
ax1 = plt.subplot(gs[1,0])

# Shade time on station
arrive1 = datetime(2017,11,14) # Arrive Davis (V1 17)
depart1 = datetime(2017,11,23) # Depart Davis (V1 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(BrO_V1_17_HM.index, BrO_V1_17_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)
ax1.plot(BrO_V1_17_HM.index, BrO_V1_17_HM['surf_vmr(ppmv)']* 1e6, marker='o', markersize=1.0, ls='-', c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,10,30,0,1,),datetime(2017,12,2,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 5
ax1 = plt.subplot(gs[1,1])

# Shade time on station
arrive1 = datetime(2017,12,21) # Arrive Casey (V2 17)
depart1 = datetime(2017,12,23) # Depart Casey (V2 17)
arrive2 = datetime(2017,12,26) # Arrive Casey (V2 17)
depart2 = datetime(2018,1,6)   # Depart Casey (V2 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(BrO_V2_17_HM.index, BrO_V2_17_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)
ax1.plot(BrO_V2_17_HM.index, BrO_V2_17_HM['surf_vmr(ppmv)']* 1e6, marker='o', markersize=1.0, ls='-', c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,12,13,0,1,),datetime(2018,1,11,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 6
ax1 = plt.subplot(gs[1,2])

# Shade time on station
arrive1 = datetime(2018,2,1)  # Arrive Mawson (V3 17)
depart1 = datetime(2018,2,18) # Depart Mawson (V3 17)
arrive2 = datetime(2018,1,27) # Arrive Davis (V3 17)
depart2 = datetime(2018,1,31) # Depart Davis (V3 17)
arrive3 = datetime(2018,2,19) # Arrive Davis (V3 17)
depart3 = datetime(2018,2,22) # Depart Davis (V3 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(BrO_V3_17M_HM.index, BrO_V3_17M_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)
ax1.plot(BrO_V3_17M_HM.index, BrO_V3_17M_HM['surf_vmr(ppmv)']* 1e6, marker='o', markersize=1.0, ls='-', c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,1,19,0,1,),datetime(2018,3,4,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 7
ax1 = plt.subplot(gs[2,0])

# Shade time on station
arrive1 = datetime(2017,11,14) # Arrive Davis (V1 17)
depart1 = datetime(2017,11,23) # Depart Davis (V1 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(O3_V1_17_HM.index,  O3_V1_17_HM['O3_(ppb)'], s= 1.0, c='green', zorder=2)
ax1.plot(O3_V1_17_HM.index, O3_V1_17_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,10,30,0,1,),datetime(2017,12,2,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,29.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 8
ax1 = plt.subplot(gs[2,1])

# Shade time on station
arrive1 = datetime(2017,12,21) # Arrive Casey (V2 17)
depart1 = datetime(2017,12,23) # Depart Casey (V2 17)
arrive2 = datetime(2017,12,26) # Arrive Casey (V2 17)
depart2 = datetime(2018,1,6)   # Depart Casey (V2 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(O3_V2_17_HM.index,  O3_V2_17_HM['O3_(ppb)'], marker='o', s= 1.0, c='green', zorder=2)
ax1.plot(O3_V2_17_HM.index, O3_V2_17_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,12,13,0,1,),datetime(2018,1,11,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,29.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 9
ax1 = plt.subplot(gs[2,2])

# Shade time on station
arrive1 = datetime(2018,2,1)  # Arrive Mawson (V3 17)
depart1 = datetime(2018,2,18) # Depart Mawson (V3 17)
arrive2 = datetime(2018,1,27) # Arrive Davis (V3 17)
depart2 = datetime(2018,1,31) # Depart Davis (V3 17)
arrive3 = datetime(2018,2,19) # Arrive Davis (V3 17)
depart3 = datetime(2018,2,22) # Depart Davis (V3 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(O3_V3_17M_HM.index,  O3_V3_17M_HM['O3_(ppb)'], marker='o', s= 1.0, c='green', zorder=2)
ax1.plot(O3_V3_17M_HM.index, O3_V3_17M_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,1,19,0,1,),datetime(2018,3,4,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,29.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 10
ax1 = plt.subplot(gs[3,0])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2017,11,14) # Arrive Davis (V1 17)
depart1 = datetime(2017,11,23) # Depart Davis (V1 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
ax1.scatter(Met_V1_17_HM.index, Met_V1_17_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_V1_17_HM.index, Met_V1_17_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2017,10,30,0,1,),datetime(2017,12,2,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-15,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('Relative humdity (%)',fontsize=12)
#ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 11
ax1 = plt.subplot(gs[3,1])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2017,12,21) # Arrive Casey (V2 17)
depart1 = datetime(2017,12,23) # Depart Casey (V2 17)
arrive2 = datetime(2017,12,26) # Arrive Casey (V2 17)
depart2 = datetime(2018,1,6)   # Depart Casey (V2 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
ax1.scatter(Met_V2_17_HM.index, Met_V2_17_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_V2_17_HM.index, Met_V2_17_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2017,12,13,0,1,),datetime(2018,1,11,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-15,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)
#ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 12
ax1 = plt.subplot(gs[3,2])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2018,2,1)  # Arrive Mawson (V3 17)
depart1 = datetime(2018,2,18) # Depart Mawson (V3 17)
arrive2 = datetime(2018,1,27) # Arrive Davis (V3 17)
depart2 = datetime(2018,1,31) # Depart Davis (V3 17)
arrive3 = datetime(2018,2,19) # Arrive Davis (V3 17)
depart3 = datetime(2018,2,22) # Depart Davis (V3 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
ax1.scatter(Met_V3_17M_HM.index, Met_V3_17M_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_V3_17M_HM.index, Met_V3_17M_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2018,1,19,0,1,),datetime(2018,3,4,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-15,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)
ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN 2018-19)
fig = plt.figure()

gs = gridspec.GridSpec(nrows=4,
                       ncols=3, 
                       figure=fig, 
                       width_ratios= [0.33, 0.33, 0.33],
                       height_ratios=[0.25, 0.25, 0.25, 0.25])

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2018,11,7)  # Arrive Davis (V1 18)
depart1 = datetime(2018,11,16) # Depart Davis (V1 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.05, "Davis", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_V1_18_HM.index, Hg0_V1_18_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="V1 (2018-19)", zorder=2)
ax1.plot(Hg0_V1_18_HM.index, Hg0_V1_18_HM['ng/m3'],    marker='o', markersize=1.0, ls='--',  c='black',   label ="V1 (2018-19)", zorder=2)
ax2.plot(Met_V1_18_HM.index,    Met_V1_18_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.74, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,10,25,0,1,),datetime(2018,11,28,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.1) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["right"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('V1 (2018-19)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[0,1])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2018,12,15) # Arrive Casey (V2 18)
depart1 = datetime(2018,12,31) # Depart Casey (V2 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.05, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_V2_18_HM.index, Hg0_V2_18_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="V2 (2018-19)", zorder=2)
ax1.plot(Hg0_V2_18_HM.index, Hg0_V2_18_HM['ng/m3'],    marker='o', markersize=1.0, ls='--',  c='black',   label ="V2 (2018-19)", zorder=2)
ax2.plot(Met_V2_18_HM.index,    Met_V2_18_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.69, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,12,6,0,1,),datetime(2019,1,7,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.1) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["left"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('V2 (2018-19)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[0,2])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2019,1,30) # Arrive Mawson (V3 18)
depart1 = datetime(2019,2,10) # Depart Mawson (V3 18)
arrive2 = datetime(2019,1,26) # Arrive Davis (V3 18)
depart2 = datetime(2019,1,29) # Depart Davis (V3 18)
arrive3 = datetime(2019,2,19) # Arrive Davis (V3 18)
depart3 = datetime(2019,2,21) # Depart Davis (V3 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 1.05, "Mawson", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive2 + (depart2 - arrive2)/2, 1.05, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax1.text(arrive3 + (depart3 - arrive3)/2, 1.05, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_V3_18M_HM.index, Hg0_V3_18M_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="V3M (2018-19)", zorder=2)
ax1.plot(Hg0_V3_18M_HM.index, Hg0_V3_18M_HM['ng/m3'],    marker='o', markersize=1.0, ls='--',  c='black',   label ="V3 (2018-19)", zorder=2)
ax2.plot(Met_V3_18M_HM.index,    Met_V3_18M_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.60, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2019,1,13,0,1,),datetime(2019,2,28,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.1) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["left"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('V3 (2018-19)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 4
ax1 = plt.subplot(gs[1,0])

# Shade time on station
arrive1 = datetime(2018,11,7)  # Arrive Davis (V1 18)
depart1 = datetime(2018,11,16) # Depart Davis (V1 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(BrO_V1_18_HM.index, BrO_V1_18_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)
ax1.plot(BrO_V1_18_HM.index, BrO_V1_18_HM['surf_vmr(ppmv)']* 1e6, marker='o', markersize=1.0, ls='-', c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,10,25,0,1,),datetime(2018,11,28,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 5
ax1 = plt.subplot(gs[1,1])

# Shade time on station
arrive1 = datetime(2018,12,15) # Arrive Casey (V2 18)
depart1 = datetime(2018,12,31) # Depart Casey (V2 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(BrO_V2_18_HM.index, BrO_V2_18_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)
ax1.plot(BrO_V2_18_HM.index, BrO_V2_18_HM['surf_vmr(ppmv)']* 1e6, marker='o', markersize=1.0, ls='-', c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,12,6,0,1,),datetime(2019,1,7,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 6
ax1 = plt.subplot(gs[1,2])

# Shade time on station
arrive1 = datetime(2019,1,30) # Arrive Mawson (V3 18)
depart1 = datetime(2019,2,10) # Depart Mawson (V3 18)
arrive2 = datetime(2019,1,26) # Arrive Davis (V3 18)
depart2 = datetime(2019,1,29) # Depart Davis (V3 18)
arrive3 = datetime(2019,2,19) # Arrive Davis (V3 18)
depart3 = datetime(2019,2,21) # Depart Davis (V3 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(BrO_V3_18M_HM.index, BrO_V3_18M_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)
ax1.plot(BrO_V3_18M_HM.index, BrO_V3_18M_HM['surf_vmr(ppmv)']* 1e6, marker='o', markersize=1.0, ls='-', c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2019,1,13,0,1,),datetime(2019,2,28,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 7
ax1 = plt.subplot(gs[2,0])

# Shade time on station
arrive1 = datetime(2018,11,7)  # Arrive Davis (V1 18)
depart1 = datetime(2018,11,16) # Depart Davis (V1 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(O3_V1_18_HM.index,  O3_V1_18_HM['O3_(ppb)'], s= 1.0, c='green', zorder=2)
ax1.plot(O3_V1_18_HM.index, O3_V1_18_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,10,25,0,1,),datetime(2018,11,28,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,29.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 8
ax1 = plt.subplot(gs[2,1])

# Shade time on station
arrive1 = datetime(2018,12,15) # Arrive Casey (V2 18)
depart1 = datetime(2018,12,31) # Depart Casey (V2 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(O3_V2_18_HM.index,  O3_V2_18_HM['O3_(ppb)'], marker='o', s= 1.0, c='green', zorder=2)
ax1.plot(O3_V2_18_HM.index, O3_V2_18_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,12,6,0,1,),datetime(2019,1,7,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,29.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 9
ax1 = plt.subplot(gs[2,2])

# Shade time on station
arrive1 = datetime(2019,1,30) # Arrive Mawson (V3 18)
depart1 = datetime(2019,2,10) # Depart Mawson (V3 18)
arrive2 = datetime(2019,1,26) # Arrive Davis (V3 18)
depart2 = datetime(2019,1,29) # Depart Davis (V3 18)
arrive3 = datetime(2019,2,19) # Arrive Davis (V3 18)
depart3 = datetime(2019,2,21) # Depart Davis (V3 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
#ax1.scatter(O3_V3_18M_HM.index,  O3_V3_18M_HM['O3_(ppb)'], marker='o', s= 1.0, c='green', zorder=2)
ax1.plot(O3_V3_18M_HM.index, O3_V3_18M_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2019,1,13,0,1,),datetime(2019,2,28,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,29.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 10
ax1 = plt.subplot(gs[3,0])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2018,11,7)  # Arrive Davis (V1 18)
depart1 = datetime(2018,11,16) # Depart Davis (V1 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
ax1.scatter(Met_V1_18_HM.index, Met_V1_18_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_V1_18_HM.index, Met_V1_18_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2018,10,25,0,1,),datetime(2018,11,28,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-15,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('Relative humdity (%)',fontsize=12)
#ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 11
ax1 = plt.subplot(gs[3,1])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2018,12,15) # Arrive Casey (V2 18)
depart1 = datetime(2018,12,31) # Depart Casey (V2 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
ax1.scatter(Met_V2_18_HM.index, Met_V2_18_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_V2_18_HM.index, Met_V2_18_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2018,12,6,0,1,),datetime(2019,1,7,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-15,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)
#ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 12
ax1 = plt.subplot(gs[3,2])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2019,1,30) # Arrive Mawson (V3 18)
depart1 = datetime(2019,2,10) # Depart Mawson (V3 18)
arrive2 = datetime(2019,1,26) # Arrive Davis (V3 18)
depart2 = datetime(2019,1,29) # Depart Davis (V3 18)
arrive3 = datetime(2019,2,19) # Arrive Davis (V3 18)
depart3 = datetime(2019,2,21) # Depart Davis (V3 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive2, depart2, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade
ax1.axvspan(arrive3, depart3, color='grey', alpha=0.7, lw=0, zorder=1) # dark shade

# Plot the variables
ax1.scatter(Met_V3_18M_HM.index, Met_V3_18M_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_V3_18M_HM.index, Met_V3_18M_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2019,1,13,0,1,),datetime(2019,2,28,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-15,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)
ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (MQIsl, PCAN 2017, SIPEXII 2012)
fig = plt.figure()

gs = gridspec.GridSpec(nrows=4,
                       ncols=4, 
                       figure=fig, 
                       width_ratios= [0.25, 0.25, 0.25, 0.25],
                       height_ratios=[0.25, 0.25, 0.25, 0.25])

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0,0])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2018,3,12) # Arrive Maquarie Island (V4 17)
depart1 = datetime(2018,3,21) # Depart Maquarie Island (V4 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 0.15, "Maquarie Island", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_V4_17_HM.index, Hg0_V4_17_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="V4 (2017-18)", zorder=2)
ax1.plot(Hg0_V4_17_HM.index, Hg0_V4_17_HM['ng/m3'],    marker='o', markersize=1.0, ls='--',  c='black',   label ="V4 (2017-18)", zorder=2)
ax2.plot(Met_V4_17_HM.index,    Met_V4_17_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.36, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,3,9,0,1,),datetime(2018,3,22,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.0) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["right"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('V4 (2017-18)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[0,1])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2019,3,8)  # Arrive Maquarie Island (V4 18)
depart1 = datetime(2019,3,23) # Depart Maquarie Island (V4 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 0.15, "Maquarie Island", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_V4_18_HM.index, Hg0_V4_18_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="V4 (2018-19)", zorder=2)
ax1.plot(Hg0_V4_18_HM.index, Hg0_V4_18_HM['ng/m3'],    marker='o', markersize=1.0, ls='--',  c='black',   label ="V4 (2018-19)", zorder=2)
ax2.plot(Met_V4_18_HM.index,    Met_V4_18_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.52, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2019,3,5,0,1,),datetime(2019,3,25,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.0) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["left"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('V4 (2018-19)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[0,2])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2017,1,26) # Arrive close to Antarctica (2017)
depart1 = datetime(2017,2,25) # Depart close to Antarctica (2017)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 0.15, "Close to Antarctica", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_PCAN_HM.index, Hg0_PCAN_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="PCAN (2017)", zorder=2)
ax1.plot(Hg0_PCAN_HM.index, Hg0_PCAN_HM['ng/m3'],    marker='o', markersize=1.0, ls='--',  c='black',   label ="PCAN (2017)", zorder=2)
ax2.plot(Met_PCAN_HM.index,    Met_PCAN_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(0.56, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,1,15,0,1,),datetime(2017,3,7,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,1.0) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["left"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('PCAN (2017)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 4
ax1 = plt.subplot(gs[0,3])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2012,9,23)  # Arrive Sea Ice (2012)
depart1 = datetime(2012,11,12) # Depart Sea Ice (2012)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax1.text(arrive1 + (depart1 - arrive1)/2, 0.30, "Within sea Ice", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot hourly Hg0
#ax1.scatter(Hg0_SIPEXII_HM.index, Hg0_SIPEXII_HM['ng/m3'],    marker='o',    s= 1.0,  c='black',   label ="SIPEXII (2012)", zorder=2)
ax1.plot(Hg0_SIPEXII_HM.index, Hg0_SIPEXII_HM['ng/m3'],    marker='o', markersize=1.0, ls='--',  c='black',   label ="SIPEXII (2012)", zorder=2)
ax2.plot(Met_SIPEXII_HM.index,    Met_SIPEXII_HM['latitude'], marker='None', ls='--', c='orange',  zorder=2)

# Plot horizontal line for median Hg0
ax1.axhline(1.07, linewidth=1.0, color='k', ls='--')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2012,9,14,0,1,),datetime(2012,11,14,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.set_ylim(0,2.0) # On Station
ax1.tick_params(axis='y', which='both', colors='black', labelsize=10)
ax2.spines["left"].set_color('black')
ax1.yaxis.label.set_color('black')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69.9,-40.1) # On Station
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax2.spines["right"].set_color('orange')
ax2.yaxis.label.set_color('orange')

# Plot the axis labels
#ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax2.set_ylabel('Latitude (($^\circ$)', fontsize=12)

#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=20, y=1.06)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 5
ax1 = plt.subplot(gs[1,0])

# Shade time on station
arrive1 = datetime(2018,3,12) # Arrive Maquarie Island (V4 17)
depart1 = datetime(2018,3,21) # Depart Maquarie Island (V4 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
#ax1.scatter(BrO_V4_17_HM.index, BrO_V4_17_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,3,9,0,1,),datetime(2018,3,22,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 6
ax1 = plt.subplot(gs[1,1])

# Shade time on station
arrive1 = datetime(2019,3,8)  # Arrive Maquarie Island (V4 18)
depart1 = datetime(2019,3,23) # Depart Maquarie Island (V4 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
#ax1.scatter(BrO_V4_18_HM.index, BrO_V4_18_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2019,3,5,0,1,),datetime(2019,3,25,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax2.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 7
ax1 = plt.subplot(gs[1,2])

# Shade time on station
arrive1 = datetime(2017,1,26) # Arrive close to Antarctica (2017)
depart1 = datetime(2017,2,25) # Depart close to Antarctica (2017)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
#ax1.scatter(BrO_PCAN_HM.index, BrO_PCAN_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,1,15,0,1,),datetime(2017,3,7,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 8
ax1 = plt.subplot(gs[1,3])

# Shade time on station
arrive1 = datetime(2012,9,23)  # Arrive Sea Ice (2012)
depart1 = datetime(2012,11,12) # Depart Sea Ice (2012)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
#ax1.scatter(BrO_SIPEXII_HM.index, BrO_SIPEXII_HM['surf_vmr(ppmv)']* 1e6, marker='o', s= 1.0, c='magenta', zorder=2)
ax1.plot(BrO_SIPEXII_HM.index, BrO_SIPEXII_HM['surf_vmr(ppmv)']* 1e6, marker='o', markersize=1.0, ls='-', c='magenta', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2012,9,14,0,1,),datetime(2012,11,14,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.9)
ax1.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax1.spines["right"].set_color('magenta')
ax1.yaxis.label.set_color('magenta')

# Plot the axis labels
#ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('BrO (pptv)', fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 9
ax1 = plt.subplot(gs[2,0])

# Shade time on station
arrive1 = datetime(2018,3,12) # Arrive Maquarie Island (V4 17)
depart1 = datetime(2018,3,21) # Depart Maquarie Island (V4 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
#ax1.scatter(O3_V4_17_HM.index,  O3_V4_17_HM['O3_(ppb)'], s= 1.0, c='green', zorder=2)
ax1.plot(O3_V4_17_HM.index, O3_V4_17_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2018,3,9,0,1,),datetime(2018,3,22,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,39.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 10
ax1 = plt.subplot(gs[2,1])

# Shade time on station
arrive1 = datetime(2019,3,8)  # Arrive Maquarie Island (V4 18)
depart1 = datetime(2019,3,23) # Depart Maquarie Island (V4 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
#ax1.scatter(O3_V4_18_HM.index,  O3_V4_18_HM['O3_(ppb)'], marker='o', s= 1.0, c='green', zorder=2)
ax1.plot(O3_V4_18_HM.index, O3_V4_18_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2019,3,5,0,1,),datetime(2019,3,25,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,39.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 11
ax1 = plt.subplot(gs[2,2])

# Shade time on station
arrive1 = datetime(2017,1,26) # Arrive close to Antarctica (2017)
depart1 = datetime(2017,2,25) # Depart close to Antarctica (2017)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
#ax1.scatter(O3_PCAN_HM.index,  O3_PCAN_HM['O3_(ppb)'], marker='o', s= 1.0, c='green', zorder=2)
ax1.plot(O3_PCAN_HM.index, O3_PCAN_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2017,1,15,0,1,),datetime(2017,3,7,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,39.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 12
ax1 = plt.subplot(gs[2,3])

# Shade time on station
arrive1 = datetime(2012,9,23)  # Arrive Sea Ice (2012)
depart1 = datetime(2012,11,12) # Depart Sea Ice (2012)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
#ax1.scatter(O3_SIPEXII_HM.index,  O3_SIPEXII_HM['O3_(ppb)'], marker='o', s= 1.0, c='green', zorder=2)
ax1.plot(O3_SIPEXII_HM.index, O3_SIPEXII_HM['O3_(ppb)'], marker='o', markersize=1.0, ls='-', c='green', zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
ax1.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(2012,9,14,0,1,),datetime(2012,11,14,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax1.set_ylim(0,39.9)
ax1.spines["right"].set_color('green')
ax1.yaxis.label.set_color('green')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 13
ax1 = plt.subplot(gs[3,0])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2018,3,12) # Arrive Maquarie Island (V4 17)
depart1 = datetime(2018,3,21) # Depart Maquarie Island (V4 17)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
ax1.scatter(Met_V4_17_HM.index, Met_V4_17_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_V4_17_HM.index, Met_V4_17_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2018,3,9,0,1,),datetime(2018,3,22,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-25,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
ax1.set_ylabel('Relative humdity (%)',fontsize=12)
#ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 14
ax1 = plt.subplot(gs[3,1])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2019,3,8)  # Arrive Maquarie Island (V4 18)
depart1 = datetime(2019,3,23) # Depart Maquarie Island (V4 18)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
ax1.scatter(Met_V4_18_HM.index, Met_V4_18_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_V4_18_HM.index, Met_V4_18_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2019,3,5,0,1,),datetime(2019,3,25,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-25,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)
#ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#Plot the legend and title
#plt.title('V1 (2017-18)', fontsize=15, y=1.01)
# legend = ax1.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#-----------------------------
# Graph 15
ax1 = plt.subplot(gs[3,2])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2017,1,26) # Arrive close to Antarctica (2017)
depart1 = datetime(2017,2,25) # Depart close to Antarctica (2017)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
ax1.scatter(Met_PCAN_HM.index, Met_PCAN_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_PCAN_HM.index, Met_PCAN_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2017,1,15,0,1,),datetime(2017,3,7,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-25,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)
#ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)

#-----------------------------
# Graph 16
ax1 = plt.subplot(gs[3,3])
ax2 = ax1.twinx()

# Shade time on station
arrive1 = datetime(2012,9,23)  # Arrive Sea Ice (2012)
depart1 = datetime(2012,11,12) # Depart Sea Ice (2012)
ax1.axvspan(arrive1, depart1, color='grey', alpha=0.7, lw=0) # dark shade

# Plot the variables
ax1.scatter(Met_SIPEXII_HM.index, Met_SIPEXII_HM['RH_Avg'],   marker='o', s= 1.0, c='blue', zorder=2)
ax2.scatter(Met_SIPEXII_HM.index, Met_SIPEXII_HM['Temp_Avg'], marker='o', s= 1.0, c='red',  zorder=2)

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.setp(ax1.get_xticklabels(), rotation=70)
plt.xlim(datetime(2012,9,14,0,1,),datetime(2012,11,14,23,59,0))

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax1.spines["right"].set_position(("axes", 1.13))
ax1.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax1.set_ylim(0,109.9)
ax2.spines["left"].set_color('blue')
ax1.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax2.spines["right"].set_position(("axes", 1.13))
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax2.set_ylim(-25,29.9)
ax2.spines["right"].set_color('red')
ax2.yaxis.label.set_color('red')

# Plot the axis labels
ax1.set_xlabel('Date', fontsize=12, labelpad=-0.1)
#ax1.set_ylabel('O$_3$ (ppb)',fontsize=12)
ax2.set_ylabel('Temperature (($^\circ$C))',fontsize=12)