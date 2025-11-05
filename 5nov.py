# numpy  :  array  menupulation   ==> 1 d array  2 d array ==> matrix  

# list  :  mutable  ==> changes  in list . 

"""l1= [1,2,3,4,5,6,6,7,8]   ==> 1 d list 
print(l1)
print(type(l1))
"""
# index start  : 0 
"""
l1[3] ="avdh"
print(l1)
"""
"""
l2 =[[1,2,3],[4,5,6],[7,8,9]]
print(l2)
for i in l2 :
    print(i)
"""

import numpy as np   # ==> access np 

"""
a= np.array([1,2,3,4,5,6,7,8,9,"ram",89.90,8j])  # default  ==> string 
print(a)

b=np.array([1,2,3,4,6,7,8,9,89.90],dtype=int)   # ==> 1 d array 
print(b)
print(b[0])  # index start  : 0
print(b[6])
print(b[2:6])  # slicing  : 2 index number  6 index number  ==> last index excluded 
print(b[1:8:2])  # 1 start index 8 end index  2 step  size 
print(b[1:8:3])  # 1 start index 8 end index  3 step  size 
print(b[-1])
print(b[4 :-2])
print(b[ : : -2])
print(b[ : : -1])
"""

c=np.array([[1,2,3],[4,5,6],[7,8,9]])  # 2 d array
# print(c)
"""
[[1 2 3]    ==> 1 row  index 0     1 col index  ==>0  
 [4 5 6]    ==> 2 row  index 1     2 col index  ==>1
 [7 8 9]]   ==> 3 row  index 2     3 col index  ==>2
 r c 
(0,0) 1 (0,1)2 (0,2)3
(1,0) 4 (1,1)5 (1,2)6
(2,0) 7 (2,1)8 (2,2)9
"""
"""print(c[0])
print(c[0][0])
print(c[2][1])
print(c[1:3][0])
"""

d=np.arange(1,20)  #  1  d array 
print(d)

e= np.arange(1,21,2)
print(e)

f =np.arange(1,21).reshape(2,10)   # total  element  ==>20   ==> matrix  ==> 2 d array 
print(f)
