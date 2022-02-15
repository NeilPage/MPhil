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
import matplotlib.gridspec as gridspec
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# REACTIVE MERCURY
DF1 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_RM_Deployment.csv')

# Hg0
PCAN    = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/PCAN_Hg0_QAQC_2017.csv')

V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_QAQC_17-18.csv')
V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_QAQC_17-18.csv')
V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_QAQC_17-18.csv')
V4_17   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V4_Hg0_QAQC_17-18.csv')

V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_QAQC_18-19.csv')
V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_QAQC_18-19.csv')
V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_QAQC_18-19.csv')
V4_18   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V4_Hg0_QAQC_18-19.csv')

# BrO
V1_17_B = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Data.csv', header=0,encoding = 'unicode_escape')
V2_17_B = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V2_17_Data.csv', header=0,encoding = 'unicode_escape')
V3_17_B = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V3_17_Data.csv', header=0,encoding = 'unicode_escape')

V1_18_B = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_18_Data.csv', header=0,encoding = 'unicode_escape')
V2_18_B = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V2_18_Data.csv', header=0,encoding = 'unicode_escape')
V3_18_B = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V3_18_Data.csv', header=0,encoding = 'unicode_escape')

# Met Data
PCAN_C = pd.read_csv('/Users/ncp532/Documents/Data/PCAN_2017/PCAN_underway_data.csv')

V1_17_C = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv') 
V2_17_C = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv') 
V3_17_C = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv') 
V4_17_C = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V04/CAMMPCAN_V4_underway_60.csv') 

V1_18_C = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv') 
V2_18_C = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv') 
V3_18_C = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv') 
V4_18_C = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V04/CAMMPCAN_V4_underway_60.csv') 

#------------------------------------------------------------------------------
# Set the date

# Hg0
PCAN['DateTime']  = pd.to_datetime(PCAN['DateTime'],  dayfirst=True)

V1_17['DateTime'] = pd.to_datetime(V1_17['DateTime'], dayfirst=True)
V2_17['DateTime'] = pd.to_datetime(V2_17['DateTime'], dayfirst=True)
V3_17['DateTime'] = pd.to_datetime(V3_17['DateTime'], dayfirst=True)
V4_17['DateTime'] = pd.to_datetime(V4_17['DateTime'], dayfirst=True)

V1_18['DateTime'] = pd.to_datetime(V1_18['DateTime'], dayfirst=True)
V2_18['DateTime'] = pd.to_datetime(V2_18['DateTime'], dayfirst=True)
V3_18['DateTime'] = pd.to_datetime(V3_18['DateTime'], dayfirst=True)
V4_18['DateTime'] = pd.to_datetime(V4_18['DateTime'], dayfirst=True)

# BrO
V1_17_B['DateTime'] = pd.to_datetime(V1_17_B['DateTime'], dayfirst=True)
V2_17_B['DateTime'] = pd.to_datetime(V2_17_B['DateTime'], dayfirst=True)
V3_17_B['DateTime'] = pd.to_datetime(V3_17_B['DateTime'], dayfirst=True)

V1_18_B['DateTime'] = pd.to_datetime(V1_18_B['DateTime'], dayfirst=True)
V2_18_B['DateTime'] = pd.to_datetime(V2_18_B['DateTime'], dayfirst=True)
V3_18_B['DateTime'] = pd.to_datetime(V3_18_B['DateTime'], dayfirst=True)

# Met Data
PCAN_C['DateTime']  = pd.to_datetime(PCAN_C['DateTime'],  dayfirst=True)

V1_17_C['DateTime'] = pd.to_datetime(V1_17_C['DateTime'], dayfirst=True)
V2_17_C['DateTime'] = pd.to_datetime(V2_17_C['DateTime'], dayfirst=True)
V3_17_C['DateTime'] = pd.to_datetime(V3_17_C['DateTime'], dayfirst=True)
V4_17_C['DateTime'] = pd.to_datetime(V4_17_C['DateTime'], dayfirst=True)

V1_18_C['DateTime'] = pd.to_datetime(V1_18_C['DateTime'], dayfirst=True)
V2_18_C['DateTime'] = pd.to_datetime(V2_18_C['DateTime'], dayfirst=True)
V3_18_C['DateTime'] = pd.to_datetime(V3_18_C['DateTime'], dayfirst=True)
V4_18_C['DateTime'] = pd.to_datetime(V4_18_C['DateTime'], dayfirst=True)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

#-----------------------------
# CAMMPCAN 2017-18
#-----------------------------
# V1_17 Davis (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V1_17_B['Time'] >= start_time) & (V1_17_B['Time'] < end_time)
V1_17_BrO = V1_17_B[Midday]

# V2_17 Casey (08:00 to 16:00)
start_time = '08:00:00'
end_time = '16:00:00'
Midday = (V2_17_B['Time'] >= start_time) & (V2_17_B['Time'] < end_time)
V2_17_BrO = V2_17_B[Midday]

# V3_17 Mawson (08:00 to 18:00)
start_time = '08:00:00'
end_time = '18:00:00'
Midday = (V3_17_B['Time'] >= start_time) & (V3_17_B['Time'] < end_time)
V3_17_BrO = V3_17_B[Midday]

#-----------------------------
# CAMMPCAN 2018-19
#-----------------------------
# V1_18 Davis (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V1_18_B['Time'] >= start_time) & (V1_18_B['Time'] < end_time)
V1_18_BrO = V1_18_B[Midday]

# V2_18 Casey (08:00 to 16:00)
start_time = '08:00:00'
end_time = '16:00:00'
Midday = (V2_18_B['Time'] >= start_time) & (V2_18_B['Time'] < end_time)
V2_18_BrO = V2_18_B[Midday]

