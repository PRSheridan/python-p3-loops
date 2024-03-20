#!/usr/bin/env python3

def happy_new_year():
    for index in range(10):
        print(10-index)
    print("Happy New Year!")

def square_integers(int_list):
    return [(val * val) for val in int_list]

def fizzbuzz():
    for index in range(1, 101):
        if ((index % 3 == 0) and (index % 5 == 0)):
            print("FizzBuzz")
        elif (index % 3 == 0):
            print("Fizz")
        elif (index % 5 == 0):
            print("Buzz")
        else:
            print(index)