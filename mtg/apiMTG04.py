#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    # create resp which is our request object
    resp = requests.get(f"{API}sets")

    print( resp.json().keys() )

if __name__ == "__main__":
    main()
