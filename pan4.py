import pandas as pd

df = pd.read_csv('ret.csv')
df.head()#print the first "n" rows in the dataframe [default n=5]

print(df)

df['Lineprice'] = df['Quantity'] * df['unitPrice']

df.head()

print(df)

df_customers = (df.groupby('CustomerID').agg(
order = ('invoiceNo','nunique'),
skus =('StockCode','nunique'),
quantity =('Quantity','sum'),
revenue=('LinePrice','sum'),
).reset_index())

df_customer.head()

print(df_customers)
