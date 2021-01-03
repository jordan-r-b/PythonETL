# Projects:

# Brazil ETL

Business problem: Multiple txt files are outputted from devices and sent to a designated folder. These files contain strings of numbers representing multiple fields of data. String has a set pattern but is not always consistent. For example the employee ID number can start at character 13 or 14 depending on the file. This requires built in data checking. Need to extract data and convert into a flat file for use with a different service. Key field in the data needs to be matched with a seperate data source for final field in flat file. Final step is to transfer file via SSH onto FTP server for upload with end service (Kronos).

Manual Steps: Designate where the raw TXT files will be placed and the username/password of the FTP server. Will need to update additional file that contains lookup table information.

Script Steps: Script will collect all files in designated folder and add to a Pandas table. Data will be formatted for needed output. Data from lookup table (currently stored in an Excel file) pulled into a seperate Pandas table. Tables are merged. SSH connection to FTP server is initialized. Check for previous version of this file is made and file is deleted if found. File is exported as .csv onto FTP server.

Files: Brazil_punch (code)

Final Output: CSV file in below format.

![Brazil Screenshot](Screenshots/Brazil_Screenshot.png?raw=true "Brazil Screenshot")

# India Data Parsing RPA

Business problem: Data from previous timekeeping system needs to be uploaded into new system. Data is not in a tabular format (shown below). Need to parse through this data line by line and export it into a usable format for Kronos timekeeping system upload. 

Steps: Place ile in the same directory as Python file.

Script Steps: Script will read .csv file line by line pulling the data into different Numpy series and Pandas tables. Built in logic based on data formatting. For example, finding a line with employee IDs means the following line will contain time information. After completion the file will be exported as a .csv in below format.

Files: India_RPA (code)

![India Screenshot](Screenshots/Brazil_Screenshot.png?raw=true "India Screenshot")

# Finance data parsing, web scraping, and machine learning

Business problem: Exported data from another system contains lines of redundant data that need to be removed so that analysis can be performed. Primary data analysis goal is to group in Pivot tables on investor or Rep. Additional analysis is then performed on data including machine learning to determine data trends.

Script Steps: Pulls in data to Pandas table. Filters out redundant data by the 'Account' column. Pulls in data into a Pandas table of lookup table with Rep/Investor info. Merges these tables. Creates Pivot tables in Pandas. Then performs machine learning using SciKit Learn. Finally, exports data to designated Excel file for ease of use/distribution within company.

![Finance Code](Screenshots/Finance_code.png?raw=true "Finance Code")

Files: Finance_RPA (code), Distro_detail (example data), Rep_lookup (example data)

Output:

Pivot Table

![Finance Pivot](Screenshots/Finance_Pivot.png?raw=true "Finance Pivot")

Data Analysis with Plotly

![Finance Graph](Screenshots/Finance_rep.png?raw=true "Finance Graph")

![Finance Analysis](Screenshots/Finance_Analysis.png?raw=true "Finance Analysis")

Machine Learning with SciKit Learn

![Finance Machine Learning](Screenshots/Finance_ML.png?raw=true "Finance Pivot")
