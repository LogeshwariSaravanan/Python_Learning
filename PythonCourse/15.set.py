"""
set
unordered
mutable
unique elements(no duplicate elements
"""

#SET OPERATIONS

s={1,2,3}
t={1,2,3,4,5,6,7}
print(s)
print(t)
s.add(6)
print("6 is added in the set s :",s)
s.update(t)
print("set t is updated in set s: ",s)
print("print the length of s",len(s))
s.remove(6)#if element not found it will return key error
print("6 is removed from set s by using remove(): ",s)
s.discard(6)#if element not found error will not be raised
print("6 is removed from set s by using remove(): ",s)
s.pop()# this remove the first element of the SET
print("this removes the first element of the set: ",s)
s.clear()#this clear all the element in the SET
print("this clear the entire set and return empty set",s)
print("print maximun of the set t: ",max(t))
print("print minimun of the set t: ",min(t))
print("print sum of all the elements of the set t: ",sum(t))


a={1,2,3}
b={1,2,3,4,5,6}
#issubset
print("this check that all the element present in a is also present in b: ",a.issubset(b))#a<=b
print("this check that all the element present in b is also present in a: ",b.issubset(a))

#issuperset
print("this check that every element of b must be present in set a: ",a.issuperset(b))#a>=b
print("this check that every element of a must be present in set b: ",b.issuperset(a))


#UNION --> a new set will be created with all the elements of a and b without duplication
print("a new set will be created with all the elements of a and b without duplication: ",a.union(b))#a|b

#INTERSECTION -->elements which are availabe in both a and b sets
print("elements which are availabe in both a and b sets: ",a.intersection(b))#a&b

#difference --> remove the common elements print remaining elements of one set
print("all the elements of a except the common element will be printed: ",a.difference(b))#a-b
print("all the elements of b except the common element will be printed: ",b.difference(a))#b-a

#SYMMETRIC DIFFERENCE -->all the elements of both the set except the common elements
print("all the elements of both the set except the common elements: ",a.symmetric_difference(t))

#sort
x={4,8,3,9,6}
print("sort of set s is: ",sorted(x))


#miscellaneous
string= '65'.join(list(set('missippi')))
print(string)
