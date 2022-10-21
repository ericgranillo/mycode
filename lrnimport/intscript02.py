#!/usr/bin/env python3

"""Alta 3 | EGranillo | Import subprocess"""

import subprocess

subprocess.call(["ip", "link", "show", "up"])

print("This program will check your interfacec.")

interface = input("Enter an interface, like, ens3: ")

subprocess.call(["ip", "addr", "show", "dev", interface])

subprocess.call(["ip", "route", "show", "dev", interface])
