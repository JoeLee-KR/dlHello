import numpy as np
import matplotlib.pyplot as plt

x = np.arange( 0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y, label="sin(x)")
plt.plot(x,z, label="cos(x)")
plt.legend()
plt.show()