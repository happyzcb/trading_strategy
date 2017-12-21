import pandas as pd
import numpy as np

# Create series
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
print(s.index)

# DataFrame
## create DataFrame
dates = pd.date_range('20130101',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)

# 导入函数库
#import jqdata

# 初始化函数，设定基准等等
def initialize(context):
    security = '000001.XSHE'
    start_date = '2016-07-01'
    end_date = '2016-07-20'
    frequency = 'daily'
    fields = ['open','high','low','close']
    df = get_price(security, start_date, end_date, frequency, fields)
    print(df)
    print('head')
    print(df.head())
    print('tail')
    print(df.tail)
    print(df.index)
    print(df.values)
    print(df.describe)
    print(df.T)
    df.sort(columns='open')
    print(df)