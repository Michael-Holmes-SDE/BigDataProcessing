# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
    *   What I need to do:
	* PHASE 0:
	1. Download 2021.annual.singlefile.zip and unzip in data/USA_full/
	2. Read the Project Requirements
	3. Read 'QCEW Area Codes and Titles' and 'QCEW Field Layouts'
	4. Fill out Phase 0 of the SDP(What does the program do, how, and changes I expect to make)
	5. Tag commit 'analyzed' and push to GitLab
	
	* PHASE 1:
	1. Design functions in Phase 1 in pseudocode
	2. Use the dictionary 'rpt'
	3. Ensure the files are read one line at a time, only one line in memory, with contents stored in the dictionary
	4. Only include required FIPS areas(Only FIPS that starts with an int and doesn't end with 3 zeros)
	5. Skip over lines for excluded FIPS areas AND that don't belong to the wanted sectors of the economy(must include desired values for 'area_fips', 'industry_code', and 'own_code' in the report)
	6. No eval()
	7. If a non-skipped line has 'industry_code' = '10' and 'own_code' = '0', add data to 'all industries' portion of report
	8. If a non-skipped line has 'industry_code' = '5112' and 'own_code' = '5', add data to 'software publishing industry' portion of report 
	5. Close file after it is read
	2. Tag commit 'designed' and push to GitLab
	
	* PHASE 2:
	1. Follow the instructions in each sub-directory of data/USA_full/ to make test cases
	2. Use the Benchmark to see how long the program should take
	3. Implement the code as defined in Phase 1 to where the program works without crashing
	4. Ensure the code can be run from any directory but the files themselves are hard-coded
	4. Explain what changed between Phase 1 and Phase 2
	5. Tag commit 'implemented' and push to GitLab
	
	* Phase 3:
	1. Test all data sets
	2. Fill out the test cases I used in SDP
	3. If bugs were found, say what they were and how it was fixed
	4. Tag commit 'tested' and push to GitLab
	
	* Phase 4:
	1. Fill out
	2. Tag commit 'deployed' and push to GitLab

	* Phase 5:
	1. Review SDP and Signature
	2. Fill out
	3. Tag commit 'final' and push to GitLab
	4. Check Starter Code Quiz score
	5. Fill out the Assignment Reflection Survey

*   [X] Explain the problem this program aims to solve.
	* This program aims to summarize the employment data for 2021 from a CSV file
    *   Describe what a *good* solution looks like.
	* A good solution will look like the following:
	[============]
	[Final Report]
	[============]

	Statistics over all industries in 2021:
	=========================================================
	Number of FIPS areas in report       3,274

	Total annual wages                   $9,749,457,535,475
	Area with maximum annual wages       New York County, New York
	Maximum reported wage                $349,820,933,687
	
	Total number of establishments       10,960,881
	Area with most establishments        Los Angeles County, California
	Maximum # of establishments          525,496
	
	Total annual employment level        144,691,578
	Area with maximum employment         Los Angeles County, California
	Maximum reported employment level    4,252,857
	
	
	Statistics over the software publishing industry in 2021:
	=========================================================
	Number of FIPS areas in report       1,627

	Total annual wages                   $111,505,515,321
	Area with maximum annual wages       King County, Washington
	Maximum reported wage                $24,259,942,206

	Total number of establishments       54,994
	Area with most establishments        New York County, New York
	Maximum # of establishments          1,636

	Total annual employment level        535,426
	Area with maximum employment         King County, Washington
	Maximum reported employment level    74,792
	
    *   List what you already know how to do.
	1. I know how to setup the output
	2. I know how to find the FIPS numbers
	3. I know how to find the large values and which they are(ie. 'Area with most establishments', 'Maximum # of establishments')
	4. I know how to (hopefully) get all of the values I need to print out from the csv file
    *   Point out any challenges that you can foresee.
	1. I don't know how to only have one line of a file at a time in the computer's memory
	2. I don't know how to split a CSV line into two using .split() when there are many commas(now I do)
	3. I'm not 100% sure I know how to get all of the values I need from the csv file
*   [X] List all of the data that is used by the program, making note of where it comes from.
	* INPUT:
	1. ONLY ONE ARGUMENT, a directory (the file names 'area-titles.csv' and '2021.annual.singlefile.csv' will be hard-coded in)
	2. If there is no argument(directory) given, the error code 'Usage: src/bigData.py DATA_DIRECTORY' is printed and the program exits
	3. If directory can't be accessed, let open() fail and give the automated error message
    *   Explain what form the output will take.
	* OUTPUT:
	1. The only output should be made by running 'print_report(rpt)' (prints can write to STDERR)
	2. Should include no extra: newlines; spaces; quote marks; FIPS codes(instead show "County, State")
	3. Test by redirecting STDOUT to a file and comparing it to the examples like so: 
	        3a. python src/big_data.py data/UT_all_industries > ut.txt
		3b. diff -u ut.txt data/UT_all_industries/output.txt
	4. Outputs the 'Number of FIPS areas in report', the 'Total annual wages', 'Area with maximum annual wages' in human readability form, the 'Maximum reported wage', the 'Total number of establishments', the 'Area with most establishments', the 'Maximum # of establishments'(num in area with most), the 'Total annual employment level', the 'Area with maximum employment'(in human form), and the 'Maximum reported employment level'
	5. That output is for both all industries and the software publishing industry (separate sections to display each)
	6. If outputting a file like 'software_industry' or 'all_industries', input zeros for all numbers and blank lines for all character lines of the section not wanted
	7. If outputting 'reversed', use tac to reverse the basic 'complete set

*   [X] List the algorithms that will be used (but don't write them yet).
	* str.split: takes arguments (self, sep, maxsplit) so set maxsplit to 1 for FIPS
	* An algorithm to see if a string has letters in it and whether the last 3 numbers are zeros
	* An algorithm to read and store one line of a file at a time in memory
	* An algorithm to find the 'area_fips', 'industry_code', and 'own_code'
	* An algorithm to find how many FIPS areas are in the report
	* An algorithm to find 'Total annual wages', 'Area with maximum annual wages', and 'Maximum reported wage'
	* An algorithm to find 'Total number of establishments', 'Area with most establishments', and 'Maximum # of establishments'
	* An algorithm to find 'Total annual employment level', 'Area with maximum employment', and 'Maximum reported employment level'
	* An algorithm to create a section of the output(with 'software_industry' or 'all_industries' as a parameter)

*   [X] Tag the last commit in this phase `analyzed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [X] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
	* Area titles and their corresponding place name are in 'area-titles.csv'
	* '2021.annual.singlefile.csv' has columns separated by commas in the following order:
	0. 'area_fips' (important)  **
	1. 'own_code' (important)  **
	2. 'industry_code' (important)  **
	3. 'agglvl_code' (not important)
	4. 'size_code' (not important)
	5. 'year' (not important)
	6. 'qtr' (not important)
	7. 'disclosure_code' (not important)
	8. 'annual_avg_estabs'   (important)  **
	9. 'annual_avg_emplvl'  (important)  **
	10. 'total_annual_wages' (important)  **
	11. None of the remaining columns are important for this program
	

	** DICTIONARY METHODS THAT MIGHT BE USEFUL **
			1. __setitem__(self, key, value, /)
 			   	Set self[key] to value.
			2. __getattribute__(self, name, /)
		     	   	Return getattr(self, name).
			3. __getitem__(...)
   			   	x.__getitem__(y) <==> x[y]
			4. __contains__(self, key, /)
		     	   	True if the dictionary has the specified key, else False.			
			5. get(self, key, default=None, /)
		     	   	Return the value for key if key is in the dictionary, else default.	
	1. Check if a directory is passed as an argument		
		if length of sys.argv is less than or equal to 1 (no directory passed)
			print('Usage: src/bigData.py DATA_DIRECTORY')
			exit	 
		*** NO NEED TO SET UP ANYTHING FOR PRINTING, 'print_report(rpt)' IS DEFINED ALREADY
	2. Create FIPS dictionary(using new module FIPS.py)
		Create FIPS as a blank dictionary by doing 'FIPS = {}'
		open(sys.argv[1]/area-titles.csv)
		for line in file
			(fipsCode, title) = line.split(',', maxsplit = 1) (should not split the title that way)
			if fipsCode is an integer (possible check if not string)					if fipsCode / 1000 is not an integer (shows if last 3 digit are zero)
				if last 3 digits are not 0:
					FIPS[int(fipsCode)] = title (key fipsCode directs to title in dictionary)
		close file

	3. Collecting info from 2021.annual.singlefile.csv
		open(sys.argv[1]/2021.annual.singlefile.csv)
		**Everything below will run twice, once for each section of industry (all and software)
		until fips of csv is the same as the one in the dictionary (use __contains__ on dictionary)
		create var areas_all = 0
		create var areas_software = 0
		create var wages_all = 0
		create var wages_software = 0
		for element in array FIPS
			if fips code of csv file (column 0) is the same as in array FIPS
				if industry_code = 10 (column 2) and own_code = 0 (column 1)
					run below with sector = 'all industries'
				if industry_code = 5112 (column 2) and own_code = 5 (column 1)
					run below with sector = 'software publishing industry'
		1. Getting num_areas
			1. For loop through
				increment var_SECTOR areas by 1
			2. Set rpt[sector]['num_areas'] to areas_SECTOR 2. Getting 
		total_annual_wages
			1. For loop through 
				increment wages_SECTOR by total_annual_wages of FIPS (column 10 of csv)
		        2. Set rpt[sector]['total_annual_wages'] to wages_SECTOR
		3. Getting max_annual_wages
			1. Create int var max_wages_var = 0
			2. Create blank string var max_wages_loc
			3. For loop through
				if total_annual_wages(column 10 of csv) is greater than max_wages_var
					max_wages_var = total_annual_wages
					set string var max_wages_loc = location of current FIPS in human form
			4. Set rpt[sector]['max_annual_wages] = [max_wages_loc, max_wages_var]
		4. getting total_estab
			1. Create var estabs = 0
			2. For loop through
				increment estabs by annual_avg_estabs of FIPS (column 8 of csv)
			3. set rpt[sector]['total_estab'] = estabs
		5. getting max_estab
			1. Create int var max_estab_var = 0
			2. Create blank string var max_estab_loc
			3. For loop through
				if annual_avg_estabs (column 8 of csv) is greater than max_estab_var
					max_estab_var = annual_avg_estabs
					set string var max_estab_loc = location of current FIPS in human form
			4. Set rpt[sector]['max_estab'] = [max_estab_loc, max_estab_var]
		6. getting total_empl
			1. Create var empl = 0
			2. For loop through
				increment empl by annual_avg_emplvl of FIPS (column 9 of csv)
			3. Set rpt[sector]['total_empl'] = empl
		7. getting max_empl
			1. Create int var max_empl_var = 0
			2. Create blank string var max_empl_loc
			3. For loop through
				if annual_avg_emplvl (column 9 of csv) is greater than max_empl_var
					max_empl_var = annual_avg_emplvl
					max_empl_loc = location of current FIPS in human form
			4. Set rpt[sector]['max_empl'] = [max_empl_loc, max_empl_var]
		close file	

*   Explain what happens in the face of good and bad input.
	1. Good Input: The program will output a file similar to the one outlined in Phase 0, with correct variables in place depending on user desired output. 
	2. Bad Input: If there is no directory passed, an error message will be printed. If an invalid directory is passed, the program will crash and generate an error message to display.
    *   Write a few specific examples that occur to you, and use them later when testing
	1. No directory passed: should print error message 'Usage: src/bigData.py DATA_DIRECTORY' and quit)
	2. Invalid directory passed: program should print automated error message and crash
	3. Program should output data correctly
*   [X] Tag the last commit in this phase `designed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [X] More or less working code.
*   [X] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
	1. Both .isdigit() and .isnumeric() didn't work to test fips area codes, so I had to .strip() then .replace() quotation marks out of the variables
	2. I learned about maxsplit's and how the maxsplit value isn't how many total elements are created, but one less because if there are extras they are all added to an element after the value of maxsplit's element 
*   [X] Tag the last commit in this phase `implemented`


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [X] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
	1. For the test cases I navigated to each directory, read using 'nano' the 'README.md' and follow the instructions to create the trimmed down csv file to test that directory. 
	2. Then the program should be run as normal from the command line, from the base of the project directory(in this case '/cs1440-assn3/') and making a new file from the result in the following way: 'python src/big_data.py data/{Directory to test} > {new file you name}'. 
	3. Then compare what was printed with the original by running 'diff -u --color=always {file you created above} data/{directory}/output.txt'
	4. If that doesn't work and you are on a Windows computer, then compare what was printed with the original by running 'diff -u -Z --color=always {file you created above} data/{directory}/output.txt'
	5. I did this for UT_software_industry, UT_all_industries, UT_reversed, USA_full, DC_software_industry, and HI_complete
	6. For each test case I ran, everything outputted as expected and no differences were detected
*   [X] Tag the last commit in this phase `tested`



## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [X] Tag the last commit in this phase `deployed`
*   [X] Your repository is pushed to GitLab.
*   [X] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [X] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [X] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
	1. I know why everything works in my program, and if a bug is reported it would probably take about an hour to find out why.
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
	1. I hope my documentation makes sense to others, and it will to me in six months.
    *   How easy will it be to add a new feature to this program in a year?
	1. It depends on the feature, it shouldn't be too difficult but not easy either.
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
	1. The program should continue to work no matter what is upgraded.
*   [X] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [X] Respond to the **Assignment Reflection Survey** on Canvas.
