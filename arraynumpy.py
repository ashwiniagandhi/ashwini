import numpy as np

print("\n1-D Array")
a = np.array([1,2,3]) 
print(a)

print("\n2-D Array")
b=np.array([[1,4],[2,3]])
print(b)

print("\n3-D ARRAY")
c=np.array([[[1,2,3],[2,3,4],[3,4,5]]])
print(c)


print('\n\n')
a = np.array([1, 2], dtype = complex) 
print(a)


print('\n\n')
a = np.arange(9).reshape(3,3)

print('First array:') 
print(a) 
print('\n')  

print('second array')
b=np.array([5,5,5])
print(b)

print('add')
c=np.add(a,b)
print(c)

print('multiplication')
d=np.multiply(a,b)
print(d)

print('divided')
e=np.divide(a,b)
print(e)

print('subtract')
f=np.subtract(a,b)
print(f)




