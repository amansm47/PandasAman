"""df["Column_Name"].sum()
df["Column_Name"].mean()
df["Column_Name"].media()
df["Column_Name"].min()
df["Column_Name"].max()
"""

import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,34,22,30, 29, 40, 25,32],
    "Salary": [50000, 60000,45000, 52000, 49000, 70000,48000, 58000],
    "Performance Score": [85,90,78,92,88,95,80,89]
}
df= pd.DataFrame(data)
avg_salary = df["Salary"].mean()
print("Average Salary:", avg_salary)