#head() tail()
#head() 5
#tail() 5
import pandas as pd
df = pd.read_json("Chap-2/sample_Data.json")

print("First 5 rows of the DataFrame:")
print(df.head())
print("\nLast 5 rows of the DataFrame:")
print(df.tail())