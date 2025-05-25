import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


new_data_set["Viewership_Millions"].plot(kind='hist',bins=20,title='Viwership in millions comparation')
plt.xlabel="Viewership_Millions"
plt.tight_layout()
plt.show()

new_data_set.plot.scatter(x="Viewership_Millions",y="Title")
plt.xlabel="Viewership_Millions"
plt.tight_layout()
plt.show()

new_data_set['Genre'].value_counts().head(5).plot(kind="bar",title="first five generes")
plt.xlabel="Genre"
plt.ylabel("Count")
plt.tight_layout()
plt.show()