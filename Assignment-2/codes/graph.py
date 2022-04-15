import numpy as np
import matplotlib.pyplot as plt

# function for plotting negative sign opening of |x+3|
def f1(x):
    return x+3;

# function for plotting positive sign opening of |x+3|
def f2(x):
    return -(x+3);
fig = plt.figure()

# generating values for plotting graph from x = -3 to 3
x1 = np.arange(-3,3,0.01)
y1 = f1(x1)
# generating values for plotting graph from x = -6 to -3
x2 = np.arange(-6,-3,0.01)
y2 = f2(x2)

ax = plt.gca()

# plotting graph from x = -3 to 3
ax.plot(x1, y1,"b")
# plotting graph from x = -6 to -3
ax.plot(x2, y2,"b")

# coloring area that we are integrating
ax.fill_between(x1,0,y1,color="yellow")
ax.fill_between(x2,0,y2,color="yellow")

# labeling axis
plt.xlabel("x-axis")
plt.ylabel("y-axis")

ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

# Displaying graph
plt.show()
