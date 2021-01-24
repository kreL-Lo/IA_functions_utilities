import nashpy as nash
import numpy as np
A = np.array([[1,0,4],[0,8,2],[4,2,3]])     
B = np.array([[2,0,1],[3,2,5],[0,-1,3]])
rps =nash.Game(A,B)
d = rps.support_enumeration()
print('PROBABILITATILE A,B')
for x in d:
    print(x)