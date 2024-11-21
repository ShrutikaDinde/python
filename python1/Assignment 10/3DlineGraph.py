
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
# Create a figure
fig = plt.figure()

# syntax for 3D projection
ax = fig.add_subplot(111, projection='3d') 
# defining all axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)

# Plotting
ax.plot3D(x, y, z, 'green')
ax.set_title("3D Line")
plt.show()