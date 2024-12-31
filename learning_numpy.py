#multidimensional array library
#numpy is fast compared to list
#numpy has fixed type, faster to read less bytes of memory
#contiguous memory

#Applications
#mathematics,plotting(matplotlib),pandas

#to install numpy - pip install numpy (in terminal)
#to upgrade pip - pip install --upgrade pip
import numpy as np

a = np.array([1,2,3])
c = np.array([1,2,3],dtype='int16') #giving size explicitly
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(a)
print(b)

#Get dimension
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#Get type
print(a.dtype)
print(c.dtype)
print(b.dtype)

#get size

print(a.itemsize)
print(c.itemsize)

#get total size
#these 2 are same
print(a.size*a.itemsize)
print(a.nbytes)


#Accessing/Changing specific elements, rows, columns, etc

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a.shape)

#get specific element
print(a[1,2])
#get specific row
print(a[0,:])
#get specific column
print(a[:,0])
#[startindex:endindex:stepsize]=endindex is exclusive
print(a[0,1:6:2])

a[:,5]=5#setting all index 5 columns to 5
print(a)

a[:,2]=[1,2]#can change different values for both rows
print(a)

b = np.array([[[1,2],[3,4],[5,6],[7,8]]])#3dimensional
print(b)

print(b[0,1,1])