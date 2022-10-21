#!/usr/bin/env python3

"""doctstring"""

# create file object in read mode
configfile = open("vlanconfig.cfg", "r")

# display file to the screen - .read()

print(configfile.read())

# close file

configfile.close()

# recreae file object to explory new method
configfile = open("vlanconfig.cfg", "r")

# make a list of file lines - .readlines()

configlist = configfile.readlines()
print(configlist)

# iterate through configlist

for x in configlist:
   # print(x, end=" ")
    print(x.strip())

# always close your file

configfile.close()
