import pandas as pd
import pdb

df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})
df2 = pd.DataFrame({"UserID": [1, 2, 3], "Score": [90, 85, 88]})

merged_df = pd.merge(df1, df2, on="ID")  
print(merged_df)
