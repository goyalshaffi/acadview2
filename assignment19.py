# q1
import numpy as np


a=np.random.random((10,1))
print(a)
print(a.shape)
b=np.mean(a)  # to find out mean of function
print(b)

# q2
c=np.random.random((20,1))
print(c)
d=np.var(c)  # to find out variation
print(d)
e=np.std(c)   #to find out standard deviation
print(e)


# q3

A=np.random.random((10,20))
B=np.random.random((20,25))
print(A)
print(B)
f=np.matmul(A,B)  # to find out the matrix multipication
print(f)
print(f.shape)
g=np.sum(f) # to find out the sum of elements of matrix
print(g)


# q4
from math import exp
a=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(a)
print(a.shape)
def f(x):
       return( 1/ (1 + exp(-x)))
for i in range(1,10):
    print(f(i))


