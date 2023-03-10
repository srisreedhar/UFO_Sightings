import os
import pandas as pd
import csv
import requests as r
import datetime as dt
import re



# All Events Data

url="https://nuforc.org/webreports/ndxevent.html"

resp=r.get(url).text
html=resp.split("<TR VALIGN=TOP><TD><A HREF=")[1:]

records=list()
for row_num,each_record in enumerate(html):
    row=dict()
    row_num = row_num+1
    row['row_id']=row_num
    row['record']=each_record.split('>')[0].strip()
    row['record_key']=each_record.split('>')[0].split('.html')[0].strip()
    row['record_date']=each_record.split('>')[1].strip('</A')
    row['record_count']=each_record.split('>')[4].strip('</TD')
    records.append(row)

# df=pd.DataFrame(records)
# df

eventkeys=row.keys()

# All Events Data - truth checker
with open('all_events.csv','w',newline='') as recordsfile:
    dict_writer=csv.DictWriter(recordsfile, eventkeys)
    dict_writer.writeheader()
    dict_writer.writerows(records)



# All States

states = r.get(url).text
states_records=states.split("<TR VALIGN=TOP><TD><A HREF=")[1:]



















# Alternative approach
# data = pd.read_html('https://nuforc.org/webreports/ndxe202303.html')
# data[0]
# :D