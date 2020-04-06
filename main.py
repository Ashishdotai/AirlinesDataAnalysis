import pandas as pd

file = 'SensorData.csv'

df = pd.read_csv(file)

#print(df)
print(df.head(10))

print(df.head(20))
