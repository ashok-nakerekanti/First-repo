#joining of sets
#union joins two sets and returns new set
s1={"a","b","c"}
s2={1,2,3,"a"}
s3=s1.union(s2)#here we can use | in lace of union
print(s3)
#update method one set into another set
s1.update(s2)
print(s1)
#intersection method returns values that are present in both sets
s4=s1.intersection(s2)#we can use  & operator in place of intersection
print(s4)
#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

#.intersection_update(set2)

print(set1)
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set3 = set1.difference(set2)

print(set3)

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1.difference_update(set2)
print(set1)