#!/usr/bin/env python3


def main():

    # lists

    challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
    
    # create variables

    a= challenge[2][1]
    b= challenge[2][0]
    c= challenge[3]
    

    # print out "My eyes! The goggles do nothing!

    print(f"My {a}! The {b} do {c}!")
    
    # trials challenge

    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    
    # create new variable

    a= trial[2]["goggles"]
    b= trial[2]["eyes"]
    c= trial[-1]
    
    # print out "My eyes! The goggles do nothing!"

    print(f"My {a}! The {b} do {c}!")

    # nightmare challenge

    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    # create new variables

    a= nightmare[0]["user"]["name"]["first"]
    b= nightmare[0]["kumquat"]
    c= nightmare[0]["d"]

    # print out "My eyes! The goggles do nothing!"

    print(f"My {a}! The {b} do {c}!")

main()
