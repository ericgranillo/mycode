#!/usr/bin/env python 3


"""Alta3 | Lists"""

def main():

wordbank= ["indentation", "spaces"]

# student list

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

# append interger 4 to list
wordbank.append(4)
print(wordbank)
# input from 0-18

#num=int(input("Pick a number from 1 and 18."))

#slicing one of the elements from tlgstudents
chosen_one= int(input("Pick a number from 1 and 18."))
        
student_name= tlgstudents[chosen_one]

print("f{student_name},always uses,{wordbank[2]} {wordbank[1]} to indent.")

main()
