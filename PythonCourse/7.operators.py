"""
operators are used to perform operations on variables and values

operator --> indicates what action or operation to perform

operand --> indicates what item to apply the action to

types of operators are:
    *Arithmetic operators   `--> + , - , * , / , % , ** , //
    *Assignment operators    --> = , += , -= , *= , /= , %= , **= , //= , &= , |= , ^= , <<= , >>=
    *Relational operators    --> == , != , > , < , >= , <=
    *Logical operators       --> and , or , not
    *Bitwise operators       --> & , | , ^ , ~ , << , >>
    *Identity operators      --> is , is not
    *Membership operators    --> in , not in

"""
#ARITHMETIC OPERATOR

print("ARITHMETIC OPERATORS")
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
print("addition of",a ,"and" , b, "is: ",a+b)
print("subtraction of",a ,"and" , b, "is: ",a-b)
print("multiplication of",a ,"and" , b, "is: ",a*b)
print("division of",a ,"and" , b, "is: ",a/b)
print("modulus of",a ,"and" , b, "is: ",a%b)
print("exponentiation of",a ,"and" , b, "is: ",a**b)
print("floor division of",a ,"and" , b, "is: ",a//b)

#ASSIGNMENT OPERATOR

print("ASSIGNMENT OPERATORS")
a=int(input("enter the value of a: "))
print("here value 5 is assigned to a by using =: ",a)
a+=5
print(a)
a-=5
print(a)

#RELATIONAL OPERATOR
print("RELATIONAL OPERATOR")
num_1 =int(input("enter the number 1: "))
num_2 =int(input("enter the number 2: "))
if num_1 >100:
    print(num_1, "is greater than 100 ")
print(num_1>num_2)
print(num_1<num_2)
print(num_1>=num_2)
print(num_1<=num_2)
print(num_1==num_2)
print(num_1!=num_2)

#LOGICAL OPERATOR

print("LOGICAL OPERATOR")
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
print(x>=y and x==y)
print(x>y or x<y)
print(not(x>y))

#BITWISE OPERATOR

print("BITWISE OPERATOR")
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
print(a&b)# bitwise multiplication
print(a|b)#bitwise OR
print(a<<b)#left shift
print(a>>b)#right shift
#<< left shift --> double the value (shortcut --> multiply the number by binary  index value
""" 12<<1
here number is 12 #index number -->3 2 1 0
choose the 1st index value ie 2   (8 4 2 1)
multiply the 12 and 2
"""
"""12<<2
12*4
"""
#>> right shift --> half the value (shortcu --> divide the nuber by binary index value


#IDENTITY OPERATOR

print("IDENTITY OPERATOR")
x=int(input("enter the value of x: "))
y=int(input("enter the value of y: "))
print(x is y)
print(x is not y)

#MEMBERSHIP OPERATOR

print("MEMBERSHIP OPERATOR")
str=input("enter the string: ")
print('s' in str)
print('e' not in str)