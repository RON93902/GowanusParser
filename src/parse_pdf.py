# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:20:52 2022

@author: STA94720
"""

### import libraries
import tabula
import os
import pandas as pd
import numpy as np
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
import re

### specify source file and parsing template
file = '122475_3919_Datatables.pdf'
template = '122475_3919_DataTables.tabula-template.json'


### Read in tables_raw from source pdf
tables_raw = tabula.read_pdf_with_template(file, template)

### clean raw data
# remove blank pages
tables_raw = [tables_raw[i] for i in range(0,len(tables_raw)) if tables_raw[i].size > 4]

# reset indices
for i in range(0,len(tables_raw)):
    tables_raw[i] = tables_raw[i].T.reset_index().T

# generate 'tables_clean' as a list of dataframes containing one set of header
# information for all data of each table from the source
tables_clean = []
j = 0
for i in range(0,len(tables_raw)):
    
    # add data to new 'tables_clean' list entry if appropriate, otherwise append to current list item (j)
    if not tables_raw[i].iloc[0,0] == 'Station Location:':
        if j > len(tables_clean)-1:
            tables_clean.append(tables_raw[i])
        else:
            tables_clean[j] = tables_clean[j].append(tables_raw[i],ignore_index=True)
    
    # insert header information into 'tables_clean' list item if end of table is reached
    # move to next dataframe from 'tables_raw' if appropriate
    if ('Total' in tables_raw[i].iloc[len(tables_raw[i].index)-1,0]):
        tables_raw[i-1].insert(0, "0", "")
        tables_raw[i-1].columns = pd.RangeIndex(tables_raw[i-1].columns.size)
        tables_clean[j] = pd.concat([tables_raw[i-1],tables_clean[j]])
        tables_clean[j] = tables_clean[j].reset_index().iloc[:,1:]
        j = j + 1

### populate final table of data
res = pd.DataFrame(columns=['ID_Short', 'STATION', 'SAMPLE_ID', 'TOP_ft', 'BOT_ft', 'SampleType', 'Analyte', 'Units', 'Result', 'Qualifier', 'Cite'])

# loop over all columns of all list items in 'tables_clean'
for j in range(0,len(tables_clean)):
    for i in tables_clean[j]:
        if i > 1:
            units = tables_clean[j].iloc[8,1] # units always shows up here so
    
    
    