#!/usr/bin/python3
'''calculate BMI'''

def cal_BMI(weight, height):
    bmi = weight // (height * height)
    print(f"your BMI is {bmi}")

cal_BMI(60, 1.9)