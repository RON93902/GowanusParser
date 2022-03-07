# Gowanus PDF Parser

## Description
This repository hosts a collection of scripts that facilitate parsing of pdf data for the Gowanas project. 

## Repository Ownership
* **Practice**: TBD
* **Sector**: TBD
* **Original Author(s)**: Kevin Stanton and Wenyong Rong
* **Contact Details for Current Repository Owner(s)**: - kevin.stanton@mottmac.com

## Requirements
* [JAVA](https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245807_df5ad55fdd604472a86a45a217032c7d)
* [tabula-py](https://github.com/tabulapdf/tabula) Python package
  * `pip install tabula-py`

## Installation Instructions

1. Install with pip <br />
`pip install git+https://github.com/mottmacdonaldglobal/GowanusParser.git`
2. Import the library <br />
`import GowanusParser`

## Running the Code
WIP

## Features of Parsed Data
*	ID_Short – abbreviated core location (station) ID, e.g. the Station GC-SD125 has a short ID of 125.
*	Station – “Station Location” field in pdf table
*	Sample_ID – “Sample Number” field in pdf table or concatenation of the Station, Top_ft and Bot_ft if easier.
*	Top_ft – from the “Sample Depth” field
*	Bot_ft -- from the “Sample Depth” field
*	SampleType – from the “Sample Type”  field. “N” for all samples except duplicates get an “FD”, duplicates have irregular “Sample Numbers” (e.g. D-03162010-2)
*	Analyte – “Parameter” field
*	Units – “Units” field
*	Result – numerical value
*	Qualifier – e.g. U, UJ, J, NJ, N, R
*	Cite – concatenate the table # for that data with “(GCRI Vol1 2011)” e.g. “Table I-11A (GCRI Vol1 2011)”
