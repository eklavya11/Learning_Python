#Mathematics
import numpy as np

a=np.array([1,2,3,4])
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)

#take the sin
print(np.sin(a))

#Linear Algebra
#In linear algebra the column count should be same as row count of matrix we multiply it with
a=np.ones((2,3))
print(a)
b=np.full((3,2),2)
print(b)

print(np.matmul(a,b))

#Find the determinant
c=np.identity(3)
print(np.linalg.det(c))

###statistics

stats = np.array([[1,2,3],[8,5,6]])
print(np.min(stats,axis=1))
print(np.min(stats))
print(np.max(stats))
print(np.sum(stats,axis=1))

#Reorganizing arrays

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape(4,2)
print(after)

#Vertically stacking vectors

v1 = np.array([1,2,3,4])
v2=np.array([5,6,7,8])

print(np.vstack([v1,v2,v1]))
print(np.hstack([v1,v2]))

