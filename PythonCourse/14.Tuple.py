"""
tuple  -->almost similar to list
ordered set elements(index value)
tuple-()
immutable that means we can access the values but we can not modify the values
Accessing --> indexing and slicing

tuples can contain list inside them
"""
tup=(1,2,5,"dog")
print(tup)
print(tup[1])
print("index value of dog is",tup.index("dog"))

print("length of tuple is",len(tup))
print(dir(tuple))

#NESTED TUPLE -->tuple inside the tuple
tup1=((1,2),("dog","cat","rat"),("name",5))
print("nested tuple ",tup1)
print(tup1[2][1])

tup3= ([1,2,3], ['a', 'b', 'c'])
tup3[0][2]=5 #tuple is immutable but here we have list inside the tuple so that we can change the list value
print(tup3)

#list is mutable so that list in the tuple can be changed
