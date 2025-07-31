"""a function is a block of code that performs specific task whenever it is called.In bigger programs ,where we have large amounts of code ,it is advisable to create or use existing functions that make the program flow organised and neat
we have two type of function 
1.built in functions
2.user defined functions"""
def calculategmean(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)
def isgreater(a,b):
    if(a>b):
        print("a number is greater")
    else:
        print("b number is greater")
a=8
b=9
print(a,b)

isgreater(a,b)

calculategmean(a,b)

c=32
d=12
print(c,d)
isgreater(c,d)

calculategmean(c,d)
#function have multiple argument types
#return statement
print("lets have a look on return function in python")
def average(*numbers):
    for i in numbers:
        sum=0
        sum =sum+i
#         return 9
#function only returns the first return  statement

        return sum/len(numbers)
c=average(5,6,4,3)
print(c)
#recursive functions
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        fact = n*factorial(n-1)
        return fact
n=int(input("enter the number:"))
print("factorial is :" , factorial(n))