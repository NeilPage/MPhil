#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:32:21 2019

@author: ncp532
"""
# FILE SYSTEM PACKAGES
from netCDF4 import Dataset,MFDataset				# function used to open multiple netcdf files
import xarray as xr

# DATA HANDLING PACKAGES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

# DRAWING PACKAGES
import cartopy.crs as ccrs
import cartopy
from matplotlib import cm                   # imports the colormap function from matplotlib
import cartopy
import matplotlib.ticker as mticker
from matplotlib.colors import BoundaryNorm
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable

#------------------------------------------------------------------------------
# DEFINE THE DATASET

# SIMULATIONS
DS1 = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_Dynamic_Ocean/trac_avg.geosfp_2x25_Hg.2013*.nc') # Dynamic Ocean
DS2 = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_LPOLARBR/trac_avg.geosfp_2x25_Hg.2013*.nc') # LPOLARBR

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
# PASSIVATION ISSUE WITH CELL A ON VOYAGES V3_18M, V3_18D and V4_18 (FILTER DATA)

Filter1    = Hg0_V3_18['Cart'] == "B"
Hg0_V3_18  = Hg0_V3_18[Filter1]

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

# # Drop nan values
# Hg0_V1_17   = Hg0_V1_17.dropna()
# Hg0_V2_17   = Hg0_V2_17.dropna()
# Hg0_V3_17   = Hg0_V3_17.dropna()
# Hg0_V4_17   = Hg0_V3_17.dropna()

# Hg0_V1_18   = Hg0_V1_18.dropna()
# Hg0_V2_18   = Hg0_V2_18.dropna()
# Hg0_V3_18   = Hg0_V3_18.dropna()
# Hg0_V4_18   = Hg0_V3_18.dropna()

# Hg0_SIPEXII = Hg0_SIPEXII.dropna()
# Hg0_PCAN    = Hg0_PCAN.dropna()

#------------------------------------------------------------------------------
# DEFINE THE VARIABLES

R       = 8.3145 # universal gas constant (J/mol K)
MM_Air  = 28.97 # Molar Mass Dry Air (g/mol)
Avo     = 6.0221 * 1e23 # Avogadro's number
MM_Hg   = 200.59 # Molar Mass Hg (g/mol)

#----------------------
# SIMULATIONS (DS1)
#----------------------
# Air Density
airden1 = DS1.variables[u'BXHGHT_S__AIRNUMDE'][:] # dry air number density (molec air/cm3) 

# Time
time1   = DS1.variables['time'][:] # in minutes

# Latitude and Longitude
lats    = DS1.variables['lat'][:] # latitude
lons    = DS1.variables['lon'][:] # longitude

# Hg0
Hg0     = DS1.variables[u'IJ_AVG_S__Hg0'][:] # Hg0 (pptv) 
Hg0     = Hg0*(1e-3)*MM_Hg/(Avo)*airden1*1e6 
Hg0_Avg = (Hg0[0,0,:,:]+Hg0[1,0,:,:]+Hg0[2,0,:,:]+Hg0[3,0,:,:]+
           Hg0[4,0,:,:]+Hg0[5,0,:,:]+Hg0[6,0,:,:]+Hg0[7,0,:,:]+
           Hg0[8,0,:,:]+Hg0[9,0,:,:]+Hg0[10,0,:,:]+Hg0[11,0,:,:])/12

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

plt.close()
#fig = plt.figure(figsize=(6, 3))

fig = plt.figure()
# #plt.subplots_adjust(hspace=0.5)
# gs = gridspec.GridSpec(1,2,
#                        width_ratios=[2, 2],
#                        height_ratios=[3])
#                        #height_ratios=[3, 3, 3])

# #--------------------------------------------
# # GRAPH 1
# ax1 = plt.subplot(gs[0], projection=projection) # (vertical no, horizontal no, graph no)

# #ax.set_global()
# ax1.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
# ax1.coastlines()
# gl = ax1.gridlines(color='gray',alpha=0.5,)
# #gl.xlocator = mticker.FixedLocator([-180, -90, 0, 90, 180])
# #gl.ylocator = mticker.FixedLocator([-90,-45,0,45,90])
# ax1.set_extent([0, 180, -35, -90], crs=ccrs.PlateCarree())

# #---------------------------
# # Plot the data 
# #cs = ax1.pcolormesh(lons_e, lats_e, Hg0[8,0,:,:] , vmin=0.4, vmax=1.6, transform=data_crs, cmap=cm.get_cmap('jet',12)) #, bins=np.arange(0,100, 10))
# #cs = ax1.pcolormesh(lons, lats, Hg0_Avg[:,:], vmin=0.4, vmax=1.6, transform=data_crs, cmap=cm.get_cmap('jet',12)) #, bins=np.arange(0,100, 10))
# #cb = fig.colorbar(cs,ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6])

# #---------------------------
# # Station location (Lon, Lat)
# Davis_lon, Davis_lat = -68.5766, 77.9674
# Mawson_lon, Mawson_lat = -67.6027, 62.8738
# Casey_lon, Casey_lat = -66.2818, 110.5276
# MacIsl_lon, MacIsl_lat = -54.2959, 158.5609
# Hobart_lon, Hobart_lat = -42.8821, 147.3272

# # Plot the station markers
# ax1.plot(Davis_lat, Davis_lon, transform=data_crs, color='k', marker='o')
# ax1.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='o')
# ax1.plot(Casey_lat, Casey_lon, transform=data_crs, color='k', marker='o')
# ax1.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='o')
# ax1.plot(Hobart_lat, Hobart_lon, transform=data_crs, color='k', marker='o')

# # Plot the marker labels
# ax1.text(Davis_lat + 2, Davis_lon - 1, 'Davis', transform=data_crs, horizontalalignment='right')
# ax1.text(Mawson_lat + 2, Mawson_lon - 1, 'Mawson', transform=data_crs, horizontalalignment='right')
# ax1.text(Casey_lat + 2, Casey_lon - 1, 'Casey', transform=data_crs, horizontalalignment='right')
# ax1.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
# ax1.text(Hobart_lat + 3, Hobart_lon +2, 'Hobart', transform=data_crs, horizontalalignment='right')

# #---------------------------
# # PLOT THE SHIP TRACKS
# #cs = ax1.scatter(SIPEXII_Long, SIPEXII_Lat, transform=data_crs, c=SIPEXII_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
# cs = ax1.scatter(PCAN_Long, PCAN_Lat, transform=data_crs, c=PCAN_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")

# #ax1.scatter(V1_17_Long, V1_17_Lat, transform=data_crs, c=V1_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
# #ax1.scatter(V2_17_Long, V2_17_Lat, transform=data_crs, c=V2_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
# #ax1.scatter(V3_17_Long, V3_17_Lat, transform=data_crs, c=V3_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
# #ax1.scatter(V4_17_Long, V4_17_Lat, transform=data_crs, c=V4_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
# #
# #ax1.scatter(V1_18_Long, V1_18_Lat, transform=data_crs, c=V1_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
# #ax1.scatter(V2_18_Long, V2_18_Lat, transform=data_crs, c=V2_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
# #ax1.scatter(V3_18_Long, V3_18_Lat, transform=data_crs, c=V3_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
# #ax1.scatter(V4_18_Long, V4_18_Lat, transform=data_crs, c=V4_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")

# # Plot the colorbar
# #divider = make_axes_locatable(ax1)
# #cax1 = divider.append_axes("right", size="5%", pad=0.05)
# #cb = fig.colorbar(cs,ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6])    
# ax1.set_aspect('auto')

# # PLOT TITLE, AXIS LABEL & LEGEND TITLE
# plt.title("PCAN (2017)",fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 2
#ax2 = plt.subplot(gs[0], projection=projection) # (vertical no, horizontal no, graph no)
ax2 = plt.subplot(121, projection=projection) # (vertical no, horizontal no, graph no)

#ax.set_global()
ax2.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax2.coastlines()
gl = ax2.gridlines(color='gray',alpha=0.5,)
#gl.xlocator = mticker.FixedLocator([-180, -90, 0, 90, 180])
#gl.ylocator = mticker.FixedLocator([-90,-45,0,45,90])
ax2.set_extent([0, 180, -35, -90], crs=ccrs.PlateCarree())

#---------------------------
# Plot the data 
#cs = ax1.pcolormesh(lons_e, lats_e, Hg0[8,0,:,:] , vmin=0.4, vmax=1.6, transform=data_crs, cmap=cm.get_cmap('jet',12)) #, bins=np.arange(0,100, 10))
#cs = ax1.pcolormesh(lons, lats, Hg0_Avg[:,:], vmin=0.4, vmax=1.6, transform=data_crs, cmap=cm.get_cmap('jet',12)) #, bins=np.arange(0,100, 10))
#cb = fig.colorbar(cs,ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6])

#---------------------------
# Station location (Lon, Lat)
Davis_lon, Davis_lat = -68.5766, 77.9674
Mawson_lon, Mawson_lat = -67.6027, 62.8738
Casey_lon, Casey_lat = -66.2818, 110.5276
MacIsl_lon, MacIsl_lat = -54.2959, 158.5609
Hobart_lon, Hobart_lat = -42.8821, 147.3272

# Plot the station markers
ax2.plot(Davis_lat, Davis_lon, transform=data_crs, color='k', marker='o')
ax2.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='o')
ax2.plot(Casey_lat, Casey_lon, transform=data_crs, color='k', marker='o')
ax2.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='o')
ax2.plot(Hobart_lat, Hobart_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax2.text(Davis_lat + 2, Davis_lon - 1, 'Davis', transform=data_crs, horizontalalignment='right')
ax2.text(Mawson_lat + 2, Mawson_lon - 1, 'Mawson', transform=data_crs, horizontalalignment='right')
ax2.text(Casey_lat + 2, Casey_lon - 1, 'Casey', transform=data_crs, horizontalalignment='right')
ax2.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
ax2.text(Hobart_lat + 3, Hobart_lon + 2, 'Hobart', transform=data_crs, horizontalalignment='right')

#---------------------------
# PLOT THE SHIP TRACKS
#cs = ax1.scatter(SIPEXII_Long, SIPEXII_Lat, transform=data_crs, c=SIPEXII_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(PCAN_Long, PCAN_Lat, transform=data_crs, c=PCAN_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")

cs = ax2.scatter(V1_17_Long, V1_17_Lat, transform=data_crs, c=V1_17_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")
ax2.scatter(V2_17_Long, V2_17_Lat, transform=data_crs, c=V2_17_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")
ax2.scatter(V3_17_Long, V3_17_Lat, transform=data_crs, c=V3_17_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax2.scatter(V4_17_Long, V4_17_Lat, transform=data_crs, c=V4_17_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")

#ax1.scatter(V1_18_Long, V1_18_Lat, transform=data_crs, c=V1_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(V2_18_Long, V2_18_Lat, transform=data_crs, c=V2_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(V3_18_Long, V3_18_Lat, transform=data_crs, c=V3_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(V4_18_Long, V4_18_Lat, transform=data_crs, c=V4_18_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")

# Plot the colorbar
#cb = fig.colorbar(cs,ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6])
ax2.set_aspect('auto')

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("CAMMPCAN (2017-18)",fontsize=15, y=1.02)

#--------------------------------------------
# GRAPH 3
#ax3 = plt.subplot(gs[1], projection=projection) # (vertical no, horizontal no, graph no)
ax3 = plt.subplot(122, projection=projection) # (vertical no, horizontal no, graph no)

#ax.set_global()
ax3.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax3.coastlines()
gl = ax3.gridlines(color='gray',alpha=0.5,)
#gl.xlocator = mticker.FixedLocator([-180, -90, 0, 90, 180])
#gl.ylocator = mticker.FixedLocator([-90,-45,0,45,90])
ax3.set_extent([0, 180, -35, -90], crs=ccrs.PlateCarree())

#---------------------------
# Plot the data 
#cs = ax1.pcolormesh(lons_e, lats_e, Hg0[8,0,:,:] , vmin=0.4, vmax=1.6, transform=data_crs, cmap=cm.get_cmap('jet',12)) #, bins=np.arange(0,100, 10))
#cs = ax1.pcolormesh(lons, lats, Hg0_Avg[:,:], vmin=0.4, vmax=1.6, transform=data_crs, cmap=cm.get_cmap('jet',12)) #, bins=np.arange(0,100, 10))
#cb = fig.colorbar(cs,ticks=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6])

#---------------------------
# Station location (Lon, Lat)
Davis_lon, Davis_lat = -68.5766, 77.9674
Mawson_lon, Mawson_lat = -67.6027, 62.8738
Casey_lon, Casey_lat = -66.2818, 110.5276
MacIsl_lon, MacIsl_lat = -54.2959, 158.5609
Hobart_lon, Hobart_lat = -42.8821, 147.3272

# Plot the station markers
ax3.plot(Davis_lat, Davis_lon, transform=data_crs, color='k', marker='o')
ax3.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='o')
ax3.plot(Casey_lat, Casey_lon, transform=data_crs, color='k', marker='o')
ax3.plot(MacIsl_lat, MacIsl_lon, transform=data_crs, color='k', marker='o')
ax3.plot(Hobart_lat, Hobart_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax3.text(Davis_lat + 2, Davis_lon - 1, 'Davis', transform=data_crs, horizontalalignment='right')
ax3.text(Mawson_lat + 2, Mawson_lon - 1, 'Mawson', transform=data_crs, horizontalalignment='right')
ax3.text(Casey_lat + 2, Casey_lon - 1, 'Casey', transform=data_crs, horizontalalignment='right')
ax3.text(MacIsl_lat - 2, MacIsl_lon - 2, 'Macquarie\nIsland', transform=data_crs, horizontalalignment='right')
ax3.text(Hobart_lat + 3, Hobart_lon + 2, 'Hobart', transform=data_crs, horizontalalignment='right')

#---------------------------
# PLOT THE SHIP TRACKS
#cs = ax1.scatter(SIPEXII_Long, SIPEXII_Lat, transform=data_crs, c=SIPEXII_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(PCAN_Long, PCAN_Lat, transform=data_crs, c=PCAN_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#
#ax1.scatter(V1_17_Long, V1_17_Lat, transform=data_crs, c=V1_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(V2_17_Long, V2_17_Lat, transform=data_crs, c=V2_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(V3_17_Long, V3_17_Lat, transform=data_crs, c=V3_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax1.scatter(V4_17_Long, V4_17_Lat, transform=data_crs, c=V4_17_Hg0, vmin=0.4, vmax=1.6, cmap=cm.get_cmap('jet',12), label="SIPEXII")

ax3.scatter(V1_18_Long, V1_18_Lat, transform=data_crs, c=V1_18_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")
ax3.scatter(V2_18_Long, V2_18_Lat, transform=data_crs, c=V2_18_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")
ax3.scatter(V3_18_Long, V3_18_Lat, transform=data_crs, c=V3_18_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")
#ax3.scatter(V4_18_Long, V4_18_Lat, transform=data_crs, c=V4_18_Hg0, vmin=0.4, vmax=1.0, cmap=cm.get_cmap('jet',12), label="SIPEXII")

# Plot the colorbar
cb = fig.colorbar(cs,ticks=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.4,1.6])
ax3.set_aspect('auto')
cb.set_label('Hg$^0$ (ng/m$^3$)', rotation=90,fontsize=15)

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
plt.title("CAMMPCAN (2018-19)",fontsize=15, y=1.02)

#--------------------------------------------

