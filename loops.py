# the syntax for loops in python are different from taht of c
for i in range(6):
#break statements
    if i==4:
        break
#continue statements in loops
    
    if i==2:
        continue
    print(i)
#loops with lists
x=["ashok","dinesh","poojitha","surya","samnv"]
for i in x:
    print(i)
    for j in i:
         print(j)
#using range in loops
for i in range(12):
    print(i)
print("next loop")
for i in range(0,6):
    print(i)
print("next loop")
for i in range(0,30,2):
    print(i)
else:
    print("finally finished")
