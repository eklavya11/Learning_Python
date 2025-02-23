import numpy as np
a=np.genfromtxt('data.txt',delimiter=',')
a=a.astype('int32')
print(a)

##Boolean Masking and Advance indexing

print(a>50)
print(a[a>20])

#you can index with a list in numpy

b=np.array([1,2,3,4,5,6,7,8,9])
print(b[[1,2,8]])