# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:20:52 2022

@author: STA94720
"""

import tabula
import os
import pandas as pd
import numpy as np

file = '122475_3919_DataTables.pdf'

tables = tabula.read_pdf(file, pages="all")

#test changes for learning git

page_1_table = tables[0]
page_2_table = tables[1]


def format_table(table_object):
    
    # 1. Create template dataframe (where the results are stored)
    ##   - columns headers = ID_Short, STATION, SAMPLE_ID, TOP_ft, BOT_ft, SampleType, Analyte, Units, Result, Qualifier, Cite
    result = pd.DataFrame(columns=['ID_Short', 'STATION', 'SAMPLE_ID', 'TOP_ft', 'BOT_ft', 'SampleType', 'Analyte', 'Units', 'Result', 'Qualifier', 'Cite'])
    
    # 2. Populate template with data taken from 'table_object'
    
#####


endOfTable = 'no'
for i in range(0,len(tables)-1):
    if endOfTable == 'yes':
        temp_dataFrame = tables[i][0:0]
    if 'Total' in tables[i].iloc[len(tables[i].index)-1,0]:
        print('yes')
        endOfTable = 'yes'
    # temp_DataFrame.append(tables[i].rows[6:])
