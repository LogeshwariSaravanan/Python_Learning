number1=int(input("enter the value of number1: "))
number2=int(input("enter the value of number2: "))
if number1>number2:
    print("greatest number is ",number1)
else:
    print("greatest number is ",number2)


lst=[]
for i in range(2):
    num=int(input("enter num "))
    lst.append(num)
print(lst)
lst.sort()
print(lst[-1])