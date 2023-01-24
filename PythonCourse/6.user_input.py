"""
Python allows for user input that means user can give input during runtime

python stops execution when it comes to the input() function, and continues when the user has give some input.
"""
name=input("enter the name: ")
print("hi "+name)

height=int(input("enter the height: "))
print(name+" is "+str(height)+'cm height')
print(name+" is "+str(height/2.54)+'inch height')
inch="{:.2f}".format(height/2.54)
print(inch)