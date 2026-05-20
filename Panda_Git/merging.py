import pandas as pd

df1 = pd.DataFrame({"letter": ["A", "B", "C", "D"], "number": [1, 2, 3, 4]})

df2 = pd.DataFrame({"letter": ["C", "D", "E", "F"], "number": [3, 4, 5, 6]})


df3 = df1.merge(df2, how="inner", on="number")


df4 = pd.concat([df1, df2]).reset_index(drop=True)


df5 = pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)


print(df3, df4, df5)
