import pandas as pd
import numpy as np
import csv


md = pd.read_csv("BIRAFFE-metadata.csv", sep=';')
#usunięcie tych rekordów gdzie osoba nie ma danych z gry w space
md = md[pd.notnull(md['SPACE'])]
md = md[pd.notnull(md['OPENNESS'])]
#zostawienie id tych osób, bo pliki mają w nazwie id
ids = md['ID'].values

import csv
import json    
print("start")
pd.set_option('display.max_columns', 500)
#import metadata
data = pd.read_csv("merged_scores.csv", sep=',')
data = data[pd.notnull(data['OPENNESS'])]
data = data[pd.notnull(data['CONSCIENTIOUSNESS'])]
data = data[pd.notnull(data['EXTRAVERSION'])]
data = data[pd.notnull(data['AGREEABLENESS'])]
data = data[pd.notnull(data['NEUROTICISM'])]

data=data[data.Score == 'GameOver']
#data.head(25)
type(data)
mean_c=[]

with open('mean_scores.csv', 'w', newline='') as csvfile:
    #nazwy kolumn- wszystkie z plików json
    fieldnames = ["P_ID","OPENNESS","CONSCIENTIOUSNESS","EXTRAVERSION","AGREEABLENESS","NEUROTICISM","Mean"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #ustawienie nagłówków
    writer.writeheader()
    for my_id in ids:
        data1=data.loc[data['P_ID'] == my_id]
        nr=data1.shape[0]
        #print(data1)
        score=data1['Value'].sum()
        mean = score/nr
        print(mean)
        new_data={ 'P_ID': data1['P_ID'].iloc[0], 'OPENNESS': data1['OPENNESS'].iloc[0], 'CONSCIENTIOUSNESS': data1['CONSCIENTIOUSNESS'].iloc[0],'EXTRAVERSION':  data1['EXTRAVERSION'].iloc[0],'AGREEABLENESS': data1['AGREEABLENESS'].iloc[0],'NEUROTICISM': data1['NEUROTICISM'].iloc[0],'Mean': mean}
        writer.writerow(new_data)

