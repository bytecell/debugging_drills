import pandas as pd
import pdb

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})

df.loc[df["A"] >= 2, "B"] = 100

print(df)  

