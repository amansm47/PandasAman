"""
vertically (row-wise) or horizontally (column-wise) concatenate pandas objects.
"""

#vertically concatenate
import pandas as pd
df_Region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Ram','Shyam']
})
#region 2 dataframe
df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['Aditi','Simran']
})

#concatenate

#df_concat= pd.concat([df_Region1,df_Region2], axis=0,ignore_index=True) #axis=0 for row wise concatenation
df_concat= pd.concat([df_Region1,df_Region2], axis=1,ignore_index=True) #axis=1 for column wise concatenation
print(df_concat)
