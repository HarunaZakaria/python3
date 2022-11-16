#!/usr/bin/python3
# this is a car game program using while loop

command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("car started ...")
    elif command == ("stop"):
        print("car stop ...")
    elif command == "help":
        print("""
start ...... to start the car
stop ....... to stop the car
quit ....... to quit

        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't Understand")
