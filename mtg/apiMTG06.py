#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    resp = requests.get(f"{API}sets")

    cardsets = resp.json().get("sets")

    # open a file we write our data into
    with open("mtgsets.index", "w") as mtgfile:
        for cardset in cardsets: # loop across all the of the sets of the MTG cards
            print(f"{cardset.get('name')} -- {cardset.get('code')}", file=mtgfile)

if __name__ == "__main__":
    main()
