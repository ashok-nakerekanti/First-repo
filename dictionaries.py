"""dictionaries are used to store values in key:value parts
A dictionary is a collection which is ordered*,changeable and do not allow duplicates."""
dict = {
    "name":"ashok",
    "DOB":"march",
    "gender":"male",
    "DOB":"june"
}
print(dict)
print(type(dict))
#dictionaries cannot have two items with same key and duplicate values will overwrite existing value
print(dict['DOB'])
THISDICT={
    "brand":"ford",
    "automatic":False,
    "year":2009,
    "colours":["red","white","green"]

}
print(THISDICT)
#the keys method will return a lists of all keys in the dictionary
x=THISDICT.keys()
print(x)
THISDICT["price"]=123446
print(x)
#The values() method returns a list of all tthe values in the dictionary.
y=THISDICT.values()
print(y)
#get items()method will return each item in a dictionary ,as tuples in a list.
z=THISDICT.items()
print(z)
print("\n")
THISDICT["model"]="red"
THISDICT.update({"year":2018})
print(THISDICT)
#pop() method rermoves the item wih the specified key name
#popitem method removes the last inserted item in the dictionary
THISDICT.pop("model")
print("\n")
print(THISDICT)
#del keyword removes the item with then specified key name
#del keyword can delete all the dictionary permanently
#clear() method empties the dictionary
"""loopsthrough the dictionaries"""
for x in THISDICT:
    print(x)#returns keys one by one
    print(THISDICT[x])
#LOOP THROUGH BOTH KEYS AND VALUES
for x,y in THISDICT.items():
    print(x,y)
"""to copy dictionaries from one variable to another"""
mydict=THISDICT.copy() # or mydict=dict(THISDICT)
print(mydict)
#NESTED DICTIONARIES
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
'''if we want add three dictionaries into a neew dictionary
simply we create 3 dictionaries and and the other dictionary will contain these 3 dictionaries '''
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
#to access the items from nested loops
print(myfamily["child2"]["name"])
#loop thrpugh nested dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

