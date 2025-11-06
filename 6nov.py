import  numpy as np  

a= np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])
""""
a[0,1:3] =[33,44]
print(a)
print(a)
print(a[0])
print(a[1,2:5])  #1 ==> row  index  2:5 col index 
print(a[1:3,1:3])
print(a[0, : : -1])
"""

# arange  : 

"""b=np.arange(1,21).reshape(5,4)   # total ==>20
# print(b)
b[0,1:3] =[33,44]  # array manupulation  
# b[1:3,1:3]=[55,66,77,88]
print(b)
"""

# np.zero() , np.ones(),np.full(),np.full_like()

"""b=np.zeros((2,4))
print(b)

c=np.ones((2,4),dtype=int)
print(c)

d=np.full((3,3),fill_value=10)
print(d)

e=np.full_like(a,fill_value=10)
print(e)
"""

# random : 

import random 

"""h=np.random.randint(low=-10,high=10,size=(3,3))
print(h)
"""
"""g= np.random.randint(low=10,high=50,size=9).reshape(3,3)
print(g)
"""

"""
i=np.random.random_sample(size=(3,3))
print(i)
"""
#task  : 1 
"""
1 1 1 1 1 
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1
"""