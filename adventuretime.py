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
      Go [direction]
      Get [item/weapon]
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
    if "Item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['Item'])
    print("---------------------------")
    # check if there's a weapon in the room, then print
    if "Weapon" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['Weapon'])
    print("---------------------------")


# an item and weapon inventory, which is initially empty
inventory = []

weapon = []

# a dictionary linking a room to other rooms
rooms = {

        'Front Garden' : {
            'North' : 'Front Entrance',
            'West'  : 'West Garden',
            'East'  : 'East Garden'
            },

        'West Garden' : {
            'West' : 'Shed',
            'East' : 'Front Garden'
            },

        'East Garden' : {
            'West' : 'Front Garden',
            'Item' : 'Potion'
            },

        'Front Entrance' : {
            'North' : 'Hall',
            'West'  : 'Entertainment Room',
            'South' : 'Front Garden',
            'East'  : 'Office',
            'Item'  : 'Key'
            },

        'Hall' : {
            'North' : 'Dining Room',
            'West'  : 'Entertainment Room',
            'South' : 'Front Entrance',
            'East'  : 'Theater Room',
            'Weapon': 'Hockey Stick'
            },

        'Dining Room' : {
            'North' : 'Backyard',
            'West'  : 'Kitchen',
            'South' : 'Hall',
            'East'  : 'Living Room',
            'Weapon': 'Knife'
            },

        'Entertainment Room' : {
            'North' : 'Kitchen',
            'East'  : 'Hall',
            'Item'  : 'Shadow Monster'
            },

        'office' : {
            'West'  : 'Front Entrance',
            'Item'  : 'Skeleton King'
            },

        'Kitchen' : {
            'South' : 'Entertainment Room',
            'East'  : 'Dining Room',
            'Item'  : 'Shrooms'
            },
        
        'Theater Room' : {
            'East' : 'Hall',
            'Item' : 'Killer Klown'
            },

        'Living Room' : {
            'West' : 'Dining Room',
            'South': 'Garage',
            'Item' : 'The Blob'
            },

        'Garage' : {
            'North' : 'Living Room',
            'Item'  : 'Rope'
            },

        'Backyard' : {
            'Item' : 'Death Dealer'
             },

        'Shed' : {
            'East'  : 'West Garden',
            'Weapon': 'Chainsaw'
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
    # .title() makes each word capitalize, .split() turns it to a list
        move = move.title().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'Go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'Get' :
        # make two checks:
        # 1. if the current room contains an item or weapon
        # 2. if the item in the room matches the item the player wishes to get
        if "Item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['Item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' added!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['Item']
        # add weapon to inventory
        elif "Weapon" in rooms[currentRoom] and move[1] in rooms[currentRoom]['Weapon']:
            weapon.append(move[1])
            print(move[1] + ' added!')
            del rooms[currentRoom]['Weapon']
        # if there's no item in the room or the item or weapon doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

        ## If a player enters a room with a monster but has chainsaw kill monster
    if 'Item' in rooms[currentRoom] and 'Shadow Monster' in rooms[currentRoom]['Item']:
        if 'Chainsaw' in weapon:
            del rooms[currentRoom]['Item']
            print('Watch out! The Shadow Monster has appeared!')
            print('Luckily, we have our trusty chainsaw!')
            print('Chop em up and cut em down, we are going old Doom!')
            # del weapon['Chainsaw']
        else:
            print('A monster has got you... GAME OVER!')
            break

        ## Define how a player was tricked and lose the gamen
    if currentRoom == 'Backyard' and 'Potion' in inventory and 'Shrooms' in inventory and 'Rope' in inventory and 'Knife' in weapon:
        print('''You have come to your senses, you murdered the entire
               family... You have the tools to end it all...''')
        break
