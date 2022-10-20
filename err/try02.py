#!/usr/bin/env python3

"""ALTA 3 | EGranillo | Try except and else"""

# start with an infinite loop

while True:
    try:
        print("Lets divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y?"))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)

    # general erro handling
    # a pratical use might be exceptions we haven't designed a solution for yet
    
    except Exception as err:
        # sys.exc_info returns a 3 tuple with into about the exception handled
        print("We did not anticipate that:", err)
