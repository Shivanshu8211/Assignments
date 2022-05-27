import math

print("(a.)")
r = int(input("enter random variable: "))
print("probability associated with random variable ",r," is ",math.comb(10,r)*1/1024)

print("(b.)")
# Here random variable y = (x-3)^3 takes th evalues y=k^2 k = 0,1,....,7
print("probability associated with random variable y=",0," is ",math.comb(10,3)*1/1024)
print("probability associated with random variable y=",1," is ",(math.comb(10,2)+math.comb(10,4))*1/1024)
print("probability associated with random variable y=",2," is ",(math.comb(10,1)+math.comb(10,5))*1/1024)
print("probability associated with random variable y=",3," is ",(math.comb(10,0)+math.comb(10,6))*1/1024)
print("probability associated with random variable y=",4," is ",math.comb(10,7)*1/1024)
print("probability associated with random variable y=",5," is ",math.comb(10,8)*1/1024)
print("probability associated with random variable y=",6," is ",math.comb(10,9)*1/1024)
print("probability associated with random variable y=",7," is ",math.comb(10,10)*1/1024)
