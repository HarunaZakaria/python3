#!/usr/bin/python3

#defining a function
def age_cal(name, yob, current_year): # place holders
    age = current_year - yob
    print(f"{name}, you are {age} years old")

#calling the function
age_cal("Haruna Zakaria", 1999, 2022) # values
age_cal("Haruna Dawuda", 1992, 2022)
age_cal("Haruna Hamis", 1995, 2022)