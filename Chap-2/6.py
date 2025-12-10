import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,34,22,30, 29, 40, 25,32],
    "Salary": [50000, 60000,45000, 52000, 49000, 70000,48000, 58000],
    "Performance Score": [85,90,78,92,88,95,80,89]
}
df = pd.DataFrame(data)
#display the dataframe
print("Sample Dataframe")
print(df)
print("Names (Single column return series)")
#single column return series
print(df['Name'])

#display multiple columns
print("\nNames and Age (Multiple columns return DataFrame)")
print(df[['Name','Age','Salary']])

#display specific rows and columns
print("\nSpecific Rows and Columns (loc)")
print(df.loc[2:5, ['Name', 'Performance Score']])