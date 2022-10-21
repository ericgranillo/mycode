#!/usr/bin/env python3

"""ALTA3 | EGranillo | Read Dracula"""

vampire = 0

def main():
    # open dracula text and read
    with open("dracula.txt", "r") as foo:
        # loop through the text and print only vampire
        for line in foo:
            if "vampire" in line.lower():
                print(line)
        
               
#        vampire = 0
#        for line in foo:
#            if "vampire" in line.lower():
#                vampire += 1
#               print("In the previous text the word vampire appeared ", vampire, " time!")
                                

main()


