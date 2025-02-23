import numpy as np

#All 0s matrix
a = np.zeros((2,3,2))
print(a)

#All 1s matrix
b=np.ones((4,2,2),dtype='int32')
print(b)

#Any other number
c=np.full((2,2),11)
print(c)

#Any other n=number (full_like) using another array

d=np.full_like(a,4)
print(d)

#Random decimal numbers
e=np.random.rand(4,2)
print(e)

f=np.random.random_sample(a.shape)
print(f)

#random integer values
g=np.random.randint(2,8,size=(3,3)) #numbers are between 2-7
print(g)

#identity matrix
h=np.identity(5)
print(h)

#Repeat an array
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)

output=np.ones((5,5))
print(output)
z=np.zeros((3,3))
print(z)
z[1,1]=9
output[1:4,1:4]=z
print(output)

###Be Careful while copying arrays!!!

##a=np.array([1,2,3])
##b=a.copy()  use b=a.copy() instead of b=a to avoud changes in a