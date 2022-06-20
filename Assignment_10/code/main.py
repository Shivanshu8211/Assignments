import numpy as np
from matplotlib.pyplot import *

# function for plotting upper region
def f1(x):
    return x+2;

# function for plotting lower region
def f2(x):
    return x-2;
fig = figure()

# generating values for plotting graph for upper region
x1 = np.arange(-6,2,0.01)
y1 = f1(x1)

# generating values for plotting graph for lower region
x2 = np.arange(-2,6,0.01)
y2 = f2(x2)

x3,y3 = [-6,0.5],[2.5,2.5]
x4,y4 = [0.5,6],[-1.5,-1.5]

ax = gca()

# plotting graph from x = -3 to 3
ax.plot(x1, y1,"b")
# plotting graph from x = -6 to -3
ax.plot(x2, y2,"b")

ax.plot(x3,y3,"b")
ax.plot(x4,y4,"b")

# coloring area that we are integrating
ax.fill_between(x1,4,y1,color="yellow")
ax.fill_between(x2,-4,y2,color="yellow")

# labeling axis
xlabel("x-axis")
ylabel("y-axis")

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

# Display garph
show()
