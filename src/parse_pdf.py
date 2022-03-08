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
import re

### user inputs
file = '122475_3919_Datatables.pdf' # data source
template = '122475_3919_DataTables.tabula-template.json' # template for parsing the main table
template_cite = '122475_3919_DataTables_cite.tabula-template.json' #template file to extract citations
Separate_Tabs="no" # "yes" or "no" Compilation Choice - One big table or One big list with all dataframes

### Read in tables_raw from source pdf
tables_raw = tabula.read_pdf_with_template(file, template)
tables_raw_cite = tabula.read_pdf_with_template(file, template_cite)

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
        tables_raw[i-1].insert(0, "0", "") # insert blank column to align column headers between front matter and main table data
        tables_raw[i-1].columns = pd.RangeIndex(tables_raw[i-1].columns.size) # reset column headers of front matter
        tables_raw[i-1] = tables_raw[i-1].reset_index().iloc[:,1:] # reset row index of front matter
        tables_raw[i-1].loc[0] = tables_raw[i-1].loc[0].str.split('.').str[0] # remove spurious '.n' column delimiters inserted upon initial read of front matter
        
        # concat front matter row data with row above if value in column 0 is nan
        rows_to_delete = []
        for row in range(1,4):
            if pd.isna(tables_raw[i-1].loc[row]).any():
                tables_raw[i-1].loc[row-1] = tables_raw[i-1][row-1:row+1].apply(lambda x: ''.join(x.astype(str)))
                tables_raw[i-1].loc[row-1] = tables_raw[i-1].loc[row-1].map(lambda x: x.rstrip('nan'))    
                rows_to_delete.append(row)
        
        # delete junk data
        for junk in rows_to_delete:
            tables_raw[i-1] = tables_raw[i-1].drop(junk)
                
        tables_clean[j] = pd.concat([tables_raw[i-1],tables_clean[j]]) # add front matter to compiled table entry
        tables_clean[j] = tables_clean[j].reset_index().iloc[:,1:] # remove the extra index in column 1
        tables_clean[j].iat[0,0] = tables_raw_cite[int(round((i+1)/2-1))].columns[0] # unstable (requires tables to always span 2 pages)
        j = j + 1
    
##### WIP #####
### populate final table of data    
#Data Compilation - Master Spreadsheet Production

# Define the mother of variables for all compiled clean tables
tables_master=[]
ID_Short=[]
STATION=[]
SAMPLE_ID=[]
TOP_ft=[]
BOT_ft=[]
SampleType=[]
Analyte=[]
Units=[]
Result=[]
Qualifier=[]
Cite=[]

#Compilation for Requested Data
for tc in range(len(tables_clean)):
    
    #Define master of variables for each table
    ID_Short2=[]
    STATION2=[]
    SAMPLE_ID2=[]
    TOP_ft2=[]
    BOT_ft2=[]
    SampleType2=[]
    Analyte2=[]
    Units2=[]
    Result2=[]
    Qualifier2=[]
    Cite2=[]

    for a in range((len(tables_clean[tc].iloc[0]))-2):
        Analyte1=np.array(tables_clean[tc].iloc[6:][0])
        Units1=np.array(tables_clean[tc].iloc[6:][1])
        Result1=np.array(tables_clean[tc].iloc[6:][2+a])
        Qualifier1=np.array(tables_clean[tc].iloc[6:][2+a])
        
        Analyte2.extend(Analyte1)
        Units2.extend(Units1)
        Result2.extend(Result1)
        Qualifier2.extend(Qualifier1)
        
    for c in range((len(tables_clean[tc].iloc[0]))-2):
        
        #Define temporary master of variables to generate more number of header and match the number of data in one column
        ID_Short1=[]
        STATION1=[]
        SAMPLE_ID1=[]
        TOP_ft1=[]
        BOT_ft1=[]
        SampleType1=[]
        Cite1=[]
        
        for b in range(len(Analyte1)):
            ID_Short1.append(tables_clean[tc].iloc[0][2+c])
            STATION1.append(tables_clean[tc].iloc[0][2+c])
            SAMPLE_ID1.append(tables_clean[tc].iloc[0][2+c])
            TOP_ft1.append(tables_clean[tc].iloc[2][2+c])
            BOT_ft1.append(tables_clean[tc].iloc[2][2+c])
            SampleType1.append(tables_clean[tc].iloc[5][2+c])
            Cite1.append(tables_clean[tc].iloc[0][0])
    
        ID_Short2.extend(ID_Short1)
        STATION2.extend(STATION1)
        SAMPLE_ID2.extend(SAMPLE_ID1)
        TOP_ft2.extend(TOP_ft1)
        BOT_ft2.extend(BOT_ft1)
        SampleType2.extend(SampleType1)
        Cite2.extend(Cite1)
        
    #Create Final List of Dataframes
    
    #If you want it to be one big table with all compiled data
    if Separate_Tabs == "no":
        ID_Short.extend(ID_Short2)
        STATION.extend(STATION2)
        SAMPLE_ID.extend(SAMPLE_ID2)
        TOP_ft.extend(TOP_ft2)
        BOT_ft.extend(BOT_ft2)
        SampleType.extend(SampleType2)
        Analyte.extend(Analyte2)
        Units.extend(Units2)
        Result.extend(Result2)
        Qualifier.extend(Qualifier2)
        Cite.extend(Cite2)
        
        tables_master=pd.DataFrame({'ID_Short': ID_Short,'STATION': STATION,'SAMPLE_ID': SAMPLE_ID,
                                'TOP_ft': TOP_ft, 'BOT_ft': BOT_ft, 'SampleType': SampleType,
                                'Analyte': Analyte, 'Units': Units, 'Result': Result,
                                'Qualifier': Qualifier, 'Cite': Cite})
    
    #If you want it to be one big list with all dataframes stored inside
    elif Separate_Tabs == "yes":
        
        tables_master2=pd.DataFrame({'ID_Short': ID_Short2,'STATION': STATION2,'SAMPLE_ID': SAMPLE_ID2,
                                'TOP_ft': TOP_ft2, 'BOT_ft': BOT_ft2, 'SampleType': SampleType2,
                                'Analyte': Analyte2, 'Units': Units2, 'Result': Result2,
                                'Qualifier': Qualifier2, 'Cite': Cite2})
        
        tables_master.append(tables_master2)

###dataframe creation and export to excel
export_dir=os.getcwd()
writer = pd.ExcelWriter(os.path.join(export_dir,'GOWANUS MASTER SUMMARY.xlsx'), engine='xlsxwriter')

#Dataframe export to each tab in the spreadsheet

if Separate_Tabs == "no":
    tables_master.to_excel(writer,'Summary Table', index = False)

elif Separate_Tabs == "yes":
    for df in range(0,len(tables_master)):
        tables_master[df].to_excel(writer,'Table Number '+str(df+1), index = False)

writer.save()
writer.close()  
