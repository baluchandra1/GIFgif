import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

x = np.linspace(-1, 1, 1000)
y1 = np.sqrt(1-x**2)
y2 = -np.sqrt(1-x**2)

fig = plt.figure()
plt.plot(x, y1, color = 'k')
plt.plot(x, y2, color = 'k')

w = random.randint(70, 90)
print(y1)
w1 = np.sqrt(1-(w/100)**2)
print(w1)
point1 = [-w/100, -w1]
point2 = [w/100, -w1]
k = random.randint(200, 800)
x_values = [point1[0], point2[0], 0, point1[0], x[k], point2[0]]
y_values = [point1[1], point2[1], 0, point1[1], y1[k], point2[1]]
plt.plot(x_values, y_values, 'bo', linestyle="--")

#def update(frame):


#ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()