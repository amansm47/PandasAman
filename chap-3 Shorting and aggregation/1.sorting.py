#sorting data
#SORTING DATA 1COLUMN sort_values()
#df.sort_values(by='column_name',true/false, inplace=true )

import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,34,22,30, 29, 40, 25,32],
    "Salary": [50000, 60000,45000, 52000, 49000, 70000,48000, 58000],
    "Performance Score": [85,90,78,92,88,95,80,89]
}
df= pd.DataFrame(data)
print("Original DataFrame")
print(df)
# df.sort_values(by='Age', ascending=True, inplace=True) #this is for accending order
df.sort_values(by='Age', ascending=False, inplace=True) #this is for decending order

print(df)