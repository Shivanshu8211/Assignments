import matplotlib.pyplot as plt

# Data from question
a=[1,1,1,1,1,2,2,2,3,3,3,5,5,5,5,5,5,7,7,7,10,10,15,15]

# Lables
plt.xlabel('No. of childrens')
plt.ylabel('Age(in years)')

# Plotting graph
plt.title('Analysis of childern of various age group playing in playground')
plt.hist(a,bins = [1,2,3,5,7,10,15,17],facecolor='r',alpha=0.8,rwidth=0.97)
plt.show()