# V3_18 Mawson (08:00 to 18:00)
start_time = '08:00:00'
end_time = '18:00:00'
Midday = (V3_18_B['Time'] >= start_time) & (V3_18_B['Time'] < end_time)
V3_18_BrO = V3_18_B[Midday]

#------------------------------------------------------------------------------
# Filter dataframe for when filter is less than 60%

V1_17F    = (V1_17_BrO['Filter'] < 0.6)
V1_17_BrO = V1_17_BrO[V1_17F]

V2_17F    = (V2_17_BrO['Filter'] < 0.6)
V2_17_BrO = V2_17_BrO[V2_17F]

V3_17F    = (V3_17_BrO['Filter'] < 0.6)
V3_17_BrO = V3_17_BrO[V3_17F]

V1_18F    = (V1_18_BrO['Filter'] < 0.6)
V1_18_BrO = V1_18_BrO[V1_18F]

V2_18F    = (V2_18_BrO['Filter'] < 0.6)
V2_18_BrO = V2_18_BrO[V2_18F]

V3_18F    = (V3_18_BrO['Filter'] < 0.6)
V3_18_BrO = V3_18_BrO[V3_18F]

#------------------------------------------------------------------------------
# Filter the datasets for each deplyment

#-----------------------------
# PCAN 2017
#-----------------------------
S1 = '2017-01-10'
E1 = '2017-01-27'
Filter1 = (PCAN['DateTime'] >= S1) & (PCAN['DateTime'] < E1)
PCAN_D1 = PCAN[Filter1]

S2 = '2017-01-27'
E2 = '2017-02-10'
Filter2 = (PCAN['DateTime'] >= S2) & (PCAN['DateTime'] < E2)
PCAN_D2 = PCAN[Filter2]

S3 = '2017-02-10'
E3 = '2017-02-24'
Filter3 = (PCAN['DateTime'] >= S3) & (PCAN['DateTime'] < E3)
PCAN_D3 = PCAN[Filter3]

S4 = '2017-02-24'
E4 = '2017-03-05'
Filter4 = (PCAN['DateTime'] >= S4) & (PCAN['DateTime'] < E4)
PCAN_D4 = PCAN[Filter4]

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
# V1_17 Davis
S1 = '2017-11-01'
E1 = '2017-11-13'
Filter1  = (V1_17['DateTime'] >= S1) & (V1_17['DateTime'] < E1)
V1_17_D1 = V1_17[Filter1]

S2 = '2017-11-13'
E2 = '2017-11-24'
Filter2  = (V1_17['DateTime'] >= S2) & (V1_17['DateTime'] < E2)
V1_17_D2 = V1_17[Filter2]

S3 = '2017-11-24'
E3 = '2017-12-03'
Filter3  = (V1_17['DateTime'] >= S3) & (V1_17['DateTime'] < E3)
V1_17_D3 = V1_17[Filter3]

# V2_17 Casey
S1 = '2017-12-02'
E1 = '2017-12-27'
Filter1  = (V2_17['DateTime'] >= S1) & (V2_17['DateTime'] < E1)
V2_17_D1 = V2_17[Filter1]

S2 = '2017-12-27'
E2 = '2018-01-04'
Filter2  = (V2_17['DateTime'] >= S2) & (V2_17['DateTime'] < E2)
V2_17_D2 = V2_17[Filter2]

S3 = '2018-01-04'
E3 = '2018-01-12'
Filter3  = (V2_17['DateTime'] >= S3) & (V2_17['DateTime'] < E3)
V2_17_D3 = V2_17[Filter3]

# V3_17 Mawson
S1 = '2018-01-12'
E1 = '2018-02-05'
Filter1  = (V3_17['DateTime'] >= S1) & (V3_17['DateTime'] < E1)
V3_17_D1 = V3_17[Filter1]

S2 = '2018-02-05'
E2 = '2018-02-19'
Filter2  = (V3_17['DateTime'] >= S2) & (V3_17['DateTime'] < E2)
V3_17_D2 = V3_17[Filter2]

S3 = '2018-02-19'
E3 = '2018-03-03'
Filter3  = (V3_17['DateTime'] >= S3) & (V3_17['DateTime'] < E3)
V3_17_D3 = V3_17[Filter3]

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
# V2_18 Casey
S1 = '2018-12-06'
E1 = '2018-12-13'
Filter1  = (V2_18['DateTime'] >= S1) & (V2_18['DateTime'] < E1)
V2_18_D1 = V2_18[Filter1]

S2 = '2018-12-18'
E2 = '2018-12-29'
Filter2  = (V2_18['DateTime'] >= S2) & (V2_18['DateTime'] < E2)
V2_18_D2 = V2_18[Filter2]

S3 = '2018-12-29'
E3 = '2019-01-07'
Filter3  = (V2_18['DateTime'] >= S3) & (V2_18['DateTime'] < E3)
V2_18_D3 = V2_18[Filter3]

# V3_18 Mawson
S1 = '2019-01-13'
E1 = '2019-01-26'
Filter1  = (V3_18['DateTime'] >= S1) & (V3_18['DateTime'] < E1)
V3_18_D1 = V3_18[Filter1]

S2 = '2019-01-27'
E2 = '2019-02-19'
Filter2  = (V3_18['DateTime'] >= S2) & (V3_18['DateTime'] < E2)
V3_18_D2 = V3_18[Filter2]

S3 = '2019-02-19'
E3 = '2019-03-02'
Filter3  = (V3_18['DateTime'] >= S3) & (V3_18['DateTime'] < E3)
V3_18_D3 = V3_18[Filter3]

# V4_18 Macquarie Island
S1 = '2019-03-15'
E1 = '2019-03-22'
Filter1  = (V4_18['DateTime'] >= S1) & (V4_18['DateTime'] < E1)
V4_18_D1 = V4_18[Filter1]

