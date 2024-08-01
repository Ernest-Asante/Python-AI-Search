import numpy  as np

ab = [1,2,3,4,5]

#print(a)
#print(a[1])
#print(a[1:4])
#print(type(a))

a_mul = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print(a_mul[0])
print(a_mul.shape)
print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)

a = np.full((2,3,4), 9)
print(a)

x_values = np.arange(0, 1000, 5)
print(x_values)