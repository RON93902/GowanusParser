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

# Extract PDF table in the format of the template
file = '122475_3919_DataTables.pdf'
template = 'cleaned.tabula-template.json'
tables_raw = tabula.read_pdf_with_template(file, template)

# Cleanup the read in dataframe
for i in range(0,len(tables_raw)):
    tables_raw[i] = tables_raw[i].T.reset_index().T
    tables_raw[i].reset_index(drop=True, inplace=True)

for i in range(0,len(tables_raw)):
    if ('Sample' in tables_raw[i].iloc[len(tables_raw[i].index)-1,0]):
        tables_raw[i].insert(0,'','')

# create a list that will store the complete tables as shown in PDF

# j = 0
# # tables_clean.append(tables_raw[0])
# for i in range(0,len(tables_raw)):
#     if ('Total' not in tables_raw[i].iloc[len(tables_raw[i].index)-1,0]):
#         tables_clean = tables_clean.concat(tables_raw[i],ignore_index=True,sort=False)
#     if ('Total' in tables_raw[i].iloc[len(tables_raw[i].index)-1,0]):
#         tables_clean[j] = tables_clean[j].append(tables_raw[i],ignore_index=True,sort=False)
#         j = j + 1

# # tabula.convert_into(pdf_path, "test.csv", output_format="csv", stream=True)