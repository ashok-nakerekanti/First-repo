#by default values are assigned as strings in python
A="ashok goud"
print(A)
a=1
b=2
print(a+b)
#to convert every string into uppercase letter
r='''to write multiple line strings
like this'''
print(r)
J= input("enter the string :")
print(J)
#string slicing
j="akgoud,32"
y=j[2:6]
print(y)
#to get characters from starting position to 6(not included 6th character)
print(j[:6])
#to get  characters from 2nd position to end position
print(j[2:])
#negative indexing
print(j[-6:-2])
#modifying strings.....
print(j.upper())
#to remove white space in string
print(J.strip())
#to replace the string
print(J.replace("a","h"))
#to separate two strings
print(j.split(","))  