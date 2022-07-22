import pandas_datareader.data as web
import datetime

start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2022, 7, 1)
df = web.DataReader('GOOGL', 'stooq', start, end)
print(df)