#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    #create resp, which is our request object
    resp = requests.get(f"{API}sets")  # this 'f' string reads : API + "sets"

    # display the methods available to our new object
    print( dir(resp) )

if __name__ == "__main__":
    main()
