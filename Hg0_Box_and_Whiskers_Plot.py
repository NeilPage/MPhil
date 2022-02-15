#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:52:12 2020

@author: ncp532
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:14:04 2019

@author: ncp532
"""


# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
from windrose import WindroseAxes

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd
from scipy import stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

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
# Sea Ice
#--------------
SI_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V1_17_BrO.csv',  index_col=0)
SI_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V2_17_BrO.csv',  index_col=0)
SI_V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V3_17M_BrO.csv', index_col=0)

SI_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V1_18_BrO.csv',  index_col=0)
SI_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V2_18_BrO.csv',  index_col=0)
SI_V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V3_18M_BrO.csv', index_col=0)

#------------------------------------------------------------------------------
# Set DateTime as the index

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
# Sea Ice
#--------------
SI_V1_17.index   = pd.to_datetime(SI_V1_17.index,   dayfirst=True)
SI_V2_17.index   = pd.to_datetime(SI_V2_17.index,   dayfirst=True)
SI_V3_17.index   = pd.to_datetime(SI_V3_17.index,   dayfirst=True)

SI_V1_18.index   = pd.to_datetime(SI_V1_18.index,   dayfirst=True)
SI_V2_18.index   = pd.to_datetime(SI_V2_18.index,   dayfirst=True)
SI_V3_18.index   = pd.to_datetime(SI_V3_18.index,   dayfirst=True)

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

#-----------------------------
# V2_17 Casey (13 Dec 2017 - 11 Jan 2018) (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018 on station)
#-----------------------------
start_date = '2017-12-13'
end_date   = '2018-01-12'
# BrO
Casey      = (Hg0_V2_17.index >= start_date) & (Hg0_V2_17.index < end_date)
Hg0_V2_17  = Hg0_V2_17[Casey]

#-----------------------------
# V3_17 Mawson (16 Jan - 6 Mar 2018) (1-17 Feb 2018 on station)
#-----------------------------
start_date = '2018-01-16'
end_date   = '2018-03-07'
# BrO
Mawson     = (Hg0_V3_17M.index >= start_date) & (Hg0_V3_17M.index < end_date)
Hg0_V3_17M = Hg0_V3_17M[Mawson]

#-----------------------------
# V3_17 Davis (16 Jan - 6 Mar 2018) (27-30 Jan 2018 and 19-21 Feb 2018 on station)
#-----------------------------
start_date = '2018-01-16'
end_date   = '2018-03-07'
# BrO
Mawson     = (Hg0_V3_17D.index >= start_date) & (Hg0_V3_17D.index < end_date)
Hg0_V3_17D = Hg0_V3_17D[Mawson]

#-----------------------------
# V4_17 Macquarie Island (9-23 Mar 2018) (12-20 Mar 2018 on station)
#-----------------------------
start_date = '2018-03-09'
end_date   = '2018-03-24'
# BrO
MQIsl      = (Hg0_V4_17.index >= start_date) & (Hg0_V4_17.index < end_date)
Hg0_V4_17  = Hg0_V4_17[MQIsl]

#-----------------------------
# V1_18 Davis (25 Oct - 28 Nov 2018) (7-15 Nov 2018 on station)
#-----------------------------
start_date = '2018-10-25'
end_date   = '2018-11-29'
# BrO
Davis      = (Hg0_V1_18.index >= start_date) & (Hg0_V1_18.index < end_date)
Hg0_V1_18  = Hg0_V1_18[Davis]

#-----------------------------
# V2_18 Casey (6 Dec 2018 - 7 Jan 2019) (15-30 Dec 2018 on station)
#-----------------------------
start_date = '2018-12-06'
end_date   = '2019-01-08'
# BrO
Casey      = (Hg0_V2_18.index >= start_date) & (Hg0_V2_18.index < end_date)
Hg0_V2_18  = Hg0_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (13 Jan - 1 Mar 2019) (30 Jan - 9 Feb 2019)
#-----------------------------
start_date = '2019-01-13'
end_date   = '2019-03-2'
# BrO
Mawson     = (Hg0_V3_18M.index >= start_date) & (Hg0_V3_18M.index < end_date)
Hg0_V3_18M = Hg0_V3_18M[Mawson]

#-----------------------------
# V3_18 Davis (13 Jan - 1 Mar 2019) (26-28 Jan 2019 and 19-20 Feb 2019 on station)
#-----------------------------
start_date = '2019-01-13'
end_date   = '2019-03-2'
# BrO
Mawson     = (Hg0_V3_18D.index >= start_date) & (Hg0_V3_18D.index < end_date)
Hg0_V3_18D = Hg0_V3_18D[Mawson]

#-----------------------------
# V4_17 Macquarie Island (5-25 Mar 2019) (8-22 Mar 2019 on station)
#-----------------------------
start_date = '2019-03-05'
end_date   = '2019-03-26'
# BrO
MQIsl      = (Hg0_V4_18.index >= start_date) & (Hg0_V4_18.index < end_date)
Hg0_V4_18  = Hg0_V4_18[MQIsl]

#-----------------------------
# SIPEXII (14 Sep to 16 Nov 2012) (23 Sep to 11 Nov 2012 close to Antarctica)
#-----------------------------
start_date  = '2012-09-14'
end_date    = '2012-11-16'
# BrO
SIPEX       = (Hg0_SIPEXII.index >= start_date) & (Hg0_SIPEXII.index < end_date)
Hg0_SIPEXII = Hg0_SIPEXII[SIPEX]

#-----------------------------
# PCAN (14 Jan to 4 Mar 2017) (26 Jan to 24 Feb 2017 close to Antarctica)
#-----------------------------
start_date = '2017-01-14'
end_date   = '2017-02-25'
# BrO
PCAN       = (Hg0_PCAN.index >= start_date) & (Hg0_PCAN.index < end_date)
Hg0_PCAN   = Hg0_PCAN[PCAN]

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
# BrO
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
# BrO
Mawson           = (Hg0_V3_17M.index >= start_date) & (Hg0_V3_17M.index < end_date)
Hg0_Mawson_V3_17 = Hg0_V3_17M[Mawson]

#-----------------------------
# V3_17 Davis (27-30 Jan 2018 and 19-21 Feb 2018)
#-----------------------------
start_date1   = '2018-01-27'
end_date1     = '2018-01-31'
start_date2   = '2018-02-19'
end_date2     = '2018-02-22'
# BrO
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
# BrO
MQIsl           = (Hg0_V4_17.index >= start_date) & (Hg0_V4_17.index < end_date)
Hg0_MQIsl_V4_17 = Hg0_V4_17[MQIsl]

#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
#-----------------------------
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# BrO
Davis           = (Hg0_V1_18.index >= start_date) & (Hg0_V1_18.index < end_date)
Hg0_Davis_V1_18 = Hg0_V1_18[Davis]

#-----------------------------
# V2_18 Casey (15-30 Dec 2018)
#-----------------------------
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# BrO
Casey           = (Hg0_V2_18.index >= start_date) & (Hg0_V2_18.index < end_date)
Hg0_Casey_V2_18 = Hg0_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#-----------------------------
start_date    = '2019-01-30'
end_date      = '2019-02-10'
# BrO
Mawson           = (Hg0_V3_18M.index >= start_date) & (Hg0_V3_18M.index < end_date)
Hg0_Mawson_V3_18 = Hg0_V3_18M[Mawson]

#-----------------------------
# V3_18 Davis (26-28 Jan 2019 and 19-20 Feb 2019)
#-----------------------------
start_date1   = '2019-01-26'
end_date1     = '2019-01-29'
start_date2   = '2019-02-19'
end_date2     = '2019-02-21'
# BrO
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
# BrO
MQIsl           = (Hg0_V4_18.index >= start_date) & (Hg0_V4_18.index < end_date)
Hg0_MQIsl_V4_18 = Hg0_V4_18[MQIsl]

#-----------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
#-----------------------------
start_date      = '2012-09-23'
end_date        = '2012-11-12'
# BrO
SIPEX           = (Hg0_SIPEXII.index >= start_date) & (Hg0_SIPEXII.index < end_date)
Hg0_SIPEXII_Ice = Hg0_SIPEXII[SIPEX]

#-----------------------------
# PCAN (26 Jan to 24 Feb 2017)
#-----------------------------
start_date     = '2017-01-26'
end_date       = '2017-02-25'
# BrO
PCAN           = (Hg0_PCAN.index >= start_date) & (Hg0_PCAN.index < end_date)
Hg0_PCAN_Ice   = Hg0_PCAN[PCAN]

#------------------------------------------------------------------------------
# Filter the datasets for time in open water

Hg0_PCAN_OW    = Hg0_PCAN.merge(Hg0_PCAN_Ice,       how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_SIPEXII_OW = Hg0_SIPEXII.merge(Hg0_SIPEXII_Ice, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V1_17_OW   = Hg0_V1_17.merge(Hg0_Davis_V1_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V2_17_OW   = Hg0_V2_17.merge(Hg0_Casey_V2_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17M_OW  = Hg0_V3_17M.merge(Hg0_Mawson_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17M_OW  = Hg0_V3_17M.merge(Hg0_Davis_V3_17,  how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17D_OW  = Hg0_V3_17D.merge(Hg0_Davis_V3_17,  how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_17D_OW  = Hg0_V3_17D.merge(Hg0_Mawson_V3_17, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V4_17_OW   = Hg0_V4_17.merge(Hg0_MQIsl_V4_17,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

Hg0_V1_18_OW   = Hg0_V1_18.merge(Hg0_Davis_V1_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V2_18_OW   = Hg0_V2_18.merge(Hg0_Casey_V2_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18M_OW  = Hg0_V3_18M.merge(Hg0_Mawson_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18M_OW  = Hg0_V3_18M.merge(Hg0_Davis_V3_18,  how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18D_OW  = Hg0_V3_18D.merge(Hg0_Davis_V3_18,  how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V3_18D_OW  = Hg0_V3_18D.merge(Hg0_Mawson_V3_18, how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
Hg0_V4_18_OW   = Hg0_V4_18.merge(Hg0_MQIsl_V4_18,   how = 'outer', indicator=True).loc[lambda x : x['_merge']=='left_only']

#------------------------------------------------------------------------------
# Define the variables

# Whole voyage
PCAN_Hg0       = np.array(Hg0_PCAN['ng/m3'])
SIPEXII_Hg0    = np.array(Hg0_SIPEXII['ng/m3'])

V1_17_Hg0      = np.array(Hg0_V1_17['ng/m3'])
V2_17_Hg0      = np.array(Hg0_V2_17['ng/m3'])
V3_17M_Hg0     = np.array(Hg0_V3_17M['ng/m3'])
V3_17D_Hg0     = np.array(Hg0_V3_17D['ng/m3'])
V4_17_Hg0      = np.array(Hg0_V4_17['ng/m3'])

V1_18_Hg0      = np.array(Hg0_V1_18['ng/m3'])
V2_18_Hg0      = np.array(Hg0_V2_18['ng/m3'])
V3_18M_Hg0     = np.array(Hg0_V3_18M['ng/m3'])
V3_18D_Hg0     = np.array(Hg0_V3_18D['ng/m3'])
V4_18_Hg0      = np.array(Hg0_V4_18['ng/m3'])

# On station
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

# Off station
OW_PCAN_Hg0    = np.array(Hg0_PCAN_OW['ng/m3'])
OW_SIPEXII_Hg0 = np.array(Hg0_SIPEXII_OW['ng/m3'])

OW_V1_17_Hg0   = np.array(Hg0_V1_17_OW['ng/m3'])
OW_V2_17_Hg0   = np.array(Hg0_V2_17_OW['ng/m3'])
OW_V3_17M_Hg0  = np.array(Hg0_V3_17M_OW['ng/m3'])
OW_V3_17D_Hg0  = np.array(Hg0_V3_17D_OW['ng/m3'])
OW_V4_17_Hg0   = np.array(Hg0_V4_17_OW['ng/m3'])

OW_V1_18_Hg0   = np.array(Hg0_V1_18_OW['ng/m3'])
OW_V2_18_Hg0   = np.array(Hg0_V2_18_OW['ng/m3'])
OW_V3_18M_Hg0  = np.array(Hg0_V3_18M_OW['ng/m3'])
OW_V3_18D_Hg0  = np.array(Hg0_V3_18D_OW['ng/m3'])
OW_V4_18_Hg0   = np.array(Hg0_V4_18_OW['ng/m3'])

# Sea ice
Hg0_Ice1_V1_17 = np.array(Hg0_Ice_V1_17['ng/m3'])
Hg0_Ice1_V2_17 = np.array(Hg0_Ice_V2_17['ng/m3'])
Hg0_Ice1_V3_17 = np.array(Hg0_Ice_V3_17['ng/m3'])

Hg0_Ice1_V1_18 = np.array(Hg0_Ice_V1_18['ng/m3'])
Hg0_Ice1_V2_18 = np.array(Hg0_Ice_V2_18['ng/m3'])
Hg0_Ice1_V3_18 = np.array(Hg0_Ice_V3_18['ng/m3'])

# Open water
Hg0_OW1_V1_17 = np.array(Hg0_OW_V1_17['ng/m3'])
Hg0_OW1_V2_17 = np.array(Hg0_OW_V2_17['ng/m3'])
Hg0_OW1_V3_17 = np.array(Hg0_OW_V3_17['ng/m3'])

Hg0_OW1_V1_18 = np.array(Hg0_OW_V1_18['ng/m3'])
Hg0_OW1_V2_18 = np.array(Hg0_OW_V2_18['ng/m3'])
Hg0_OW1_V3_18 = np.array(Hg0_OW_V3_18['ng/m3'])

#------------------------------------------------------------------------------
# BUILD A DATAFRAME FOR THE BOXPLOT

# Whole voyage
data1  = [V1_17_Hg0, V2_17_Hg0, V3_17M_Hg0, V3_17D_Hg0, V4_17_Hg0]
data2  = [V1_18_Hg0, V2_18_Hg0, V3_18M_Hg0, V3_18D_Hg0, V4_18_Hg0]
data3  = [SIPEXII_Hg0]
data4  = [PCAN_Hg0]

# On station
data5  = [Hg0_Davis1_17, Hg0_Casey_17, Hg0_Mawson_17, Hg0_Davis3_17, Hg0_MQIsl_17]
data6  = [Hg0_Davis1_18, Hg0_Casey_18, Hg0_Mawson_18, Hg0_Davis3_18, Hg0_MQIsl_18]
data7  = [Hg0_SIPEXII_12]
data8  = [Hg0_PCAN_17]

# Off station
data9  = [OW_V1_17_Hg0, OW_V2_17_Hg0, OW_V3_17M_Hg0, OW_V3_17D_Hg0, OW_V4_17_Hg0]
data10 = [OW_V1_18_Hg0, OW_V2_18_Hg0, OW_V3_18M_Hg0, OW_V3_18D_Hg0, OW_V4_18_Hg0]
data11 = [OW_SIPEXII_Hg0]
data12 = [OW_PCAN_Hg0]

# Sea Ice
data13 = [Hg0_Ice1_V1_17, Hg0_Ice1_V2_17, Hg0_Ice1_V3_17]
data14 = [Hg0_Ice1_V1_18, Hg0_Ice1_V2_18, Hg0_Ice1_V3_18]

# Open Water
data15 = [Hg0_OW1_V1_17, Hg0_OW1_V2_17, Hg0_OW1_V3_17]
data16 = [Hg0_OW1_V1_18, Hg0_OW1_V2_18, Hg0_OW1_V3_18]

#------------------------------------------------------------------------------
# COMBINE VOYAGES TO GET CAMPAIGN TOTAL

# Whole voyage
CAMMPCAN1718_All = np.concatenate((Hg0_V1_17['ng/m3'],     Hg0_V2_17['ng/m3'],     Hg0_V3_17M['ng/m3']), axis = None)
CAMMPCAN1819_All = np.concatenate((Hg0_V1_18['ng/m3'],     Hg0_V2_18['ng/m3'],     Hg0_V3_18M['ng/m3']), axis = None)
CAMMPCAN_OverAll = np.concatenate((CAMMPCAN1718_All, CAMMPCAN1819_All), axis = None)

# Sea Ice
CAMMPCAN1718_Ice = np.concatenate((Hg0_Ice1_V1_17, Hg0_Ice1_V2_17, Hg0_Ice1_V3_17), axis = None)
CAMMPCAN1819_Ice = np.concatenate((Hg0_Ice1_V1_18, Hg0_Ice1_V2_18, Hg0_Ice1_V3_18), axis = None)
CAMMPCAN_IceAll  = np.concatenate((CAMMPCAN1718_Ice, CAMMPCAN1819_Ice), axis = None)

# Open Water
CAMMPCAN1718_OW  = np.concatenate((Hg0_OW1_V1_17,  Hg0_OW1_V2_17,  Hg0_OW1_V3_17), axis = None)
CAMMPCAN1819_OW  = np.concatenate((Hg0_OW1_V1_18,  Hg0_OW1_V2_18,  Hg0_OW1_V3_18), axis = None)
CAMMPCAN_OWAll   = np.concatenate((CAMMPCAN1718_OW, CAMMPCAN1819_OW), axis = None)

#------------------------------------------------------------------------------
# Make a list of the number of values in each distribution

# text to include with label
j = 'n = '

#-----------------
# Whole voyage
#-----------------

# CAMMPCAN 2017-18
N1_V1_17   = len(V1_17_Hg0)
N1_V2_17   = len(V2_17_Hg0)
N1_V3_17M  = len(V3_17M_Hg0)
N1_V3_17D  = len(V3_17D_Hg0)
N1_V4_17   = len(V4_17_Hg0)

# CAMMPCAN 2018-19
N1_V1_18   = len(V1_18_Hg0)
N1_V2_18   = len(V2_18_Hg0)
N1_V3_18M  = len(V3_18M_Hg0)
N1_V3_18D  = len(V3_18D_Hg0)
N1_V4_18   = len(V4_18_Hg0)

# SIPPEX 2012
N1_SIPEXII = len(SIPEXII_Hg0)

# PCAN 2017
N1_PCAN    = len(PCAN_Hg0)

DF1 = [N1_V1_17, N1_V1_18, N1_V2_17, N1_V2_18, N1_V3_17M, N1_V3_18M, N1_V3_17D, N1_V3_18D, N1_V4_17, N1_V4_18, N1_SIPEXII, N1_PCAN]

#-----------------
# On station
#-----------------

# CAMMPCAN 2017-18
N2_V1_17  = len(Hg0_Davis1_17)
N2_V2_17  = len(Hg0_Casey_17)
N2_V3_17M = len(Hg0_Mawson_17)
N2_V3_17D = len(Hg0_Davis3_17)
N2_V4_17  = len(Hg0_MQIsl_17)

# CAMMPCAN 2018-19
N2_V1_18  = len(Hg0_Davis1_18)
N2_V2_18  = len(Hg0_Casey_18)
N2_V3_18M = len(Hg0_Mawson_18)
N2_V3_18D = len(Hg0_Davis3_18)
N2_V4_18  = len(Hg0_MQIsl_18)

# SIPPEX 2012
N2_SIPEXII = len(Hg0_SIPEXII_12)

# PCAN 2017
N2_PCAN = len(Hg0_PCAN_17)

DF2 = [N2_V1_17, N2_V1_18, N2_V2_17, N2_V2_18, N2_V3_17M, N2_V3_18M, N2_V3_17D, N2_V3_18D, N2_V4_17, N2_V4_18, N2_SIPEXII, N2_PCAN]

#-----------------
# Off station
#-----------------

# CAMMPCAN 2017-18
N3_V1_17   = len(OW_V1_17_Hg0)
N3_V2_17   = len(OW_V2_17_Hg0)
N3_V3_17M  = len(OW_V3_17M_Hg0)
N3_V3_17D  = len(OW_V3_17D_Hg0)
N3_V4_17   = len(OW_V4_17_Hg0)

# CAMMPCAN 2018-19
N3_V1_18   = len(OW_V1_18_Hg0)
N3_V2_18   = len(OW_V2_18_Hg0)
N3_V3_18M  = len(OW_V3_18M_Hg0)
N3_V3_18D  = len(OW_V3_18D_Hg0)
N3_V4_18   = len(OW_V4_18_Hg0)

# SIPPEX 2012
N3_SIPEXII = len(OW_SIPEXII_Hg0)

# PCAN 2017
N3_PCAN    = len(OW_PCAN_Hg0)

DF3 = [N3_V1_17, N3_V1_18, N3_V2_17, N3_V2_18, N3_V3_17M, N3_V3_18M, N3_V3_17D, N3_V3_18D, N3_V4_17, N3_V4_18, N3_SIPEXII, N3_PCAN]

#-----------------
# Sea Ice
#-----------------

N4_V1_17 = len(Hg0_Ice1_V1_17)
N4_V2_17 = len(Hg0_Ice1_V2_17)
N4_V3_17 = len(Hg0_Ice1_V3_17)

N4_V1_18 = len(Hg0_Ice1_V1_18)
N4_V2_18 = len(Hg0_Ice1_V2_18)
N4_V3_18 = len(Hg0_Ice1_V3_18)

DF4 = [N4_V1_17, N4_V1_18, N4_V2_17, N4_V2_18, N4_V3_17, N4_V3_18]

#-----------------
# Open Water
#-----------------

N5_V1_17 = len(Hg0_OW1_V1_17)
N5_V2_17 = len(Hg0_OW1_V2_17)
N5_V3_17 = len(Hg0_OW1_V3_17)

N5_V1_18 = len(Hg0_OW1_V1_18)
N5_V2_18 = len(Hg0_OW1_V2_18)
N5_V3_18 = len(Hg0_OW1_V3_18)

DF5 = [N5_V1_17, N5_V1_18, N5_V2_17, N5_V2_18, N5_V3_17, N5_V3_18]

#-----------------
# Campaign total
#-----------------
# Whole voyage
N_CAMMPCAN1718_All = len(CAMMPCAN1718_All)
N_CAMMPCAN1819_All = len(CAMMPCAN1819_All)
N_CAMMPCAN_OverAll = len(CAMMPCAN_OverAll)

# Sea Ice
N_CAMMPCAN1718_Ice = len(CAMMPCAN1718_Ice)
N_CAMMPCAN1819_Ice = len(CAMMPCAN1819_Ice)
N_CAMMPCAN_IceAll  = len(CAMMPCAN_IceAll)

# Open Water
N_CAMMPCAN1718_OW  = len(CAMMPCAN1718_OW)
N_CAMMPCAN1819_OW  = len(CAMMPCAN1819_OW)
N_CAMMPCAN_OWAll   = len(CAMMPCAN_OWAll)

#------------------------------------------------------------------------------
# CALCULATE THE MEAN HG0

# Whole voyage
V1_17_Mean_All  = np.mean(Hg0_V1_17['ng/m3'])
V2_17_Mean_All  = np.mean(Hg0_V2_17['ng/m3'])
V3_17_Mean_All  = np.mean(Hg0_V3_17M['ng/m3'])

V1_18_Mean_All  = np.mean(Hg0_V1_18['ng/m3'])
V2_18_Mean_All  = np.mean(Hg0_V2_18['ng/m3'])
V3_18_Mean_All  = np.mean(Hg0_V3_18M['ng/m3'])

# Sea ice
V1_17_Mean_S    = np.mean(Hg0_Ice_V1_17['ng/m3'])
V2_17_Mean_S    = np.mean(Hg0_Ice_V2_17['ng/m3'])
V3_17_Mean_S    = np.mean(Hg0_Ice_V3_17['ng/m3'])

V1_18_Mean_S    = np.mean(Hg0_Ice_V1_18['ng/m3'])
V2_18_Mean_S    = np.mean(Hg0_Ice_V2_18['ng/m3'])
V3_18_Mean_S    = np.mean(Hg0_Ice_V3_18['ng/m3'])

# Open water
V1_17_Mean_OW   = np.mean(Hg0_OW_V1_17['ng/m3'])
V2_17_Mean_OW   = np.mean(Hg0_OW_V2_17['ng/m3'])
V3_17_Mean_OW   = np.mean(Hg0_OW_V3_17['ng/m3'])

V1_18_Mean_OW   = np.mean(Hg0_OW_V1_18['ng/m3'])
V2_18_Mean_OW   = np.mean(Hg0_OW_V2_18['ng/m3'])
V3_18_Mean_OW   = np.mean(Hg0_OW_V3_18['ng/m3'])

#-----------------
# Campaign total
#-----------------
# Whole voyage
Mean_CAMMPCAN1718_All = np.mean(CAMMPCAN1718_All)
Mean_CAMMPCAN1819_All = np.mean(CAMMPCAN1819_All)
Mean_CAMMPCAN_OverAll = np.mean(CAMMPCAN_OverAll)

# Sea Ice
Mean_CAMMPCAN1718_Ice = np.mean(CAMMPCAN1718_Ice)
Mean_CAMMPCAN1819_Ice = np.mean(CAMMPCAN1819_Ice)
Mean_CAMMPCAN_IceAll  = np.mean(CAMMPCAN_IceAll)

# Open Water
Mean_CAMMPCAN1718_OW  = np.mean(CAMMPCAN1718_OW)
Mean_CAMMPCAN1819_OW  = np.mean(CAMMPCAN1819_OW)
Mean_CAMMPCAN_OWAll   = np.mean(CAMMPCAN_OWAll)

#------------------------------------------------------------------------------
# CALCULATE THE HG0 STANDARD DEVIATION

# Whole voyage
V1_17_std_All  = np.std(Hg0_V1_17['ng/m3'])
V2_17_std_All  = np.std(Hg0_V2_17['ng/m3'])
V3_17_std_All  = np.std(Hg0_V3_17M['ng/m3'])

V1_18_std_All  = np.std(Hg0_V1_18['ng/m3'])
V2_18_std_All  = np.std(Hg0_V2_18['ng/m3'])
V3_18_std_All  = np.std(Hg0_V3_18M['ng/m3'])

# Sea ice
V1_17_std_S    = np.std(Hg0_Ice_V1_17['ng/m3'])
V2_17_std_S    = np.std(Hg0_Ice_V2_17['ng/m3'])
V3_17_std_S    = np.std(Hg0_Ice_V3_17['ng/m3'])

V1_18_std_S    = np.std(Hg0_Ice_V1_18['ng/m3'])
V2_18_std_S    = np.std(Hg0_Ice_V2_18['ng/m3'])
V3_18_std_S    = np.std(Hg0_Ice_V3_18['ng/m3'])

# Open water
V1_17_std_OW   = np.std(Hg0_OW_V1_17['ng/m3'])
V2_17_std_OW   = np.std(Hg0_OW_V2_17['ng/m3'])
V3_17_std_OW   = np.std(Hg0_OW_V3_17['ng/m3'])

V1_18_std_OW   = np.std(Hg0_OW_V1_18['ng/m3'])
V2_18_std_OW   = np.std(Hg0_OW_V2_18['ng/m3'])
V3_18_std_OW   = np.std(Hg0_OW_V3_18['ng/m3'])

#-----------------
# Campaign total
#-----------------
# Whole voyage
std_CAMMPCAN1718_All = np.std(CAMMPCAN1718_All)
std_CAMMPCAN1819_All = np.std(CAMMPCAN1819_All)
std_CAMMPCAN_OverAll = np.std(CAMMPCAN_OverAll)

# Sea Ice
std_CAMMPCAN1718_Ice = np.std(CAMMPCAN1718_Ice)
std_CAMMPCAN1819_Ice = np.std(CAMMPCAN1819_Ice)
std_CAMMPCAN_IceAll  = np.std(CAMMPCAN_IceAll)

# Open Water
std_CAMMPCAN1718_OW  = np.std(CAMMPCAN1718_OW)
std_CAMMPCAN1819_OW  = np.std(CAMMPCAN1819_OW)
std_CAMMPCAN_OWAll   = np.std(CAMMPCAN_OWAll)

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN HG0

# Whole voyage
V1_17_Median_All  = np.median(Hg0_V1_17['ng/m3'])
V2_17_Median_All  = np.median(Hg0_V2_17['ng/m3'])
V3_17_Median_All  = np.mean(Hg0_V3_17M['ng/m3'])

V1_18_Median_All  = np.median(Hg0_V1_18['ng/m3'])
V2_18_Median_All  = np.median(Hg0_V2_18['ng/m3'])
V3_18_Median_All  = np.mean(Hg0_V3_18M['ng/m3'])

# Sea ice
V1_17_Median_S    = np.median(Hg0_Ice_V1_17['ng/m3'])
V2_17_Median_S    = np.median(Hg0_Ice_V2_17['ng/m3'])
V3_17_Median_S    = np.median(Hg0_Ice_V3_17['ng/m3'])

V1_18_Median_S    = np.median(Hg0_Ice_V1_18['ng/m3'])
V2_18_Median_S    = np.median(Hg0_Ice_V2_18['ng/m3'])
V3_18_Median_S    = np.median(Hg0_Ice_V3_18['ng/m3'])

# Open water
V1_17_Median_OW   = np.median(Hg0_OW_V1_17['ng/m3'])
V2_17_Median_OW   = np.median(Hg0_OW_V2_17['ng/m3'])
V3_17_Median_OW   = np.median(Hg0_OW_V3_17['ng/m3'])

V1_18_Median_OW   = np.median(Hg0_OW_V1_18['ng/m3'])
V2_18_Median_OW   = np.median(Hg0_OW_V2_18['ng/m3'])
V3_18_Median_OW   = np.median(Hg0_OW_V3_18['ng/m3'])

#-----------------
# Campaign total
#-----------------
# Whole voyage
Median_CAMMPCAN1718_All = np.median(CAMMPCAN1718_All)
Median_CAMMPCAN1819_All = np.median(CAMMPCAN1819_All)
Median_CAMMPCAN_OverAll = np.median(CAMMPCAN_OverAll)

# Sea Ice
Median_CAMMPCAN1718_Ice = np.median(CAMMPCAN1718_Ice)
Median_CAMMPCAN1819_Ice = np.median(CAMMPCAN1819_Ice)
Median_CAMMPCAN_IceAll  = np.median(CAMMPCAN_IceAll)

# Open Water
Median_CAMMPCAN1718_OW  = np.median(CAMMPCAN1718_OW)
Median_CAMMPCAN1819_OW  = np.median(CAMMPCAN1819_OW)
Median_CAMMPCAN_OWAll   = np.median(CAMMPCAN_OWAll)

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN ABSOLUTE DEVIATION HG0

# Whole voyage
V1_17_MAD_All = stats.median_absolute_deviation(Hg0_V1_17['ng/m3'])
V2_17_MAD_All = stats.median_absolute_deviation(Hg0_V2_17['ng/m3'])
V3_17_MAD_All = stats.median_absolute_deviation(Hg0_V3_17M['ng/m3'])

V1_18_MAD_All = stats.median_absolute_deviation(Hg0_V1_18['ng/m3'])
V2_18_MAD_All = stats.median_absolute_deviation(Hg0_V2_18['ng/m3'])
V3_18_MAD_All = stats.median_absolute_deviation(Hg0_V3_18M['ng/m3'])

# Sea ice
V1_17_MAD_S   = stats.median_absolute_deviation(Hg0_Ice_V1_17['ng/m3'])
V2_17_MAD_S   = stats.median_absolute_deviation(Hg0_Ice_V2_17['ng/m3'])
V3_17_MAD_S   = stats.median_absolute_deviation(Hg0_Ice_V3_17['ng/m3'])

V1_18_MAD_S   = stats.median_absolute_deviation(Hg0_Ice_V1_18['ng/m3'])
V2_18_MAD_S   = stats.median_absolute_deviation(Hg0_Ice_V2_18['ng/m3'])
V3_18_MAD_S   = stats.median_absolute_deviation(Hg0_Ice_V3_18['ng/m3'])

# Open ocean
V1_17_MAD_OW  = stats.median_absolute_deviation(Hg0_OW_V1_17['ng/m3'])
V2_17_MAD_OW  = stats.median_absolute_deviation(Hg0_OW_V2_17['ng/m3'])
V3_17_MAD_OW  = stats.median_absolute_deviation(Hg0_OW_V3_17['ng/m3'])

V1_18_MAD_OW  = stats.median_absolute_deviation(Hg0_OW_V1_18['ng/m3'])
V2_18_MAD_OW  = stats.median_absolute_deviation(Hg0_OW_V2_18['ng/m3'])
V3_18_MAD_OW  = stats.median_absolute_deviation(Hg0_OW_V3_18['ng/m3'])

#-----------------
# Campaign total
#-----------------
# Whole voyage
MAD_CAMMPCAN1718_All = stats.median_absolute_deviation(CAMMPCAN1718_All)
MAD_CAMMPCAN1819_All = stats.median_absolute_deviation(CAMMPCAN1819_All)
MAD_CAMMPCAN_OverAll = stats.median_absolute_deviation(CAMMPCAN_OverAll)

# Sea Ice
MAD_CAMMPCAN1718_Ice = stats.median_absolute_deviation(CAMMPCAN1718_Ice)
MAD_CAMMPCAN1819_Ice = stats.median_absolute_deviation(CAMMPCAN1819_Ice)
MAD_CAMMPCAN_IceAll  = stats.median_absolute_deviation(CAMMPCAN_IceAll)

# Open Water
MAD_CAMMPCAN1718_OW  = stats.median_absolute_deviation(CAMMPCAN1718_OW)
MAD_CAMMPCAN1819_OW  = stats.median_absolute_deviation(CAMMPCAN1819_OW)
MAD_CAMMPCAN_OWAll   = stats.median_absolute_deviation(CAMMPCAN_OWAll)

#------------------------------------------------------------------------------
# CALCULATE THE MINIMUM HG0

# Whole voyage
V1_17_MIN_All = np.min(Hg0_V1_17['ng/m3'])
V2_17_MIN_All = np.min(Hg0_V2_17['ng/m3'])
V3_17_MIN_All = np.min(Hg0_V3_17M['ng/m3'])

V1_18_MIN_All = np.min(Hg0_V1_18['ng/m3'])
V2_18_MIN_All = np.min(Hg0_V2_18['ng/m3'])
V3_18_MIN_All = np.min(Hg0_V3_18M['ng/m3'])

# Sea ice
V1_17_MIN_S   = np.min(Hg0_Ice_V1_17['ng/m3'])
V2_17_MIN_S   = np.min(Hg0_Ice_V2_17['ng/m3'])
V3_17_MIN_S   = np.min(Hg0_Ice_V3_17['ng/m3'])

V1_18_MIN_S   = np.min(Hg0_Ice_V1_18['ng/m3'])
V2_18_MIN_S   = np.min(Hg0_Ice_V2_18['ng/m3'])
V3_18_MIN_S   = np.min(Hg0_Ice_V3_18['ng/m3'])

# Open water
V1_17_MIN_OW  = np.min(Hg0_OW_V1_17['ng/m3'])
V2_17_MIN_OW  = np.min(Hg0_OW_V2_17['ng/m3'])
V3_17_MIN_OW  = np.min(Hg0_OW_V3_17['ng/m3'])

V1_18_MIN_OW  = np.min(Hg0_OW_V1_18['ng/m3'])
V2_18_MIN_OW  = np.min(Hg0_OW_V2_18['ng/m3'])
V3_18_MIN_OW  = np.min(Hg0_OW_V3_18['ng/m3'])

#-----------------
# Campaign total
#-----------------
# Whole voyage
MIN_CAMMPCAN1718_All = np.min(CAMMPCAN1718_All)
MIN_CAMMPCAN1819_All = np.min(CAMMPCAN1819_All)
MIN_CAMMPCAN_OverAll = np.min(CAMMPCAN_OverAll)

# Sea Ice
MIN_CAMMPCAN1718_Ice = np.min(CAMMPCAN1718_Ice)
MIN_CAMMPCAN1819_Ice = np.min(CAMMPCAN1819_Ice)
MIN_CAMMPCAN_IceAll  = np.min(CAMMPCAN_IceAll)

# Open Water
MIN_CAMMPCAN1718_OW  = np.min(CAMMPCAN1718_OW)
MIN_CAMMPCAN1819_OW  = np.min(CAMMPCAN1819_OW)
MIN_CAMMPCAN_OWAll   = np.min(CAMMPCAN_OWAll)

#------------------------------------------------------------------------------
# PERCENTILES

# 5th
P5_CAMMPCAN1718_All = np.percentile(CAMMPCAN1718_All,    5)
P5_CAMMPCAN1819_All = np.percentile(CAMMPCAN1819_All,    5)
P5_CAMMPCAN_OverAll = np.percentile(CAMMPCAN_OverAll,    5)

# 25th
P25_CAMMPCAN1718_All = np.percentile(CAMMPCAN1718_All,   25)
P25_CAMMPCAN1819_All = np.percentile(CAMMPCAN1819_All,   25)
P25_CAMMPCAN_OverAll = np.percentile(CAMMPCAN_OverAll,   25)

# 75th
P75_CAMMPCAN1718_All = np.percentile(CAMMPCAN1718_All,   75)
P75_CAMMPCAN1819_All = np.percentile(CAMMPCAN1819_All,   75)
P75_CAMMPCAN_OverAll = np.percentile(CAMMPCAN_OverAll,   75)

# 95th
P95_CAMMPCAN1718_All = np.percentile(CAMMPCAN1718_All,   95)
P95_CAMMPCAN1819_All = np.percentile(CAMMPCAN1819_All,   95)
P95_CAMMPCAN_OverAll = np.percentile(CAMMPCAN_OverAll,   95)

#------------------------------------------------------------------------------
# CALCULATE THE MAXIMUM HG0

# Whole voyage
V1_17_MAX_All = np.max(Hg0_V1_17['ng/m3'])
V2_17_MAX_All = np.max(Hg0_V2_17['ng/m3'])
V3_17_MAX_All = np.max(Hg0_V3_17M['ng/m3'])

V1_18_MAX_All = np.max(Hg0_V1_18['ng/m3'])
V2_18_MAX_All = np.max(Hg0_V2_18['ng/m3'])
V3_18_MAX_All = np.max(Hg0_V3_17M['ng/m3'])

# Sea ice
V1_17_MAX_S   = np.max(Hg0_Ice_V1_17['ng/m3'])
V2_17_MAX_S   = np.max(Hg0_Ice_V2_17['ng/m3'])
V3_17_MAX_S   = np.max(Hg0_Ice_V3_17['ng/m3'])

V1_18_MAX_S   = np.max(Hg0_Ice_V1_18['ng/m3'])
V2_18_MAX_S   = np.max(Hg0_Ice_V2_18['ng/m3'])
V3_18_MAX_S   = np.max(Hg0_Ice_V3_18['ng/m3'])

# Open water
V1_17_MAX_OW  = np.max(Hg0_OW_V1_17['ng/m3'])
V2_17_MAX_OW  = np.max(Hg0_OW_V2_17['ng/m3'])
V3_17_MAX_OW  = np.max(Hg0_OW_V3_17['ng/m3'])

V1_18_MAX_OW  = np.max(Hg0_OW_V1_18['ng/m3'])
V2_18_MAX_OW  = np.max(Hg0_OW_V2_18['ng/m3'])
V3_18_MAX_OW  = np.max(Hg0_OW_V3_18['ng/m3'])

#-----------------
# Campaign total
#-----------------
# Whole voyage
MAX_CAMMPCAN1718_All = np.max(CAMMPCAN1718_All)
MAX_CAMMPCAN1819_All = np.max(CAMMPCAN1819_All)
MAX_CAMMPCAN_OverAll = np.max(CAMMPCAN_OverAll)

# Sea Ice
MAX_CAMMPCAN1718_Ice = np.max(CAMMPCAN1718_Ice)
MAX_CAMMPCAN1819_Ice = np.max(CAMMPCAN1819_Ice)
MAX_CAMMPCAN_IceAll  = np.max(CAMMPCAN_IceAll)

# Open Water
MAX_CAMMPCAN1718_OW  = np.max(CAMMPCAN1718_OW)
MAX_CAMMPCAN1819_OW  = np.max(CAMMPCAN1819_OW)
MAX_CAMMPCAN_OWAll   = np.max(CAMMPCAN_OWAll)

#------------------------------------------------------------------------------
# Welches T-Test on Hg0
 
#----------------------
# T-test for the means of 2 indpendent populations
# (Note: unequal sample sizes and/or variance, therefore Welches t-test)
#----------------------

# Between Sea ice & Open water
WT_stat_V1_17,   WT_pval_V1_17   = stats.ttest_ind(Hg0_Ice_V1_17['ng/m3'],  Hg0_OW_V1_17['ng/m3'],   equal_var = False)
WT_stat_V2_17,   WT_pval_V2_17   = stats.ttest_ind(Hg0_Ice_V2_17['ng/m3'],  Hg0_OW_V2_17['ng/m3'],   equal_var = False)
WT_stat_V3_17,   WT_pval_V3_17   = stats.ttest_ind(Hg0_Ice_V3_17['ng/m3'],  Hg0_OW_V3_17['ng/m3'],   equal_var = False)

WT_stat_V1_18,   WT_pval_V1_18   = stats.ttest_ind(Hg0_Ice_V1_18['ng/m3'],  Hg0_OW_V1_18['ng/m3'],   equal_var = False)
WT_stat_V2_18,   WT_pval_V2_18   = stats.ttest_ind(Hg0_Ice_V2_18['ng/m3'],  Hg0_OW_V2_18['ng/m3'],   equal_var = False)
WT_stat_V3_18,   WT_pval_V3_18   = stats.ttest_ind(Hg0_Ice_V3_18['ng/m3'],  Hg0_OW_V3_18['ng/m3'],   equal_var = False)

#-----------------
# Campaign total
#-----------------
WT_stat_CAMP_1718,   WT_pval_CAMP_1718 = stats.ttest_ind(CAMMPCAN1718_Ice, CAMMPCAN1718_OW, equal_var = False)
WT_stat_CAMP_1819,   WT_pval_CAMP_1819 = stats.ttest_ind(CAMMPCAN1819_Ice, CAMMPCAN1819_OW, equal_var = False)
WT_stat_CAMP_All,    WT_pval_CAMP_All  = stats.ttest_ind(CAMMPCAN_IceAll,  CAMMPCAN_OWAll,  equal_var = False)

#------------------------------------------------------------------------------
# KS-Test on BrO (Kolmogorov-Smirnov Test)

# Interannual variability (2017-18 to 2018-19)
#KS_stat_1,       KS_pval_1       = stats.ks_2samp(BrO_V1_17_D,               BrO_V1_18_D,             alternative='two-sided', mode='auto')

# Between Sea ice & Open water
KS_stat_V1_17,   KS_pval_V1_17   = stats.ks_2samp(Hg0_Ice_V1_17['ng/m3'],  Hg0_OW_V1_17['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V2_17,   KS_pval_V2_17   = stats.ks_2samp(Hg0_Ice_V2_17['ng/m3'],  Hg0_OW_V2_17['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_17,   KS_pval_V3_17   = stats.ks_2samp(Hg0_Ice_V3_17['ng/m3'],  Hg0_OW_V3_17['ng/m3'],   alternative='two-sided', mode='auto')

KS_stat_V1_18,   KS_pval_V1_18   = stats.ks_2samp(Hg0_Ice_V1_18['ng/m3'],  Hg0_OW_V1_18['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V2_18,   KS_pval_V2_18   = stats.ks_2samp(Hg0_Ice_V2_18['ng/m3'],  Hg0_OW_V2_18['ng/m3'],   alternative='two-sided', mode='auto')
KS_stat_V3_18,   KS_pval_V3_18   = stats.ks_2samp(Hg0_Ice_V3_18['ng/m3'],  Hg0_OW_V3_18['ng/m3'],   alternative='two-sided', mode='auto')

#-----------------
# Campaign total
#-----------------
KS_stat_CAMP_1718, KS_pval_CAMP_1718 = stats.ks_2samp(CAMMPCAN1718_Ice, CAMMPCAN1718_OW, alternative='two-sided', mode='auto')
KS_stat_CAMP_1819, KS_pval_CAMP_1819 = stats.ks_2samp(CAMMPCAN1819_Ice, CAMMPCAN1819_OW, alternative='two-sided', mode='auto')
KS_stat_CAMP_All,  KS_pval_CAMP_All  = stats.ks_2samp(CAMMPCAN_IceAll,  CAMMPCAN_OWAll,  alternative='two-sided', mode='auto')

#------------------------------------------------------------------------------
#BUILD DATAFRAME FOR THE STATISTICAL RESULTS (VOYAGE)

# Build a pandas dataframe (Voyage Hg0)
dfHg_Stats = {'No_All':         [N1_V1_17,         N1_V2_17,         N1_V3_17M,        N1_V1_18,         N1_V2_18,         N1_V3_18M,        N_CAMMPCAN1718_All,      N_CAMMPCAN1819_All,      N_CAMMPCAN_OverAll],
              'No_S':           [N4_V1_17,         N4_V2_17,         N4_V3_17,         N4_V1_18,         N4_V2_18,         N4_V3_18,         N_CAMMPCAN1718_Ice,      N_CAMMPCAN1819_Ice,      N_CAMMPCAN_IceAll],
              'No_OW':          [N5_V1_17,         N5_V2_17,         N5_V3_17,         N5_V1_18,         N5_V2_18,         N5_V3_18,         N_CAMMPCAN1718_OW,       N_CAMMPCAN1819_OW,       N_CAMMPCAN_OWAll],
              'Mean_All':       [V1_17_Mean_All,   V2_17_Mean_All,   V3_17_Mean_All,   V1_18_Mean_All,   V2_18_Mean_All,   V3_18_Mean_All,   Mean_CAMMPCAN1718_All,   Mean_CAMMPCAN1819_All,   Mean_CAMMPCAN_OverAll],
              'Mean_S':         [V1_17_Mean_S,     V2_17_Mean_S,     V3_17_Mean_S,     V1_18_Mean_S,     V2_18_Mean_S,     V3_18_Mean_S,     Mean_CAMMPCAN1718_Ice,   Mean_CAMMPCAN1819_Ice,   Mean_CAMMPCAN_IceAll],
              'Mean_OW':        [V1_17_Mean_OW,    V2_17_Mean_OW,    V3_17_Mean_OW,    V1_18_Mean_OW,    V2_18_Mean_OW,    V3_18_Mean_OW,    Mean_CAMMPCAN1718_OW,    Mean_CAMMPCAN1819_OW,    Mean_CAMMPCAN_OWAll],
              'StDev_All':      [V1_17_std_All,    V2_17_std_All,    V3_17_std_All,    V1_18_std_All,    V2_18_std_All,    V3_18_std_All,    std_CAMMPCAN1718_All,    std_CAMMPCAN1819_All,    std_CAMMPCAN_OverAll],
              'StDev_S':        [V1_17_std_S,      V2_17_std_S,      V3_17_std_S,      V1_18_std_S,      V2_18_std_S,      V3_18_std_S,      std_CAMMPCAN1718_Ice,    std_CAMMPCAN1819_Ice,    std_CAMMPCAN_IceAll],
              'StDev_OW':       [V1_17_std_OW,     V2_17_std_OW,     V3_17_std_OW,     V1_18_std_OW,     V2_18_std_OW,     V3_18_std_OW,     std_CAMMPCAN1718_OW,     std_CAMMPCAN1819_OW,     std_CAMMPCAN_OWAll],
              'Median_All':     [V1_17_Median_All, V2_17_Median_All, V3_17_Median_All, V1_18_Median_All, V2_18_Median_All, V3_18_Median_All, Median_CAMMPCAN1718_All, Median_CAMMPCAN1819_All, Mean_CAMMPCAN_OverAll],
              'Median_S':       [V1_17_Median_S,   V2_17_Median_S,   V3_17_Median_S,   V1_18_Median_S,   V2_18_Median_S,   V3_18_Median_S,   Median_CAMMPCAN1718_Ice, Median_CAMMPCAN1819_Ice, Mean_CAMMPCAN_IceAll],
              'Median_OW':      [V1_17_Median_OW,  V2_17_Median_OW,  V3_17_Median_OW,  V1_18_Median_OW,  V2_18_Median_OW,  V3_18_Median_OW,  Median_CAMMPCAN1718_OW,  Median_CAMMPCAN1819_OW,  Mean_CAMMPCAN_OWAll],
              'MAD_All':        [V1_17_MAD_All,    V2_17_MAD_All,    V3_17_MAD_All,    V1_18_MAD_All,    V2_18_MAD_All,    V3_18_MAD_All,    MAD_CAMMPCAN1718_All,    MAD_CAMMPCAN1819_All,    MAD_CAMMPCAN_OverAll],
              'MAD_S':          [V1_17_MAD_S,      V2_17_MAD_S,      V3_17_MAD_S,      V1_18_MAD_S,      V2_18_MAD_S,      V3_18_MAD_S,      MAD_CAMMPCAN1718_Ice,    MAD_CAMMPCAN1819_Ice,    MAD_CAMMPCAN_IceAll],
              'MAD_OW':         [V1_17_MAD_OW,     V2_17_MAD_OW,     V3_17_MAD_OW,     V1_18_MAD_OW,     V2_18_MAD_OW,     V3_18_MAD_OW,     MAD_CAMMPCAN1718_OW,     MAD_CAMMPCAN1819_OW,     MAD_CAMMPCAN_OWAll],
              'MIN_All':        [V1_17_MIN_All,    V2_17_MIN_All,    V3_17_MIN_All,    V1_18_MIN_All,    V2_18_MIN_All,    V3_18_MIN_All,    MIN_CAMMPCAN1718_All,    MIN_CAMMPCAN1819_All,    MIN_CAMMPCAN_OverAll],
              'MIN_S':          [V1_17_MIN_S,      V2_17_MIN_S,      V3_17_MIN_S,      V1_18_MIN_S,      V2_18_MIN_S,      V3_18_MIN_S,      MIN_CAMMPCAN1718_Ice,    MIN_CAMMPCAN1819_Ice,    MIN_CAMMPCAN_IceAll],
              'MIN_OW':         [V1_17_MIN_OW,     V2_17_MIN_OW,     V3_17_MIN_OW,     V1_18_MIN_OW,     V2_18_MIN_OW,     V3_18_MIN_OW,     MIN_CAMMPCAN1718_OW,     MIN_CAMMPCAN1819_OW,     MIN_CAMMPCAN_OWAll],
              'MAX_All':        [V1_17_MAX_All,    V2_17_MAX_All,    V3_17_MAX_All,    V1_18_MAX_All,    V2_18_MAX_All,    V3_18_MAX_All,    MAX_CAMMPCAN1718_All,    MAX_CAMMPCAN1819_All,    MAX_CAMMPCAN_OverAll],
              'MAX_S':          [V1_17_MAX_S,      V2_17_MAX_S,      V3_17_MAX_S,      V1_18_MAX_S,      V2_18_MAX_S,      V3_18_MAX_S,      MAX_CAMMPCAN1718_Ice,    MAX_CAMMPCAN1819_Ice,    MAX_CAMMPCAN_IceAll],
              'MAX_OW':         [V1_17_MAX_OW,     V2_17_MAX_OW,     V3_17_MAX_OW,     V1_18_MAX_OW,     V2_18_MAX_OW,     V3_18_MAX_OW,     MAX_CAMMPCAN1718_OW,     MAX_CAMMPCAN1819_OW,     MAX_CAMMPCAN_OWAll],
              'Welches (stat)': [WT_stat_V1_17,    WT_stat_V2_17,    WT_stat_V3_17,    WT_stat_V1_18,    WT_stat_V2_18,    WT_stat_V3_18,    WT_stat_CAMP_1718,       WT_stat_CAMP_1819,       WT_stat_CAMP_All],
              'Welches (pval)': [WT_pval_V1_17,    WT_pval_V2_17,    WT_pval_V3_17,    WT_pval_V1_18,    WT_pval_V2_18,    WT_pval_V3_18,    WT_pval_CAMP_1718,       WT_pval_CAMP_1819,       WT_pval_CAMP_All],
              'KS-Test (stat)': [KS_stat_V1_17,    KS_stat_V2_17,    KS_stat_V3_17,    KS_stat_V1_18,    KS_stat_V2_18,    KS_stat_V3_18,    KS_stat_CAMP_1718,       KS_stat_CAMP_1819,       KS_stat_CAMP_All],
              'KS-Test (pval)': [KS_pval_V1_17,    KS_pval_V2_17,    KS_pval_V3_17,    KS_pval_V1_18,    KS_pval_V2_18,    KS_pval_V3_18,    KS_pval_CAMP_1718,       KS_pval_CAMP_1819,       KS_pval_CAMP_All]}
dfHg_Stats = pd.DataFrame(dfHg_Stats, columns = ['No_All','No_S','No_OW','Mean_All','Mean_S','Mean_OW','StDev_All','StDev_S','StDev_OW',
                                                 'Median_All','Median_S','Median_OW','MAD_All','MAD_S','MAD_OW','MIN_All','MIN_S',
                                                 'MIN_OW','MAX_All','MAX_S','MAX_OW','Welches (stat)','Welches (pval)','KS-Test (stat)','KS-Test (pval)'],
                          index = ['V1_17','V2_17','V3_17','V1_18','V2_18','V3_18','CAMP1718','CAMP1819','CAMMPALL'])
#dfHg_Stats = dfHg_Stats.T
dfHg_Stats.to_csv('/Users/ncp532/Documents/Data/Antarctic_Hg/Hg_Stats_SeaIceOpenWater.csv')

# #------------------------------------------------------------------------------
# # PLOT THE GRAPH
# # Graph 1
# fig1, ax1 = plt.subplots()

# # option 1, specify props dictionaries
# c1 = "black"
# c2 = "blue"

# box1 = ax1.boxplot(data1, positions=[1,2,3,4,5], notch=True, patch_artist=True,
#             boxprops=dict(facecolor=c2, color=c1),
#             capprops=dict(color=c1),
#             whiskerprops=dict(color=c1),
#             flierprops=dict(color=c1, markeredgecolor=c1),
#             medianprops=dict(color=c1),widths=(0.25,0.25,0.25,0.25,0.25)
#             )

# # option 2, set all colors individually
# c3 = "black"
# c4 = "red"
# box2 = ax1.boxplot(data2, positions=[1.5,2.5,3.5,4.5,5.5], notch=True, patch_artist=True,widths=(0.25,0.25,0.25,0.25,0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box2[item], color=c3)
# plt.setp(box2["boxes"], facecolor=c4)
# plt.setp(box2["fliers"], markeredgecolor=c3)

# # option 2, set all colors individually
# c5 = "black"
# c6 = "green"
# box3 = ax1.boxplot(data3, positions=[6], notch=True, patch_artist=True,widths=(0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box3[item], color=c5)
# plt.setp(box3["boxes"], facecolor=c6)
# plt.setp(box3["fliers"], markeredgecolor=c5)

# c7 = "black"
# c8 = "orange"
# box4 = ax1.boxplot(data4, positions=[6.5], notch=True, patch_artist=True,widths=(0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box4[item], color=c7)
# plt.setp(box4["boxes"], facecolor=c8)
# plt.setp(box4["fliers"], markeredgecolor=c7)

# for i, v in enumerate(DF1):
#     ax1.text((i/2)+0.85 ,v/DF1[i]-1.1,j + str(DF1[i]),fontsize=10,color='black',fontweight='bold')
    
# plt.xlim(0.5,7)
# plt.ylim(-0.2,1.6)
# #plt.xticks([1,1.5,2,2.5,3,3.5],['Davis V1\n(2017-18)','Davis V1\n(2018-19)','Casey V2\n(2017-18)','Casey V2\n(2018-19)','Mawson V3\n(2017-18)','Mawson V3\n(2018-19)'])
# plt.xticks([1.25,2.25,3.25,4.25,5.25,6,6.5],['Davis (V1)','Casey (V2)','Mawson (V3)','Davis (V3)','Macquarie\nIsland (V4)','SIPEXII','PCAN'])
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.set_title('Hg$^0$ concentrations for CAMMPCAN, SIPEXII and PCAN',fontsize=20,y=1.02)
# ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=16, labelpad=15)
# ax1.set_xlabel('Voyage', fontsize=16, labelpad=15)
# ax1.legend([box1["boxes"][0], box2["boxes"][0], box3["boxes"][0], box4["boxes"][0]],['2017-18', '2018-19', '2012', '2017'], loc='upper left',title='Season')
# plt.show()

# #--------------------------
# # Graph 2
# fig2, ax1 = plt.subplots()

# # option 1, specify props dictionaries
# c1 = "black"
# c2 = "blue"

# box1 = ax1.boxplot(data5, positions=[1,2,3,4,5], notch=True, patch_artist=True,
#             boxprops=dict(facecolor=c2, color=c1),
#             capprops=dict(color=c1),
#             whiskerprops=dict(color=c1),
#             flierprops=dict(color=c1, markeredgecolor=c1),
#             medianprops=dict(color=c1),widths=(0.25,0.25,0.25,0.25,0.25)
#             )

# # option 2, set all colors individually
# c3 = "black"
# c4 = "red"
# box2 = ax1.boxplot(data6, positions=[1.5,2.5,3.5,4.5,5.5], notch=True, patch_artist=True,widths=(0.25,0.25,0.25,0.25,0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box2[item], color=c3)
# plt.setp(box2["boxes"], facecolor=c4)
# plt.setp(box2["fliers"], markeredgecolor=c3)

# # option 2, set all colors individually
# c5 = "black"
# c6 = "green"
# box3 = ax1.boxplot(data7, positions=[6], notch=True, patch_artist=True,widths=(0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box3[item], color=c5)
# plt.setp(box3["boxes"], facecolor=c6)
# plt.setp(box3["fliers"], markeredgecolor=c5)

# c7 = "black"
# c8 = "orange"
# box4 = ax1.boxplot(data8, positions=[6.5], notch=True, patch_artist=True,widths=(0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box4[item], color=c7)
# plt.setp(box4["boxes"], facecolor=c8)
# plt.setp(box4["fliers"], markeredgecolor=c7)

# for i, v in enumerate(DF2):
#     ax1.text((i/2)+0.85 ,v/DF2[i]-1.1,j + str(DF2[i]),fontsize=10,color='black',fontweight='bold')
    
# plt.xlim(0.5,7)
# plt.ylim(-0.2,1.6)
# #plt.xticks([1,1.5,2,2.5,3,3.5],['Davis V1\n(2017-18)','Davis V1\n(2018-19)','Casey V2\n(2017-18)','Casey V2\n(2018-19)','Mawson V3\n(2017-18)','Mawson V3\n(2018-19)'])
# plt.xticks([1.25,2.25,3.25,4.25,5.25,6,6.5],['Davis (V1)','Casey (V2)','Mawson (V3)','Davis (V3)','Macquarie\nIsland (V4)','SIPEXII','PCAN'])
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.set_title('Hg$^0$ concentrations for CAMMPCAN, SIPEXII and PCAN',fontsize=20,y=1.02)
# ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=16, labelpad=15)
# ax1.set_xlabel('Voyage', fontsize=16, labelpad=15)
# ax1.legend([box1["boxes"][0], box2["boxes"][0], box3["boxes"][0], box4["boxes"][0]],['2017-18', '2018-19', '2012', '2017'], loc='upper left',title='Season')
# plt.show()

# #--------------------------
# # Graph 3
# fig3, ax1 = plt.subplots()

# # option 1, specify props dictionaries
# c1 = "black"
# c2 = "blue"

# box1 = ax1.boxplot(data9, positions=[1,2,3,4,5], notch=True, patch_artist=True,
#             boxprops=dict(facecolor=c2, color=c1),
#             capprops=dict(color=c1),
#             whiskerprops=dict(color=c1),
#             flierprops=dict(color=c1, markeredgecolor=c1),
#             medianprops=dict(color=c1),widths=(0.25,0.25,0.25,0.25,0.25)
#             )

# # option 2, set all colors individually
# c3 = "black"
# c4 = "red"
# box2 = ax1.boxplot(data10, positions=[1.5,2.5,3.5,4.5,5.5], notch=True, patch_artist=True,widths=(0.25,0.25,0.25,0.25,0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box2[item], color=c3)
# plt.setp(box2["boxes"], facecolor=c4)
# plt.setp(box2["fliers"], markeredgecolor=c3)

# # option 2, set all colors individually
# c5 = "black"
# c6 = "green"
# box3 = ax1.boxplot(data11, positions=[6], notch=True, patch_artist=True,widths=(0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box3[item], color=c5)
# plt.setp(box3["boxes"], facecolor=c6)
# plt.setp(box3["fliers"], markeredgecolor=c5)

# c7 = "black"
# c8 = "orange"
# box4 = ax1.boxplot(data12, positions=[6.5], notch=True, patch_artist=True,widths=(0.25))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box4[item], color=c7)
# plt.setp(box4["boxes"], facecolor=c8)
# plt.setp(box4["fliers"], markeredgecolor=c7)

# for i, v in enumerate(DF3):
#     ax1.text((i/2)+0.85 ,v/DF3[i]-1.1,j + str(DF3[i]),fontsize=10,color='black',fontweight='bold')
    
# plt.xlim(0.5,7)
# plt.ylim(-0.2,1.6)
# #plt.xticks([1,1.5,2,2.5,3,3.5],['Davis V1\n(2017-18)','Davis V1\n(2018-19)','Casey V2\n(2017-18)','Casey V2\n(2018-19)','Mawson V3\n(2017-18)','Mawson V3\n(2018-19)'])
# plt.xticks([1.25,2.25,3.25,4.25,5.25,6,6.5],['Davis (V1)','Casey (V2)','Mawson (V3)','Davis (V3)','Macquarie\nIsland (V4)','SIPEXII','PCAN'])
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.set_title('Hg$^0$ concentrations for CAMMPCAN, SIPEXII and PCAN',fontsize=20,y=1.02)
# ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=16, labelpad=15)
# ax1.set_xlabel('Voyage', fontsize=16, labelpad=15)
# ax1.legend([box1["boxes"][0], box2["boxes"][0], box3["boxes"][0], box4["boxes"][0]],['2017-18', '2018-19', '2012', '2017'], loc='upper left',title='Season')
# plt.show()

# #--------------------------
# # Graph 4
# fig4, ax1 = plt.subplots()

# #-----------------
# # Whole voyage
# #-----------------
# # option 1, specify props dictionaries
# c1 = "black"
# c2 = "blue"

# box1 = ax1.boxplot(data1, positions=[0.7,1.7,2.7,3.7,4.7], notch=True, patch_artist=True,
#             boxprops=dict(facecolor=c2, color=c1),
#             capprops=dict(color=c1),
#             whiskerprops=dict(color=c1),
#             flierprops=dict(color=c1, markeredgecolor=c1),
#             medianprops=dict(color=c1),widths=(0.12,0.12,0.12,0.12,0.12)
#             )

# # option 2, set all colors individually
# c3 = "black"
# c4 = "red"
# box2 = ax1.boxplot(data2, positions=[1.2,2.2,3.2,4.2,5.2], notch=True, patch_artist=True,widths=(0.12,0.12,0.12,0.12,0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box2[item], color=c3)
# plt.setp(box2["boxes"], facecolor=c4)
# plt.setp(box2["fliers"], markeredgecolor=c3)

# # option 2, set all colors individually
# c5 = "black"
# c6 = "green"
# box3 = ax1.boxplot(data3, positions=[5.7], notch=True, patch_artist=True,widths=(0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box3[item], color=c5)
# plt.setp(box3["boxes"], facecolor=c6)
# plt.setp(box3["fliers"], markeredgecolor=c5)

# c7 = "black"
# c8 = "orange"
# box4 = ax1.boxplot(data4, positions=[6.2], notch=True, patch_artist=True,widths=(0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box4[item], color=c7)
# plt.setp(box4["boxes"], facecolor=c8)
# plt.setp(box4["fliers"], markeredgecolor=c7)

# for i, v in enumerate(DF1):
#     ax1.text((i/2)+0.85 ,v/DF1[i]-1.1,j + str(DF1[i]),fontsize=10,color='black',fontweight='bold')

# #-----------------
# # At station
# #-----------------
# # option 1, specify props dictionaries
# c1 = "black"
# c2 = "blue"

# box1 = ax1.boxplot(data5, positions=[0.82,1.82,2.82,3.82,4.82], notch=True, patch_artist=True,
#             boxprops=dict(facecolor=c2, color=c1),
#             capprops=dict(color=c1),
#             whiskerprops=dict(color=c1),
#             flierprops=dict(color=c1, markeredgecolor=c1),
#             medianprops=dict(color=c1),widths=(0.12,0.12,0.12,0.12,0.12)
#             )

# # option 2, set all colors individually
# c3 = "black"
# c4 = "red"
# box2 = ax1.boxplot(data6, positions=[1.32,2.32,3.32,4.32,5.32], notch=True, patch_artist=True,widths=(0.12,0.12,0.12,0.12,0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box2[item], color=c3)
# plt.setp(box2["boxes"], facecolor=c4)
# plt.setp(box2["fliers"], markeredgecolor=c3)

# # option 2, set all colors individually
# c5 = "black"
# c6 = "green"
# box3 = ax1.boxplot(data7, positions=[5.82], notch=True, patch_artist=True,widths=(0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box3[item], color=c5)
# plt.setp(box3["boxes"], facecolor=c6)
# plt.setp(box3["fliers"], markeredgecolor=c5)

# c7 = "black"
# c8 = "orange"
# box4 = ax1.boxplot(data8, positions=[6.32], notch=True, patch_artist=True,widths=(0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box4[item], color=c7)
# plt.setp(box4["boxes"], facecolor=c8)
# plt.setp(box4["fliers"], markeredgecolor=c7)

# for i, v in enumerate(DF2):
#     ax1.text((i/2)+0.85 ,v/DF2[i]-1.1,j + str(DF2[i]),fontsize=10,color='black',fontweight='bold')

# #-----------------
# # Open water
# #-----------------
# # option 1, specify props dictionaries
# c1 = "black"
# c2 = "blue"

# box1 = ax1.boxplot(data9, positions=[0.94,1.94,2.94,3.94,4.94], notch=True, patch_artist=True,
#             boxprops=dict(facecolor=c2, color=c1),
#             capprops=dict(color=c1),
#             whiskerprops=dict(color=c1),
#             flierprops=dict(color=c1, markeredgecolor=c1),
#             medianprops=dict(color=c1),widths=(0.12,0.12,0.12,0.12,0.12)
#             )

# # option 2, set all colors individually
# c3 = "black"
# c4 = "red"
# box2 = ax1.boxplot(data10, positions=[1.44,2.44,3.44,4.44,5.44], notch=True, patch_artist=True,widths=(0.12,0.12,0.12,0.12,0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box2[item], color=c3)
# plt.setp(box2["boxes"], facecolor=c4)
# plt.setp(box2["fliers"], markeredgecolor=c3)

# # option 2, set all colors individually
# c5 = "black"
# c6 = "green"
# box3 = ax1.boxplot(data11, positions=[5.92], notch=True, patch_artist=True,widths=(0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box3[item], color=c5)
# plt.setp(box3["boxes"], facecolor=c6)
# plt.setp(box3["fliers"], markeredgecolor=c5)

# c7 = "black"
# c8 = "orange"
# box4 = ax1.boxplot(data12, positions=[6.44], notch=True, patch_artist=True,widths=(0.12))
# for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
#         plt.setp(box4[item], color=c7)
# plt.setp(box4["boxes"], facecolor=c8)
# plt.setp(box4["fliers"], markeredgecolor=c7)

# for i, v in enumerate(DF3):
#     ax1.text((i/2)+0.85 ,v/DF3[i]-1.1,j + str(DF3[i]),fontsize=10,color='black',fontweight='bold')
    
# plt.xlim(0.2,6.94)
# plt.ylim(-0.2,1.6)
# #plt.xticks([1,1.5,2,2.5,3,3.5],['Davis V1\n(2017-18)','Davis V1\n(2018-19)','Casey V2\n(2017-18)','Casey V2\n(2018-19)','Mawson V3\n(2017-18)','Mawson V3\n(2018-19)'])
# plt.xticks([0.95,1.95,2.95,3.95,4.95,5.82,6.32],['Davis (V1)','Casey (V2)','Mawson (V3)','Davis (V3)','Macquarie\nIsland (V4)','SIPEXII','PCAN'])
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

# ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax1.set_title('Hg$^0$ concentrations for CAMMPCAN, SIPEXII and PCAN',fontsize=20,y=1.02)
# ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=16, labelpad=15)
# ax1.set_xlabel('Voyage', fontsize=16, labelpad=15)
# ax1.legend([box1["boxes"][0], box2["boxes"][0], box3["boxes"][0], box4["boxes"][0]],['2017-18', '2018-19', '2012', '2017'], loc='upper left',title='Season')
# plt.show()

#--------------------------
# Graph 5
fig5, ax1 = plt.subplots()

#-----------------
# On station
#-----------------
# option 1, specify props dictionaries
c1 = "black"
c2 = "blue"

box1 = ax1.boxplot(data5, positions=[0.73,1.73,2.73,3.73,4.73], notch=True, showfliers=False, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.18,0.18,0.18,0.18,0.18)
            )

# option 2, set all colors individually
c3 = "black"
c4 = "red"
box2 = ax1.boxplot(data6, positions=[1.19,2.19,3.19,4.19,5.19], notch=True, showfliers=False, patch_artist=True, widths=(0.18,0.18,0.18,0.18,0.18))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box2[item], color=c3)
plt.setp(box2["boxes"], facecolor=c4)
plt.setp(box2["fliers"], markeredgecolor=c3)

# option 2, set all colors individually
c5 = "black"
c6 = "green"
box3 = ax1.boxplot(data7, positions=[5.73], notch=True, showfliers=False, patch_artist=True, widths=(0.18))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3[item], color=c5)
plt.setp(box3["boxes"], facecolor=c6)
plt.setp(box3["fliers"], markeredgecolor=c5)

c7 = "black"
c8 = "orange"
box4 = ax1.boxplot(data8, positions=[6.19], notch=True, showfliers=False, patch_artist=True, widths=(0.18))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4[item], color=c7)
plt.setp(box4["boxes"], facecolor=c8)
plt.setp(box4["fliers"], markeredgecolor=c7)

for i, v in enumerate(DF2):
    ax1.text((i/2)+0.6 ,v/DF2[i]-1.1,j + str(DF2[i]),fontsize=12,color='black',fontweight='bold')

#-----------------
# Off station
#-----------------
# option 1, specify props dictionaries
c1 = "black"
c2 = "blue"

box5 = ax1.boxplot(data9, positions=[0.91,1.91,2.91,3.91,4.91], notch=True, showfliers=False, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.18,0.18,0.18,0.18,0.18)
            )
plt.setp(box5["boxes"], hatch = '///')

# option 2, set all colors individually
c3 = "black"
c4 = "red"
box6 = ax1.boxplot(data10, positions=[1.37,2.37,3.37,4.37,5.37], notch=True, showfliers=False, patch_artist=True, widths=(0.18,0.18,0.18,0.18,0.18))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box6[item], color=c3)
plt.setp(box6["boxes"], facecolor=c4)
plt.setp(box6["fliers"], markeredgecolor=c3)
plt.setp(box6["boxes"], hatch = '///')

# option 2, set all colors individually
c5 = "black"
c6 = "green"
box7 = ax1.boxplot(data11, positions=[5.91], notch=True, showfliers=False, patch_artist=True, widths=(0.18))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box7[item], color=c5)
plt.setp(box7["boxes"], facecolor=c6)
plt.setp(box7["fliers"], markeredgecolor=c5)
plt.setp(box7["boxes"], hatch = '///')

c7 = "black"
c8 = "orange"
box8 = ax1.boxplot(data12, positions=[6.37], notch=True, showfliers=False, patch_artist=True, widths=(0.18))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box8[item], color=c7)
plt.setp(box8["boxes"], facecolor=c8)
plt.setp(box8["fliers"], markeredgecolor=c7)
plt.setp(box8["boxes"], hatch = '///')

for i, v in enumerate(DF3):
    ax1.text((i/2)+0.6 ,v/DF3[i]-1.15,j + str(DF3[i]),fontsize=12,color='dimgrey',fontweight='bold')

# Plot vertical lines to seperate each voyage
plt.axvline(1.54, linewidth=0.5, color='grey')
plt.axvline(2.54, linewidth=0.5, color='grey')
plt.axvline(3.54, linewidth=0.5, color='grey')
plt.axvline(4.54, linewidth=0.5, color='grey')
plt.axvline(5.54, linewidth=0.5, color='grey')
plt.axvline(6.05, linewidth=0.5, color='grey')
    
plt.xlim(0.33,6.77)
plt.ylim(-0.2,1.5)
#plt.xticks([1,1.5,2,2.5,3,3.5],['Davis V1\n(2017-18)','Davis V1\n(2018-19)','Casey V2\n(2017-18)','Casey V2\n(2018-19)','Mawson V3\n(2017-18)','Mawson V3\n(2018-19)'])
plt.xticks([1.04,2.04,3.04,4.04,5.04,5.795,6.41],['Davis (V1)','Casey (V2)','Mawson (V3)','Davis (V3)','Macquarie\nIsland (V4)','SIPEXII','PCAN'],fontsize=15)
plt.yticks(fontsize=15)

ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax1.set_title('Hg$^0$ concentrations for CAMMPCAN, SIPEXII and PCAN',fontsize=20,y=1.02)
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=20, labelpad=15)
ax1.set_xlabel('Voyage', fontsize=20, labelpad=15)
lg = ax1.legend([box1["boxes"][0], box2["boxes"][0], box3["boxes"][0], box4["boxes"][0]],['2017-18', '2018-19', '2012', '2017'], loc='upper left',title='Season',fontsize=15)
lg.get_title().set_fontsize(15)
plt.show()

#--------------------------
# Graph 6
fig6, ax1 = plt.subplots()

#-----------------
# Sea Ice
#-----------------
# option 1, specify props dictionaries
c1 = "black"
c2 = "blue"

box1 = ax1.boxplot(data13, positions=[0.73,1.73,2.73], notch=True, showfliers=False, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.18,0.18,0.18)
            )

# option 2, set all colors individually
c3 = "black"
c4 = "red"
box2 = ax1.boxplot(data14, positions=[1.19,2.19,3.19], notch=True, showfliers=False, patch_artist=True, widths=(0.18,0.18,0.18))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box2[item], color=c3)
plt.setp(box2["boxes"], facecolor=c4)
plt.setp(box2["fliers"], markeredgecolor=c3)

for i, v in enumerate(DF4):
    ax1.text((i/2)+0.6 ,v/DF4[i]-1.1,j + str(DF4[i]),fontsize=12,color='black',fontweight='bold')

#-----------------
# Open water
#-----------------
# option 1, specify props dictionaries
c1 = "black"
c2 = "blue"

box3 = ax1.boxplot(data15, positions=[0.91,1.91,2.91], notch=True, showfliers=False, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.18,0.18,0.18)
            )
plt.setp(box3["boxes"], hatch = '///')

# option 2, set all colors individually
c3 = "black"
c4 = "red"
box4 = ax1.boxplot(data16, positions=[1.37,2.37,3.37], notch=True, showfliers=False, patch_artist=True, widths=(0.18,0.18,0.18))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4[item], color=c3)
plt.setp(box4["boxes"], facecolor=c4)
plt.setp(box4["fliers"], markeredgecolor=c3)
plt.setp(box4["boxes"], hatch = '///')

for i, v in enumerate(DF5):
    ax1.text((i/2)+0.6 ,v/DF5[i]-1.15,j + str(DF5[i]),fontsize=12,color='dimgrey',fontweight='bold')

# Plot vertical lines to seperate each voyage
plt.axvline(1.54, linewidth=0.5, color='grey')
plt.axvline(2.54, linewidth=0.5, color='grey')
    
plt.xlim(0.33,3.64)
plt.ylim(-0.2,1.5)
#plt.xticks([1,1.5,2,2.5,3,3.5],['Davis V1\n(2017-18)','Davis V1\n(2018-19)','Casey V2\n(2017-18)','Casey V2\n(2018-19)','Mawson V3\n(2017-18)','Mawson V3\n(2018-19)'])
plt.xticks([1.04,2.04,3.04],['V1','V2','V3'],fontsize=15)
plt.yticks(fontsize=15)

ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax1.set_title('Hg$^0$ concentrations for CAMMPCAN, SIPEXII and PCAN',fontsize=20,y=1.02)
ax1.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=20, labelpad=15)
ax1.set_xlabel('Voyage', fontsize=20, labelpad=15)
lg = ax1.legend([box1["boxes"][0], box3["boxes"][0],box2["boxes"][0], box4["boxes"][0]],['2017-18', '2018-19','2017-18', '2018-19'], loc='upper left',title='Season',fontsize=15)
lg.get_title().set_fontsize(15)
plt.show()