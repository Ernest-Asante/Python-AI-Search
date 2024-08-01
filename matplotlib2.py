import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

ax = plt.axes(projection="3d")

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax.scatter(x, y, z)
ax.set_title("3D Plot")
ax.set_xlabel("test")
plt.show()