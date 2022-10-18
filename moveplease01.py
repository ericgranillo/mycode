#!/usr/bin/env python3

import shutil   # shell utility to used to move files

import os # provide access to low level os operations

def main():
    
    os.chdir("/home/student/mycode/") # move into this working directory

    shutil.move("raynor.obj", "ceph_storage/") # try moving the file raynor.obj into ceph_storage/ dir

    xname= input("what is the new name for kerrigan.obj?") # collect input from the user

    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname) # moving kerrigan.obj into ceph_storage with new name

main() # this calls our main fuction


