# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:20:52 2022

@author: STA94720
"""

import tabula
import os
import pandas as pd
import numpy as np
# import re
# import sys
# from PyPDF2 import PdfFileWriter, PdfFileReader

file = '122475_3919_DataTables.pdf'

# # Clean pdf file
# pdf_in = PdfFileReader(file,'rb')
# pdf_out = PdfFileWriter()
# for p in [pdf_in.getPage(i) for i in range(0, pdf_in.getNumPages())]:
#     text = p.extractText()
#     if not re.search(r'Page Intentionally Left Blank', text, re.I):
#         pdf_out.addPage(p)
# with open('cleaned.pdf', 'wb') as f:
#     pdf_out.write(f)

# Read in tables from pdf file
tables = tabula.read_pdf(file, pages="all")

# table_I9A, index 0 to 44 in tables
# table_I10A, index 45 to 67 in tables
# table_I12A, index 68 to 88 in tables

# create a list to store all the complete tables in PDF file
target = []

target.append(tables[0][:6])
j = 0
for i in range(45):
    if ('Total' in tables[i].iloc[len(tables[i].index)-1,0]):
        j = j + 1

    target[j] = target[j].append(tables[i-1].append(tables[i][6:], ignore_index = True) )
        
        
      
        
# endOfTable = 'no'
# for i in range(0,len(tables)-1):
#     if endOfTable == 'yes':
#         temp_dataFrame = tables[i][0:0]
#     if 'Total' in tables[i].iloc[len(tables[i].index)-1,0]:
#         print('yes')
#         endOfTable = 'yes'
#     # temp_DataFrame.append(tables[i].rows[6:])

# tabula.convert_into(pdf_path, "test.csv", output_format="csv", stream=True)