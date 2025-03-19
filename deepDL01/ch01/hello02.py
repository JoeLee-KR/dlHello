import numpy as np

x = np.array([1.2,4.2,9.3])
print(x)

y = np.array([1.0,2.0,3.0])
print(y)

z = 2

print( x+y )
print(x * y)
print(x/y)
print(x/z)

x = np.array( [ [3,0], [0,6] ] )
print(x)

X = np.array( [[51,55], [14,19], [0,4]] )
print(x)

for RRR in X:
    print(RRR)

X = X.flatten()
print(X)
print( X[np.array([0,2,4])] )
print( X[ [0,2,4] ] )
print( X>15 )
print( X[ X>15 ])