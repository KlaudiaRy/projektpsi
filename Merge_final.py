import pandas as pd
import numpy as np

print("start")
pd.set_option('display.max_columns', 500)
#import metadata
md = pd.read_csv("data1/BIRAFFE-metadata.csv", sep=';')

#usunięcie tych rekordów gdzie osoba nie ma danych z gry w space
md = md[pd.notnull(md['SPACE'])]
md.head()
#zostawienie id tych osób, bo pliki mają w nazwie id
ids = md['ID'].values

import csv
import json           

import os.path

#nowy plik test4.csv
with open('data1/merged.csv', 'w', newline='') as csvfile:
    #nazwy kolumn- wszystkie z plików json
    fieldnames = ["Timestamp","Affective","Order1","Order2","Order3","Order4","Asteroid","Type","ID","By","Bolt","Key","Value","Score","P_ID","OPENNESS","CONSCIENTIOUSNESS","EXTRAVERSION","AGREEABLENESS","NEUROTICISM","Scene","RotationX","RotationY","RotationZ","RotationW","PositionX","PositionY","PositionZ"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #ustawienie nagłówków
    writer.writeheader()
    
    #dla każdego id otwórz plik json
    for my_id in ids:
        fi=open("data1/SUB" + str(my_id) + "-Space.json")
        x = json.load(fi)
        person=md.loc[md['ID']==my_id]
        #dla każdej paczki danych (w tych klamerkach: {} z pliku)
        for i in x:
            #sprawdź czy ma klucz 'ID'
            if (('ID' or 'Value') in i):
                json_data = pd.DataFrame.to_json(person,orient='records')
                #print(len(json_data))
                json_data=json_data[:-1]
                json_data=json_data[1:]
                #print("\n\n",json_data)
                pr=json.loads(json_data)
                pr['P_ID'] = pr.pop('ID')
                #print(pr)
                #print(i)
                person_data = { 'P_ID': int(pr['P_ID']), 'OPENNESS': pr['OPENNESS'], 'CONSCIENTIOUSNESS': pr['CONSCIENTIOUSNESS'],'EXTRAVERSION': pr['EXTRAVERSION'],'AGREEABLENESS': pr['AGREEABLENESS'],'NEUROTICISM': pr['NEUROTICISM']}
                person_data.update(i)
               # print("\n",pr)
                #i=i
                #zapisz w pliku test4.csv
                writer.writerow(person_data)
                
print("gotowe!")