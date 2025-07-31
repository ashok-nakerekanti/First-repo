a=33
b=33
if a>b:
     print("a is greater")
elif b>a:
     print("b is greater")
else  :
    print("both are equal")
#short hand if else statements
print("a is the shorter") if a<b else print("b is shorter")
print("A") if a>b else print("=") if a == b else print("no condition is true")
#using logical operators
c=1
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
     print("b is greater ")  
else:
     print("c is greater")
if a>b or a>c:
     print("atlest one of the condition is true")
#nested if statements
x=35
if x>10:
    print("x is greater than 10")
    if x>20:
        print("x is also greater than 29")
    else:
        print("x is not greater than 20")
    