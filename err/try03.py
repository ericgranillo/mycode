#!/usr/bin/env python3

"""ALTA 3 | EGranillo | Try and except and else"""

# start with an infinite loop
while True:
    try:
        print("\nLet's divide x by y!")
        x = int(input("what is the integer value of x? "))
        y = int(input("what is the integer vulue of y? "))
        print("The vlue of x/y: ", x/y)
    except ZeroDivisionError as err:
        print("Handling run-time error:", err)
    except ValueError as err:
        print("That was not a legal value for division:", err)

    # general error handling
    # a practiccal use might be exceptions we havent desigened a solution for yet
    except Exception as err:
        # sys.exc_infor returns a 3 tuple with into about the exception handled
        print("We did not anticipate that:", err)

        # raise by itself simply calls the previouis exception that was thrown
        raise
    # else ONLY runs if there wasnt any errors
    else:
        print("\nThanks for learning to handle errors!")
        break
