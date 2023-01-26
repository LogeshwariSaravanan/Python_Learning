"""
SI=(p*n*r)/100

p -->principle
n -->number of years
r -->rate of interest
SI -->simple interest

CI=p*(1+r/100)**t

"""
p=int(input("enter the principle amount "))
n=int(input("enter the number of years "))
r=int(input("enter the rate of interest "))
SI=(p*n*r)/100
print("simple interest for {} is {}".format(p,SI))
