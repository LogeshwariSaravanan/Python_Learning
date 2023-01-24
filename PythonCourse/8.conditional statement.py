"""
conditional statements are used check the condition is true or false
"""
#If statement
# if the condition is true it will execute
print("IF STATEMENT")
a=5
b=4
if a>b:
    print("a is greater than b")


name="logeshwari"
if name[0]=='l' or name[0]=='L':
    print("true")


"""
if the condition is false it move to else and then execute
"""
print("IF ELSE STATEMENT")
a=10
b=5
if a<b:
    print("a is greater than b")
else:
    print("b is greater than a")


password_correct=True
if password_correct:
    print("logged In")
    print("Have a Nice Day")
else:
    print("Incorrect Password")
    print("Try Again")
print("Bye")


#elif ladder
ind_score=360
if ind_score>=360:
    print("India will Win")
elif ind_score<=250:
    print("India might Win")
elif ind_score>=150:
    print("Australia might Win")
else:
    print("Australia will Win")

"""
To check more than one condition we have to use elif statement
"""
print("IF ELIF ELSE STATEMENT")
a=5
b=5
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")
else:
    print("b is greater than a")


"""
NESTED IF --> IF STATEMENT INSIDE IF STATEMENTS 
"""
print("NESTED LOOP")
x=30
if x>10:
    print("Above ten")
    if x<50:
        print("and below 50")
    else:
        print("not below 50")


#check if the given num is three digit even number

num=int(input("enter the number: "))
if 99 < num < 1000:
    if num%2==0:
        print(num," is the three digit even number")
    else:
        print(num," is the three digit odd number")
else:
    print("enter three digit number")





