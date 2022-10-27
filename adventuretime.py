#!/usr/bin/env python3
"""TLG Learning| EGranillo |  Adventure time:
    Let's go on a trip you'll never remember"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    Murder House an RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    print('Weapons:', weapon)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    # check if there's a weapon in the room, then print
    if "weapon" in rooms[currentRoom]:
        print('You see a ' +rooms[currentRoom]['weapon'])
    print("---------------------------")


# an item and weapon inventory, which is initially empty
inventory = []

weapon = []

# a dictionary linking a room to other rooms
rooms = {

        'Front Garden' : {
            'north' : 'Front Entrance',
            'west'  : 'West Garden',
            'east'  : 'East Garden'
            },

        'West Garden' : {
            'west' : 'Shed',
            'east' : 'Front Garden'
            },

        'East Garden' : {
            'west' : 'Front Garden',
            'item' : 'Potion'
            },

        'Front Entrance' : {
            'north' : 'Hall',
            'west'  : 'Entertainment Room',
            'south' : 'Front Garden',
            'east'  : 'Office',
            'item'  : 'Key'
            },

        'Hall' : {
            'north' : 'Dining Room',
            'west'  : 'Entertainment Room',
            'south' : 'Front Entrance',
            'east'  : 'Theater Room',
            'weapon': 'Hockey Stick'
            },

        'Dining Room' : {
            'north' : 'Backyard',
            'west'  : 'Kitchen',
            'south' : 'Hall',
            'east'  : 'Living Room',
            'weapon': 'Knife'
            },

        'Entertainment Room' : {
            'north' : 'Kitchen',
            'east'  : 'Hall',
            'item'  : 'Shadow Monster'
            },

        'office' : {
            'west'  : 'Front Entrance',
            'item'  : 'Skeleton King'
            },

        'Kitchen' : {
            'south' : 'Entertainment Room',
            'east'  : 'Dining Room',
            'item'  : 'Shrooms'
            },
        
        'Theater Room' : {
            'east' : 'Hall',
            'item' : 'Killer Klown'
            },

        'Living Room' : {
            'west' : 'Dining Room',
            'south': 'Garage',
            'item' : 'The Blob'
            },

        'Garage' : {
            'north' : 'Living Room',
            'item'  : 'Rope'
            },

        'Backyard' : {
            'item' : 'Death Dealer'
             },

        'Shed' : {
            'east'  : 'West Garden',
            'weapon': 'chainsaw'
            }

         }

# start the player in the Hall
currentRoom = 'Front Garden'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' added!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # add weapon to inventory
        if "weapon" in rooms[currentRoom] and move[1] in rooms[currentRoom]['weapon']:
            weapon.append(move[1])
            print(move[1] + ' added!')
            del rooms[currentRoom]['weapon']
        # if there's no item in the room or the item or weapon doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

        ## If a player enters a room with a monster but has chainsaw kill monster
    if 'item' in rooms[currentRoom] and 'Shadow Monster' in rooms[currentRoom]['item']:
        if 'chainsaw' in weapon:
            del rooms[currentRoom]['item']
            print('''Chop em up and cut em down, we are going old
           school Doom on this monster. Not putting its hands
            on my cookie.''')
        else:
            print('A monster has got you... GAME OVER!')
            break

        ## Define how a player was tricked and lose the gamen
    if currentRoom == 'Backyard' and 'Potion' in inventory and 'Shrooms' in inventory and 'Rope' in inventory and 'Knife' in weapon:
        print('''You have come to your senses, you murdered the entire
               family... You have the tools to end it all...''')
        break
