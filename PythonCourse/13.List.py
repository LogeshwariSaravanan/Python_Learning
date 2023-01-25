#LIST
"""
list are used to multiple item in a single variable
list is one of the 4 build in datatypes in python used to store collection of data
the other 3 are Tuple, Set, Dictionary

list -->[]
list items are ordered, changeable and allow duplicate values.
list is mutable
iterable
indexing and slicing
"""

cities=["erode","chennai","coimbatore","trichy","salem","karur"]
print(cities)
for i in cities:
  print(i)
val=[7,5,9,3,4,8]
print(val)
list1=["chennai",5,"erode"]
print(list1)

list2=cities+val+list1
print(list2)
print(list2.count(5))

#GETTING LIST ITEM FROM USER
lst =[]
for i in range (5):
  ele = input ("enter the list item ")
  lst.append (ele)
print (lst)


lst1 = list (map (int, input ().split ()))
print (lst1)

#ACCESSING LIST WITH INDEXING
print("first city in cities list is ",cities[0])
print("second value in val list is ",val[1])


#MODIFY LIST ITEMS
cities[3]="tiruppur"
print("modify the fourth city trichy into tiruppur ", cities)
val[5]="six"
print("modify the sixth value 8 into six ",val)

#APPEND -->add list item in the last
cities.append("trichy")
print("here trichy is append in the cities list ",cities)

#INSERT
cities.insert(2,"tanjor")
print("tanjor is insserted in 2nd index ",cities)

#REMOVE USING DEL
del cities[2]
print("2nd index value tanjor is deleted ",cities)


#REMOVE USING POP() -->removes last value of the list
cities.pop()
print("pop() removes the last list item ",cities)

#REMOVE BY VALUE
cities.remove("salem")
print("this removes karur in this list ",cities)

#TEMPERORY SORT
print("this print temporary sorted cities list",sorted(cities))


#PERMANENT SORT
cities.sort()
print("permanently sorted cities list ",cities)

#REVERSE
cities.reverse()
print("reverse the cities list ",cities)

#LENGTH OF LIST
print("length of cities list ",len(cities))
print("length of val list ",len(val))

#INDEX VALUE OF LIST ITEM
print("index value of erode is ",cities.index("erode"))

print(dir(list))