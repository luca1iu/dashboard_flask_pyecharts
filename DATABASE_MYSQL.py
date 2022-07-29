import pandas as pd
from sqlalchemy import create_engine, MetaData

pd.set_option('display.max_rows', None)  # 不限制
pd.set_option('display.max_rows', 200)  # 200行
pd.set_option('display.max_columns', None)  # 不限制
pd.set_option('display.max_columns', 200)  # 200列

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('deploy', 'Genetsis2019@',
                                                               'rm-uf66010lgas9h78138o.mysql.rds.aliyuncs.com', '3306',
                                                               'g-data-prod'))

engine2 = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('deploy', 'Genetsis2019@',
                                                                'rm-uf66010lgas9h78138o.mysql.rds.aliyuncs.com', '3306',
                                                                'lladro'))

conn = engine.connect()
metadata = MetaData()
connection = engine.connect()
print(engine.table_names())
print(engine2.table_names())


