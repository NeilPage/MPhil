#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:19:13 2017

@author: ncp532
"""
# FILE SYSTEM PACKAGES
from netCDF4 import MFDataset				# function used to open multiple netcdf files

# DRAWING PACKAGES
import cartopy.crs as ccrs
import matplotlib.pyplot as plt			# imports pyplot (provides a MATLAB-like plotting function)
import matplotlib as mpl				    # import matplotlib package as shorter nickname
import matplotlib.colors as colors			# for visual representation of matplotlib colormaps
from matplotlib import cm                   # imports the colormap function from matplotlib
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from mpl_toolkits.axes_grid1 import make_axes_locatable

# DATE AND TIME HANDLING PACKAGES
from datetime import datetime,timedelta		# functions to handle date and time

# DATA HANDLING PACKAGES
import math						         # package to do mathematical calculations (such as log, exponential)
import numpy as np					    # import package as shorter nickname - Numpy as great at handling multidimensional data arrays.
import pandas as pd

#------------------------------------------------------------------------------
# DEFINE THE DATASET

# Simulations
dataset1 = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_Dynamic_Ocean/trac_avg.geosfp_2x25_Hg.2013*.nc') # Dynamic Ocean
dataset2 = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_LPOLARBR/trac_avg.geosfp_2x25_Hg.2013*.nc') # LPOLARBR

# Observations
SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/SIPEXII_Data.csv',header=0,encoding = 'unicode_escape')
#V1 = pd.read_csv('/Users/ncp532/Documents/Data/SIPEX_II_Mercury_Air/SIPEXII_Hg0_Lat_Long.csv') # Hg0 data for CAMPCANN V1 (2017/18)
#V2 = pd.read_csv('/Users/ncp532/Documents/Data/SIPEX_II_Mercury_Air/SIPEXII_Hg0_Lat_Long.csv') # Hg0 data for CAMPCANN V2 (2017/18)
#V3 = pd.read_csv('/Users/ncp532/Documents/Data/SIPEX_II_Mercury_Air/SIPEXII_Hg0_Lat_Long.csv') # Hg0 data for CAMPCANN V3 (2017/18)
#V4 = pd.read_csv('/Users/ncp532/Documents/Data/SIPEX_II_Mercury_Air/SIPEXII_Hg0_Lat_Long.csv') # Hg0 data for CAMPCANN V4 (2017/18)

SIPEXII_Long = np.array(SIPEXII['LONGITUDE']) # Longitude for SIPEXII
SIPEXII_Lat = np.array(SIPEXII['LATITUDE']) # Latitude for SIPEXII
SIPEXII_Hg0 = np.array(SIPEXII['ng/m3']) # Hg0 for SIPEXII

#------------------------------------------------------------------------------
# GET THE VARIABLES YOU WOULD LIKE FROM THE GEOS-CHEM SIMULATION
# you can display the variable names by typing "dataset1" into the python console
# you can display more information about individual variables by typing "dataset1.variables['INSERT THE VARIABLES NAME']" into the python console
# e.g. for Hg0 type "dataset1.variables['IJ_AVG_S__Hg0']" into the python console

# Atmospheric Parameters
R       = 8.3145 # universal gas constant (J/mol K)
MM_Air  = 28.97 # Molar Mass Dry Air (g/mol)
Avo     = 6.0221*1e23 # Avogadro's number
MM_Hg   = 200.59 # Molar Mass Hg (g/mol)
MM_BrO   = 95.904 # Molar Mass BrO (g/mol)
MM_Br   = 79.904 # Molar Mass Br (g/mol)

# - - - - - - - - - - - - - - - - - - - - - - -
# Dynamic Ocean
airden1 = dataset1.variables[u'BXHGHT_S__AIRNUMDE'][:] # dry air number density (molec air/cm3) 

# Hg0
Hg0_a     = dataset1.variables[u'IJ_AVG_S__Hg0'][:] # Hg0 (pptv) 
Hg0_a     = Hg0_a*(1e-3)*MM_Hg/(Avo)*airden1*1e6 
Hg0_a_Av   = (Hg0_a[8,0,:,:] + Hg0_a[9,0,:,:]) / 2 # Mean simulated Hg0 concentration for Sept and Oct

# BrO
BrO_a     = dataset1.variables[u'PL_HG2_S__BrO'][:] # BrO concentration (molec/cm3) 
#BrO_a     = BrO_a*(1e-3)*MM_BrO/(Avo)*airden1
BrO_a_Av   = (BrO_a[8,0,:,:] + BrO_a[9,0,:,:]) / 2 # Mean simulated BrO concentration for Sept and Oct

# Br
Br_a      = dataset1.variables[u'PL_HG2_S__Br'][:] # BrO concentration (molec/cm3) 
#Br_a      = Br_a*(1e-3)*MM_Br/(Avo)*airden1
Br_a_Av   = (Br_a[8,0,:,:] + Br_a[9,0,:,:]) / 2 # Mean simulated Br concentration for Sept and Oct

# - - - - - - - - - - - - - - - - - - - - - - -
# LPOLARBR
airden2 = dataset2.variables[u'BXHGHT_S__AIRNUMDE'][:] # dry air number density (molec air/cm3) 

# Hg0
Hg0_b     = dataset2.variables[u'IJ_AVG_S__Hg0'][:] # Hg0 (pptv) 
Hg0_b     = Hg0_b*(1e-3)*MM_Hg/(Avo)*airden2*1e6 
Hg0_b_Av  = (Hg0_b[8,0,:,:] + Hg0_b[9,0,:,:]) / 2 # Mean simulated Hg0 concentration for Sept and Oct

# BrO
BrO_b     = dataset2.variables[u'PL_HG2_S__BrO'][:] # BrO concentration (molec/cm3) 
#BrO_b     = BrO_b*(1e-3)*MM_BrO/(Avo)*airden2
BrO_b_Av  = (BrO_b[8,0,:,:] + BrO_b[9,0,:,:]) / 2 # Mean simulated BrO concentration for Sept and Oct

# Br
Br_b      = dataset2.variables[u'PL_HG2_S__Br'][:] # BrO concentration (molec/cm3) 
#Br_b      = Br_b*(1e-3)*MM_Br/(Avo)*airden2
Br_b_Av   = (Br_b[8,0,:,:] + Br_b[9,0,:,:]) / 2 # Mean simulated Br concentration for Sept and Oct

# BrO + Br
BrOBr_b   = BrO_b + Br_b

# Polar BrO Concentration
BrO_Pol   = dataset2.variables[u'PL_HG2_S__BrO_pol'][:] # Polar BrO concentration (pptv) 

# Polar Br Concentration
Br_Pol    = dataset2.variables[u'PL_HG2_S__Br_pol'][:] # Polar BrO concentration (pptv) 

# Polar BrO + Br
BrOBr_Pol = BrO_Pol + Br_Pol

# Hg Ocean up flux
Hg_Ocean  = dataset2.variables[u'HG_SRCE__Hg_up'][:] # Hg Ocean up flux (kg)

# Snow emission of Hg0
Hg0_Snow  = dataset2.variables[u'HG_SRCE__Hg0_snow'][:] # Snow emission of Hg (kg)

# - - - - - - - - - - - - - - - - - - - - - - -
# DIFFERENCE (between Dynamic Ocean & LPOLARBR)

# Hg0
Hg0_Diff = Hg0_a - Hg0_b

# BrO
BrO_Diff = BrO_a - BrO_b

# Br
Br_Diff = Br_a - Br_b

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
# DEFFINE THE FUNCTION FOR PLOTTING YOUR MAP
def plotkg(x, bar, tit):  # (x = the value to be plotted, bar = colorbar (Y/N), tit = title for map)
    lons, lats = np.meshgrid(lons_e,lats_e)
    
    # NORMAL MAP PLOT
    # - - - - - - - - - - - - - - - - - - - - - - -
#    # Antarctica
#    m=Basemap(llcrnrlat=-90,  urcrnrlat=-20,          # set the latitude limits
#              llcrnrlon=-0, urcrnrlon=179,         # set the longitude limits
#              resolution='c',projection='gall')      # choose the resolution and projection type        

#    # Greenland
#    m=Basemap(llcrnrlat=55,  urcrnrlat=90,          # set the latitude limits
#              llcrnrlon=-80, urcrnrlon=-10,         # set the longitude limits
#              resolution='c',projection='gall')      # choose the resolution and projection type 
    
    # World
    m=Basemap(llcrnrlat=-90,  urcrnrlat=90,          # set the latitude limits
              llcrnrlon=-180, urcrnrlon=179,         # set the longitude limits
              resolution='c',projection='gall')      # choose the resolution and projection type 
    # - - - - - - - - - - - - - - - - - - - - - - -
          
    mlons,mlats = m(lons, lats) # convert lons/lat from middle of grid-box to to corner of grid-box
    cs=m.pcolormesh(mlons, mlats, x, latlon=False,   cmap=cm.plasma) # vmin=0.0, vmax=300, # Hg (define the colorbar attributes (colors used, add "_r" to flip the color scale))    
    #cs=m.pcolormesh(mlons, mlats, x, latlon=False,  vmin=0.4, vmax=1.6, cmap=cm.plasma) # Hg (define the colorbar attributes (colors used, add "_r" to flip the color scale))    
    #cs=m.pcolormesh(mlons, mlats, x, latlon=False,  cmap=cm.plasma) # vmin=100000, vmax=8000000, # BrO (define the colorbar attributes (colors used, add "_r" to flip the color scale))    
    m.drawcoastlines() # draw coastlines on the map
    
    # FORMAT THE COLORBAR
    if bar=='Y': # Y if you want a colorbar, N if you don't
        cb=m.colorbar(cs,"bottom",size="5%", pad="15%") # Position the colorbar next to your map and define its size
        #cb.set_label(r"$ng$ $m$$^-$$^3$", fontsize =10) # Hg (add text for the colourbar label and define fontsize)
        #cb.set_label(r"$molecules/cm$$^3$", fontsize =10) # BrO, Br, BrO+Br (add text for the colourbar label and define fontsize)
        cb.set_label(r"$kg/month$", fontsize =10) # Hg flux
        cb.ax.tick_params(labelsize=10, rotation=25) # add numbers to the colorbar
        cb.ax.minorticks_on()           # add ticks to the colorbar
    
    # PLOT PARALLELS AND MERIDANS
    # - - - - - - - - - - - - - - - - - - - - - - -
#    # Antarctica
#    parallels = np.arange(-90,10, 10.0)  # set the latitude limits and how often you wish parallels to be plotted
#    m.drawparallels(parallels,labels=[True,False,True,False], fontsize=10) # define the fontsize for parallels
#    meridians = np.arange(-180,179,30.0) # set the longitude limits and how often you wish meridans to be plotted
#    m.drawmeridians(meridians,labels=[True,False,False,True], fontsize=10) # define the fontsize for meridans
    
#    # Greenland
#    parallels = np.arange(55, 90, 10.0)  # set the latitude limits and how often you wish parallels to be plotted
#    m.drawparallels(parallels,labels=[True,False,True,False], fontsize=10) # define the fontsize for parallels
#    meridians = np.arange(-80,-10,10.0) # set the longitude limits and how often you wish meridans to be plotted
#    m.drawmeridians(meridians,labels=[True,False,False,True], fontsize=10, rotation=25) # define the fontsize for meridans
    
     # World
    parallels = np.arange(-90, 90, 30.0)  # set the latitude limits and how often you wish parallels to be plotted
    m.drawparallels(parallels,labels=[True,False,True,False], fontsize=10) # define the fontsize for parallels
    meridians = np.arange(-180,179,30.0) # set the longitude limits and how often you wish meridans to be plotted
    m.drawmeridians(meridians,labels=[True,False,False,True], fontsize=10, rotation=25) # define the fontsize for meridans
    # - - - - - - - - - - - - - - - - - - - - - - -
#    # PLOT LOCATION MARKERS FOR MONITORING SITES
#    lons1 = [144.6832, 77.3423, 18.4897, 140.0007, 123.1956, 2.3206, -71.2512, 166.4006]    # [Cape Grim, Amsterdam Island, Cape Point, Mawson, Davis, Casey, Macquarie Island, Dumont d'Urville, Concordia, Troll, Bariloche, McMurdo]
#    lats1 = [-40.6832, -37.4748, -34.3535, -66.3946, -75.0559, -72.0041, -41.7438, -77.5047]  # [Cape Grim, Amsterdam Island, Cape Point, Mawson, Davis, Casey, Macquarie Island, Dumont d'Urville, Concordia, Troll, Bariloche, McMurdo]
#    x1,y1 = m(lons1, lats1)
#    
#    # OPTION 1: if you want plain location markers use this line
#    m.scatter(x1, y1, c='white', edgecolors='black', s=50) # define the location markers (color, edgecolor, size)
#    
#    # PLOT THE LOCATION MARKERS FOR AAD STATIONS
#    lons2 = [62.5227, 77.5803, 110.3136, 158.5609]    # [Mawson, Davis, Casey, Macquarie Island]
#    lats2 = [-67.3612, -68.3436, -66.1657, -54.2959]  # [Mawson, Davis, Casey, Macquarie Island]
#    x2,y2 = m(lons2, lats2)
#    
#    # OPTION 1: if you want plain location markers use this line
#    m.scatter(x2, y2, c='black', edgecolors='black', s=50) # define the location markers (color, edgecolor, size)    
    
    # PLOT THE LABELS FOR THE X-AXIS and Y-AXIS
#    plt.xlabel('Longitude [$^\circ$]', fontsize=15, labelpad=30) # (text displayed, fontsize, distance between map and label) 
#    plt.ylabel('Latitude [$^\circ$]', fontsize=15, labelpad=50)  # (text displayed, fontsize, distance between map and label) 
    
    # DEFINE FONTSIZE FOR THE MAP TITLE
    plt.title(tit, fontsize=10)
    return m

#------------------------------------------------------------------------------
# START PLOTTING THE MAP
fig = plt.figure()

# CHOOSE HOW MANY FIGURES YOU WISH TO PLOT
# - - - - - - - - - - - - - - - - - - - - - - -
## Dynamic Ocean
#ax1 = plt.subplot(311) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_a_Av[:,:], 'Y', "Simulated GEM Concentrations (Sept & Oct 2012)") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
## - - - - - - - - - - - - - - - - - - - - - - -
## LPOLARBR
#ax1 = plt.subplot(312) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b_Av[:,:], 'Y', "Simulated GEM Concentrations (Sept & Oct 2012)") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
# - - - - - - - - - - - - - - - - - - - - - - -
## Hg0
##Jan
#ax1 = plt.subplot(341) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[0,0,:,:], 'Y', "Jan") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Feb
#ax1 = plt.subplot(342) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[1,0,:,:], 'Y', "Feb") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Mar
#ax1 = plt.subplot(343) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[2,0,:,:], 'Y', "Mar") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Apr
#ax1 = plt.subplot(344) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[3,0,:,:], 'Y', "Apr") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##May
#ax1 = plt.subplot(345) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[4,0,:,:], 'Y', "May") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jun
#ax1 = plt.subplot(346) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[5,0,:,:], 'Y', "Jun") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jul
#ax1 = plt.subplot(347) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[6,0,:,:], 'Y', "Jul") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Aug
#ax1 = plt.subplot(348) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[7,0,:,:], 'Y', "Aug") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Sep
#ax1 = plt.subplot(349) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[8,0,:,:], 'Y', "Sep") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Oct
#ax1 = plt.subplot(3,4,10) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[9,0,:,:], 'Y', "Oct") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Nov
#ax1 = plt.subplot(3,4,11) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[10,0,:,:], 'Y', "Nov") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Dec
#ax1 = plt.subplot(3,4,12) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_b[11,0,:,:], 'Y', "Dec") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']

## DIFFERENCE Hg0
##Jan
#ax1 = plt.subplot(341) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[0,0,:,:], 'Y', "Jan") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Feb
#ax1 = plt.subplot(342) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[1,0,:,:], 'Y', "Feb") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Mar
#ax1 = plt.subplot(343) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[2,0,:,:], 'Y', "Mar") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Apr
#ax1 = plt.subplot(344) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[3,0,:,:], 'Y', "Apr") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##May
#ax1 = plt.subplot(345) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[4,0,:,:], 'Y', "May") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jun
#ax1 = plt.subplot(346) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[5,0,:,:], 'Y', "Jun") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jul
#ax1 = plt.subplot(347) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[6,0,:,:], 'Y', "Jul") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Aug
#ax1 = plt.subplot(348) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[7,0,:,:], 'Y', "Aug") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Sep
#ax1 = plt.subplot(349) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[8,0,:,:], 'Y', "Sep") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Oct
#ax1 = plt.subplot(3,4,10) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[9,0,:,:], 'Y', "Oct") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Nov
#ax1 = plt.subplot(3,4,11) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[10,0,:,:], 'Y', "Nov") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Dec
#ax1 = plt.subplot(3,4,12) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg0_Diff[11,0,:,:], 'Y', "Dec") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']

# - - - - - - - - - - - - - - - - - - - - - - -
## DIFFERENCE BrO
##Jan
#ax1 = plt.subplot(341) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[0,0,:,:], 'Y', "Jan") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Feb
#ax1 = plt.subplot(342) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[1,0,:,:], 'Y', "Feb") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Mar
#ax1 = plt.subplot(343) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[2,0,:,:], 'Y', "Mar") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Apr
#ax1 = plt.subplot(344) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[3,0,:,:], 'Y', "Apr") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##May
#ax1 = plt.subplot(345) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[4,0,:,:], 'Y', "May") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jun
#ax1 = plt.subplot(346) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[5,0,:,:], 'Y', "Jun") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jul
#ax1 = plt.subplot(347) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[6,0,:,:], 'Y', "Jul") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Aug
#ax1 = plt.subplot(348) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[7,0,:,:], 'Y', "Aug") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Sep
#ax1 = plt.subplot(349) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[8,0,:,:], 'Y', "Sep") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Oct
#ax1 = plt.subplot(3,4,10) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[9,0,:,:], 'Y', "Oct") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Nov
#ax1 = plt.subplot(3,4,11) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[10,0,:,:], 'Y', "Nov") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Dec
#ax1 = plt.subplot(3,4,12) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrO_b[11,0,:,:], 'Y', "Dec") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']

# - - - - - - - - - - - - - - - - - - - - - - -
## DIFFERENCE Br
##Jan
#ax1 = plt.subplot(341) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[0,0,:,:], 'Y', "Jan") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Feb
#ax1 = plt.subplot(342) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[1,0,:,:], 'Y', "Feb") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Mar
#ax1 = plt.subplot(343) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[2,0,:,:], 'Y', "Mar") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Apr
#ax1 = plt.subplot(344) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[3,0,:,:], 'Y', "Apr") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##May
#ax1 = plt.subplot(345) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[4,0,:,:], 'Y', "May") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jun
#ax1 = plt.subplot(346) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[5,0,:,:], 'Y', "Jun") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jul
#ax1 = plt.subplot(347) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[6,0,:,:], 'Y', "Jul") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Aug
#ax1 = plt.subplot(348) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[7,0,:,:], 'Y', "Aug") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Sep
#ax1 = plt.subplot(349) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[8,0,:,:], 'Y', "Sep") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Oct
#ax1 = plt.subplot(3,4,10) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[9,0,:,:], 'Y', "Oct") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Nov
#ax1 = plt.subplot(3,4,11) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[10,0,:,:], 'Y', "Nov") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Dec
#ax1 = plt.subplot(3,4,12) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Br_b[11,0,:,:], 'Y', "Dec") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']

# - - - - - - - - - - - - - - - - - - - - - - -
## DIFFERENCE BrO + Br
##Jan
#ax1 = plt.subplot(341) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[0,0,:,:], 'Y', "Jan") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Feb
#ax1 = plt.subplot(342) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[1,0,:,:], 'Y', "Feb") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Mar
#ax1 = plt.subplot(343) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[2,0,:,:], 'Y', "Mar") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Apr
#ax1 = plt.subplot(344) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[3,0,:,:], 'Y', "Apr") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##May
#ax1 = plt.subplot(345) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[4,0,:,:], 'Y', "May") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jun
#ax1 = plt.subplot(346) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[5,0,:,:], 'Y', "Jun") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jul
#ax1 = plt.subplot(347) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[6,0,:,:], 'Y', "Jul") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Aug
#ax1 = plt.subplot(348) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[7,0,:,:], 'Y', "Aug") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Sep
#ax1 = plt.subplot(349) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[8,0,:,:], 'Y', "Sep") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Oct
#ax1 = plt.subplot(3,4,10) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[9,0,:,:], 'Y', "Oct") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Nov
#ax1 = plt.subplot(3,4,11) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[10,0,:,:], 'Y', "Nov") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Dec
#ax1 = plt.subplot(3,4,12) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(BrOBr_b[11,0,:,:], 'Y', "Dec") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']

# - - - - - - - - - - - - - - - - - - - - - - -
## Hg Ocean up flux
##Jan
#ax1 = plt.subplot(341) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[0,:,:], 'Y', "Jan") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Feb
#ax1 = plt.subplot(342) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[1,:,:], 'Y', "Feb") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Mar
#ax1 = plt.subplot(343) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[2,:,:], 'Y', "Mar") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Apr
#ax1 = plt.subplot(344) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[3,:,:], 'Y', "Apr") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##May
#ax1 = plt.subplot(345) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[4,:,:], 'Y', "May") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jun
#ax1 = plt.subplot(346) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[5,:,:], 'Y', "Jun") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Jul
#ax1 = plt.subplot(347) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[6,:,:], 'Y', "Jul") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Aug
#ax1 = plt.subplot(348) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[7,:,:], 'Y', "Aug") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Sep
#ax1 = plt.subplot(349) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[8,:,:], 'Y', "Sep") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Oct
#ax1 = plt.subplot(3,4,10) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[9,:,:], 'Y', "Oct") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Nov
#ax1 = plt.subplot(3,4,11) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[10,:,:], 'Y', "Nov") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
##Dec
#ax1 = plt.subplot(3,4,12) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
#ax1 = plotkg(Hg_Ocean[11,:,:], 'Y', "Dec") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']

# - - - - - - - - - - - - - - - - - - - - - - -
# Snow emission of Hg0
#Jan
ax1 = plt.subplot(341) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[0,:,:], 'Y', "Jan") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Feb
ax1 = plt.subplot(342) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[1,:,:], 'Y', "Feb") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Mar
ax1 = plt.subplot(343) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[2,:,:], 'Y', "Mar") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Apr
ax1 = plt.subplot(344) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[3,:,:], 'Y', "Apr") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#May
ax1 = plt.subplot(345) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[4,:,:], 'Y', "May") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Jun
ax1 = plt.subplot(346) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[5,:,:], 'Y', "Jun") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Jul
ax1 = plt.subplot(347) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[6,:,:], 'Y', "Jul") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Aug
ax1 = plt.subplot(348) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[7,:,:], 'Y', "Aug") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Sep
ax1 = plt.subplot(349) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[8,:,:], 'Y', "Sep") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Oct
ax1 = plt.subplot(3,4,10) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[9,:,:], 'Y', "Oct") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Nov
ax1 = plt.subplot(3,4,11) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[10,:,:], 'Y', "Nov") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']
#Dec
ax1 = plt.subplot(3,4,12) # subplot(number of figures vertical, number of figures horizontal, total number of figures)
ax1 = plotkg(Hg0_Snow[11,:,:], 'Y', "Dec") # Hg$^0$ Note that Hg0 is an array Hg0['time','lev','lat','lon']