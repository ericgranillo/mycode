#!/usr/bin/env python3

"""Alta3 | EGranillo | Working with for loops"""

def main():

    # create the list called vendors
    vendors = ["ciscos", "juniper", "big_ip", "f5", "arista"]
    # loop across the list vendors
    for x in vendors:
        print("The vendor is: " + x) # each time through the loop print value of x
    print("/nOur loop had ended.") # when the loop ends print this

main()
