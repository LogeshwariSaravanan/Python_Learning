"""
iterating statements or looping statements
loop --> repeat a set of code
looping over the statement untill it becomes false

types of looping statement --> for loop, while loop

"""

#for --> we know the count(predefined count)

for i in range(10):
    print(i)

#looping through a string

name=input("enter the name: ")
for i in name:
    print(i)

#NESTED LOOP --> LOOP INSIDE A LOOP
#INNER LOOP will be executed one time for each iteration of OUTER LOOP

for x in range(1,6):
    for y in range(x):
        print("*",end=" ")
    print()