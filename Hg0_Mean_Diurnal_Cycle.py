#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:55:26 2019

@author: ncp532
"""

# Date and Time handling package
from datetime import datetime,time,timedelta		# functions to handle date and time

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

#--------------
# Hg0
#--------------
Hg0_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_QAQC_17-18.csv')
Hg0_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_QAQC_17-18.csv')
Hg0_V3_17M  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_QAQC_17-18.csv')
Hg0_V3_17D  = Hg0_V3_17M
Hg0_V4_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V4_Hg0_QAQC_17-18.csv')

Hg0_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_QAQC_18-19.csv')
Hg0_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_QAQC_18-19.csv')
Hg0_V3_18M  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_QAQC_18-19.csv')
Hg0_V3_18D  = Hg0_V3_18M
Hg0_V4_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V4_Hg0_QAQC_18-19.csv')

Hg0_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_QAQC_2012.csv')
Hg0_PCAN    = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/PCAN_Hg0_QAQC_2017.csv')

#--------------
# Sea Ice
#--------------
SI_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V1_17_BrO.csv',  index_col=0)
SI_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V2_17_BrO.csv',  index_col=0)
SI_V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V3_17M_BrO.csv', index_col=0)

SI_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V1_18_BrO.csv',  index_col=0)
SI_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V2_18_BrO.csv',  index_col=0)
SI_V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V3_18M_BrO.csv', index_col=0)

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

Met_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/ShipTrack/SIPEXII_underway_60.csv',   index_col=0) 
Met_PCAN    = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/ShipTrack/PCAN_underway_60.csv',         index_col=0) 

# O3
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
Hg0_V1_17['DateTime']    = pd.to_datetime(Hg0_V1_17['DateTime'],   dayfirst=True)
Hg0_V2_17['DateTime']    = pd.to_datetime(Hg0_V2_17['DateTime'],   dayfirst=True)
Hg0_V3_17M['DateTime']   = pd.to_datetime(Hg0_V3_17M['DateTime'],  dayfirst=True)
Hg0_V3_17D['DateTime']   = (pd.to_datetime(Hg0_V3_17D['DateTime'], dayfirst=True) + timedelta(hours=2))
Hg0_V4_17['DateTime']    = pd.to_datetime(Hg0_V4_17['DateTime'],   dayfirst=True)

Hg0_V1_18['DateTime']    = pd.to_datetime(Hg0_V1_18['DateTime'],   dayfirst=True)
Hg0_V2_18['DateTime']    = pd.to_datetime(Hg0_V2_18['DateTime'],   dayfirst=True)
Hg0_V3_18M['DateTime']   = pd.to_datetime(Hg0_V3_18M['DateTime'],  dayfirst=True)
Hg0_V3_18D['DateTime']   = (pd.to_datetime(Hg0_V3_18D['DateTime'], dayfirst=True) + timedelta(hours=2))
Hg0_V4_18['DateTime']    = pd.to_datetime(Hg0_V4_18['DateTime'],   dayfirst=True)

Hg0_SIPEXII['DateTime']  = pd.to_datetime(Hg0_SIPEXII['DateTime'], dayfirst=True)
Hg0_PCAN['DateTime']     = pd.to_datetime(Hg0_PCAN['DateTime'],    dayfirst=True)

#------------------------------------------------------------------------------
# Set DateTime as the index

#--------------
# Hg0
#--------------
Hg0_V1_17.index   = Hg0_V1_17['DateTime']
Hg0_V2_17.index   = Hg0_V2_17['DateTime']
Hg0_V3_17M.index  = Hg0_V3_17M['DateTime']
Hg0_V3_17D.index  = Hg0_V3_17D['DateTime']
Hg0_V4_17.index   = Hg0_V4_17['DateTime']

Hg0_V1_18.index   = Hg0_V1_18['DateTime']
Hg0_V2_18.index   = Hg0_V2_18['DateTime']
Hg0_V3_18M.index  = Hg0_V3_18M['DateTime']
Hg0_V3_18D.index  = Hg0_V3_18D['DateTime']
Hg0_V4_18.index   = Hg0_V4_18['DateTime']

Hg0_SIPEXII.index = Hg0_SIPEXII['DateTime']
Hg0_PCAN.index    = Hg0_PCAN['DateTime']

#--------------
# Sea Ice
#--------------
SI_V1_17.index   = pd.to_datetime(SI_V1_17.index,   dayfirst=True)
SI_V2_17.index   = pd.to_datetime(SI_V2_17.index,   dayfirst=True)
SI_V3_17.index   = pd.to_datetime(SI_V3_17.index,   dayfirst=True)

SI_V1_18.index   = pd.to_datetime(SI_V1_18.index,   dayfirst=True)
SI_V2_18.index   = pd.to_datetime(SI_V2_18.index,   dayfirst=True)
SI_V3_18.index   = pd.to_datetime(SI_V3_18.index,   dayfirst=True)

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
# RESAMPLE THE SEA ICE DATASETS TO 1-HOUR TIME RESOLUTION

# Upsamle to 5 min resolution
SI_V1_17 = SI_V1_17.resample('5T').mean()
SI_V2_17 = SI_V2_17.resample('5T').mean()
SI_V3_17 = SI_V3_17.resample('5T').mean()

SI_V1_18 = SI_V1_18.resample('5T').mean()
SI_V2_18 = SI_V2_18.resample('5T').mean()
SI_V3_18 = SI_V3_18.resample('5T').mean()

# Interpolate the data
SI_V1_17 = SI_V1_17.interpolate(method='time')
SI_V2_17 = SI_V2_17.interpolate(method='time')
SI_V3_17 = SI_V3_17.interpolate(method='time')

SI_V1_18 = SI_V1_18.interpolate(method='time')
SI_V2_18 = SI_V2_18.interpolate(method='time')
SI_V3_18 = SI_V3_18.interpolate(method='time')

# Replace NaN with 0.0
SI_V1_17['ng/m3'] = SI_V1_17['ng/m3'].fillna(0)
SI_V2_17['ng/m3'] = SI_V2_17['ng/m3'].fillna(0)
SI_V3_17['ng/m3'] = SI_V3_17['ng/m3'].fillna(0)

SI_V1_18['ng/m3'] = SI_V1_18['ng/m3'].fillna(0)
SI_V2_18['ng/m3'] = SI_V2_18['ng/m3'].fillna(0)
SI_V3_18['ng/m3'] = SI_V3_18['ng/m3'].fillna(0)

# Drop Hg0 row from Sea Ice
SI_V1_17 = SI_V1_17.drop(columns=['ng/m3','surf_vmr(ppmv)'])
SI_V2_17 = SI_V2_17.drop(columns=['ng/m3','surf_vmr(ppmv)'])
SI_V3_17 = SI_V3_17.drop(columns=['ng/m3','surf_vmr(ppmv)'])

SI_V1_18 = SI_V1_18.drop(columns=['ng/m3','surf_vmr(ppmv)'])
SI_V2_18 = SI_V2_18.drop(columns=['ng/m3','surf_vmr(ppmv)'])
SI_V3_18 = SI_V3_18.drop(columns=['ng/m3','surf_vmr(ppmv)'])

#------------------------------------------------------------------------------
# MERGE THE Hg0 & SEA ICE DATAFRAMES TO ONLY INCLUDE THE SAME DATES

Hg0_V1_17  = pd.concat([Hg0_V1_17,  SI_V1_17], axis=1, join='inner')
Hg0_V2_17  = pd.concat([Hg0_V2_17,  SI_V2_17], axis=1, join='inner')
Hg0_V3_17M = pd.concat([Hg0_V3_17M, SI_V3_17], axis=1, join='inner')

Hg0_V1_18  = pd.concat([Hg0_V1_18,  SI_V1_18], axis=1, join='inner')
Hg0_V2_18  = pd.concat([Hg0_V2_18,  SI_V2_18], axis=1, join='inner')
Hg0_V3_18M = pd.concat([Hg0_V3_18M, SI_V3_18], axis=1, join='inner')

#------------------------------------------------------------------------------
# PASSIVATION ISSUE WITH CELL A ON VOYAGES V3_18M, V3_18D and V4_18 (FILTER DATA)

Filter1    = Hg0_V3_18M['Cart'] == "B"
Hg0_V3_18M = Hg0_V3_18M[Filter1]

Filter2    = Hg0_V3_18D['Cart'] == "B"
Hg0_V3_18D = Hg0_V3_18D[Filter2]

Filter3    = Hg0_V4_18['Cart'] == "B"
Hg0_V4_18  = Hg0_V4_18[Filter3]

#------------------------------------------------------------------------------
# CALCULATE RELATIVE HUMIDITY AVERAGE (Port/Strbrd)

Met_V1_17['RH_Avg']   = Met_V1_17[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V1_17
Met_V2_17['RH_Avg']   = Met_V2_17[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V2_17
Met_V3_17M['RH_Avg']  = Met_V3_17M[['rel_humidity_strbrd_percent',  'rel_humidity_port_percent']].mean(axis=1)  # V3_17
Met_V3_17D['RH_Avg']  = Met_V3_17D[['rel_humidity_strbrd_percent',  'rel_humidity_port_percent']].mean(axis=1)  # V3_17
Met_V4_17['RH_Avg']   = Met_V4_17[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V4_17

Met_V1_18['RH_Avg']   = Met_V1_18[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V1_18
Met_V2_18['RH_Avg']   = Met_V2_18[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V2_18
Met_V3_18M['RH_Avg']  = Met_V3_18M[['rel_humidity_strbrd_percent',  'rel_humidity_port_percent']].mean(axis=1)  # V3_18
Met_V3_18D['RH_Avg']  = Met_V3_18D[['rel_humidity_strbrd_percent',  'rel_humidity_port_percent']].mean(axis=1)  # V3_18
Met_V4_18['RH_Avg']   = Met_V4_18[['rel_humidity_strbrd_percent',   'rel_humidity_port_percent']].mean(axis=1)  # V4_18

Met_PCAN['RH_Avg']    = Met_PCAN[['Starboard Humidity (%)',         'Port Humidity (%)']].mean(axis=1)          # PCAN
Met_SIPEXII['RH_Avg'] = Met_SIPEXII[['rel_humidity_strbrd_percent', 'rel_humidity_port_percent']].mean(axis=1)  # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE TEMPERATURE AVERAGE (Port/Strbrd)

Met_V1_17['Temp_Avg']   = Met_V1_17[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V1_17
Met_V2_17['Temp_Avg']   = Met_V2_17[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V2_17
Met_V3_17M['Temp_Avg']  = Met_V3_17M[['temp_air_strbrd_degc',           'temp_air_port_degc']].mean(axis=1)  # V3_17
Met_V3_17D['Temp_Avg']  = Met_V3_17D[['temp_air_strbrd_degc',           'temp_air_port_degc']].mean(axis=1)  # V3_17
Met_V4_17['Temp_Avg']   = Met_V4_17[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V4_17

Met_V1_18['Temp_Avg']   = Met_V1_18[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V1_18
Met_V2_18['Temp_Avg']   = Met_V2_18[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V2_18
Met_V3_18M['Temp_Avg']  = Met_V3_18M[['temp_air_strbrd_degc',           'temp_air_port_degc']].mean(axis=1)  # V3_18
Met_V3_18D['Temp_Avg']  = Met_V3_18D[['temp_air_strbrd_degc',           'temp_air_port_degc']].mean(axis=1)  # V3_18
Met_V4_18['Temp_Avg']   = Met_V4_18[['temp_air_strbrd_degc',            'temp_air_port_degc']].mean(axis=1)  # V4_18

Met_PCAN['Temp_Avg']    = Met_PCAN[['Starboard Air Temperature (degC)', 'Port Air Temperature (degC)']].mean(axis=1) # PCAN
Met_SIPEXII['Temp_Avg'] = Met_SIPEXII[['temp_air_strbrd_degc',          'temp_air_port_degc']].mean(axis=1)  # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE SOLAR RADIATION (Port/Strbrd)

Met_V1_17['SolRad_Avg']   = Met_V1_17[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V1_17
Met_V2_17['SolRad_Avg']   = Met_V2_17[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V2_17
Met_V3_17M['SolRad_Avg']  = Met_V3_17M[['rad_slr_strbrd_wperm2',      'rad_slr_port_wperm2']].mean(axis=1)  # V3_17
Met_V3_17D['SolRad_Avg']  = Met_V3_17D[['rad_slr_strbrd_wperm2',      'rad_slr_port_wperm2']].mean(axis=1)  # V3_17
Met_V4_17['SolRad_Avg']   = Met_V4_17[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V4_17

Met_V1_18['SolRad_Avg']   = Met_V1_18[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V1_18
Met_V2_18['SolRad_Avg']   = Met_V2_18[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V2_18
Met_V3_18M['SolRad_Avg']  = Met_V3_18M[['rad_slr_strbrd_wperm2',      'rad_slr_port_wperm2']].mean(axis=1)  # V3_18
Met_V3_18D['SolRad_Avg']  = Met_V3_18D[['rad_slr_strbrd_wperm2',      'rad_slr_port_wperm2']].mean(axis=1)  # V3_18
Met_V4_18['SolRad_Avg']   = Met_V4_18[['rad_slr_strbrd_wperm2',       'rad_slr_port_wperm2']].mean(axis=1)  # V4_18

Met_PCAN['SolRad_Avg']    = Met_PCAN[['Starboard Radiometer (W/m^2)', 'Port Radiometer (W/m^2)']].mean(axis=1) # PCAN
Met_SIPEXII['SolRad_Avg'] = Met_SIPEXII[['rad_slr_strbrd_wperm2',     'rad_slr_port_wperm2']].mean(axis=1)  # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE WIND SPEED (Port/Strbrd)

Met_V1_17['WS_Avg']   = Met_V1_17[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V1_17
Met_V2_17['WS_Avg']   = Met_V2_17[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V2_17
Met_V3_17M['WS_Avg']  = Met_V3_17M[['wnd_spd_strbrd_corr_knot',       'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V3_17
Met_V3_17D['WS_Avg']  = Met_V3_17D[['wnd_spd_strbrd_corr_knot',       'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V3_17
Met_V4_17['WS_Avg']   = Met_V4_17[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V4_17

Met_V1_18['WS_Avg']   = Met_V1_18[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V1_18
Met_V2_18['WS_Avg']   = Met_V2_18[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V2_18
Met_V3_18M['WS_Avg']  = Met_V3_18M[['wnd_spd_strbrd_corr_knot',       'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V3_18
Met_V3_18D['WS_Avg']  = Met_V3_18D[['wnd_spd_strbrd_corr_knot',       'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V3_18
Met_V4_18['WS_Avg']   = Met_V4_18[['wnd_spd_strbrd_corr_knot',        'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # V4_18

Met_PCAN['WS_Avg']    = Met_PCAN[['Starboard True Wind Speed (knot)', 'Port True Wind Speed (knot)']].mean(axis=1) * 0.514444444 # PCAN
Met_SIPEXII['WS_Avg'] = Met_SIPEXII[['wnd_spd_strbrd_corr_knot',      'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444 # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE WIND DIRECTION (Port/Strbrd)

Met_V1_17['WD_Avg']   = Met_V1_17[['wnd_dir_strbrd_corr_deg',               'wnd_dir_port_corr_deg']].mean(axis=1) # V1_17
Met_V2_17['WD_Avg']   = Met_V2_17[['wnd_dir_strbrd_corr_deg',               'wnd_dir_port_corr_deg']].mean(axis=1) # V2_17
Met_V3_17M['WD_Avg']  = Met_V3_17M[['wnd_dir_strbrd_corr_deg',              'wnd_dir_port_corr_deg']].mean(axis=1) # V3_17
Met_V3_17D['WD_Avg']  = Met_V3_17D[['wnd_dir_strbrd_corr_deg',              'wnd_dir_port_corr_deg']].mean(axis=1) # V3_17
Met_V4_17['WD_Avg']   = Met_V4_17[['wnd_dir_strbrd_corr_deg',               'wnd_dir_port_corr_deg']].mean(axis=1) # V4_17

Met_V1_18['WD_Avg']   = Met_V1_18[['wnd_dir_strbrd_corr_deg',               'wnd_dir_port_corr_deg']].mean(axis=1) # V1_18
Met_V2_18['WD_Avg']   = Met_V2_18[['wnd_dir_strbrd_corr_deg',               'wnd_dir_port_corr_deg']].mean(axis=1) # V2_18
Met_V3_18M['WD_Avg']  = Met_V3_18M[['wnd_dir_strbrd_corr_deg',              'wnd_dir_port_corr_deg']].mean(axis=1) # V3_18
Met_V3_18D['WD_Avg']  = Met_V3_18D[['wnd_dir_strbrd_corr_deg',              'wnd_dir_port_corr_deg']].mean(axis=1) # V3_18
Met_V4_18['WD_Avg']   = Met_V4_18[['wnd_dir_strbrd_corr_deg',               'wnd_dir_port_corr_deg']].mean(axis=1) # V4_18

Met_PCAN['WD_Avg']    = Met_PCAN[['Starboard True Wind Direction (degree)', 'Port True Wind Direction (degree)']].mean(axis=1) # PCAN
Met_SIPEXII['WD_Avg'] = Met_SIPEXII[['wnd_dir_strbrd_corr_deg',             'wnd_dir_port_corr_deg']].mean(axis=1) # SIPEXII

#------------------------------------------------------------------------------
# DAILY VALUES (MEAN, MIN, MAX)

# #----------
# # Hg0
# #----------
# # Calculate
# Stat_Hg0_V1_17 = Hg0_V1_17['ng/m3'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Hg0_V2_17 = Hg0_V2_17['ng/m3'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Hg0_V3_17 = Hg0_V3_17M['ng/m3'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Hg0_V1_18 = Hg0_V1_18['ng/m3'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Hg0_V2_18 = Hg0_V2_18['ng/m3'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Hg0_V3_18 = Hg0_V3_18M['ng/m3'].resample('D').agg(['mean','std','median','mad','min', 'max'])

# # # Save as .csv
# # Stat_Hg0_V1_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Hg0_V1_17.csv')
# # Stat_Hg0_V2_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Hg0_V2_17.csv')
# # Stat_Hg0_V3_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Hg0_V3_17.csv')
# # Stat_Hg0_V1_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Hg0_V1_18.csv')
# # Stat_Hg0_V2_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Hg0_V2_18.csv')
# # Stat_Hg0_V3_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Hg0_V3_18.csv')

# #----------
# # O3
# #----------
# # Calculate
# Stat_O3_V1_17 = O3_V1_17['O3_(ppb)'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_O3_V2_17 = O3_V2_17['O3_(ppb)'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_O3_V3_17 = O3_V3_17M['O3_(ppb)'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_O3_V1_18 = O3_V1_18['O3_(ppb)'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_O3_V2_18 = O3_V2_18['O3_(ppb)'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_O3_V3_18 = O3_V3_18M['O3_(ppb)'].resample('D').agg(['mean','std','median','mad','min', 'max'])

# # Save as .csv
# Stat_O3_V1_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_O3_V1_17.csv')
# Stat_O3_V2_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_O3_V2_17.csv')
# Stat_O3_V3_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_O3_V3_17.csv')
# Stat_O3_V1_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_O3_V1_18.csv')
# Stat_O3_V2_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_O3_V2_18.csv')
# Stat_O3_V3_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_O3_V3_18.csv')

# #----------
# # BrO
# #----------
# # Calculate'surf_vmr(ppmv)']) * 1e6
# Stat_BrO_V1_17 = BrO_V1_17['surf_vmr(ppmv)'].resample('D').agg(['mean','std','median','mad','min', 'max']) * 1e6
# Stat_BrO_V2_17 = BrO_V2_17['surf_vmr(ppmv)'].resample('D').agg(['mean','std','median','mad','min', 'max']) * 1e6
# Stat_BrO_V3_17 = BrO_V3_17M['surf_vmr(ppmv)'].resample('D').agg(['mean','std','median','mad','min', 'max']) * 1e6
# Stat_BrO_V1_18 = BrO_V1_18['surf_vmr(ppmv)'].resample('D').agg(['mean','std','median','mad','min', 'max']) * 1e6
# Stat_BrO_V2_18 = BrO_V2_18['surf_vmr(ppmv)'].resample('D').agg(['mean','std','median','mad','min', 'max']) * 1e6
# Stat_BrO_V3_18 = BrO_V3_18M['surf_vmr(ppmv)'].resample('D').agg(['mean','std','median','mad','min', 'max']) * 1e6

# # Save as .csv
# Stat_BrO_V1_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_BrO_V1_17.csv')
# Stat_BrO_V2_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_BrO_V2_17.csv')
# Stat_BrO_V3_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_BrO_V3_17.csv')
# Stat_BrO_V1_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_BrO_V1_18.csv')
# Stat_BrO_V2_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_BrO_V2_18.csv')
# Stat_BrO_V3_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_BrO_V3_18.csv')

# #----------
# # Relative Humidity
# #----------
# Stat_RH_V1_17 = Met_V1_17['RH_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_RH_V2_17 = Met_V2_17['RH_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_RH_V3_17 = Met_V3_17M['RH_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_RH_V1_18 = Met_V1_18['RH_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_RH_V2_18 = Met_V2_18['RH_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_RH_V3_18 = Met_V3_18M['RH_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])

# # Save as .csv
# Stat_RH_V1_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_RH_V1_17.csv')
# Stat_RH_V2_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_RH_V2_17.csv')
# Stat_RH_V3_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_RH_V3_17.csv')
# Stat_RH_V1_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_RH_V1_18.csv')
# Stat_RH_V2_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_RH_V2_18.csv')
# Stat_RH_V3_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_RH_V3_18.csv')

# #----------
# # Temperature
# #----------
# Stat_Temp_V1_17 = Met_V1_17['Temp_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Temp_V2_17 = Met_V2_17['Temp_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Temp_V3_17 = Met_V3_17M['Temp_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Temp_V1_18 = Met_V1_18['Temp_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Temp_V2_18 = Met_V2_18['Temp_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_Temp_V3_18 = Met_V3_18M['Temp_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])

# # Save as .csv
# Stat_Temp_V1_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Temp_V1_17.csv')
# Stat_Temp_V2_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Temp_V2_17.csv')
# Stat_Temp_V3_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Temp_V3_17.csv')
# Stat_Temp_V1_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Temp_V1_18.csv')
# Stat_Temp_V2_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Temp_V2_18.csv')
# Stat_Temp_V3_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_Temp_V3_18.csv')

# #----------
# # Solar Radiation
# #----------
# Stat_SolRad_V1_17 = Met_V1_17['SolRad_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_SolRad_V2_17 = Met_V2_17['SolRad_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_SolRad_V3_17 = Met_V3_17M['SolRad_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_SolRad_V1_18 = Met_V1_18['SolRad_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_SolRad_V2_18 = Met_V2_18['SolRad_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_SolRad_V3_18 = Met_V3_18M['SolRad_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])

# # Save as .csv
# Stat_SolRad_V1_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_SolRad_V1_17.csv')
# Stat_SolRad_V2_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_SolRad_V2_17.csv')
# Stat_SolRad_V3_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_SolRad_V3_17.csv')
# Stat_SolRad_V1_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_SolRad_V1_18.csv')
# Stat_SolRad_V2_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_SolRad_V2_18.csv')
# Stat_SolRad_V3_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_SolRad_V3_18.csv')

# #----------
# # Wind Speed
# #----------
# Stat_WS_V1_17 = Met_V1_17['WS_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WS_V2_17 = Met_V2_17['WS_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WS_V3_17 = Met_V3_17M['WS_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WS_V1_18 = Met_V1_18['WS_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WS_V2_18 = Met_V2_18['WS_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WS_V3_18 = Met_V3_18M['WS_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])

# # Save as .csv
# Stat_WS_V1_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WS_V1_17.csv')
# Stat_WS_V2_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WS_V2_17.csv')
# Stat_WS_V3_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WS_V3_17.csv')
# Stat_WS_V1_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WS_V1_18.csv')
# Stat_WS_V2_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WS_V2_18.csv')
# Stat_WS_V3_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WS_V3_18.csv')

# #----------
# # Wind Direction
# #----------
# Stat_WD_V1_17 = Met_V1_17['WD_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WD_V2_17 = Met_V2_17['WD_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WD_V3_17 = Met_V3_17M['WD_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WD_V1_18 = Met_V1_18['WD_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WD_V2_18 = Met_V2_18['WD_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])
# Stat_WD_V3_18 = Met_V3_18M['WD_Avg'].resample('D').agg(['mean','std','median','mad','min', 'max'])

# # Save as .csv
# Stat_WD_V1_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WD_V1_17.csv')
# Stat_WD_V2_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WD_V2_17.csv')
# Stat_WD_V3_17.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WD_V3_17.csv')
# Stat_WD_V1_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WD_V1_18.csv')
# Stat_WD_V2_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WD_V2_18.csv')
# Stat_WD_V3_18.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Stat_WD_V3_18.csv')

#------------------------------------------------------------------------------
# SEPERATE THE DATASETS FOR SEA ICE & OPEN WATER

# Sea Ice
Filter        = Hg0_V1_17['Sea Ice Conc (0-1)']  > 0
Hg0_Ice_V1_17 = Hg0_V1_17[Filter]

Filter        = Hg0_V2_17['Sea Ice Conc (0-1)']  > 0
Hg0_Ice_V2_17 = Hg0_V2_17[Filter]

Filter        = Hg0_V3_17M['Sea Ice Conc (0-1)'] > 0
Hg0_Ice_V3_17 = Hg0_V3_17M[Filter]

Filter        = Hg0_V1_18['Sea Ice Conc (0-1)']  > 0
Hg0_Ice_V1_18 = Hg0_V1_18[Filter]

Filter        = Hg0_V2_18['Sea Ice Conc (0-1)']  > 0
Hg0_Ice_V2_18 = Hg0_V2_18[Filter]

Filter        = Hg0_V3_18M['Sea Ice Conc (0-1)'] > 0
Hg0_Ice_V3_18 = Hg0_V3_18M[Filter]

# Open Water
Filter        = Hg0_V1_17['Sea Ice Conc (0-1)']  == 0
Hg0_OW_V1_17  = Hg0_V1_17[Filter]

Filter        = Hg0_V2_17['Sea Ice Conc (0-1)']  == 0
Hg0_OW_V2_17  = Hg0_V2_17[Filter]

Filter        = Hg0_V3_17M['Sea Ice Conc (0-1)'] == 0
Hg0_OW_V3_17  = Hg0_V3_17M[Filter]

Filter        = Hg0_V1_18['Sea Ice Conc (0-1)']  == 0
Hg0_OW_V1_18  = Hg0_V1_18[Filter]

Filter        = Hg0_V2_18['Sea Ice Conc (0-1)']  == 0
Hg0_OW_V2_18  = Hg0_V2_18[Filter]

Filter        = Hg0_V3_18M['Sea Ice Conc (0-1)'] == 0
Hg0_OW_V3_18  = Hg0_V3_18M[Filter]

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
# Define the variables

#-----------------------------
# Whole voyage
#-----------------------------
# Hg0
PCAN_Hg0        = np.array(Hg0_PCAN['ng/m3'])
SIPEXII_Hg0     = np.array(Hg0_SIPEXII['ng/m3'])

V1_17_Hg0       = np.array(Hg0_V1_17['ng/m3'])
V2_17_Hg0       = np.array(Hg0_V2_17['ng/m3'])
V3_17M_Hg0      = np.array(Hg0_V3_17M['ng/m3'])
V3_17D_Hg0      = np.array(Hg0_V3_17D['ng/m3'])
V4_17_Hg0       = np.array(Hg0_V4_17['ng/m3'])

V1_18_Hg0       = np.array(Hg0_V1_18['ng/m3'])
V2_18_Hg0       = np.array(Hg0_V2_18['ng/m3'])
V3_18M_Hg0      = np.array(Hg0_V3_18M['ng/m3'])
V3_18D_Hg0      = np.array(Hg0_V3_18D['ng/m3'])
V4_18_Hg0       = np.array(Hg0_V4_18['ng/m3'])

# BrO
SIPEXII_BrO     = np.array(BrO_SIPEXII['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

V1_17_BrO       = np.array(BrO_V1_17['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to pptv
V2_17_BrO       = np.array(BrO_V2_17['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to pptv
V3_17M_BrO      = np.array(BrO_V3_17M['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
V3_17D_BrO      = np.array(BrO_V3_17D['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv

V1_18_BrO       = np.array(BrO_V1_18['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to pptv
V2_18_BrO       = np.array(BrO_V2_18['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to pptv
V3_18M_BrO      = np.array(BrO_V3_18M['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
V3_18D_BrO      = np.array(BrO_V3_18D['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv

# O3
SIPEXII_O3     = np.array(O3_SIPEXII['O3_(ppb)'])
PCAN_O3        = np.array(O3_PCAN['O3_(ppb)'])
V1_17_O3       = np.array(O3_V1_17['O3_(ppb)'])
V2_17_O3       = np.array(O3_V2_17['O3_(ppb)'])
V3_17M_O3      = np.array(O3_V3_17M['O3_(ppb)'])
V3_17D_O3      = np.array(O3_V3_17D['O3_(ppb)'])
V4_17_O3       = np.array(O3_V4_17['O3_(ppb)'])

V1_18_O3       = np.array(O3_V1_18['O3_(ppb)'])
V2_18_O3       = np.array(O3_V2_18['O3_(ppb)'])
V3_18M_O3      = np.array(O3_V3_18M['O3_(ppb)'])
V3_18D_O3      = np.array(O3_V3_18D['O3_(ppb)'])
V4_18_O3       = np.array(O3_V4_18['O3_(ppb)'])

#-----------------------------
# At station
#-----------------------------
# Hg0
Hg0_PCAN_17    = np.array(Hg0_PCAN_Ice['ng/m3'])
Hg0_SIPEXII_12 = np.array(Hg0_SIPEXII_Ice['ng/m3'])

Hg0_Davis1_17  = np.array(Hg0_Davis_V1_17['ng/m3'])
Hg0_Casey_17   = np.array(Hg0_Casey_V2_17['ng/m3'])
Hg0_Mawson_17  = np.array(Hg0_Mawson_V3_17['ng/m3'])
Hg0_Davis3_17  = np.array(Hg0_Davis_V3_17['ng/m3'])
Hg0_MQIsl_17   = np.array(Hg0_MQIsl_V4_17['ng/m3'])

Hg0_Davis1_18  = np.array(Hg0_Davis_V1_18['ng/m3'])
Hg0_Casey_18   = np.array(Hg0_Casey_V2_18['ng/m3'])
Hg0_Mawson_18  = np.array(Hg0_Mawson_V3_18['ng/m3'])
Hg0_Davis3_18  = np.array(Hg0_Davis_V3_18['ng/m3'])
Hg0_MQIsl_18   = np.array(Hg0_MQIsl_V4_18['ng/m3'])

# BrO
BrO_SIPEXII_12 = np.array(BrO_SIPEXII_Ice['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv

BrO_Davis1_17  = np.array(BrO_Davis_V1_17['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
BrO_Casey_17   = np.array(BrO_Casey_V2_17['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
BrO_Mawson_17  = np.array(BrO_Mawson_V3_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_Davis3_17  = np.array(BrO_Davis_V3_17['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv

BrO_Davis1_18  = np.array(BrO_Davis_V1_18['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
BrO_Casey_18   = np.array(BrO_Casey_V2_18['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
BrO_Mawson_18  = np.array(BrO_Mawson_V3_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_Davis3_18  = np.array(BrO_Davis_V3_18['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv

# O3
O3_SIPEXII_12 = np.array(O3_SIPEXII_Ice['O3_(ppb)'])
O3_PCAN_17    = np.array(O3_PCAN_Ice['O3_(ppb)'])

O3_Davis1_17  = np.array(O3_Davis_V1_17['O3_(ppb)'])
O3_Casey_17   = np.array(O3_Casey_V2_17['O3_(ppb)'])
O3_Mawson_17  = np.array(O3_Mawson_V3_17['O3_(ppb)'])
O3_Davis3_17  = np.array(O3_Davis_V3_17['O3_(ppb)'])
O3_MQIsl_17   = np.array(O3_MQIsl_V4_17['O3_(ppb)'])

O3_Davis1_18  = np.array(O3_Davis_V1_18['O3_(ppb)'])
O3_Casey_18   = np.array(O3_Casey_V2_18['O3_(ppb)'])
O3_Mawson_18  = np.array(O3_Mawson_V3_18['O3_(ppb)'])
O3_Davis3_18  = np.array(O3_Davis_V3_18['O3_(ppb)'])
O3_MQIsl_18   = np.array(O3_MQIsl_V4_18['O3_(ppb)'])

#-----------------------------
# Sea ice
#-----------------------------
# Hg0
Hg0_Ice1_V1_17 = np.array(Hg0_Ice_V1_17['ng/m3'])
Hg0_Ice1_V2_17 = np.array(Hg0_Ice_V2_17['ng/m3'])
Hg0_Ice1_V3_17 = np.array(Hg0_Ice_V3_17['ng/m3'])

Hg0_Ice1_V1_18 = np.array(Hg0_Ice_V1_18['ng/m3'])
Hg0_Ice1_V2_18 = np.array(Hg0_Ice_V2_18['ng/m3'])
Hg0_Ice1_V3_18 = np.array(Hg0_Ice_V3_18['ng/m3'])

#-----------------------------
# Open water
#-----------------------------
# Hg0
Hg0_OW1_V1_17 = np.array(Hg0_OW_V1_17['ng/m3'])
Hg0_OW1_V2_17 = np.array(Hg0_OW_V2_17['ng/m3'])
Hg0_OW1_V3_17 = np.array(Hg0_OW_V3_17['ng/m3'])

Hg0_OW1_V1_18 = np.array(Hg0_OW_V1_18['ng/m3'])
Hg0_OW1_V2_18 = np.array(Hg0_OW_V2_18['ng/m3'])
Hg0_OW1_V3_18 = np.array(Hg0_OW_V3_18['ng/m3'])

#------------------------------------------------------------------------------
# SET THE DATE AND TIME (Hg0)

#------------------------------------
# Whole Voyage
#------------------------------------
# V1_17
tim1a = np.array(Hg0_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1a=[]
for i in range(len(tim1a)):
    test = datetime.strptime(tim1a[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1a.append(test)

# V2_17
tim2a = np.array(Hg0_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2a=[]
for i in range(len(tim2a)):
    test = datetime.strptime(tim2a[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2a.append(test)

# V3_17M
tim3a = np.array(Hg0_V3_17M['Time'])

#CONVERT TO DATETIME FROM STRING
time3a=[]
for i in range(len(tim3a)):
    test = datetime.strptime(tim3a[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3a.append(test)

# V3_17D
tim4a = np.array(Hg0_V3_17D['Time'])

#CONVERT TO DATETIME FROM STRING
time4a=[]
for i in range(len(tim4a)):
    test = datetime.strptime(tim4a[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4a.append(test)
    
# V4_17
tim5a = np.array(Hg0_V4_17['Time'])

#CONVERT TO DATETIME FROM STRING
time5a=[]
for i in range(len(tim5a)):
    test = datetime.strptime(tim5a[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time5a.append(test)
    
# V1_18
tim6a = np.array(Hg0_V1_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6a=[]
for i in range(len(tim6a)):
    test = datetime.strptime(tim6a[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time6a.append(test)

# V2_18
tim7a = np.array(Hg0_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time7a=[]
for i in range(len(tim7a)):
    test = datetime.strptime(tim7a[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time7a.append(test)

# V3_18M
tim8a = np.array(Hg0_V3_18M['Time'])

#CONVERT TO DATETIME FROM STRING
time8a=[]
for i in range(len(tim8a)):
    test = datetime.strptime(tim8a[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time8a.append(test)

# V3_18D
tim9a = np.array(Hg0_V3_18D['Time'])

#CONVERT TO DATETIME FROM STRING
time9a=[]
for i in range(len(tim9a)):
    test = datetime.strptime(tim9a[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time9a.append(test)
    
# V4_18
tim10a = np.array(Hg0_V4_18['Time'])

#CONVERT TO DATETIME FROM STRING
time10a=[]
for i in range(len(tim10a)):
    test = datetime.strptime(tim10a[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time10a.append(test)
    
# PCAN
tim11a = np.array(Hg0_PCAN['Time'])

#CONVERT TO DATETIME FROM STRING
time11a=[]
for i in range(len(tim11a)):
    test = datetime.strptime(tim11a[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time11a.append(test)
    
# SIPEXII
tim12a = np.array(Hg0_SIPEXII['Time'])

#CONVERT TO DATETIME FROM STRING
time12a=[]
for i in range(len(tim12a)):
    test = datetime.strptime(tim12a[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time12a.append(test)

#------------------------------------
# At Station
#------------------------------------
# Davis (V1_17)
tim1b = np.array(Hg0_Davis_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1b=[]
for i in range(len(tim1b)):
    test = datetime.strptime(tim1b[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1b.append(test)

# Casey (V2_17)
tim2b = np.array(Hg0_Casey_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2b=[]
for i in range(len(tim2b)):
    test = datetime.strptime(tim2b[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2b.append(test)

# Mawson (V3_17)
tim3b = np.array(Hg0_Mawson_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time3b=[]
for i in range(len(tim3b)):
    test = datetime.strptime(tim3b[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3b.append(test)

# Davis (V3_17)
tim4b = np.array(Hg0_Davis_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time4b=[]
for i in range(len(tim4b)):
    test = datetime.strptime(tim4b[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4b.append(test)
    
# Macquarie Island (V4_17)
tim5b = np.array(Hg0_MQIsl_V4_17['Time'])

#CONVERT TO DATETIME FROM STRING
time5b=[]
for i in range(len(tim5b)):
    test = datetime.strptime(tim5b[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time5b.append(test)
    
# Davis (V1_18)
tim6b = np.array(Hg0_Davis_V1_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6b=[]
for i in range(len(tim6b)):
    test = datetime.strptime(tim6b[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time6b.append(test)

# Casey (V2_18)
tim7b = np.array(Hg0_Casey_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time7b=[]
for i in range(len(tim7b)):
    test = datetime.strptime(tim7b[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time7b.append(test)

# Mawson (V3_18)
tim8b = np.array(Hg0_Mawson_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time8b=[]
for i in range(len(tim8b)):
    test = datetime.strptime(tim8b[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time8b.append(test)

# Davis (V3_18)
tim9b = np.array(Hg0_Davis_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time9b=[]
for i in range(len(tim9b)):
    test = datetime.strptime(tim9b[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time9b.append(test)
    
# Macquarie Island (V4_18)
tim10b = np.array(Hg0_MQIsl_V4_18['Time'])

#CONVERT TO DATETIME FROM STRING
time10b=[]
for i in range(len(tim10b)):
    test = datetime.strptime(tim10b[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time10b.append(test)
    
# PCAN
tim11b = np.array(Hg0_PCAN_Ice['Time'])

#CONVERT TO DATETIME FROM STRING
time11b=[]
for i in range(len(tim11b)):
    test = datetime.strptime(tim11b[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time11b.append(test)
    
# SIPEXII
tim12b = np.array(Hg0_SIPEXII_Ice['Time'])

#CONVERT TO DATETIME FROM STRING
time12b=[]
for i in range(len(tim12b)):
    test = datetime.strptime(tim12b[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time12b.append(test)
    
#------------------------------------
# Sea Ice
#------------------------------------
# V1_17
tim1c = np.array(Hg0_Ice_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1c=[]
for i in range(len(tim1c)):
    test = datetime.strptime(tim1c[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1c.append(test)

# V2_17
tim2c = np.array(Hg0_Ice_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2c=[]
for i in range(len(tim2c)):
    test = datetime.strptime(tim2c[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2c.append(test)
    
# V3_17
tim3c = np.array(Hg0_Ice_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time3c=[]
for i in range(len(tim3c)):
    test = datetime.strptime(tim3c[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3c.append(test)

# V1_18
tim4c = np.array(Hg0_Ice_V1_18['Time'])
#CONVERT TO DATETIME FROM STRING
time4c=[]
for i in range(len(tim4c)):
    test = datetime.strptime(tim4c[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4c.append(test)

# V2_18
tim5c = np.array(Hg0_Ice_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time5c=[]
for i in range(len(tim5c)):
    test = datetime.strptime(tim5c[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time5c.append(test)

# V3_18
tim6c = np.array(Hg0_Ice_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6c=[]
for i in range(len(tim6c)):
    test = datetime.strptime(tim6c[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time6c.append(test)

#------------------------------------
# Open Water
#------------------------------------
# V1_17
tim1d = np.array(Hg0_OW_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1d=[]
for i in range(len(tim1d)):
    test = datetime.strptime(tim1d[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1d.append(test)

# V2_17
tim2d = np.array(Hg0_OW_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2d=[]
for i in range(len(tim2d)):
    test = datetime.strptime(tim2d[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2d.append(test)
    
# V3_17
tim3d = np.array(Hg0_OW_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time3d=[]
for i in range(len(tim3d)):
    test = datetime.strptime(tim3d[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3d.append(test)

# V1_18
tim4d = np.array(Hg0_OW_V1_18['Time'])
#CONVERT TO DATETIME FROM STRING
time4d=[]
for i in range(len(tim4d)):
    test = datetime.strptime(tim4d[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4d.append(test)

# V2_18
tim5d = np.array(Hg0_OW_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time5d=[]
for i in range(len(tim5d)):
    test = datetime.strptime(tim5d[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time5d.append(test)
    
# V3_18
tim6d = np.array(Hg0_OW_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6d=[]
for i in range(len(tim6d)):
    test = datetime.strptime(tim6d[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time6d.append(test)
    
#------------------------------------------------------------------------------
# SET THE DATE AND TIME (BrO)

#------------------------------------
# Whole Voyage
#------------------------------------
# V1_17
tim1z = np.array(BrO_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1z=[]
for i in range(len(tim1z)):
    test = datetime.strptime(tim1z[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1z.append(test)
    
# V2_17
tim2z = np.array(BrO_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2z=[]
for i in range(len(tim2z)):
    test = datetime.strptime(tim2z[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2z.append(test)
    
# V3_17M
tim3z = np.array(BrO_V3_17M['Time'])

#CONVERT TO DATETIME FROM STRING
time3z=[]
for i in range(len(tim3z)):
    test = datetime.strptime(tim3z[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3z.append(test)
    
# V3_17D
tim4z = np.array(BrO_V3_17D['Time'])

#CONVERT TO DATETIME FROM STRING
time4z=[]
for i in range(len(tim4z)):
    test = datetime.strptime(tim4z[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4z.append(test)
    
# V1_18
tim5z = np.array(BrO_V1_18['Time'])

#CONVERT TO DATETIME FROM STRING
time5z=[]
for i in range(len(tim5z)):
    test = datetime.strptime(tim5z[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time5z.append(test)
    
# V2_18
tim6z = np.array(BrO_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6z=[]
for i in range(len(tim6z)):
    test = datetime.strptime(tim6z[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time6z.append(test)
    
# V3_18M
tim7z = np.array(BrO_V3_18M['Time'])

#CONVERT TO DATETIME FROM STRING
time7z=[]
for i in range(len(tim7z)):
    test = datetime.strptime(tim7z[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time7z.append(test)

# V3_18D
tim8z = np.array(BrO_V3_18D['Time'])

#CONVERT TO DATETIME FROM STRING
time8z=[]
for i in range(len(tim8z)):
    test = datetime.strptime(tim8z[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time8z.append(test)
    
# SIPEXII
tim9z = np.array(BrO_SIPEXII['Time'])

#CONVERT TO DATETIME FROM STRING
time9z=[]
for i in range(len(tim9z)):
    test = datetime.strptime(tim9z[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time9z.append(test)
    
#------------------------------------
# At Station
#------------------------------------
# Davis (V1_17)
tim1y = np.array(BrO_Davis_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1y=[]
for i in range(len(tim1y)):
    test = datetime.strptime(tim1y[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1y.append(test)
    
# Casey (V2_17)
tim2y = np.array(BrO_Casey_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2y=[]
for i in range(len(tim2y)):
    test = datetime.strptime(tim2y[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2y.append(test)
    
# Mawson (V3_17)
tim3y = np.array(BrO_Mawson_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time3y=[]
for i in range(len(tim3y)):
    test = datetime.strptime(tim3y[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3y.append(test)
    
# Davis (V3_17)
tim4y = np.array(BrO_Davis_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time4y=[]
for i in range(len(tim4y)):
    test = datetime.strptime(tim4y[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4y.append(test)
    
# Davis (V1_18)
tim5y = np.array(BrO_Davis_V1_18['Time'])

#CONVERT TO DATETIME FROM STRING
time5y=[]
for i in range(len(tim5y)):
    test = datetime.strptime(tim5y[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time5y.append(test)
    
# Casey (V2_18)
tim6y = np.array(BrO_Casey_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6y=[]
for i in range(len(tim6y)):
    test = datetime.strptime(tim6y[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time6y.append(test)
    
# Mawson (V3_18)
tim7y = np.array(BrO_Mawson_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time7y=[]
for i in range(len(tim7y)):
    test = datetime.strptime(tim7y[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time7y.append(test)
    
# Davis (V3_18)
tim8y = np.array(BrO_Davis_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time8y=[]
for i in range(len(tim8y)):
    test = datetime.strptime(tim8y[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time8y.append(test)
    
# SIPEXII
tim9y = np.array(BrO_SIPEXII_Ice['Time'])

#CONVERT TO DATETIME FROM STRING
time9y=[]
for i in range(len(tim9y)):
    test = datetime.strptime(tim9y[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time9y.append(test)

#------------------------------------------------------------------------------
# SET THE DATE AND TIME (O3)

#------------------------------------
# Whole Voyage
#------------------------------------
# V1_17
tim1a_O3 = np.array(O3_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1a_O3=[]
for i in range(len(tim1a_O3)):
    test = datetime.strptime(tim1a_O3[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1a_O3.append(test)

# V2_17
tim2a_O3 = np.array(O3_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2a_O3=[]
for i in range(len(tim2a_O3)):
    test = datetime.strptime(tim2a_O3[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2a_O3.append(test)

# V3_17M
tim3a_O3 = np.array(O3_V3_17M['Time'])

#CONVERT TO DATETIME FROM STRING
time3a_O3=[]
for i in range(len(tim3a_O3)):
    test = datetime.strptime(tim3a_O3[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3a_O3.append(test)

# V3_17D
tim4a_O3 = np.array(O3_V3_17D['Time'])

#CONVERT TO DATETIME FROM STRING
time4a_O3=[]
for i in range(len(tim4a_O3)):
    test = datetime.strptime(tim4a_O3[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4a_O3.append(test)
    
# V4_17
tim5a_O3 = np.array(O3_V4_17['Time'])

#CONVERT TO DATETIME FROM STRING
time5a_O3=[]
for i in range(len(tim5a_O3)):
    test = datetime.strptime(tim5a_O3[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time5a_O3.append(test)
    
# V1_18
tim6a_O3 = np.array(O3_V1_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6a_O3=[]
for i in range(len(tim6a_O3)):
    test = datetime.strptime(tim6a_O3[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time6a_O3.append(test)

# V2_18
tim7a_O3 = np.array(O3_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time7a_O3=[]
for i in range(len(tim7a_O3)):
    test = datetime.strptime(tim7a_O3[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time7a_O3.append(test)

# V3_18M
tim8a_O3 = np.array(O3_V3_18M['Time'])

#CONVERT TO DATETIME FROM STRING
time8a_O3=[]
for i in range(len(tim8a_O3)):
    test = datetime.strptime(tim8a_O3[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time8a_O3.append(test)

# V3_18D
tim9a_O3 = np.array(O3_V3_18D['Time'])

#CONVERT TO DATETIME FROM STRING
time9a_O3=[]
for i in range(len(tim9a_O3)):
    test = datetime.strptime(tim9a_O3[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time9a_O3.append(test)
    
# V4_18
tim10a_O3 = np.array(O3_V4_18['Time'])

#CONVERT TO DATETIME FROM STRING
time10a_O3=[]
for i in range(len(tim10a_O3)):
    test = datetime.strptime(tim10a_O3[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time10a_O3.append(test)
    
# PCAN
tim11a_O3 = np.array(O3_PCAN['Time'])

#CONVERT TO DATETIME FROM STRING
time11a_O3=[]
for i in range(len(tim11a_O3)):
    test = datetime.strptime(tim11a_O3[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time11a_O3.append(test)
    
# SIPEXII
tim12a_O3 = np.array(O3_SIPEXII['Time'])

#CONVERT TO DATETIME FROM STRING
time12a_O3=[]
for i in range(len(tim12a_O3)):
    test = datetime.strptime(tim12a_O3[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time12a_O3.append(test)

#------------------------------------
# At Station
#------------------------------------
# Davis (V1_17)
tim1b_O3 = np.array(O3_Davis_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1b_O3=[]
for i in range(len(tim1b_O3)):
    test = datetime.strptime(tim1b_O3[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1b_O3.append(test)

# Casey (V2_17)
tim2b_O3 = np.array(O3_Casey_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2b_O3=[]
for i in range(len(tim2b_O3)):
    test = datetime.strptime(tim2b_O3[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2b_O3.append(test)

# Mawson (V3_17)
tim3b_O3 = np.array(O3_Mawson_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time3b_O3=[]
for i in range(len(tim3b_O3)):
    test = datetime.strptime(tim3b_O3[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3b_O3.append(test)

# Davis (V3_17)
tim4b_O3 = np.array(O3_Davis_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time4b_O3=[]
for i in range(len(tim4b_O3)):
    test = datetime.strptime(tim4b_O3[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4b_O3.append(test)
    
# Macquarie Island (V4_17)
tim5b_O3 = np.array(O3_MQIsl_V4_17['Time'])

#CONVERT TO DATETIME FROM STRING
time5b_O3=[]
for i in range(len(tim5b_O3)):
    test = datetime.strptime(tim5b_O3[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time5b_O3.append(test)
    
# Davis (V1_18)
tim6b_O3 = np.array(O3_Davis_V1_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6b_O3=[]
for i in range(len(tim6b_O3)):
    test = datetime.strptime(tim6b_O3[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time6b_O3.append(test)

# Casey (V2_18)
tim7b_O3 = np.array(O3_Casey_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time7b_O3=[]
for i in range(len(tim7b_O3)):
    test = datetime.strptime(tim7b_O3[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time7b_O3.append(test)

# Mawson (V3_18)
tim8b_O3 = np.array(O3_Mawson_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time8b_O3=[]
for i in range(len(tim8b_O3)):
    test = datetime.strptime(tim8b_O3[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time8b_O3.append(test)

# Davis (V3_18)
tim9b_O3 = np.array(O3_Davis_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time9b_O3=[]
for i in range(len(tim9b_O3)):
    test = datetime.strptime(tim9b_O3[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time9b_O3.append(test)
    
# Macquarie Island (V4_18)
tim10b_O3 = np.array(O3_MQIsl_V4_18['Time'])

#CONVERT TO DATETIME FROM STRING
time10b_O3=[]
for i in range(len(tim10b_O3)):
    test = datetime.strptime(tim10b_O3[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time10b_O3.append(test)

# PCAN
tim11b_O3 = np.array(O3_PCAN_Ice['Time'])

#CONVERT TO DATETIME FROM STRING
time11b_O3=[]
for i in range(len(tim11b_O3)):
    test = datetime.strptime(tim11b_O3[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time11b_O3.append(test)
    
# SIPEXII
tim12b_O3 = np.array(O3_SIPEXII_Ice['Time'])

#CONVERT TO DATETIME FROM STRING
time12b_O3=[]
for i in range(len(tim12b_O3)):
    test = datetime.strptime(tim12b_O3[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time12b_O3.append(test)

#------------------------------------------------------------------------------
# SET THE DATE AND TIME (Met)

#------------------------------------
# Whole Voyage
#------------------------------------
# V1_17
tim1a_Met = np.array(Met_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1a_Met=[]
for i in range(len(tim1a_Met)):
    test = datetime.strptime(tim1a_Met[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1a_Met.append(test)

# V2_17
tim2a_Met = np.array(Met_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2a_Met=[]
for i in range(len(tim2a_Met)):
    test = datetime.strptime(tim2a_Met[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2a_Met.append(test)

# V3_17M
tim3a_Met = np.array(Met_V3_17M['Time'])

#CONVERT TO DATETIME FROM STRING
time3a_Met=[]
for i in range(len(tim3a_Met)):
    test = datetime.strptime(tim3a_Met[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3a_Met.append(test)

# V3_17D
tim4a_Met = np.array(Met_V3_17D['Time'])

#CONVERT TO DATETIME FROM STRING
time4a_Met=[]
for i in range(len(tim4a_Met)):
    test = datetime.strptime(tim4a_Met[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4a_Met.append(test)
    
# V4_17
tim5a_Met = np.array(Met_V4_17['Time'])

#CONVERT TO DATETIME FROM STRING
time5a_Met=[]
for i in range(len(tim5a_Met)):
    test = datetime.strptime(tim5a_Met[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time5a_Met.append(test)
    
# V1_18
tim6a_Met = np.array(Met_V1_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6a_Met=[]
for i in range(len(tim6a_Met)):
    test = datetime.strptime(tim6a_Met[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time6a_Met.append(test)

# V2_18
tim7a_Met = np.array(Met_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time7a_Met=[]
for i in range(len(tim7a_Met)):
    test = datetime.strptime(tim7a_Met[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time7a_Met.append(test)

# V3_18M
tim8a_Met = np.array(Met_V3_18M['Time'])

#CONVERT TO DATETIME FROM STRING
time8a_Met=[]
for i in range(len(tim8a_Met)):
    test = datetime.strptime(tim8a_Met[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time8a_Met.append(test)

# V3_18D
tim9a_Met = np.array(Met_V3_18D['Time'])

#CONVERT TO DATETIME FROM STRING
time9a_Met=[]
for i in range(len(tim9a_Met)):
    test = datetime.strptime(tim9a_Met[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time9a_Met.append(test)
    
# V4_18
tim10a_Met = np.array(Met_V4_18['Time'])

#CONVERT TO DATETIME FROM STRING
time10a_Met=[]
for i in range(len(tim10a_Met)):
    test = datetime.strptime(tim10a_Met[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time10a_Met.append(test)
    
# PCAN
tim11a_Met = np.array(Met_PCAN['Time'])

#CONVERT TO DATETIME FROM STRING
time11a_Met=[]
for i in range(len(tim11a_Met)):
    test = datetime.strptime(tim11a_Met[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time11a_Met.append(test)
    
# SIPEXII
tim12a_Met = np.array(Met_SIPEXII['Time'])

#CONVERT TO DATETIME FROM STRING
time12a_Met=[]
for i in range(len(tim12a_Met)):
    test = datetime.strptime(tim12a_Met[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time12a_Met.append(test)

#------------------------------------
# At Station
#------------------------------------
# Davis (V1_17)
tim1b_Met = np.array(Met_Davis_V1_17['Time'])
#CONVERT TO DATETIME FROM STRING
time1b_Met=[]
for i in range(len(tim1b_Met)):
    test = datetime.strptime(tim1b_Met[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time1b_Met.append(test)

# Casey (V2_17)
tim2b_Met = np.array(Met_Casey_V2_17['Time'])

#CONVERT TO DATETIME FROM STRING
time2b_Met=[]
for i in range(len(tim2b_Met)):
    test = datetime.strptime(tim2b_Met[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time2b_Met.append(test)

# Mawson (V3_17)
tim3b_Met = np.array(Met_Mawson_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time3b_Met=[]
for i in range(len(tim3b_Met)):
    test = datetime.strptime(tim3b_Met[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time3b_Met.append(test)

# Davis (V3_17)
tim4b_Met = np.array(Met_Davis_V3_17['Time'])

#CONVERT TO DATETIME FROM STRING
time4b_Met=[]
for i in range(len(tim4b_Met)):
    test = datetime.strptime(tim4b_Met[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time4b_Met.append(test)
    
# Macquarie Island (V4_17)
tim5b_Met = np.array(Met_MQIsl_V4_17['Time'])

#CONVERT TO DATETIME FROM STRING
time5b_Met=[]
for i in range(len(tim5b_Met)):
    test = datetime.strptime(tim5b_Met[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time5b_Met.append(test)
    
# Davis (V1_18)
tim6b_Met = np.array(Met_Davis_V1_18['Time'])

#CONVERT TO DATETIME FROM STRING
time6b_Met=[]
for i in range(len(tim6b_Met)):
    test = datetime.strptime(tim6b_Met[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time6b_Met.append(test)

# Casey (V2_18)
tim7b_Met = np.array(Met_Casey_V2_18['Time'])

#CONVERT TO DATETIME FROM STRING
time7b_Met=[]
for i in range(len(tim7b_Met)):
    test = datetime.strptime(tim7b_Met[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time7b_Met.append(test)

# Mawson (V3_18)
tim8b_Met = np.array(Met_Mawson_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time8b_Met=[]
for i in range(len(tim8b_Met)):
    test = datetime.strptime(tim8b_Met[i],'%H:%M:%S') + timedelta(hours=5)
    test = test.replace(day=1)
    time8b_Met.append(test)

# Davis (V3_18)
tim9b_Met = np.array(Met_Davis_V3_18['Time'])

#CONVERT TO DATETIME FROM STRING
time9b_Met=[]
for i in range(len(tim9b_Met)):
    test = datetime.strptime(tim9b_Met[i],'%H:%M:%S') + timedelta(hours=7)
    test = test.replace(day=1)
    time9b_Met.append(test)
    
# Macquarie Island (V4_18)
tim10b_Met = np.array(Met_MQIsl_V4_18['Time'])

#CONVERT TO DATETIME FROM STRING
time10b_Met=[]
for i in range(len(tim10b_Met)):
    test = datetime.strptime(tim10b_Met[i],'%H:%M:%S') + timedelta(hours=11)
    test = test.replace(day=1)
    time10b_Met.append(test)
    
# PCAN
tim11b_Met = np.array(Met_PCAN_Ice['Time'])

#CONVERT TO DATETIME FROM STRING
time11b_Met=[]
for i in range(len(tim11b_Met)):
    test = datetime.strptime(tim11b_Met[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time11b_Met.append(test)
    
# SIPEXII
tim12b_Met = np.array(Met_SIPEXII_Ice['Time'])

#CONVERT TO DATETIME FROM STRING
time12b_Met=[]
for i in range(len(tim12b_Met)):
    test = datetime.strptime(tim12b_Met[i],'%H:%M:%S') + timedelta(hours=8)
    test = test.replace(day=1)
    time12b_Met.append(test)
 
#------------------------------------------------------------------------------
# CALCULATE A MEAN Hg0 CONCENTRATION FOR EACH HOUR OF THE DAY
    
# Function to calculate the hourly mean
def hourlyM(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').mean()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

#----------------------
# Whole Voyage
#----------------------
# Hg0
Hg0_V1_17_HM,   time1_HMa  = hourlyM(V1_17_Hg0[:],   time1a) # V1_17
Hg0_V2_17_HM,   time2_HMa  = hourlyM(V2_17_Hg0[:],   time2a) # V2_17
Hg0_V3_17M_HM,  time3_HMa  = hourlyM(V3_17M_Hg0[:],  time3a) # V3_17 (Mawson)
Hg0_V3_17D_HM,  time4_HMa  = hourlyM(V3_17D_Hg0[:],  time4a) # V3_17 (Davis)
Hg0_V4_17_HM,   time5_HMa  = hourlyM(V4_17_Hg0[:],   time5a) # V4_17

Hg0_V1_18_HM,   time6_HMa  = hourlyM(V1_18_Hg0[:],   time6a) # V1_18
Hg0_V2_18_HM,   time7_HMa  = hourlyM(V2_18_Hg0[:],   time7a) # V2_18
Hg0_V3_18M_HM,  time8_HMa  = hourlyM(V3_18M_Hg0[:],  time8a) # V3_18 (Mawson)
Hg0_V3_18D_HM,  time9_HMa  = hourlyM(V3_18D_Hg0[:],  time9a) # V3_18 (Davis)
Hg0_V4_18_HM,   time10_HMa = hourlyM(V4_18_Hg0[:],   time10a) # V4_18

Hg0_PCAN_HM,    time11_HMa = hourlyM(PCAN_Hg0[:],    time11a) # PCAN
Hg0_SIPEXII_HM, time12_HMa = hourlyM(SIPEXII_Hg0[:], time12a) # SIPEXII

# BrO
BrO_V1_17_HM,   time1_HMz  = hourlyM(V1_17_BrO[:],   time1z) # V1_17
BrO_V2_17_HM,   time2_HMz  = hourlyM(V2_17_BrO[:],   time2z) # V2_17
BrO_V3_17M_HM,  time3_HMz  = hourlyM(V3_17M_BrO[:],  time3z) # V3_17 (Mawson)
BrO_V3_17D_HM,  time4_HMz  = hourlyM(V3_17D_BrO[:],  time4z) # V3_17 (Davis)

BrO_V1_18_HM,   time6_HMz  = hourlyM(V1_18_BrO[:],   time5z) # V1_18
BrO_V2_18_HM,   time7_HMz  = hourlyM(V2_18_BrO[:],   time6z) # V2_18
BrO_V3_18M_HM,  time8_HMz  = hourlyM(V3_18M_BrO[:],  time7z) # V3_18 (Mawson)
BrO_V3_18D_HM,  time9_HMz  = hourlyM(V3_18D_BrO[:],  time8z) # V3_18 (Davis)

BrO_SIPEXII_HM, time12_HMz = hourlyM(SIPEXII_BrO[:], time9z) # SIPEXII

# O3
O3_V1_17_HM,   time1_HMa  = hourlyM(V1_17_O3[:],   time1a_O3) # V1_17
O3_V2_17_HM,   time2_HMa  = hourlyM(V2_17_O3[:],   time2a_O3) # V2_17
O3_V3_17M_HM,  time3_HMa  = hourlyM(V3_17M_O3[:],  time3a_O3) # V3_17 (Mawson)
O3_V3_17D_HM,  time4_HMa  = hourlyM(V3_17D_O3[:],  time4a_O3) # V3_17 (Davis)
O3_V4_17_HM,   time5_HMa  = hourlyM(V4_17_O3[:],   time5a_O3) # V4_17

O3_V1_18_HM,   time6_HMa  = hourlyM(V1_18_O3[:],   time6a_O3) # V1_18
O3_V2_18_HM,   time7_HMa  = hourlyM(V2_18_O3[:],   time7a_O3) # V2_18
O3_V3_18M_HM,  time8_HMa  = hourlyM(V3_18M_O3[:],  time8a_O3) # V3_18 (Mawson)
O3_V3_18D_HM,  time9_HMa  = hourlyM(V3_18D_O3[:],  time9a_O3) # V3_18 (Davis)
O3_V4_18_HM,   time10_HMa = hourlyM(V4_18_O3[:],   time10a_O3) # V4_18

O3_PCAN_HM,    time11_HMa = hourlyM(PCAN_O3[:],    time11a_O3) # PCAN
O3_SIPEXII_HM, time12_HMa = hourlyM(SIPEXII_O3[:], time12a_O3) # SIPEXII

#----------------------
# At Station
#----------------------
# Hg0
Hg0_Davis17_HM1,    time1_HMb  = hourlyM(Hg0_Davis1_17[:],  time1b) # V1_17
Hg0_Casey17_HM,     time2_HMb  = hourlyM(Hg0_Casey_17[:],   time2b) # V2_17
Hg0_Mawson17_HM,    time3_HMb  = hourlyM(Hg0_Mawson_17[:],  time3b) # V3_17
Hg0_Davis17_HM3,    time4_HMb  = hourlyM(Hg0_Davis3_17[:],  time4b) # V3_17
Hg0_MQIsl17_HM,     time5_HMb  = hourlyM(Hg0_MQIsl_17[:],   time5b) # V4_17

Hg0_Davis18_HM1,    time6_HMb  = hourlyM(Hg0_Davis1_18[:],  time6b) # V1_18
Hg0_Casey18_HM,     time7_HMb  = hourlyM(Hg0_Casey_18[:],   time7b) # V2_18
Hg0_Mawson18_HM,    time8_HMb  = hourlyM(Hg0_Mawson_18[:],  time8b) # V3_18
Hg0_Davis18_HM3,    time9_HMb  = hourlyM(Hg0_Davis3_18[:],  time9b) # V3_18
Hg0_MQIsl18_HM,     time10_HMb = hourlyM(Hg0_MQIsl_18[:],   time10b) # V4_18

Hg0_PCAN17_HM,      time11_HMb = hourlyM(Hg0_PCAN_17[:],    time11b) # PCAN
Hg0_SIPEXII12_HM,   time12_HMb = hourlyM(Hg0_SIPEXII_12[:], time12b) # SIPEXII

# BrO
BrO_Davis17_HM1,  time1_HMy  = hourlyM(BrO_Davis1_17[:], time1y) # V1_17
BrO_Casey17_HM,   time2_HMy  = hourlyM(BrO_Casey_17[:],  time2y) # V2_17
BrO_Mawson17_HM,  time3_HMy  = hourlyM(BrO_Mawson_17[:], time3y) # V3_17 (Mawson)
BrO_Davis17_HM3,  time4_HMy  = hourlyM(BrO_Davis3_17[:], time4y) # V3_17 (Davis)

BrO_Davis18_HM1,  time6_HMy  = hourlyM(BrO_Davis1_18[:], time5y) # V1_18
BrO_Casey18_HM,   time7_HMy  = hourlyM(BrO_Casey_18[:],  time6y) # V2_18
BrO_Mawson18_HM,  time8_HMy  = hourlyM(BrO_Mawson_18[:], time7y) # V3_18 (Mawson)
BrO_Davis18_HM3,  time9_HMy  = hourlyM(BrO_Davis3_18[:], time8y) # V3_18 (Davis)

BrO_SIPEXII12_HM, time12_HMy = hourlyM(BrO_SIPEXII_12[:], time9y) # SIPEXII

# O3
O3_Davis17_HM1,  time1_HMb  = hourlyM(O3_Davis1_17[:], time1b_O3) # V1_17
O3_Casey17_HM,   time2_HMb  = hourlyM(O3_Casey_17[:],  time2b_O3) # V2_17
O3_Mawson17_HM,  time3_HMb  = hourlyM(O3_Mawson_17[:], time3b_O3) # V3_17 (Mawson)
O3_Davis17_HM3,  time4_HMb  = hourlyM(O3_Davis3_17[:], time4b_O3) # V3_17 (Davis)
O3_MQIsl17_HM,   time5_HMb  = hourlyM(O3_MQIsl_17[:],  time5b_O3) # V4_17

O3_Davis18_HM1,  time6_HMb  = hourlyM(O3_Davis1_18[:], time6b_O3) # V1_18
O3_Casey18_HM,   time7_HMb  = hourlyM(O3_Casey_18[:],  time7b_O3) # V2_18
O3_Mawson18_HM,  time8_HMb  = hourlyM(O3_Mawson_18[:], time8b_O3) # V3_18 (Mawson)
O3_Davis18_HM3,  time9_HMb  = hourlyM(O3_Davis3_18[:], time9b_O3) # V3_18 (Davis)
O3_MQIsl18_HM,   time5_HMb  = hourlyM(O3_MQIsl_18[:],  time10b_O3) # V4_17

O3_PCAN17_HM,    time11_HMb = hourlyM(O3_PCAN_17[:],   time11b_O3) # PCAN
O3_SIPEXII12_HM, time12_HMb = hourlyM(O3_SIPEXII_12[:],time12b_O3) # SIPEXII

# RH
RH_Davis17_HM1,    time1_HMb  = hourlyM(np.array(Met_Davis_V1_17['RH_Avg']),  time1b_Met) # V1_17
RH_Casey17_HM,     time2_HMb  = hourlyM(np.array(Met_Casey_V2_17['RH_Avg']),  time2b_Met) # V2_17
RH_Mawson17_HM,    time3_HMb  = hourlyM(np.array(Met_Mawson_V3_17['RH_Avg']), time3b_Met) # V3_17
RH_Davis17_HM3,    time4_HMb  = hourlyM(np.array(Met_Davis_V3_17['RH_Avg']),  time4b_Met) # V3_17
RH_MQIsl17_HM,     time5_HMb  = hourlyM(np.array(Met_MQIsl_V4_17['RH_Avg']),  time5b_Met) # V4_17

RH_Davis18_HM1,    time6_HMb  = hourlyM(np.array(Met_Davis_V1_18['RH_Avg']),  time6b_Met) # V1_18
RH_Casey18_HM,     time7_HMb  = hourlyM(np.array(Met_Casey_V2_18['RH_Avg']),  time7b_Met) # V2_18
RH_Mawson18_HM,    time8_HMb  = hourlyM(np.array(Met_Mawson_V3_18['RH_Avg']), time8b_Met) # V3_18
RH_Davis18_HM3,    time9_HMb  = hourlyM(np.array(Met_Davis_V3_18['RH_Avg']),  time9b_Met) # V3_18
RH_MQIsl18_HM,     time10_HMb = hourlyM(np.array(Met_MQIsl_V4_18['RH_Avg']),  time10b_Met) # V4_18

RH_PCAN17_HM,      time11_HMb = hourlyM(np.array(Met_PCAN_Ice['RH_Avg']),     time11b_Met) # PCAN
RH_SIPEXII12_HM,   time12_HMb = hourlyM(np.array(Met_SIPEXII_Ice['RH_Avg']),  time12b_Met) # SIPEXII

# Temp
Temp_Davis17_HM1,    time1_HMb  = hourlyM(np.array(Met_Davis_V1_17['Temp_Avg']),  time1b_Met) # V1_17
Temp_Casey17_HM,     time2_HMb  = hourlyM(np.array(Met_Casey_V2_17['Temp_Avg']),  time2b_Met) # V2_17
Temp_Mawson17_HM,    time3_HMb  = hourlyM(np.array(Met_Mawson_V3_17['Temp_Avg']), time3b_Met) # V3_17
Temp_Davis17_HM3,    time4_HMb  = hourlyM(np.array(Met_Davis_V3_17['Temp_Avg']),  time4b_Met) # V3_17
Temp_MQIsl17_HM,     time5_HMb  = hourlyM(np.array(Met_MQIsl_V4_17['Temp_Avg']),  time5b_Met) # V4_17

Temp_Davis18_HM1,    time6_HMb  = hourlyM(np.array(Met_Davis_V1_18['Temp_Avg']),  time6b_Met) # V1_18
Temp_Casey18_HM,     time7_HMb  = hourlyM(np.array(Met_Casey_V2_18['Temp_Avg']),  time7b_Met) # V2_18
Temp_Mawson18_HM,    time8_HMb  = hourlyM(np.array(Met_Mawson_V3_18['Temp_Avg']), time8b_Met) # V3_18
Temp_Davis18_HM3,    time9_HMb  = hourlyM(np.array(Met_Davis_V3_18['Temp_Avg']),  time9b_Met) # V3_18
Temp_MQIsl18_HM,     time10_HMb = hourlyM(np.array(Met_MQIsl_V4_18['Temp_Avg']),  time10b_Met) # V4_18

Temp_PCAN17_HM,      time11_HMb = hourlyM(np.array(Met_PCAN_Ice['Temp_Avg']),     time11b_Met) # PCAN
Temp_SIPEXII12_HM,   time12_HMb = hourlyM(np.array(Met_SIPEXII_Ice['Temp_Avg']),  time12b_Met) # SIPEXII

# SolRad
SR_Davis17_HM1,    time1_HMb  = hourlyM(np.array(Met_Davis_V1_17['SolRad_Avg']),  time1b_Met) # V1_17
SR_Casey17_HM,     time2_HMb  = hourlyM(np.array(Met_Casey_V2_17['SolRad_Avg']),  time2b_Met) # V2_17
SR_Mawson17_HM,    time3_HMb  = hourlyM(np.array(Met_Mawson_V3_17['SolRad_Avg']), time3b_Met) # V3_17
SR_Davis17_HM3,    time4_HMb  = hourlyM(np.array(Met_Davis_V3_17['SolRad_Avg']),  time4b_Met) # V3_17
SR_MQIsl17_HM,     time5_HMb  = hourlyM(np.array(Met_MQIsl_V4_17['SolRad_Avg']),  time5b_Met) # V4_17

SR_Davis18_HM1,    time6_HMb  = hourlyM(np.array(Met_Davis_V1_18['SolRad_Avg']),  time6b_Met) # V1_18
SR_Casey18_HM,     time7_HMb  = hourlyM(np.array(Met_Casey_V2_18['SolRad_Avg']),  time7b_Met) # V2_18
SR_Mawson18_HM,    time8_HMb  = hourlyM(np.array(Met_Mawson_V3_18['SolRad_Avg']), time8b_Met) # V3_18
SR_Davis18_HM3,    time9_HMb  = hourlyM(np.array(Met_Davis_V3_18['SolRad_Avg']),  time9b_Met) # V3_18
SR_MQIsl18_HM,     time10_HMb = hourlyM(np.array(Met_MQIsl_V4_18['SolRad_Avg']),  time10b_Met) # V4_18

SR_PCAN17_HM,      time11_HMb = hourlyM(np.array(Met_PCAN_Ice['SolRad_Avg']),     time11b_Met) # PCAN
SR_SIPEXII12_HM,   time12_HMb = hourlyM(np.array(Met_SIPEXII_Ice['SolRad_Avg']),  time12b_Met) # SIPEXII

# Wind Speed
WS_Davis17_HM1,    time1_HMb  = hourlyM(np.array(Met_Davis_V1_17['WS_Avg']),  time1b_Met) # V1_17
WS_Casey17_HM,     time2_HMb  = hourlyM(np.array(Met_Casey_V2_17['WS_Avg']),  time2b_Met) # V2_17
WS_Mawson17_HM,    time3_HMb  = hourlyM(np.array(Met_Mawson_V3_17['WS_Avg']), time3b_Met) # V3_17
WS_Davis17_HM3,    time4_HMb  = hourlyM(np.array(Met_Davis_V3_17['WS_Avg']),  time4b_Met) # V3_17
WS_MQIsl17_HM,     time5_HMb  = hourlyM(np.array(Met_MQIsl_V4_17['WS_Avg']),  time5b_Met) # V4_17

WS_Davis18_HM1,    time6_HMb  = hourlyM(np.array(Met_Davis_V1_18['WS_Avg']),  time6b_Met) # V1_18
WS_Casey18_HM,     time7_HMb  = hourlyM(np.array(Met_Casey_V2_18['WS_Avg']),  time7b_Met) # V2_18
WS_Mawson18_HM,    time8_HMb  = hourlyM(np.array(Met_Mawson_V3_18['WS_Avg']), time8b_Met) # V3_18
WS_Davis18_HM3,    time9_HMb  = hourlyM(np.array(Met_Davis_V3_18['WS_Avg']),  time9b_Met) # V3_18
WS_MQIsl18_HM,     time10_HMb = hourlyM(np.array(Met_MQIsl_V4_18['WS_Avg']),  time10b_Met) # V4_18

WS_PCAN17_HM,      time11_HMb = hourlyM(np.array(Met_PCAN_Ice['WS_Avg']),     time11b_Met) # PCAN
WS_SIPEXII12_HM,   time12_HMb = hourlyM(np.array(Met_SIPEXII_Ice['WS_Avg']),  time12b_Met) # SIPEXII

#----------------------
# Sea Ice
#----------------------
Hg0_Ice_V1_17_HM,   time1_HMc  = hourlyM(Hg0_Ice1_V1_17[:], time1c) # V1_17
Hg0_Ice_V2_17_HM,   time2_HMc  = hourlyM(Hg0_Ice1_V2_17[:], time2c) # V2_17
Hg0_Ice_V3_17_HM,   time3_HMc  = hourlyM(Hg0_Ice1_V3_17[:], time3c) # V3_17

Hg0_Ice_V1_18_HM,   time4_HMc  = hourlyM(Hg0_Ice1_V1_18[:], time4c) # V1_18
Hg0_Ice_V2_18_HM,   time5_HMc  = hourlyM(Hg0_Ice1_V2_18[:], time5c) # V2_18
Hg0_Ice_V3_18_HM,   time6_HMc  = hourlyM(Hg0_Ice1_V3_18[:], time6c) # V3_18

#----------------------
# Open Water
#----------------------
Hg0_OW_V1_17_HM,    time1_HMd  = hourlyM(Hg0_OW1_V1_17[:], time1d) # V1_17
Hg0_OW_V2_17_HM,    time2_HMd  = hourlyM(Hg0_OW1_V2_17[:], time2d) # V2_17
Hg0_OW_V3_17_HM,    time3_HMd  = hourlyM(Hg0_OW1_V3_17[:], time3d) # V3_17

Hg0_OW_V1_18_HM,    time4_HMd  = hourlyM(Hg0_OW1_V1_18[:], time4d) # V1_18
Hg0_OW_V2_18_HM,    time5_HMd  = hourlyM(Hg0_OW1_V2_18[:], time5d) # V2_18
Hg0_OW_V3_18_HM,    time6_HMd  = hourlyM(Hg0_OW1_V3_18[:], time6d) # V3_18

#------------------------------------------------------------------------------
# Append the first value to complete the diurnal cycle

#----------------------
# At Station
#----------------------
# Hg0
Hg0_Davis17_HM1  = np.append(Hg0_Davis17_HM1,  Hg0_Davis17_HM1[0])
Hg0_Casey17_HM   = np.append(Hg0_Casey17_HM,   Hg0_Casey17_HM[0])
Hg0_Mawson17_HM  = np.append(Hg0_Mawson17_HM,  Hg0_Mawson17_HM[0])
Hg0_Davis17_HM3  = np.append(Hg0_Davis17_HM3,  Hg0_Davis17_HM3[0])
Hg0_MQIsl17_HM   = np.append(Hg0_MQIsl17_HM,   Hg0_MQIsl17_HM[0])

Hg0_Davis18_HM1  = np.append(Hg0_Davis18_HM1,  Hg0_Davis18_HM1[0])
Hg0_Casey18_HM   = np.append(Hg0_Casey18_HM,   Hg0_Casey18_HM[0])
Hg0_Mawson18_HM  = np.append(Hg0_Mawson18_HM,  Hg0_Mawson18_HM[0])
Hg0_Davis18_HM3  = np.append(Hg0_Davis18_HM3,  Hg0_Davis18_HM3[0])
Hg0_MQIsl18_HM   = np.append(Hg0_MQIsl18_HM,   Hg0_MQIsl18_HM[0])

Hg0_PCAN17_HM    = np.append(Hg0_PCAN17_HM,    Hg0_PCAN17_HM[0])
Hg0_SIPEXII12_HM = np.append(Hg0_SIPEXII12_HM, Hg0_SIPEXII12_HM[0])

# # BrO
# BrO_Davis17_HM1  = np.append(BrO_Davis17_HM1,  BrO_Davis17_HM1[0])
# BrO_Casey17_HM   = np.append(BrO_Casey17_HM,   BrO_Casey17_HM[0])
# BrO_Mawson17_HM  = np.append(BrO_Mawson17_HM,  BrO_Mawson17_HM[0])
# BrO_Davis17_HM3  = np.append(BrO_Davis17_HM3,  BrO_Davis17_HM3[0])

# BrO_Davis18_HM1  = np.append(BrO_Davis18_HM1,  BrO_Davis18_HM1[0])
# BrO_Casey18_HM   = np.append(BrO_Casey18_HM,   BrO_Casey18_HM[0])
# BrO_Mawson18_HM  = np.append(BrO_Mawson18_HM,  BrO_Mawson18_HM[0])
# BrO_Davis18_HM3  = np.append(BrO_Davis18_HM3,  BrO_Davis18_HM3[0])

# BrO_SIPEXII12_HM = np.append(BrO_SIPEXII12_HM, BrO_SIPEXII12_HM[0])

# O3
O3_Davis17_HM1  = np.append(O3_Davis17_HM1,  O3_Davis17_HM1[0])
O3_Casey17_HM   = np.append(O3_Casey17_HM,   O3_Casey17_HM[0])
O3_Mawson17_HM  = np.append(O3_Mawson17_HM,  O3_Mawson17_HM[0])
O3_Davis17_HM3  = np.append(O3_Davis17_HM3,  O3_Davis17_HM3[0])
O3_MQIsl17_HM   = np.append(O3_MQIsl17_HM,   O3_MQIsl17_HM[0])

O3_Davis18_HM1  = np.append(O3_Davis18_HM1,  O3_Davis18_HM1[0])
O3_Casey18_HM   = np.append(O3_Casey18_HM,   O3_Casey18_HM[0])
O3_Mawson18_HM  = np.append(O3_Mawson18_HM,  O3_Mawson18_HM[0])
O3_Davis18_HM3  = np.append(O3_Davis18_HM3,  O3_Davis18_HM3[0])
O3_MQIsl18_HM   = np.append(O3_MQIsl18_HM,   O3_MQIsl18_HM[0])

O3_PCAN17_HM    = np.append(O3_PCAN17_HM,    O3_PCAN17_HM[0])
O3_SIPEXII12_HM = np.append(O3_SIPEXII12_HM, O3_SIPEXII12_HM[0])

# RH
RH_Davis17_HM1  = np.append(RH_Davis17_HM1,  RH_Davis17_HM1[0])
RH_Casey17_HM   = np.append(RH_Casey17_HM,   RH_Casey17_HM[0])
RH_Mawson17_HM  = np.append(RH_Mawson17_HM,  RH_Mawson17_HM[0])
RH_Davis17_HM3  = np.append(RH_Davis17_HM3,  RH_Davis17_HM3[0])
RH_MQIsl17_HM   = np.append(RH_MQIsl17_HM,   RH_MQIsl17_HM[0])

RH_Davis18_HM1  = np.append(RH_Davis18_HM1,  RH_Davis18_HM1[0])
RH_Casey18_HM   = np.append(RH_Casey18_HM,   RH_Casey18_HM[0])
RH_Mawson18_HM  = np.append(RH_Mawson18_HM,  RH_Mawson18_HM[0])
RH_Davis18_HM3  = np.append(RH_Davis18_HM3,  RH_Davis18_HM3[0])
RH_MQIsl18_HM   = np.append(RH_MQIsl18_HM,   RH_MQIsl18_HM[0])

RH_PCAN17_HM    = np.append(RH_PCAN17_HM,    RH_PCAN17_HM[0])
RH_SIPEXII12_HM = np.append(RH_SIPEXII12_HM, RH_SIPEXII12_HM[0])

# Temp
Temp_Davis17_HM1  = np.append(Temp_Davis17_HM1,  Temp_Davis17_HM1[0])
Temp_Casey17_HM   = np.append(Temp_Casey17_HM,   Temp_Casey17_HM[0])
Temp_Mawson17_HM  = np.append(Temp_Mawson17_HM,  Temp_Mawson17_HM[0])
Temp_Davis17_HM3  = np.append(Temp_Davis17_HM3,  Temp_Davis17_HM3[0])
Temp_MQIsl17_HM   = np.append(Temp_MQIsl17_HM,   Temp_MQIsl17_HM[0])

Temp_Davis18_HM1  = np.append(Temp_Davis18_HM1,  Temp_Davis18_HM1[0])
Temp_Casey18_HM   = np.append(Temp_Casey18_HM,   Temp_Casey18_HM[0])
Temp_Mawson18_HM  = np.append(Temp_Mawson18_HM,  Temp_Mawson18_HM[0])
Temp_Davis18_HM3  = np.append(Temp_Davis18_HM3,  Temp_Davis18_HM3[0])
Temp_MQIsl18_HM   = np.append(Temp_MQIsl18_HM,   Temp_MQIsl18_HM[0])

Temp_PCAN17_HM    = np.append(Temp_PCAN17_HM,    Temp_PCAN17_HM[0])
Temp_SIPEXII12_HM = np.append(Temp_SIPEXII12_HM, Temp_SIPEXII12_HM[0])

# SolRad
SR_Davis17_HM1  = np.append(SR_Davis17_HM1,  SR_Davis17_HM1[0])
SR_Casey17_HM   = np.append(SR_Casey17_HM,   SR_Casey17_HM[0])
SR_Mawson17_HM  = np.append(SR_Mawson17_HM,  SR_Mawson17_HM[0])
SR_Davis17_HM3  = np.append(SR_Davis17_HM3,  SR_Davis17_HM3[0])
SR_MQIsl17_HM   = np.append(SR_MQIsl17_HM,   SR_MQIsl17_HM[0])

SR_Davis18_HM1  = np.append(SR_Davis18_HM1,  SR_Davis18_HM1[0])
SR_Casey18_HM   = np.append(SR_Casey18_HM,   SR_Casey18_HM[0])
SR_Mawson18_HM  = np.append(SR_Mawson18_HM,  SR_Mawson18_HM[0])
SR_Davis18_HM3  = np.append(SR_Davis18_HM3,  SR_Davis18_HM3[0])
SR_MQIsl18_HM   = np.append(SR_MQIsl18_HM,   SR_MQIsl18_HM[0])

SR_PCAN17_HM    = np.append(SR_PCAN17_HM,    SR_PCAN17_HM[0])
SR_SIPEXII12_HM = np.append(SR_SIPEXII12_HM, SR_SIPEXII12_HM[0])

# Wind Speed
WS_Davis17_HM1  = np.append(WS_Davis17_HM1,  WS_Davis17_HM1[0])
WS_Casey17_HM   = np.append(WS_Casey17_HM,   WS_Casey17_HM[0])
WS_Mawson17_HM = np.append(WS_Mawson17_HM,  WS_Mawson17_HM[0])
WS_Davis17_HM3  = np.append(WS_Davis17_HM3,  WS_Davis17_HM3[0])
WS_MQIsl17_HM   = np.append(WS_MQIsl17_HM,   WS_MQIsl17_HM[0])

WS_Davis18_HM1  = np.append(WS_Davis18_HM1,  WS_Davis18_HM1[0])
WS_Casey18_HM   = np.append(WS_Casey18_HM,   WS_Casey18_HM[0])
WS_Mawson18_HM  = np.append(WS_Mawson18_HM,  WS_Mawson18_HM[0])
WS_Davis18_HM3  = np.append(WS_Davis18_HM3,  WS_Davis18_HM3[0])
WS_MQIsl18_HM   = np.append(WS_MQIsl18_HM,   WS_MQIsl18_HM[0])

WS_PCAN17_HM    = np.append(WS_PCAN17_HM,    WS_PCAN17_HM[0])
WS_SIPEXII12_HM = np.append(WS_SIPEXII12_HM, WS_SIPEXII12_HM[0])

#----------------------
# Sea Ice
#----------------------
Hg0_Ice_V1_17_HM = np.append(Hg0_Ice_V1_17_HM, Hg0_Ice_V1_17_HM[0])
Hg0_Ice_V2_17_HM = np.append(Hg0_Ice_V2_17_HM, Hg0_Ice_V2_17_HM[0])
Hg0_Ice_V3_17_HM = np.append(Hg0_Ice_V3_17_HM, Hg0_Ice_V3_17_HM[0])

Hg0_Ice_V1_18_HM = np.append(Hg0_Ice_V1_18_HM, Hg0_Ice_V1_18_HM[0])
Hg0_Ice_V2_18_HM = np.append(Hg0_Ice_V2_18_HM, Hg0_Ice_V2_18_HM[0])
Hg0_Ice_V3_18_HM = np.append(Hg0_Ice_V3_18_HM, Hg0_Ice_V3_18_HM[0])
#----------------------
# Sea Ice
#----------------------
Hg0_OW_V1_17_HM  = np.append(Hg0_OW_V1_17_HM,  Hg0_OW_V1_17_HM[0])
Hg0_OW_V2_17_HM  = np.append(Hg0_OW_V2_17_HM,  Hg0_OW_V2_17_HM[0])
Hg0_OW_V3_17_HM  = np.append(Hg0_OW_V3_17_HM,  Hg0_OW_V3_17_HM[0])

Hg0_OW_V1_18_HM  = np.append(Hg0_OW_V1_18_HM,  Hg0_OW_V1_18_HM[0])
Hg0_OW_V2_18_HM  = np.append(Hg0_OW_V2_18_HM,  Hg0_OW_V2_18_HM[0])
Hg0_OW_V3_18_HM  = np.append(Hg0_OW_V3_18_HM,  Hg0_OW_V3_18_HM[0])

b = datetime(1900,1,1,23,59,0)
time1_HMa  = np.append(time1_HMa,   b)
time2_HMa  = np.append(time2_HMa,   b)
time3_HMa  = np.append(time3_HMa,   b)
time4_HMa  = np.append(time4_HMa,   b)
time5_HMa  = np.append(time5_HMa,   b)

time6_HMa  = np.append(time6_HMa,   b)
time7_HMa  = np.append(time7_HMa,   b)
time8_HMa  = np.append(time8_HMa,   b)
time9_HMa  = np.append(time9_HMa,   b)
time10_HMa  = np.append(time10_HMa, b)

time11_HMa  = np.append(time11_HMa, b)
time12_HMa  = np.append(time12_HMa, b)

#------------------------------------------------------------------------------
# CALCULATE A MEDIAN Hg0 CONCENTRATION FOR EACH HOUR OF THE DAY
    
# Function to calculate the hourly median
def hourlyMed(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').median()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

#----------------------
# Whole Voyage
#----------------------
# Hg0
Hg0_V1_17_HMed,   time1_HMeda  = hourlyMed(V1_17_Hg0[:],   time1a) # V1_17
Hg0_V2_17_HMed,   time2_HMeda  = hourlyMed(V2_17_Hg0[:],   time2a) # V2_17
Hg0_V3_17M_HMed,  time3_HMeda  = hourlyMed(V3_17M_Hg0[:],  time3a) # V3_17 (Mawson)
Hg0_V3_17D_HMed,  time4_HMeda  = hourlyMed(V3_17D_Hg0[:],  time4a) # V3_17 (Davis)
Hg0_V4_17_HMed,   time5_HMeda  = hourlyMed(V4_17_Hg0[:],   time5a) # V4_17

Hg0_V1_18_HMed,   time6_HMeda  = hourlyMed(V1_18_Hg0[:],   time6a) # V1_18
Hg0_V2_18_HMed,   time7_HMeda  = hourlyMed(V2_18_Hg0[:],   time7a) # V2_18
Hg0_V3_18M_HMed,  time8_HMeda  = hourlyMed(V3_18M_Hg0[:],  time8a) # V3_18 (Mawson)
Hg0_V3_18D_HMed,  time9_HMeda  = hourlyMed(V3_18D_Hg0[:],  time9a) # V3_18 (Davis)
Hg0_V4_18_HMed,   time10_HMeda = hourlyMed(V4_18_Hg0[:],   time10a) # V4_18

Hg0_PCAN_HMed,    time11_HMeda = hourlyMed(PCAN_Hg0[:],    time11a) # PCAN
Hg0_SIPEXII_HMed, time12_HMeda = hourlyMed(SIPEXII_Hg0[:], time12a) # SIPEXII

# BrO
BrO_V1_17_HMed,   time1_HMz  = hourlyMed(V1_17_BrO[:],   time1z) # V1_17
BrO_V2_17_HMed,   time2_HMz  = hourlyMed(V2_17_BrO[:],   time2z) # V2_17
BrO_V3_17M_HMed,  time3_HMz  = hourlyMed(V3_17M_BrO[:],  time3z) # V3_17 (Mawson)
BrO_V3_17D_HMed,  time4_HMz  = hourlyMed(V3_17D_BrO[:],  time4z) # V3_17 (Davis)

BrO_V1_18_HMed,   time6_HMz  = hourlyMed(V1_18_BrO[:],   time5z) # V1_18
BrO_V2_18_HMed,   time7_HMz  = hourlyMed(V2_18_BrO[:],   time6z) # V2_18
BrO_V3_18M_HMed,  time8_HMz  = hourlyMed(V3_18M_BrO[:],  time7z) # V3_18 (Mawson)
BrO_V3_18D_HMed,  time9_HMz  = hourlyMed(V3_18D_BrO[:],  time8z) # V3_18 (Davis)

BrO_SIPEXII_HMed, time12_HMz = hourlyMed(SIPEXII_BrO[:], time9z) # SIPEXII

#----------------------
# At Station
#----------------------
# Hg0
Hg0_Davis17_HMed1,    time1_HMedb  = hourlyMed(Hg0_Davis1_17[:],  time1b) # V1_17
Hg0_Casey17_HMed,     time2_HMedb  = hourlyMed(Hg0_Casey_17[:],   time2b) # V2_17
Hg0_Mawson17_HMed,    time3_HMedb  = hourlyMed(Hg0_Mawson_17[:],  time3b) # V3_17
Hg0_Davis17_HMed3,    time4_HMedb  = hourlyMed(Hg0_Davis3_17[:],  time4b) # V3_17
Hg0_MQIsl17_HMed,     time5_HMedb  = hourlyMed(Hg0_MQIsl_17[:],   time5b) # V4_17

Hg0_Davis18_HMed1,    time6_HMedb  = hourlyMed(Hg0_Davis1_18[:],  time6b) # V1_18
Hg0_Casey18_HMed,     time7_HMedb  = hourlyMed(Hg0_Casey_18[:],   time7b) # V2_18
Hg0_Mawson18_HMed,    time8_HMedb  = hourlyMed(Hg0_Mawson_18[:],  time8b) # V3_18
Hg0_Davis18_HMed3,    time9_HMedb  = hourlyMed(Hg0_Davis3_18[:],  time9b) # V3_18
Hg0_MQIsl18_HMed,     time10_HMedb = hourlyMed(Hg0_MQIsl_18[:],   time10b) # V4_18

Hg0_PCAN17_HMed,      time11_HMedb = hourlyMed(Hg0_PCAN_17[:],    time11b) # PCAN
Hg0_SIPEXII12_HMed,   time12_HMedb = hourlyMed(Hg0_SIPEXII_12[:], time12b) # SIPEXII

# BrO
BrO_Davis17_HMed1,  time1_HMy  = hourlyMed(BrO_Davis1_17[:], time1y) # V1_17
BrO_Casey17_HMed,   time2_HMy  = hourlyMed(BrO_Casey_17[:],  time2y) # V2_17
BrO_Mawson17_HMed,  time3_HMy  = hourlyMed(BrO_Mawson_17[:], time3y) # V3_17 (Mawson)
BrO_Davis17_HMed3,  time4_HMy  = hourlyMed(BrO_Davis3_17[:], time4y) # V3_17 (Davis)

BrO_Davis18_HMed1,  time6_HMy  = hourlyMed(BrO_Davis1_18[:], time5y) # V1_18
BrO_Casey18_HMed,   time7_HMy  = hourlyMed(BrO_Casey_18[:],  time6y) # V2_18
BrO_Mawson18_HMed,  time8_HMy  = hourlyMed(BrO_Mawson_18[:], time7y) # V3_18 (Mawson)
BrO_Davis18_HMed3,  time9_HMy  = hourlyMed(BrO_Davis3_18[:], time8y) # V3_18 (Davis)

BrO_SIPEXII12_HMed, time12_HMy = hourlyMed(BrO_SIPEXII_12[:], time9y) # SIPEXII

# O3
O3_Davis17_HMed1,  time1_HMb  = hourlyMed(O3_Davis1_17[:], time1b_O3) # V1_17
O3_Casey17_HMed,   time2_HMb  = hourlyMed(O3_Casey_17[:],  time2b_O3) # V2_17
O3_Mawson17_HMed,  time3_HMb  = hourlyMed(O3_Mawson_17[:], time3b_O3) # V3_17 (Mawson)
O3_Davis17_HMed3,  time4_HMb  = hourlyMed(O3_Davis3_17[:], time4b_O3) # V3_17 (Davis)
O3_MQIsl17_HMed,   time5_HMb  = hourlyMed(O3_MQIsl_17[:],  time5b_O3) # V4_17

O3_Davis18_HMed1,  time6_HMb  = hourlyMed(O3_Davis1_18[:], time6b_O3) # V1_18
O3_Casey18_HMed,   time7_HMb  = hourlyMed(O3_Casey_18[:],  time7b_O3) # V2_18
O3_Mawson18_HMed,  time8_HMb  = hourlyMed(O3_Mawson_18[:], time8b_O3) # V3_18 (Mawson)
O3_Davis18_HMed3,  time9_HMb  = hourlyMed(O3_Davis3_18[:], time9b_O3) # V3_18 (Davis)
O3_MQIsl18_HMed,   time10_HMb = hourlyMed(O3_MQIsl_18[:],  time10b_O3) # V4_18

O3_PCAN17_HMed,    time11_HMb = hourlyMed(O3_PCAN_17[:],   time11b_O3) # PCAN
O3_SIPEXII12_HMed, time12_HMb = hourlyMed(O3_SIPEXII_12[:],time12b_O3) # SIPEXII

# RH
RH_Davis17_HMed1,    time1_HMb  = hourlyMed(np.array(Met_Davis_V1_17['RH_Avg']),  time1b_Met) # V1_17
RH_Casey17_HMed,     time2_HMb  = hourlyMed(np.array(Met_Casey_V2_17['RH_Avg']),  time2b_Met) # V2_17
RH_Mawson17_HMed,    time3_HMb  = hourlyMed(np.array(Met_Mawson_V3_17['RH_Avg']), time3b_Met) # V3_17
RH_Davis17_HMed3,    time4_HMb  = hourlyMed(np.array(Met_Davis_V3_17['RH_Avg']),  time4b_Met) # V3_17
RH_MQIsl17_HMed,     time5_HMb  = hourlyMed(np.array(Met_MQIsl_V4_17['RH_Avg']),  time5b_Met) # V4_17

RH_Davis18_HMed1,    time6_HMb  = hourlyMed(np.array(Met_Davis_V1_18['RH_Avg']),  time6b_Met) # V1_18
RH_Casey18_HMed,     time7_HMb  = hourlyMed(np.array(Met_Casey_V2_18['RH_Avg']),  time7b_Met) # V2_18
RH_Mawson18_HMed,    time8_HMb  = hourlyMed(np.array(Met_Mawson_V3_18['RH_Avg']), time8b_Met) # V3_18
RH_Davis18_HMed3,    time9_HMb  = hourlyMed(np.array(Met_Davis_V3_18['RH_Avg']),  time9b_Met) # V3_18
RH_MQIsl18_HMed,     time10_HMb = hourlyMed(np.array(Met_MQIsl_V4_18['RH_Avg']),  time10b_Met) # V4_18

RH_PCAN17_HMed,      time11_HMb = hourlyMed(np.array(Met_PCAN_Ice['RH_Avg']),     time11b_Met) # PCAN
RH_SIPEXII12_HMed,   time12_HMb = hourlyMed(np.array(Met_SIPEXII_Ice['RH_Avg']),  time12b_Met) # SIPEXII

# Temp
Temp_Davis17_HMed1,    time1_HMb  = hourlyM(np.array(Met_Davis_V1_17['Temp_Avg']),  time1b_Met) # V1_17
Temp_Casey17_HMed,     time2_HMb  = hourlyM(np.array(Met_Casey_V2_17['Temp_Avg']),  time2b_Met) # V2_17
Temp_Mawson17_HMed,    time3_HMb  = hourlyM(np.array(Met_Mawson_V3_17['Temp_Avg']), time3b_Met) # V3_17
Temp_Davis17_HMed3,    time4_HMb  = hourlyM(np.array(Met_Davis_V3_17['Temp_Avg']),  time4b_Met) # V3_17
Temp_MQIsl17_HMed,     time5_HMb  = hourlyM(np.array(Met_MQIsl_V4_17['Temp_Avg']),  time5b_Met) # V4_17

Temp_Davis18_HMed1,    time6_HMb  = hourlyM(np.array(Met_Davis_V1_18['Temp_Avg']),  time6b_Met) # V1_18
Temp_Casey18_HMed,     time7_HMb  = hourlyM(np.array(Met_Casey_V2_18['Temp_Avg']),  time7b_Met) # V2_18
Temp_Mawson18_HMed,    time8_HMb  = hourlyM(np.array(Met_Mawson_V3_18['Temp_Avg']), time8b_Met) # V3_18
Temp_Davis18_HMed3,    time9_HMb  = hourlyM(np.array(Met_Davis_V3_18['Temp_Avg']),  time9b_Met) # V3_18
Temp_MQIsl18_HMed,     time10_HMb = hourlyM(np.array(Met_MQIsl_V4_18['Temp_Avg']),  time10b_Met) # V4_18

Temp_PCAN17_HMed,      time11_HMb = hourlyM(np.array(Met_PCAN_Ice['Temp_Avg']),     time11b_Met) # PCAN
Temp_SIPEXII12_HMed,   time12_HMb = hourlyM(np.array(Met_SIPEXII_Ice['Temp_Avg']),  time12b_Met) # SIPEXII

# SolRad
SR_Davis17_HMed1,    time1_HMb  = hourlyMed(np.array(Met_Davis_V1_17['SolRad_Avg']),  time1b_Met) # V1_17
SR_Casey17_HMed,     time2_HMb  = hourlyMed(np.array(Met_Casey_V2_17['SolRad_Avg']),  time2b_Met) # V2_17
SR_Mawson17_HMed,    time3_HMb  = hourlyMed(np.array(Met_Mawson_V3_17['SolRad_Avg']), time3b_Met) # V3_17
SR_Davis17_HMed3,    time4_HMb  = hourlyMed(np.array(Met_Davis_V3_17['SolRad_Avg']),  time4b_Met) # V3_17
SR_MQIsl17_HMed,     time5_HMb  = hourlyMed(np.array(Met_MQIsl_V4_17['SolRad_Avg']),  time5b_Met) # V4_17

SR_Davis18_HMed1,    time6_HMb  = hourlyMed(np.array(Met_Davis_V1_18['SolRad_Avg']),  time6b_Met) # V1_18
SR_Casey18_HMed,     time7_HMb  = hourlyMed(np.array(Met_Casey_V2_18['SolRad_Avg']),  time7b_Met) # V2_18
SR_Mawson18_HMed,    time8_HMb  = hourlyMed(np.array(Met_Mawson_V3_18['SolRad_Avg']), time8b_Met) # V3_18
SR_Davis18_HMed3,    time9_HMb  = hourlyMed(np.array(Met_Davis_V3_18['SolRad_Avg']),  time9b_Met) # V3_18
SR_MQIsl18_HMed,     time10_HMb = hourlyMed(np.array(Met_MQIsl_V4_18['SolRad_Avg']),  time10b_Met) # V4_18

SR_PCAN17_HMed,      time11_HMb = hourlyMed(np.array(Met_PCAN_Ice['SolRad_Avg']),     time11b_Met) # PCAN
SR_SIPEXII12_HMed,   time12_HMb = hourlyMed(np.array(Met_SIPEXII_Ice['SolRad_Avg']),  time12b_Met) # SIPEXII

# Wind Speed
WS_Davis17_HMed1,    time1_HMb  = hourlyMed(np.array(Met_Davis_V1_17['WS_Avg']),  time1b_Met) # V1_17
WS_Casey17_HMed,     time2_HMb  = hourlyMed(np.array(Met_Casey_V2_17['WS_Avg']),  time2b_Met) # V2_17
WS_Mawson17_HMed,    time3_HMb  = hourlyMed(np.array(Met_Mawson_V3_17['WS_Avg']), time3b_Met) # V3_17
WS_Davis17_HMed3,    time4_HMb  = hourlyMed(np.array(Met_Davis_V3_17['WS_Avg']),  time4b_Met) # V3_17
WS_MQIsl17_HMed,     time5_HMb  = hourlyMed(np.array(Met_MQIsl_V4_17['WS_Avg']),  time5b_Met) # V4_17

WS_Davis18_HMed1,    time6_HMb  = hourlyMed(np.array(Met_Davis_V1_18['WS_Avg']),  time6b_Met) # V1_18
WS_Casey18_HMed,     time7_HMb  = hourlyMed(np.array(Met_Casey_V2_18['WS_Avg']),  time7b_Met) # V2_18
WS_Mawson18_HMed,    time8_HMb  = hourlyMed(np.array(Met_Mawson_V3_18['WS_Avg']), time8b_Met) # V3_18
WS_Davis18_HMed3,    time9_HMb  = hourlyMed(np.array(Met_Davis_V3_18['WS_Avg']),  time9b_Met) # V3_18
WS_MQIsl18_HMed,     time10_HMb = hourlyMed(np.array(Met_MQIsl_V4_18['WS_Avg']),  time10b_Met) # V4_18

WS_PCAN17_HMed,      time11_HMb = hourlyMed(np.array(Met_PCAN_Ice['WS_Avg']),     time11b_Met) # PCAN
WS_SIPEXII12_HMed,   time12_HMb = hourlyMed(np.array(Met_SIPEXII_Ice['WS_Avg']),  time12b_Met) # SIPEXII

#----------------------
# Sea Ice
#----------------------
Hg0_Ice_V1_17_HMed,   time1_HMedc  = hourlyMed(Hg0_Ice1_V1_17[:], time1c) # V1_17
Hg0_Ice_V2_17_HMed,   time2_HMedc  = hourlyMed(Hg0_Ice1_V2_17[:], time2c) # V2_17
Hg0_Ice_V3_17_HMed,   time3_HMedc  = hourlyMed(Hg0_Ice1_V3_17[:], time3c) # V3_17

Hg0_Ice_V1_18_HMed,   time4_HMedc  = hourlyMed(Hg0_Ice1_V1_18[:], time4c) # V1_18
Hg0_Ice_V2_18_HMed,   time5_HMedc  = hourlyMed(Hg0_Ice1_V2_18[:], time5c) # V2_18
Hg0_Ice_V3_18_HMed,   time6_HMedc  = hourlyMed(Hg0_Ice1_V3_18[:], time6c) # V3_18

#----------------------
# Open Water
#----------------------
Hg0_OW_V1_17_HMed,    time1_HMedd  = hourlyMed(Hg0_OW1_V1_17[:], time1d) # V1_17
Hg0_OW_V2_17_HMed,    time2_HMedd  = hourlyMed(Hg0_OW1_V2_17[:], time2d) # V2_17
Hg0_OW_V3_17_HMed,    time3_HMedd  = hourlyMed(Hg0_OW1_V3_17[:], time3d) # V3_17

Hg0_OW_V1_18_HMed,    time4_HMedd  = hourlyMed(Hg0_OW1_V1_18[:], time4d) # V1_18
Hg0_OW_V2_18_HMed,    time5_HMedd  = hourlyMed(Hg0_OW1_V2_18[:], time5d) # V2_18
Hg0_OW_V3_18_HMed,    time6_HMedd  = hourlyMed(Hg0_OW1_V3_18[:], time6d) # V3_18

#------------------------------------------------------------------------------
# Append the first value to complete the diurnal cycle
# Hg0
Hg0_Davis17_HMed1  = np.append(Hg0_Davis17_HMed1,  Hg0_Davis17_HMed1[0])
Hg0_Casey17_HMed   = np.append(Hg0_Casey17_HMed,   Hg0_Casey17_HMed[0])
Hg0_Mawson17_HMed  = np.append(Hg0_Mawson17_HMed,  Hg0_Mawson17_HMed[0])
Hg0_Davis17_HMed3  = np.append(Hg0_Davis17_HMed3,  Hg0_Davis17_HMed3[0])
Hg0_MQIsl17_HMed   = np.append(Hg0_MQIsl17_HMed,   Hg0_MQIsl17_HMed[0])

Hg0_Davis18_HMed1  = np.append(Hg0_Davis18_HMed1,  Hg0_Davis18_HMed1[0])
Hg0_Casey18_HMed   = np.append(Hg0_Casey18_HMed,   Hg0_Casey18_HMed[0])
Hg0_Mawson18_HMed  = np.append(Hg0_Mawson18_HMed,  Hg0_Mawson18_HMed[0])
Hg0_Davis18_HMed3  = np.append(Hg0_Davis18_HMed3,  Hg0_Davis18_HMed3[0])
Hg0_MQIsl18_HMed   = np.append(Hg0_MQIsl18_HMed,   Hg0_MQIsl18_HMed[0])

Hg0_PCAN17_HMed    = np.append(Hg0_PCAN17_HMed,    Hg0_PCAN17_HMed[0])
Hg0_SIPEXII12_HMed = np.append(Hg0_SIPEXII12_HMed, Hg0_SIPEXII12_HMed[0])

# BrO
# BrO_Davis17_HMed1  = np.append(BrO_Davis17_HMed1,  BrO_Davis17_HMed1[23])
# BrO_Casey17_HMed   = np.append(BrO_Casey17_HMed,   BrO_Casey17_HMed[23])
# BrO_Mawson17_HMed  = np.append(BrO_Mawson17_HMed,  BrO_Mawson17_HMed[23])
# BrO_Davis17_HMed3  = np.append(BrO_Davis17_HMed3,  BrO_Davis17_HMed3[23])

# BrO_Davis18_HMed1  = np.append(BrO_Davis18_HMed1,  BrO_Davis18_HMed1[23])
# BrO_Casey18_HMed   = np.append(BrO_Casey18_HMed,   BrO_Casey18_HMed[23])
# BrO_Mawson18_HMed  = np.append(BrO_Mawson18_HMed,  BrO_Mawson18_HMed[23])
# BrO_Davis18_HMed3  = np.append(BrO_Davis18_HMed3,  BrO_Davis18_HMed3[23])

# BrO_SIPEXII12_HMed = np.append(BrO_SIPEXII12_HMed, BrO_SIPEXII12_HMed[23])

# O3
O3_Davis17_HMed1  = np.append(O3_Davis17_HMed1,  O3_Davis17_HMed1[0])
O3_Casey17_HMed   = np.append(O3_Casey17_HMed,   O3_Casey17_HMed[0])
O3_Mawson17_HMed  = np.append(O3_Mawson17_HMed,  O3_Mawson17_HMed[0])
O3_Davis17_HMed3  = np.append(O3_Davis17_HMed3,  O3_Davis17_HMed3[0])
O3_MQIsl17_HMed   = np.append(O3_MQIsl17_HMed,   O3_MQIsl17_HMed[0])

O3_Davis18_HMed1  = np.append(O3_Davis18_HMed1,  O3_Davis18_HMed1[0])
O3_Casey18_HMed   = np.append(O3_Casey18_HMed,   O3_Casey18_HMed[0])
O3_Mawson18_HMed  = np.append(O3_Mawson18_HMed,  O3_Mawson18_HMed[0])
O3_Davis18_HMed3  = np.append(O3_Davis18_HMed3,  O3_Davis18_HMed3[0])
O3_MQIsl18_HMed   = np.append(O3_MQIsl18_HMed,   O3_MQIsl18_HMed[0])

O3_PCAN17_HMed    = np.append(O3_PCAN17_HMed,    O3_PCAN17_HMed[0])
O3_SIPEXII12_HMed = np.append(O3_SIPEXII12_HMed, O3_SIPEXII12_HMed[0])

# RH
RH_Davis17_HMed1  = np.append(RH_Davis17_HMed1,  RH_Davis17_HMed1[0])
RH_Casey17_HMed   = np.append(RH_Casey17_HMed,   RH_Casey17_HMed[0])
RH_Mawson17_HMed  = np.append(RH_Mawson17_HMed,  RH_Mawson17_HMed[0])
RH_Davis17_HMed3  = np.append(RH_Davis17_HMed3,  RH_Davis17_HMed3[0])
RH_MQIsl17_HMed   = np.append(RH_MQIsl17_HMed,   RH_MQIsl17_HMed[0])

RH_Davis18_HMed1  = np.append(RH_Davis18_HMed1,  RH_Davis18_HMed1[0])
RH_Casey18_HMed   = np.append(RH_Casey18_HMed,   RH_Casey18_HMed[0])
RH_Mawson18_HMed  = np.append(RH_Mawson18_HMed,  RH_Mawson18_HMed[0])
RH_Davis18_HMed3  = np.append(RH_Davis18_HMed3,  RH_Davis18_HMed3[0])
RH_MQIsl18_HMed   = np.append(RH_MQIsl18_HMed,   RH_MQIsl18_HMed[0])

RH_PCAN17_HMed    = np.append(RH_PCAN17_HMed,    RH_PCAN17_HMed[0])
RH_SIPEXII12_HMed = np.append(RH_SIPEXII12_HMed, RH_SIPEXII12_HMed[0])

# Temp
Temp_Davis17_HMed1  = np.append(Temp_Davis17_HMed1,  Temp_Davis17_HMed1[0])
Temp_Casey17_HMed   = np.append(Temp_Casey17_HMed,   Temp_Casey17_HMed[0])
Temp_Mawson17_HMed  = np.append(Temp_Mawson17_HMed,  Temp_Mawson17_HMed[0])
Temp_Davis17_HMed3  = np.append(Temp_Davis17_HMed3,  Temp_Davis17_HMed3[0])
Temp_MQIsl17_HMed   = np.append(Temp_MQIsl17_HMed,   Temp_MQIsl17_HMed[0])

Temp_Davis18_HMed1  = np.append(Temp_Davis18_HMed1,  Temp_Davis18_HMed1[0])
Temp_Casey18_HMed   = np.append(Temp_Casey18_HMed,   Temp_Casey18_HMed[0])
Temp_Mawson18_HMed  = np.append(Temp_Mawson18_HMed,  Temp_Mawson18_HMed[0])
Temp_Davis18_HMed3  = np.append(Temp_Davis18_HMed3,  Temp_Davis18_HMed3[0])
Temp_MQIsl18_HMed   = np.append(Temp_MQIsl18_HMed,   Temp_MQIsl18_HMed[0])

Temp_PCAN17_HMed    = np.append(Temp_PCAN17_HMed,    Temp_PCAN17_HMed[0])
Temp_SIPEXII12_HMed = np.append(Temp_SIPEXII12_HMed, Temp_SIPEXII12_HMed[0])

# SolRad
SR_Davis17_HMed1  = np.append(SR_Davis17_HMed1,  SR_Davis17_HMed1[0])
SR_Casey17_HMed   = np.append(SR_Casey17_HMed,   SR_Casey17_HMed[0])
SR_Mawson17_HMed  = np.append(SR_Mawson17_HMed,  SR_Mawson17_HMed[0])
SR_Davis17_HMed3  = np.append(SR_Davis17_HMed3,  SR_Davis17_HMed3[0])
SR_MQIsl17_HMed   = np.append(SR_MQIsl17_HMed,   SR_MQIsl17_HMed[0])

SR_Davis18_HMed1  = np.append(SR_Davis18_HMed1,  SR_Davis18_HMed1[0])
SR_Casey18_HMed   = np.append(SR_Casey18_HMed,   SR_Casey18_HMed[0])
SR_Mawson18_HMed  = np.append(SR_Mawson18_HMed,  SR_Mawson18_HMed[0])
SR_Davis18_HMed3  = np.append(SR_Davis18_HMed3,  SR_Davis18_HMed3[0])
SR_MQIsl18_HMed   = np.append(SR_MQIsl18_HMed,   SR_MQIsl18_HMed[0])

SR_PCAN17_HMed    = np.append(SR_PCAN17_HMed,    SR_PCAN17_HMed[0])
SR_SIPEXII12_HMed = np.append(SR_SIPEXII12_HMed, SR_SIPEXII12_HMed[0])

# Wind Speed
WS_Davis17_HMed1  = np.append(WS_Davis17_HMed1,  WS_Davis17_HMed1[0])
WS_Casey17_HMed   = np.append(WS_Casey17_HMed,   WS_Casey17_HMed[0])
WS_Mawson17_HMed = np.append(WS_Mawson17_HMed,  WS_Mawson17_HMed[0])
WS_Davis17_HMed3  = np.append(WS_Davis17_HMed3,  WS_Davis17_HMed3[0])
WS_MQIsl17_HMed   = np.append(WS_MQIsl17_HMed,   WS_MQIsl17_HMed[0])

WS_Davis18_HMed1  = np.append(WS_Davis18_HMed1,  WS_Davis18_HMed1[0])
WS_Casey18_HMed   = np.append(WS_Casey18_HMed,   WS_Casey18_HMed[0])
WS_Mawson18_HMed  = np.append(WS_Mawson18_HMed,  WS_Mawson18_HMed[0])
WS_Davis18_HMed3  = np.append(WS_Davis18_HMed3,  WS_Davis18_HMed3[0])
WS_MQIsl18_HMed   = np.append(WS_MQIsl18_HMed,   WS_MQIsl18_HMed[0])

WS_PCAN17_HMed    = np.append(WS_PCAN17_HMed,    WS_PCAN17_HMed[0])
WS_SIPEXII12_HMed = np.append(WS_SIPEXII12_HMed, WS_SIPEXII12_HMed[0])

# Sea Ice
Hg0_Ice_V1_17_HMed = np.append(Hg0_Ice_V1_17_HMed, Hg0_Ice_V1_17_HMed[0])
Hg0_Ice_V2_17_HMed = np.append(Hg0_Ice_V2_17_HMed, Hg0_Ice_V2_17_HMed[0])
Hg0_Ice_V3_17_HMed = np.append(Hg0_Ice_V3_17_HMed, Hg0_Ice_V3_17_HMed[0])

Hg0_Ice_V1_18_HMed = np.append(Hg0_Ice_V1_18_HMed, Hg0_Ice_V1_18_HMed[0])
Hg0_Ice_V2_18_HMed = np.append(Hg0_Ice_V2_18_HMed, Hg0_Ice_V2_18_HMed[0])
Hg0_Ice_V3_18_HMed = np.append(Hg0_Ice_V3_18_HMed, Hg0_Ice_V3_18_HMed[0])

# Sea Ice
Hg0_OW_V1_17_HMed  = np.append(Hg0_OW_V1_17_HMed,  Hg0_OW_V1_17_HMed[0])
Hg0_OW_V2_17_HMed  = np.append(Hg0_OW_V2_17_HMed,  Hg0_OW_V2_17_HMed[0])
Hg0_OW_V3_17_HMed  = np.append(Hg0_OW_V3_17_HMed,  Hg0_OW_V3_17_HMed[0])

Hg0_OW_V1_18_HMed  = np.append(Hg0_OW_V1_18_HMed,  Hg0_OW_V1_18_HMed[0])
Hg0_OW_V2_18_HMed  = np.append(Hg0_OW_V2_18_HMed,  Hg0_OW_V2_18_HMed[0])
Hg0_OW_V3_18_HMed  = np.append(Hg0_OW_V3_18_HMed,  Hg0_OW_V3_18_HMed[0])

#------------------------------------------------------------------------------
# CALCULATE THE STANDARD DEVIATION FOR THE Hg0 DAILY AVERAGE (MEAN)

# Function to calculate the standard deviation
def hourlySTD(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').std()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

#----------------------
# Whole Voyage
#----------------------
# Hg0
Hg0_V1_17_HSTD,   time1_HSTDa  = hourlySTD(V1_17_Hg0[:],   time1a) # V1_17
Hg0_V2_17_HSTD,   time2_HSTDa  = hourlySTD(V2_17_Hg0[:],   time2a) # V2_17
Hg0_V3_17M_HSTD,  time3_HSTDa  = hourlySTD(V3_17M_Hg0[:],  time3a) # V3_17 (Mawson)
Hg0_V3_17D_HSTD,  time4_HSTDa  = hourlySTD(V3_17D_Hg0[:],  time4a) # V3_17 (Davis)
Hg0_V4_17_HSTD,   time5_HSTDa  = hourlySTD(V4_17_Hg0[:],   time5a) # V4_17

Hg0_V1_18_HSTD,   time6_HSTDa  = hourlySTD(V1_18_Hg0[:],   time6a) # V1_18
Hg0_V2_18_HSTD,   time7_HSTDa  = hourlySTD(V2_18_Hg0[:],   time7a) # V2_18
Hg0_V3_18M_HSTD,  time8_HSTDa  = hourlySTD(V3_18M_Hg0[:],  time8a) # V3_18 (Mawson)
Hg0_V3_18D_HSTD,  time9_HSTDa  = hourlySTD(V3_18D_Hg0[:],  time9a) # V3_18 (Davis)
Hg0_V4_18_HSTD,   time10_HSTDa = hourlySTD(V4_18_Hg0[:],   time10a) # V4_18

Hg0_PCAN_HSTD,    time11_HSTDa = hourlySTD(PCAN_Hg0[:],    time11a) # PCAN
Hg0_SIPEXII_HSTD, time12_HSTDa = hourlySTD(SIPEXII_Hg0[:], time12a) # SIPEXII

# BrO
BrO_V1_17_HSTD,   time1_HSTDz  = hourlySTD(V1_17_BrO[:],   time1z) # V1_17
BrO_V2_17_HSTD,   time2_HSTDz  = hourlySTD(V2_17_BrO[:],   time2z) # V2_17
BrO_V3_17M_HSTD,  time3_HSTDz  = hourlySTD(V3_17M_BrO[:],  time3z) # V3_17 (Mawson)
BrO_V3_17D_HSTD,  time4_HSTDz  = hourlySTD(V3_17D_BrO[:],  time4z) # V3_17 (Davis)

BrO_V1_18_HSTD,   time6_HSTDz  = hourlySTD(V1_18_BrO[:],   time5z) # V1_18
BrO_V2_18_HSTD,   time7_HSTDz  = hourlySTD(V2_18_BrO[:],   time6z) # V2_18
BrO_V3_18M_HSTD,  time8_HSTDz  = hourlySTD(V3_18M_BrO[:],  time7z) # V3_18 (Mawson)
BrO_V3_18D_HSTD,  time9_HSTDz  = hourlySTD(V3_18D_BrO[:],  time8z) # V3_18 (Davis)

BrO_SIPEXII_HSTD, time12_HSTDz = hourlySTD(SIPEXII_BrO[:], time9z) # SIPEXII

#----------------------
# At Station
#----------------------
# Hg0
Hg0_Davis17_HSTD1,    time1_HSTDb  = hourlySTD(Hg0_Davis1_17[:],  time1b) # V1_17
Hg0_Casey17_HSTD,     time2_HSTDb  = hourlySTD(Hg0_Casey_17[:],   time2b) # V2_17
Hg0_Mawson17_HSTD,    time3_HSTDb  = hourlySTD(Hg0_Mawson_17[:],  time3b) # V3_17
Hg0_Davis17_HSTD3,    time4_HSTDb  = hourlySTD(Hg0_Davis3_17[:],  time4b) # V3_17
Hg0_MQIsl17_HSTD,     time5_HSTDb  = hourlySTD(Hg0_MQIsl_17[:],   time5b) # V4_17

Hg0_Davis18_HSTD1,    time6_HSTDb  = hourlySTD(Hg0_Davis1_18[:],  time6b) # V1_18
Hg0_Casey18_HSTD,     time7_HSTDb  = hourlySTD(Hg0_Casey_18[:],   time7b) # V2_18
Hg0_Mawson18_HSTD,    time8_HSTDb  = hourlySTD(Hg0_Mawson_18[:],  time8b) # V3_18
Hg0_Davis18_HSTD3,    time9_HSTDb  = hourlySTD(Hg0_Davis3_18[:],  time9b) # V3_18
Hg0_MQIsl18_HSTD,     time10_HSTDb = hourlySTD(Hg0_MQIsl_18[:],   time10b) # V4_18

Hg0_PCAN17_HSTD,    time11_HSTDb = hourlySTD(Hg0_PCAN_17[:],    time11b) # PCAN
Hg0_SIPEXII12_HSTD, time12_HSTDb = hourlySTD(Hg0_SIPEXII_12[:], time12b) # SIPEXII

# BrO
BrO_Davis17_HSTD1,  time1_HMy  = hourlySTD(BrO_Davis1_17[:], time1y) # V1_17
BrO_Casey17_HSTD,   time2_HMy  = hourlySTD(BrO_Casey_17[:],  time2y) # V2_17
BrO_Mawson17_HSTD,  time3_HMy  = hourlySTD(BrO_Mawson_17[:], time3y) # V3_17 (Mawson)
BrO_Davis17_HSTD3,  time4_HMy  = hourlySTD(BrO_Davis3_17[:], time4y) # V3_17 (Davis)

BrO_Davis18_HSTD1,  time6_HMy  = hourlySTD(BrO_Davis1_18[:], time5y) # V1_18
BrO_Casey18_HSTD,   time7_HMy  = hourlySTD(BrO_Casey_18[:],  time6y) # V2_18
BrO_Mawson18_HSTD,  time8_HMy  = hourlySTD(BrO_Mawson_18[:], time7y) # V3_18 (Mawson)
BrO_Davis18_HSTD3,  time9_HMy  = hourlySTD(BrO_Davis3_18[:], time8y) # V3_18 (Davis)

BrO_SIPEXII12_HSTD, time12_HMy = hourlySTD(BrO_SIPEXII_12[:], time9y) # SIPEXII

# O3
O3_Davis17_HSTD1,  time1_HMb  = hourlySTD(O3_Davis1_17[:], time1b_O3) # V1_17
O3_Casey17_HSTD,   time2_HMb  = hourlySTD(O3_Casey_17[:],  time2b_O3) # V2_17
O3_Mawson17_HSTD,  time3_HMb  = hourlySTD(O3_Mawson_17[:], time3b_O3) # V3_17 (Mawson)
O3_Davis17_HSTD3,  time4_HMb  = hourlySTD(O3_Davis3_17[:], time4b_O3) # V3_17 (Davis)
O3_MQIsl17_HSTD,   time5_HMb  = hourlySTD(O3_MQIsl_17[:],  time5b_O3) # V4_17

O3_Davis18_HSTD1,  time6_HMb  = hourlySTD(O3_Davis1_18[:], time6b_O3) # V1_18
O3_Casey18_HSTD,   time7_HMb  = hourlySTD(O3_Casey_18[:],  time7b_O3) # V2_18
O3_Mawson18_HSTD,  time8_HMb  = hourlySTD(O3_Mawson_18[:], time8b_O3) # V3_18 (Mawson)
O3_Davis18_HSTD3,  time9_HMb  = hourlySTD(O3_Davis3_18[:], time9b_O3) # V3_18 (Davis)
O3_MQIsl18_HSTD,   time10_HMb = hourlySTD(O3_MQIsl_18[:],  time10b_O3) # V4_18

O3_PCAN17_HSTD,    time11_HMb = hourlySTD(O3_PCAN_17[:],   time11b_O3) # PCAN
O3_SIPEXII12_HSTD, time12_HMb = hourlySTD(O3_SIPEXII_12[:],time12b_O3) # SIPEXII

# RH
RH_Davis17_HSTD1,    time1_HMb  = hourlySTD(np.array(Met_Davis_V1_17['RH_Avg']),  time1b_Met) # V1_17
RH_Casey17_HSTD,     time2_HMb  = hourlySTD(np.array(Met_Casey_V2_17['RH_Avg']),  time2b_Met) # V2_17
RH_Mawson17_HSTD,    time3_HMb  = hourlySTD(np.array(Met_Mawson_V3_17['RH_Avg']), time3b_Met) # V3_17
RH_Davis17_HSTD3,    time4_HMb  = hourlySTD(np.array(Met_Davis_V3_17['RH_Avg']),  time4b_Met) # V3_17
RH_MQIsl17_HSTD,     time5_HMb  = hourlySTD(np.array(Met_MQIsl_V4_17['RH_Avg']),  time5b_Met) # V4_17

RH_Davis18_HSTD1,    time6_HMb  = hourlySTD(np.array(Met_Davis_V1_18['RH_Avg']),  time6b_Met) # V1_18
RH_Casey18_HSTD,     time7_HMb  = hourlySTD(np.array(Met_Casey_V2_18['RH_Avg']),  time7b_Met) # V2_18
RH_Mawson18_HSTD,    time8_HMb  = hourlySTD(np.array(Met_Mawson_V3_18['RH_Avg']), time8b_Met) # V3_18
RH_Davis18_HSTD3,    time9_HMb  = hourlySTD(np.array(Met_Davis_V3_18['RH_Avg']),  time9b_Met) # V3_18
RH_MQIsl18_HSTD,     time10_HMb = hourlySTD(np.array(Met_MQIsl_V4_18['RH_Avg']),  time10b_Met) # V4_18

RH_PCAN17_HSTD,      time11_HMb = hourlySTD(np.array(Met_PCAN_Ice['RH_Avg']),     time11b_Met) # PCAN
RH_SIPEXII12_HSTD,   time12_HMb = hourlySTD(np.array(Met_SIPEXII_Ice['RH_Avg']),  time12b_Met) # SIPEXII

# Temp
Temp_Davis17_HSTD1,    time1_HMb  = hourlySTD(np.array(Met_Davis_V1_17['Temp_Avg']),  time1b_Met) # V1_17
Temp_Casey17_HSTD,     time2_HMb  = hourlySTD(np.array(Met_Casey_V2_17['Temp_Avg']),  time2b_Met) # V2_17
Temp_Mawson17_HSTD,    time3_HMb  = hourlySTD(np.array(Met_Mawson_V3_17['Temp_Avg']), time3b_Met) # V3_17
Temp_Davis17_HSTD3,    time4_HMb  = hourlySTD(np.array(Met_Davis_V3_17['Temp_Avg']),  time4b_Met) # V3_17
Temp_MQIsl17_HSTD,     time5_HMb  = hourlySTD(np.array(Met_MQIsl_V4_17['Temp_Avg']),  time5b_Met) # V4_17

Temp_Davis18_HSTD1,    time6_HMb  = hourlySTD(np.array(Met_Davis_V1_18['Temp_Avg']),  time6b_Met) # V1_18
Temp_Casey18_HSTD,     time7_HMb  = hourlySTD(np.array(Met_Casey_V2_18['Temp_Avg']),  time7b_Met) # V2_18
Temp_Mawson18_HSTD,    time8_HMb  = hourlySTD(np.array(Met_Mawson_V3_18['Temp_Avg']), time8b_Met) # V3_18
Temp_Davis18_HSTD3,    time9_HMb  = hourlySTD(np.array(Met_Davis_V3_18['Temp_Avg']),  time9b_Met) # V3_18
Temp_MQIsl18_HSTD,     time10_HMb = hourlySTD(np.array(Met_MQIsl_V4_18['Temp_Avg']),  time10b_Met) # V4_18

Temp_PCAN17_HSTD,      time11_HMb = hourlySTD(np.array(Met_PCAN_Ice['Temp_Avg']),     time11b_Met) # PCAN
Temp_SIPEXII12_HSTD,   time12_HMb = hourlySTD(np.array(Met_SIPEXII_Ice['Temp_Avg']),  time12b_Met) # SIPEXII

# SolRad
SR_Davis17_HSTD1,    time1_HMb  = hourlySTD(np.array(Met_Davis_V1_17['SolRad_Avg']),  time1b_Met) # V1_17
SR_Casey17_HSTD,     time2_HMb  = hourlySTD(np.array(Met_Casey_V2_17['SolRad_Avg']),  time2b_Met) # V2_17
SR_Mawson17_HSTD,    time3_HMb  = hourlySTD(np.array(Met_Mawson_V3_17['SolRad_Avg']), time3b_Met) # V3_17
SR_Davis17_HSTD3,    time4_HMb  = hourlySTD(np.array(Met_Davis_V3_17['SolRad_Avg']),  time4b_Met) # V3_17
SR_MQIsl17_HSTD,     time5_HMb  = hourlySTD(np.array(Met_MQIsl_V4_17['SolRad_Avg']),  time5b_Met) # V4_17

SR_Davis18_HSTD1,    time6_HMb  = hourlySTD(np.array(Met_Davis_V1_18['SolRad_Avg']),  time6b_Met) # V1_18
SR_Casey18_HSTD,     time7_HMb  = hourlySTD(np.array(Met_Casey_V2_18['SolRad_Avg']),  time7b_Met) # V2_18
SR_Mawson18_HSTD,    time8_HMb  = hourlySTD(np.array(Met_Mawson_V3_18['SolRad_Avg']), time8b_Met) # V3_18
SR_Davis18_HSTD3,    time9_HMb  = hourlySTD(np.array(Met_Davis_V3_18['SolRad_Avg']),  time9b_Met) # V3_18
SR_MQIsl18_HSTD,     time10_HMb = hourlySTD(np.array(Met_MQIsl_V4_18['SolRad_Avg']),  time10b_Met) # V4_18

SR_PCAN17_HSTD,      time11_HMb = hourlySTD(np.array(Met_PCAN_Ice['SolRad_Avg']),     time11b_Met) # PCAN
SR_SIPEXII12_HSTD,   time12_HMb = hourlySTD(np.array(Met_SIPEXII_Ice['SolRad_Avg']),  time12b_Met) # SIPEXII

# Wind Speed
WS_Davis17_HSTD1,    time1_HMb  = hourlySTD(np.array(Met_Davis_V1_17['WS_Avg']),  time1b_Met) # V1_17
WS_Casey17_HSTD,     time2_HMb  = hourlySTD(np.array(Met_Casey_V2_17['WS_Avg']),  time2b_Met) # V2_17
WS_Mawson17_HSTD,    time3_HMb  = hourlySTD(np.array(Met_Mawson_V3_17['WS_Avg']), time3b_Met) # V3_17
WS_Davis17_HSTD3,    time4_HMb  = hourlySTD(np.array(Met_Davis_V3_17['WS_Avg']),  time4b_Met) # V3_17
WS_MQIsl17_HSTD,     time5_HMb  = hourlySTD(np.array(Met_MQIsl_V4_17['WS_Avg']),  time5b_Met) # V4_17

WS_Davis18_HSTD1,    time6_HMb  = hourlySTD(np.array(Met_Davis_V1_18['WS_Avg']),  time6b_Met) # V1_18
WS_Casey18_HSTD,     time7_HMb  = hourlySTD(np.array(Met_Casey_V2_18['WS_Avg']),  time7b_Met) # V2_18
WS_Mawson18_HSTD,    time8_HMb  = hourlySTD(np.array(Met_Mawson_V3_18['WS_Avg']), time8b_Met) # V3_18
WS_Davis18_HSTD3,    time9_HMb  = hourlySTD(np.array(Met_Davis_V3_18['WS_Avg']),  time9b_Met) # V3_18
WS_MQIsl18_HSTD,     time10_HMb = hourlySTD(np.array(Met_MQIsl_V4_18['WS_Avg']),  time10b_Met) # V4_18

WS_PCAN17_HSTD,      time11_HMb = hourlySTD(np.array(Met_PCAN_Ice['WS_Avg']),     time11b_Met) # PCAN
WS_SIPEXII12_HSTD,   time12_HMb = hourlySTD(np.array(Met_SIPEXII_Ice['WS_Avg']),  time12b_Met) # SIPEXII

#----------------------
# Sea Ice
#----------------------
Hg0_Ice_V1_17_HSTD,   time1_HSTDc  = hourlySTD(Hg0_Ice1_V1_17[:], time1c) # V1_17
Hg0_Ice_V2_17_HSTD,   time2_HSTDc  = hourlySTD(Hg0_Ice1_V2_17[:], time2c) # V2_17
Hg0_Ice_V3_17_HSTD,   time3_HSTDc  = hourlySTD(Hg0_Ice1_V3_17[:], time3c) # V3_17

Hg0_Ice_V1_18_HSTD,   time4_HSTDc  = hourlySTD(Hg0_Ice1_V1_18[:], time4c) # V1_18
Hg0_Ice_V2_18_HSTD,   time5_HSTDc  = hourlySTD(Hg0_Ice1_V2_18[:], time5c) # V2_18
Hg0_Ice_V3_18_HSTD,   time6_HSTDc  = hourlySTD(Hg0_Ice1_V3_18[:], time6c) # V3_18

#----------------------
# Open Water
#----------------------
Hg0_OW_V1_17_HSTD,    time1_HSTDd  = hourlySTD(Hg0_OW1_V1_17[:], time1d) # V1_17
Hg0_OW_V2_17_HSTD,    time2_HSTDd  = hourlySTD(Hg0_OW1_V2_17[:], time2d) # V2_17
Hg0_OW_V3_17_HSTD,    time3_HSTDd  = hourlySTD(Hg0_OW1_V3_17[:], time3d) # V3_17

Hg0_OW_V1_18_HSTD,    time4_HSTDd  = hourlySTD(Hg0_OW1_V1_18[:], time4d) # V1_18
Hg0_OW_V2_18_HSTD,    time5_HSTDd  = hourlySTD(Hg0_OW1_V2_18[:], time5d) # V2_18
Hg0_OW_V3_18_HSTD,    time6_HSTDd  = hourlySTD(Hg0_OW1_V3_18[:], time6d) # V3_18

#------------------------------------------------------------------------------
# Append the first value to complete the diurnal cycle
# Hg0
Hg0_Davis17_HSTD1  = np.append(Hg0_Davis17_HSTD1,  Hg0_Davis17_HSTD1[0])
Hg0_Casey17_HSTD   = np.append(Hg0_Casey17_HSTD,   Hg0_Casey17_HSTD[0])
Hg0_Mawson17_HSTD  = np.append(Hg0_Mawson17_HSTD,  Hg0_Mawson17_HSTD[0])
Hg0_Davis17_HSTD3  = np.append(Hg0_Davis17_HSTD3,  Hg0_Davis17_HSTD3[0])
Hg0_MQIsl17_HSTD   = np.append(Hg0_MQIsl17_HSTD,   Hg0_MQIsl17_HSTD[0])

Hg0_Davis18_HSTD1  = np.append(Hg0_Davis18_HSTD1,  Hg0_Davis18_HSTD1[0])
Hg0_Casey18_HSTD   = np.append(Hg0_Casey18_HSTD,   Hg0_Casey18_HSTD[0])
Hg0_Mawson18_HSTD  = np.append(Hg0_Mawson18_HSTD,  Hg0_Mawson18_HSTD[0])
Hg0_Davis18_HSTD3  = np.append(Hg0_Davis18_HSTD3,  Hg0_Davis18_HSTD3[0])
Hg0_MQIsl18_HSTD   = np.append(Hg0_MQIsl18_HSTD,   Hg0_MQIsl18_HSTD[0])

Hg0_PCAN17_HSTD    = np.append(Hg0_PCAN17_HSTD,    Hg0_PCAN17_HSTD[0])
Hg0_SIPEXII12_HSTD = np.append(Hg0_SIPEXII12_HSTD, Hg0_SIPEXII12_HSTD[0])

# BrO
# BrO_Davis17_HSTD1  = np.append(BrO_Davis17_HSTD1,  BrO_Davis17_HSTD1[23])
# BrO_Casey17_HSTD   = np.append(BrO_Casey17_HSTD,   BrO_Casey17_HSTD[23])
# BrO_Mawson17_HSTD  = np.append(BrO_Mawson17_HSTD,  BrO_Mawson17_HSTD[23])
# BrO_Davis17_HSTD3  = np.append(BrO_Davis17_HSTD3,  BrO_Davis17_HSTD3[23])

# BrO_Davis18_HSTD1  = np.append(BrO_Davis18_HSTD1,  BrO_Davis18_HSTD1[23])
# BrO_Casey18_HSTD   = np.append(BrO_Casey18_HSTD,   BrO_Casey18_HSTD[23])
# BrO_Mawson18_HSTD  = np.append(BrO_Mawson18_HSTD,  BrO_Mawson18_HSTD[23])
# BrO_Davis18_HSTD3  = np.append(BrO_Davis18_HSTD3,  BrO_Davis18_HSTD3[23])

# BrO_SIPEXII12_HSTD = np.append(BrO_SIPEXII12_HSTD, BrO_SIPEXII12_HSTD[23])

# O3
O3_Davis17_HSTD1  = np.append(O3_Davis17_HSTD1,  O3_Davis17_HSTD1[0])
O3_Casey17_HSTD   = np.append(O3_Casey17_HSTD,   O3_Casey17_HSTD[0])
O3_Mawson17_HSTD  = np.append(O3_Mawson17_HSTD,  O3_Mawson17_HSTD[0])
O3_Davis17_HSTD3  = np.append(O3_Davis17_HSTD3,  O3_Davis17_HSTD3[0])
O3_MQIsl17_HSTD   = np.append(O3_MQIsl17_HSTD,   O3_MQIsl17_HSTD[0])

O3_Davis18_HSTD1  = np.append(O3_Davis18_HSTD1,  O3_Davis18_HSTD1[0])
O3_Casey18_HSTD   = np.append(O3_Casey18_HSTD,   O3_Casey18_HSTD[0])
O3_Mawson18_HSTD  = np.append(O3_Mawson18_HSTD,  O3_Mawson18_HSTD[0])
O3_Davis18_HSTD3  = np.append(O3_Davis18_HSTD3,  O3_Davis18_HSTD3[0])
O3_MQIsl18_HSTD   = np.append(O3_MQIsl18_HSTD,   O3_MQIsl18_HSTD[0])

O3_PCAN17_HSTD    = np.append(O3_PCAN17_HSTD,    O3_PCAN17_HSTD[0])
O3_SIPEXII12_HSTD = np.append(O3_SIPEXII12_HSTD, O3_SIPEXII12_HSTD[0])

# RH
RH_Davis17_HSTD1  = np.append(RH_Davis17_HSTD1,  RH_Davis17_HSTD1[0])
RH_Casey17_HSTD   = np.append(RH_Casey17_HSTD,   RH_Casey17_HSTD[0])
RH_Mawson17_HSTD  = np.append(RH_Mawson17_HSTD,  RH_Mawson17_HSTD[0])
RH_Davis17_HSTD3  = np.append(RH_Davis17_HSTD3,  RH_Davis17_HSTD3[0])
RH_MQIsl17_HSTD   = np.append(RH_MQIsl17_HSTD,   RH_MQIsl17_HSTD[0])

RH_Davis18_HSTD1  = np.append(RH_Davis18_HSTD1,  RH_Davis18_HSTD1[0])
RH_Casey18_HSTD   = np.append(RH_Casey18_HSTD,   RH_Casey18_HSTD[0])
RH_Mawson18_HSTD  = np.append(RH_Mawson18_HSTD,  RH_Mawson18_HSTD[0])
RH_Davis18_HSTD3  = np.append(RH_Davis18_HSTD3,  RH_Davis18_HSTD3[0])
RH_MQIsl18_HSTD   = np.append(RH_MQIsl18_HSTD,   RH_MQIsl18_HSTD[0])

RH_PCAN17_HSTD    = np.append(RH_PCAN17_HSTD,    RH_PCAN17_HSTD[0])
RH_SIPEXII12_HSTD = np.append(RH_SIPEXII12_HSTD, RH_SIPEXII12_HSTD[0])

# Temp
Temp_Davis17_HSTD1  = np.append(Temp_Davis17_HSTD1,  Temp_Davis17_HSTD1[0])
Temp_Casey17_HSTD   = np.append(Temp_Casey17_HSTD,   Temp_Casey17_HSTD[0])
Temp_Mawson17_HSTD  = np.append(Temp_Mawson17_HSTD,  Temp_Mawson17_HSTD[0])
Temp_Davis17_HSTD3  = np.append(Temp_Davis17_HSTD3,  Temp_Davis17_HSTD3[0])
Temp_MQIsl17_HSTD   = np.append(Temp_MQIsl17_HSTD,   Temp_MQIsl17_HSTD[0])

Temp_Davis18_HSTD1  = np.append(Temp_Davis18_HSTD1,  Temp_Davis18_HSTD1[0])
Temp_Casey18_HSTD   = np.append(Temp_Casey18_HSTD,   Temp_Casey18_HSTD[0])
Temp_Mawson18_HSTD  = np.append(Temp_Mawson18_HSTD,  Temp_Mawson18_HSTD[0])
Temp_Davis18_HSTD3  = np.append(Temp_Davis18_HSTD3,  Temp_Davis18_HSTD3[0])
Temp_MQIsl18_HSTD   = np.append(Temp_MQIsl18_HSTD,   Temp_MQIsl18_HSTD[0])

Temp_PCAN17_HSTD    = np.append(Temp_PCAN17_HSTD,    Temp_PCAN17_HSTD[0])
Temp_SIPEXII12_HSTD = np.append(Temp_SIPEXII12_HSTD, Temp_SIPEXII12_HSTD[0])

# SolRad
SR_Davis17_HSTD1  = np.append(SR_Davis17_HSTD1,  SR_Davis17_HSTD1[0])
SR_Casey17_HSTD   = np.append(SR_Casey17_HSTD,   SR_Casey17_HSTD[0])
SR_Mawson17_HSTD  = np.append(SR_Mawson17_HSTD,  SR_Mawson17_HSTD[0])
SR_Davis17_HSTD3  = np.append(SR_Davis17_HSTD3,  SR_Davis17_HSTD3[0])
SR_MQIsl17_HSTD   = np.append(SR_MQIsl17_HSTD,   SR_MQIsl17_HSTD[0])

SR_Davis18_HSTD1  = np.append(SR_Davis18_HSTD1,  SR_Davis18_HSTD1[0])
SR_Casey18_HSTD   = np.append(SR_Casey18_HSTD,   SR_Casey18_HSTD[0])
SR_Mawson18_HSTD  = np.append(SR_Mawson18_HSTD,  SR_Mawson18_HSTD[0])
SR_Davis18_HSTD3  = np.append(SR_Davis18_HSTD3,  SR_Davis18_HSTD3[0])
SR_MQIsl18_HSTD   = np.append(SR_MQIsl18_HSTD,   SR_MQIsl18_HSTD[0])

SR_PCAN17_HSTD    = np.append(SR_PCAN17_HSTD,    SR_PCAN17_HSTD[0])
SR_SIPEXII12_HSTD = np.append(SR_SIPEXII12_HSTD, SR_SIPEXII12_HSTD[0])

# Wind Speed
WS_Davis17_HSTD1  = np.append(WS_Davis17_HSTD1,  WS_Davis17_HSTD1[0])
WS_Casey17_HSTD   = np.append(WS_Casey17_HSTD,   WS_Casey17_HSTD[0])
WS_Mawson17_HSTD = np.append(WS_Mawson17_HSTD,  WS_Mawson17_HSTD[0])
WS_Davis17_HSTD3  = np.append(WS_Davis17_HSTD3,  WS_Davis17_HSTD3[0])
WS_MQIsl17_HSTD   = np.append(WS_MQIsl17_HSTD,   WS_MQIsl17_HSTD[0])

WS_Davis18_HSTD1  = np.append(WS_Davis18_HSTD1,  WS_Davis18_HSTD1[0])
WS_Casey18_HSTD   = np.append(WS_Casey18_HSTD,   WS_Casey18_HSTD[0])
WS_Mawson18_HSTD  = np.append(WS_Mawson18_HSTD,  WS_Mawson18_HSTD[0])
WS_Davis18_HSTD3  = np.append(WS_Davis18_HSTD3,  WS_Davis18_HSTD3[0])
WS_MQIsl18_HSTD   = np.append(WS_MQIsl18_HSTD,   WS_MQIsl18_HSTD[0])

WS_PCAN17_HSTD    = np.append(WS_PCAN17_HSTD,    WS_PCAN17_HSTD[0])
WS_SIPEXII12_HSTD = np.append(WS_SIPEXII12_HSTD, WS_SIPEXII12_HSTD[0])

# Sea Ice
Hg0_Ice_V1_17_HSTD = np.append(Hg0_Ice_V1_17_HSTD, Hg0_Ice_V1_17_HSTD[0])
Hg0_Ice_V2_17_HSTD = np.append(Hg0_Ice_V2_17_HSTD, Hg0_Ice_V2_17_HSTD[0])
Hg0_Ice_V3_17_HSTD = np.append(Hg0_Ice_V3_17_HSTD, Hg0_Ice_V3_17_HSTD[0])

Hg0_Ice_V1_18_HSTD = np.append(Hg0_Ice_V1_18_HSTD, Hg0_Ice_V1_18_HSTD[0])
Hg0_Ice_V2_18_HSTD = np.append(Hg0_Ice_V2_18_HSTD, Hg0_Ice_V2_18_HSTD[0])
Hg0_Ice_V3_18_HSTD = np.append(Hg0_Ice_V3_18_HSTD, Hg0_Ice_V3_18_HSTD[0])

# Sea Ice
Hg0_OW_V1_17_HSTD  = np.append(Hg0_OW_V1_17_HSTD,  Hg0_OW_V1_17_HSTD[0])
Hg0_OW_V2_17_HSTD  = np.append(Hg0_OW_V2_17_HSTD,  Hg0_OW_V2_17_HSTD[0])
Hg0_OW_V3_17_HSTD  = np.append(Hg0_OW_V3_17_HSTD,  Hg0_OW_V3_17_HSTD[0])

Hg0_OW_V1_18_HSTD  = np.append(Hg0_OW_V1_18_HSTD,  Hg0_OW_V1_18_HSTD[0])
Hg0_OW_V2_18_HSTD  = np.append(Hg0_OW_V2_18_HSTD,  Hg0_OW_V2_18_HSTD[0])
Hg0_OW_V3_18_HSTD  = np.append(Hg0_OW_V3_18_HSTD,  Hg0_OW_V3_18_HSTD[0])

#------------------------------------------------------------------------------
# CALCULATE THE 5th PERCENTILE FOR THE Hg0 DAILY AVERAGE (MEAN)

# Function to calculate the standard deviation
def hourly5P(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').quantile(q=0.05)
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

#----------------------
# Whole Voyage
#----------------------
# Hg0
Hg0_V1_17_H5P,     time1_H5Pa  = hourly5P(V1_17_Hg0[:],      time1a) # V1_17
Hg0_V2_17_H5P,     time2_H5Pa  = hourly5P(V2_17_Hg0[:],      time2a) # V2_17
Hg0_V3_17M_H5P,    time3_H5Pa  = hourly5P(V3_17M_Hg0[:],     time3a) # V3_17 (Mawson)
Hg0_V3_17D_H5P,    time4_H5Pa  = hourly5P(V3_17D_Hg0[:],     time4a) # V3_17 (Davis)
Hg0_V4_17_H5P,     time5_H5Pa  = hourly5P(V4_17_Hg0[:],      time5a) # V4_17

Hg0_V1_18_H5P,     time6_H5Pa  = hourly5P(V1_18_Hg0[:],      time6a) # V1_18
Hg0_V2_18_H5P,     time7_H5Pa  = hourly5P(V2_18_Hg0[:],      time7a) # V2_18
Hg0_V3_18M_H5P,    time8_H5Pa  = hourly5P(V3_18M_Hg0[:],     time8a) # V3_18 (Mawson)
Hg0_V3_18D_H5P,    time9_H5Pa  = hourly5P(V3_18D_Hg0[:],     time9a) # V3_18 (Davis)
Hg0_V4_18_H5P,     time10_H5Pa = hourly5P(V4_18_Hg0[:],      time10a) # V4_18

Hg0_PCAN_H5P,      time11_H5Pa = hourly5P(PCAN_Hg0[:],       time11a) # PCAN
Hg0_SIPEXII_H5P,   time12_H5Pa = hourly5P(SIPEXII_Hg0[:],    time12a) # SIPEXII

# BrO
BrO_V1_17_H5P,   time1_HMz  = hourly5P(V1_17_BrO[:],   time1z) # V1_17
BrO_V2_17_H5P,   time2_HMz  = hourly5P(V2_17_BrO[:],   time2z) # V2_17
BrO_V3_17M_H5P,  time3_HMz  = hourly5P(V3_17M_BrO[:],  time3z) # V3_17 (Mawson)
BrO_V3_17D_H5P,  time4_HMz  = hourly5P(V3_17D_BrO[:],  time4z) # V3_17 (Davis)

BrO_V1_18_H5P,   time6_HMz  = hourly5P(V1_18_BrO[:],   time5z) # V1_18
BrO_V2_18_H5P,   time7_HMz  = hourly5P(V2_18_BrO[:],   time6z) # V2_18
BrO_V3_18M_H5P,  time8_HMz  = hourly5P(V3_18M_BrO[:],  time7z) # V3_18 (Mawson)
BrO_V3_18D_H5P,  time9_HMz  = hourly5P(V3_18D_BrO[:],  time8z) # V3_18 (Davis)

BrO_SIPEXII_H5P, time12_HMz = hourly5P(SIPEXII_BrO[:], time9z) # SIPEXII

#----------------------
# At Station
#----------------------
# Hg0
Hg0_Davis17_H5P1,  time1_H5Pb  = hourly5P(Hg0_Davis1_17[:],  time1b) # V1_17
Hg0_Casey17_H5P,   time2_H5Pb  = hourly5P(Hg0_Casey_17[:],   time2b) # V2_17
Hg0_Mawson17_H5P,  time3_H5Pb  = hourly5P(Hg0_Mawson_17[:],  time3b) # V3_17
Hg0_Davis17_H5P3,  time4_H5Pb  = hourly5P(Hg0_Davis3_17[:],  time4b) # V3_17
Hg0_MQIsl17_H5P,   time5_H5Pb  = hourly5P(Hg0_MQIsl_17[:],   time5b) # V4_17

Hg0_Davis18_H5P1,  time6_H5Pb  = hourly5P(Hg0_Davis1_18[:],  time6b) # V1_18
Hg0_Casey18_H5P,   time7_H5Pb  = hourly5P(Hg0_Casey_18[:],   time7b) # V2_18
Hg0_Mawson18_H5P,  time8_H5Pb  = hourly5P(Hg0_Mawson_18[:],  time8b) # V3_18
Hg0_Davis18_H5P3,  time9_H5Pb  = hourly5P(Hg0_Davis3_18[:],  time9b) # V3_18
Hg0_MQIsl18_H5P,   time10_H5Pb = hourly5P(Hg0_MQIsl_18[:],   time10b) # V4_18

Hg0_PCAN17_H5P,    time11_H5Pb = hourly5P(Hg0_PCAN_17[:],    time11b) # PCAN
Hg0_SIPEXII12_H5P, time12_H5Pb = hourly5P(Hg0_SIPEXII_12[:], time12b) # SIPEXII

# BrO
BrO_Davis17_H5P1,  time1_HMy  = hourly5P(BrO_Davis1_17[:], time1y) # V1_17
BrO_Casey17_H5P,   time2_HMy  = hourly5P(BrO_Casey_17[:],  time2y) # V2_17
BrO_Mawson17_H5P,  time3_HMy  = hourly5P(BrO_Mawson_17[:], time3y) # V3_17 (Mawson)
BrO_Davis17_H5P3,  time4_HMy  = hourly5P(BrO_Davis3_17[:], time4y) # V3_17 (Davis)

BrO_Davis18_H5P1,  time6_HMy  = hourly5P(BrO_Davis1_18[:], time5y) # V1_18
BrO_Casey18_H5P,   time7_HMy  = hourly5P(BrO_Casey_18[:],  time6y) # V2_18
BrO_Mawson18_H5P,  time8_HMy  = hourly5P(BrO_Mawson_18[:], time7y) # V3_18 (Mawson)
BrO_Davis18_H5P3,  time9_HMy  = hourly5P(BrO_Davis3_18[:], time8y) # V3_18 (Davis)

BrO_SIPEXII12_H5P, time12_HMy = hourly5P(BrO_SIPEXII_12[:], time9y) # SIPEXII

# O3
O3_Davis17_H5P1,  time1_HMb  = hourly5P(O3_Davis1_17[:], time1b_O3) # V1_17
O3_Casey17_H5P,   time2_HMb  = hourly5P(O3_Casey_17[:],  time2b_O3) # V2_17
O3_Mawson17_H5P,  time3_HMb  = hourly5P(O3_Mawson_17[:], time3b_O3) # V3_17 (Mawson)
O3_Davis17_H5P3,  time4_HMb  = hourly5P(O3_Davis3_17[:], time4b_O3) # V3_17 (Davis)
O3_MQIsl17_H5P,   time5_HMb  = hourly5P(O3_MQIsl_17[:],  time5b_O3) # V4_17

O3_Davis18_H5P1,  time6_HMb  = hourly5P(O3_Davis1_18[:], time6b_O3) # V1_18
O3_Casey18_H5P,   time7_HMb  = hourly5P(O3_Casey_18[:],  time7b_O3) # V2_18
O3_Mawson18_H5P,  time8_HMb  = hourly5P(O3_Mawson_18[:], time8b_O3) # V3_18 (Mawson)
O3_Davis18_H5P3,  time9_HMb  = hourly5P(O3_Davis3_18[:], time9b_O3) # V3_18 (Davis)
O3_MQIsl18_H5P,   time10_HMb = hourly5P(O3_MQIsl_18[:],  time10b_O3) # V4_18

O3_PCAN17_H5P,    time11_HMb = hourly5P(O3_PCAN_17[:],   time11b_O3) # PCAN
O3_SIPEXII12_H5P, time12_HMb = hourly5P(O3_SIPEXII_12[:],time12b_O3) # SIPEXII

# RH
RH_Davis17_H5P1,    time1_HMb  = hourly5P(np.array(Met_Davis_V1_17['RH_Avg']),  time1b_Met) # V1_17
RH_Casey17_H5P,     time2_HMb  = hourly5P(np.array(Met_Casey_V2_17['RH_Avg']),  time2b_Met) # V2_17
RH_Mawson17_H5P,    time3_HMb  = hourly5P(np.array(Met_Mawson_V3_17['RH_Avg']), time3b_Met) # V3_17
RH_Davis17_H5P3,    time4_HMb  = hourly5P(np.array(Met_Davis_V3_17['RH_Avg']),  time4b_Met) # V3_17
RH_MQIsl17_H5P,     time5_HMb  = hourly5P(np.array(Met_MQIsl_V4_17['RH_Avg']),  time5b_Met) # V4_17

RH_Davis18_H5P1,    time6_HMb  = hourly5P(np.array(Met_Davis_V1_18['RH_Avg']),  time6b_Met) # V1_18
RH_Casey18_H5P,     time7_HMb  = hourly5P(np.array(Met_Casey_V2_18['RH_Avg']),  time7b_Met) # V2_18
RH_Mawson18_H5P,    time8_HMb  = hourly5P(np.array(Met_Mawson_V3_18['RH_Avg']), time8b_Met) # V3_18
RH_Davis18_H5P3,    time9_HMb  = hourly5P(np.array(Met_Davis_V3_18['RH_Avg']),  time9b_Met) # V3_18
RH_MQIsl18_H5P,     time10_HMb = hourly5P(np.array(Met_MQIsl_V4_18['RH_Avg']),  time10b_Met) # V4_18

RH_PCAN17_H5P,      time11_HMb = hourly5P(np.array(Met_PCAN_Ice['RH_Avg']),     time11b_Met) # PCAN
RH_SIPEXII12_H5P,   time12_HMb = hourly5P(np.array(Met_SIPEXII_Ice['RH_Avg']),  time12b_Met) # SIPEXII

# Temp
Temp_Davis17_H5P1,    time1_HMb  = hourly5P(np.array(Met_Davis_V1_17['Temp_Avg']),  time1b_Met) # V1_17
Temp_Casey17_H5P,     time2_HMb  = hourly5P(np.array(Met_Casey_V2_17['Temp_Avg']),  time2b_Met) # V2_17
Temp_Mawson17_H5P,    time3_HMb  = hourly5P(np.array(Met_Mawson_V3_17['Temp_Avg']), time3b_Met) # V3_17
Temp_Davis17_H5P3,    time4_HMb  = hourly5P(np.array(Met_Davis_V3_17['Temp_Avg']),  time4b_Met) # V3_17
Temp_MQIsl17_H5P,     time5_HMb  = hourly5P(np.array(Met_MQIsl_V4_17['Temp_Avg']),  time5b_Met) # V4_17

Temp_Davis18_H5P1,    time6_HMb  = hourly5P(np.array(Met_Davis_V1_18['Temp_Avg']),  time6b_Met) # V1_18
Temp_Casey18_H5P,     time7_HMb  = hourly5P(np.array(Met_Casey_V2_18['Temp_Avg']),  time7b_Met) # V2_18
Temp_Mawson18_H5P,    time8_HMb  = hourly5P(np.array(Met_Mawson_V3_18['Temp_Avg']), time8b_Met) # V3_18
Temp_Davis18_H5P3,    time9_HMb  = hourly5P(np.array(Met_Davis_V3_18['Temp_Avg']),  time9b_Met) # V3_18
Temp_MQIsl18_H5P,     time10_HMb = hourly5P(np.array(Met_MQIsl_V4_18['Temp_Avg']),  time10b_Met) # V4_18

Temp_PCAN17_H5P,      time11_HMb = hourly5P(np.array(Met_PCAN_Ice['Temp_Avg']),     time11b_Met) # PCAN
Temp_SIPEXII12_H5P,   time12_HMb = hourly5P(np.array(Met_SIPEXII_Ice['Temp_Avg']),  time12b_Met) # SIPEXII

# SolRad
SR_Davis17_H5P1,    time1_HMb  = hourly5P(np.array(Met_Davis_V1_17['SolRad_Avg']),  time1b_Met) # V1_17
SR_Casey17_H5P,     time2_HMb  = hourly5P(np.array(Met_Casey_V2_17['SolRad_Avg']),  time2b_Met) # V2_17
SR_Mawson17_H5P,    time3_HMb  = hourly5P(np.array(Met_Mawson_V3_17['SolRad_Avg']), time3b_Met) # V3_17
SR_Davis17_H5P3,    time4_HMb  = hourly5P(np.array(Met_Davis_V3_17['SolRad_Avg']),  time4b_Met) # V3_17
SR_MQIsl17_H5P,     time5_HMb  = hourly5P(np.array(Met_MQIsl_V4_17['SolRad_Avg']),  time5b_Met) # V4_17

SR_Davis18_H5P1,    time6_HMb  = hourly5P(np.array(Met_Davis_V1_18['SolRad_Avg']),  time6b_Met) # V1_18
SR_Casey18_H5P,     time7_HMb  = hourly5P(np.array(Met_Casey_V2_18['SolRad_Avg']),  time7b_Met) # V2_18
SR_Mawson18_H5P,    time8_HMb  = hourly5P(np.array(Met_Mawson_V3_18['SolRad_Avg']), time8b_Met) # V3_18
SR_Davis18_H5P3,    time9_HMb  = hourly5P(np.array(Met_Davis_V3_18['SolRad_Avg']),  time9b_Met) # V3_18
SR_MQIsl18_H5P,     time10_HMb = hourly5P(np.array(Met_MQIsl_V4_18['SolRad_Avg']),  time10b_Met) # V4_18

SR_PCAN17_H5P,      time11_HMb = hourly5P(np.array(Met_PCAN_Ice['SolRad_Avg']),     time11b_Met) # PCAN
SR_SIPEXII12_H5P,   time12_HMb = hourly5P(np.array(Met_SIPEXII_Ice['SolRad_Avg']),  time12b_Met) # SIPEXII

# Wind Speed
WS_Davis17_H5P1,    time1_HMb  = hourly5P(np.array(Met_Davis_V1_17['WS_Avg']),  time1b_Met) # V1_17
WS_Casey17_H5P,     time2_HMb  = hourly5P(np.array(Met_Casey_V2_17['WS_Avg']),  time2b_Met) # V2_17
WS_Mawson17_H5P,    time3_HMb  = hourly5P(np.array(Met_Mawson_V3_17['WS_Avg']), time3b_Met) # V3_17
WS_Davis17_H5P3,    time4_HMb  = hourly5P(np.array(Met_Davis_V3_17['WS_Avg']),  time4b_Met) # V3_17
WS_MQIsl17_H5P,     time5_HMb  = hourly5P(np.array(Met_MQIsl_V4_17['WS_Avg']),  time5b_Met) # V4_17

WS_Davis18_H5P1,    time6_HMb  = hourly5P(np.array(Met_Davis_V1_18['WS_Avg']),  time6b_Met) # V1_18
WS_Casey18_H5P,     time7_HMb  = hourly5P(np.array(Met_Casey_V2_18['WS_Avg']),  time7b_Met) # V2_18
WS_Mawson18_H5P,    time8_HMb  = hourly5P(np.array(Met_Mawson_V3_18['WS_Avg']), time8b_Met) # V3_18
WS_Davis18_H5P3,    time9_HMb  = hourly5P(np.array(Met_Davis_V3_18['WS_Avg']),  time9b_Met) # V3_18
WS_MQIsl18_H5P,     time10_HMb = hourly5P(np.array(Met_MQIsl_V4_18['WS_Avg']),  time10b_Met) # V4_18

WS_PCAN17_H5P,      time11_HMb = hourly5P(np.array(Met_PCAN_Ice['WS_Avg']),     time11b_Met) # PCAN
WS_SIPEXII12_H5P,   time12_HMb = hourly5P(np.array(Met_SIPEXII_Ice['WS_Avg']),  time12b_Met) # SIPEXII

#----------------------
# Sea Ice
#----------------------
Hg0_Ice_V1_17_H5P, time1_H5Pc  = hourly5P(Hg0_Ice1_V1_17[:], time1c) # V1_17
Hg0_Ice_V2_17_H5P, time2_H5Pc  = hourly5P(Hg0_Ice1_V2_17[:], time2c) # V2_17
Hg0_Ice_V3_17_H5P, time3_H5Pc  = hourly5P(Hg0_Ice1_V3_17[:], time3c) # V3_17

Hg0_Ice_V1_18_H5P, time4_H5Pc  = hourly5P(Hg0_Ice1_V1_18[:], time4c) # V1_18
Hg0_Ice_V2_18_H5P, time5_H5Pc  = hourly5P(Hg0_Ice1_V2_18[:], time5c) # V2_18
Hg0_Ice_V3_18_H5P, time6_H5Pc  = hourly5P(Hg0_Ice1_V3_18[:], time6c) # V3_18

#----------------------
# Open Water
#----------------------
Hg0_OW_V1_17_H5P,  time1_H5Pd  = hourly5P(Hg0_OW1_V1_17[:], time1d) # V1_17
Hg0_OW_V2_17_H5P,  time2_H5Pd  = hourly5P(Hg0_OW1_V2_17[:], time2d) # V2_17
Hg0_OW_V3_17_H5P,  time3_H5Pd  = hourly5P(Hg0_OW1_V3_17[:], time3d) # V3_17

Hg0_OW_V1_18_H5P,  time4_H5Pd  = hourly5P(Hg0_OW1_V1_18[:], time4d) # V1_18
Hg0_OW_V2_18_H5P,  time5_H5Pd  = hourly5P(Hg0_OW1_V2_18[:], time5d) # V2_18
Hg0_OW_V3_18_H5P,  time6_H5Pd  = hourly5P(Hg0_OW1_V3_18[:], time6d) # V3_18

#------------------------------------------------------------------------------
# Append the first value to complete the diurnal cycle
# Hg0
Hg0_Davis17_H5P1  = np.append(Hg0_Davis17_H5P1,  Hg0_Davis17_H5P1[0])
Hg0_Casey17_H5P   = np.append(Hg0_Casey17_H5P,   Hg0_Casey17_H5P[0])
Hg0_Mawson17_H5P  = np.append(Hg0_Mawson17_H5P,  Hg0_Mawson17_H5P[0])
Hg0_Davis17_H5P3  = np.append(Hg0_Davis17_H5P3,  Hg0_Davis17_H5P3[0])
Hg0_MQIsl17_H5P   = np.append(Hg0_MQIsl17_H5P,   Hg0_MQIsl17_H5P[0])

Hg0_Davis18_H5P1  = np.append(Hg0_Davis18_H5P1,  Hg0_Davis18_H5P1[0])
Hg0_Casey18_H5P   = np.append(Hg0_Casey18_H5P,   Hg0_Casey18_H5P[0])
Hg0_Mawson18_H5P  = np.append(Hg0_Mawson18_H5P,  Hg0_Mawson18_H5P[0])
Hg0_Davis18_H5P3  = np.append(Hg0_Davis18_H5P3,  Hg0_Davis18_H5P3[0])
Hg0_MQIsl18_H5P   = np.append(Hg0_MQIsl18_H5P,   Hg0_MQIsl18_H5P[0])

Hg0_PCAN17_H5P    = np.append(Hg0_PCAN17_H5P,    Hg0_PCAN17_H5P[0])
Hg0_SIPEXII12_H5P = np.append(Hg0_SIPEXII12_H5P, Hg0_SIPEXII12_H5P[0])

# BrO
# BrO_Davis17_H5P1  = np.append(BrO_Davis17_H5P1,  BrO_Davis17_H5P1[23])
# BrO_Casey17_H5P   = np.append(BrO_Casey17_H5P,   BrO_Casey17_H5P[23])
# BrO_Mawson17_H5P  = np.append(BrO_Mawson17_H5P,  BrO_Mawson17_H5P[23])
# BrO_Davis17_H5P3  = np.append(BrO_Davis17_H5P3,  BrO_Davis17_H5P3[23])

# BrO_Davis18_H5P1  = np.append(BrO_Davis18_H5P1,  BrO_Davis18_H5P1[23])
# BrO_Casey18_H5P   = np.append(BrO_Casey18_H5P,   BrO_Casey18_H5P[23])
# BrO_Mawson18_H5P  = np.append(BrO_Mawson18_H5P,  BrO_Mawson18_H5P[23])
# BrO_Davis18_H5P3  = np.append(BrO_Davis18_H5P3,  BrO_Davis18_H5P3[23])

# BrO_SIPEXII12_H5P = np.append(BrO_SIPEXII12_H5P, BrO_SIPEXII12_H5P[23])

# O3
O3_Davis17_H5P1  = np.append(O3_Davis17_H5P1,  O3_Davis17_H5P1[0])
O3_Casey17_H5P   = np.append(O3_Casey17_H5P,   O3_Casey17_H5P[0])
O3_Mawson17_H5P  = np.append(O3_Mawson17_H5P,  O3_Mawson17_H5P[0])
O3_Davis17_H5P3  = np.append(O3_Davis17_H5P3,  O3_Davis17_H5P3[0])
O3_MQIsl17_H5P   = np.append(O3_MQIsl17_H5P,   O3_MQIsl17_H5P[0])

O3_Davis18_H5P1  = np.append(O3_Davis18_H5P1,  O3_Davis18_H5P1[0])
O3_Casey18_H5P   = np.append(O3_Casey18_H5P,   O3_Casey18_H5P[0])
O3_Mawson18_H5P  = np.append(O3_Mawson18_H5P,  O3_Mawson18_H5P[0])
O3_Davis18_H5P3  = np.append(O3_Davis18_H5P3,  O3_Davis18_H5P3[0])
O3_MQIsl18_H5P   = np.append(O3_MQIsl18_H5P,   O3_MQIsl18_H5P[0])

O3_PCAN17_H5P    = np.append(O3_PCAN17_H5P,    O3_PCAN17_H5P[0])
O3_SIPEXII12_H5P = np.append(O3_SIPEXII12_H5P, O3_SIPEXII12_H5P[0])

# RH
RH_Davis17_H5P1  = np.append(RH_Davis17_H5P1,  RH_Davis17_H5P1[0])
RH_Casey17_H5P   = np.append(RH_Casey17_H5P,   RH_Casey17_H5P[0])
RH_Mawson17_H5P  = np.append(RH_Mawson17_H5P,  RH_Mawson17_H5P[0])
RH_Davis17_H5P3  = np.append(RH_Davis17_H5P3,  RH_Davis17_H5P3[0])
RH_MQIsl17_H5P   = np.append(RH_MQIsl17_H5P,   RH_MQIsl17_H5P[0])

RH_Davis18_H5P1  = np.append(RH_Davis18_H5P1,  RH_Davis18_H5P1[0])
RH_Casey18_H5P   = np.append(RH_Casey18_H5P,   RH_Casey18_H5P[0])
RH_Mawson18_H5P  = np.append(RH_Mawson18_H5P,  RH_Mawson18_H5P[0])
RH_Davis18_H5P3  = np.append(RH_Davis18_H5P3,  RH_Davis18_H5P3[0])
RH_MQIsl18_H5P   = np.append(RH_MQIsl18_H5P,   RH_MQIsl18_H5P[0])

RH_PCAN17_H5P    = np.append(RH_PCAN17_H5P,    RH_PCAN17_H5P[0])
RH_SIPEXII12_H5P = np.append(RH_SIPEXII12_H5P, RH_SIPEXII12_H5P[0])

# Temp
Temp_Davis17_H5P1  = np.append(Temp_Davis17_H5P1,  Temp_Davis17_H5P1[0])
Temp_Casey17_H5P   = np.append(Temp_Casey17_H5P,   Temp_Casey17_H5P[0])
Temp_Mawson17_H5P  = np.append(Temp_Mawson17_H5P,  Temp_Mawson17_H5P[0])
Temp_Davis17_H5P3  = np.append(Temp_Davis17_H5P3,  Temp_Davis17_H5P3[0])
Temp_MQIsl17_H5P   = np.append(Temp_MQIsl17_H5P,   Temp_MQIsl17_H5P[0])

Temp_Davis18_H5P1  = np.append(Temp_Davis18_H5P1,  Temp_Davis18_H5P1[0])
Temp_Casey18_H5P   = np.append(Temp_Casey18_H5P,   Temp_Casey18_H5P[0])
Temp_Mawson18_H5P  = np.append(Temp_Mawson18_H5P,  Temp_Mawson18_H5P[0])
Temp_Davis18_H5P3  = np.append(Temp_Davis18_H5P3,  Temp_Davis18_H5P3[0])
Temp_MQIsl18_H5P   = np.append(Temp_MQIsl18_H5P,   Temp_MQIsl18_H5P[0])

Temp_PCAN17_H5P    = np.append(Temp_PCAN17_H5P,    Temp_PCAN17_H5P[0])
Temp_SIPEXII12_H5P = np.append(Temp_SIPEXII12_H5P, Temp_SIPEXII12_H5P[0])

# SolRad
SR_Davis17_H5P1  = np.append(SR_Davis17_H5P1,  SR_Davis17_H5P1[0])
SR_Casey17_H5P   = np.append(SR_Casey17_H5P,   SR_Casey17_H5P[0])
SR_Mawson17_H5P  = np.append(SR_Mawson17_H5P,  SR_Mawson17_H5P[0])
SR_Davis17_H5P3  = np.append(SR_Davis17_H5P3,  SR_Davis17_H5P3[0])
SR_MQIsl17_H5P   = np.append(SR_MQIsl17_H5P,   SR_MQIsl17_H5P[0])

SR_Davis18_H5P1  = np.append(SR_Davis18_H5P1,  SR_Davis18_H5P1[0])
SR_Casey18_H5P   = np.append(SR_Casey18_H5P,   SR_Casey18_H5P[0])
SR_Mawson18_H5P  = np.append(SR_Mawson18_H5P,  SR_Mawson18_H5P[0])
SR_Davis18_H5P3  = np.append(SR_Davis18_H5P3,  SR_Davis18_H5P3[0])
SR_MQIsl18_H5P   = np.append(SR_MQIsl18_H5P,   SR_MQIsl18_H5P[0])

SR_PCAN17_H5P    = np.append(SR_PCAN17_H5P,    SR_PCAN17_H5P[0])
SR_SIPEXII12_H5P = np.append(SR_SIPEXII12_H5P, SR_SIPEXII12_H5P[0])

# Wind Speed
WS_Davis17_H5P1  = np.append(WS_Davis17_H5P1,  WS_Davis17_H5P1[0])
WS_Casey17_H5P   = np.append(WS_Casey17_H5P,   WS_Casey17_H5P[0])
WS_Mawson17_H5P = np.append(WS_Mawson17_H5P,  WS_Mawson17_H5P[0])
WS_Davis17_H5P3  = np.append(WS_Davis17_H5P3,  WS_Davis17_H5P3[0])
WS_MQIsl17_H5P   = np.append(WS_MQIsl17_H5P,   WS_MQIsl17_H5P[0])

WS_Davis18_H5P1  = np.append(WS_Davis18_H5P1,  WS_Davis18_H5P1[0])
WS_Casey18_H5P   = np.append(WS_Casey18_H5P,   WS_Casey18_H5P[0])
WS_Mawson18_H5P  = np.append(WS_Mawson18_H5P,  WS_Mawson18_H5P[0])
WS_Davis18_H5P3  = np.append(WS_Davis18_H5P3,  WS_Davis18_H5P3[0])
WS_MQIsl18_H5P   = np.append(WS_MQIsl18_H5P,   WS_MQIsl18_H5P[0])

WS_PCAN17_H5P    = np.append(WS_PCAN17_H5P,    WS_PCAN17_H5P[0])
WS_SIPEXII12_H5P = np.append(WS_SIPEXII12_H5P, WS_SIPEXII12_H5P[0])

# Sea Ice
Hg0_Ice_V1_17_H5P = np.append(Hg0_Ice_V1_17_H5P, Hg0_Ice_V1_17_H5P[0])
Hg0_Ice_V2_17_H5P = np.append(Hg0_Ice_V2_17_H5P, Hg0_Ice_V2_17_H5P[0])
Hg0_Ice_V3_17_H5P = np.append(Hg0_Ice_V3_17_H5P, Hg0_Ice_V3_17_H5P[0])

Hg0_Ice_V1_18_H5P = np.append(Hg0_Ice_V1_18_H5P, Hg0_Ice_V1_18_H5P[0])
Hg0_Ice_V2_18_H5P = np.append(Hg0_Ice_V2_18_H5P, Hg0_Ice_V2_18_H5P[0])
Hg0_Ice_V3_18_H5P = np.append(Hg0_Ice_V3_18_H5P, Hg0_Ice_V3_18_H5P[0])

# Sea Ice
Hg0_OW_V1_17_H5P  = np.append(Hg0_OW_V1_17_H5P,  Hg0_OW_V1_17_H5P[0])
Hg0_OW_V2_17_H5P  = np.append(Hg0_OW_V2_17_H5P,  Hg0_OW_V2_17_H5P[0])
Hg0_OW_V3_17_H5P  = np.append(Hg0_OW_V3_17_H5P,  Hg0_OW_V3_17_H5P[0])

Hg0_OW_V1_18_H5P  = np.append(Hg0_OW_V1_18_H5P,  Hg0_OW_V1_18_H5P[0])
Hg0_OW_V2_18_H5P  = np.append(Hg0_OW_V2_18_H5P,  Hg0_OW_V2_18_H5P[0])
Hg0_OW_V3_18_H5P  = np.append(Hg0_OW_V3_18_H5P,  Hg0_OW_V3_18_H5P[0])

#------------------------------------------------------------------------------
# CALCULATE THE 25th PERCENTILE FOR THE Hg0 DAILY AVERAGE (MEAN)

# Function to calculate the standard deviation
def hourly25P(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').quantile(q=0.25)
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

#----------------------
# Whole Voyage
#----------------------
# Hg0
Hg0_V1_17_H25P,     time1_H25Pa  = hourly25P(V1_17_Hg0[:],      time1a) # V1_17
Hg0_V2_17_H25P,     time2_H25Pa  = hourly25P(V2_17_Hg0[:],      time2a) # V2_17
Hg0_V3_17M_H25P,    time3_H25Pa  = hourly25P(V3_17M_Hg0[:],     time3a) # V3_17 (Mawson)
Hg0_V3_17D_H25P,    time4_H25Pa  = hourly25P(V3_17D_Hg0[:],     time4a) # V3_17 (Davis)
Hg0_V4_17_H25P,     time5_H25Pa  = hourly25P(V4_17_Hg0[:],      time5a) # V4_17

Hg0_V1_18_H25P,     time6_H25Pa  = hourly25P(V1_18_Hg0[:],      time6a) # V1_18
Hg0_V2_18_H25P,     time7_H25Pa  = hourly25P(V2_18_Hg0[:],      time7a) # V2_18
Hg0_V3_18M_H25P,    time8_H25Pa  = hourly25P(V3_18M_Hg0[:],     time8a) # V3_18 (Mawson)
Hg0_V3_18D_H25P,    time9_H25Pa  = hourly25P(V3_18D_Hg0[:],     time9a) # V3_18 (Davis)
Hg0_V4_18_H25P,     time10_H25Pa = hourly25P(V4_18_Hg0[:],      time10a) # V4_18

Hg0_PCAN_H25P,      time11_H25Pa = hourly25P(PCAN_Hg0[:],       time11a) # PCAN
Hg0_SIPEXII_H25P,   time12_H25Pa = hourly25P(SIPEXII_Hg0[:],    time12a) # SIPEXII

# BrO
BrO_V1_17_H25P,   time1_HMz  = hourly25P(V1_17_BrO[:],   time1z) # V1_17
BrO_V2_17_H25P,   time2_HMz  = hourly25P(V2_17_BrO[:],   time2z) # V2_17
BrO_V3_17M_H25P,  time3_HMz  = hourly25P(V3_17M_BrO[:],  time3z) # V3_17 (Mawson)
BrO_V3_17D_H25P,  time4_HMz  = hourly25P(V3_17D_BrO[:],  time4z) # V3_17 (Davis)

BrO_V1_18_H25P,   time6_HMz  = hourly25P(V1_18_BrO[:],   time5z) # V1_18
BrO_V2_18_H25P,   time7_HMz  = hourly25P(V2_18_BrO[:],   time6z) # V2_18
BrO_V3_18M_H25P,  time8_HMz  = hourly25P(V3_18M_BrO[:],  time7z) # V3_18 (Mawson)
BrO_V3_18D_H25P,  time9_HMz  = hourly25P(V3_18D_BrO[:],  time8z) # V3_18 (Davis)

BrO_SIPEXII_Hv, time12_HMz = hourly25P(SIPEXII_BrO[:], time9z) # SIPEXII

#----------------------
# At Station
#----------------------
# Hg0
Hg0_Davis17_H25P1,  time1_H25Pb  = hourly25P(Hg0_Davis1_17[:],  time1b) # V1_17
Hg0_Casey17_H25P,   time2_H25Pb  = hourly25P(Hg0_Casey_17[:],   time2b) # V2_17
Hg0_Mawson17_H25P,  time3_H25Pb  = hourly25P(Hg0_Mawson_17[:],  time3b) # V3_17
Hg0_Davis17_H25P3,  time4_H25Pb  = hourly25P(Hg0_Davis3_17[:],  time4b) # V3_17
Hg0_MQIsl17_H25P,   time5_H25Pb  = hourly25P(Hg0_MQIsl_17[:],   time5b) # V4_17

Hg0_Davis18_H25P1,  time6_H25Pb  = hourly25P(Hg0_Davis1_18[:],  time6b) # V1_18
Hg0_Casey18_H25P,   time7_H25Pb  = hourly25P(Hg0_Casey_18[:],   time7b) # V2_18
Hg0_Mawson18_H25P,  time8_H25Pb  = hourly25P(Hg0_Mawson_18[:],  time8b) # V3_18
Hg0_Davis18_H25P3,  time9_H25Pb  = hourly25P(Hg0_Davis3_18[:],  time9b) # V3_18
Hg0_MQIsl18_H25P,   time10_H25Pb = hourly25P(Hg0_MQIsl_18[:],   time10b) # V4_18

Hg0_PCAN17_H25P,    time11_H25Pb = hourly25P(Hg0_PCAN_17[:],    time11b) # PCAN
Hg0_SIPEXII12_H25P, time12_H25Pb = hourly25P(Hg0_SIPEXII_12[:], time12b) # SIPEXII

# BrO
BrO_Davis17_H25P1,  time1_HMy  = hourly25P(BrO_Davis1_17[:],  time1y) # V1_17
BrO_Casey17_H25P,   time2_HMy  = hourly25P(BrO_Casey_17[:],  time2y) # V2_17
BrO_Mawson17_H25P,  time3_HMy  = hourly25P(BrO_Mawson_17[:], time3y) # V3_17 (Mawson)
BrO_Davis17_H25P3,  time4_HMy  = hourly25P(BrO_Davis3_17[:],  time4y) # V3_17 (Davis)

BrO_Davis18_H25P1,  time6_HMy  = hourly25P(BrO_Davis1_18[:],  time5y) # V1_18
BrO_Casey18_H25P,   time7_HMy  = hourly25P(BrO_Casey_18[:],  time6y) # V2_18
BrO_Mawson18_H25P,  time8_HMy  = hourly25P(BrO_Mawson_18[:], time7y) # V3_18 (Mawson)
BrO_Davis18_H25P3,  time9_HMy  = hourly25P(BrO_Davis3_18[:],  time8y) # V3_18 (Davis)

BrO_SIPEXII12_H25P, time12_HMy = hourly25P(BrO_SIPEXII_12[:],  time9y) # SIPEXII

# O3
O3_Davis17_H25P1,  time1_HMb  = hourly25P(O3_Davis1_17[:], time1b_O3) # V1_17
O3_Casey17_H25P,   time2_HMb  = hourly25P(O3_Casey_17[:],  time2b_O3) # V2_17
O3_Mawson17_H25P,  time3_HMb  = hourly25P(O3_Mawson_17[:], time3b_O3) # V3_17 (Mawson)
O3_Davis17_H25P3,  time4_HMb  = hourly25P(O3_Davis3_17[:], time4b_O3) # V3_17 (Davis)
O3_MQIsl17_H25P,   time5_HMb  = hourly25P(O3_MQIsl_17[:],  time5b_O3) # V4_17

O3_Davis18_H25P1,  time6_HMb  = hourly25P(O3_Davis1_18[:], time6b_O3) # V1_18
O3_Casey18_H25P,   time7_HMb  = hourly25P(O3_Casey_18[:],  time7b_O3) # V2_18
O3_Mawson18_H25P,  time8_HMb  = hourly25P(O3_Mawson_18[:], time8b_O3) # V3_18 (Mawson)
O3_Davis18_H25P3,  time9_HMb  = hourly25P(O3_Davis3_18[:], time9b_O3) # V3_18 (Davis)
O3_MQIsl18_H25P,   time10_HMb = hourly25P(O3_MQIsl_18[:],  time10b_O3) # V4_18

O3_PCAN17_H25P,    time11_HMb = hourly25P(O3_PCAN_17[:],   time11b_O3) # PCAN
O3_SIPEXII12_H25P, time12_HMb = hourly25P(O3_SIPEXII_12[:], time12b_O3) # SIPEXII

# RH
RH_Davis17_H25P1,    time1_HMb  = hourly25P(np.array(Met_Davis_V1_17['RH_Avg']),  time1b_Met) # V1_17
RH_Casey17_H25P,     time2_HMb  = hourly25P(np.array(Met_Casey_V2_17['RH_Avg']),  time2b_Met) # V2_17
RH_Mawson17_H25P,    time3_HMb  = hourly25P(np.array(Met_Mawson_V3_17['RH_Avg']), time3b_Met) # V3_17
RH_Davis17_H25P3,    time4_HMb  = hourly25P(np.array(Met_Davis_V3_17['RH_Avg']),  time4b_Met) # V3_17
RH_MQIsl17_H25P,     time5_HMb  = hourly25P(np.array(Met_MQIsl_V4_17['RH_Avg']),  time5b_Met) # V4_17

RH_Davis18_H25P1,    time6_HMb  = hourly25P(np.array(Met_Davis_V1_18['RH_Avg']),  time6b_Met) # V1_18
RH_Casey18_H25P,     time7_HMb  = hourly25P(np.array(Met_Casey_V2_18['RH_Avg']),  time7b_Met) # V2_18
RH_Mawson18_H25P,    time8_HMb  = hourly25P(np.array(Met_Mawson_V3_18['RH_Avg']), time8b_Met) # V3_18
RH_Davis18_H25P3,    time9_HMb  = hourly25P(np.array(Met_Davis_V3_18['RH_Avg']),  time9b_Met) # V3_18
RH_MQIsl18_H25P,     time10_HMb = hourly25P(np.array(Met_MQIsl_V4_18['RH_Avg']),  time10b_Met) # V4_18

RH_PCAN17_H25P,      time11_HMb = hourly25P(np.array(Met_PCAN_Ice['RH_Avg']),     time11b_Met) # PCAN
RH_SIPEXII12_H25P,   time12_HMb = hourly25P(np.array(Met_SIPEXII_Ice['RH_Avg']),  time12b_Met) # SIPEXII

# Temp
Temp_Davis17_H25P1,    time1_HMb  = hourly25P(np.array(Met_Davis_V1_17['Temp_Avg']),  time1b_Met) # V1_17
Temp_Casey17_H25P,     time2_HMb  = hourly25P(np.array(Met_Casey_V2_17['Temp_Avg']),  time2b_Met) # V2_17
Temp_Mawson17_H25P,    time3_HMb  = hourly25P(np.array(Met_Mawson_V3_17['Temp_Avg']), time3b_Met) # V3_17
Temp_Davis17_H25P3,    time4_HMb  = hourly25P(np.array(Met_Davis_V3_17['Temp_Avg']),  time4b_Met) # V3_17
Temp_MQIsl17_H25P,     time5_HMb  = hourly25P(np.array(Met_MQIsl_V4_17['Temp_Avg']),  time5b_Met) # V4_17

Temp_Davis18_H25P1,    time6_HMb  = hourly25P(np.array(Met_Davis_V1_18['Temp_Avg']),  time6b_Met) # V1_18
Temp_Casey18_H25P,     time7_HMb  = hourly25P(np.array(Met_Casey_V2_18['Temp_Avg']),  time7b_Met) # V2_18
Temp_Mawson18_H25P,    time8_HMb  = hourly25P(np.array(Met_Mawson_V3_18['Temp_Avg']), time8b_Met) # V3_18
Temp_Davis18_H25P3,    time9_HMb  = hourly25P(np.array(Met_Davis_V3_18['Temp_Avg']),  time9b_Met) # V3_18
Temp_MQIsl18_H25P,     time10_HMb = hourly25P(np.array(Met_MQIsl_V4_18['Temp_Avg']),  time10b_Met) # V4_18

Temp_PCAN17_H25P,      time11_HMb = hourly25P(np.array(Met_PCAN_Ice['Temp_Avg']),     time11b_Met) # PCAN
Temp_SIPEXII12_H25P,   time12_HMb = hourly25P(np.array(Met_SIPEXII_Ice['Temp_Avg']),  time12b_Met) # SIPEXII

# SolRad
SR_Davis17_H25P1,    time1_HMb  = hourly25P(np.array(Met_Davis_V1_17['SolRad_Avg']),  time1b_Met) # V1_17
SR_Casey17_H25P,     time2_HMb  = hourly25P(np.array(Met_Casey_V2_17['SolRad_Avg']),  time2b_Met) # V2_17
SR_Mawson17_H25P,    time3_HMb  = hourly25P(np.array(Met_Mawson_V3_17['SolRad_Avg']), time3b_Met) # V3_17
SR_Davis17_H25P3,    time4_HMb  = hourly25P(np.array(Met_Davis_V3_17['SolRad_Avg']),  time4b_Met) # V3_17
SR_MQIsl17_H25P,     time5_HMb  = hourly25P(np.array(Met_MQIsl_V4_17['SolRad_Avg']),  time5b_Met) # V4_17

SR_Davis18_H25P1,    time6_HMb  = hourly25P(np.array(Met_Davis_V1_18['SolRad_Avg']),  time6b_Met) # V1_18
SR_Casey18_H25P,     time7_HMb  = hourly25P(np.array(Met_Casey_V2_18['SolRad_Avg']),  time7b_Met) # V2_18
SR_Mawson18_H25P,    time8_HMb  = hourly25P(np.array(Met_Mawson_V3_18['SolRad_Avg']), time8b_Met) # V3_18
SR_Davis18_H25P3,    time9_HMb  = hourly25P(np.array(Met_Davis_V3_18['SolRad_Avg']),  time9b_Met) # V3_18
SR_MQIsl18_H25P,     time10_HMb = hourly25P(np.array(Met_MQIsl_V4_18['SolRad_Avg']),  time10b_Met) # V4_18

SR_PCAN17_H25P,      time11_HMb = hourly25P(np.array(Met_PCAN_Ice['SolRad_Avg']),     time11b_Met) # PCAN
SR_SIPEXII12_H25P,   time12_HMb = hourly25P(np.array(Met_SIPEXII_Ice['SolRad_Avg']),  time12b_Met) # SIPEXII

# Wind Speed
WS_Davis17_H25P1,    time1_HMb  = hourly25P(np.array(Met_Davis_V1_17['WS_Avg']),  time1b_Met) # V1_17
WS_Casey17_H25P,     time2_HMb  = hourly25P(np.array(Met_Casey_V2_17['WS_Avg']),  time2b_Met) # V2_17
WS_Mawson17_H25P,    time3_HMb  = hourly25P(np.array(Met_Mawson_V3_17['WS_Avg']), time3b_Met) # V3_17
WS_Davis17_H25P3,    time4_HMb  = hourly25P(np.array(Met_Davis_V3_17['WS_Avg']),  time4b_Met) # V3_17
WS_MQIsl17_H25P,     time5_HMb  = hourly25P(np.array(Met_MQIsl_V4_17['WS_Avg']),  time5b_Met) # V4_17

WS_Davis18_H25P1,    time6_HMb  = hourly25P(np.array(Met_Davis_V1_18['WS_Avg']),  time6b_Met) # V1_18
WS_Casey18_H25P,     time7_HMb  = hourly25P(np.array(Met_Casey_V2_18['WS_Avg']),  time7b_Met) # V2_18
WS_Mawson18_H25P,    time8_HMb  = hourly25P(np.array(Met_Mawson_V3_18['WS_Avg']), time8b_Met) # V3_18
WS_Davis18_H25P3,    time9_HMb  = hourly25P(np.array(Met_Davis_V3_18['WS_Avg']),  time9b_Met) # V3_18
WS_MQIsl18_H25P,     time10_HMb = hourly25P(np.array(Met_MQIsl_V4_18['WS_Avg']),  time10b_Met) # V4_18

WS_PCAN17_H25P,      time11_HMb = hourly25P(np.array(Met_PCAN_Ice['WS_Avg']),     time11b_Met) # PCAN
WS_SIPEXII12_H25P,   time12_HMb = hourly25P(np.array(Met_SIPEXII_Ice['WS_Avg']),  time12b_Met) # SIPEXII

#----------------------
# Sea Ice
#----------------------
Hg0_Ice_V1_17_H25P, time1_H5Pc  = hourly25P(Hg0_Ice1_V1_17[:], time1c) # V1_17
Hg0_Ice_V2_17_H25P, time2_H5Pc  = hourly25P(Hg0_Ice1_V2_17[:], time2c) # V2_17
Hg0_Ice_V3_17_H25P, time3_H5Pc  = hourly25P(Hg0_Ice1_V3_17[:], time3c) # V3_17

Hg0_Ice_V1_18_H25P, time4_H5Pc  = hourly25P(Hg0_Ice1_V1_18[:], time4c) # V1_18
Hg0_Ice_V2_18_H25P, time5_H5Pc  = hourly25P(Hg0_Ice1_V2_18[:], time5c) # V2_18
Hg0_Ice_V3_18_H25P, time6_H5Pc  = hourly25P(Hg0_Ice1_V3_18[:], time6c) # V3_18

#----------------------
# Open Water
#----------------------
Hg0_OW_V1_17_H25P,  time1_H25Pd = hourly25P(Hg0_OW1_V1_17[:], time1d) # V1_17
Hg0_OW_V2_17_H25P,  time2_H25Pd = hourly25P(Hg0_OW1_V2_17[:], time2d) # V2_17
Hg0_OW_V3_17_H25P,  time3_H25Pd = hourly25P(Hg0_OW1_V3_17[:], time3d) # V3_17

Hg0_OW_V1_18_H25P,  time4_H25Pd = hourly25P(Hg0_OW1_V1_18[:], time4d) # V1_18
Hg0_OW_V2_18_H25P,  time5_H25Pd = hourly25P(Hg0_OW1_V2_18[:], time5d) # V2_18
Hg0_OW_V3_18_H25P,  time6_H25Pd = hourly25P(Hg0_OW1_V3_18[:], time6d) # V3_18

#------------------------------------------------------------------------------
# Append the first value to complete the diurnal cycle
# Hg0
Hg0_Davis17_H25P1  = np.append(Hg0_Davis17_H25P1,  Hg0_Davis17_H25P1[0])
Hg0_Casey17_H25P   = np.append(Hg0_Casey17_H25P,   Hg0_Casey17_H25P[0])
Hg0_Mawson17_H25P  = np.append(Hg0_Mawson17_H25P,  Hg0_Mawson17_H25P[0])
Hg0_Davis17_H25P3  = np.append(Hg0_Davis17_H25P3,  Hg0_Davis17_H25P3[0])
Hg0_MQIsl17_H25P   = np.append(Hg0_MQIsl17_H25P,   Hg0_MQIsl17_H25P[0])

Hg0_Davis18_H25P1  = np.append(Hg0_Davis18_H25P1,  Hg0_Davis18_H25P1[0])
Hg0_Casey18_H25P   = np.append(Hg0_Casey18_H25P,   Hg0_Casey18_H25P[0])
Hg0_Mawson18_H25P  = np.append(Hg0_Mawson18_H25P,  Hg0_Mawson18_H25P[0])
Hg0_Davis18_H25P3  = np.append(Hg0_Davis18_H25P3,  Hg0_Davis18_H25P3[0])
Hg0_MQIsl18_H25P   = np.append(Hg0_MQIsl18_H25P,   Hg0_MQIsl18_H25P[0])

Hg0_PCAN17_H25P    = np.append(Hg0_PCAN17_H25P,    Hg0_PCAN17_H25P[0])
Hg0_SIPEXII12_H25P = np.append(Hg0_SIPEXII12_H25P, Hg0_SIPEXII12_H25P[0])

# BrO
# BrO_Davis17_H25P1  = np.append(BrO_Davis17_H25P1,  BrO_Davis17_H25P1[23])
# BrO_Casey17_H25P   = np.append(BrO_Casey17_H25P,   BrO_Casey17_H25P[23])
# BrO_Mawson17_H25P  = np.append(BrO_Mawson17_H25P,  BrO_Mawson17_H25P[23])
# BrO_Davis17_H25P3  = np.append(BrO_Davis17_H25P3,  BrO_Davis17_H25P3[23])

# BrO_Davis18_H25P1  = np.append(BrO_Davis18_H25P1,  BrO_Davis18_H25P1[23])
# BrO_Casey18_H25P   = np.append(BrO_Casey18_H25P,   BrO_Casey18_H25P[23])
# BrO_Mawson18_H25P  = np.append(BrO_Mawson18_H25P,  BrO_Mawson18_H25P[23])
# BrO_Davis18_H25P3  = np.append(BrO_Davis18_H25P3,  BrO_Davis18_H25P3[23])

# BrO_SIPEXII12_H25P = np.append(BrO_SIPEXII12_H25P, BrO_SIPEXII12_H25P[23])

# O3
O3_Davis17_H25P1  = np.append(O3_Davis17_H25P1,  O3_Davis17_H25P1[0])
O3_Casey17_H25P   = np.append(O3_Casey17_H25P,   O3_Casey17_H25P[0])
O3_Mawson17_H25P  = np.append(O3_Mawson17_H25P,  O3_Mawson17_H25P[0])
O3_Davis17_H25P3  = np.append(O3_Davis17_H25P3,  O3_Davis17_H25P3[0])
O3_MQIsl17_H25P   = np.append(O3_MQIsl17_H25P,   O3_MQIsl17_H25P[0])

O3_Davis18_H25P1  = np.append(O3_Davis18_H25P1,  O3_Davis18_H25P1[0])
O3_Casey18_H25P   = np.append(O3_Casey18_H25P,   O3_Casey18_H25P[0])
O3_Mawson18_H25P  = np.append(O3_Mawson18_H25P,  O3_Mawson18_H25P[0])
O3_Davis18_H25P3  = np.append(O3_Davis18_H25P3,  O3_Davis18_H25P3[0])
O3_MQIsl18_H25P   = np.append(O3_MQIsl18_H25P,   O3_MQIsl18_H25P[0])

O3_PCAN17_H25P    = np.append(O3_PCAN17_H25P,    O3_PCAN17_H25P[0])
O3_SIPEXII12_H25P = np.append(O3_SIPEXII12_H25P, O3_SIPEXII12_H25P[0])

# RH
RH_Davis17_H25P1  = np.append(RH_Davis17_H25P1,  RH_Davis17_H25P1[0])
RH_Casey17_H25P   = np.append(RH_Casey17_H25P,   RH_Casey17_H25P[0])
RH_Mawson17_H25P  = np.append(RH_Mawson17_H25P,  RH_Mawson17_H25P[0])
RH_Davis17_H25P3  = np.append(RH_Davis17_H25P3,  RH_Davis17_H25P3[0])
RH_MQIsl17_H25P   = np.append(RH_MQIsl17_H25P,   RH_MQIsl17_H25P[0])

RH_Davis18_H25P1  = np.append(RH_Davis18_H25P1,  RH_Davis18_H25P1[0])
RH_Casey18_H25P   = np.append(RH_Casey18_H25P,   RH_Casey18_H25P[0])
RH_Mawson18_H25P  = np.append(RH_Mawson18_H25P,  RH_Mawson18_H25P[0])
RH_Davis18_H25P3  = np.append(RH_Davis18_H25P3,  RH_Davis18_H25P3[0])
RH_MQIsl18_H25P   = np.append(RH_MQIsl18_H25P,   RH_MQIsl18_H25P[0])

RH_PCAN17_H25P    = np.append(RH_PCAN17_H25P,    RH_PCAN17_H25P[0])
RH_SIPEXII12_H25P = np.append(RH_SIPEXII12_H25P, RH_SIPEXII12_H25P[0])

# Temp
Temp_Davis17_H25P1  = np.append(Temp_Davis17_H25P1,  Temp_Davis17_H25P1[0])
Temp_Casey17_H25P   = np.append(Temp_Casey17_H25P,   Temp_Casey17_H25P[0])
Temp_Mawson17_H25P  = np.append(Temp_Mawson17_H25P,  Temp_Mawson17_H25P[0])
Temp_Davis17_H25P3  = np.append(Temp_Davis17_H25P3,  Temp_Davis17_H25P3[0])
Temp_MQIsl17_H25P   = np.append(Temp_MQIsl17_H25P,   Temp_MQIsl17_H25P[0])

Temp_Davis18_H25P1  = np.append(Temp_Davis18_H25P1,  Temp_Davis18_H25P1[0])
Temp_Casey18_H25P   = np.append(Temp_Casey18_H25P,   Temp_Casey18_H25P[0])
Temp_Mawson18_H25P  = np.append(Temp_Mawson18_H25P,  Temp_Mawson18_H25P[0])
Temp_Davis18_H25P3  = np.append(Temp_Davis18_H25P3,  Temp_Davis18_H25P3[0])
Temp_MQIsl18_H25P   = np.append(Temp_MQIsl18_H25P,   Temp_MQIsl18_H25P[0])

Temp_PCAN17_H25P    = np.append(Temp_PCAN17_H25P,    Temp_PCAN17_H25P[0])
Temp_SIPEXII12_H25P = np.append(Temp_SIPEXII12_H25P, Temp_SIPEXII12_H25P[0])

# SolRad
SR_Davis17_H25P1  = np.append(SR_Davis17_H25P1,  SR_Davis17_H25P1[0])
SR_Casey17_H25P   = np.append(SR_Casey17_H25P,   SR_Casey17_H25P[0])
SR_Mawson17_H25P  = np.append(SR_Mawson17_H25P,  SR_Mawson17_H25P[0])
SR_Davis17_H25P3  = np.append(SR_Davis17_H25P3,  SR_Davis17_H25P3[0])
SR_MQIsl17_H25P   = np.append(SR_MQIsl17_H25P,   SR_MQIsl17_H25P[0])

SR_Davis18_H25P1  = np.append(SR_Davis18_H25P1,  SR_Davis18_H25P1[0])
SR_Casey18_H25P   = np.append(SR_Casey18_H25P,   SR_Casey18_H25P[0])
SR_Mawson18_H25P  = np.append(SR_Mawson18_H25P,  SR_Mawson18_H25P[0])
SR_Davis18_H25P3  = np.append(SR_Davis18_H25P3,  SR_Davis18_H25P3[0])
SR_MQIsl18_H25P   = np.append(SR_MQIsl18_H25P,   SR_MQIsl18_H25P[0])

SR_PCAN17_H25P    = np.append(SR_PCAN17_H25P,    SR_PCAN17_H25P[0])
SR_SIPEXII12_H25P = np.append(SR_SIPEXII12_H25P, SR_SIPEXII12_H25P[0])

# Wind Speed
WS_Davis17_H25P1  = np.append(WS_Davis17_H25P1,  WS_Davis17_H25P1[0])
WS_Casey17_H25P   = np.append(WS_Casey17_H25P,   WS_Casey17_H25P[0])
WS_Mawson17_H25P = np.append(WS_Mawson17_H25P,  WS_Mawson17_H25P[0])
WS_Davis17_H25P3  = np.append(WS_Davis17_H25P3,  WS_Davis17_H25P3[0])
WS_MQIsl17_H25P   = np.append(WS_MQIsl17_H25P,   WS_MQIsl17_H25P[0])

WS_Davis18_H25P1  = np.append(WS_Davis18_H25P1,  WS_Davis18_H25P1[0])
WS_Casey18_H25P   = np.append(WS_Casey18_H25P,   WS_Casey18_H25P[0])
WS_Mawson18_H25P  = np.append(WS_Mawson18_H25P,  WS_Mawson18_H25P[0])
WS_Davis18_H25P3  = np.append(WS_Davis18_H25P3,  WS_Davis18_H25P3[0])
WS_MQIsl18_H25P   = np.append(WS_MQIsl18_H25P,   WS_MQIsl18_H25P[0])

WS_PCAN17_H25P    = np.append(WS_PCAN17_H25P,    WS_PCAN17_H25P[0])
WS_SIPEXII12_H25P = np.append(WS_SIPEXII12_H25P, WS_SIPEXII12_H25P[0])

# Sea Ice
Hg0_Ice_V1_17_H25P = np.append(Hg0_Ice_V1_17_H25P, Hg0_Ice_V1_17_H25P[0])
Hg0_Ice_V2_17_H25P = np.append(Hg0_Ice_V2_17_H25P, Hg0_Ice_V2_17_H25P[0])
Hg0_Ice_V3_17_H25P = np.append(Hg0_Ice_V3_17_H25P, Hg0_Ice_V3_17_H25P[0])

Hg0_Ice_V1_18_H25P = np.append(Hg0_Ice_V1_18_H25P, Hg0_Ice_V1_18_H25P[0])
Hg0_Ice_V2_18_H25P = np.append(Hg0_Ice_V2_18_H25P, Hg0_Ice_V2_18_H25P[0])
Hg0_Ice_V3_18_H25P = np.append(Hg0_Ice_V3_18_H25P, Hg0_Ice_V3_18_H25P[0])

# Sea Ice
Hg0_OW_V1_17_H25P  = np.append(Hg0_OW_V1_17_H25P,  Hg0_OW_V1_17_H25P[0])
Hg0_OW_V2_17_H25P  = np.append(Hg0_OW_V2_17_H25P,  Hg0_OW_V2_17_H25P[0])
Hg0_OW_V3_17_H25P  = np.append(Hg0_OW_V3_17_H25P,  Hg0_OW_V3_17_H25P[0])

Hg0_OW_V1_18_H25P  = np.append(Hg0_OW_V1_18_H25P,  Hg0_OW_V1_18_H25P[0])
Hg0_OW_V2_18_H25P  = np.append(Hg0_OW_V2_18_H25P,  Hg0_OW_V2_18_H25P[0])
Hg0_OW_V3_18_H25P  = np.append(Hg0_OW_V3_18_H25P,  Hg0_OW_V3_18_H25P[0])

#------------------------------------------------------------------------------
# CALCULATE THE 75th PERCENTILE FOR THE Hg0 DAILY AVERAGE (MEAN)

# Function to calculate the standard deviation
def hourly75P(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').quantile(q=0.75)
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

#----------------------
# Whole Voyage
#----------------------
# Hg0
Hg0_V1_17_H75P,     time1_H75Pa  = hourly75P(V1_17_Hg0[:],      time1a) # V1_17
Hg0_V2_17_H75P,     time2_H75Pa  = hourly75P(V2_17_Hg0[:],      time2a) # V2_17
Hg0_V3_17M_H75P,    time3_H75Pa  = hourly75P(V3_17M_Hg0[:],     time3a) # V3_17 (Mawson)
Hg0_V3_17D_H75P,    time4_H75Pa  = hourly75P(V3_17D_Hg0[:],     time4a) # V3_17 (Davis)
Hg0_V4_17_H75P,     time5_H75Pa  = hourly75P(V4_17_Hg0[:],      time5a) # V4_17

Hg0_V1_18_H75P,     time6_H75Pa  = hourly75P(V1_18_Hg0[:],      time6a) # V1_18
Hg0_V2_18_H75P,     time7_H75Pa  = hourly75P(V2_18_Hg0[:],      time7a) # V2_18
Hg0_V3_18M_H75P,    time8_H75Pa  = hourly75P(V3_18M_Hg0[:],     time8a) # V3_18 (Mawson)
Hg0_V3_18D_H75P,    time9_H75Pa  = hourly75P(V3_18D_Hg0[:],     time9a) # V3_18 (Davis)
Hg0_V4_18_H75P,     time10_H75Pa = hourly75P(V4_18_Hg0[:],      time10a) # V4_18

Hg0_PCAN_H75P,      time11_H75Pa = hourly75P(PCAN_Hg0[:],       time11a) # PCAN
Hg0_SIPEXII_H75P,   time12_H75Pa = hourly75P(SIPEXII_Hg0[:],    time12a) # SIPEXII

# BrO
BrO_V1_17_H75P,   time1_HMz  = hourly75P(V1_17_BrO[:],   time1z) # V1_17
BrO_V2_17_H75P,   time2_HMz  = hourly75P(V2_17_BrO[:],   time2z) # V2_17
BrO_V3_17M_H75P,  time3_HMz  = hourly75P(V3_17M_BrO[:],  time3z) # V3_17 (Mawson)
BrO_V3_17D_H75P,  time4_HMz  = hourly75P(V3_17D_BrO[:],  time4z) # V3_17 (Davis)

BrO_V1_18_H75P,   time6_HMz  = hourly75P(V1_18_BrO[:],   time5z) # V1_18
BrO_V2_18_H75P,   time7_HMz  = hourly75P(V2_18_BrO[:],   time6z) # V2_18
BrO_V3_18M_H75P,  time8_HMz  = hourly75P(V3_18M_BrO[:],  time7z) # V3_18 (Mawson)
BrO_V3_18D_H75P,  time9_HMz  = hourly75P(V3_18D_BrO[:],  time8z) # V3_18 (Davis)

BrO_SIPEXII_H75P, time12_HMz = hourly75P(SIPEXII_BrO[:], time9z) # SIPEXII

#----------------------
# At Station
#----------------------
# Hg0
Hg0_Davis17_H75P1,  time1_H75Pb  = hourly75P(Hg0_Davis1_17[:],  time1b) # V1_17
Hg0_Casey17_H75P,   time2_H75Pb  = hourly75P(Hg0_Casey_17[:],   time2b) # V2_17
Hg0_Mawson17_H75P,  time3_H75Pb  = hourly75P(Hg0_Mawson_17[:],  time3b) # V3_17
Hg0_Davis17_H75P3,  time4_H75Pb  = hourly75P(Hg0_Davis3_17[:],  time4b) # V3_17
Hg0_MQIsl17_H75P,   time5_H75Pb  = hourly75P(Hg0_MQIsl_17[:],   time5b) # V4_17

Hg0_Davis18_H75P1,  time6_H75Pb  = hourly75P(Hg0_Davis1_18[:],  time6b) # V1_18
Hg0_Casey18_H75P,   time7_H75Pb  = hourly75P(Hg0_Casey_18[:],   time7b) # V2_18
Hg0_Mawson18_H75P,  time8_H75Pb  = hourly75P(Hg0_Mawson_18[:],  time8b) # V3_18
Hg0_Davis18_H75P3,  time9_H75Pb  = hourly75P(Hg0_Davis3_18[:],  time9b) # V3_18
Hg0_MQIsl18_H75P,   time10_H75Pb = hourly75P(Hg0_MQIsl_18[:],   time10b) # V4_18

Hg0_PCAN17_H75P,    time11_H75Pb = hourly75P(Hg0_PCAN_17[:],    time11b) # PCAN
Hg0_SIPEXII12_H75P, time12_H75Pb = hourly75P(Hg0_SIPEXII_12[:], time12b) # SIPEXII

# BrO
BrO_Davis17_H75P1,  time1_HMy  = hourly75P(BrO_Davis1_17[:],  time1y) # V1_17
BrO_Casey17_H75P,   time2_HMy  = hourly75P(BrO_Casey_17[:],  time2y) # V2_17
BrO_Mawson17_H75P,  time3_HMy  = hourly75P(BrO_Mawson_17[:], time3y) # V3_17 (Mawson)
BrO_Davis17_H75P3,  time4_HMy  = hourly75P(BrO_Davis3_17[:],  time4y) # V3_17 (Davis)

BrO_Davis18_H75P1,  time6_HMy  = hourly75P(BrO_Davis1_18[:],  time5y) # V1_18
BrO_Casey18_H75P,   time7_HMy  = hourly75P(BrO_Casey_18[:],  time6y) # V2_18
BrO_Mawson18_H75P,  time8_HMy  = hourly75P(BrO_Mawson_18[:], time7y) # V3_18 (Mawson)
BrO_Davis18_H75P3,  time9_HMy  = hourly75P(BrO_Davis3_18[:],  time8y) # V3_18 (Davis)

BrO_SIPEXII12_H75P, time12_HMy = hourly75P(BrO_SIPEXII_12[:],  time9y) # SIPEXII

# O3
O3_Davis17_H75P1,  time1_HMb  = hourly75P(O3_Davis1_17[:], time1b_O3) # V1_17
O3_Casey17_H75P,   time2_HMb  = hourly75P(O3_Casey_17[:],  time2b_O3) # V2_17
O3_Mawson17_H75P,  time3_HMb  = hourly75P(O3_Mawson_17[:], time3b_O3) # V3_17 (Mawson)
O3_Davis17_H75P3,  time4_HMb  = hourly75P(O3_Davis3_17[:], time4b_O3) # V3_17 (Davis)
O3_MQIsl17_H75P,   time5_HMb  = hourly75P(O3_MQIsl_17[:],  time5b_O3) # V4_17

O3_Davis18_H75P1,  time6_HMb  = hourly75P(O3_Davis1_18[:], time6b_O3) # V1_18
O3_Casey18_H75P,   time7_HMb  = hourly75P(O3_Casey_18[:],  time7b_O3) # V2_18
O3_Mawson18_H75P,  time8_HMb  = hourly75P(O3_Mawson_18[:], time8b_O3) # V3_18 (Mawson)
O3_Davis18_H75P3,  time9_HMb  = hourly75P(O3_Davis3_18[:], time9b_O3) # V3_18 (Davis)
O3_MQIsl18_H75P,   time10_HMb = hourly75P(O3_MQIsl_18[:],  time10b_O3) # V4_18

O3_PCAN17_H75P,    time11_HMb = hourly75P(O3_PCAN_17[:],   time11b_O3) # PCAN
O3_SIPEXII12_H75P, time12_HMb = hourly75P(O3_SIPEXII_12[:], time12b_O3) # SIPEXII

# RH
RH_Davis17_H75P1,    time1_HMb  = hourly75P(np.array(Met_Davis_V1_17['RH_Avg']),  time1b_Met) # V1_17
RH_Casey17_H75P,     time2_HMb  = hourly75P(np.array(Met_Casey_V2_17['RH_Avg']),  time2b_Met) # V2_17
RH_Mawson17_H75P,    time3_HMb  = hourly75P(np.array(Met_Mawson_V3_17['RH_Avg']), time3b_Met) # V3_17
RH_Davis17_H75P3,    time4_HMb  = hourly75P(np.array(Met_Davis_V3_17['RH_Avg']),  time4b_Met) # V3_17
RH_MQIsl17_H75P,     time5_HMb  = hourly75P(np.array(Met_MQIsl_V4_17['RH_Avg']),  time5b_Met) # V4_17

RH_Davis18_H75P1,    time6_HMb  = hourly75P(np.array(Met_Davis_V1_18['RH_Avg']),  time6b_Met) # V1_18
RH_Casey18_H75P,     time7_HMb  = hourly75P(np.array(Met_Casey_V2_18['RH_Avg']),  time7b_Met) # V2_18
RH_Mawson18_H75P,    time8_HMb  = hourly75P(np.array(Met_Mawson_V3_18['RH_Avg']), time8b_Met) # V3_18
RH_Davis18_H75P3,    time9_HMb  = hourly75P(np.array(Met_Davis_V3_18['RH_Avg']),  time9b_Met) # V3_18
RH_MQIsl18_H75P,     time10_HMb = hourly75P(np.array(Met_MQIsl_V4_18['RH_Avg']),  time10b_Met) # V4_18

RH_PCAN17_H75P,      time11_HMb = hourly75P(np.array(Met_PCAN_Ice['RH_Avg']),     time11b_Met) # PCAN
RH_SIPEXII12_H75P,   time12_HMb = hourly75P(np.array(Met_SIPEXII_Ice['RH_Avg']),  time12b_Met) # SIPEXII

# Temp
Temp_Davis17_H75P1,    time1_HMb  = hourly75P(np.array(Met_Davis_V1_17['Temp_Avg']),  time1b_Met) # V1_17
Temp_Casey17_H75P,     time2_HMb  = hourly75P(np.array(Met_Casey_V2_17['Temp_Avg']),  time2b_Met) # V2_17
Temp_Mawson17_H75P,    time3_HMb  = hourly75P(np.array(Met_Mawson_V3_17['Temp_Avg']), time3b_Met) # V3_17
Temp_Davis17_H75P3,    time4_HMb  = hourly75P(np.array(Met_Davis_V3_17['Temp_Avg']),  time4b_Met) # V3_17
Temp_MQIsl17_H75P,     time5_HMb  = hourly75P(np.array(Met_MQIsl_V4_17['Temp_Avg']),  time5b_Met) # V4_17

Temp_Davis18_H75P1,    time6_HMb  = hourly75P(np.array(Met_Davis_V1_18['Temp_Avg']),  time6b_Met) # V1_18
Temp_Casey18_H75P,     time7_HMb  = hourly75P(np.array(Met_Casey_V2_18['Temp_Avg']),  time7b_Met) # V2_18
Temp_Mawson18_H75P,    time8_HMb  = hourly75P(np.array(Met_Mawson_V3_18['Temp_Avg']), time8b_Met) # V3_18
Temp_Davis18_H75P3,    time9_HMb  = hourly75P(np.array(Met_Davis_V3_18['Temp_Avg']),  time9b_Met) # V3_18
Temp_MQIsl18_H75P,     time10_HMb = hourly75P(np.array(Met_MQIsl_V4_18['Temp_Avg']),  time10b_Met) # V4_18

Temp_PCAN17_H75P,      time11_HMb = hourly75P(np.array(Met_PCAN_Ice['Temp_Avg']),     time11b_Met) # PCAN
Temp_SIPEXII12_H75P,   time12_HMb = hourly75P(np.array(Met_SIPEXII_Ice['Temp_Avg']),  time12b_Met) # SIPEXII

# SolRad
SR_Davis17_H75P1,    time1_HMb  = hourly75P(np.array(Met_Davis_V1_17['SolRad_Avg']),  time1b_Met) # V1_17
SR_Casey17_H75P,     time2_HMb  = hourly75P(np.array(Met_Casey_V2_17['SolRad_Avg']),  time2b_Met) # V2_17
SR_Mawson17_H75P,    time3_HMb  = hourly75P(np.array(Met_Mawson_V3_17['SolRad_Avg']), time3b_Met) # V3_17
SR_Davis17_H75P3,    time4_HMb  = hourly75P(np.array(Met_Davis_V3_17['SolRad_Avg']),  time4b_Met) # V3_17
SR_MQIsl17_H75P,     time5_HMb  = hourly75P(np.array(Met_MQIsl_V4_17['SolRad_Avg']),  time5b_Met) # V4_17

SR_Davis18_H75P1,    time6_HMb  = hourly75P(np.array(Met_Davis_V1_18['SolRad_Avg']),  time6b_Met) # V1_18
SR_Casey18_H75P,     time7_HMb  = hourly75P(np.array(Met_Casey_V2_18['SolRad_Avg']),  time7b_Met) # V2_18
SR_Mawson18_H75P,    time8_HMb  = hourly75P(np.array(Met_Mawson_V3_18['SolRad_Avg']), time8b_Met) # V3_18
SR_Davis18_H75P3,    time9_HMb  = hourly75P(np.array(Met_Davis_V3_18['SolRad_Avg']),  time9b_Met) # V3_18
SR_MQIsl18_H75P,     time10_HMb = hourly75P(np.array(Met_MQIsl_V4_18['SolRad_Avg']),  time10b_Met) # V4_18

SR_PCAN17_H75P,      time11_HMb = hourly75P(np.array(Met_PCAN_Ice['SolRad_Avg']),     time11b_Met) # PCAN
SR_SIPEXII12_H75P,   time12_HMb = hourly75P(np.array(Met_SIPEXII_Ice['SolRad_Avg']),  time12b_Met) # SIPEXII

# Wind Speed
WS_Davis17_H75P1,    time1_HMb  = hourly75P(np.array(Met_Davis_V1_17['WS_Avg']),  time1b_Met) # V1_17
WS_Casey17_H75P,     time2_HMb  = hourly75P(np.array(Met_Casey_V2_17['WS_Avg']),  time2b_Met) # V2_17
WS_Mawson17_H75P,    time3_HMb  = hourly75P(np.array(Met_Mawson_V3_17['WS_Avg']), time3b_Met) # V3_17
WS_Davis17_H75P3,    time4_HMb  = hourly75P(np.array(Met_Davis_V3_17['WS_Avg']),  time4b_Met) # V3_17
WS_MQIsl17_H75P,     time5_HMb  = hourly75P(np.array(Met_MQIsl_V4_17['WS_Avg']),  time5b_Met) # V4_17

WS_Davis18_H75P1,    time6_HMb  = hourly75P(np.array(Met_Davis_V1_18['WS_Avg']),  time6b_Met) # V1_18
WS_Casey18_H75P,     time7_HMb  = hourly75P(np.array(Met_Casey_V2_18['WS_Avg']),  time7b_Met) # V2_18
WS_Mawson18_H75P,    time8_HMb  = hourly75P(np.array(Met_Mawson_V3_18['WS_Avg']), time8b_Met) # V3_18
WS_Davis18_H75P3,    time9_HMb  = hourly75P(np.array(Met_Davis_V3_18['WS_Avg']),  time9b_Met) # V3_18
WS_MQIsl18_H75P,     time10_HMb = hourly75P(np.array(Met_MQIsl_V4_18['WS_Avg']),  time10b_Met) # V4_18

WS_PCAN17_H75P,      time11_HMb = hourly75P(np.array(Met_PCAN_Ice['WS_Avg']),     time11b_Met) # PCAN
WS_SIPEXII12_H75P,   time12_HMb = hourly75P(np.array(Met_SIPEXII_Ice['WS_Avg']),  time12b_Met) # SIPEXII

#----------------------
# Sea Ice
#----------------------
Hg0_Ice_V1_17_H75P, time1_H75Pc  = hourly75P(Hg0_Ice1_V1_17[:], time1c) # V1_17
Hg0_Ice_V2_17_H75P, time2_H75Pc  = hourly75P(Hg0_Ice1_V2_17[:], time2c) # V2_17
Hg0_Ice_V3_17_H75P, time3_H75Pc  = hourly75P(Hg0_Ice1_V3_17[:], time3c) # V3_17

Hg0_Ice_V1_18_H75P, time4_H75Pc  = hourly75P(Hg0_Ice1_V1_18[:], time4c) # V1_18
Hg0_Ice_V2_18_H75P, time5_H75Pc  = hourly75P(Hg0_Ice1_V2_18[:], time5c) # V2_18
Hg0_Ice_V3_18_H75P, time6_H75Pc  = hourly75P(Hg0_Ice1_V3_18[:], time6c) # V3_18

#----------------------
# Open Water
#----------------------
Hg0_OW_V1_17_H75P,  time1_H75Pd  = hourly75P(Hg0_OW1_V1_17[:], time1d) # V1_17
Hg0_OW_V2_17_H75P,  time2_H75Pd  = hourly75P(Hg0_OW1_V2_17[:], time2d) # V2_17
Hg0_OW_V3_17_H75P,  time3_H75Pd  = hourly75P(Hg0_OW1_V3_17[:], time3d) # V3_17

Hg0_OW_V1_18_H75P,  time4_H75Pd  = hourly75P(Hg0_OW1_V1_18[:], time4d) # V1_18
Hg0_OW_V2_18_H75P,  time5_H75Pd  = hourly75P(Hg0_OW1_V2_18[:], time5d) # V2_18
Hg0_OW_V3_18_H75P,  time6_H75Pd  = hourly75P(Hg0_OW1_V3_18[:], time6d) # V3_18

#------------------------------------------------------------------------------
# Append the first value to complete the diurnal cycle
# Hg0
Hg0_Davis17_H75P1  = np.append(Hg0_Davis17_H75P1,  Hg0_Davis17_H75P1[0])
Hg0_Casey17_H75P   = np.append(Hg0_Casey17_H75P,   Hg0_Casey17_H75P[0])
Hg0_Mawson17_H75P  = np.append(Hg0_Mawson17_H75P,  Hg0_Mawson17_H75P[0])
Hg0_Davis17_H75P3  = np.append(Hg0_Davis17_H75P3,  Hg0_Davis17_H75P3[0])
Hg0_MQIsl17_H75P   = np.append(Hg0_MQIsl17_H75P,   Hg0_MQIsl17_H75P[0])

Hg0_Davis18_H75P1  = np.append(Hg0_Davis18_H75P1,  Hg0_Davis18_H75P1[0])
Hg0_Casey18_H75P   = np.append(Hg0_Casey18_H75P,   Hg0_Casey18_H75P[0])
Hg0_Mawson18_H75P  = np.append(Hg0_Mawson18_H75P,  Hg0_Mawson18_H75P[0])
Hg0_Davis18_H75P3  = np.append(Hg0_Davis18_H75P3,  Hg0_Davis18_H75P3[0])
Hg0_MQIsl18_H75P   = np.append(Hg0_MQIsl18_H75P,   Hg0_MQIsl18_H75P[0])

Hg0_PCAN17_H75P    = np.append(Hg0_PCAN17_H75P,    Hg0_PCAN17_H75P[0])
Hg0_SIPEXII12_H75P = np.append(Hg0_SIPEXII12_H75P, Hg0_SIPEXII12_H75P[0])

# BrO
# BrO_Davis17_HM1  = np.append(BrO_Davis17_HM1,  BrO_Davis17_HM1[23])
# BrO_Casey17_HM   = np.append(BrO_Casey17_HM,   BrO_Casey17_HM[23])
# BrO_Mawson17_HM  = np.append(BrO_Mawson17_HM,  BrO_Mawson17_HM[23])
# BrO_Davis17_HM3  = np.append(BrO_Davis17_HM3,  BrO_Davis17_HM3[23])

# BrO_Davis18_HM1  = np.append(BrO_Davis18_HM1,  BrO_Davis18_HM1[23])
# BrO_Casey18_HM   = np.append(BrO_Casey18_HM,   BrO_Casey18_HM[23])
# BrO_Mawson18_HM  = np.append(BrO_Mawson18_HM,  BrO_Mawson18_HM[23])
# BrO_Davis18_HM3  = np.append(BrO_Davis18_HM3,  BrO_Davis18_HM3[23])

# BrO_SIPEXII12_HM = np.append(BrO_SIPEXII12_HM, BrO_SIPEXII12_HM[23])

# O3
O3_Davis17_H75P1  = np.append(O3_Davis17_H75P1,  O3_Davis17_H75P1[0])
O3_Casey17_H75P   = np.append(O3_Casey17_H75P,   O3_Casey17_H75P[0])
O3_Mawson17_H75P  = np.append(O3_Mawson17_H75P,  O3_Mawson17_H75P[0])
O3_Davis17_H75P3  = np.append(O3_Davis17_H75P3,  O3_Davis17_H75P3[0])
O3_MQIsl17_H75P   = np.append(O3_MQIsl17_H75P,   O3_MQIsl17_H75P[0])

O3_Davis18_H75P1  = np.append(O3_Davis18_H75P1,  O3_Davis18_H75P1[0])
O3_Casey18_H75P   = np.append(O3_Casey18_H75P,   O3_Casey18_H75P[0])
O3_Mawson18_H75P  = np.append(O3_Mawson18_H75P,  O3_Mawson18_H75P[0])
O3_Davis18_H75P3  = np.append(O3_Davis18_H75P3,  O3_Davis18_H75P3[0])
O3_MQIsl18_H75P   = np.append(O3_MQIsl18_H75P,   O3_MQIsl18_H75P[0])

O3_PCAN17_H75P    = np.append(O3_PCAN17_H75P,    O3_PCAN17_H75P[0])
O3_SIPEXII12_H75P = np.append(O3_SIPEXII12_H75P, O3_SIPEXII12_H75P[0])

# RH
RH_Davis17_H75P1  = np.append(RH_Davis17_H75P1,  RH_Davis17_H75P1[0])
RH_Casey17_H75P   = np.append(RH_Casey17_H75P,   RH_Casey17_H75P[0])
RH_Mawson17_H75P  = np.append(RH_Mawson17_H75P,  RH_Mawson17_H75P[0])
RH_Davis17_H75P3  = np.append(RH_Davis17_H75P3,  RH_Davis17_H75P3[0])
RH_MQIsl17_H75P   = np.append(RH_MQIsl17_H75P,   RH_MQIsl17_H75P[0])

RH_Davis18_H75P1  = np.append(RH_Davis18_H75P1,  RH_Davis18_H75P1[0])
RH_Casey18_H75P   = np.append(RH_Casey18_H75P,   RH_Casey18_H75P[0])
RH_Mawson18_H75P  = np.append(RH_Mawson18_H75P,  RH_Mawson18_H75P[0])
RH_Davis18_H75P3  = np.append(RH_Davis18_H75P3,  RH_Davis18_H75P3[0])
RH_MQIsl18_H75P   = np.append(RH_MQIsl18_H75P,   RH_MQIsl18_H75P[0])

RH_PCAN17_H75P    = np.append(RH_PCAN17_H75P,    RH_PCAN17_H75P[0])
RH_SIPEXII12_H75P = np.append(RH_SIPEXII12_H75P, RH_SIPEXII12_H75P[0])

# Temp
Temp_Davis17_H75P1  = np.append(Temp_Davis17_H75P1,  Temp_Davis17_H75P1[0])
Temp_Casey17_H75P   = np.append(Temp_Casey17_H75P,   Temp_Casey17_H75P[0])
Temp_Mawson17_H75P  = np.append(Temp_Mawson17_H75P,  Temp_Mawson17_H75P[0])
Temp_Davis17_H75P3  = np.append(Temp_Davis17_H75P3,  Temp_Davis17_H75P3[0])
Temp_MQIsl17_H75P   = np.append(Temp_MQIsl17_H75P,   Temp_MQIsl17_H75P[0])

Temp_Davis18_H75P1  = np.append(Temp_Davis18_H75P1,  Temp_Davis18_H75P1[0])
Temp_Casey18_H75P   = np.append(Temp_Casey18_H75P,   Temp_Casey18_H75P[0])
Temp_Mawson18_H75P  = np.append(Temp_Mawson18_H75P,  Temp_Mawson18_H75P[0])
Temp_Davis18_H75P3  = np.append(Temp_Davis18_H75P3,  Temp_Davis18_H75P3[0])
Temp_MQIsl18_H75P   = np.append(Temp_MQIsl18_H75P,   Temp_MQIsl18_H75P[0])

Temp_PCAN17_H75P    = np.append(Temp_PCAN17_H75P,    Temp_PCAN17_H75P[0])
Temp_SIPEXII12_H75P = np.append(Temp_SIPEXII12_H75P, Temp_SIPEXII12_H75P[0])

# SolRad
SR_Davis17_H75P1  = np.append(SR_Davis17_H75P1,  SR_Davis17_H75P1[0])
SR_Casey17_H75P   = np.append(SR_Casey17_H75P,   SR_Casey17_H75P[0])
SR_Mawson17_H75P  = np.append(SR_Mawson17_H75P,  SR_Mawson17_H75P[0])
SR_Davis17_H75P3  = np.append(SR_Davis17_H75P3,  SR_Davis17_H75P3[0])
SR_MQIsl17_H75P   = np.append(SR_MQIsl17_H75P,   SR_MQIsl17_H75P[0])

SR_Davis18_H75P1  = np.append(SR_Davis18_H75P1,  SR_Davis18_H75P1[0])
SR_Casey18_H75P   = np.append(SR_Casey18_H75P,   SR_Casey18_H75P[0])
SR_Mawson18_H75P  = np.append(SR_Mawson18_H75P,  SR_Mawson18_H75P[0])
SR_Davis18_H75P3  = np.append(SR_Davis18_H75P3,  SR_Davis18_H75P3[0])
SR_MQIsl18_H75P   = np.append(SR_MQIsl18_H75P,   SR_MQIsl18_H75P[0])

SR_PCAN17_H75P    = np.append(SR_PCAN17_H75P,    SR_PCAN17_H75P[0])
SR_SIPEXII12_H75P = np.append(SR_SIPEXII12_H75P, SR_SIPEXII12_H75P[0])

# Wind Speed
WS_Davis17_H75P1  = np.append(WS_Davis17_H75P1,  WS_Davis17_H75P1[0])
WS_Casey17_H75P   = np.append(WS_Casey17_H75P,   WS_Casey17_H75P[0])
WS_Mawson17_H75P = np.append(WS_Mawson17_H75P,  WS_Mawson17_H75P[0])
WS_Davis17_H75P3  = np.append(WS_Davis17_H75P3,  WS_Davis17_H75P3[0])
WS_MQIsl17_H75P   = np.append(WS_MQIsl17_H75P,   WS_MQIsl17_H75P[0])

WS_Davis18_H75P1  = np.append(WS_Davis18_H75P1,  WS_Davis18_H75P1[0])
WS_Casey18_H75P   = np.append(WS_Casey18_H75P,   WS_Casey18_H75P[0])
WS_Mawson18_H75P  = np.append(WS_Mawson18_H75P,  WS_Mawson18_H75P[0])
WS_Davis18_H75P3  = np.append(WS_Davis18_H75P3,  WS_Davis18_H75P3[0])
WS_MQIsl18_H75P   = np.append(WS_MQIsl18_H75P,   WS_MQIsl18_H75P[0])

WS_PCAN17_H75P    = np.append(WS_PCAN17_H75P,    WS_PCAN17_H75P[0])
WS_SIPEXII12_H75P = np.append(WS_SIPEXII12_H75P, WS_SIPEXII12_H75P[0])

# Sea Ice
Hg0_Ice_V1_17_H75P = np.append(Hg0_Ice_V1_17_H75P, Hg0_Ice_V1_17_H75P[0])
Hg0_Ice_V2_17_H75P = np.append(Hg0_Ice_V2_17_H75P, Hg0_Ice_V2_17_H75P[0])
Hg0_Ice_V3_17_H75P = np.append(Hg0_Ice_V3_17_H75P, Hg0_Ice_V3_17_H75P[0])

Hg0_Ice_V1_18_H75P = np.append(Hg0_Ice_V1_18_H75P, Hg0_Ice_V1_18_H75P[0])
Hg0_Ice_V2_18_H75P = np.append(Hg0_Ice_V2_18_H75P, Hg0_Ice_V2_18_H75P[0])
Hg0_Ice_V3_18_H75P = np.append(Hg0_Ice_V3_18_H75P, Hg0_Ice_V3_18_H75P[0])

# Open water
Hg0_OW_V1_17_H75P  = np.append(Hg0_OW_V1_17_H75P,  Hg0_OW_V1_17_H75P[0])
Hg0_OW_V2_17_H75P  = np.append(Hg0_OW_V2_17_H75P,  Hg0_OW_V2_17_H75P[0])
Hg0_OW_V3_17_H75P  = np.append(Hg0_OW_V3_17_H75P,  Hg0_OW_V3_17_H75P[0])

Hg0_OW_V1_18_H75P  = np.append(Hg0_OW_V1_18_H75P,  Hg0_OW_V1_18_H75P[0])
Hg0_OW_V2_18_H75P  = np.append(Hg0_OW_V2_18_H75P,  Hg0_OW_V2_18_H75P[0])
Hg0_OW_V3_18_H75P  = np.append(Hg0_OW_V3_18_H75P,  Hg0_OW_V3_18_H75P[0])

#------------------------------------------------------------------------------
# CALCULATE THE 95th PERCENTILE FOR THE Hg0 DAILY AVERAGE (MEAN)

# Function to calculate the standard deviation
def hourly95P(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').quantile(q=0.95)
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

#----------------------
# Whole Voyage
#----------------------
# Hg0
Hg0_V1_17_H95P,     time1_H95Pa  = hourly95P(V1_17_Hg0[:],      time1a) # V1_17
Hg0_V2_17_H95P,     time2_H95Pa  = hourly95P(V2_17_Hg0[:],      time2a) # V2_17
Hg0_V3_17M_H95P,    time3_H95Pa  = hourly95P(V3_17M_Hg0[:],     time3a) # V3_17 (Mawson)
Hg0_V3_17D_H95P,    time4_H95Pa  = hourly95P(V3_17D_Hg0[:],     time4a) # V3_17 (Davis)
Hg0_V4_17_H95P,     time5_H95Pa  = hourly95P(V4_17_Hg0[:],      time5a) # V4_17

Hg0_V1_18_H95P,     time6_H95Pa  = hourly95P(V1_18_Hg0[:],      time6a) # V1_18
Hg0_V2_18_H95P,     time7_H95Pa  = hourly95P(V2_18_Hg0[:],      time7a) # V2_18
Hg0_V3_18M_H95P,    time8_H95Pa  = hourly95P(V3_18M_Hg0[:],     time8a) # V3_18 (Mawson)
Hg0_V3_18D_H95P,    time9_H95Pa  = hourly95P(V3_18D_Hg0[:],     time9a) # V3_18 (Davis)
Hg0_V4_18_H95P,     time10_H95Pa = hourly95P(V4_18_Hg0[:],      time10a) # V4_18

Hg0_PCAN_H95P,      time11_H95Pa = hourly95P(PCAN_Hg0[:],       time11a) # PCAN
Hg0_SIPEXII_H95P,   time12_H95Pa = hourly95P(SIPEXII_Hg0[:],    time12a) # SIPEXII

# BrO
BrO_V1_17_H95P,   time1_HMz  = hourly95P(V1_17_BrO[:],   time1z) # V1_17
BrO_V2_17_H95P,   time2_HMz  = hourly95P(V2_17_BrO[:],   time2z) # V2_17
BrO_V3_17M_H95P,  time3_HMz  = hourly95P(V3_17M_BrO[:],  time3z) # V3_17 (Mawson)
BrO_V3_17D_H95P,  time4_HMz  = hourly95P(V3_17D_BrO[:],  time4z) # V3_17 (Davis)

BrO_V1_18_H95P,   time6_HMz  = hourly95P(V1_18_BrO[:],   time5z) # V1_18
BrO_V2_18_H95P,   time7_HMz  = hourly95P(V2_18_BrO[:],   time6z) # V2_18
BrO_V3_18M_H95P,  time8_HMz  = hourly95P(V3_18M_BrO[:],  time7z) # V3_18 (Mawson)
BrO_V3_18D_H95P,  time9_HMz  = hourly95P(V3_18D_BrO[:],  time8z) # V3_18 (Davis)

BrO_SIPEXII_H95P, time12_HMz = hourly95P(SIPEXII_BrO[:], time9z) # SIPEXII

#----------------------
# At Station
#----------------------
# Hg0
Hg0_Davis17_H95P1,  time1_H95Pb  = hourly95P(Hg0_Davis1_17[:],  time1b) # V1_17
Hg0_Casey17_H95P,   time2_H95Pb  = hourly95P(Hg0_Casey_17[:],   time2b) # V2_17
Hg0_Mawson17_H95P,  time3_H95Pb  = hourly95P(Hg0_Mawson_17[:],  time3b) # V3_17
Hg0_Davis17_H95P3,  time4_H95Pb  = hourly95P(Hg0_Davis3_17[:],  time4b) # V3_17
Hg0_MQIsl17_H95P,   time5_H95Pb  = hourly95P(Hg0_MQIsl_17[:],   time5b) # V4_17

Hg0_Davis18_H95P1,  time6_H95Pb  = hourly95P(Hg0_Davis1_18[:],  time6b) # V1_18
Hg0_Casey18_H95P,   time7_H95Pb  = hourly95P(Hg0_Casey_18[:],   time7b) # V2_18
Hg0_Mawson18_H95P,  time8_H95Pb  = hourly95P(Hg0_Mawson_18[:],  time8b) # V3_18
Hg0_Davis18_H95P3,  time9_H95Pb  = hourly95P(Hg0_Davis3_18[:],  time9b) # V3_18
Hg0_MQIsl18_H95P,   time10_H95Pb = hourly95P(Hg0_MQIsl_18[:],   time10b) # V4_18

Hg0_PCAN17_H95P,    time11_H95Pb = hourly95P(Hg0_PCAN_17[:],    time11b) # PCAN
Hg0_SIPEXII12_H95P, time12_H95Pb = hourly95P(Hg0_SIPEXII_12[:], time12b) # SIPEXII

# BrO
BrO_Davis17_H95P1,  time1_HMy  = hourly95P(BrO_Davis1_17[:],  time1y) # V1_17
BrO_Casey17_H95P,   time2_HMy  = hourly95P(BrO_Casey_17[:],  time2y) # V2_17
BrO_Mawson17_H95P,  time3_HMy  = hourly95P(BrO_Mawson_17[:], time3y) # V3_17 (Mawson)
BrO_Davis17_H95P3,  time4_HMy  = hourly95P(BrO_Davis3_17[:],  time4y) # V3_17 (Davis)

BrO_Davis18_H95P1,  time6_HMy  = hourly95P(BrO_Davis1_18[:],  time5y) # V1_18
BrO_Casey18_H95P,   time7_HMy  = hourly95P(BrO_Casey_18[:],  time6y) # V2_18
BrO_Mawson18_H95P,  time8_HMy  = hourly95P(BrO_Mawson_18[:], time7y) # V3_18 (Mawson)
BrO_Davis18_H95P3,  time9_HMy  = hourly95P(BrO_Davis3_18[:],  time8y) # V3_18 (Davis)

BrO_SIPEXII12_H95P, time12_HMy = hourly95P(BrO_SIPEXII_12[:],  time9y) # SIPEXII

# O3
O3_Davis17_H95P1,  time1_HMb  = hourly95P(O3_Davis1_17[:], time1b_O3) # V1_17
O3_Casey17_H95P,   time2_HMb  = hourly95P(O3_Casey_17[:],  time2b_O3) # V2_17
O3_Mawson17_H95P,  time3_HMb  = hourly95P(O3_Mawson_17[:], time3b_O3) # V3_17 (Mawson)
O3_Davis17_H95P3,  time4_HMb  = hourly95P(O3_Davis3_17[:], time4b_O3) # V3_17 (Davis)
O3_MQIsl17_H95P,   time5_HMb  = hourly95P(O3_MQIsl_17[:],  time5b_O3) # V4_17

O3_Davis18_H95P1,  time6_HMb  = hourly95P(O3_Davis1_18[:], time6b_O3) # V1_18
O3_Casey18_H95P,   time7_HMb  = hourly95P(O3_Casey_18[:],  time7b_O3) # V2_18
O3_Mawson18_H95P,  time8_HMb  = hourly95P(O3_Mawson_18[:], time8b_O3) # V3_18 (Mawson)
O3_Davis18_H95P3,  time9_HMb  = hourly95P(O3_Davis3_18[:], time9b_O3) # V3_18 (Davis)
O3_MQIsl18_H95P,   time10_HMb = hourly95P(O3_MQIsl_18[:],  time10b_O3) # V4_18

O3_PCAN17_H95P,    time11_HMb = hourly95P(O3_PCAN_17[:],   time11b_O3) # PCAN
O3_SIPEXII12_H95P, time12_HMb = hourly95P(O3_SIPEXII_12[:], time12b_O3) # SIPEXII

# RH
RH_Davis17_H95P1,    time1_HMb  = hourly95P(np.array(Met_Davis_V1_17['RH_Avg']),  time1b_Met) # V1_17
RH_Casey17_H95P,     time2_HMb  = hourly95P(np.array(Met_Casey_V2_17['RH_Avg']),  time2b_Met) # V2_17
RH_Mawson17_H95P,    time3_HMb  = hourly95P(np.array(Met_Mawson_V3_17['RH_Avg']), time3b_Met) # V3_17
RH_Davis17_H95P3,    time4_HMb  = hourly95P(np.array(Met_Davis_V3_17['RH_Avg']),  time4b_Met) # V3_17
RH_MQIsl17_H95P,     time5_HMb  = hourly95P(np.array(Met_MQIsl_V4_17['RH_Avg']),  time5b_Met) # V4_17

RH_Davis18_H95P1,    time6_HMb  = hourly95P(np.array(Met_Davis_V1_18['RH_Avg']),  time6b_Met) # V1_18
RH_Casey18_H95P,     time7_HMb  = hourly95P(np.array(Met_Casey_V2_18['RH_Avg']),  time7b_Met) # V2_18
RH_Mawson18_H95P,    time8_HMb  = hourly95P(np.array(Met_Mawson_V3_18['RH_Avg']), time8b_Met) # V3_18
RH_Davis18_H95P3,    time9_HMb  = hourly95P(np.array(Met_Davis_V3_18['RH_Avg']),  time9b_Met) # V3_18
RH_MQIsl18_H95P,     time10_HMb = hourly95P(np.array(Met_MQIsl_V4_18['RH_Avg']),  time10b_Met) # V4_18

RH_PCAN17_H95P,      time11_HMb = hourly95P(np.array(Met_PCAN_Ice['RH_Avg']),     time11b_Met) # PCAN
RH_SIPEXII12_H95P,   time12_HMb = hourly95P(np.array(Met_SIPEXII_Ice['RH_Avg']),  time12b_Met) # SIPEXII

# Temp
Temp_Davis17_H95P1,    time1_HMb  = hourly95P(np.array(Met_Davis_V1_17['Temp_Avg']),  time1b_Met) # V1_17
Temp_Casey17_H95P,     time2_HMb  = hourly95P(np.array(Met_Casey_V2_17['Temp_Avg']),  time2b_Met) # V2_17
Temp_Mawson17_H95P,    time3_HMb  = hourly95P(np.array(Met_Mawson_V3_17['Temp_Avg']), time3b_Met) # V3_17
Temp_Davis17_H95P3,    time4_HMb  = hourly95P(np.array(Met_Davis_V3_17['Temp_Avg']),  time4b_Met) # V3_17
Temp_MQIsl17_H95P,     time5_HMb  = hourly95P(np.array(Met_MQIsl_V4_17['Temp_Avg']),  time5b_Met) # V4_17

Temp_Davis18_H95P1,    time6_HMb  = hourly95P(np.array(Met_Davis_V1_18['Temp_Avg']),  time6b_Met) # V1_18
Temp_Casey18_H95P,     time7_HMb  = hourly95P(np.array(Met_Casey_V2_18['Temp_Avg']),  time7b_Met) # V2_18
Temp_Mawson18_H95P,    time8_HMb  = hourly95P(np.array(Met_Mawson_V3_18['Temp_Avg']), time8b_Met) # V3_18
Temp_Davis18_H95P3,    time9_HMb  = hourly95P(np.array(Met_Davis_V3_18['Temp_Avg']),  time9b_Met) # V3_18
Temp_MQIsl18_H95P,     time10_HMb = hourly95P(np.array(Met_MQIsl_V4_18['Temp_Avg']),  time10b_Met) # V4_18

Temp_PCAN17_H95P,      time11_HMb = hourly95P(np.array(Met_PCAN_Ice['Temp_Avg']),     time11b_Met) # PCAN
Temp_SIPEXII12_H95P,   time12_HMb = hourly95P(np.array(Met_SIPEXII_Ice['Temp_Avg']),  time12b_Met) # SIPEXII

# SolRad
SR_Davis17_H95P1,    time1_HMb  = hourly95P(np.array(Met_Davis_V1_17['SolRad_Avg']),  time1b_Met) # V1_17
SR_Casey17_H95P,     time2_HMb  = hourly95P(np.array(Met_Casey_V2_17['SolRad_Avg']),  time2b_Met) # V2_17
SR_Mawson17_H95P,    time3_HMb  = hourly95P(np.array(Met_Mawson_V3_17['SolRad_Avg']), time3b_Met) # V3_17
SR_Davis17_H95P3,    time4_HMb  = hourly95P(np.array(Met_Davis_V3_17['SolRad_Avg']),  time4b_Met) # V3_17
SR_MQIsl17_H95P,     time5_HMb  = hourly95P(np.array(Met_MQIsl_V4_17['SolRad_Avg']),  time5b_Met) # V4_17

SR_Davis18_H95P1,    time6_HMb  = hourly95P(np.array(Met_Davis_V1_18['SolRad_Avg']),  time6b_Met) # V1_18
SR_Casey18_H95P,     time7_HMb  = hourly95P(np.array(Met_Casey_V2_18['SolRad_Avg']),  time7b_Met) # V2_18
SR_Mawson18_H95P,    time8_HMb  = hourly95P(np.array(Met_Mawson_V3_18['SolRad_Avg']), time8b_Met) # V3_18
SR_Davis18_H95P3,    time9_HMb  = hourly95P(np.array(Met_Davis_V3_18['SolRad_Avg']),  time9b_Met) # V3_18
SR_MQIsl18_H95P,     time10_HMb = hourly95P(np.array(Met_MQIsl_V4_18['SolRad_Avg']),  time10b_Met) # V4_18

SR_PCAN17_H95P,      time11_HMb = hourly95P(np.array(Met_PCAN_Ice['SolRad_Avg']),     time11b_Met) # PCAN
SR_SIPEXII12_H95P,   time12_HMb = hourly95P(np.array(Met_SIPEXII_Ice['SolRad_Avg']),  time12b_Met) # SIPEXII

# Wind Speed
WS_Davis17_H95P1,    time1_HMb  = hourly95P(np.array(Met_Davis_V1_17['WS_Avg']),  time1b_Met) # V1_17
WS_Casey17_H95P,     time2_HMb  = hourly95P(np.array(Met_Casey_V2_17['WS_Avg']),  time2b_Met) # V2_17
WS_Mawson17_H95P,    time3_HMb  = hourly95P(np.array(Met_Mawson_V3_17['WS_Avg']), time3b_Met) # V3_17
WS_Davis17_H95P3,    time4_HMb  = hourly95P(np.array(Met_Davis_V3_17['WS_Avg']),  time4b_Met) # V3_17
WS_MQIsl17_H95P,     time5_HMb  = hourly95P(np.array(Met_MQIsl_V4_17['WS_Avg']),  time5b_Met) # V4_17

WS_Davis18_H95P1,    time6_HMb  = hourly95P(np.array(Met_Davis_V1_18['WS_Avg']),  time6b_Met) # V1_18
WS_Casey18_H95P,     time7_HMb  = hourly95P(np.array(Met_Casey_V2_18['WS_Avg']),  time7b_Met) # V2_18
WS_Mawson18_H95P,    time8_HMb  = hourly95P(np.array(Met_Mawson_V3_18['WS_Avg']), time8b_Met) # V3_18
WS_Davis18_H95P3,    time9_HMb  = hourly95P(np.array(Met_Davis_V3_18['WS_Avg']),  time9b_Met) # V3_18
WS_MQIsl18_H95P,     time10_HMb = hourly95P(np.array(Met_MQIsl_V4_18['WS_Avg']),  time10b_Met) # V4_18

WS_PCAN17_H95P,      time11_HMb = hourly95P(np.array(Met_PCAN_Ice['WS_Avg']),     time11b_Met) # PCAN
WS_SIPEXII12_H95P,   time12_HMb = hourly95P(np.array(Met_SIPEXII_Ice['WS_Avg']),  time12b_Met) # SIPEXII

#----------------------
# Sea Ice
#----------------------
Hg0_Ice_V1_17_H95P, time1_H95Pc  = hourly95P(Hg0_Ice1_V1_17[:], time1c) # V1_17
Hg0_Ice_V2_17_H95P, time2_H95Pc  = hourly95P(Hg0_Ice1_V2_17[:], time2c) # V2_17
Hg0_Ice_V3_17_H95P, time3_H95Pc  = hourly95P(Hg0_Ice1_V3_17[:], time3c) # V3_17

Hg0_Ice_V1_18_H95P, time4_H95Pc  = hourly95P(Hg0_Ice1_V1_18[:], time4c) # V1_18
Hg0_Ice_V2_18_H95P, time5_H95Pc  = hourly95P(Hg0_Ice1_V2_18[:], time5c) # V2_18
Hg0_Ice_V3_18_H95P, time6_H95Pc  = hourly95P(Hg0_Ice1_V3_18[:], time6c) # V3_18

#----------------------
# Open Water
#----------------------
Hg0_OW_V1_17_H95P,  time1_H95Pd  = hourly95P(Hg0_OW1_V1_17[:], time1d) # V1_17
Hg0_OW_V2_17_H95P,  time2_H95Pd  = hourly95P(Hg0_OW1_V2_17[:], time2d) # V2_17
Hg0_OW_V3_17_H95P,  time3_H95Pd  = hourly95P(Hg0_OW1_V3_17[:], time3d) # V3_17

Hg0_OW_V1_18_H95P,  time4_H95Pd  = hourly95P(Hg0_OW1_V1_18[:], time4d) # V1_18
Hg0_OW_V2_18_H95P,  time5_H95Pd  = hourly95P(Hg0_OW1_V2_18[:], time5d) # V2_18
Hg0_OW_V3_18_H95P,  time6_H95Pd  = hourly95P(Hg0_OW1_V3_18[:], time6d) # V3_18

#------------------------------------------------------------------------------
# Append the first value to complete the diurnal cycle
# Hg0
Hg0_Davis17_H95P1  = np.append(Hg0_Davis17_H95P1,  Hg0_Davis17_H95P1[0])
Hg0_Casey17_H95P   = np.append(Hg0_Casey17_H95P,   Hg0_Casey17_H95P[0])
Hg0_Mawson17_H95P  = np.append(Hg0_Mawson17_H95P,  Hg0_Mawson17_H95P[0])
Hg0_Davis17_H95P3  = np.append(Hg0_Davis17_H95P3,  Hg0_Davis17_H95P3[0])
Hg0_MQIsl17_H95P   = np.append(Hg0_MQIsl17_H95P,   Hg0_MQIsl17_H95P[0])

Hg0_Davis18_H95P1  = np.append(Hg0_Davis18_H95P1,  Hg0_Davis18_H95P1[0])
Hg0_Casey18_H95P   = np.append(Hg0_Casey18_H95P,   Hg0_Casey18_H95P[0])
Hg0_Mawson18_H95P  = np.append(Hg0_Mawson18_H95P,  Hg0_Mawson18_H95P[0])
Hg0_Davis18_H95P3  = np.append(Hg0_Davis18_H95P3,  Hg0_Davis18_H95P3[0])
Hg0_MQIsl18_H95P   = np.append(Hg0_MQIsl18_H95P,   Hg0_MQIsl18_H95P[0])

Hg0_PCAN17_H95P    = np.append(Hg0_PCAN17_H95P,    Hg0_PCAN17_H95P[0])
Hg0_SIPEXII12_H95P = np.append(Hg0_SIPEXII12_H95P, Hg0_SIPEXII12_H95P[0])

# BrO
# BrO_Davis17_H95P1  = np.append(BrO_Davis17_H95P1,  BrO_Davis17_H95P1[23])
# BrO_Casey17_H95P   = np.append(BrO_Casey17_H95P,   BrO_Casey17_H95P[23])
# BrO_Mawson17_H95P  = np.append(BrO_Mawson17_H95P,  BrO_Mawson17_H95P[23])
# BrO_Davis17_H95P3  = np.append(BrO_Davis17_H95P3,  BrO_Davis17_H95P3[23])

# BrO_Davis18_H95P1  = np.append(BrO_Davis18_H95P1,  BrO_Davis18_H95P1[23])
# BrO_Casey18_H95P   = np.append(BrO_Casey18_H95P,   BrO_Casey18_H95P[23])
# BrO_Mawson18_H95P  = np.append(BrO_Mawson18_H95P,  BrO_Mawson18_H95P[23])
# BrO_Davis18_H95P3  = np.append(BrO_Davis18_H95P3,  BrO_Davis18_H95P3[23])

# BrO_SIPEXII12_H95P = np.append(BrO_SIPEXII12_H95P, BrO_SIPEXII12_H95P[23])

# O3
O3_Davis17_H95P1  = np.append(O3_Davis17_H95P1,  O3_Davis17_H95P1[0])
O3_Casey17_H95P   = np.append(O3_Casey17_H95P,   O3_Casey17_H95P[0])
O3_Mawson17_H95P  = np.append(O3_Mawson17_H95P,  O3_Mawson17_H95P[0])
O3_Davis17_H95P3  = np.append(O3_Davis17_H95P3,  O3_Davis17_H95P3[0])
O3_MQIsl17_H95P   = np.append(O3_MQIsl17_H95P,   O3_MQIsl17_H95P[0])

O3_Davis18_H95P1  = np.append(O3_Davis18_H95P1,  O3_Davis18_H95P1[0])
O3_Casey18_H95P   = np.append(O3_Casey18_H95P,   O3_Casey18_H95P[0])
O3_Mawson18_H95P  = np.append(O3_Mawson18_H95P,  O3_Mawson18_H95P[0])
O3_Davis18_H95P3  = np.append(O3_Davis18_H95P3,  O3_Davis18_H95P3[0])
O3_MQIsl18_H95P   = np.append(O3_MQIsl18_H95P,   O3_MQIsl18_H95P[0])

O3_PCAN17_H95P    = np.append(O3_PCAN17_H95P,    O3_PCAN17_H95P[0])
O3_SIPEXII12_H95P = np.append(O3_SIPEXII12_H95P, O3_SIPEXII12_H95P[0])

# RH
RH_Davis17_H95P1  = np.append(RH_Davis17_H95P1,  RH_Davis17_H95P1[0])
RH_Casey17_H95P   = np.append(RH_Casey17_H95P,   RH_Casey17_H95P[0])
RH_Mawson17_H95P  = np.append(RH_Mawson17_H95P,  RH_Mawson17_H95P[0])
RH_Davis17_H95P3  = np.append(RH_Davis17_H95P3,  RH_Davis17_H95P3[0])
RH_MQIsl17_H95P   = np.append(RH_MQIsl17_H95P,   RH_MQIsl17_H95P[0])

RH_Davis18_H95P1  = np.append(RH_Davis18_H95P1,  RH_Davis18_H95P1[0])
RH_Casey18_H95P   = np.append(RH_Casey18_H95P,   RH_Casey18_H95P[0])
RH_Mawson18_H95P  = np.append(RH_Mawson18_H95P,  RH_Mawson18_H95P[0])
RH_Davis18_H95P3  = np.append(RH_Davis18_H95P3,  RH_Davis18_H95P3[0])
RH_MQIsl18_H95P   = np.append(RH_MQIsl18_H95P,   RH_MQIsl18_H95P[0])

RH_PCAN17_H95P    = np.append(RH_PCAN17_H95P,    RH_PCAN17_H95P[0])
RH_SIPEXII12_H95P = np.append(RH_SIPEXII12_H95P, RH_SIPEXII12_H95P[0])

# Temp
Temp_Davis17_H95P1  = np.append(Temp_Davis17_H95P1,  Temp_Davis17_H95P1[0])
Temp_Casey17_H95P   = np.append(Temp_Casey17_H95P,   Temp_Casey17_H95P[0])
Temp_Mawson17_H95P  = np.append(Temp_Mawson17_H95P,  Temp_Mawson17_H95P[0])
Temp_Davis17_H95P3  = np.append(Temp_Davis17_H95P3,  Temp_Davis17_H95P3[0])
Temp_MQIsl17_H95P   = np.append(Temp_MQIsl17_H95P,   Temp_MQIsl17_H95P[0])

Temp_Davis18_H95P1  = np.append(Temp_Davis18_H95P1,  Temp_Davis18_H95P1[0])
Temp_Casey18_H95P   = np.append(Temp_Casey18_H95P,   Temp_Casey18_H95P[0])
Temp_Mawson18_H95P  = np.append(Temp_Mawson18_H95P,  Temp_Mawson18_H95P[0])
Temp_Davis18_H95P3  = np.append(Temp_Davis18_H95P3,  Temp_Davis18_H95P3[0])
Temp_MQIsl18_H95P   = np.append(Temp_MQIsl18_H95P,   Temp_MQIsl18_H95P[0])

Temp_PCAN17_H95P    = np.append(Temp_PCAN17_H95P,    Temp_PCAN17_H95P[0])
Temp_SIPEXII12_H95P = np.append(Temp_SIPEXII12_H95P, Temp_SIPEXII12_H95P[0])

# SolRad
SR_Davis17_H95P1  = np.append(SR_Davis17_H95P1,  SR_Davis17_H95P1[0])
SR_Casey17_H95P   = np.append(SR_Casey17_H95P,   SR_Casey17_H95P[0])
SR_Mawson17_H95P  = np.append(SR_Mawson17_H95P,  SR_Mawson17_H95P[0])
SR_Davis17_H95P3  = np.append(SR_Davis17_H95P3,  SR_Davis17_H95P3[0])
SR_MQIsl17_H95P   = np.append(SR_MQIsl17_H95P,   SR_MQIsl17_H95P[0])

SR_Davis18_H95P1  = np.append(SR_Davis18_H95P1,  SR_Davis18_H95P1[0])
SR_Casey18_H95P   = np.append(SR_Casey18_H95P,   SR_Casey18_H95P[0])
SR_Mawson18_H95P  = np.append(SR_Mawson18_H95P,  SR_Mawson18_H95P[0])
SR_Davis18_H95P3  = np.append(SR_Davis18_H95P3,  SR_Davis18_H95P3[0])
SR_MQIsl18_H95P   = np.append(SR_MQIsl18_H95P,   SR_MQIsl18_H95P[0])

SR_PCAN17_H95P    = np.append(SR_PCAN17_H95P,    SR_PCAN17_H95P[0])
SR_SIPEXII12_H95P = np.append(SR_SIPEXII12_H95P, SR_SIPEXII12_H95P[0])

# Wind Speed
WS_Davis17_H95P1  = np.append(WS_Davis17_H95P1,  WS_Davis17_H95P1[0])
WS_Casey17_H95P   = np.append(WS_Casey17_H95P,   WS_Casey17_H95P[0])
WS_Mawson17_H95P = np.append(WS_Mawson17_H95P,  WS_Mawson17_H95P[0])
WS_Davis17_H95P3  = np.append(WS_Davis17_H95P3,  WS_Davis17_H95P3[0])
WS_MQIsl17_H95P   = np.append(WS_MQIsl17_H95P,   WS_MQIsl17_H95P[0])

WS_Davis18_H95P1  = np.append(WS_Davis18_H95P1,  WS_Davis18_H95P1[0])
WS_Casey18_H95P   = np.append(WS_Casey18_H95P,   WS_Casey18_H95P[0])
WS_Mawson18_H95P  = np.append(WS_Mawson18_H95P,  WS_Mawson18_H95P[0])
WS_Davis18_H95P3  = np.append(WS_Davis18_H95P3,  WS_Davis18_H95P3[0])
WS_MQIsl18_H95P   = np.append(WS_MQIsl18_H95P,   WS_MQIsl18_H95P[0])

WS_PCAN17_H95P    = np.append(WS_PCAN17_H95P,    WS_PCAN17_H95P[0])
WS_SIPEXII12_H95P = np.append(WS_SIPEXII12_H95P, WS_SIPEXII12_H95P[0])

# Sea Ice
Hg0_Ice_V1_17_H95P = np.append(Hg0_Ice_V1_17_H95P, Hg0_Ice_V1_17_H95P[0])
Hg0_Ice_V2_17_H95P = np.append(Hg0_Ice_V2_17_H95P, Hg0_Ice_V2_17_H95P[0])
Hg0_Ice_V3_17_H95P = np.append(Hg0_Ice_V3_17_H95P, Hg0_Ice_V3_17_H95P[0])

Hg0_Ice_V1_18_H95P = np.append(Hg0_Ice_V1_18_H95P, Hg0_Ice_V1_18_H95P[0])
Hg0_Ice_V2_18_H95P = np.append(Hg0_Ice_V2_18_H95P, Hg0_Ice_V2_18_H95P[0])
Hg0_Ice_V3_18_H95P = np.append(Hg0_Ice_V3_18_H95P, Hg0_Ice_V3_18_H95P[0])

# Sea Ice
Hg0_OW_V1_17_H95P  = np.append(Hg0_OW_V1_17_H95P,  Hg0_OW_V1_17_H95P[0])
Hg0_OW_V2_17_H95P  = np.append(Hg0_OW_V2_17_H95P,  Hg0_OW_V2_17_H95P[0])
Hg0_OW_V3_17_H95P  = np.append(Hg0_OW_V3_17_H95P,  Hg0_OW_V3_17_H95P[0])

Hg0_OW_V1_18_H95P  = np.append(Hg0_OW_V1_18_H95P,  Hg0_OW_V1_18_H95P[0])
Hg0_OW_V2_18_H95P  = np.append(Hg0_OW_V2_18_H95P,  Hg0_OW_V2_18_H95P[0])
Hg0_OW_V3_18_H95P  = np.append(Hg0_OW_V3_18_H95P,  Hg0_OW_V3_18_H95P[0])

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN ABSOLUTE DEVIATION FOR THE Hg0 DAILY MEDIAN
# MAD = median(| x - median(x)|)

#------------------------------------
# Whole Voyage
#------------------------------------
# V1_17

# 1) Find the median
Hg0_V1_17.index  = Hg0_V1_17.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V1_17        = Hg0_V1_17.sort_index()
Hg0_V1_17_MEDIAN = (Hg0_V1_17['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V1_17_X      = np.array(Hg0_V1_17['ng/m3'])
Hg0_V1_17_X_M    = Hg0_V1_17_X - Hg0_V1_17_MEDIAN
# 3) find the absolute value for the difference
Hg0_V1_17_ABS    = Hg0_V1_17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V1_17_MAD    = Hg0_V1_17_ABS.rolling('1h').median()
Hg0_V1_17_MAD    = Hg0_V1_17_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V1_17_MAD    = np.array(Hg0_V1_17_MAD[:]) # convert from pandas.df to np.array
Hg0_V1_17_MAD    = Hg0_V1_17_MAD[~np.isnan(Hg0_V1_17_MAD)] # drop the nan values

# V2_17

# 1) Find the median
Hg0_V2_17.index  = Hg0_V2_17.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V2_17        = Hg0_V2_17.sort_index()
Hg0_V2_17_MEDIAN = (Hg0_V2_17['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V2_17_X      = np.array(Hg0_V2_17['ng/m3'])
Hg0_V2_17_X_M    = Hg0_V2_17_X - Hg0_V2_17_MEDIAN
# 3) find the absolute value for the difference
Hg0_V2_17_ABS    = Hg0_V2_17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V2_17_MAD    = Hg0_V2_17_ABS.rolling('1h').median()
Hg0_V2_17_MAD    = Hg0_V2_17_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V2_17_MAD    = np.array(Hg0_V2_17_MAD[:]) # convert from pandas.df to np.array
Hg0_V2_17_MAD    = Hg0_V2_17_MAD[~np.isnan(Hg0_V2_17_MAD)] # drop the nan values

# V3_17M (Mawson)

# 1) Find the median
Hg0_V3_17M.index  = Hg0_V3_17M.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V3_17M        = Hg0_V3_17M.sort_index()
Hg0_V3_17M_MEDIAN = (Hg0_V3_17M['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V3_17M_X      = np.array(Hg0_V3_17M['ng/m3'])
Hg0_V3_17M_X_M    = Hg0_V3_17M_X - Hg0_V3_17M_MEDIAN
# 3) find the absolute value for the difference
Hg0_V3_17M_ABS    = Hg0_V3_17M_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V3_17M_MAD    = Hg0_V3_17M_ABS.rolling('1h').median()
Hg0_V3_17M_MAD    = Hg0_V3_17M_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V3_17M_MAD    = np.array(Hg0_V3_17M_MAD[:]) # convert from pandas.df to np.array
Hg0_V3_17M_MAD    = Hg0_V3_17M_MAD[~np.isnan(Hg0_V3_17M_MAD)] # drop the nan values

# V3_17M (Davis)

# 1) Find the median
Hg0_V3_17D.index  = Hg0_V3_17D.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V3_17D        = Hg0_V3_17D.sort_index()
Hg0_V3_17D_MEDIAN = (Hg0_V3_17D['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V3_17D_X      = np.array(Hg0_V3_17D['ng/m3'])
Hg0_V3_17D_X_M    = Hg0_V3_17D_X - Hg0_V3_17D_MEDIAN
# 3) find the absolute value for the difference
Hg0_V3_17D_ABS    = Hg0_V3_17D_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V3_17D_MAD    = Hg0_V3_17D_ABS.rolling('1h').median()
Hg0_V3_17D_MAD    = Hg0_V3_17D_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V3_17D_MAD    = np.array(Hg0_V3_17D_MAD[:]) # convert from pandas.df to np.array
Hg0_V3_17D_MAD    = Hg0_V3_17D_MAD[~np.isnan(Hg0_V3_17D_MAD)] # drop the nan values

# V4_17

# 1) Find the median
Hg0_V4_17.index  = Hg0_V4_17.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V4_17        = Hg0_V4_17.sort_index()
Hg0_V4_17_MEDIAN = (Hg0_V4_17['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V4_17_X      = np.array(Hg0_V4_17['ng/m3'])
Hg0_V4_17_X_M    = Hg0_V4_17_X - Hg0_V4_17_MEDIAN
# 3) find the absolute value for the difference
Hg0_V4_17_ABS    = Hg0_V4_17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V4_17_MAD    = Hg0_V4_17_ABS.rolling('1h').median()
Hg0_V4_17_MAD    = Hg0_V4_17_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V4_17_MAD    = np.array(Hg0_V4_17_MAD[:]) # convert from pandas.df to np.array
Hg0_V4_17_MAD    = Hg0_V4_17_MAD[~np.isnan(Hg0_V4_17_MAD)] # drop the nan values

# V1_18

# 1) Find the median
Hg0_V1_18.index  = Hg0_V1_18.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V1_18        = Hg0_V1_18.sort_index()
Hg0_V1_18_MEDIAN = (Hg0_V1_18['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V1_18_X      = np.array(Hg0_V1_18['ng/m3'])
Hg0_V1_18_X_M    = Hg0_V1_18_X - Hg0_V1_18_MEDIAN
# 3) find the absolute value for the difference
Hg0_V1_18_ABS    = Hg0_V1_18_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V1_18_MAD    = Hg0_V1_18_ABS.rolling('1h').median()
Hg0_V1_18_MAD    = Hg0_V1_18_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V1_18_MAD    = np.array(Hg0_V1_18_MAD[:]) # convert from pandas.df to np.array
Hg0_V1_18_MAD    = Hg0_V1_18_MAD[~np.isnan(Hg0_V1_18_MAD)] # drop the nan values

# V2_17

# 1) Find the median
Hg0_V2_18.index  = Hg0_V2_18.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V2_18        = Hg0_V2_18.sort_index()
Hg0_V2_18_MEDIAN = (Hg0_V2_18['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V2_18_X      = np.array(Hg0_V2_18['ng/m3'])
Hg0_V2_18_X_M    = Hg0_V2_18_X - Hg0_V2_18_MEDIAN
# 3) find the absolute value for the difference
Hg0_V2_18_ABS    = Hg0_V2_18_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V2_18_MAD    = Hg0_V2_18_ABS.rolling('1h').median()
Hg0_V2_18_MAD    = Hg0_V2_18_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V2_18_MAD    = np.array(Hg0_V2_18_MAD[:]) # convert from pandas.df to np.array
Hg0_V2_18_MAD    = Hg0_V2_18_MAD[~np.isnan(Hg0_V2_18_MAD)] # drop the nan values

# V3_17M (Mawson)

# 1) Find the median
Hg0_V3_18M.index  = Hg0_V3_18M.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V3_18M        = Hg0_V3_18M.sort_index()
Hg0_V3_18M_MEDIAN = (Hg0_V3_18M['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V3_18M_X      = np.array(Hg0_V3_18M['ng/m3'])
Hg0_V3_18M_X_M    = Hg0_V3_18M_X - Hg0_V3_18M_MEDIAN
# 3) find the absolute value for the difference
Hg0_V3_18M_ABS    = Hg0_V3_18M_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V3_18M_MAD    = Hg0_V3_18M_ABS.rolling('1h').median()
Hg0_V3_18M_MAD    = Hg0_V3_18M_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V3_18M_MAD    = np.array(Hg0_V3_18M_MAD[:]) # convert from pandas.df to np.array
Hg0_V3_18M_MAD    = Hg0_V3_18M_MAD[~np.isnan(Hg0_V3_18M_MAD)] # drop the nan values

# V3_17M (Davis)

# 1) Find the median
Hg0_V3_18D.index  = Hg0_V3_18D.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V3_18D        = Hg0_V3_18D.sort_index()
Hg0_V3_18D_MEDIAN = (Hg0_V3_18D['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V3_18D_X      = np.array(Hg0_V3_18D['ng/m3'])
Hg0_V3_18D_X_M    = Hg0_V3_18D_X - Hg0_V3_18D_MEDIAN
# 3) find the absolute value for the difference
Hg0_V3_18D_ABS    = Hg0_V3_18D_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V3_18D_MAD    = Hg0_V3_18D_ABS.rolling('1h').median()
Hg0_V3_18D_MAD    = Hg0_V3_18D_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V3_18D_MAD    = np.array(Hg0_V3_18D_MAD[:]) # convert from pandas.df to np.array
Hg0_V3_18D_MAD    = Hg0_V3_18D_MAD[~np.isnan(Hg0_V3_18D_MAD)] # drop the nan values

# V4_18

# 1) Find the median
Hg0_V4_18.index  = Hg0_V4_18.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_V4_18        = Hg0_V4_18.sort_index()
Hg0_V4_18_MEDIAN = (Hg0_V4_18['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_V4_18_X      = np.array(Hg0_V4_18['ng/m3'])
Hg0_V4_18_X_M    = Hg0_V4_18_X - Hg0_V4_18_MEDIAN
# 3) find the absolute value for the difference
Hg0_V4_18_ABS    = Hg0_V4_18_X_M.abs()
# 4) find the median of the absolute difference
Hg0_V4_18_MAD    = Hg0_V4_18_ABS.rolling('1h').median()
Hg0_V4_18_MAD    = Hg0_V4_18_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_V4_18_MAD    = np.array(Hg0_V4_18_MAD[:]) # convert from pandas.df to np.array
Hg0_V4_18_MAD    = Hg0_V4_18_MAD[~np.isnan(Hg0_V4_18_MAD)] # drop the nan values

# PCAN

# 1) Find the median
Hg0_PCAN.index  = Hg0_PCAN.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_PCAN        = Hg0_PCAN.sort_index()
Hg0_PCAN_MEDIAN = (Hg0_PCAN['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_PCAN_X      = np.array(Hg0_PCAN['ng/m3'])
Hg0_PCAN_X_M    = Hg0_PCAN_X - Hg0_PCAN_MEDIAN
# 3) find the absolute value for the difference
Hg0_PCAN_ABS    = Hg0_PCAN_X_M.abs()
# 4) find the median of the absolute difference
Hg0_PCAN_MAD    = Hg0_PCAN_ABS.rolling('1h').median()
Hg0_PCAN_MAD    = Hg0_PCAN_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_PCAN_MAD    = np.array(Hg0_PCAN_MAD[:]) # convert from pandas.df to np.array
Hg0_PCAN_MAD    = Hg0_PCAN_MAD[~np.isnan(Hg0_PCAN_MAD)] # drop the nan values

# SIPEXII

# 1) Find the median
Hg0_SIPEXII.index  = Hg0_SIPEXII.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_SIPEXII        = Hg0_SIPEXII.sort_index()
Hg0_SIPEXII_MEDIAN = (Hg0_SIPEXII['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_SIPEXII_X      = np.array(Hg0_SIPEXII['ng/m3'])
Hg0_SIPEXII_X_M    = Hg0_SIPEXII_X - Hg0_SIPEXII_MEDIAN
# 3) find the absolute value for the difference
Hg0_SIPEXII_ABS    = Hg0_SIPEXII_X_M.abs()
# 4) find the median of the absolute difference
Hg0_SIPEXII_MAD    = Hg0_SIPEXII_ABS.rolling('1h').median()
Hg0_SIPEXII_MAD    = Hg0_SIPEXII_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_SIPEXII_MAD    = np.array(Hg0_SIPEXII_MAD[:]) # convert from pandas.df to np.array
Hg0_SIPEXII_MAD    = Hg0_SIPEXII_MAD[~np.isnan(Hg0_SIPEXII_MAD)] # drop the nan values

#------------------------------------
# At Station
#------------------------------------
# V1_17

# 1) Find the median
Hg0_Davis_V1_17.index  = Hg0_Davis_V1_17.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_Davis_V1_17        = Hg0_Davis_V1_17.sort_index()
Hg0_Davis_V1_17_MEDIAN = (Hg0_Davis_V1_17['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_Davis_V1_17_X      = np.array(Hg0_Davis_V1_17['ng/m3'])
Hg0_Davis_V1_17_X_M    = Hg0_Davis_V1_17_X - Hg0_Davis_V1_17_MEDIAN
# 3) find the absolute value for the difference
Hg0_Davis_V1_17_ABS    = Hg0_Davis_V1_17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_Davis17_MAD1       = Hg0_Davis_V1_17_ABS.rolling('1h').median()
Hg0_Davis17_MAD1       = Hg0_Davis17_MAD1.resample('1h').mean() # convert the MAD to a daily value
Hg0_Davis17_MAD1       = np.array(Hg0_Davis17_MAD1[:]) # convert from pandas.df to np.array
Hg0_Davis17_MAD1       = Hg0_Davis17_MAD1[~np.isnan(Hg0_Davis17_MAD1)] # drop the nan values

# V2_17

# 1) Find the median
Hg0_Casey_V2_17.index  = Hg0_Casey_V2_17.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_Casey_V2_17        = Hg0_Casey_V2_17.sort_index()
Hg0_Casey_V2_17_MEDIAN = (Hg0_Casey_V2_17['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_Casey_V2_17_X      = np.array(Hg0_Casey_V2_17['ng/m3'])
Hg0_Casey_V2_17_X_M    = Hg0_Casey_V2_17_X - Hg0_Casey_V2_17_MEDIAN
# 3) find the absolute value for the difference
Hg0_Casey_V2_17_ABS    = Hg0_Casey_V2_17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_Casey17_MAD        = Hg0_Casey_V2_17_ABS.rolling('1h').median()
Hg0_Casey17_MAD        = Hg0_Casey17_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_Casey17_MAD        = np.array(Hg0_Casey17_MAD[:]) # convert from pandas.df to np.array
Hg0_Casey17_MAD        = Hg0_Casey17_MAD[~np.isnan(Hg0_Casey17_MAD)] # drop the nan values

# V3_17M (Mawson)

# 1) Find the median
Hg0_Mawson_V3_17.index  = Hg0_Mawson_V3_17.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_Mawson_V3_17        = Hg0_Mawson_V3_17.sort_index()
Hg0_Mawson_V3_17_MEDIAN = (Hg0_Mawson_V3_17['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_Mawson_V3_17_X      = np.array(Hg0_Mawson_V3_17['ng/m3'])
Hg0_Mawson_V3_17_X_M    = Hg0_Mawson_V3_17_X - Hg0_Mawson_V3_17_MEDIAN
# 3) find the absolute value for the difference
Hg0_Mawson_V3_17_ABS    = Hg0_Mawson_V3_17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_Mawson17_MAD        = Hg0_Mawson_V3_17_ABS.rolling('1h').median()
Hg0_Mawson17_MAD        = Hg0_Mawson17_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_Mawson17_MAD        = np.array(Hg0_Mawson17_MAD[:]) # convert from pandas.df to np.array
Hg0_Mawson17_MAD        = Hg0_Mawson17_MAD[~np.isnan(Hg0_Mawson17_MAD)] # drop the nan values

# V3_17M (Davis)

# 1) Find the median
Hg0_Davis_V3_17.index  = Hg0_Davis_V3_17.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_Davis_V3_17        = Hg0_Davis_V3_17.sort_index()
Hg0_Davis_V3_17_MEDIAN = (Hg0_Davis_V3_17['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_Davis_V3_17_X      = np.array(Hg0_Davis_V3_17['ng/m3'])
Hg0_Davis_V3_17_X_M    = Hg0_Davis_V3_17_X - Hg0_Davis_V3_17_MEDIAN
# 3) find the absolute value for the difference
Hg0_Davis_V3_17_ABS    = Hg0_Davis_V3_17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_Davis17_MAD3       = Hg0_Davis_V3_17_ABS.rolling('1h').median()
Hg0_Davis17_MAD3       = Hg0_Davis17_MAD3.resample('1h').mean() # convert the MAD to a daily value
Hg0_Davis17_MAD3       = np.array(Hg0_Davis17_MAD3[:]) # convert from pandas.df to np.array
Hg0_Davis17_MAD3       = Hg0_Davis17_MAD3[~np.isnan(Hg0_Davis17_MAD3)] # drop the nan values

# V4_17

# 1) Find the median
Hg0_MQIsl_V4_17.index  = Hg0_MQIsl_V4_17.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_MQIsl_V4_17        = Hg0_MQIsl_V4_17.sort_index()
Hg0_MQIsl_V4_17_MEDIAN = (Hg0_MQIsl_V4_17['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_MQIsl_V4_17_X      = np.array(Hg0_MQIsl_V4_17['ng/m3'])
Hg0_MQIsl_V4_17_X_M    = Hg0_MQIsl_V4_17_X - Hg0_MQIsl_V4_17_MEDIAN
# 3) find the absolute value for the difference
Hg0_MQIsl_V4_17_ABS    = Hg0_MQIsl_V4_17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_MQIsl17_MAD        = Hg0_MQIsl_V4_17_ABS.rolling('1h').median()
Hg0_MQIsl17_MAD        = Hg0_MQIsl17_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_MQIsl17_MAD        = np.array(Hg0_MQIsl17_MAD[:]) # convert from pandas.df to np.array
Hg0_MQIsl17_MAD        = Hg0_MQIsl17_MAD[~np.isnan(Hg0_MQIsl17_MAD)] # drop the nan values

# V1_18

# 1) Find the median
Hg0_Davis_V1_18.index  = Hg0_Davis_V1_18.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_Davis_V1_18        = Hg0_Davis_V1_18.sort_index()
Hg0_Davis_V1_18_MEDIAN = (Hg0_Davis_V1_18['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_Davis_V1_18_X      = np.array(Hg0_Davis_V1_18['ng/m3'])
Hg0_Davis_V1_18_X_M    = Hg0_Davis_V1_18_X - Hg0_Davis_V1_18_MEDIAN
# 3) find the absolute value for the difference
Hg0_Davis_V1_18_ABS    = Hg0_Davis_V1_18_X_M.abs()
# 4) find the median of the absolute difference
Hg0_Davis18_MAD1       = Hg0_Davis_V1_18_ABS.rolling('1h').median()
Hg0_Davis18_MAD1       = Hg0_Davis18_MAD1.resample('1h').mean() # convert the MAD to a daily value
Hg0_Davis18_MAD1       = np.array(Hg0_Davis18_MAD1[:]) # convert from pandas.df to np.array
Hg0_Davis18_MAD1       = Hg0_Davis18_MAD1[~np.isnan(Hg0_Davis18_MAD1)] # drop the nan values

# V2_17

# 1) Find the median
Hg0_Casey_V2_18.index  = Hg0_Casey_V2_18.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_Casey_V2_18        = Hg0_Casey_V2_18.sort_index()
Hg0_Casey_V2_18_MEDIAN = (Hg0_Casey_V2_18['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_Casey_V2_18_X      = np.array(Hg0_Casey_V2_18['ng/m3'])
Hg0_Casey_V2_18_X_M    = Hg0_Casey_V2_18_X - Hg0_Casey_V2_18_MEDIAN
# 3) find the absolute value for the difference
Hg0_Casey_V2_18_ABS    = Hg0_Casey_V2_18_X_M.abs()
# 4) find the median of the absolute difference
Hg0_Casey18_MAD        = Hg0_Casey_V2_18_ABS.rolling('1h').median()
Hg0_Casey18_MAD        = Hg0_Casey18_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_Casey18_MAD        = np.array(Hg0_Casey18_MAD[:]) # convert from pandas.df to np.array
Hg0_Casey18_MAD        = Hg0_Casey18_MAD[~np.isnan(Hg0_Casey18_MAD)] # drop the nan values

# V3_17M (Mawson)

# 1) Find the median
Hg0_Mawson_V3_18.index  = Hg0_Mawson_V3_18.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_Mawson_V3_18        = Hg0_Mawson_V3_18.sort_index()
Hg0_Mawson_V3_18_MEDIAN = (Hg0_Mawson_V3_18['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_Mawson_V3_18_X      = np.array(Hg0_Mawson_V3_18['ng/m3'])
Hg0_Mawson_V3_18_X_M    = Hg0_Mawson_V3_18_X - Hg0_Mawson_V3_18_MEDIAN
# 3) find the absolute value for the difference
Hg0_Mawson_V3_18_ABS    = Hg0_Mawson_V3_18_X_M.abs()
# 4) find the median of the absolute difference
Hg0_Mawson18_MAD        = Hg0_Mawson_V3_18_ABS.rolling('1h').median()
Hg0_Mawson18_MAD        = Hg0_Mawson18_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_Mawson18_MAD        = np.array(Hg0_Mawson18_MAD[:]) # convert from pandas.df to np.array
Hg0_Mawson18_MAD        = Hg0_Mawson18_MAD[~np.isnan(Hg0_Mawson18_MAD)] # drop the nan values

# V3_17M (Davis)

# 1) Find the median
Hg0_Davis_V3_18.index  = Hg0_Davis_V3_18.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_Davis_V3_18        = Hg0_Davis_V3_18.sort_index()
Hg0_Davis_V3_18_MEDIAN = (Hg0_Davis_V3_18['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_Davis_V3_18_X      = np.array(Hg0_Davis_V3_18['ng/m3'])
Hg0_Davis_V3_18_X_M    = Hg0_Davis_V3_18_X - Hg0_Davis_V3_18_MEDIAN
# 3) find the absolute value for the difference
Hg0_Davis_V3_18_ABS    = Hg0_Davis_V3_18_X_M.abs()
# 4) find the median of the absolute difference
Hg0_Davis18_MAD3       = Hg0_Davis_V3_18_ABS.rolling('1h').median()
Hg0_Davis18_MAD3       = Hg0_Davis18_MAD3.resample('1h').mean() # convert the MAD to a daily value
Hg0_Davis18_MAD3       = np.array(Hg0_Davis18_MAD3[:]) # convert from pandas.df to np.array
Hg0_Davis18_MAD3       = Hg0_Davis18_MAD3[~np.isnan(Hg0_Davis18_MAD3)] # drop the nan values

# V4_17

# 1) Find the median
Hg0_MQIsl_V4_18.index  = Hg0_MQIsl_V4_18.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_MQIsl_V4_18        = Hg0_MQIsl_V4_18.sort_index()
Hg0_MQIsl_V4_18_MEDIAN = (Hg0_MQIsl_V4_18['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_MQIsl_V4_18_X      = np.array(Hg0_MQIsl_V4_18['ng/m3'])
Hg0_MQIsl_V4_18_X_M    = Hg0_MQIsl_V4_18_X - Hg0_MQIsl_V4_18_MEDIAN
# 3) find the absolute value for the difference
Hg0_MQIsl_V4_18_ABS    = Hg0_MQIsl_V4_18_X_M.abs()
# 4) find the median of the absolute difference
Hg0_MQIsl18_MAD        = Hg0_MQIsl_V4_18_ABS.rolling('1h').median()
Hg0_MQIsl18_MAD        = Hg0_MQIsl18_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_MQIsl18_MAD        = np.array(Hg0_MQIsl18_MAD[:]) # convert from pandas.df to np.array
Hg0_MQIsl18_MAD        = Hg0_MQIsl18_MAD[~np.isnan(Hg0_MQIsl18_MAD)] # drop the nan values

# PCAN

# 1) Find the median
Hg0_PCAN_Ice.index = Hg0_PCAN_Ice.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_PCAN_Ice       = Hg0_PCAN_Ice.sort_index()
Hg0_PCAN17_MEDIAN  = (Hg0_PCAN_Ice['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_PCAN17_X       = np.array(Hg0_PCAN_Ice['ng/m3'])
Hg0_PCAN17_X_M     = Hg0_PCAN17_X - Hg0_PCAN17_MEDIAN
# 3) find the absolute value for the difference
Hg0_PCAN17_ABS     = Hg0_PCAN17_X_M.abs()
# 4) find the median of the absolute difference
Hg0_PCAN17_MAD     = Hg0_PCAN17_ABS.rolling('1h').median()
Hg0_PCAN17_MAD     = Hg0_PCAN17_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_PCAN17_MAD     = np.array(Hg0_PCAN17_MAD[:]) # convert from pandas.df to np.array
Hg0_PCAN17_MAD     = Hg0_PCAN17_MAD[~np.isnan(Hg0_PCAN17_MAD)] # drop the nan values

# SIPEXII

# 1) Find the median
Hg0_SIPEXII_Ice.index = Hg0_SIPEXII_Ice.index.map(lambda t: t.replace(year=1900, month=1, day=1))
Hg0_SIPEXII_Ice       = Hg0_SIPEXII_Ice.sort_index()
Hg0_SIPEXII12_MEDIAN  = (Hg0_SIPEXII_Ice['ng/m3'].rolling('1h').median())
# 2) subtract the median from each value in X
Hg0_SIPEXII12_X       = np.array(Hg0_SIPEXII_Ice['ng/m3'])
Hg0_SIPEXII12_X_M     = Hg0_SIPEXII12_X - Hg0_SIPEXII12_MEDIAN
# 3) find the absolute value for the difference
Hg0_SIPEXII12_ABS     = Hg0_SIPEXII12_X_M.abs()
# 4) find the median of the absolute difference
Hg0_SIPEXII12_MAD     = Hg0_SIPEXII12_ABS.rolling('1h').median()
Hg0_SIPEXII12_MAD     = Hg0_SIPEXII12_MAD.resample('1h').mean() # convert the MAD to a daily value
Hg0_SIPEXII12_MAD     = np.array(Hg0_SIPEXII12_MAD[:]) # convert from pandas.df to np.array
Hg0_SIPEXII12_MAD     = Hg0_SIPEXII12_MAD[~np.isnan(Hg0_SIPEXII12_MAD)] # drop the nan values

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()

gs = gridspec.GridSpec(nrows=5,
                       ncols=3, 
                       figure=fig, 
                       width_ratios= [0.33, 0.33, 0.33],
                       height_ratios=[0.2, 0.2, 0.2, 0.2, 0.2],
                       hspace=0.3)

#------------------------------
# Graph 1
ax  = plt.subplot(gs[0,0]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,2,26)  # Earliest sunrise
sunriseL = datetime(1900,1,1,3,26)  # Latest sunrise
sunsetE  = datetime(1900,1,1,23,43) # Earliest sunset
sunsetL  = datetime(1900,1,1,0,41) # Latest sunset
ax.axvspan(sunsetL, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, b, color='grey', alpha=0.4, lw=0)
ax.axvspan(a, sunsetL, color='grey', alpha=0.4, lw=0)

# Plot the variables
ax.plot(time1_HMa,  Hg0_Davis17_HMed1, marker='None', c='black', markersize = 3.0, ls='-', label ='Davis (V1)')
ax2.plot(time1_HMy, BrO_Davis17_HMed1, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time1_HMa, O3_Davis17_HMed1,  marker='None', c='green', markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_Davis17_HMed1,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_Davis17_HMed1,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_Davis17_HMed1, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time1_HMa, Hg0_Davis17_H5P1,  'b-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time1_HMa, Hg0_Davis17_H25P1, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time1_HMa, Hg0_Davis17_H75P1, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time1_HMa, Hg0_Davis17_H95P1, 'b-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time1_HMa, Hg0_Davis17_H25P1, Hg0_Davis17_H75P1, facecolor='blue', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax.spines["right"].set_color('blue')
# ax.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.set_ylim(5,30)
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax2.set_ylabel('BrO (pptv)',   fontsize=15)
# ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 2
ax  = plt.subplot(gs[1,0]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
sunrise = datetime(1900,1,1,4,15)
sunset  = datetime(1900,1,1,3,10)
ax.axvspan(sunset, sunrise, color='grey', alpha=0.4, lw=0)

# Plot the variables
ax.plot(time1_HMa,  Hg0_Casey17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='Casey (V2)')
ax2.plot(time2_HMy, BrO_Casey17_HMed, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time2_HMa, O3_Casey17_HMed,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_Casey17_HMed,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_Casey17_HMed,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_Casey17_HMed, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time2_HMa, Hg0_Casey17_H5P,  'b-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time2_HMa, Hg0_Casey17_H25P, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time2_HMa, Hg0_Casey17_H75P, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time2_HMa, Hg0_Casey17_H95P, 'b-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time2_HMa, Hg0_Casey17_H25P, Hg0_Casey17_H75P, facecolor='blue', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax.spines["right"].set_color('blue')
# ax.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax2.set_ylabel('BrO (pptv)',   fontsize=15)
# ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 3
ax  = plt.subplot(gs[2,0]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,3,32)  # Earliest sunrise
sunriseL = datetime(1900,1,1,4,46)  # Latest sunrise
sunsetE  = datetime(1900,1,1,21,15) # Earliest sunset
sunsetL  = datetime(1900,1,1,22,27) # Latest sunset
ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# Plot the variables
ax.plot(time3_HMa,  Hg0_Mawson17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='Mawson (V3)')
ax2.plot(time3_HMy, BrO_Mawson17_HMed, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time3_HMa, O3_Mawson17_HMed,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_Mawson17_HMed,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_Mawson17_HMed,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_Mawson17_HMed, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time3_HMa, Hg0_Mawson17_H5P,  'b-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time3_HMa, Hg0_Mawson17_H25P, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time3_HMa, Hg0_Mawson17_H75P, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time3_HMa, Hg0_Mawson17_H95P, 'b-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time3_HMa, Hg0_Mawson17_H25P, Hg0_Mawson17_H75P, facecolor='blue', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax.spines["right"].set_color('blue')
# ax.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax2.set_ylabel('BrO (pptv)',   fontsize=15)
# ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 4
ax  = plt.subplot(gs[3,0]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,3,45)  # Earliest sunrise
sunriseL = datetime(1900,1,1,5,46)  # Latest sunrise
sunsetE  = datetime(1900,1,1,22,4) # Earliest sunset
sunsetL  = datetime(1900,1,1,0,17) # Latest sunset
ax.axvspan(a,sunsetL, color='grey', alpha=0.4, lw=0) # dark shade
ax.axvspan(sunsetL, sunriseE, color='grey', alpha=0.7, lw=0) # light shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, b, color='grey', alpha=0.4, lw=0)

# Plot the variables
ax.plot(time4_HMa,  Hg0_Davis17_HMed3, marker='None', c='black', markersize = 3.0, ls='-', label ='Davis (V3)')
ax2.plot(time4_HMy, BrO_Davis17_HMed3, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time4_HMa, O3_Davis17_HMed3,  marker='None', c='green', markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_Davis17_HMed3,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_Davis17_HMed3,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_Davis17_HMed3, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time4_HMa, Hg0_Davis17_H5P3,  'b-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time4_HMa, Hg0_Davis17_H25P3, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time4_HMa, Hg0_Davis17_H75P3, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time4_HMa, Hg0_Davis17_H95P3, 'b-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time4_HMa, Hg0_Davis17_H25P3, Hg0_Davis17_H75P3, facecolor='blue', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax.spines["right"].set_color('blue')
# ax.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.set_ylim(5,30)
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
# ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax2.set_ylabel('BrO (pptv)',   fontsize=15)
# ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 5
ax  = plt.subplot(gs[4,0]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,6,8)  # Earliest sunrise
sunriseL = datetime(1900,1,1,6,24)  # Latest sunrise
sunsetE  = datetime(1900,1,1,18,28) # Earliest sunset
sunsetL  = datetime(1900,1,1,18,58) # Latest sunset
ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# Plot the variables
ax.plot(time5_HMa,  Hg0_MQIsl17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='Macquarie Island (V4)')
ax3.plot(time5_HMa, O3_MQIsl17_HMed,  marker='None', c='green', markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_MQIsl17_HMed,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_MQIsl17_HMed,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_MQIsl17_HMed, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time5_HMa, Hg0_MQIsl17_H5P,  'b-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time5_HMa, Hg0_MQIsl17_H25P, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time5_HMa, Hg0_MQIsl17_H75P, 'b-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time5_HMa, Hg0_MQIsl17_H95P, 'b-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time5_HMa, Hg0_MQIsl17_H25P, Hg0_MQIsl17_H75P, facecolor='blue', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='blue', labelsize=10)
# ax.spines["right"].set_color('blue')
# ax.yaxis.label.set_color('blue')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.set_ylim(5,30)
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
#ax2.set_ylabel('BrO (pptv)',   fontsize=15)
#ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 6
ax  = plt.subplot(gs[0,1]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,3,21)  # Earliest sunrise
sunriseL = datetime(1900,1,1,4,6)  # Latest sunrise
sunsetE  = datetime(1900,1,1,23,0) # Earliest sunset
sunsetL  = datetime(1900,1,1,23,48) # Latest sunset
ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# Plot the variables
ax.plot(time6_HMa,  Hg0_Davis18_HMed1, marker='None', c='black', markersize = 3.0, ls='-', label ='Davis (V1)')
ax2.plot(time6_HMy, BrO_Davis18_HMed1, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time6_HMa, O3_Davis18_HMed1,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_Davis18_HMed1,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_Davis18_HMed1,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_Davis18_HMed1, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time6_HMa, Hg0_Davis18_H5P1,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time6_HMa, Hg0_Davis18_H25P1, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time6_HMa, Hg0_Davis18_H75P1, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time6_HMa, Hg0_Davis18_H95P1, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time6_HMa, Hg0_Davis18_H25P1, Hg0_Davis18_H75P1, facecolor='red', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax.spines["right"].set_color('red')
# ax.yaxis.label.set_color('red')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
# ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax2.set_ylabel('BrO (pptv)',   fontsize=15)
# ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 7
ax  = plt.subplot(gs[1,1]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Plot the variables
ax.plot(time7_HMa,  Hg0_Casey18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='Casey (V2)')
ax2.plot(time7_HMy, BrO_Casey18_HMed, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time7_HMa, O3_Casey18_HMed,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_Casey18_HMed,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_Casey18_HMed,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_Casey18_HMed, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time7_HMa, Hg0_Casey18_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time7_HMa, Hg0_Casey18_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time7_HMa, Hg0_Casey18_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time7_HMa, Hg0_Casey18_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time7_HMa, Hg0_Casey18_H25P, Hg0_Casey18_H75P, facecolor='red', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='red', labelsize=10)
# ax.spines["right"].set_color('red')
# ax.yaxis.label.set_color('red')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
# ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
#ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
ax2.set_ylabel('BrO (pptv)',   fontsize=15)
ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 8
ax  = plt.subplot(gs[2,1]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,3,21)  # Earliest sunrise
sunriseL = datetime(1900,1,1,4,10)  # Latest sunrise
sunsetE  = datetime(1900,1,1,21,51) # Earliest sunset
sunsetL  = datetime(1900,1,1,22,37) # Latest sunset
ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# Plot the variables
ax.plot(time8_HMa,  Hg0_Mawson18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='Mawson (V3)')
ax2.plot(time8_HMy, BrO_Mawson18_HMed, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time8_HMa, O3_Mawson18_HMed,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_Mawson18_HMed,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_Mawson18_HMed,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_Mawson18_HMed, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time8_HMa, Hg0_Mawson18_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time8_HMa, Hg0_Mawson18_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time8_HMa, Hg0_Mawson18_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time8_HMa, Hg0_Mawson18_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time8_HMa, Hg0_Mawson18_H25P, Hg0_Mawson18_H75P, facecolor='red', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax.spines["right"].set_color('red')
# ax.yaxis.label.set_color('red')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
#ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
ax2.set_ylabel('BrO (pptv)',   fontsize=15)
ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 9
ax  = plt.subplot(gs[3,1]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,3,36)  # Earliest sunrise
sunriseL = datetime(1900,1,1,5,50)  # Latest sunrise
sunsetE  = datetime(1900,1,1,22,9) # Earliest sunset
sunsetL  = datetime(1900,1,1,0,25) # Latest sunset
ax.axvspan(a, sunsetL, color='grey', alpha=0.4, lw=0) # dark shade
ax.axvspan(sunsetL, sunriseE, color='grey', alpha=0.7, lw=0) # light shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0)
ax.axvspan(sunsetE, b, color='grey', alpha=0.4, lw=0)

# Plot the variables
ax.plot(time9_HMa,  Hg0_Davis18_HMed3, marker='None', c='black', markersize = 3.0, ls='-', label ='Davis (V3)')
ax2.plot(time9_HMy, BrO_Davis18_HMed3, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time9_HMa, O3_Davis18_HMed3,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_Davis18_HMed3,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_Davis18_HMed3,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_Davis18_HMed3, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time9_HMa, Hg0_Davis18_H5P3,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time9_HMa, Hg0_Davis18_H25P3, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time9_HMa, Hg0_Davis18_H75P3, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time9_HMa, Hg0_Davis18_H95P3, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time9_HMa, Hg0_Davis18_H25P3, Hg0_Davis18_H75P3, facecolor='red', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='red', labelsize=10)
# ax.spines["right"].set_color('red')
# ax.yaxis.label.set_color('red')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
# ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
# ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax2.set_ylabel('BrO (pptv)',   fontsize=15)
# ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 10
ax  = plt.subplot(gs[4,1]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,6,0)  # Earliest sunrise
sunriseL = datetime(1900,1,1,6,27)  # Latest sunrise
sunsetE  = datetime(1900,1,1,18,33) # Earliest sunset
sunsetL  = datetime(1900,1,1,19,8) # Latest sunset
ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# Plot the variables
ax.plot(time10_HMa,  Hg0_MQIsl18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='Macquarie Island (V4)')
ax3.plot(time10_HMa, O3_MQIsl18_HMed,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_MQIsl18_HMed,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_MQIsl18_HMed,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_MQIsl18_HMed, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time10_HMa, Hg0_MQIsl18_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time10_HMa, Hg0_MQIsl18_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time10_HMa, Hg0_MQIsl18_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time10_HMa, Hg0_MQIsl18_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time10_HMa, Hg0_MQIsl18_H25P, Hg0_MQIsl18_H75P, facecolor='red', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='red', labelsize=10)
ax.spines["right"].set_color('red')
# ax.yaxis.label.set_color('red')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
#ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
#ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
ax2.set_ylabel('BrO (pptv)',   fontsize=15)
ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 11
ax  = plt.subplot(gs[0,2]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,3,26)  # Earliest sunrise
sunriseL = datetime(1900,1,1,5,40)  # Latest sunrise
sunsetE  = datetime(1900,1,1,17,57) # Earliest sunset
sunsetL  = datetime(1900,1,1,20,40) # Latest sunset
ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# Plot the variables
ax.plot(time12_HMa,  Hg0_SIPEXII12_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='SIPEXII (2012)')
ax2.plot(time12_HMy, BrO_SIPEXII12_HMed, marker='None', c='magenta',  markersize = 3.0, ls='-')
ax3.plot(time12_HMa, O3_SIPEXII12_HMed,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_SIPEXII12_HMed,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_SIPEXII12_HMed,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_SIPEXII12_HMed, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time11_HMa, Hg0_SIPEXII12_H5P,  c='cyan', ls='-', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time11_HMa, Hg0_SIPEXII12_H25P, c='cyan', ls='-', linewidth=2, alpha=0.7, label='_nolegend_')
#ax.plot(time11_HMa, Hg0_SIPEXII12_H75P, c='cyan', ls='-', linewidth=2, alpha=0.7, label='_nolegend_')
ax.plot(time11_HMa, Hg0_SIPEXII12_H95P, c='cyan', ls='-', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time11_HMa, Hg0_SIPEXII12_H25P, Hg0_SIPEXII12_H75P, facecolor='cyan', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='cyan', labelsize=10)
ax.spines["right"].set_color('cyan')
# ax.yaxis.label.set_color('cyan')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
#ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
ax2.set_ylabel('BrO (pptv)',   fontsize=15)
ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 12
ax  = plt.subplot(gs[3,2]) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax4 = ax.twinx()
# ax5 = ax.twinx()
# ax6 = ax.twinx()

# Shade betwen sunset and sunrise 
a = datetime(1900,1,1,0,0)
b = datetime(1900,1,1,23,59,0)
sunriseE = datetime(1900,1,1,3,13)  # Earliest sunrise
sunriseL = datetime(1900,1,1,4,6)  # Latest sunrise
sunsetE  = datetime(1900,1,1,19,48) # Earliest sunset
sunsetL  = datetime(1900,1,1,21,42) # Latest sunset
ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# Plot the variables
ax.plot(time1_HMa,  Hg0_PCAN17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='PCAN (2017)')
ax3.plot(time1_HMa, O3_PCAN17_HMed,  marker='None', c='green',  markersize = 3.0, ls='-')

# ax4.plot(time1_HMa, RH_PCAN17_HMed,   marker='None', c='orange',  markersize = 3.0, ls='-')
# ax5.plot(time1_HMa, SR_PCAN17_HMed,   marker='None', c='magenta', markersize = 3.0, ls='-')
# ax6.plot(time1_HMa, Temp_PCAN17_HMed, marker='None', c='red',     markersize = 3.0, ls='-')

# Plot the percentiles
ax.plot(time1_HMa, Hg0_PCAN17_H5P, ls='-', c='orange', linewidth=1, alpha=0.7, label='_nolegend_')
#ax.plot(time12_HMa, Hg0_PCAN17_H25P, ls='-', c='orange', linewidth=2, alpha=0.3, label='_nolegend_')
#ax.plot(time12_HMa, Hg0_PCAN17_H75P, ls='-', c='orange', linewidth=2, alpha=0.3, label='_nolegend_')
ax.plot(time1_HMa, Hg0_PCAN17_H95P, ls='-', c='orange', linewidth=1, alpha=0.7, label='_nolegend_')
ax.fill_between(time1_HMa, Hg0_PCAN17_H25P, Hg0_PCAN17_H75P, facecolor='orange', alpha=0.7) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.5) # On Station
ax.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax.spines["right"].set_color('orange')
# ax.yaxis.label.set_color('orange')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,7)
ax2.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax2.spines["right"].set_color('magenta')
# ax2.yaxis.label.set_color('magenta')

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.spines["right"].set_position(("axes", 1.13))
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.set_ylim(5,30)
ax3.spines["right"].set_color('green')
# ax3.yaxis.label.set_color('green')

# Plot the axis labels, legend and title
#ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
ax2.set_ylabel('BrO (pptv)',   fontsize=15)
ax3.set_ylabel('O$_3$ (ppb)',      fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

# #------------------------------------------------------------------------------
# # PLOT THE GRAPH
# fig = plt.figure()

# gs = gridspec.GridSpec(nrows=4,
#                        ncols=3, 
#                        figure=fig, 
#                        width_ratios= [0.33, 0.33, 0.33],
#                        height_ratios=[0.2, 0.2, 0.2, 0.2],
#                        hspace=0.3)

# #------------------------------
# # Graph 1
# ax=plt.subplot(gs[0,0]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,2,26)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,3,26)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,23,43) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,0,41) # Latest sunset
# # ax.axvspan(sunsetL, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, b, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(a, sunsetL, color='grey', alpha=0.4, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_Ice_V1_17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V1 (2017-18))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_Ice_V1_17_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V1_17_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V1_17_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_Ice_V1_17_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_Ice_V1_17_H25P, Hg0_Ice_V1_17_H75P, facecolor='red', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 2
# ax=plt.subplot(gs[0,1]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # sunrise = datetime(1900,1,1,4,15)
# # sunset  = datetime(1900,1,1,3,10)
# # ax.axvspan(sunset, sunrise, color='grey', alpha=0.4, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_Ice_V2_17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V2 (2017-18))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_Ice_V2_17_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V2_17_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V2_17_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_Ice_V2_17_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_Ice_V2_17_H25P, Hg0_Ice_V2_17_H75P, facecolor='red', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 3
# ax=plt.subplot(gs[0,2]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,3,32)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,4,46)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,21,15) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,22,27) # Latest sunset
# # ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_Ice_V3_17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V3 (2017-18))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_Ice_V3_17_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V3_17_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V3_17_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_Ice_V3_17_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_Ice_V3_17_H25P, Hg0_Ice_V3_17_H75P, facecolor='red', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 4
# ax=plt.subplot(gs[1,0]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,3,45)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,5,46)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,22,4) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,0,17) # Latest sunset
# # ax.axvspan(a,sunsetL, color='grey', alpha=0.4, lw=0) # dark shade
# # ax.axvspan(sunsetL, sunriseE, color='grey', alpha=0.7, lw=0) # light shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, b, color='grey', alpha=0.4, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_OW_V1_17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V1 (2017-18))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_OW_V1_17_H5P,  'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V1_17_H25P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V1_17_H75P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_OW_V1_17_H95P, 'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_OW_V1_17_H25P, Hg0_OW_V1_17_H75P, facecolor='green', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 5
# ax=plt.subplot(gs[1,1]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,6,8)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,6,24)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,18,28) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,18,58) # Latest sunset
# # ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_OW_V2_17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V2 (2017-18))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_OW_V2_17_H5P,  'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V2_17_H25P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V2_17_H75P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_OW_V2_17_H95P, 'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_OW_V2_17_H25P, Hg0_OW_V2_17_H75P, facecolor='green', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 6
# ax=plt.subplot(gs[1,2]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,3,21)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,4,6)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,23,0) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,23,48) # Latest sunset
# # ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_OW_V3_17_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V3 (2017-18))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_OW_V3_17_H5P,  'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V3_17_H25P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V3_17_H75P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_OW_V3_17_H95P, 'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_OW_V3_17_H25P, Hg0_OW_V3_17_H75P, facecolor='green', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# #ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 7
# ax=plt.subplot(gs[2,0]) # options graph 1 (vertical no, horizontal no, graph no)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_Ice_V1_18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V1 (2018-19))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_Ice_V1_18_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V1_18_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V1_18_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_Ice_V1_18_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_Ice_V1_18_H25P, Hg0_Ice_V1_18_H75P, facecolor='red', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# #ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 8
# ax=plt.subplot(gs[2,1]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,3,21)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,4,10)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,21,51) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,22,37) # Latest sunset
# # ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_Ice_V2_18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V2 (2018-19))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_Ice_V2_18_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V2_18_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V2_18_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_Ice_V2_18_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_Ice_V2_18_H25P, Hg0_Ice_V2_18_H75P, facecolor='red', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# #ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 9
# ax=plt.subplot(gs[2,2]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,3,36)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,5,50)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,22,9) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,0,25) # Latest sunset
# # ax.axvspan(a, sunsetL, color='grey', alpha=0.4, lw=0) # dark shade
# # ax.axvspan(sunsetL, sunriseE, color='grey', alpha=0.7, lw=0) # light shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(sunsetE, b, color='grey', alpha=0.4, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_Ice_V3_18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V3 (2018-19))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_Ice_V3_18_H5P,  'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V3_18_H25P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_Ice_V3_18_H75P, 'r-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_Ice_V3_18_H95P, 'r-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_Ice_V3_18_H25P, Hg0_Ice_V3_18_H75P, facecolor='red', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# #ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 10
# ax=plt.subplot(gs[3,0]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,6,0)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,6,27)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,18,33) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,19,8) # Latest sunset
# # ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_OW_V1_18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V1 (2018-19))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_OW_V1_18_H5P,  'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V1_18_H25P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V1_18_H75P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_OW_V1_18_H95P, 'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_OW_V1_18_H25P, Hg0_OW_V1_18_H75P, facecolor='green', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# #ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

# #------------------------------
# # Graph 11
# ax=plt.subplot(gs[3,1]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,3,26)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,5,40)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,17,57) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,20,40) # Latest sunset
# # ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_OW_V2_18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V2 (2018-19))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_OW_V2_18_H5P,  'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V2_18_H25P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V2_18_H75P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_OW_V2_18_H95P, 'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_OW_V2_18_H25P, Hg0_OW_V2_18_H75P, facecolor='green', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# #ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# #ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='lower left')

# #------------------------------
# # Graph 12
# ax=plt.subplot(gs[3,2]) # options graph 1 (vertical no, horizontal no, graph no)

# # # Shade betwen sunset and sunrise 
# # a = datetime(1900,1,1,0,0)
# # b = datetime(1900,1,1,23,59,0)
# # sunriseE = datetime(1900,1,1,3,13)  # Earliest sunrise
# # sunriseL = datetime(1900,1,1,4,6)  # Latest sunrise
# # sunsetE  = datetime(1900,1,1,19,48) # Earliest sunset
# # sunsetL  = datetime(1900,1,1,21,42) # Latest sunset
# # ax.axvspan(a, sunriseE, color='grey', alpha=0.7, lw=0) # dark shade
# # ax.axvspan(sunriseE, sunriseL, color='grey', alpha=0.4, lw=0) # light shade
# # ax.axvspan(sunsetE, sunsetL, color='grey', alpha=0.4, lw=0)
# # ax.axvspan(sunsetL, b, color='grey', alpha=0.7, lw=0)

# # Plot the variables
# ax.plot(time1_HMa, Hg0_OW_V3_18_HMed, marker='None', c='black', markersize = 3.0, ls='-', label ='V3 (2018-19))')

# # Plot the percentiles
# ax.plot(time1_HMa, Hg0_OW_V3_18_H5P,  'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V3_18_H25P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# #ax.plot(time1_HMa, Hg0_OW_V3_18_H75P, 'g-', linewidth=2, alpha=0.7, label='_nolegend_')
# ax.plot(time1_HMa, Hg0_OW_V3_18_H95P, 'g-', linewidth=1, alpha=0.7, label='_nolegend_')
# ax.fill_between(time1_HMa, Hg0_OW_V3_18_H25P, Hg0_OW_V3_18_H75P, facecolor='green', alpha=0.7) # fill the distribution

# # Plot the MAD
# #UL1 = Hg0_Davis17_HMed1 + Hg0_Davis17_MAD1 # find the upper limit
# #LL1 = Hg0_Davis17_HMed1 - Hg0_Davis17_MAD1 # find the lower limit
# #ax.plot(time1_HMa, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
# #ax.plot(time1_HMa, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
# #ax.fill_between(time1_HMa, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# # Format x-axis
# #plt.xticks(rotation=45)
# xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# #xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_minor_formatter(xminor_formatter)
# ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
# #ax2.axes.get_xaxis().set_visible(False)

# # Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.3,0.7) # All
# ax.set_ylim(0,1.5) # On Station
# plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# # Plot the axis labels, legend and title
# #ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
# ax.set_xlabel('Time (hours)', fontsize=15)
# #Plot the legend and title
# #plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
# #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN 2017-18)
fig = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=4, 
                       figure=fig, 
                       width_ratios= [0.25, 0.25, 0.25, 0.25],
                       height_ratios=[0.5, 0.5],
                       hspace=0.3)

#------------------------------
# Graph 1 (Hg0)
ax  = plt.subplot(gs[0,0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  Hg0_Davis17_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time1_HMa,  Hg0_Casey17_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time1_HMa,  Hg0_Mawson17_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time1_HMa,  Hg0_Davis17_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, Hg0_Davis17_H25P1, Hg0_Davis17_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_Casey17_H25P,  Hg0_Casey17_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_Mawson17_H25P, Hg0_Mawson17_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_Davis17_H25P3, Hg0_Davis17_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# # Plot the variables
# ax.plot(time1_HMa,  Hg0_Davis17_HM1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
# ax.plot(time1_HMa,  Hg0_Casey17_HM,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
# ax.plot(time1_HMa,  Hg0_Mawson17_HM, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
# ax.plot(time1_HMa,  Hg0_Davis17_HM3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# # Upper Limit
# UL1 = Hg0_Davis17_HM1 + Hg0_Davis17_HSTD1 # find the upper limit
# UL2 = Hg0_Casey17_HM  + Hg0_Casey17_HSTD  # find the upper limit
# UL3 = Hg0_Mawson17_HM + Hg0_Mawson17_HSTD # find the upper limit
# UL4 = Hg0_Davis17_HM3 + Hg0_Davis17_HSTD3 # find the upper limit

# # Lower Limit
# LL1 = Hg0_Davis17_HM1 - Hg0_Davis17_HSTD1 # find the lower limit
# LL2 = Hg0_Casey17_HM  - Hg0_Casey17_HSTD  # find the lower limit
# LL3 = Hg0_Mawson17_HM - Hg0_Mawson17_HSTD # find the lower limit
# LL4 = Hg0_Davis17_HM3 - Hg0_Davis17_HSTD3 # find the lower limit

# # Plot the percentiles
# ax.fill_between(time1_HMa, UL1, LL1, facecolor='red',     alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL2, LL2,  facecolor='green',   alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL3, LL3, facecolor='blue',    alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL4, LL4, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax.set_ylim(0.3,0.7) # All
ax.set_ylim(0.2,0.8) # On Station
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Plot the axis labels, legend and title
ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 2 (BrO)
ax  = plt.subplot(gs[0,1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMy,  BrO_Davis17_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMy,  BrO_Casey17_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMy,  BrO_Mawson17_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMy,  BrO_Davis17_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMy, BrO_Davis17_H25P1, BrO_Davis17_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMy, BrO_Casey17_H25P,  BrO_Casey17_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMy, BrO_Mawson17_H25P, BrO_Mawson17_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMy, BrO_Davis17_H25P3, BrO_Davis17_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(1,7)

# Plot the axis labels, legend and title
#ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
ax.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 3 (O3)
ax  = plt.subplot(gs[0,2]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  O3_Davis17_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  O3_Casey17_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  O3_Mawson17_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  O3_Davis17_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, O3_Davis17_H25P1, O3_Davis17_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, O3_Casey17_H25P,  O3_Casey17_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, O3_Mawson17_H25P, O3_Mawson17_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, O3_Davis17_H25P3, O3_Davis17_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(5,25)

# Plot the axis labels, legend and title
ax.set_ylabel('O$_3$ (ppm)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 4 (RH)
ax  = plt.subplot(gs[0,3]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  RH_Davis17_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  RH_Casey17_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  RH_Mawson17_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  RH_Davis17_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, RH_Davis17_H25P1, RH_Davis17_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, RH_Casey17_H25P,  RH_Casey17_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, RH_Mawson17_H25P, RH_Mawson17_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, RH_Davis17_H25P3, RH_Davis17_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(35,95)

# Plot the axis labels, legend and title
ax.set_ylabel('RH (%)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 5 (Wind Speed)
ax  = plt.subplot(gs[1,0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  WS_Davis17_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  WS_Casey17_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  WS_Mawson17_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  WS_Davis17_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, WS_Davis17_H25P1, WS_Davis17_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, WS_Casey17_H25P,  WS_Casey17_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, WS_Mawson17_H25P, WS_Mawson17_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, WS_Davis17_H25P3, WS_Davis17_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,20)

# Plot the axis labels, legend and title
ax.set_ylabel('Wind Speed (m/s)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 6 (Temp)
ax  = plt.subplot(gs[1,1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  Temp_Davis17_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  Temp_Casey17_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  Temp_Mawson17_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  Temp_Davis17_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, Temp_Davis17_H25P1, Temp_Davis17_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, Temp_Casey17_H25P,  Temp_Casey17_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, Temp_Mawson17_H25P, Temp_Mawson17_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, Temp_Davis17_H25P3, Temp_Davis17_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(-10,5)

# Plot the axis labels, legend and title
ax.set_ylabel('Temp (C)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 7 (SolRad)
ax  = plt.subplot(gs[1,2]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  SR_Davis17_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  SR_Casey17_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  SR_Mawson17_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  SR_Davis17_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, SR_Davis17_H25P1, SR_Davis17_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, SR_Casey17_H25P,  SR_Casey17_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, SR_Mawson17_H25P, SR_Mawson17_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, SR_Davis17_H25P3, SR_Davis17_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,1300)

# Plot the axis labels, legend and title
ax.set_ylabel('SolRad (W/M$^2$)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)

#------------------------------
# Plot the legend
lg = ax.legend(bbox_to_anchor=(1.15, 0.75), loc=2, borderaxespad=0.,title='Voyage',fontsize=15)
lg.get_title().set_fontsize(15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN 2018-19)
fig = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=4, 
                       figure=fig, 
                       width_ratios= [0.25, 0.25, 0.25, 0.25],
                       height_ratios=[0.5, 0.5],
                       hspace=0.3)

#------------------------------
# Graph 1 (Hg0)
ax  = plt.subplot(gs[0,0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  Hg0_Davis18_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time1_HMa,  Hg0_Casey18_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time1_HMa,  Hg0_Mawson18_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time1_HMa,  Hg0_Davis18_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, Hg0_Davis18_H25P1, Hg0_Davis18_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_Casey18_H25P,  Hg0_Casey18_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_Mawson18_H25P, Hg0_Mawson18_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_Davis18_H25P3, Hg0_Davis18_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# # Plot the variables
# ax.plot(time1_HMa,  Hg0_Davis17_HM1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
# ax.plot(time1_HMa,  Hg0_Casey17_HM,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
# ax.plot(time1_HMa,  Hg0_Mawson17_HM, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
# ax.plot(time1_HMa,  Hg0_Davis17_HM3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# # Upper Limit
# UL1 = Hg0_Davis17_HM1 + Hg0_Davis17_HSTD1 # find the upper limit
# UL2 = Hg0_Casey17_HM  + Hg0_Casey17_HSTD  # find the upper limit
# UL3 = Hg0_Mawson17_HM + Hg0_Mawson17_HSTD # find the upper limit
# UL4 = Hg0_Davis17_HM3 + Hg0_Davis17_HSTD3 # find the upper limit

# # Lower Limit
# LL1 = Hg0_Davis17_HM1 - Hg0_Davis17_HSTD1 # find the lower limit
# LL2 = Hg0_Casey17_HM  - Hg0_Casey17_HSTD  # find the lower limit
# LL3 = Hg0_Mawson17_HM - Hg0_Mawson17_HSTD # find the lower limit
# LL4 = Hg0_Davis17_HM3 - Hg0_Davis17_HSTD3 # find the lower limit

# # Plot the percentiles
# ax.fill_between(time1_HMa, UL1, LL1, facecolor='red',     alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL2, LL2,  facecolor='green',   alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL3, LL3, facecolor='blue',    alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL4, LL4, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax.set_ylim(0.3,0.7) # All
ax.set_ylim(0.1,0.8) # On Station
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Plot the axis labels, legend and title
ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 2 (BrO)
ax  = plt.subplot(gs[0,1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time6_HMy,  BrO_Davis18_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time7_HMy,  BrO_Casey18_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time8_HMy,  BrO_Mawson18_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time9_HMy,  BrO_Davis18_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time6_HMy, BrO_Davis18_H25P1, BrO_Davis18_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time7_HMy, BrO_Casey18_H25P,  BrO_Casey18_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time8_HMy, BrO_Mawson18_H25P, BrO_Mawson18_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time9_HMy, BrO_Davis18_H25P3, BrO_Davis18_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.set_ylim(1.5,5.5)

# Plot the axis labels, legend and title
#ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
ax.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 3 (O3)
ax  = plt.subplot(gs[0,2]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  O3_Davis18_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  O3_Casey18_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  O3_Mawson18_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  O3_Davis18_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, O3_Davis18_H25P1, O3_Davis18_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, O3_Casey18_H25P,  O3_Casey18_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, O3_Mawson18_H25P, O3_Mawson18_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, O3_Davis18_H25P3, O3_Davis18_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(11,28)

# Plot the axis labels, legend and title
ax.set_ylabel('O$_3$ (ppm)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 4 (RH)
ax  = plt.subplot(gs[0,3]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  RH_Davis18_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  RH_Casey18_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  RH_Mawson18_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  RH_Davis18_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, RH_Davis18_H25P1, RH_Davis18_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, RH_Casey18_H25P,  RH_Casey18_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, RH_Mawson18_H25P, RH_Mawson18_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, RH_Davis18_H25P3, RH_Davis18_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(40,100)

# Plot the axis labels, legend and title
ax.set_ylabel('RH (%)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 5 (Wind Speed)
ax  = plt.subplot(gs[1,0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  WS_Davis18_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  WS_Casey18_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  WS_Mawson18_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  WS_Davis18_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, WS_Davis18_H25P1, WS_Davis18_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, WS_Casey18_H25P,  WS_Casey18_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, WS_Mawson18_H25P, WS_Mawson18_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, WS_Davis18_H25P3, WS_Davis18_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,15)

# Plot the axis labels, legend and title
ax.set_ylabel('Wind Speed (m/s)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 6 (Temp)
ax  = plt.subplot(gs[1,1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  Temp_Davis18_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  Temp_Casey18_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  Temp_Mawson18_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  Temp_Davis18_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, Temp_Davis18_H25P1, Temp_Davis18_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, Temp_Casey18_H25P,  Temp_Casey18_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, Temp_Mawson18_H25P, Temp_Mawson18_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, Temp_Davis18_H25P3, Temp_Davis18_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(-13,2)

# Plot the axis labels, legend and title
ax.set_ylabel('Temp (C)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 7 (SolRad)
ax  = plt.subplot(gs[1,2]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  SR_Davis18_HMed1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
ax.plot(time2_HMa,  SR_Casey18_HMed,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
ax.plot(time3_HMa,  SR_Mawson18_HMed, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
ax.plot(time4_HMa,  SR_Davis18_HMed3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# Plot the percentiles
ax.fill_between(time1_HMa, SR_Davis18_H25P1, SR_Davis18_H75P1, facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, SR_Casey18_H25P,  SR_Casey18_H75P,  facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, SR_Mawson18_H25P, SR_Mawson18_H75P, facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, SR_Davis18_H25P3, SR_Davis18_H75P3, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,1000)

# Plot the axis labels, legend and title
ax.set_ylabel('SolRad (W/M$^2$)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)

#------------------------------
# Plot the legend
lg = ax.legend(bbox_to_anchor=(1.15, 0.75), loc=2, borderaxespad=0.,title='Voyage',fontsize=15)
lg.get_title().set_fontsize(15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (MQIsl, PCAN, SIPEXII)
fig = plt.figure()

gs = gridspec.GridSpec(nrows=2,
                       ncols=4, 
                       figure=fig, 
                       width_ratios= [0.25, 0.25, 0.25, 0.25],
                       height_ratios=[0.5, 0.5],
                       hspace=0.3)

#------------------------------
# Graph 1 (Hg0)
ax  = plt.subplot(gs[0,0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  Hg0_MQIsl17_HMed,   marker='None', c='red',     markersize = 3.0, ls='-', label ='Maq Isl (2017/18)')
ax.plot(time1_HMa,  Hg0_MQIsl18_HMed,   marker='None', c='green',   markersize = 3.0, ls='-', label ='Maq Isl (2018/19)')
ax.plot(time1_HMa,  Hg0_PCAN17_HMed,    marker='None', c='blue',    markersize = 3.0, ls='-', label ='PCAN (2017)')
ax.plot(time1_HMa,  Hg0_SIPEXII12_HMed, marker='None', c='magenta', markersize = 3.0, ls='-', label ='SIPEXII (2012)')

# Plot the percentiles
ax.fill_between(time1_HMa, Hg0_MQIsl17_H25P,   Hg0_MQIsl17_H75P,   facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_MQIsl18_H25P,   Hg0_MQIsl18_H75P,   facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_PCAN17_H25P,    Hg0_PCAN17_H75P,    facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time1_HMa, Hg0_SIPEXII12_H25P, Hg0_SIPEXII12_H75P, facecolor='magenta', alpha=0.2) # fill the distribution

# # Plot the variables
# ax.plot(time1_HMa,  Hg0_Davis17_HM1, marker='None', c='red',     markersize = 3.0, ls='-', label ='Davis (V1)')
# ax.plot(time1_HMa,  Hg0_Casey17_HM,  marker='None', c='green',   markersize = 3.0, ls='-', label ='Casey (V2)')
# ax.plot(time1_HMa,  Hg0_Mawson17_HM, marker='None', c='blue',    markersize = 3.0, ls='-', label ='Mawson (V3)')
# ax.plot(time1_HMa,  Hg0_Davis17_HM3, marker='None', c='magenta', markersize = 3.0, ls='-', label ='Davis (V3)')

# # Upper Limit
# UL1 = Hg0_Davis17_HM1 + Hg0_Davis17_HSTD1 # find the upper limit
# UL2 = Hg0_Casey17_HM  + Hg0_Casey17_HSTD  # find the upper limit
# UL3 = Hg0_Mawson17_HM + Hg0_Mawson17_HSTD # find the upper limit
# UL4 = Hg0_Davis17_HM3 + Hg0_Davis17_HSTD3 # find the upper limit

# # Lower Limit
# LL1 = Hg0_Davis17_HM1 - Hg0_Davis17_HSTD1 # find the lower limit
# LL2 = Hg0_Casey17_HM  - Hg0_Casey17_HSTD  # find the lower limit
# LL3 = Hg0_Mawson17_HM - Hg0_Mawson17_HSTD # find the lower limit
# LL4 = Hg0_Davis17_HM3 - Hg0_Davis17_HSTD3 # find the lower limit

# # Plot the percentiles
# ax.fill_between(time1_HMa, UL1, LL1, facecolor='red',     alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL2, LL2,  facecolor='green',   alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL3, LL3, facecolor='blue',    alpha=0.2) # fill the distribution
# ax.fill_between(time1_HMa, UL4, LL4, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax.set_ylim(0.3,0.7) # All
ax.set_ylim(0.2,1.2) # On Station
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Plot the axis labels, legend and title
ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 2 (BrO)
ax  = plt.subplot(gs[0,1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
#ax.plot(time5_HMy,  BrO_MQIsl17_HMed,   marker='None', c='red',     markersize = 3.0, ls='-', label ='Maq Isl (2017/18)')
#x.plot(time10_HMy, BrO_MQIsl18_HMed,   marker='None', c='green',   markersize = 3.0, ls='-', label ='Maq Isl (2018/19)')
#ax.plot(time11_HMy, BrO_PCAN17_HMed,    marker='None', c='blue',    markersize = 3.0, ls='-', label ='PCAN (2017)')
ax.plot(time12_HMy, BrO_SIPEXII12_HMed, marker='None', c='magenta', markersize = 3.0, ls='-', label ='SIPEXII (2012)')

# Plot the percentiles
#ax.fill_between(time5_HMy,  BrO_MQIsl17_H25P,   BrO_MQIsl17_H75P,   facecolor='red',     alpha=0.2) # fill the distribution
#ax.fill_between(time10_HMy, BrO_MQIsl18_H25P,   BrO_MQIsl18_H75P,   facecolor='green',   alpha=0.2) # fill the distribution
#ax.fill_between(time11_HMy, BrO_PCAN17_H25P,    BrO_PCAN17_H75P,    facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time12_HMy, BrO_SIPEXII12_H25P, BrO_SIPEXII12_H75P, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(1,8)

# Plot the axis labels, legend and title
#ax.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=15)
ax.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 3 (O3)
ax  = plt.subplot(gs[0,2]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  O3_MQIsl17_HMed,   marker='None', c='red',     markersize = 3.0, ls='-', label ='Maq Isl (2017/18)')
ax.plot(time2_HMa,  O3_MQIsl18_HMed,   marker='None', c='green',   markersize = 3.0, ls='-', label ='Maq Isl (2018/19)')
ax.plot(time3_HMa,  O3_PCAN17_HMed,    marker='None', c='blue',    markersize = 3.0, ls='-', label ='PCAN (2017)')
ax.plot(time4_HMa,  O3_SIPEXII12_HMed, marker='None', c='magenta', markersize = 3.0, ls='-', label ='SIPEXII (2012)')

# Plot the percentiles
ax.fill_between(time1_HMa, O3_MQIsl17_H25P,   O3_MQIsl17_H75P,   facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, O3_MQIsl18_H25P,   O3_MQIsl18_H75P,   facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, O3_PCAN17_H25P,    O3_PCAN17_H75P,    facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, O3_SIPEXII12_H25P, O3_SIPEXII12_H75P, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(5,40)

# Plot the axis labels, legend and title
ax.set_ylabel('O$_3$ (ppm)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 4 (RH)
ax  = plt.subplot(gs[0,3]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  RH_MQIsl17_HMed,   marker='None', c='red',     markersize = 3.0, ls='-', label ='Maq Isl (2017/18)')
ax.plot(time2_HMa,  RH_MQIsl18_HMed,   marker='None', c='green',   markersize = 3.0, ls='-', label ='Maq Isl (2018/19)')
ax.plot(time3_HMa,  RH_PCAN17_HMed,    marker='None', c='blue',    markersize = 3.0, ls='-', label ='PCAN (2017)')
ax.plot(time4_HMa,  RH_SIPEXII12_HMed, marker='None', c='magenta', markersize = 3.0, ls='-', label ='SIPEXII (2012)')

# Plot the percentiles
ax.fill_between(time1_HMa, RH_MQIsl17_H25P,   RH_MQIsl17_H75P,   facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, RH_MQIsl18_H25P,   RH_MQIsl18_H75P,   facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, RH_PCAN17_H25P,    RH_PCAN17_H75P,    facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, RH_SIPEXII12_H25P, RH_SIPEXII12_H75P, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(65,105)

# Plot the axis labels, legend and title
ax.set_ylabel('RH (%)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 5 (Wind Speed)
ax  = plt.subplot(gs[1,0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time4_HMa,  WS_MQIsl17_HMed,   marker='None', c='red',     markersize = 3.0, ls='-', label ='Maq Isl (2017/18)')
ax.plot(time2_HMa,  WS_MQIsl18_HMed,   marker='None', c='green',   markersize = 3.0, ls='-', label ='Maq Isl (2018/19)')
ax.plot(time3_HMa,  WS_PCAN17_HMed,    marker='None', c='blue',    markersize = 3.0, ls='-', label ='PCAN (2017)')
ax.plot(time4_HMa,  WS_SIPEXII12_HMed, marker='None', c='magenta', markersize = 3.0, ls='-', label ='SIPEXII (2012)')

# Plot the percentiles
ax.fill_between(time1_HMa, WS_MQIsl17_H25P,   WS_MQIsl17_H75P,   facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, WS_MQIsl18_H25P,   WS_MQIsl18_H75P,   facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, WS_PCAN17_H25P,    WS_PCAN17_H75P,    facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, WS_SIPEXII12_H25P, WS_SIPEXII12_H75P, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,20)

# Plot the axis labels, legend and title
ax.set_ylabel('Wind Speed (m/s)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)

#------------------------------
# Graph 6 (Temp)
ax  = plt.subplot(gs[1,1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  Temp_MQIsl17_HMed,   marker='None', c='red',     markersize = 3.0, ls='-', label ='Maq Isl (2017/18)')
ax.plot(time2_HMa,  Temp_MQIsl18_HMed,   marker='None', c='green',   markersize = 3.0, ls='-', label ='Maq Isl (2018/19)')
ax.plot(time3_HMa,  Temp_PCAN17_HMed,    marker='None', c='blue',    markersize = 3.0, ls='-', label ='PCAN (2017)')
ax.plot(time4_HMa,  Temp_SIPEXII12_HMed, marker='None', c='magenta', markersize = 3.0, ls='-', label ='SIPEXII (2012)')

# Plot the percentiles
ax.fill_between(time1_HMa, Temp_MQIsl17_H25P,   Temp_MQIsl17_H75P,   facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, Temp_MQIsl18_H25P,   Temp_MQIsl18_H75P,   facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, Temp_PCAN17_H25P,    Temp_PCAN17_H75P,    facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, Temp_SIPEXII12_H25P, Temp_SIPEXII12_H75P, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(-15,10)

# Plot the axis labels, legend and title
ax.set_ylabel('Temp (C)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')

#------------------------------
# Graph 7 (SolRad)
ax  = plt.subplot(gs[1,2]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(time1_HMa,  SR_MQIsl17_HMed,   marker='None', c='red',     markersize = 3.0, ls='-', label ='Maq Isl (2017/18)')
ax.plot(time2_HMa,  SR_MQIsl18_HMed,   marker='None', c='green',   markersize = 3.0, ls='-', label ='Maq Isl (2018/19)')
ax.plot(time3_HMa,  SR_PCAN17_HMed,    marker='None', c='blue',    markersize = 3.0, ls='-', label ='PCAN (2017)')
ax.plot(time4_HMa,  SR_SIPEXII12_HMed, marker='None', c='magenta', markersize = 3.0, ls='-', label ='SIPEXII (2012)')

# Plot the percentiles
ax.fill_between(time1_HMa, SR_MQIsl17_H25P,   SR_MQIsl17_H75P,   facecolor='red',     alpha=0.2) # fill the distribution
ax.fill_between(time2_HMa, SR_MQIsl18_H25P,   SR_MQIsl18_H75P,   facecolor='green',   alpha=0.2) # fill the distribution
ax.fill_between(time3_HMa, SR_PCAN17_H25P,    SR_PCAN17_H75P,    facecolor='blue',    alpha=0.2) # fill the distribution
ax.fill_between(time4_HMa, SR_SIPEXII12_H25P, SR_SIPEXII12_H75P, facecolor='magenta', alpha=0.2) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(200))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,700)

# Plot the axis labels, legend and title
ax.set_ylabel('SolRad (W/M$^2$)', fontsize=15)
#ax2.set_ylabel('BrO VMR (pptv)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)

#------------------------------
# Plot the legend
lg = ax.legend(bbox_to_anchor=(1.15, 0.75), loc=2, borderaxespad=0.,title='Voyage',fontsize=15)
lg.get_title().set_fontsize(15)