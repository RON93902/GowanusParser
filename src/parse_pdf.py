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

#test changes for learning git


