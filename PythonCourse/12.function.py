# FUNCTION --> block of code which only runs when it is called
"""
function definition --> block of code is explained
function calling --> it is used to execute the function
A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""

def factorial(x):#fuction definition
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact

number=int(input("enter the number: "))
print(factorial(number))#function call

# types of arguments:--> 4 types
# 1.REQUIRED arguments
# 2.KEYWORD arguments
# 3.DEFAULT arguments
# 4.VARIABLE LENGTH arguments


# EXAMPLE FOR REQUIRED arguments
"""
no.of arguments should be same in both function definition and function call
order/position is required
"""
print("REQUIRED ARGUMENTS")


def display(a, b):
    print(a, b)


display(2, 3)

# EXAMPLE FOR KEYWORD arguments
"""
order/position is not required
initialization will be done based on keword(name)
"""

print("KEYWORD ARGUMENTS")


def display1(a, b):
    print(a, b)


display1(b=10, a=20)

# EXAMPLE FOR DEFFAULT ARGUMENTS
"""
no.of arguments need not be match with both f.call and f.definition
some arguments will be consider as DEFAULT
"""
print("DEFAULT ARGUMENTS")


def display2(name="abc", course="B.E"):
    print(name, course)


display2(name="pqr", course="B.Sc")
display2(name="lmn")
display2()

# EXAMPLE FOR VARIABLE LENGTH ARGUMENTS
"""
arbitary no of ARGUMENTS
By placing * as prefix to the arguments of f.definition
"""

print("VARIABLE LENGTH ARGUMENTS")


def display3(*subjects):
    for i in subjects:
        print(i)


display3("B.E", "B.Sc", "B.TECH", "MCA", "MBA")