S2 = '2019-03-22'
E2 = '2019-03-24'
Filter2  = (V4_18['DateTime'] >= S2) & (V4_18['DateTime'] < E2)
V4_18_D2 = V4_18[Filter2]

#-----------------------------
# CAMMPCAN BrO
#----------------------------

# V1_17 Davis
S1 = '2017-11-01'
E1 = '2017-11-13'
Filter1    = (V1_17_BrO['DateTime'] >= S1) & (V1_17_BrO['DateTime'] < E1)
V1_17_D1_B = V1_17_BrO[Filter1]

S2 = '2017-11-13'
E2 = '2017-11-24'
Filter2    = (V1_17_BrO['DateTime'] >= S2) & (V1_17_BrO['DateTime'] < E2)
V1_17_D2_B = V1_17_BrO[Filter2]

S3 = '2017-11-24'
E3 = '2017-12-03'
Filter3    = (V1_17_BrO['DateTime'] >= S3) & (V1_17_BrO['DateTime'] < E3)
V1_17_D3_B = V1_17_BrO[Filter3]

# V2_17 Casey
S1 = '2017-12-02'
E1 = '2017-12-27'
Filter1    = (V2_17_BrO['DateTime'] >= S1) & (V2_17_BrO['DateTime'] < E1)
V2_17_D1_B = V2_17_BrO[Filter1]

S2 = '2017-12-27'
E2 = '2018-01-04'
Filter2    = (V2_17_BrO['DateTime'] >= S2) & (V2_17_BrO['DateTime'] < E2)
V2_17_D2_B = V2_17_BrO[Filter2]

S3 = '2018-01-04'
E3 = '2018-01-12'
Filter3    = (V2_17_BrO['DateTime'] >= S3) & (V2_17_BrO['DateTime'] < E3)
V2_17_D3_B = V2_17_BrO[Filter3]

# V3_17 Mawson
S1 = '2018-01-12'
E1 = '2018-02-05'
Filter1    = (V3_17_BrO['DateTime'] >= S1) & (V3_17_BrO['DateTime'] < E1)
V3_17_D1_B = V3_17_BrO[Filter1]

S2 = '2018-02-05'
E2 = '2018-02-19'
Filter2    = (V3_17_BrO['DateTime'] >= S2) & (V3_17_BrO['DateTime'] < E2)
V3_17_D2_B = V3_17_BrO[Filter2]

S3 = '2018-02-19'
E3 = '2018-03-03'
Filter3    = (V3_17_BrO['DateTime'] >= S3) & (V3_17_BrO['DateTime'] < E3)
V3_17_D3_B = V3_17_BrO[Filter3]

# V2_18 Casey
S1 = '2018-12-06'
E1 = '2018-12-13'
Filter1    = (V2_18_BrO['DateTime'] >= S1) & (V2_18_BrO['DateTime'] < E1)
V2_18_D1_B = V2_18_BrO[Filter1]

S2 = '2018-12-18'
E2 = '2018-12-29'
Filter2    = (V2_18_BrO['DateTime'] >= S2) & (V2_18_BrO['DateTime'] < E2)
V2_18_D2_B = V2_18_BrO[Filter2]

S3 = '2018-12-29'
E3 = '2019-01-07'
Filter3    = (V2_18_BrO['DateTime'] >= S3) & (V2_18_BrO['DateTime'] < E3)
V2_18_D3_B = V2_18_BrO[Filter3]

# V3_18 Mawson
S1 = '2019-01-13'
E1 = '2019-01-26'
Filter1    = (V3_18_BrO['DateTime'] >= S1) & (V3_18_BrO['DateTime'] < E1)
V3_18_D1_B = V3_18_BrO[Filter1]

S2 = '2019-01-27'
E2 = '2019-02-19'
Filter2    = (V3_18_BrO['DateTime'] >= S2) & (V3_18_BrO['DateTime'] < E2)
V3_18_D2_B = V3_18_BrO[Filter2]

S3 = '2019-02-19'
E3 = '2019-03-02'
Filter3    = (V3_18_BrO['DateTime'] >= S3) & (V3_18_BrO['DateTime'] < E3)
V3_18_D3_B = V3_18_BrO[Filter3]

#-----------------------------
# Met Data
#----------------------------

S1 = '2017-01-10'
E1 = '2017-01-27'
Filter1   = (PCAN_C['DateTime'] >= S1) & (PCAN_C['DateTime'] < E1)
PCAN_D1_C = PCAN_C[Filter1]

S2 = '2017-01-27'
E2 = '2017-02-10'
Filter2   = (PCAN_C['DateTime'] >= S2) & (PCAN_C['DateTime'] < E2)
PCAN_D2_C = PCAN_C[Filter2]

S3 = '2017-02-10'
E3 = '2017-02-24'
Filter3   = (PCAN_C['DateTime'] >= S3) & (PCAN_C['DateTime'] < E3)
PCAN_D3_C = PCAN_C[Filter3]

S4 = '2017-02-24'
E4 = '2017-03-05'
Filter4   = (PCAN_C['DateTime'] >= S4) & (PCAN_C['DateTime'] < E4)
PCAN_D4_C = PCAN_C[Filter4]

# V1_17 Davis
S1 = '2017-11-01'
E1 = '2017-11-13'
Filter1    = (V1_17_C['DateTime'] >= S1) & (V1_17_C['DateTime'] < E1)
V1_17_D1_C = V1_17_C[Filter1]

S2 = '2017-11-13'
E2 = '2017-11-24'
Filter2    = (V1_17_C['DateTime'] >= S2) & (V1_17_C['DateTime'] < E2)
V1_17_D2_C = V1_17_C[Filter2]

S3 = '2017-11-24'
E3 = '2017-12-03'
Filter3    = (V1_17_C['DateTime'] >= S3) & (V1_17_C['DateTime'] < E3)
V1_17_D3_C = V1_17_C[Filter3]

