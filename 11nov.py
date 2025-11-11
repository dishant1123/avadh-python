import  numpy as np 

"""a= np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

print(a)
"""
# print  : 
"""
1. [[14,15],
    [19,20]]
    
2. [2,8,14,20]    
"""

# mathematical method  : 

"""
axis in numpy  : 

axis =0 do col wise 
axis =1 do row wise
"""

"""x=np.random.randint(low=0,high=10,size=(3,3))
print(x)

# print(x.sum())
# print(x.sum(axis=0))
# print(x.sum(axis=1))

# print(x+10)
print(x*2)
# print(x/3)
"""

# matrix multiplication  :
"""
a=np.random.randint(low=0,high=10,size=9).reshape(3,3)
b=np.random.randint(low=-5,high=10,size=9).reshape(3,3)

print("a=\n",a)
print("b=\n",b)

# print(a+b)  # addition ==> element  wise 
# print(a*b)  # it is  not matrix  multiplication ==> element wise 

matrix_multiply=np.matmul(a,b)
print(matrix_multiply)
"""

"""a=np.random.randint(low=0,high=10,size=9).reshape(3,3)
print(a)
x=np.sin(a)
y=np.sqrt(a)
print("x=\n",x)
print("y=\n",y)
"""

#np.where() => condition  
"""
b=np.random.randint(low=-5,high=10,size=9).reshape(3,3)

c=np.random.randint(low=-10,high=10,size=10)
print(c)
print(np.where(c>0))

print(b)
print(np.where(b>0))
"""

# np.nonzero() : 
b=np.random.randint(low=-5,high=10,size=9).reshape(3,3)
print(b)

# print(np.nonzero(b)) 
print(np.count_nonzero(b))
