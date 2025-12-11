#merging joinning dataframes
import pandas as pd

#customer dataframe
df_cusotmer = pd.DataFrame({
    "CustomerID":[1,2,3,4],
    "CustomerName":["Ram","Shyam","Aditi","Simran"]
})

#orders dataframe
df_orders = pd.DataFrame({
    'CustomerID':[1,2,1,3,4,2],
    'OrderAmount':[250,450,300,150,500,700]
})

#merge
# df_merged = pd.merge(df_cusotmer, df_orders, on='CustomerID', how='inner')#inner join

df_merged = pd.merge(df_cusotmer, df_orders, on='CustomerID', how='outer')#outer join

print("inner join:")
print(df_merged)   

