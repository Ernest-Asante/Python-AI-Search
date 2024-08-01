import numpy2 as np
from numpy2 import random

a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(c[1, 2])

print(b[::2])


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
x = arr.copy()
y = arr.view()

print(arr.shape)
print(newarr)
print(x.base)
print(y.base)

for x in c:
  for y in x:
    print(y)



arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

x = random.randint(100)
print(x)

y=random.randint(100, size=(5))

print(y)

z = random.randint(100, size=(3, 5))

print(z)

u = random.rand(5)

print(u)

w = random.choice([3, 5, 7, 9], size=(3, 5))

print(w)


p = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(p)