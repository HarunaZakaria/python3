#!/usr/bin/python3
"""login authentication"""

usrname = "haruna"
password = "harun"

print("Welcome to my app")
usrname_username = input("username: ").lower()
user_password = input("password: ")

if (usrname_username == usrname and user_password == password):
    print("you have successfully logged in")
elif (usrname_username == usrname):
    print("incorrect password")

else:
    print("incorrect username or password,try gain")