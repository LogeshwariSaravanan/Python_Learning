
"""
python has a build-in modules that we can use for mathematical tasks.
for that we have to import math module
this math module has a set of methods and constants
"""
import math#math - module
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print(a+b)#addition
print(a-b)#subtraction
print(a*b)#multiplication
print(a/b)# gives quotient value
print(a%b)#gives remainder value
c=float(input("enter the float value: "))
print("this function return the round off value of c: ",round(c))
d=-5
print("this function return the absolute value of d: ",abs(d))#absolute
print(a**b)
print("this function return a power b value:",pow(a,b))
print("this function return maximum of a and b: ",max(a,b))
print("this function return minimum of a and b: ",min(a,b))

#using math modules
print("this function return round off to the next number: ",math.ceil(c))#round off to next number
print("this function return round off to the previous number: ",math.floor(c))#round off to previous number
print("this function return the factorial value: ",math.factorial(b))