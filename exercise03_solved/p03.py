import pandas as pd
import pdb

data = {
    "ID": [1, 2, 3, 4],
    "Score": [50, 60, 70, 80]
}

df = pd.DataFrame(data)

df["Score"] = df["Score"].apply(lambda x: x*2)

print(df)  
