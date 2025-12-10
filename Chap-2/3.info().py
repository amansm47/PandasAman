#info() function in pandas is used to get a concise summary of a DataFrame.   It provides information about the DataFrame including the number of non-null entries, data types of each column, and memory usage.
import pandas as pd
df = pd.read_json("Chap-2/sample_Data.json")

print("Displaying the info of data set:")
print(df.info())

