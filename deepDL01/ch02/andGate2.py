import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
	    print("0")
    elif tmp > 0:
        print("1")
AND(0,0)
AND(1,0)
AND(0,1)
AND(1,1)
