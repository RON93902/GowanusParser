# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:20:52 2022

@author: STA94720
"""

import tabula
import os
import pandas as pd
import numpy as np
import re
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


file = '122475_3919_DataTables.pdf'
template = 'cleaned.tabula-template.json'

# Read in tables from pdf file
tables = tabula.read_pdf(file, pages="all")

# create a list to store all the complete tables in PDF file
target = []

target.append(tables[0][:6])
j = 0 + 1
for i in range(45):
    if ('Total' in tables[i].iloc[len(tables[i].index)-1,0]):
        j = j + 1

    target[j] = target[j].append(tables[i-1].append(tables[i][6:], ignore_index = True) )

# Read in tables from cleaned pdf
tables = tabula.read_pdf_with_template(file, template)
for i in range(0,len(tables)):
    tables[i] = tables[i].T.reset_index().T

# # def format_table(table_object):
    
# #     # 1. Create template dataframe (where the results are stored)
# #     ##   - columns headers = ID_Short, STATION, SAMPLE_ID, TOP_ft, BOT_ft, SampleType, Analyte, Units, Result, Qualifier, Cite
# #     result = pd.DataFrame(columns=['ID_Short', 'STATION', 'SAMPLE_ID', 'TOP_ft', 'BOT_ft', 'SampleType', 'Analyte', 'Units', 'Result', 'Qualifier', 'Cite'])
    
# #     # 2. Populate template with data taken from 'table_object'

# target = []
# target.append(tables[0][:6])
# j = 0
# for i in range(45):
#     if ('Total' in tables[i].iloc[len(tables[i].index)-1,0]):
#         j = j + 1

#     target[j] = target[j].append(tables[i-1].append(tables[i][6:], ignore_index = True) )
#     table_I9A[2*i-1]= temp_dataFrame
        
for i in range(0,len(tables)-1):
    if (tables[i] == 'GEC-SD-98').any().idxmax() > 0:
        print('table ', i)

df = tables[0]
a = df.where(df=='GC-SED-83').dropna(how='all')      
      
        
# endOfTable = 'no'
# for i in range(0,len(tables)-1):
#     if endOfTable == 'yes':
#         temp_dataFrame = tables[i][0:0]
#     if 'Total' in tables[i].iloc[len(tables[i].index)-1,0]:
#         print('yes')
#         endOfTable = 'yes'
#     # temp_DataFrame.append(tables[i].rows[6:])

# tabula.convert_into(pdf_path, "test.csv", output_format="csv", stream=True)