#!/usr/bin/env python
# coding: utf-8

# In[16]:


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
with open('data1/test4.csv', 'w', newline='') as csvfile:
    #nazwy kolumn- wszystkie z plików json
    fieldnames = ["Timestamp","Affective","Order1","Order2","Order3","Order4","Asteroid","Type","ID","By","Bolt","Key","Scene","RotationX","RotationY","RotationZ","RotationW","PositionX","PositionY","PositionZ"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #ustawienie nagłówków
    writer.writeheader()
    
    #dla każdego id otwórz plik json
    for my_id in ids:
        fi=open("data1/SUB" + str(my_id) + "-Space.json")
        x = json.load(fi)
        #dla każdej paczki danych (w tych klamerkach: {} z pliku)
        for i in x:
            #sprawdź czy ma klucz 'ID'
            if ('ID' in i):
                #zapisz w pliku test4.csv
                writer.writerow(i)
                
print("gotowe!")


# In[19]:

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
#otwórz plik test4.csv z ',' jako separatorem danych
md1 = pd.read_csv("data1/test4.csv", sep=',')

#pozbywanie się kolumn nie mających znaczenia dla eksperymentu
md1 = md1.drop(['Affective','Timestamp','Order1','Order2','Order3','Order4', 'Scene', 'RotationX', 'RotationY','RotationZ','RotationW','PositionX','PositionY','PositionZ'], axis=1)
#wyświetl początek
md1.head()



