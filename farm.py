#!/usr/bin/env python3

"""ALTA3 | EGranillo | Farmloop challenge"""

# list and dict of farms and animals

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

ne_farm = farms[0]["agriculture"]
w_farm = farms[0]["agriculture"]
se_farm = farms[0]["agriculture"]

def main():
    # return the animals in NE farm
    print("These are the animals in the NE farm: \n")
    for x in ne_farm:
        print(x, end=" ",)

    # allows user input of farms and prints items in farm
    print("\n", "These are the farms to choose from")
    for farm in farms:
        print("\n", farm["name"])

    pick = input("I choose farm: \n")

    if pick.lower() == "NE farm":
        print(*ne_farm)
        
    elif pick.lower() == "W farm":
        print(*w_farm)

    else:
        print(*se_farm)

    

main()
