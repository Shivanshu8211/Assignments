import sympy as sy
import math
from scipy.integrate import quad
x=sy.Symbol("x")

f= lambda y : math.exp(-1*y**2/2)/math.sqrt(2*math.pi)

def G(x):
	y,err=quad(f,-math.inf,x)
	return y

for i in range(6):
    x=float(input("Enter k value:"))
    print("p(k) value is :",round(2*G(x)-1,4))
