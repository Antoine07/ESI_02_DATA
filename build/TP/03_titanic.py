import numpy as np
import urllib.request
import pandas as pd 

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = urllib.request.urlopen(url)
# print(data)

# DataFrame
titanic_data =  pd.read_csv(data)

print(titanic_data.head(2))