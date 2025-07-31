'''sets are used store multiple items in a single varaiable
A set is a collection of which is unordered,unchangeble,and unindexed'''
myset={"ashok","dinesh","surya"}
print(myset)
#in sets duplicates are not allowed
set_1={1,2,3,1,3,2}
print(set_1)
##in sets True and 1 and False and 0 are considered as ssame and treated as duplicates
set_2={32,43,True,1}
print(set_2)
print(type(set_2))
##using set constructor we can make a set
set3=set(("ash","cash","ash"))
print(set3)
##we cannot access items ina set by referring to an index or a key as these are unindexed
#we can access through for loop 
for i in set_2:
    print(i)
##to check wheter the item is present is set or not
print(32 in set_2)
##to add one item to the set ,using index add() 
set3.add(3)
print(set3)
#to add items from another set,tuple and list we use update()
set_1.update(set_2)
print(set_1)
#to remove set items we use remove() or discard()
set3.remove("cash")
print(set3)
#clear empties the set
set3.clear()
print(set3)
#del keyword will delete the set permanently
