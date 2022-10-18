#!/usr/bin/env python3

"""ALTA3 | EGranillo | more conditionals"""

# prompt user to input an ip address
ipchk= input("Apply an IP address: ")

# if user set IP of gateway
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the gateway was set: " + ipchk + " This is not recommended.")

elif ipchk: # if any data is provided, this will test true
    print("Looks like the IP address was set: " + ipchk)

else: # if data is not provided
    print("You did not provide input.")

