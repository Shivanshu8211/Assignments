import matplotlib.pyplot as plt

# Data from question
"""  __________________________________________
        Age(in years)   |  Number of children 
            1-2         |         5
            2-3         |         3
            3-5         |         6
            5-7         |         12
            7-10        |         9
           10-15        |         10
           15-17        |         4
     ___________________|_______________________
"""
l_val=[1,2,3,5,7,10,15]
r_val=[2,3,5,7,10,15,17]
freq=[5,3,6,12,9,10,4]
"""
Adjusted Frequency =(Frequency×Required size of interval)/Current size of interval
Required size of interval = minimum size of interval
"""
# Calculating Adjusted frequency
adjusted_freq = []
minimum_interval = min(r_val)-min(l_val)
for i in range(len(freq)):
    adjusted_freq.append((freq[i]*minimum_interval)//(r_val[i]-l_val[i]))

# Creating required list 'a' for plotting histogram  
a=[]
for i in range(len(adjusted_freq)):
    for j in range(adjusted_freq[i]):
        a.append((l_val[i]+r_val[i])/2)    

# Lables
plt.xlabel('No. of childrens')
plt.ylabel('Age(in years)')

# Plotting graph
plt.title('Analysis of childern of various age group playing in playground')
plt.hist(a,bins = [1,2,3,5,7,10,15,17],facecolor='r',alpha=0.9,rwidth=0.97)
plt.show()
