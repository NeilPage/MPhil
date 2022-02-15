#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:27:01 2019

@author: ncp532
"""
# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
from windrose import WindroseAxes
from matplotlib.lines import Line2D
import matplotlib.ticker as ticker

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd

# Date and Time handling package
from datetime import datetime, timedelta		# functions to handle date and time

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

#------------------------------------------------------------------------------
# PASSIVATION ISSUE WITH CELL A ON VOYAGES V3_18M, V3_18D and V4_18 (FILTER DATA)

Filter1    = Hg0_V3_18M['Cart'] == "B"
Hg0_V3_18M = Hg0_V3_18M[Filter1]

Filter2    = Hg0_V3_18D['Cart'] == "B"
Hg0_V3_18D = Hg0_V3_18D[Filter2]

Filter3    = Hg0_V4_18['Cart'] == "B"
Hg0_V4_18  = Hg0_V4_18[Filter3]

#------------------------------------------------------------------------------
# RESAMPLE MET DATA TO 5-MIN TIME RESOLUTION

Hg0_V4_17   = Hg0_V4_17.resample('5T').mean()

#--------------
# Met
#--------------
Met_V1_17   = Met_V1_17.resample('5T').mean()
Met_V2_17   = Met_V2_17.resample('5T').mean()
Met_V3_17M  = Met_V3_17M.resample('5T').mean()
Met_V3_17D  = Met_V3_17D.resample('5T').mean()
Met_V4_17   = Met_V4_17.resample('5T').mean()

Met_V1_18   = Met_V1_18.resample('5T').mean()
Met_V2_18   = Met_V2_18.resample('5T').mean()
Met_V3_18M  = Met_V3_18M.resample('5T').mean()
Met_V3_18D  = Met_V3_18D.resample('5T').mean()
Met_V4_18   = Met_V4_18.resample('5T').mean()

Met_SIPEXII = Met_SIPEXII.resample('5T').mean()
Met_PCAN    = Met_PCAN.resample('5T').mean()

#------------------------------------------------------------------------------
# MERGE THE HG0 & MET DATASETS

Hg0_V1_17    = Hg0_V1_17.join(Met_V1_17)
Hg0_V2_17    = Hg0_V2_17.join(Met_V2_17)
Hg0_V3_17M   = Hg0_V3_17M.join(Met_V3_17M)
Hg0_V3_17D   = Hg0_V3_17D.join(Met_V3_17D)
Hg0_V4_17    = Hg0_V4_17.join(Met_V4_17)

Hg0_V1_18    = Hg0_V1_18.join(Met_V1_18)
Hg0_V2_18    = Hg0_V2_18.join(Met_V2_18)
Hg0_V3_18M   = Hg0_V3_18M.join(Met_V3_18M)
Hg0_V3_18D   = Hg0_V3_18D.join(Met_V3_18D)
Hg0_V4_18    = Hg0_V4_18.join(Met_V4_18)

Hg0_SIPEXII  = Hg0_SIPEXII.join(Met_SIPEXII)
Hg0_PCAN     = Hg0_PCAN.join(Met_PCAN)

#------------------------------------------------------------------------------
# ADD A COLUMN FOR AVERAGE WIND DIRECTION & WIND SPEED

# Wind Direction (corellated)
Hg0_V1_17['Wnd_Dir_Avg']   = Hg0_V1_17[['wnd_dir_strbrd_corr_deg',  'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_V2_17['Wnd_Dir_Avg']   = Hg0_V2_17[['wnd_dir_strbrd_corr_deg',  'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_V3_17M['Wnd_Dir_Avg']  = Hg0_V3_17M[['wnd_dir_strbrd_corr_deg', 'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_V3_17D['Wnd_Dir_Avg']  = Hg0_V3_17D[['wnd_dir_strbrd_corr_deg', 'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_V4_17['Wnd_Dir_Avg']   = Hg0_V4_17[['wnd_dir_strbrd_corr_deg',  'wnd_dir_port_corr_deg']].mean(axis=1)

Hg0_V1_18['Wnd_Dir_Avg']   = Hg0_V1_18[['wnd_dir_strbrd_corr_deg',  'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_V2_18['Wnd_Dir_Avg']   = Hg0_V2_18[['wnd_dir_strbrd_corr_deg',  'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_V3_18M['Wnd_Dir_Avg']  = Hg0_V3_18M[['wnd_dir_strbrd_corr_deg', 'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_V3_18D['Wnd_Dir_Avg']  = Hg0_V3_18D[['wnd_dir_strbrd_corr_deg', 'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_V4_18['Wnd_Dir_Avg']   = Hg0_V4_18[['wnd_dir_strbrd_corr_deg',  'wnd_dir_port_corr_deg']].mean(axis=1)

Hg0_SIPEXII['Wnd_Dir_Avg'] = Hg0_SIPEXII[['wnd_dir_strbrd_corr_deg', 'wnd_dir_port_corr_deg']].mean(axis=1)
Hg0_PCAN['Wnd_Dir_Avg']    = Hg0_PCAN[['Starboard True Wind Direction (degree)', 'Port True Wind Direction (degree)']].mean(axis=1) 

# Wind Speed (corellated)
Hg0_V1_17['Wnd_Spd_Avg']   = Hg0_V1_17[['wnd_spd_strbrd_corr_knot',  'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_V2_17['Wnd_Spd_Avg']   = Hg0_V2_17[['wnd_spd_strbrd_corr_knot',  'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_V3_17M['Wnd_Spd_Avg']  = Hg0_V3_17M[['wnd_spd_strbrd_corr_knot', 'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_V3_17D['Wnd_Spd_Avg']  = Hg0_V3_17D[['wnd_spd_strbrd_corr_knot', 'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_V4_17['Wnd_Spd_Avg']   = Hg0_V4_17[['wnd_spd_strbrd_corr_knot',  'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444

Hg0_V1_18['Wnd_Spd_Avg']   = Hg0_V1_18[['wnd_spd_strbrd_corr_knot',  'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_V2_18['Wnd_Spd_Avg']   = Hg0_V2_18[['wnd_spd_strbrd_corr_knot',  'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_V3_18M['Wnd_Spd_Avg']  = Hg0_V3_18M[['wnd_spd_strbrd_corr_knot', 'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_V3_18D['Wnd_Spd_Avg']  = Hg0_V3_18D[['wnd_spd_strbrd_corr_knot', 'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_V4_18['Wnd_Spd_Avg']   = Hg0_V4_18[['wnd_spd_strbrd_corr_knot',  'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444

Hg0_SIPEXII['Wnd_Spd_Avg'] = Hg0_SIPEXII[['wnd_spd_strbrd_corr_knot', 'wnd_spd_port_corr_knot']].mean(axis=1) * 0.514444444
Hg0_PCAN['Wnd_Spd_Avg']    = Hg0_PCAN[['Starboard True Wind Speed (knot)', 'Port True Wind Speed (knot)']].mean(axis=1) * 0.514444444

#------------------------------------------------------------------------------
# FILTER FOR TIME ON STATION

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
# V4_17 Macquarie Island (5-25 Mar 2019) (8-22 Mar 2019 on station)
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

#-----------------------------
# PCAN (26 Jan to 24 Feb 2017)
#-----------------------------
start_date     = '2017-01-26'
end_date       = '2017-02-25'
# Hg0
PCAN         = (Hg0_PCAN.index >= start_date) & (Hg0_PCAN.index < end_date)
Hg0_PCAN_Ice = Hg0_PCAN[PCAN]

#------------------------------------------------------------------------------
# PLOT A WIND ROSE OF WIND SPEED AND WIND DIRECTION

fig = plt.figure(figsize=(20,15)) # (width, height)

color = ['blue', 'skyblue','limegreen','yellow','red']

#-----------------------------
# Graph 1

rect_1 = [0, 0.7, 0.225, 0.225]     # [left, bottom, width, height] as a fraction of total figure size
ax = WindroseAxes(fig, rect_1)    # creates the axes of specified dimensions 
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_Davis_V1_17['Wnd_Dir_Avg'], Hg0_Davis_V1_17['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 25, step=5))
ax.set_yticklabels(np.arange(5, 25, step=5))
ax.set_ylim(0,25)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
ax.set_title("V1 (Davis)", fontsize=15, position=(0.5, 1.1))

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "    CAMMPCAN (2017-18)    ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 2

rect_2 = [0.175, 0.7, 0.225, 0.225]     # [left, bottom, width, height]
ax = WindroseAxes(fig, rect_2)
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_Casey_V2_17['Wnd_Dir_Avg'], Hg0_Casey_V2_17['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 20, step=5))
ax.set_yticklabels(np.arange(5, 20, step=5))
ax.set_ylim(0,20)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
ax.set_title("V2 (Casey)", fontsize=15, position=(0.5, 1.1))

#-----------------------------
# Graph 3

rect_3 = [0.35, 0.7, 0.225, 0.225]     # [left, bottom, width, height]
ax = WindroseAxes(fig, rect_3)
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_Mawson_V3_17['Wnd_Dir_Avg'], Hg0_Mawson_V3_17['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 30, step=5))
ax.set_yticklabels(np.arange(5, 30, step=5))
ax.set_ylim(0,30)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
ax.set_title("V3 (Mawson)", fontsize=15, position=(0.5, 1.1))

#-----------------------------
# Graph 4

rect_4 = [0.525, 0.7, 0.225, 0.225]     # [left, bottom, width, height] as a fraction of total figure size
ax = WindroseAxes(fig, rect_4)    # creates the axes of specified dimensions 
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_Davis_V3_17['Wnd_Dir_Avg'], Hg0_Davis_V3_17['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 25, step=5))
ax.set_yticklabels(np.arange(5, 25, step=5))
ax.set_ylim(0,25)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
ax.set_title("V3 (Davis)", fontsize=15, position=(0.5, 1.1))

#-----------------------------
# Graph 5

rect_5 = [0.7, 0.7, 0.225, 0.225]     # [left, bottom, width, height] as a fraction of total figure size
#rect_5 = [0.525, 0.7, 0.225, 0.225]
ax = WindroseAxes(fig, rect_5)    # creates the axes of specified dimensions 
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_MQIsl_V4_17['Wnd_Dir_Avg'], Hg0_MQIsl_V4_17['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 30, step=5))
ax.set_yticklabels(np.arange(5, 30, step=5))
ax.set_ylim(0,30)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
ax.set_title("V4 (Macquarie Island)", fontsize=15, position=(0.5, 1.1))

#-----------------------------
# Graph 6

rect_6 = [0, 0.375, 0.225, 0.225]     # [left, bottom, width, height]
ax = WindroseAxes(fig, rect_6)
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_Davis_V1_18['Wnd_Dir_Avg'], Hg0_Davis_V1_18['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 25, step=5))
ax.set_yticklabels(np.arange(5, 25, step=5))
ax.set_ylim(0,25)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
#ax.set_title("V1 (Davis))", position=(0.5, 1.1))

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "    CAMMPCAN (2018-19)    ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 7

rect_7 = [0.175, 0.375, 0.225, 0.225]     # [left, bottom, width, height]
ax = WindroseAxes(fig, rect_7)
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_Casey_V2_18['Wnd_Dir_Avg'], Hg0_Casey_V2_18['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 25, step=5))
ax.set_yticklabels(np.arange(5, 25, step=5))
ax.set_ylim(0,25)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
#ax.set_title("V2 (Casey)", position=(0.5, 1.1))

#-----------------------------
# Graph 8

rect_8 = [0.35, 0.375, 0.225, 0.225]     # [left, bottom, width, height] as a fraction of total figure size
ax = WindroseAxes(fig, rect_8)    # creates the axes of specified dimensions 
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_Mawson_V3_18['Wnd_Dir_Avg'], Hg0_Mawson_V3_18['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(10, 50, step=10))
ax.set_yticklabels(np.arange(10, 50, step=10))
ax.set_ylim(0,50)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
#ax.set_title("V3 (Mawson)", position=(0.5, 1.1))

#-----------------------------
# Graph 9

rect_9 = [0.525, 0.375, 0.225, 0.225]     # [left, bottom, width, height]
ax = WindroseAxes(fig, rect_9)
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_Davis_V3_18['Wnd_Dir_Avg'], Hg0_Davis_V3_18['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 20, step=5))
ax.set_yticklabels(np.arange(5, 20, step=5))
ax.set_ylim(0,20)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
#ax.set_title("V3 (Davis)", position=(0.5, 1.1))

#-----------------------------
# Graph 10

rect_10 = [0.7, 0.375, 0.225, 0.225]     # [left, bottom, width, height]
ax = WindroseAxes(fig, rect_10)
fig.add_axes(ax)

# Plot the data
ax.bar(Hg0_MQIsl_V4_18['Wnd_Dir_Avg'], Hg0_MQIsl_V4_18['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 30, step=5))
ax.set_yticklabels(np.arange(5, 30, step=5))
ax.set_ylim(0,20)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
#ax.set_title("V4 (Macquraie Island)", position=(0.5, 1.1))

# #-----------------------------
# # Graph 11

# rect_11 = [0, 0.05, 0.225, 0.225]     # [left, bottom, width, height]
# ax = WindroseAxes(fig, rect_11)
# fig.add_axes(ax)

# # Plot the data
# ax.bar(Hg0_SIPEXII_Ice['Wnd_Dir_Avg'], Hg0_SIPEXII_Ice['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color, opening=1.0, edgecolor='black')

# # Title
# #ax.set_title("SIPEXII (2012)", position=(0.5, 1.1))

# # Text box in upper left
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
# ax.text(-0.35, 0.5, "        SIPEXII (2012)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
# Graph 12

rect_12 = [0, 0.05, 0.225, 0.225]     # [left, bottom, width, height]
ax = WindroseAxes(fig, rect_12)
fig.add_axes(ax)

# Plot the data
lines = ax.bar(Hg0_PCAN_Ice['Wnd_Dir_Avg'], Hg0_PCAN_Ice['ng/m3'], bins=np.arange(0, 1.25, 0.25), normed=True, colors=color,opening=1.0, edgecolor='black')

# Set up percentage labels
ax.set_yticks(np.arange(5, 20, step=5))
ax.set_yticklabels(np.arange(5, 20, step=5))
ax.set_ylim(0,20)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Set up directional labels
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])

# Title
#ax.set_title("PCAN (2017)", position=(0.5, 1.1))

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "        PCAN (2017)        ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#-----------------------------
ax.set_legend()
lg = ax.legend(title="Hg$^0$ (ng/m3)", fontsize=12, loc=(1.6, 0))
plt.setp(lg.get_title(),fontsize=12)

