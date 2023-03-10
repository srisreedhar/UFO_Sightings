# Final Data file

import os
import pandas as pd
import csv
import requests as r
import datetime as dt
from ndxevent import records


urls = ["https://nuforc.org/webreports/"+i['record'] for i in records]
dataframes=[]
logger=list()

for each_url in urls:
    filelog=dict()
    filename=each_url.split("/")[-1]
    filelog[filename]=each_url.split("/")[-1]
    filelog['starttime']= dt.datetime.now()
    df = pd.read_html(each_url)[0]
    df['snapshot_date']=str(dt.date.today())
    df['filename']=filename
    dataframes.append(df)
    filelog['stoptime']= dt.datetime.now()
    filelog['processed_time'] = filelog['stoptime'] - filelog['starttime']
    filelog['rows_inserted'] = df.shape[0]
    logger.append(filelog)



# print(len(dataframes))
# print("/n")
# print(logger)

finaldata = pd.concat(dataframes,ignore_index=True)
finaldata.to_csv('ufo_rowlevel_data.csv')