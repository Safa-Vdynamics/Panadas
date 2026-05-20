import pandas as pd

df1 = pd.DataFrame({"letter": ["A", "B", "C", "D"], "number": [1, 2, 3, 4]})

df2 = pd.DataFrame({"letter": ["C", "D", "E", "F"], "number": [3, 4, 5, 6]})


df3 = df1.merge(df2, how="left", on="number")
print(df3)
