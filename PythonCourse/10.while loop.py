#WHILE LOOP --> execute a set of statements as long as a condition is true
# remember to increment the variable used in the condition, or else loop become infinite
number =1
while number<=10:
    print(number)
    number+=1


alpha = " "
while not alpha.isalpha():
    alpha=input ("enter an alphabet: ")
print("you have entered "+ alpha)

x=10
while x>0:
    print(x)
    x=x-1
print(x)