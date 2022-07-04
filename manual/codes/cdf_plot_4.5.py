#Importing numpy, scipy, mpmath and pyplot         
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,100)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list

randvar = np.loadtxt('Tri.dat',dtype='double')
for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x.T,err,'o',label='Experimental cdf')
#plt.plot(x.T,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

##################################################################################
x = np.linspace(-4,0,100)
plt.plot(x,x-x);
x = np.linspace(0,1,100)
plt.plot(x,(x**2)/2,label='Theoretical cdf');
x = np.linspace(1,2,100)
plt.plot(x,-(x**2)/2 +2*x -1);
x = np.linspace(2,4,100)
plt.plot(x,x-x+1);
leg = plt.legend();
##################################################################################

plt.show() #opening the plot window
