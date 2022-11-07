#check if user name is >= 5 and <= 25
name = input("Please what is your name: ")
if len(name) < 5:
    print("your name is too short")
elif len(name) <= 25:
    print("you have a nice name")
else:
    print("your name is too long")