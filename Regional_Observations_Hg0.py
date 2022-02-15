#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:32:21 2019

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
import cartopy
from matplotlib import cm                   # imports the colormap function from matplotlib
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt             
import matplotlib.dates as mdates            
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# DEFINE THE DATASET

dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y %H:%M:%S')

# OBSERVATIONS
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

RVXue   = pd.read_csv('/Users/ncp532/Documents/Data/RVXuelong_Hg_2014/RVXuelong_Hg0_Lat_Long.csv') # Hg0 data for RVXue (2014/15)
CHINARE = pd.read_csv('/Users/ncp532/Documents/Data/CHINARE_2012_13/CHINARE_Hg0_Lat_Long.csv') # Hg0 data for CHINARE

OSO_V1  = pd.read_csv('/Users/ncp532/Documents/Data/OSO_2010_11/OSO_V1_Hg0_Lat_Long.csv') # Hg0 data for OSO
OSO_V2  = pd.read_csv('/Users/ncp532/Documents/Data/OSO_2010_11/OSO_V2_Hg0_Lat_Long.csv') # Hg0 data for OSO
OSO_V3  = pd.read_csv('/Users/ncp532/Documents/Data/OSO_2010_11/OSO_V3_Hg0_Lat_Long.csv') # Hg0 data for OSO

ANTXXIX = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/ANTXXIX_V6-7_Hg0_2013.csv') # Hg0 data from Michelle Nerentorp

DomeC   = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/DomeC_Hg0_2012_2013.csv', parse_dates=['DateTime'], date_parser=dateparse)
DumontD = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/DumontD_Hg0_2012_2015.csv', parse_dates=['DateTime'], date_parser=dateparse)
McMurdo = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/McMurdo_Hg0_2003.csv', parse_dates=['DateTime'], date_parser=dateparse)
TerraNB = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/TerraNB_Hg0_2000_2001.csv', parse_dates=['DateTime'], date_parser=dateparse)
Troll   = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Troll_Hg0_2011_2015.csv', parse_dates=['DateTime'], date_parser=dateparse)

CapeG   = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/CapeG_Hg0_2011_2017.csv', parse_dates=['DateTime'], date_parser=dateparse)
CapeP   = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/CapeP_Hg0_2012_2016.csv', parse_dates=['DateTime'], date_parser=dateparse)
Barilo  = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Barilo_Hg0_2012_2017.csv', parse_dates=['DateTime'], date_parser=dateparse)
AmsIsl  = pd.read_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/AmsIsl_Hg0_2012_2015.csv', parse_dates=['DateTime'], date_parser=dateparse)

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
# DEFINE THE VARIABLES

#----------------------
# OBSERVATIONS
#----------------------
SIPEXII_Long = np.array(Hg0_SIPEXII['longitude'])
SIPEXII_Lat  = np.array(Hg0_SIPEXII['latitude'])
SIPEXII_Hg0  = np.array(Hg0_SIPEXII['ng/m3'])

PCAN_Long    = np.array(Hg0_PCAN['longitude'])
PCAN_Lat     = np.array(Hg0_PCAN['latitude'])
PCAN_Hg0     = np.array(Hg0_PCAN['ng/m3'])

V1_17_Long   = np.array(Hg0_V1_17['longitude'])
V1_17_Lat    = np.array(Hg0_V1_17['latitude'])
V1_17_Hg0    = np.array(Hg0_V1_17['ng/m3'])

V2_17_Long   = np.array(Hg0_V2_17['longitude'])
V2_17_Lat    = np.array(Hg0_V2_17['latitude'])
V2_17_Hg0    = np.array(Hg0_V2_17['ng/m3'])

V3_17_Long   = np.array(Hg0_V3_17['longitude'])
V3_17_Lat    = np.array(Hg0_V3_17['latitude'])
V3_17_Hg0    = np.array(Hg0_V3_17['ng/m3'])

V4_17_Long   = np.array(Hg0_V4_17['longitude'])
V4_17_Lat    = np.array(Hg0_V4_17['latitude'])
V4_17_Hg0    = np.array(Hg0_V4_17['ng/m3'])

V1_18_Long   = np.array(Hg0_V1_18['longitude'])
V1_18_Lat    = np.array(Hg0_V1_18['latitude'])
V1_18_Hg0    = np.array(Hg0_V1_18['ng/m3'])

V2_18_Long   = np.array(Hg0_V2_18['longitude'])
V2_18_Lat    = np.array(Hg0_V2_18['latitude'])
V2_18_Hg0    = np.array(Hg0_V2_18['ng/m3'])

V3_18_Long   = np.array(Hg0_V3_18['longitude'])
V3_18_Lat    = np.array(Hg0_V3_18['latitude'])
V3_18_Hg0    = np.array(Hg0_V3_18['ng/m3'])

V4_18_Long   = np.array(Hg0_V4_18['longitude'])
V4_18_Lat    = np.array(Hg0_V4_18['latitude'])
V4_18_Hg0    = np.array(Hg0_V4_18['ng/m3'])

RVXue_Long   = np.array(RVXue['LONGITUDE']) # Longitude for RVXue
RVXue_Lat    = np.array(RVXue['LATITUDE']) # Latitude for RVXue
RVXue_Hg0    = np.array(RVXue['ng/m3']) # Hg0 for RVXue

