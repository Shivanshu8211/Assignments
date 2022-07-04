#Importing numpy, scipy, mpmath and pyplot         
import numpy as np
import math
import matplotlib.pyplot as plt

#################################################
new_pdf = []
X = np.linspace(-4,4,500)
for i in X:
	if i<0:
		new_pdf.append(0)
	else:
		new_pdf.append(1-math.exp(-i/2))
#################################################

x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('N_uni.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x.T,err,"o")#plotting the CDF
plt.plot(X,new_pdf)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.show() #opening the plot window
