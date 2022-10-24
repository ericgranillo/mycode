#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    resp = requests.get(f"{API}sets")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    print( resp.json() )

if __name__ == "__main__":
    main()
