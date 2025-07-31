tup=(1,3,2,"green",True)
print(type(tup),tup)
##tuples are not changable as We can change in lists
#it gives error
# tup[0]=34
# print(tup)
print(len(tup))
print(tup[0])
print(tup[-1])
if 3 in tup:
    print("yes 3 is in the tup")
##we can update tuples by changing into lists and then converting into tuples again
x=(1,3,4,5,6)
y=list(x)
y[1]=32
y.remove(5)
y.append(True)
x=tuple(y)
print(x)
z=("ashok",)
x+=z
print(x)
#to delete tuple completely
## del x (the tuple will be deleted)
#packing meant by creating tuple and assining values to it
#unpacking meant by extracting values back into variables
names=("leaf","blood","banana")

(green,red,yellow)=names
print(green)
print(red)
print(yellow)
#*(asteristic) at the before of the variable name is used to assign all the values to one variable
(red,*fruits)=names
print(red)
print(fruits)
#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#loops throughn the tuples
for i in fruits:
    print(i)
print("\n")
for j in range(len(fruits)):
    print(fruits[j])
#joining of tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
mytuple=tuple3*2
print(mytuple)
#tuple built in functions
print(fruits.count("apple"))
print(fruits.index("apple"))