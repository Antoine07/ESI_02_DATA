import os
import csv
import numpy as np
import urllib.request
import pandas as pd 

file = 'titanic.csv'
path = os.path.abspath(file)

if  not ( os.path.exists(path) and os.path.getsize(path) > 0 ) :
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    data = urllib.request.urlopen(url)
    titanic_data =  pd.read_csv(data)
    titanic_data.to_csv(path, index=False)

    
titanic_data =  pd.read_csv(path)