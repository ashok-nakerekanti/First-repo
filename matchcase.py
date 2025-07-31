'''instead of writing many if else statements we can use match statement'''
day=int(input("enter the day:"))
match day:
  case 1|2|3|4|5:
    print("its a working day")
  
  case 6|7:
    print("its a weekend")
  
  case _:
    print("week lo undevi 7 days ra labbe")

