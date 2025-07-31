# def inverted(d):
#     inverted={}
#     for key,value in d.items():
#         inverted[value]=key
#     return inverted

# n=int(input("enter the number of key value pairs:"))
# user_dict={}
# for i in range(n):
#     key=input("enter the key:")
#     value=input("enter the value:")
#     user_dict[key]=value
# user_dict[key]=value

# invert=inverted(user_dict)
# print("original dictionary:",user_dict)
# print("inverted dictionary:",invert)


# def capitize(word):
#     result=""
#     new_word=True
#     for char in word:
#         if char==" ":
#             result+=char
#             new_word=True
#         else:
#             if new_word:
#                 if 'a' <= char <='z' :
#                     result+=chr(ord(char)-32)
#                 else:
#                     result+=char
#                 new_word=False
#             else:
#                 if 'A' <= char <='Z' :
#                     result+=chr(ord(char)+32)
#                 else:
#                     result+=char
#     return result
# word="hello my dear wOrld"
# capitize(word)
# print(capitize(word))
def generate_binary_strings(n, prefix=""):
    if n == 0:
        print(prefix)
        return
    generate_binary_strings(n - 1, prefix + "0")
    generate_binary_strings(n - 1, prefix + "1")

# Example usage:
generate_binary_strings(3)
