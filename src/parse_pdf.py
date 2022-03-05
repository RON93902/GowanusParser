# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:20:52 2022

@author: STA94720
"""

import tabula
import os
import pandas as pd
import numpy as np
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
import re

file = '122475_3919_Datatables.pdf'
template = 'cleaned.tabula-template.json'


# Read in tables_raw from cleaned pdf
tables_raw = tabula.read_pdf_with_template(file, template)
for i in range(0,len(tables_raw)):
    tables_raw[i] = tables_raw[i].T.reset_index().T



tables_clean = []
tables_clean.append(tables_raw[0][:6])
j = 0
for i in range(0,len(tables_raw)):
    
    if not tables_raw[i].iloc[0,0] == 'Station Location:':
        tables_clean[j] = tables_clean[j].append(tables_raw[i], ignore_index = True)
    
    if ('Total' in tables_raw[i].iloc[len(tables_raw[i].index)-1,0]):
        j = j + 1
        
    

# # def format_table(table_object):
    
# #     # 1. Create template dataframe (where the results are stored)
# #     ##   - columns headers = ID_Short, STATION, SAMPLE_ID, TOP_ft, BOT_ft, SampleType, Analyte, Units, Result, Qualifier, Cite
# #     result = pd.DataFrame(columns=['ID_Short', 'STATION', 'SAMPLE_ID', 'TOP_ft', 'BOT_ft', 'SampleType', 'Analyte', 'Units', 'Result', 'Qualifier', 'Cite'])
    
# #     # 2. Populate template with data taken from 'table_object'
        
# endOfTable = 'no'
# for i in range(0,len(tables_raw)-1):
#     if endOfTable == 'yes':
#         temp_dataFrame = tables_raw[i][0:0]
#     if 'Total' in tables_raw[i].iloc[len(tables_raw[i].index)-1,0]:
#         print('yes')
#         endOfTable = 'yes'
#     # temp_DataFrame.append(tables_raw[i].rows[6:])

# tabula.convert_into(pdf_path, "test.csv", output_format="csv", stream=True)