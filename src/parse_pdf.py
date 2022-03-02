# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:20:52 2022

@author: STA94720
"""

#### CURRENT WORKING MODULES ####

import tabula
import os
import pandas as pd

file = '122475_3919_DataTables.pdf'

tables = tabula.read_pdf(file, pages="all")


#### TESTING MODULES BEGIN ####

# import PyPDF2 as pdf

# reader = pdf.PdfFileReader('122475_3919_DataTables.pdf')

# text = reader.getPage(0).extractText()

######

# import camelot
# import pandas as pd

# file = '122475_3919_DataTables.pdf'

# tables = camelot.read_pdf(file)

# print("Total tables extracted:", tables.n)
# print(tables[0].df)

#### TESTING MODULES END ####