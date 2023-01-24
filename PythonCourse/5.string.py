"""
string are iterable
immutable
indexing and slicing
positive indexing and negative indexing
inbulit methods or functions

"""
#string concatenation
message="hello "
name='logesh'
final=message+name
print(final)
print(final*2)

#method
print(final.upper())
print(name.capitalize())
print(name.find("g"))  #invoking a method
print(message.upper())
print(final.title())
print(len(message))
print(len(final))
print("hello \t world")#escape sequence


#string slicing
#string_name[start: stop: jump]

str="welcome to python programming"
print(str)
print(str[5:15])
print(str[10])
print(str[: :-1])# reverse the string


#strings are iterable

for i in str:
    print(i)
for x in range(len(str)):
    print(x,str[x])


# some build-in methods in string

print("capitalise the first letter in entire string: ",str.capitalize())

print("capitalise the first letter in each word: ",str.title())

print("print all letter in upper case: ",str.upper())

print("print all letter in lower case: ",str.lower())

print("count the number of o in string: ",str.count("o"))

print("check that the string ends with g: ",str.endswith("g"))

print("check that the string ends with o: ",str.endswith("o"))

print("check that the string starts with o: ",str.startswith("w"))

print("find the index value of first occurance of t: ",str.find("t"))#find gives the  index value of first occurance of substring

print("find the index value of first occurance  of o: ",str.find("o"))

print("find the index value of last occurance of o: ",str.rfind("o"))#rfind gives the index value of last occurance of substring

print("find the index value of last occurance of p: ",str.index("p"))

print("find the index value of last occurance of p: ",str.rindex("p"))

print("check the entire string is lower: ",str.islower())

print("check the entire string is upper: ",str.isupper())

print("check the first letter of each word is capital: ",str.istitle())

print("print the maximum of string: ",max(str))

print("print the minimum of string: ",min(str))#give space because space is the minimum value

print("convert upper to lower and lower to upper: ",str.swapcase())

print("length of this string is: ",len(str))


#string concatenation

fname="Logeshwari"
lname="Saravanan"
name=fname+" "+lname
print(name)

#format string -->To combine string and numbers we have to use format() method

age=22
detail="{} is {} years old"
print(detail.format(name,age))
