# import numpy as np

# #to print all the prime numbers in range of k
# k= int(input("enter the number:"))
# count=0
# if k<=1:
#     print("itself is the primenumber")
# elif k<0:
#     print("enter the positive number")
# for i in range(2,k+1):
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             is_prime=False
#     if is_prime:
#         print(i)

# lst_1=[1,2,3,4,5]
# arr_1=np.array(lst_1)
# lst_2=[3,2,1,8,9,10]
# arr_2=np.array(lst_2)
# common=[]
# for i in arr_1:
#     for j in arr_2:
#         if i==j and i not in common:
#             common.append(i)
# print(common)
 #gcd of two numbers
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# print(gcd(a,b))
# Read words from file
with open("Hello.py", "r") as file:
    words = [line.strip() for line in file]

# Add missing single-letter words
words.append("I")
words.append("a")
words.append("")  # optional, if you need empty string

# Remove duplicates
words = list(set(words))

# Show the result
print("Words list updated!")
print(words)
