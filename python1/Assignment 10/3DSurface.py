from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T
z = (np.sin(x**2) + np.cos(y**2))

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis')

plt.show()

