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