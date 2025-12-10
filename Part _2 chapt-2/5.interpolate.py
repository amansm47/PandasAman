#interpolate() function uses linear interpolation to fill in missing values in a pandas DataFrame or Series.
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

#linear,polynomial,time

df = df.infer_objects(copy=False)
df.interpolate(method="linear",axis=0,inplace=True)

print(df)