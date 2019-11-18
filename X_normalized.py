import numpy as np

X = np.random.random((5,5))
stdv = np.std(X)

Z = ((X-X.mean())/stdv)
print(Z)
