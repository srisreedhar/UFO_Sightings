import os
import pandas as pd
import csv
import requests as r
import datetime as dt
import re



# All States
url = "https://nuforc.org/webreports/ndxloc.html"
states = r.get(url).text
states_records=states.split("<TR VALIGN=TOP><TD><A HREF=")[1:]

state_records=list()
for each_state in states_records:
    row=dict()
    row['record']=each_state.split('>')[0].strip()
    row['record_key']=each_state.split('>')[0].split('.html')[0].strip()
    row['record_state']=each_state.split('>')[1].split('<')[0]
    row['record_count']=re.findall(r'<TD>(\d+)</TD>',each_state)[0]
    row['snapshot_date']=str(dt.date.today())
    state_records.append(row)

filename="allstates_"+str(dt.date.today())+".csv"

statekeys=row.keys()
with open(filename,'w',newline='') as opfile:
    dict_writer=csv.DictWriter(opfile, statekeys)
    dict_writer.writeheader()
    dict_writer.writerows(state_records)