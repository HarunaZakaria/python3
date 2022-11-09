#!/usr/bin/python3
#give directions base on traffic light

light = input("what is the color of the light now: ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get ready to go")
elif light == "green":
    print("Go")
else:
    print("you have enterdd a wrong color")