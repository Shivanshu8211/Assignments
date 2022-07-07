import matplotlib.pyplot as plt
import numpy as np
"""
f_1 = open("X.dat",'r')
f_2 = open("Y.dat",'r')
X = f_1.readlines()
Y = f_2.readlines()
"""
X = np.linspace(0,1,1000000)
Y = np.loadtxt('Y.dat',unpack = True)
plt.scatter(X,Y)
plt.show()
