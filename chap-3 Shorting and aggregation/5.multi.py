#multiple groupings
import pandas as pd

data= {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,34,22,30, 22, 40, 34,32],
    "Salary": [50000, 60000,45000, 52000, 49000, 70000,48000, 58000]
}
df= pd.DataFrame(data)
grouped = df.groupby(['Age','Salary'])["Salary"].size()
print(grouped)