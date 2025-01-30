import pandas as pd
import pdb

data = {
    "ID": [101, 102, 103, 104, 105],
    "Category": ["A", "B", "A", "B", "C"],
    "Value": [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

filtered_df = df[df["Category"] == "A"]

print(filtered_df)  

