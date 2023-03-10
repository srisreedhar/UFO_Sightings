import os
import pandas as pd
import csv
import requests as r
import datetime as dt
import re


url = "https://nuforc.org/webreports/ndxshape.html"
shape_records = r.get(url).text.split("<TR VALIGN=TOP><TD><A HREF=")[1:]
# shape_records=shapes.split("<TR VALIGN=TOP><TD><A HREF=")[1:]

all_shape_records=list()
for each_shape in shape_records:
    row=dict()
    row['shape']=each_shape.split('>')[1].split('<')[0]
    row['record_url']=each_shape.split('>')[0].strip()
    row['shape_count']= re.findall(r'<TD>(\d+)</TD>', each_shape)[0]
    row['snapshot_date']=str(dt.date.today())
    all_shape_records.append(row)

filename="allshapes_"+str(dt.date.today())+".csv"
shapekeys=row.keys()


with open(filename,'w',newline='') as opfile:
    dict_writer=csv.DictWriter(opfile, shapekeys)
    dict_writer.writeheader()
    dict_writer.writerows(all_shape_records)