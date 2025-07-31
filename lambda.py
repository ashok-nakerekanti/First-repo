"""a lambda function  is A small anonymous function
A lambds function can take any number of arguments  ,but can only have one expression"""
x=lambda a : a+10
print(x(5))
y=lambda c,b : c*b
print(y(5,6))
#lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)


