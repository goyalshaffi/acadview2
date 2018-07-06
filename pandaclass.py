import pandas as pd
import numpy as np

'''
data={'name':['tom','jack','steve','ricky'],'age':[28,34,29,42]}
df=pd.DataFrame(data)
print(df)


df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)
print(df.head(2))
print(df.tail(2))


import numpy as np
data={'name':pd.Series(['tom','jack','steve','ricky']),
      'age':pd.Series([28,34,29,42])}
      #'rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df=pd.DataFrame(data)
print("our data series is:")
print(df)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)
'''
df=pd.read_csv('sample.csv')
print(df)
print(df["name"])
data=np.array(['a','b','c','d'])
s=pd.Series(data)
print(s)
data1={'a':0.,'b':1.,'c':2.}
f=pd.Series(data1)
print(f)