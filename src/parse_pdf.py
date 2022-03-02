# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:20:52 2022

@author: STA94720
"""

import tabula
import os
import pandas as pd

file = '122475_3919_DataTables.pdf'

tables = tabula.read_pdf(file, pages="all")

page_1_table = tables[0]
page_2_table = tables[1]


def format_table(table_object):
    
    # 1. Create template dataframe (where the results are stored)
    ##   - columns headers = ID_Short, STATION, SAMPLE_ID, TOP_ft, BOT_ft, SampleType, Analyte, Units, Result, Qualifier, Cite
    result = pd.DataFrame(columns=['ID_Short', 'STATION', 'SAMPLE_ID', 'TOP_ft', 'BOT_ft', 'SampleType', 'Analyte', 'Units', 'Result', 'Qualifier', 'Cite'])
    
    # 2. Populate template with data taken from 'table_object'
    

