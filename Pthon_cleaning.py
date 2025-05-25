import numpy as np
import pandas as pd

#cleaning the data
data_set=pd.read_csv("data.csv",na_values=[""," ","  ","\t","\xa0"])

data_set.replace(r'^\s*$', np.nan, regex=True, inplace=True)


print (data_set)

for col in data_set.columns:
    if data_set[col].dtype=="object":
        data_set[col].fillna(data_set[col].mode()[0],inplace=True)
    else:
        data_set[col].fillna(data_set[col].mean(),inplace=True)
        
print("missing vales",data_set.isna().sum())


data_set.to_csv("cleaned_data_file.csv", index=False)

#taking the cleaned csv file for analysing the data

new_data_set=pd.read_csv("cleaned_data_file.csv")

#No duplicate values in the data set
print(new_data_set.duplicated().sum())