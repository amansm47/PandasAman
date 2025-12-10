#fillna()
#fillna(value,inplace=True) function is used to fill missing values in a DataFrame or Series in pandas.
import pandas as pd

data= {
    "Name": [ 'Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],  

    "Age" : [28,None, 22, 30, 29, 40,25,32],

    "Salary": [50000, None, 45000, 52000, 49000, 70000,48000, 58000],

    "Performance_Score": [85, None, 78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)

#df.fillna(value=0, inplace=True)   
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Performance_Score'].fillna(df['Performance_Score'].mean(), inplace=True)
print(df)