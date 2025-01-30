import pandas as pd
import pdb

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})

subset = df[df["A"] >= 2]

subset["B"] = 100  

print(df)  

