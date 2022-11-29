import numpy as np

# create int array
a = np.array([2, 3, 4])
print(a)
print(a.dtype)  # int64

# create float array
b = np.array([1.2, 3.5, 5.1])
print(b)
print(b.dtype)  # float64

# a = np.array(1, 2, 3, 4)  # WRONG
# a = np.array([1, 2, 3, 4])  # RIGHT

# if both int and float, int => float (1 => 1.)
c = np.array([(1.5, 2, 3), (4, 5, 6)])
print(c)
print(c.dtype)  # float64

# create complex array
d = np.array([[1, 2], [3, 4]], dtype=complex)
print(d)
print(d.dtype)  # complex128
