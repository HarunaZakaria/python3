#check if sosmeone is retired or not
age = int(input("please what is your age: "))
if (age < 60):
    print("You are still a worker")
elif (age == 60):
    print("you should retired now")
elif (age > 60):
    print("you must have retired long time")
else:
    print("There was aproblem with your age")