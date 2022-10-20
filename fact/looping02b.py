#!/usr/bin/env python3

"""ALTA3 | EGranillo | Looping across a file opened with 'with'"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # creat list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="")
# not need to close our file - closed automatically
