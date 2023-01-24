
"""
Variables -->Variables are containers for storing data values

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""
#dynamically typed language

price=100
print(price)
name="LogeshwariSaravanan" #name - variable
print(name)
print("hi "+name)


"""
Rules for naming a variable
    *variable name must start with letter or underscore character.
    *variable should not start with number.
    *variable names are case sensitive.
    *variable name contain alpha-numeric character.
    *variable name should not key words
"""

# many value to multiple variables

x,y,z="apple","orange","banana"
print(x)
print(y)
print(z)
name, height, age="logeshwari", 135,22
print(age)
print(name)
print(age)

#one value to multiple variables

a=b=c=10
print(a,b,c)
like=dislike=100
print(like)
print(dislike)

#unpack a list

numbers=[100,400,500,600]
l,*m,n=numbers
print(l)
print(m)
print(n)