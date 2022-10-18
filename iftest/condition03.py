#!/usr/bin/env python3

hostname = input("What value should we set for hostname?\n")

## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

elif hostname.lower() == "cowboys": # if hostname isn't mtg, and its cowboy run the following
    print("We dont like you cowgirls around these parts!") # if hostname is bear print out following
    print("Go on get!")
    
else: # if either hostnames were not found, run the following
    print("That hostname was not found")
    print("hostname does not match expected config")

## always print out to the user

print("Exiting the script")

