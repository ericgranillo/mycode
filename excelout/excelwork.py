#!/usr/bin/env python3

import pyexcel

def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is he driver asssociated with this device? ")
    d = {"IP": input_ip, "driver": input_driver}
    return d


def main():
    mylistdict = []
    print("Hello! This porgram will make you a *.xls file")

    while True:
        mylistdict.append(get_ip_data())
        keep_going = input("\nWould you like to add another value? Enter to conitnue, or type 'q' to quit: ")
        if (keep_going.lower() == 'q'):
            break
    filename = input("\What is the name of the *.xls file? ")

    pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

    print("The file " + filename + ".xls should be in your local directory")

main()
