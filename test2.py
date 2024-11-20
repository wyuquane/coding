import numpy as np
N = 120
ma = np.arange(N)
ma = ma.reshape(8,15)
ma = ma.transpose()
ma = ma.reshape(2,4,-1)
print(ma)
transposed = ma.transpose((1,0,2))
print(transposed[0,1,2])