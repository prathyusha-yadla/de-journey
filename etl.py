import pandas as pd
#Extract the csv file 
df =pd.read_csv("sales.csv")
#transform add the total column
df["total"] = df["quantity"] *df["price"]
#load it as parquet 
df.to_parquet("sales.parquet", index=False)

print("done! rows:", len(df))
print(df)