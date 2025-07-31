# def is_sorted(lst):
#     l=len(lst)
#     for i in range(l+1):
#         if lst[i]<lst[i+1]:
#             return True
#         else:
#             return False
         
# lst =[1,3,4,7,6]
# print(is_sorted(lst))
# Function to invert dictionary
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted

# Read dictionary from user
user_dict = {}
n = int(input("How many key-value pairs? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

# Invert the dictionary
inverted = invert_dict(user_dict)

# Show results
print("Original dictionary:", user_dict)
print("Inverted dictionary:", inverted)


