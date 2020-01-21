import pandas as pd
import numpy as np

print("start")
pd.set_option('display.max_columns', 500)
#import metadata
md = pd.read_csv("data1/BIRAFFE-metadata.csv", sep=';')

#drop subjects without 'procedure' files available
md = md[pd.notnull(md['SPACE'])]
md.head()
#extract ids and convert to the np array
ids = md['ID'].values

import csv
import json           

import os.path

with open('data1/test4.csv', 'w', newline='') as csvfile:
    fieldnames = ["Timestamp","Affective","Order1","Order2","Order3","Order4","Asteroid","Type","ID","By","Bolt","Key","Scene","RotationX","RotationY","RotationZ","RotationW","PositionX","PositionY","PositionZ"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for my_id in ids:
        fi=open("data1/SUB" + str(my_id) + "-Space.json")
        x = json.load(fi)
        for i in x:
            if ('ID' in i):
                writer.writerow(i)
                
print("gotowe!")