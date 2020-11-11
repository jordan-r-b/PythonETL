import pandas as pd
import numpy as np

#Variables for data load. Change path to directory of data
punch_data = []
punch_files = []
path = 'C:\\Users\\50063903\\Desktop\\Brazil_punch\\'

#Read all txt files in directory
import os
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]

for file in text_files:
    f = open((path+file), "r")
    #append each line in the file to a list
    punch_data.append(f.readlines())
    f.close()


#Hard Coded first draft# File from Brazil time clocks where employee number and date/time of punch is stored
#punch_data = open('C:\\Users\\50063903\\Desktop\\Brazil_punch\\ba1905.txt')


# In[43]:


#File listing company employee number with PIS number
emp_list = pd.read_csv('C:\\Users\\50063903\\Desktop\\Brazil_punch\\emp_num.csv')


# In[44]:


#Importing this data into a Pandas dataframe to more easily modify/write files
df = pd.DataFrame(punch_data,columns = ['Data'])


# In[ ]:


df_emp = pd.DataFrame(emp_list)


# In[6]:


#Cleaning up \n from data
df = df.replace(r'\n',' ', regex=True) 


# In[7]:


#Data is in a single string, seperated into rows, that needs to be sliced into different columns
#Data is at a fixed index in each string
#Data below is for the employee compnay number known as PIS in Brazil
df['PIS_Number'] = df.Data.str[23:]


# In[8]:


df['Hour'] = df.Data.str[18:20]


# In[9]:


df['Minute'] = df.Data.str[20:22]


# In[10]:


df['Day'] = df.Data.str[10:12]


# In[11]:


df['Month'] = df.Data.str[12:14]


# In[12]:


df['Year'] = df.Data.str[14:18]


# In[13]:


#Date column for import needed as mm/dd/yy
df['Date'] = df.Month + '/' + df.Day + '/' + df.Year.str[2:]


# In[14]:


#Time column for import need as HHMM
df['Time'] = df.Hour + df.Minute


# In[15]:


#Importing from txt file brings the values over as objects. Convert to int in order to merge
df["PIS_Number"] = pd.to_numeric(df["PIS_Number"], errors = 'coerce',downcast = 'integer')


# In[22]:


df_combined = df.merge(df_emp,how='inner',on='PIS_Number')


# In[23]:


df_combined


# In[18]:


#Convert Employee number from float to int for export
df_combined['Employee_Number'] = df_combined['Employee_Number '].astype('Int64', copy=False)


# In[21]:


#Export flat file to be imported by third party interface.  Only need columns listed
df_combined.to_csv('PunchImport.csv',index = False,columns = ['Employee_Number ','Time', 'Date'])


# In[ ]:




