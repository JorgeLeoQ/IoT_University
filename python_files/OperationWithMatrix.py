#operation with numpy library
import numpy as np
from numpy import pi
#range operatio, create array with specific space
A = np.arange(10,30,5)
B = np.arange(0,2,0.3)

print(A)
print()
print(B)

#to define function 
x = np.linspace(0, 2*pi, 100)
f = np.sin(x)

#Basic operation
a = np.array([20,30,40,50]) #[20,30,40,50]
b = np.arange(4) #[0,1,2,3]

c = a-b # [20,30,40,50] - [0,1,2,3] = [20, 29, 38, 47]

d = b**2 #[0, 1, 4, 9]

e = 10*np.sin(a) #[ 9.12945251, -9.88031624,  7.4511316 , -2.62374854]

print(a < 35) #[ True,  True, False, False]

#product beetwen matrix
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])

C = A * B #elementwise product

D = A @ B #matrix product

E = A.dot(B) #another matrix product

rg = np.random.default_rng(1)     # create instance of default random number generator
a = np.ones((2,3), dtype=int)
b = rg.random((2,3))
a *= 3
b += a

#sum all elements and min max
a = rg.random((2,3))

print(a.sum())
print(a.min())
print(a.max())
