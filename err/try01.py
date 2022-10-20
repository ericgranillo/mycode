#!/usr/bin/env python3

"""ALTA3 | EGranillo | Try and except logic"""

# Start with an infinite loop

while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again...")
