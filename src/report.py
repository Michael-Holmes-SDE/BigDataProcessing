# Standard BLS report format  	  	  
#  	  	  
# DO NOT EDIT THIS FILE!!!  	  	  

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


def print_report(dat):  	  	  
    print(f"""\
[==========================================================]
[ US BLS Quarterly Census of Employment and Wages for {dat['year']} ]
[==========================================================]

Statistics over all industries
-----------------------------------------------------------
Number of FIPS areas in report       {dat['all']['num_areas']:,}

Total annual wages                   ${dat['all']['total_annual_wages']:,}
Area with maximum annual wages       {dat['all']['max_annual_wage'][0]}
Maximum reported wage                ${dat['all']['max_annual_wage'][1]:,}

Total number of establishments       {dat['all']['total_estab']:,}
Area with most establishments        {dat['all']['max_estab'][0]}
Maximum # of establishments          {dat['all']['max_estab'][1]:,}

Total annual employment level        {dat['all']['total_empl']:,}
Area with maximum employment         {dat['all']['max_empl'][0]}
Maximum reported employment level    {dat['all']['max_empl'][1]:,}


Statistics in the software publishing industry
-----------------------------------------------------------
Number of FIPS areas in report       {dat['soft']['num_areas']:,}

Total annual wages                   ${dat['soft']['total_annual_wages']:,}
Area with maximum annual wages       {dat['soft']['max_annual_wage'][0]}
Maximum reported wage                ${dat['soft']['max_annual_wage'][1]:,}

Total number of establishments       {dat['soft']['total_estab']:,}
Area with most establishments        {dat['soft']['max_estab'][0]}
Maximum # of establishments          {dat['soft']['max_estab'][1]:,}

Total annual employment level        {dat['soft']['total_empl']:,}
Area with maximum employment         {dat['soft']['max_empl'][0]}
Maximum reported employment level    {dat['soft']['max_empl'][1]:,}""")  	  	  
