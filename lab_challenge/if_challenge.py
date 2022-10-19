#!/usr/bin/env python3
"""ALTA3 Labs | EGranillo | if/elif/else Challlenge"""

def main():
    # define seasons
    #Season= [ "Spring", "Summer", "Fall", "Winter"]
    
    # define Cities
    spring_cities= ["Miami,", "Cancun,", "Honolulu,","Milan"]
    summer_cities= ["Florence,", "Ibiza,", "Paris,", "Copenhagen"]
    fall_cities= ["Tokyo,", "Buenos Aires,", "Cabo San Lucas,", "Chiang Mai"]
    winter_cities= ["Lima,", "Sydney,", "Bali,", "Fiji"]

    # welcome user to virtual travel advisor

    print("Welcome to your virtual travel advisor! \n")

    # ask user which season to travel

    season_input= input("What season are you thingking of traveling in? \n -> ")
    
    # if statements to determine which city to travel by seasons 

    if season_input.lower() == "spring":
        print("Ready for a spring vacation, me too! Pick from one of these wonderful cities:\n") # prompt for choosing cities
        print(*spring_cities, " \n") # list cities to visit
        input("This vacation im going to:\n -> ") # user input of city
        print("All set, now book your trip on your favorite rocket ship!") # close out statement

    elif season_input.lower() == "summer":
        print("Time to take a break! Pick one of these wonderful cities to post on your gram:\n")
        print(*summer_cities, " \n")
        input("This summer vacation im going to:\n -> ") 
        print("All set, now leave the kids at home with their grandparents and soak up the sun!")

    elif season_input.lower() == "fall":
        print("Sounds like you need a vacation for your vacation. Pick from one of these beautiful cities to show everyone how cultured you are: \n") 
        print(*fall_cities, "\n") 
        input("This fall vacation im going to \n -> ") 
        print("Great choice! Try not to get lost while you're there!") 
   
    elif season_input.lower() == "winter":
        print("Looks like the weather outside is frightful, but a winter vacation sounds delightful! Pick from one of these wonderlands: \n") 
        print(*winter_cities, "\n") 
        input("This winter vacation im going to \n -> ") 
        print("Great choice! Now take me with you its cold in this virtual box!") 

    else: # if user input is not one of the choices throw this error
        print("Looks like you entered gibberish or nothing. Be prepared to be sucked into the magical land of Narnia!")
         
if __name__ == "__main__":
    main()
