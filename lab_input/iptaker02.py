#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # Collect string input form the user

    user_input = input("Please enter an IPv4 IP address:")

    ## the line below creates a single string that is passed to print()

    # print("You told me to the IPv4 address is: " + user_input)


    ## print() can be give a sereies of objects separated by a comma

    print("You told me the IPv4 address is:", user_input)


    # asking user for 'vendor name'

    vendor = input("Please input the vendor name:")
    print(vendor)


main()

