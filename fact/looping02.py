#!/usr/bin/env python3

"""Alta3 | EGranilo | Using files as a source for the for-loop"""

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create a list of lines

dnslist = dnsfile.readlines()

# loop over lines

for svr in dnslist:
    # print and end without a new line
    print(svr, end=" ") # the line we read ALREADY contain a \n (newline)

# close the file (we created the list of lines)
dnsfile.close() # best practice to close your file
