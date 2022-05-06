import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Accesing tables
read_tab1 = pd.read_excel("Tables\\Table_1.xlsx")

# Data from question
"""  __________________________________________
        Age(in years)   |  Number of childrens 
            1-2         |         5
            2-3         |         3
            3-5         |         6
            5-7         |         12
            7-10        |         9
           10-15        |         10
           15-17        |         4
     ___________________|_______________________
"""

# Reading data from table 1 given in quetion from Table_1.xlsx
l_val = read_tab1["L_Age"]
r_val = read_tab1["U_Age"]
freq = read_tab1["Number of children"]
class_interval = ["{}-{}".format(l_val[i],r_val[i])for i in range(7)]
    
"""
Adjusted Frequency =(Frequency×Required size of interval)/Current size of interval
Required size of interval = minimum size of interval
"""

# Calculating Adjusted frequency
adjusted_freq = []
minimum_interval = min(r_val) - min(l_val)
for i in range(len(freq)):
    adjusted_freq.append((freq[i]*minimum_interval)//(r_val[i]-l_val[i]))

# Creating required list 'a' for plotting histogram  
a=[]
for i in range(len(adjusted_freq)):
    for j in range(adjusted_freq[i]):
        a.append((l_val[i]+r_val[i])/2)

# writing data in table 2
write = pd.DataFrame({"Age(in years)":class_interval,"Adjusted fequency":adjusted_freq})
write.to_excel("Tables\\Table_2.xlsx",index=False)

# Lables
plt.xlabel('No. of childrens')
plt.ylabel('Age(in years)')

# Plotting graph
plt.title('Analysis of childern of various age group playing in playground')
plt.hist(a,bins = [1,2,3,5,7,10,15,17],facecolor='r',alpha=0.9,rwidth=0.97)
plt.show()