CHINARE_Long = np.array(CHINARE['LONGITUDE']) # Longitude for CHINARE
CHINARE_Lat  = np.array(CHINARE['LATITUDE']) # Latitude for CHINARE
CHINARE_Hg0  = np.array(CHINARE['ng/m3']) # Hg0 for CHINARE

OSO_V1_Long  = np.array(OSO_V1['LONGITUDE']) # Longitude for OSO
OSO_V1_Lat   = np.array(OSO_V1['LATITUDE']) # Latitude for OSO
#OSO_V1_Hg0  = np.array(OSO_V1['ng/m3']) # Hg0 for OSO

OSO_V2_Long  = np.array(OSO_V2['LONGITUDE']) # Longitude for OSO
OSO_V2_Lat   = np.array(OSO_V2['LATITUDE']) # Latitude for OSO
#OSO_V2_Hg0  = np.array(OSO_V2['ng/m3']) # Hg0 for OSO

OSO_V3_Long  = np.array(OSO_V3['LONGITUDE']) # Longitude for OSO
OSO_V3_Lat   = np.array(OSO_V3['LATITUDE']) # Latitude for OSO
#OSO_V2_Hg0  = np.array(OSO_V3['ng/m3']) # Hg0 for OSO

ANTXXIX_Long   = np.array(ANTXXIX['Longitude'])
ANTXXIX_Lat    = np.array(ANTXXIX['Latitude'])
ANTXXIX_Hg0    = np.array(ANTXXIX['GEM'])

DomeC_Hg0    = np.array(DomeC['ng/m3'])
DumontD_Hg0  = np.array(DumontD['ng/m3'])
McMurdo_Hg0  = np.array(McMurdo['ng/m3'])
TerraNB_Hg0  = np.array(TerraNB['ng/m3'])
Troll_Hg0    = np.array(Troll['ng/m3'])

CapeG_Hg0   = np.array(CapeG['ng/m3'])
CapeP_Hg0   = np.array(CapeP['ng/m3'])
Barilo_Hg0  = np.array(Barilo['ng/m3'])
AmsIsl_Hg0  = np.array(AmsIsl['ng/m3'])

#------------------------------------------------------------------------------
# SET THE DATE

DomeC['DateTime'] = pd.to_datetime(DomeC['DateTime'])
DumontD['DateTime'] = pd.to_datetime(DumontD['DateTime'])
McMurdo['DateTime'] = pd.to_datetime(McMurdo['DateTime'])
TerraNB['DateTime'] = pd.to_datetime(TerraNB['DateTime'])
Troll['DateTime'] = pd.to_datetime(Troll['DateTime'])

CapeG['DateTime'] = pd.to_datetime(CapeG['DateTime'])
CapeP['DateTime'] = pd.to_datetime(CapeP['DateTime'])
Barilo['DateTime'] = pd.to_datetime(Barilo['DateTime'])
AmsIsl['DateTime'] = pd.to_datetime(AmsIsl['DateTime'])

DomeC   = DomeC.set_index('DateTime')
DumontD = DumontD.set_index('DateTime')
McMurdo = McMurdo.set_index('DateTime')
TerraNB = TerraNB.set_index('DateTime')
Troll   = Troll.set_index('DateTime')

CapeG   = CapeG.set_index('DateTime')
CapeP   = CapeP.set_index('DateTime')
Barilo  = Barilo.set_index('DateTime')
AmsIsl  = AmsIsl.set_index('DateTime')

#-----------------
# DomeC
dat1 = np.array(DomeC['Date'])
tim1 = np.array(DomeC['Time'])
dattim1 = dat1+' '+tim1

#CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(dattim1)):
    date1.append(datetime.strptime(dattim1[i],'%d/%m/%Y %H:%M:%S'))

#-----------------
# DumontD
dat2 = np.array(DumontD['Date'])
tim2 = np.array(DumontD['Time'])
dattim2 = dat2+' '+tim2

#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y %H:%M:%S'))

#-----------------
# McMurdo
dat3 = np.array(McMurdo['Date'])
tim3 = np.array(McMurdo['Time'])
dattim3 = dat3+' '+tim3

#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y %H:%M:%S'))

#-----------------
# TerraNB
dat4 = np.array(TerraNB['Date'])
tim4 = np.array(TerraNB['Time'])
dattim4 = dat4+' '+tim4

#CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(dattim4)):
    date4.append(datetime.strptime(dattim4[i],'%d/%m/%Y %H:%M:%S'))

#-----------------
# Troll
dat5 = np.array(Troll['Date'])
tim5 = np.array(Troll['Time'])
dattim5 = dat5+' '+tim5

#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    date5.append(datetime.strptime(dattim5[i],'%d/%m/%Y %H:%M:%S'))

#-----------------
# CapeG
dat6 = np.array(CapeG['Date'])
tim6 = np.array(CapeG['Time'])
dattim6 = dat6+' '+tim6

#CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(dattim6)):
    date6.append(datetime.strptime(dattim6[i],'%d/%m/%Y %H:%M:%S'))

#-----------------
# CapeP
dat7 = np.array(CapeP['Date'])
tim7 = np.array(CapeP['Time'])
dattim7 = dat7+' '+tim7

