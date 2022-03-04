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

file = '122475_3919_DataTables.pdf'


# Clean pdf file
pdf_in = PdfFileReader(file,'rb')
pdf_out = PdfFileWriter()
for p in [pdf_in.getPage(i) for i in range(0, pdf_in.getNumPages())]:
    text = p.extractText()
    if not re.search(r'Page Intentionally Left Blank', text, re.I):
        pdf_out.addPage(p)
with open('cleaned.pdf', 'wb') as f:
    pdf_out.write(f)

# Read in tables from cleaned pdf
tables = tabula.read_pdf('cleaned.pdf', pages="all", pandas_options={'header': None}, multiple_tables=True)

# table_I9A, index 0 to 44 in tables
# table_I10A, index 45 to 67 in tables
# table_I12A, index 68 to 88 in tables

#test changes for learning git

# page_1_table = tables[0]
# page_2_table = tables[1]

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
        
        
        
      
        
# endOfTable = 'no'
# for i in range(0,len(tables)-1):
#     if endOfTable == 'yes':
#         temp_dataFrame = tables[i][0:0]
#     if 'Total' in tables[i].iloc[len(tables[i].index)-1,0]:
#         print('yes')
#         endOfTable = 'yes'
#     # temp_DataFrame.append(tables[i].rows[6:])

# tabula.convert_into(pdf_path, "test.csv", output_format="csv", stream=True)