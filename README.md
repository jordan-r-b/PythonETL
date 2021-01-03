# Projects:

# Brazil_punch

Business problem: Multiple txt files are outputted from devices and sent to a designated folder. These files contain strings of numbers representing multiple fields of data. String has a set pattern but is not always consistent. For example the employee ID number can start at character 13 or 14 depending on the file. This requires built in data checking. Need to extract data and convert into a flat file for use with a different service. Key field in the data needs to be matched with a seperate data source for final field in flat file. Final step is to transfer file via SSH onto FTP server for upload with end service (Kronos).

Steps: Only steps are to designate where the raw TXT files will be placed and the username/password of the FTP server.

Final Output: CSV file in below format.

![Final Output](Screenshots/Brazil_Screenshot.png?raw=true "Final Output")

# India_ETL

Business problem: Data from previous timekeeping system needs to be uploaded into new system. Data is not in a tabular format (shown below). Need to parse through this data line by line and export it into a usable format for Kronos timekeeping system upload. 

Steps: File in the same directory as Python file.
PythonETL 1.0

Original python script without example file formats. Will include examples in future.
