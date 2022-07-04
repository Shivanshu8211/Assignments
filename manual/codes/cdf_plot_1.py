#Importing numpy, scipy, mpmath and pyplot         
import numpy as np
import matplotlib.pyplot as plt

################################################################
new_cdf = []
X = np.linspace(-1,2,100)
for i in X:
	if i<0:
		new_cdf.append(0)
	elif i>1:
		new_cdf.append(1)
	else:
		new_cdf.append(i)
###############################################################

x = np.linspace(-4,4,50)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x.T,err,'o')
plt.plot(X,new_cdf)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.show() #opening the plot window
