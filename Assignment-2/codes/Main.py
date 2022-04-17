"""
Assignment-2 (AI1103)
Shivanshu
AI21btech11027

Q8:- Evaluate integral of |x+3| over limit -6 to 3.
"""

from scipy.integrate import quad

def f(x):
    return abs(x+3);

print("Here we are calculating the  integration of |x+3| for some limit...")
l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))

ival,error = quad(f,l,u)
print("The integral of |x+3| over limit ",l," to ",u," is :",ival)

