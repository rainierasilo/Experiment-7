import numpy as np

A = np.arange(1,101,1)
a = A.resize(10,10)

B = np.multiply(A,A)
divide = B[B%3 == 0]
print(B)
