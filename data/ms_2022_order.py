import pandas as pd
from pyecharts.faker import Faker

df = pd.read_csv('ms_order_day.csv')
print(df.info())
print(df.head())

print(df['pay_time'].values[:30])
print(df['GMV'].astype('int').values[:30])


print(Faker.days_attrs)
print(Faker.days_values)
for i in df['GMV'].astype('int').values[:30]:
    print(type(i))
