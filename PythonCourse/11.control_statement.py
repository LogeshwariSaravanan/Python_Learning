"""
control statemnts -->break, continue, pass

break --> exit the loop
continue --> only exit the current loop
pass --> nothing

EOF -->END OF FILE
pass is used to remove end of file
"""

#BREAK after print statement
print("BREAK")
for i in range(10):
    print(i)
    if i>=7:
        break


# break before print stattement
print("break before print statement")
for x in range(10):
    if x >= 7:
        break
    print(x)


#CONTINUE after print statement
print("CONTINUE example 1")
for i in range(10):
    print(i)
    if i==7:
        continue

#continue before print statement
print("continue before print statement example 2")
for i in range(11):
    if i==7 or i==9:
        continue
    print(i)

print("continue example 3")
for i in range(10):
    if i%2==0:
        continue
    print(i)

