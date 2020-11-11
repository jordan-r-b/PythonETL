import pandas as pd
import numpy as np

di = ['Label',16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'a','b','c']


df = pd.read_csv("ATTENDANCE SUMMARY.csv")




df.columns = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)




df.fillna(0, inplace=True)




dfin = pd.DataFrame()
dfout = pd.DataFrame()
dfwork = pd.DataFrame()




gems = []
gems_list = []
tup = []




for i, x in df.iterrows():
    if df.iloc[i].astype(str).str.contains('-').any():
        #Get first cell if column contains GEMS info, add to list
        gems_list.append(df.iloc[i][1])
        print('True')
        pass
    elif 'In Time' in [df.iloc[i][1]]:
        print('In')
        #If row is in times, get row and append
        tup = []
        tup = (df.iloc[i])
        dfin = dfin.append(tup)
        pass
    elif 'Out Time' in [df.iloc[i][1]]:
        out = []
        out = (df.iloc[i])
        dfout = dfout.append(out)
        print('Out')
    elif 'Work Hours' in [df.iloc[i][1]]:
        work = []
        work = (df.iloc[i])
        dfwork = dfwork.append(work)
        print('Work')
    else:
        pass
        print('False')




dfin['GEMS'] = gems_list
dfout['GEMS'] = gems_list
dfwork['GEMS'] = gems_list




dfin.columns = di
dfout.columns = di




#Melt turns wide DataFrame into a long DataFrame by use of an ID column
dfin2 = pd.melt(dfin, id_vars = ['c'])
dfout2 = pd.melt(dfout, id_vars = ['c'])




dffinal




dffinal.to_csv('final.csv')






