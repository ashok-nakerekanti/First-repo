'''>lists are collection of data items
   >they store multiple items in a single variable
   >list items are seeparated by commas and enclosed within square brackets
   >lists are changable means we can use them after creation'''
list=[2,"ashok",3.5,True,"india",6,9]
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
##negative indexing
print(list[-1])
print(list[-2])
##to convert into positive indexing
print(list[len(list)-3]) 
marks=[2,3,4]
print(marks)
print(type(marks))
#one list can have different data types
if "ashok" in list:
    print("yes it is in the list")
else:
    print("it is not in the list")
print(list[0:3])
print(list[1:-1])
print(list[1:8:2])
lst=[i+3 for i in range(16)]
print(lst)
lst=[i*i for i in range(16) if i%2==0]
print(lst)
#to insert in the list
print(list)
list.insert(2,"cool")
print(list)
