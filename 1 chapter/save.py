import pandas as pd
data={
  "name": ["Alice", "Bob", "Charlie"],
  "age": [25, 30, 35],  
    "city": ["New York", "Los Angeles", "Chicago"]
}
df=pd.DataFrame(data)
print(df)
# 1)->Save the DataFrame to a CSV file
# df.to_csv("output.csv", index=False)
# 2)->Save the DataFrame to an Excel file
# df.to_excel("output.xlsx", index=False)

# 3)->Save the DataFrame to a JSON file
df.to_json("output.json", orient="records", lines=False)