# V2_17 Casey
S1 = '2017-12-02'
E1 = '2017-12-27'
Filter1    = (V2_17_C['DateTime'] >= S1) & (V2_17_C['DateTime'] < E1)
V2_17_D1_C = V2_17_C[Filter1]

S2 = '2017-12-27'
E2 = '2018-01-04'
Filter2    = (V2_17_C['DateTime'] >= S2) & (V2_17_C['DateTime'] < E2)
V2_17_D2_C = V2_17_C[Filter2]

S3 = '2018-01-04'
E3 = '2018-01-12'
Filter3    = (V2_17_C['DateTime'] >= S3) & (V2_17_C['DateTime'] < E3)
V2_17_D3_C = V2_17_C[Filter3]

# V3_17 Mawson
S1 = '2018-01-12'
E1 = '2018-02-05'
Filter1    = (V3_17_C['DateTime'] >= S1) & (V3_17_C['DateTime'] < E1)
V3_17_D1_C = V3_17_C[Filter1]

S2 = '2018-02-05'
E2 = '2018-02-19'
Filter2    = (V3_17_C['DateTime'] >= S2) & (V3_17_C['DateTime'] < E2)
V3_17_D2_C = V3_17_C[Filter2]

S3 = '2018-02-19'
E3 = '2018-03-03'
Filter3    = (V3_17_C['DateTime'] >= S3) & (V3_17_C['DateTime'] < E3)
V3_17_D3_C = V3_17_C[Filter3]

# V2_18 Casey
S1 = '2018-12-06'
E1 = '2018-12-13'
Filter1    = (V2_18_C['DateTime'] >= S1) & (V2_18_C['DateTime'] < E1)
V2_18_D1_C = V2_18_C[Filter1]

S2 = '2018-12-18'
E2 = '2018-12-29'
Filter2    = (V2_18_C['DateTime'] >= S2) & (V2_18_C['DateTime'] < E2)
V2_18_D2_C = V2_18_C[Filter2]

S3 = '2018-12-29'
E3 = '2019-01-07'
Filter3    = (V2_18_C['DateTime'] >= S3) & (V2_18_C['DateTime'] < E3)
V2_18_D3_C = V2_18_C[Filter3]

# V3_18 Mawson
S1 = '2019-01-13'
E1 = '2019-01-26'
Filter1    = (V3_18_C['DateTime'] >= S1) & (V3_18_C['DateTime'] < E1)
V3_18_D1_C = V3_18_C[Filter1]

S2 = '2019-01-27'
E2 = '2019-02-19'
Filter2    = (V3_18_C['DateTime'] >= S2) & (V3_18_C['DateTime'] < E2)
V3_18_D2_C = V3_18_C[Filter2]

S3 = '2019-02-19'
E3 = '2019-03-02'
Filter3    = (V3_18_C['DateTime'] >= S3) & (V3_18_C['DateTime'] < E3)
V3_18_D3_C = V3_18_C[Filter3]

# V4_18 Macquarie Island
S1 = '2019-03-15'
E1 = '2019-03-22'
Filter1    = (V4_18_C['DateTime'] >= S1) & (V4_18_C['DateTime'] < E1)
V4_18_D1_C = V4_18_C[Filter1]

S2 = '2019-03-22'
E2 = '2019-03-24'
Filter2    = (V4_18_C['DateTime'] >= S2) & (V4_18_C['DateTime'] < E2)
V4_18_D2_C = V4_18_C[Filter2]

#------------------------------------------------------------------------------
# CALCULATE THE MEAN HG0

#-----------------------------
# PCAN 2017
#----------------------------
PCAN_M1  = np.mean(PCAN_D1['ng/m3'])
PCAN_M2  = np.mean(PCAN_D2['ng/m3'])
PCAN_M3  = np.mean(PCAN_D3['ng/m3'])
PCAN_M4  = np.mean(PCAN_D4['ng/m3'])

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
V1_17_M1 = np.mean(V1_17_D1['ng/m3'])
V1_17_M2 = np.mean(V1_17_D2['ng/m3'])
V1_17_M3 = np.mean(V1_17_D3['ng/m3'])

V2_17_M1 = np.mean(V2_17_D1['ng/m3'])
V2_17_M2 = np.mean(V2_17_D2['ng/m3'])
V2_17_M3 = np.mean(V2_17_D3['ng/m3'])

V3_17_M1 = np.mean(V3_17_D1['ng/m3'])
V3_17_M2 = np.mean(V3_17_D2['ng/m3'])
V3_17_M3 = np.mean(V3_17_D3['ng/m3'])

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
V2_18_M1 = np.mean(V2_18_D1['ng/m3'])
V2_18_M2 = np.mean(V2_18_D2['ng/m3'])
V2_18_M3 = np.mean(V2_18_D3['ng/m3'])

V3_18_M1 = np.mean(V3_18_D1['ng/m3'])
V3_18_M2 = np.mean(V3_18_D2['ng/m3'])
V3_18_M3 = np.mean(V3_18_D3['ng/m3'])

