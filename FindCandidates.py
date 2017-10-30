import pandas as pd
import numpy as np
import os
from time import ctime
import sys
from pathlib import Path
home = str(Path.home())
sys.path.append(home + '/PycharmProjects/General')
print(sys.path)
import pyodbc as odbc
#from NCHGeneral import Use, Save, fewSpreadsheets, postAgg, getFN, RenameVars, toMySQL
#from NCHGeneral import *
pd.options.mode.chained_assignment = None  # default='warn'
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
print('------------------------------')
print('Program start time: ' + ctime())
print('------------------------------')

#####################
## Program purpose ##
#####################
'''
This script executes the logic for identifying patients who are candidates for palliative care.
It goes further than the existing SQL Server scripts by focusing on the most recent authorization for 
each patient and seeing if the patient has been previously flagged.
'''

###############
## Functions ##
###############
# functions needed to:
#   1) Read data
#   2) Flag cancer types that are universally in

import pyodbc as odbc

connstring = 'DSN=bidataca2;DATABASE=EDW;Trusted_Connection = True'
conn = odbc.connect(connstring)
sql = 'SELECT Top 100 * from EDW.dbo.AuthPrice'
df = pd.read_sql(sql, conn)
conn.close()
print(df.head())