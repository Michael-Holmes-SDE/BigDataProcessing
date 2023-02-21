#!/usr/bin/env python  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

import time
import sys
from report import print_report

# print_report takes a dictionary with these contents:  	  	  
rpt = {
    'year': 2021,

    'all': {
        'num_areas': 0,
        'total_annual_wages': 0,
        'max_annual_wage': ["", 0],
        'total_estab': 0,
        'max_estab': ["", 0],
        'total_empl': 0,
        'max_empl': ["", 0],
    },

    'soft': {
        'num_areas': 0,
        'total_annual_wages': 0,
        'max_annual_wage': ["", 0],
        'total_estab': 0,
        'max_estab': ["", 0],
        'total_empl': 0,
        'max_empl': ["", 0],
    },
}
# Is directory given?
if len(sys.argv) <= 1:
    print('Usage: src/bigData.py DATA_DIRECTORY')
    exit()
print("Reading the databases...", file=sys.stderr)
before = time.time()  # Start timer
FIPS = {}
file = open(sys.argv[1] + '/area-titles.csv')
# Adding relevant fips areas and their names to the FIPS dictionary
for line in file:
    (fipsCode, title) = line.split(',', maxsplit=1)
    fipsCode = fipsCode.strip().replace("\"", "")
    title = title.strip().replace("\"", "")
    if fipsCode.isdigit():
        if not fipsCode.endswith('000'):
            FIPS[fipsCode] = title
file.close()


# Getting data when called
def gettingData(industry, fipsCode, annualAvgEstabs, annualAvgEmplvl, totalAnnualWages):
    rpt[industry]['num_areas'] += 1
    rpt[industry]['total_annual_wages'] += int(totalAnnualWages)
    if int(totalAnnualWages) > int(rpt[industry]['max_annual_wage'][1]):
        rpt[industry]['max_annual_wage'] = [FIPS[fipsCode], int(totalAnnualWages)]
    rpt[industry]['total_estab'] += int(annualAvgEstabs)
    if int(annualAvgEstabs) > int(rpt[industry]['max_estab'][1]):
        rpt[industry]['max_estab'] = [FIPS[fipsCode], int(annualAvgEstabs)]
    rpt[industry]['total_empl'] += int(annualAvgEmplvl)
    if int(annualAvgEmplvl) > int(rpt[industry]['max_empl'][1]):
        rpt[industry]['max_empl'] = [FIPS[fipsCode], int(annualAvgEmplvl)]


# Getting data from each line in file and checking if it is a relevant fips, ownCode and industryCode to pass onto gettingData
file = open(sys.argv[1] + '/2021.annual.singlefile.csv')
for line in file:
    valuesList = line.split(',', maxsplit=11)
    fipsCode = valuesList[0].strip().replace("\"", "")
    ownCode = valuesList[1].strip().replace("\"", "")
    industryCode = valuesList[2].strip().replace("\"", "")
    annualAvgEstabs = valuesList[8].strip().replace("\"", "")
    annualAvgEmplvl = valuesList[9].strip().replace("\"", "")
    totalAnnualWages = valuesList[10].strip().replace("\"", "")  # (POSSIBLY) GET RID OF VARIABLES AFTER EVERYTHING WORKS AND USE THE DICTIONARY
    industry = ""
    if fipsCode in FIPS:
        if ownCode == "0" and industryCode == "10":
            industry = 'all'
            gettingData(industry, fipsCode, annualAvgEstabs, annualAvgEmplvl, totalAnnualWages)
        if ownCode == '5' and industryCode == '5112':
            industry = 'soft'
            gettingData(industry, fipsCode, annualAvgEstabs, annualAvgEmplvl, totalAnnualWages)
file.close()

# End timer and print time it took to create the report
after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report  	  	  
print_report(rpt)