V4_18_M1 = np.mean(V4_18_D1['ng/m3'])
V4_18_M2 = np.mean(V4_18_D2['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE MEAN BrO

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
V1_17_M1_B = np.mean(V1_17_D1_B['surf_vmr(ppmv)']* 1e6)
V1_17_M2_B = np.mean(V1_17_D2_B['surf_vmr(ppmv)']* 1e6)
V1_17_M3_B = np.mean(V1_17_D3_B['surf_vmr(ppmv)']* 1e6)

V2_17_M1_B = np.mean(V2_17_D1_B['surf_vmr(ppmv)']* 1e6)
V2_17_M2_B = np.mean(V2_17_D2_B['surf_vmr(ppmv)']* 1e6)
V2_17_M3_B = np.mean(V2_17_D3_B['surf_vmr(ppmv)']* 1e6)

V3_17_M1_B = np.mean(V3_17_D1_B['surf_vmr(ppmv)']* 1e6)
V3_17_M2_B = np.mean(V3_17_D2_B['surf_vmr(ppmv)']* 1e6)
V3_17_M3_B = np.mean(V3_17_D3_B['surf_vmr(ppmv)']* 1e6)

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
V2_18_M1_B = np.mean(V2_18_D1_B['surf_vmr(ppmv)']* 1e6)
V2_18_M2_B = np.mean(V2_18_D2_B['surf_vmr(ppmv)']* 1e6)
V2_18_M3_B = np.mean(V2_18_D3_B['surf_vmr(ppmv)']* 1e6)

V3_18_M1_B = np.mean(V3_18_D1_B['surf_vmr(ppmv)']* 1e6)
V3_18_M2_B = np.mean(V3_18_D2_B['surf_vmr(ppmv)']* 1e6)
V3_18_M3_B = np.mean(V3_18_D3_B['surf_vmr(ppmv)']* 1e6)

#------------------------------------------------------------------------------
# CALCULATE THE MEAN PRECIPITATION

#-----------------------------
# PCAN 2017
#----------------------------
PCAN_M1_C  = np.mean(PCAN_D1_C['Accumulated Hourly Rain (mm)'])
PCAN_M2_C  = np.mean(PCAN_D2_C['Accumulated Hourly Rain (mm)'])
PCAN_M3_C  = np.mean(PCAN_D3_C['Accumulated Hourly Rain (mm)'])
PCAN_M4_C  = np.mean(PCAN_D4_C['Accumulated Hourly Rain (mm)'])

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
V1_17_M1_C = np.mean(V1_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V1_17_M2_C = np.mean(V1_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V1_17_M3_C = np.mean(V1_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

V2_17_M1_C = np.mean(V2_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V2_17_M2_C = np.mean(V2_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V2_17_M3_C = np.mean(V2_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

V3_17_M1_C = np.mean(V3_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V3_17_M2_C = np.mean(V3_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V3_17_M3_C = np.mean(V3_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
V2_18_M1_C = np.mean(V2_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V2_18_M2_C = np.mean(V2_18_D2_C['RAIN_ACCUM_FOREMST_MM'])
V2_18_M3_C = np.mean(V2_18_D3_C['RAIN_ACCUM_FOREMST_MM'])

V3_18_M1_C = np.mean(V3_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V3_18_M2_C = np.mean(V3_18_D2_C['RAIN_ACCUM_FOREMST_MM'])
V3_18_M3_C = np.mean(V3_18_D3_C['RAIN_ACCUM_FOREMST_MM'])

V4_18_M1_C = np.mean(V4_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V4_18_M2_C = np.mean(V4_18_D2_C['RAIN_ACCUM_FOREMST_MM'])

#------------------------------------------------------------------------------
# CALCULATE THE TOTAL PRECIPITATION

#-----------------------------
# PCAN 2017
#----------------------------
PCAN_S1_C  = np.sum(PCAN_D1_C['Accumulated Hourly Rain (mm)'])
PCAN_S2_C  = np.sum(PCAN_D2_C['Accumulated Hourly Rain (mm)'])
PCAN_S3_C  = np.sum(PCAN_D3_C['Accumulated Hourly Rain (mm)'])
PCAN_S4_C  = np.sum(PCAN_D4_C['Accumulated Hourly Rain (mm)'])

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
V1_17_S1_C = np.sum(V1_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V1_17_S2_C = np.sum(V1_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V1_17_S3_C = np.sum(V1_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

V2_17_S1_C = np.sum(V2_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V2_17_S2_C = np.sum(V2_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V2_17_S3_C = np.sum(V2_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

V3_17_S1_C = np.sum(V3_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V3_17_S2_C = np.sum(V3_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V3_17_S3_C = np.sum(V3_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
V2_18_S1_C = np.sum(V2_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V2_18_S2_C = np.sum(V2_18_D2_C['RAIN_ACCUM_FOREMST_MM'])
V2_18_S3_C = np.sum(V2_18_D3_C['RAIN_ACCUM_FOREMST_MM'])

V3_18_S1_C = np.sum(V3_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V3_18_S2_C = np.sum(V3_18_D2_C['RAIN_ACCUM_FOREMST_MM'])
V3_18_S3_C = np.sum(V3_18_D3_C['RAIN_ACCUM_FOREMST_MM'])

V4_18_S1_C = np.sum(V4_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V4_18_S2_C = np.sum(V4_18_D2_C['RAIN_ACCUM_FOREMST_MM'])

#------------------------------------------------------------------------------
# CALCULATE THE MEAN WIND SPEED

#-----------------------------
# PCAN 2017
#----------------------------
PCAN_WS1  = (np.mean(PCAN_D1_C['Port True Wind Speed (knot)'] + PCAN_D1_C['Starboard True Wind Speed (knot)'])* 0.514444444)/2
PCAN_WS2  = (np.mean(PCAN_D2_C['Port True Wind Speed (knot)'] + PCAN_D2_C['Starboard True Wind Speed (knot)'])* 0.514444444)/2
PCAN_WS3  = (np.mean(PCAN_D3_C['Port True Wind Speed (knot)'] + PCAN_D3_C['Starboard True Wind Speed (knot)'])* 0.514444444)/2
PCAN_WS4  = (np.mean(PCAN_D4_C['Port True Wind Speed (knot)'] + PCAN_D4_C['Starboard True Wind Speed (knot)'])* 0.514444444)/2

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
V1_17_WS1  = (np.mean(V1_17_D1_C['WND_SPD_STRBD_CORR_KNOT'] + V1_17_D1_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V1_17_WS2  = (np.mean(V1_17_D2_C['WND_SPD_STRBD_CORR_KNOT'] + V1_17_D2_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V1_17_WS3  = (np.mean(V1_17_D3_C['WND_SPD_STRBD_CORR_KNOT'] + V1_17_D3_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2

V2_17_WS1  = (np.mean(V2_17_D1_C['WND_SPD_STRBD_CORR_KNOT'] + V2_17_D1_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V2_17_WS2  = (np.mean(V2_17_D2_C['WND_SPD_STRBD_CORR_KNOT'] + V2_17_D2_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V2_17_WS3  = (np.mean(V2_17_D3_C['WND_SPD_STRBD_CORR_KNOT'] + V2_17_D3_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2

V3_17_WS1  = (np.mean(V3_17_D1_C['WND_SPD_STRBD_CORR_KNOT'] + V3_17_D1_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V3_17_WS2  = (np.mean(V3_17_D2_C['WND_SPD_STRBD_CORR_KNOT'] + V3_17_D2_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V3_17_WS3  = (np.mean(V3_17_D3_C['WND_SPD_STRBD_CORR_KNOT'] + V3_17_D3_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
V2_18_WS1  = (np.mean(V2_18_D1_C['WND_SPD_STRBD_CORR_KNOT'] + V2_18_D1_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V2_18_WS2  = (np.mean(V2_18_D2_C['WND_SPD_STRBD_CORR_KNOT'] + V2_18_D2_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V2_18_WS3  = (np.mean(V2_18_D3_C['WND_SPD_STRBD_CORR_KNOT'] + V2_18_D3_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2

V3_18_WS1  = (np.mean(V3_18_D1_C['WND_SPD_STRBD_CORR_KNOT'] + V3_18_D1_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V3_18_WS2  = (np.mean(V3_18_D2_C['WND_SPD_STRBD_CORR_KNOT'] + V3_18_D2_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V3_18_WS3  = (np.mean(V3_18_D3_C['WND_SPD_STRBD_CORR_KNOT'] + V3_18_D3_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2

V4_18_WS1  = (np.mean(V4_18_D1_C['WND_SPD_STRBD_CORR_KNOT'] + V4_18_D1_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2
V4_18_WS2  = (np.mean(V4_18_D2_C['WND_SPD_STRBD_CORR_KNOT'] + V4_18_D2_C['WND_SPD_PORT_CORR_KNOT'])* 0.514444444)/2

#------------------------------------------------------------------------------
# CALCULATE THE HG0 STANDARD DEVIATION

#-----------------------------
# PCAN 2017
#----------------------------
PCAN_SD1  = np.std(PCAN_D1['ng/m3'])
PCAN_SD2  = np.std(PCAN_D2['ng/m3'])
PCAN_SD3  = np.std(PCAN_D3['ng/m3'])
PCAN_SD4  = np.std(PCAN_D4['ng/m3'])

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
V1_17_SD1 = np.std(V1_17_D1['ng/m3'])
V1_17_SD2 = np.std(V1_17_D2['ng/m3'])
V1_17_SD3 = np.std(V1_17_D3['ng/m3'])

V2_17_SD1 = np.std(V2_17_D1['ng/m3'])
V2_17_SD2 = np.std(V2_17_D2['ng/m3'])
V2_17_SD3 = np.std(V2_17_D3['ng/m3'])

V3_17_SD1 = np.std(V3_17_D1['ng/m3'])
V3_17_SD2 = np.std(V3_17_D2['ng/m3'])
V3_17_SD3 = np.std(V3_17_D3['ng/m3'])

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
V2_18_SD1 = np.std(V2_18_D1['ng/m3'])
V2_18_SD2 = np.std(V2_18_D2['ng/m3'])
V2_18_SD3 = np.std(V2_18_D3['ng/m3'])

V3_18_SD1 = np.std(V3_18_D1['ng/m3'])
V3_18_SD2 = np.std(V3_18_D2['ng/m3'])
V3_18_SD3 = np.std(V3_18_D3['ng/m3'])

V4_18_SD1 = np.std(V4_18_D1['ng/m3'])
V4_18_SD2 = np.std(V4_18_D2['ng/m3'])

#------------------------------------------------------------------------------
# CALCULATE THE BrO STANDARD DEVIATION

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
V1_17_SD1_B = np.std(V1_17_D1_B['surf_vmr(ppmv)']* 1e6)
V1_17_SD2_B = np.std(V1_17_D2_B['surf_vmr(ppmv)']* 1e6)
V1_17_SD3_B = np.std(V1_17_D3_B['surf_vmr(ppmv)']* 1e6)

V2_17_SD1_B = np.std(V2_17_D1_B['surf_vmr(ppmv)']* 1e6)
V2_17_SD2_B = np.std(V2_17_D2_B['surf_vmr(ppmv)']* 1e6)
V2_17_SD3_B = np.std(V2_17_D3_B['surf_vmr(ppmv)']* 1e6)

V3_17_SD1_B = np.std(V3_17_D1_B['surf_vmr(ppmv)']* 1e6)
V3_17_SD2_B = np.std(V3_17_D2_B['surf_vmr(ppmv)']* 1e6)
V3_17_SD3_B = np.std(V3_17_D3_B['surf_vmr(ppmv)']* 1e6)

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
V2_18_SD1_B = np.std(V2_18_D1_B['surf_vmr(ppmv)']* 1e6)
V2_18_SD2_B = np.std(V2_18_D2_B['surf_vmr(ppmv)']* 1e6)
V2_18_SD3_B = np.std(V2_18_D3_B['surf_vmr(ppmv)']* 1e6)

V3_18_SD1_B = np.std(V3_18_D1_B['surf_vmr(ppmv)']* 1e6)
V3_18_SD2_B = np.std(V3_18_D2_B['surf_vmr(ppmv)']* 1e6)
V3_18_SD3_B = np.std(V3_18_D3_B['surf_vmr(ppmv)']* 1e6)

#------------------------------------------------------------------------------
# CALCULATE THE PRECIPITATION STANDARD DEVIATION

#-----------------------------
# PCAN 2017
#----------------------------
PCAN_SD1_C  = np.std(PCAN_D1_C['Accumulated Hourly Rain (mm)'])
PCAN_SD2_C  = np.std(PCAN_D2_C['Accumulated Hourly Rain (mm)'])
PCAN_SD3_C  = np.std(PCAN_D3_C['Accumulated Hourly Rain (mm)'])
PCAN_SD4_C  = np.std(PCAN_D4_C['Accumulated Hourly Rain (mm)'])

#-----------------------------
# CAMMPCAN 2017-18
#----------------------------
V1_17_SD1_C = np.std(V1_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V1_17_SD2_C = np.std(V1_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V1_17_SD3_C = np.std(V1_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

V2_17_SD1_C = np.std(V2_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V2_17_SD2_C = np.std(V2_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V2_17_SD3_C = np.std(V2_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

V3_17_SD1_C = np.std(V3_17_D1_C['RAIN_ACCUM_FOREMST_MM'])
V3_17_SD2_C = np.std(V3_17_D2_C['RAIN_ACCUM_FOREMST_MM'])
V3_17_SD3_C = np.std(V3_17_D3_C['RAIN_ACCUM_FOREMST_MM'])

#-----------------------------
# CAMMPCAN 2018-19
#----------------------------
V2_18_SD1_C = np.std(V2_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V2_18_SD2_C = np.std(V2_18_D2_C['RAIN_ACCUM_FOREMST_MM'])
V2_18_SD3_C = np.std(V2_18_D3_C['RAIN_ACCUM_FOREMST_MM'])

V3_18_SD1_C = np.std(V3_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V3_18_SD2_C = np.std(V3_18_D2_C['RAIN_ACCUM_FOREMST_MM'])
V3_18_SD3_C = np.std(V3_18_D3_C['RAIN_ACCUM_FOREMST_MM'])

V4_18_SD1_C = np.std(V4_18_D1_C['RAIN_ACCUM_FOREMST_MM'])
V4_18_SD2_C = np.std(V4_18_D2_C['RAIN_ACCUM_FOREMST_MM'])

#------------------------------------------------------------------------------
# BUILD A DATAFRAME FOR THE HG0 MEAN AND STDEV

data1 = [V1_17_M1, V1_17_M2, V1_17_M3, V2_17_M1, V2_17_M2, V2_17_M3, V3_17_M1, V3_17_M2, V3_17_M3, np.nan, np.nan,
          np.nan, np.nan, np.nan, V2_18_M1, V2_18_M2, V2_18_M3, V3_18_M1, V3_18_M2, V3_18_M3, V4_18_M1, V4_18_M2,
         PCAN_M1, PCAN_M2, PCAN_M3, PCAN_M4]

data1 = np.round(data1, 2)

data2 = [V1_17_SD1, V1_17_SD2, V1_17_SD3, V2_17_SD1, V2_17_SD2, V2_17_SD3, V3_17_SD1, V3_17_SD2, V3_17_SD3, np.nan, np.nan,
          np.nan, np.nan, np.nan, V2_18_SD1, V2_18_SD2, V2_18_SD3, V3_18_SD1, V3_18_SD2, V3_18_SD3, V4_18_SD1, V4_18_SD2,
         PCAN_SD1, PCAN_SD2, PCAN_SD3, PCAN_SD4]

#------------------------------------------------------------------------------
# BUILD A DATAFRAME FOR THE BrO MEAN AND STDEV

data3 = [-1, V1_17_M2_B, V1_17_M3_B, V2_17_M1_B, V2_17_M2_B, V2_17_M3_B, V3_17_M1_B, V3_17_M2_B, V3_17_M3_B, np.nan, np.nan,
          np.nan, np.nan, np.nan, V2_18_M1_B, V2_18_M2_B, V2_18_M3_B, V3_18_M1_B, V3_18_M2_B, V3_18_M3_B, np.nan, np.nan,
         np.nan, np.nan, np.nan, -1]

data3 = np.round(data3, 2)

data4 = [V1_17_SD1_B, V1_17_SD2_B, V1_17_SD3_B, V2_17_SD1_B, V2_17_SD2_B, V2_17_SD3_B, V3_17_SD1_B, V3_17_SD2_B, V3_17_SD3_B, np.nan, np.nan,
          np.nan, np.nan, np.nan, V2_18_SD1_B, V2_18_SD2_B, V2_18_SD3_B, V3_18_SD1_B, V3_18_SD2_B, V3_18_SD3_B, np.nan, np.nan,
         np.nan, np.nan, np.nan, np.nan]

#------------------------------------------------------------------------------
# BUILD A DATAFRAME FOR THE PRECIPITATION TOTAL

data5 = [V1_17_S1_C, V1_17_S2_C, V1_17_S3_C, V2_17_S1_C, V2_17_S2_C, V2_17_S3_C, V3_17_S1_C, V3_17_S2_C, V3_17_S3_C, np.nan, np.nan,
         np.nan, np.nan, np.nan, V2_18_S1_C, V2_18_S2_C, V2_18_S3_C, V3_18_S1_C, V3_18_S2_C, V3_18_S3_C, np.nan, np.nan,
         PCAN_S1_C, PCAN_S2_C, PCAN_S3_C, PCAN_S4_C]

data5 = np.round(data5, 2)

data6 = [V1_17_M1_C, V1_17_M2_C, V1_17_M3_C, V2_17_M1_C, V2_17_M2_C, V2_17_M3_C, V3_17_M1_C, V3_17_M2_C, V3_17_M3_C, np.nan, np.nan,
         np.nan, np.nan, np.nan, V2_18_M1_C, V2_18_M2_C, V2_18_M3_C, V3_18_M1_C, V3_18_M2_C, V3_18_M3_C, np.nan, np.nan,
         PCAN_M1_C, PCAN_M2_C, PCAN_M3_C, PCAN_M4_C]

data6 = np.round(data6, 2)

#------------------------------------------------------------------------------
# BUILD A DATAFRAME FOR THE WIND SPEED MEAN

data7 = [V1_17_WS1, V1_17_WS2, V1_17_WS3, V2_17_WS1, V2_17_WS2, V2_17_WS3, V3_17_WS1, V3_17_WS2, V3_17_WS3, np.nan, np.nan,
         np.nan, np.nan, np.nan, V2_18_WS1, V2_18_WS2, V2_18_WS3, V3_18_WS1, V3_18_WS2, V3_18_WS3, np.nan, np.nan,
         PCAN_WS1, PCAN_WS2, PCAN_WS3, PCAN_WS4]

data7 = np.round(data7, 2)

#------------------------------------------------------------------------------
# PLOT THE GRAPH

fig = plt.figure()

gs = gridspec.GridSpec(nrows=3,
                       ncols=1, 
                       figure=fig, 
                       width_ratios= [1],
                       height_ratios=[0.25, 0.25, 0.67],
                       hspace=0.0)

#-----------------------------
# Graph 1
ax1 = plt.subplot(gs[0])

# Configurations for the datasets
bar_width = 0.3
opacity = 0.8

# Plot the data
rects4 = ax1.errorbar(DF1['Deployment'], data3, color='k', marker='o', linestyle= '', label='BrO', yerr=data4, capsize=2)

for i, v in enumerate(data3):
    t = ax1.text(i-0.25 ,v/data3[i],data3[i],fontsize=10,color='black',fontweight='bold')
    t.set_bbox(dict(facecolor='white', edgecolor='white'))

# Axis labels, title and legend
ax1.axes.get_xaxis().set_visible(False)
#ax1.spines['bottom'].set_visible(False)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0,7.5)
ax1.set_ylabel('BrO VMR (pptv)', fontsize=16, labelpad=15)
ax1.set_title('RM, Hg$^0$ and BrO concentrations observed during CAMMPCAN and PCAN',fontsize=20,y=1.02)

#-----------------------------
# Graph 2
ax1 = plt.subplot(gs[1])
ax2 = ax1.twinx()

# Configurations for the datasets
bar_width = 0.3
opacity = 0.8

# Plot the data
rects5 = ax2.errorbar(DF1['Deployment'], data1, color='grey', marker='o', linestyle= '', label='Hg$^0$', yerr=data2, capsize=2)

for i, v in enumerate(data1):
    t = ax2.text(i-0.25 ,v/data1[i]-1,data1[i],fontsize=10,color='black',fontweight='bold')
    t.set_bbox(dict(facecolor='white', edgecolor='white'))

# Axis labels, title and legend
ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)
#ax1.spines['bottom'].set_visible(False)
#ax2.spines['bottom'].set_visible(False)
#ax1.spines['top'].set_visible(False)
#ax2.spines['top'].set_visible(False)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=16, labelpad=15)

#-----------------------------
# Graph 3
ax1 = plt.subplot(gs[2])
ax2 = ax1.twinx()

# Configurations for the datasets
bar_width = 0.3
opacity = 0.8

# Plot the data
rects1 = ax1.bar(DF1['Deployment'], DF1['RM_Conc'], bar_width, alpha=opacity, color='b', ec='black', label='CAMMPCAN (2017-18)', yerr=DF1['StDev'], capsize=2)
rects2 = ax1.bar(DF1['Deployment'][11:22], DF1['RM_Conc'][11:22], bar_width, alpha=opacity, color='r', ec='black', label='CAMMPCAN (2018-19)', yerr=DF1['StDev'][11:22], capsize=2)
rects3 = ax1.bar(DF1['Deployment'][22:26], DF1['RM_Conc'][22:26], bar_width, alpha=opacity, color='g', ec='black', label='PCAN (2017)', yerr=DF1['StDev'][22:26], capsize=2)
#rects6 = ax2.bar(DF1.index+0.3, data5, bar_width, alpha=opacity, color='y', ec='black', label='Precipitation')
rects7 = ax2.bar(DF1.index+0.3, data7, bar_width, alpha=opacity, color='y', ec='black', label='Wind Speed (m/s)')

# Label the data values

#for i, v in enumerate(data5):
#    ax2.text(i-0.25 ,v/data5[i]-10,data5[i],fontsize=10,color='black',fontweight='bold')

for i, v in enumerate(DF1['RM_Conc']):
    ax1.text(i-0.25 ,v/DF1['RM_Conc'][i]-10,DF1['RM_Conc'][i],fontsize=10,color='black',fontweight='bold')

# Set up ticks for X and Y axis
#ax1.spines['top'].set_visible(False)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_xticklabels(DF1['Deployment'],rotation=90)
ax1.set_ylim(0,290)

# Axis labels, title and legend
ax1.set_ylabel('RM (pg/m$^3$)', fontsize=16, labelpad=15)
#ax2.set_ylabel('Total Precipitation (mm)', fontsize=16, labelpad=15)
ax2.set_ylabel('Wind Speed (m/s)', fontsize=16, labelpad=15)
ax1.set_xlabel('Filter Deployment', fontsize=16, labelpad=15)
fig.legend(loc='upper left', bbox_to_anchor=(0.125, 0.5), title='Season',fontsize=12)

plt.show()