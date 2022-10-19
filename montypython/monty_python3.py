#!/usr/bin/env python3

"""Alta3 | EGranillo | Conditional with while loops"""

rounds = 0

answer = " "

while rounds < 3 and answer != "Brian":
    rounds += 1  # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s the life of _____": ')
    answer = answer.capitalize()

    if answer == "Brian": # logins to check if user gave correc answer
        print("Correct!")
    elif answer == "Shrubbery":
        print("You gave the super secret answer!")
    elif round == 3: # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:   # is answer was wrong
        print("Sorry. Try again!")

