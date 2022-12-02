#!/usr/bin/python3

#defining a function
def age_cal(name, yob, current_year): #parameters [place holders]
    age = current_year - yob
    print(f"{name}, you are {age} years old")

#calling the function
age_cal("Haruna Zakaria", 1999, 2022) # argument [values]
age_cal("Haruna Dawuda", 1992, 2022)
age_cal("Haruna Hamis", 1995, 2022)
age_cal("Haruna Sualehu", 2005, 2022)