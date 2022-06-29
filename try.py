from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

# create the parametric curve
x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

# create the first plot
point, = ax.plot([], [], [], 'r.')
point2, = ax.plot([], [], [], '.')
# line, = ax.plot(x, y, z, label='parametric curve')
# ax.legend()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])


# second option - move the point position at every frame
def update_point(n, x, y, z, point):
    point2.set_data([x[0:n], y[0:n]])
    point2.set_3d_properties(z[0:n], 'z')
    point.set_data([x[n], y[n]])
    point.set_3d_properties(z[n], 'z')
    # point.set_array([255,0,0])
    return point


ani = animation.FuncAnimation(fig, update_point, 99, fargs=(x, y, z, point))
ani.save('test5.gif', writer='pillow')
plt.show()
