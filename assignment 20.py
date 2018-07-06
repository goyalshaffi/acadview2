 # q1
import pandas as pd
'''
data={'name':['tom','jack','steve','ricky'],'age':[28,34,29,42],'mail id':['toma@gmail.com','jack@gmail.com','steve@gmail.com','ricky@gmail.com'],
      'phone no':[5872789379,7689036091,9879797767,6869810878]}
df=pd.DataFrame(data)
print(df)
'''

# q2

df=pd.read_csv('assignment.csv')
print(df)
# a
print(df.head(5))
# b
print(df.head(10))
# d
print(df.tail(5))
# c
print(df['MinTemp'].max())
print(df['MinTemp'].mean())
print(df['MinTemp'].median())
print(df['MinTemp'].mode())






