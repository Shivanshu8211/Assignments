print("Write the the expression which is in the mod : ")
exp=list(input())
l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))
"""
The expression |x+3| is changing its sign at x=-3
so we need to integrate it from lower limt to -3
and then fro -3 to upper limit.
"""
# integration from lower limit to -3
# I1 = -((x^2/2) + 3x)
I1 = -((((-3)**2)/2) + 3*(-3) - ((((l)**2)/2) + 3*(l)))

# integration from -3 to upper limit
# I2 = (x^2/2) + 3x
I2 = ((u**2)/2) + 3*(u) - ((((-3)**2)/2) + 3*(-3))

I = I1+I2
print("The integral of |x-3| over limit -6 to 3 is :",I)