#CONVERT TO DATETIME FROM STRING
date7=[]
for i in range(len(dattim7)):
    date7.append(datetime.strptime(dattim7[i],'%d/%m/%Y %H:%M:%S'))

#-----------------
# Barilo
dat8 = np.array(Barilo['Date'])
tim8 = np.array(Barilo['Time'])
dattim8 = dat8+' '+tim8

#CONVERT TO DATETIME FROM STRING
date8=[]
for i in range(len(dattim8)):
    date8.append(datetime.strptime(dattim8[i],'%d/%m/%Y %H:%M:%S'))

#-----------------
# AmsIsl
dat9 = np.array(AmsIsl['Date'])
tim9 = np.array(AmsIsl['Time'])
dattim9 = dat9+' '+tim9

#CONVERT TO DATETIME FROM STRING
date9=[]
for i in range(len(dattim9)):
    date9.append(datetime.strptime(dattim9[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------------------------------------------------
# ADD A MONTH COLUMN TO EACH DATASET

#DumontD['month'] = DumontD.index.month
#McMurdo['month'] = McMurdo.index.month
#TerraNB['month'] = TerraNB.index.month
#Troll['month']   = Troll.index.month

#CapeG['month']   = CapeG.index.month
#CapeP['month']   = CapeP.index.month
#Barilo['month']  = Barilo.index.month
#AmsIsl['month']  = AmsIsl.index.month

#------------------------------------------------------------------------------
# CALCULATE THE MEAN

Mean_DomeC   = np.nanmean(DomeC_Hg0)
Mean_DumontD = np.nanmean(DumontD_Hg0)
Mean_McMurdo = np.nanmean(McMurdo_Hg0)
Mean_TerraNB = np.nanmean(TerraNB_Hg0)
Mean_Troll   = np.nanmean(Troll_Hg0)

Mean_CapeG   = np.nanmean(CapeG_Hg0)
Mean_CapeP   = np.nanmean(CapeP_Hg0)
Mean_Barilo  = np.nanmean(Barilo_Hg0)
Mean_AmsIsl  = np.nanmean(AmsIsl_Hg0)

#------------------------------------------------------------------------------
# CALCULATE THE HG0 MONTHLY AVERAGE (MEAN)

MM_DomeC   = DomeC.groupby(DomeC.index.month).mean()
MM_DumontD = DumontD.groupby(DumontD.index.month).mean()
MM_McMurdo = McMurdo.groupby(McMurdo.index.month).mean()
MM_TerraNB = TerraNB.groupby(TerraNB.index.month).mean()
MM_Troll   = Troll.groupby(Troll.index.month).mean()

MM_CapeG   = CapeG.groupby(CapeG.index.month).mean()
MM_CapeP   = CapeP.groupby(CapeP.index.month).mean()
MM_Barilo  = Barilo.groupby(Barilo.index.month).mean()
MM_AmsIsl  = AmsIsl.groupby(AmsIsl.index.month).mean()

#------------------------------------------------------------------------------
# CALCULATE THE HG0 MONTHLY STANDARD DEVIATION

STD_DomeC   = DomeC.groupby(DomeC.index.month).std()
STD_DumontD = DumontD.groupby(DumontD.index.month).std()
STD_McMurdo = McMurdo.groupby(McMurdo.index.month).std()
STD_TerraNB = TerraNB.groupby(TerraNB.index.month).std()
STD_Troll   = Troll.groupby(Troll.index.month).std()

STD_CapeG   = CapeG.groupby(CapeG.index.month).std()
STD_CapeP   = CapeP.groupby(CapeP.index.month).std()
STD_Barilo  = Barilo.groupby(Barilo.index.month).std()
STD_AmsIsl  = AmsIsl.groupby(AmsIsl.index.month).std()

#------------------------------------------------------------------------------
# REORDER THE DATAFRAMES TO START IN SEPTEMBER

# Cut at July
cut_val = 7

MM_DomeC   = pd.concat((MM_DomeC.loc[cut_val:],   MM_DomeC.loc[:cut_val-1])).reset_index()
MM_DumontD = pd.concat((MM_DumontD.loc[cut_val:], MM_DumontD.loc[:cut_val-1])).reset_index()
MM_McMurdo = pd.concat((MM_McMurdo.loc[cut_val:], MM_McMurdo.loc[:cut_val-1])).reset_index()
MM_McMurdo['Order'] = np.array([3,4])
MM_TerraNB = pd.concat((MM_TerraNB.loc[cut_val:], MM_TerraNB.loc[:cut_val-1])).reset_index()
MM_TerraNB['Order'] = np.array([4,5,6])
MM_Troll   = pd.concat((MM_Troll.loc[cut_val:],   MM_Troll.loc[:cut_val-1])).reset_index()

MM_CapeG   = pd.concat((MM_CapeG.loc[cut_val:],   MM_CapeG.loc[:cut_val-1])).reset_index()
MM_CapeP   = pd.concat((MM_CapeP.loc[cut_val:],   MM_CapeP.loc[:cut_val-1])).reset_index()
MM_Barilo  = pd.concat((MM_Barilo.loc[cut_val:],  MM_Barilo.loc[:cut_val-1])).reset_index()
MM_AmsIsl  = pd.concat((MM_AmsIsl.loc[cut_val:],  MM_AmsIsl.loc[:cut_val-1])).reset_index()

STD_DomeC   = pd.concat((STD_DomeC.loc[cut_val:],   STD_DomeC.loc[:cut_val-1])).reset_index()
STD_DumontD = pd.concat((STD_DumontD.loc[cut_val:], STD_DumontD.loc[:cut_val-1])).reset_index()
STD_McMurdo = pd.concat((STD_McMurdo.loc[cut_val:], STD_McMurdo.loc[:cut_val-1])).reset_index()
STD_TerraNB = pd.concat((STD_TerraNB.loc[cut_val:], STD_TerraNB.loc[:cut_val-1])).reset_index()
STD_Troll   = pd.concat((STD_Troll.loc[cut_val:],   STD_Troll.loc[:cut_val-1])).reset_index()

STD_CapeG   = pd.concat((STD_CapeG.loc[cut_val:],   STD_CapeG.loc[:cut_val-1])).reset_index()
STD_CapeP   = pd.concat((STD_CapeP.loc[cut_val:],   STD_CapeP.loc[:cut_val-1])).reset_index()
STD_Barilo  = pd.concat((STD_Barilo.loc[cut_val:],  STD_Barilo.loc[:cut_val-1])).reset_index()
STD_AmsIsl  = pd.concat((STD_AmsIsl.loc[cut_val:],  STD_AmsIsl.loc[:cut_val-1])).reset_index()

#------------------------------------------------------------------------------
# FIX THE LATITUDE AND LONGITUDE FOR PLOTTING (based on a size of 2x2.5 for each gridbox) 
# NOTE: GEOS-Chem defines the latitude and longitude based on the bottom-left corner of each grid-box
#       we have to correct the latitude and longitude to represent the middle of each grid-box
#       if we dont do this the map will be slightly off centre when plotted

# Values for the longitudinal edge of each gridbox
lons_e = np.array([ -181.25, -178.75, -176.25, -173.75, -171.25, -168.75,
                    -166.25, -163.75, -161.25, -158.75, -156.25, -153.75,
                    -151.25, -148.75, -146.25, -143.75, -141.25, -138.75,
                    -136.25, -133.75, -131.25, -128.75, -126.25, -123.75,
                    -121.25, -118.75, -116.25, -113.75, -111.25, -108.75,
                    -106.25, -103.75, -101.25,  -98.75,  -96.25,  -93.75,
                    -91.25,  -88.75,  -86.25,  -83.75, -81.25,  -78.75,
                    -76.25,  -73.75,  -71.25,  -68.75,  -66.25,  -63.75,
                    -61.25,  -58.75,  -56.25,  -53.75,  -51.25,  -48.75,
                    -46.25,  -43.75,  -41.25,  -38.75,  -36.25,  -33.75,
                    -31.25,  -28.75,  -26.25,  -23.75, -21.25,  -18.75,
                    -16.25,  -13.75,  -11.25,   -8.75,   -6.25,   -3.75,
                    -1.25,    1.25,    3.75,    6.25,    8.75,   11.25,
                    13.75,   16.25,   18.75,   21.25,   23.75,   26.25,
                      28.75,   31.25,   33.75,   36.25,  38.75,   41.25,
                      43.75,   46.25,   48.75,   51.25,   53.75,   56.25,
                      58.75,   61.25,   63.75,   66.25,   68.75,   71.25,
                      73.75,   76.25,   78.75,   81.25,   83.75,   86.25,
                      88.75,   91.25,   93.75,   96.25,   98.75,  101.25,
                      103.75,  106.25,  108.75,  111.25,  113.75,  116.25,
                      118.75,  121.25,  123.75,  126.25,  128.75,  131.25,
                      133.75,  136.25,  138.75,  141.25,  143.75,  146.25,
                      148.75,  151.25,  153.75,  156.25,  158.75,  161.25,
                      163.75,  166.25,  168.75,  171.25,  173.75,  176.25,
                      178.75,])
# Values for the longitudinal middle of each gridbox
lons_m= np.array([-180.0, -177.5, -175.0, -172.5, -170.0, -167.5, -165.0, -162.5,
                       -160.0, -157.5, -155.0, -152.5, -150.0, -147.5, -145.0, -142.5,
                       -140.0, -137.5, -135.0, -132.5, -130.0, -127.5, -125.0, -122.5,
                       -120.0, -117.5, -115.0, -112.5, -110.0, -107.5, -105.0, -102.5,
                       -100.0,  -97.5,  -95.0,  -92.5,  -90.0,  -87.5,  -85.0,  -82.5,
                       -80.0,  -77.5,  -75.0,  -72.5,  -70.0,  -67.5,  -65.0,  -62.5,
                       -60.0,  -57.5,  -55.0,  -52.5,  -50.0,  -47.5,  -45.0,  -42.5,
                       -40.0,  -37.5,  -35.0,  -32.5,  -30.0,  -27.5,  -25.0,  -22.5,
                       -20.0,  -17.5,  -15.0,  -12.5,  -10.0,   -7.5,   -5.0,   -2.5,
                       0.0,    2.5,    5.0,    7.5,   10.0,   12.5,   15.0,   17.5,
                       20.0,   22.5,   25.0,   27.5,   30.0,   32.5,   35.0,   37.5,
                       40.0,   42.5,   45.0,   47.5,   50.0,   52.5,   55.0,   57.5,
                       60.0,   62.5,   65.0,   67.5,   70.0,   72.5,   75.0,   77.5,
                       80.0,   82.5,   85.0,   87.5,   90.0,   92.5,   95.0,   97.5,
                       100.0,  102.5,  105.0,  107.5,  110.0,  112.5,  115.0,  117.5,
                       120.0,  122.5,  125.0,  127.5,  130.0,  132.5,  135.0,  137.5,
                       140.0,  142.5,  145.0,  147.5,  150.0,  152.5,  155.0,  157.5,
                       160.0,  162.5,  165.0,  167.5,  170.0,  172.5,  175.0,  177.5,
                       ])
# Values for the latitudinal edge of each gridbox
lats_e=np.array([  -90.,  -89.,  -87.,  -85.,  -83.,  -81.,  -79.,  -77.,
                 -75.,  -73.,  -71.,  -69.,  -67.,  -65.,  -63.,  -61.,
                 -59.,  -57.,  -55.,  -53.,  -51.,  -49.,  -47.,  -45.,
                 -43.,  -41.,  -39.,  -37.,  -35.,  -33.,  -31.,  -29.,
                 -27.,  -25.,  -23.,  -21.,  -19.,  -17.,  -15.,  -13.,
                 -11.,   -9.,   -7.,   -5.,   -3.,   -1.,    1.,    3.,
                 5.,    7.,    9.,   11.,   13.,   15.,   17.,   19.,
                 21.,   23.,   25.,   27.,   29.,   31.,   33.,   35.,
                 37.,   39.,   41.,   43.,   45.,   47.,   49.,   51.,
                 53.,   55.,   57.,   59.,   61.,   63.,   65.,   67.,
                 69.,   71.,   73.,   75.,   77.,   79.,   81.,   83.,
                 85.,   87.,   89.,   90., ])
# Values for the latitudinal edge of each gridbox
lats_m=np.array([  -89.5, -88.,  -86.,  -84.,  -82.,  -80.,  -78.,  -76.,
                -74.,  -72.,  -70.,  -68.,  -66.,  -64.,  -62.,  -60.,
                -58.,  -56.,  -54.,  -52.,  -50.,  -48.,  -46.,  -44.,
                -42.,  -40.,  -38.,  -36.,  -34.,  -32.,  -30.,  -28.,
                -26.,  -24.,  -22.,  -20.,  -18.,  -16.,  -14.,  -12.,
                -10.,   -8.,   -6.,   -4.,   -2.,    0.,    2.,    4.,
                6.,    8.,   10.,   12.,   14.,   16.,   18.,   20.,
                22.,   24.,   26.,   28.,   30.,   32.,   34.,   36.,
                38.,   40.,   42.,   44.,   46.,   48.,   50.,   52.,
                54.,   56.,   58.,   60.,   62.,   64.,   66.,   68.,
                70.,   72.,   74.,   76.,   78.,   80.,   82.,   84.,
                86.,   88.,   89.5, ])

#------------------------------------------------------------------------------
# START PLOTTING THE MAP

# The data are defined in lat/lon coordinate system, so PlateCarree()
# is the appropriate coordinate system:
data_crs = ccrs.PlateCarree()

# We will view the map on a polar stereo coordinate system
projection = ccrs.SouthPolarStereo(central_longitude=0)

# Build Date Array
DateC = np.array([9,10,11,12,1,2,3,4,5,6,7,8])
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['J','F','M','A','M','J','J','A','S','O','N','D'])

plt.close()
#fig = plt.figure(figsize=(6, 3))

fig = plt.figure()

gs = gridspec.GridSpec(nrows=3,
                       ncols=5, 
                       figure=fig, 
                       width_ratios= [1, 1, 1, 1, 1],
                       height_ratios=[1, 1, 1],
                       wspace=0.3,
                       hspace=0.4)

plt.subplots_adjust(hspace=0.5)

#--------------------------------------------
# GRAPH 1 (ANTARCTICA MAP)
ax1 = plt.subplot(gs[0:2,1:4], projection=projection) # (vertical no, horizontal no, graph no)

#ax.set_global()
ax1.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax1.coastlines()
gl = ax1.gridlines(color='gray',alpha=0.5,)
#gl.xlocator = mticker.FixedLocator([-180, -90, 0, 90, 180])
#gl.ylocator = mticker.FixedLocator([-90,-45,0,45,90])
ax1.set_extent([-180, 180, -30, -90], crs=ccrs.PlateCarree())

#---------------------------
# Plot the data 
#cs = ax1.pcolormesh(lons_e, lats_e, Hg0[8,0,:,:] , vmin=0.4, vmax=1.6, transform=data_crs, cmap=cm.get_cmap('jet',12)) #, bins=np.arange(0,100, 10))
#cs = ax1.pcolormesh(lons, lats, Hg0_Avg[:,:], vmin=0.4, vmax=1.6, transform=data_crs, cmap=cm.get_cmap('jet',12)) #, bins=np.arange(0,100, 10))
#cb = fig.colorbar(cs,ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6])

#---------------------------
# PLOT THE SHIP TRACKS
ax1.scatter(SIPEXII_Long, SIPEXII_Lat, transform=data_crs, c=SIPEXII_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(PCAN_Long, PCAN_Lat, transform=data_crs, c=PCAN_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="PCAN")

#ax1.scatter(V1_17_Long, V1_17_Lat, transform=data_crs, c=V1_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="V1_17")
#ax1.scatter(V2_17_Long, V2_17_Lat, transform=data_crs, c=V2_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="V2_17")
#ax1.scatter(V3_17_Long, V3_17_Lat, transform=data_crs, c=V3_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="V3_17")
#ax1.scatter(V4_17_Long, V4_17_Lat, transform=data_crs, c=V4_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="V4_17")
#
#ax1.scatter(V1_18_Long, V1_18_Lat, transform=data_crs, c=V1_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="V1_18")
#ax1.scatter(V2_18_Long, V2_18_Lat, transform=data_crs, c=V2_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="V2_18")
#ax1.scatter(V3_18_Long, V3_18_Lat, transform=data_crs, c=V3_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="V3_18")
#ax1.scatter(V4_18_Long, V4_18_Lat, transform=data_crs, c=V4_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="V4_18")

cs = ax1.scatter(RVXue_Long, RVXue_Lat, transform=data_crs, zorder=2, c=RVXue_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="RV Xuelong")
ax1.scatter(CHINARE_Long, CHINARE_Lat, transform=data_crs, zorder=2, c=CHINARE_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="CHINARE")

#ax1.scatter(OSO_V1_Long, OSO_V1_Lat, transform=data_crs, c='purple', vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="OSO_V1")
#ax1.scatter(OSO_V2_Long, OSO_V2_Lat, transform=data_crs, c='blue', vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="OSO_V2")
#ax1.scatter(OSO_V3_Long, OSO_V3_Lat, transform=data_crs, c='red', vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="OSO_V3")

ax1.scatter(ANTXXIX_Long, ANTXXIX_Lat, transform=data_crs, zorder=2, c=ANTXXIX_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="ANTXXIX_V7")

#---------------------------
# Station location (Lon, Lat)
#Davis_lon, Davis_lat       = -68.5766, 77.9674
#Mawson_lon, Mawson_lat     = -67.6027, 62.8738
#Casey_lon, Casey_lat       = -66.2818, 110.5276
#MacIsl_lon, MacIsl_lat     = -54.2959, 158.5609
#Hobart_lon, Hobart_lat     = -42.8821, 147.3272

CapeGrim_lat, CapeGrim_lon = -40.6832, 144.6832
AmsIsl_lat, AmsIsl_lon     = -37.4748, 77.3423
CapePnt_lat, CapePnt_lon   = -34.3535, 18.4897
DuUrv_lat, DuUrv_lon       = -66.3946, 140.0007
Concor_lat, Concor_lon     = -75.0559, 123.1956
Troll_lat, Troll_lon       = -72.0041, 2.3206
Barilo_lat, Barilo_lon     = -41.7438, -71.2512
McMurdo_lat, McMurdo_lon   = -77.5047, 166.4006
#Neumayer_lat, Neumayer_lon = -70.6770, -8.2720
TerraNB_lat, TerraNB_lon   = -74.6940, 164.114

# Plot the station markers
#ax1.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='o')
#ax1.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='o')
#ax1.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='o')
#ax1.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='o')
#ax1.plot(Hobart_lat, Hobart_lon, transform=data_crs, color='k', marker='o')

#ax1.plot(CapeGrim_lon, CapeGrim_lat, transform=data_crs, color='k', marker='o')
#ax1.plot(AmsIsl_lon,   AmsIsl_lat,   transform=data_crs, color='k', marker='o')
#ax1.plot(CapePnt_lon,  CapePnt_lat,  transform=data_crs, color='k', marker='o')
#ax1.plot(DuUrv_lon,    DuUrv_lat,    transform=data_crs, color='k', marker='o')
#ax1.plot(Concor_lon,   Concor_lat,   transform=data_crs, color='k', marker='o')
#ax1.plot(Troll_lon,    Troll_lat,    transform=data_crs, color='k', marker='o')
#ax1.plot(Barilo_lon,   Barilo_lat,   transform=data_crs, color='k', marker='o')
#ax1.plot(McMurdo_lon,  McMurdo_lat,  transform=data_crs, color='k', marker='o')
#ax1.plot(Neumayer_lon, Neumayer_lat, transform=data_crs, color='k', marker='o')
#ax1.plot(TerraNB_lon,  TerraNB_lat,  transform=data_crs, color='k', marker='o')

lons = [CapeGrim_lon,AmsIsl_lon,CapePnt_lon,DuUrv_lon,Concor_lon,Troll_lon,Barilo_lon,McMurdo_lon,TerraNB_lon]
lats = [CapeGrim_lat,AmsIsl_lat,CapePnt_lat,DuUrv_lat,Concor_lat,Troll_lat,Barilo_lat,McMurdo_lat,TerraNB_lat]
obs  = [Mean_CapeG,Mean_AmsIsl,Mean_CapeP,Mean_DumontD,Mean_DomeC,Mean_Troll,Mean_Barilo,Mean_McMurdo,Mean_TerraNB]

#lons = [144.6832, 131.0447, 151.1018, 18.4897, 77.3423]
#lats = [-40.6832, -12.2491, -32.4777, -34.3535, -37.4748]
#obs  = [0.902, 0.965, 0.828, 1.033, 1.031]
ax1.scatter(lons, lats, c=obs, transform=data_crs, zorder=2, vmin=0.4, vmax = 1.6, cmap=cm.get_cmap('jet',12), edgecolors='black', s=100)

# Plot the marker labels
#ax1.text(Davis_lat + 2,  Davis_lon - 1,  'Davis',             transform=data_crs, horizontalalignment='right')
#ax1.text(Mawson_lat + 2, Mawson_lon - 1, 'Mawson',            transform=data_crs, horizontalalignment='right')
#ax1.text(Casey_lat + 2,  Casey_lon - 1,  'Casey',             transform=data_crs, horizontalalignment='right')
#ax1.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
#ax1.text(Hobart_lat + 3, Hobart_lon +2,  'Hobart',            transform=data_crs, horizontalalignment='right')

ax1.text(CapeGrim_lon - 6, CapeGrim_lat +1, 'Cape Grim',        transform=data_crs, horizontalalignment='right')
ax1.text(AmsIsl_lon - 2,   AmsIsl_lat + 2,  'Amsterdam Island', transform=data_crs, horizontalalignment='right')
ax1.text(CapePnt_lon - 2,  CapePnt_lat + 1, 'Cape Point',       transform=data_crs, horizontalalignment='right')
ax1.text(DuUrv_lon  -8,    DuUrv_lat      ,   "Dumont\nd'Urville",  transform=data_crs, horizontalalignment='right')
ax1.text(Concor_lon + 2,   Concor_lat - 1,  'Concordia',        transform=data_crs, horizontalalignment='right')
ax1.text(Troll_lon + 15,   Troll_lat - 1,  'Troll',            transform=data_crs, horizontalalignment='right')
ax1.text(Barilo_lon + 3,   Barilo_lat - 1,  'Bariloche',        transform=data_crs, horizontalalignment='right')
ax1.text(McMurdo_lon + 4,  McMurdo_lat + 1, 'McMurdo',          transform=data_crs, horizontalalignment='right')
#ax1.text(Neumayer_lon - 5, Neumayer_lat - 2,'Neumayer',         transform=data_crs, horizontalalignment='right')
ax1.text(TerraNB_lon +2,   TerraNB_lat + 2,  'Terra Nova Bay',   transform=data_crs, horizontalalignment='right')

#---------------------------
# Plot the colorbar
#divider = make_axes_locatable(ax1)
#cax1 = divider.append_axes("right", size="5%", pad=0.05)
#cb = fig.colorbar(cs,ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6])    
ax1.set_aspect('auto')

# PLOT THE COLORBAR
cb = fig.colorbar(cs,ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6])
ax1.set_aspect('auto')
cb.set_label('Hg$^0$ (ng/m$^3$)', rotation=90,fontsize=15)

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("Regional observations of Hg$^0$",fontsize=20, y=1.02)

#--------------------------------------------
# GRAPH 2 (TROLL)

ax2=plt.subplot(gs[0, 0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax2.plot(MM_Troll.index, MM_Troll['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL2 = MM_Troll['ng/m3'] + STD_Troll['ng/m3'] # find the upper limit
LL2 = MM_Troll['ng/m3'] - STD_Troll['ng/m3'] # find the lower limit
ax2.plot(MM_Troll.index, UL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax2.plot(MM_Troll.index, LL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax2.fill_between(MM_Troll.index, UL2, LL2, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.tick_params(axis='y', which='both')
ax2.set_ylim(0.5,1.9)

# Plot the axis labels
ax2.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax2.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title('Troll', fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 3 (BARILOCHE)
ax3=plt.subplot(gs[1, 0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax3.plot(MM_Barilo.index, MM_Barilo['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL3 = MM_Barilo['ng/m3'] + STD_Barilo['ng/m3'] # find the upper limit
LL3 = MM_Barilo['ng/m3'] - STD_Barilo['ng/m3'] # find the lower limit
ax3.plot(MM_Barilo.index, UL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax3.plot(MM_Barilo.index, LL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax3.fill_between(MM_Barilo.index, UL3, LL3, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.tick_params(axis='y', which='both')
ax3.set_ylim(0.5,1.9)

# Plot the axis labels
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax3.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title('Bariloche', fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 4 (MC MURDO)
ax4=plt.subplot(gs[2, 0]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
#ax4.plot(MM_McMurdo.index, MM_McMurdo['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')
ax4.plot(MM_McMurdo['Order'], MM_McMurdo['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL4 = MM_McMurdo['ng/m3'] + STD_McMurdo['ng/m3'] # find the upper limit
LL4 = MM_McMurdo['ng/m3'] - STD_McMurdo['ng/m3'] # find the lower limit
#ax4.plot(MM_McMurdo.index, UL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax4.plot(MM_McMurdo.index, LL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax4.fill_between(MM_McMurdo.index, UL4, LL4, facecolor='blue', alpha=0.3) # fill the distribution
ax4.plot(MM_McMurdo['Order'], UL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax4.plot(MM_McMurdo['Order'], LL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax4.fill_between(MM_McMurdo['Order'], UL4, LL4, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax4.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax4.tick_params(axis='y', which='both')
ax4.set_ylim(0.5,1.9)

# Plot the axis labels
ax4.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax4.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title('McMurdo', fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 5 (CAPE POINT)
ax5=plt.subplot(gs[0, 4]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax5.plot(MM_CapeP.index, MM_CapeP['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL5 = MM_CapeP['ng/m3'] + STD_CapeP['ng/m3'] # find the upper limit
LL5 = MM_CapeP['ng/m3'] - STD_CapeP['ng/m3'] # find the lower limit
ax5.plot(MM_CapeP.index, UL5, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax5.plot(MM_CapeP.index, LL5, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax5.fill_between(MM_CapeP.index, UL5, LL5, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax5.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax5.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax5.tick_params(axis='y', which='both')
ax5.set_ylim(0.5,1.9)

# Plot the axis labels
ax5.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax5.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title('Cape Point', fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 6 (AMSTERDAM ISLAND)
ax6=plt.subplot(gs[1, 4]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax6.plot(MM_AmsIsl.index, MM_AmsIsl['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL6 = MM_AmsIsl['ng/m3'] + STD_AmsIsl['ng/m3'] # find the upper limit
LL6 = MM_AmsIsl['ng/m3'] - STD_AmsIsl['ng/m3'] # find the lower limit
ax6.plot(MM_AmsIsl.index, UL6, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax6.plot(MM_AmsIsl.index, LL6, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax6.fill_between(MM_AmsIsl.index, UL6, LL6, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax6.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax6.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax6.tick_params(axis='y', which='both')
ax6.set_ylim(0.5,1.9)

# Plot the axis labels
ax6.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax6.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title('Amsterdam Island', fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 7 (CAPE GRIM)
ax7=plt.subplot(gs[2, 4]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax7.plot(MM_CapeG.index, MM_CapeG['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL7 = MM_CapeG['ng/m3'] + STD_CapeG['ng/m3'] # find the upper limit
LL7 = MM_CapeG['ng/m3'] - STD_CapeG['ng/m3'] # find the lower limit
ax7.plot(MM_CapeG.index, UL7, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax7.plot(MM_CapeG.index, LL7, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax7.fill_between(MM_CapeG.index, UL7, LL7, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax7.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax7.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax7.tick_params(axis='y', which='both')
ax7.set_ylim(0.5,1.9)

# Plot the axis labels
ax7.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax7.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title('Cape Grim', fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 8 (TERRA NOVA BAY)
ax8=plt.subplot(gs[2, 1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
#ax8.plot(MM_TerraNB.index, MM_TerraNB['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')
ax8.plot(MM_TerraNB['Order'], MM_TerraNB['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL8 = MM_TerraNB['ng/m3'] + STD_TerraNB['ng/m3'] # find the upper limit
LL8 = MM_TerraNB['ng/m3'] - STD_TerraNB['ng/m3'] # find the lower limit
#ax8.plot(MM_TerraNB.index, UL8, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax8.plot(MM_TerraNB.index, LL8, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax8.fill_between(MM_TerraNB.index, UL8, LL8, facecolor='blue', alpha=0.3) # fill the distribution
ax8.plot(MM_TerraNB['Order'], UL8, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax8.plot(MM_TerraNB['Order'], LL8, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax8.fill_between(MM_TerraNB['Order'], UL8, LL8, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax8.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax8.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax8.tick_params(axis='y', which='both')
ax8.set_ylim(0.5,1.9)

# Plot the axis labels
ax8.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax8.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title('Terra Nova Bay', fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 9 (CONCORDIA)
ax9=plt.subplot(gs[2, 2]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax9.plot(MM_DomeC.index, MM_DomeC['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL9 = MM_DomeC['ng/m3'] + STD_DomeC['ng/m3'] # find the upper limit
LL9 = MM_DomeC['ng/m3'] - STD_DomeC['ng/m3'] # find the lower limit
ax9.plot(MM_DomeC.index, UL9, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax9.plot(MM_DomeC.index, LL9, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax9.fill_between(MM_DomeC.index, UL9, LL9, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax9.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax9.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax9.tick_params(axis='y', which='both')
ax9.set_ylim(0.5,1.9)

# Plot the axis labels
ax9.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax9.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title('Dome C', fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 10 (DUMONT D'URVILLE)
ax10=plt.subplot(gs[2, 3]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax10.plot(MM_DumontD.index, MM_DumontD['ng/m3'], marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')

# Plot the St Dev
UL10 = MM_DumontD['ng/m3'] + STD_DumontD['ng/m3'] # find the upper limit
LL10 = MM_DumontD['ng/m3'] - STD_DumontD['ng/m3'] # find the lower limit
ax10.plot(MM_DumontD.index, UL10, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax10.plot(MM_DumontD.index, LL10, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax10.fill_between(MM_DumontD.index, UL10, LL10, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['J','A','S','O','N','D','J','F','M','A','M','J'])
plt.xticks(fontsize=10)

# Format y-axis 1
ax10.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax10.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax10.tick_params(axis='y', which='both')
ax10.set_ylim(0.5,1.9)

# Plot the axis labels
ax10.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=12)
ax10.set_xlabel('Month', fontsize=12)

#Plot the legend and title
plt.title("Dumont d'Urville", fontsize=15, y=1.02)
