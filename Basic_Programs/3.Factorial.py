"""
FACTORIAL -->multiplication of all the integer smaller than or equal to num

for example factorial of 5 is -->5*4*3*2*1 which is 120
"""

num=int(input("enter the number "))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)