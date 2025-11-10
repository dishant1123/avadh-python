import  numpy as np

"""a= np.arange(1,21,2)
# print(a)

b= np.arange(1,21).reshape(5,4)
# print(b)

c=np.zeros((2,4),dtype=int)
# print(c)

d=np.ones((2,4),dtype=int)
# print(d)

e=np.ones((3,5,2),dtype=int)
# print(e)

s=np.ones((3,4,3),dtype=int)
# print(s)

t=np.full((3,4),fill_value=10)
# print(t)

y=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

print(y)

g=np.full_like(y,fill_value=10)
# print(g)

g=g.reshape(10,2)
print(g)
"""
# random : 

import random  

"""a=np.random.random_sample((5,5))
print(a)

b= np.linspace(1,10,num=3)   # 1 start  10  end  num =5 
print(b)

# formula  :  end -start  / n-1    ==> 10 -1 / 2 ==> 4.5

"""

# array attributes : 
x=np.random.randint(low=-30,high=50,size=12).reshape(4,3)
print(x)

print(x.shape)
print(x.ndim)
print(x.size)
print(x.itemsize)  # how many bytes to store  each array element 

print(x.T)  # transpose  

