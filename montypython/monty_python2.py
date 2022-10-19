#!/usr/bin/env python3
"""Alta# | EGranillo | while loops"""

rounds = 0


while True:
    rounds = rounds + 1
    print("Finish the movie titile, 'Monty Python\'s The LIfe of _____'")
    answer = input("your guess --> ")

    if answer == 'Brian':
        print('Correct')
        break
    elif rounds == 3:
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry! Try again!')

