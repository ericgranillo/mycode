#!/usr/bin/env python3
"""TLG Learning| EGranillo- Credit to Alta3 |  Adventure time:
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
            'East' : 'Front Garden',
            'Item' : 'Rope'
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
            'Weapon': 'Knife',
            'Item'  : 'Lighter'
            },

        'Entertainment Room' : {
            'North' : 'Kitchen',
            'East'  : 'Hall',
            'Item'  : 'Shadow Monster'
            },

        'Office' : {
            'North' : 'Theater Room',
            'West'  : 'Front Entrance',
            'Item'  : 'Skeleton King'
            },

        'Kitchen' : {
            'South' : 'Entertainment Room',
            'East'  : 'Dining Room',
            'Item'  : 'Shrooms'
            },

        'Theater Room' : {
            'West' : 'Hall',
            'South': 'Office',
            'Item' : 'Killer Klown'
            },

        'Living Room' : {
            'West' : 'Dining Room',
            'South': 'Garage',
            'Item' : 'Green Blob'
            },

        'Garage' : {
            'North' : 'Living Room',
            'Item'  : 'Gas Can'
            },

        'Backyard' : {
            'South': 'Dining Room',
            'Item' : 'Death Dealer'
             },

        'Shed' : {
            'East'  : 'West Garden',
            'Weapon': 'Og Chainsaw'
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
        if 'Og Chainsaw' in weapon:
            del rooms[currentRoom]['Item']
            print('Watch out! The Shadow Monster has appeared!\n')
            print('Luckily, we have our trusty chainsaw!\n')
            print('Chop em up and cut em down, we are going OG Doom!')
            # del weapon['Chainsaw']
        else:
            print('The Shadow Monster has attacked you... find the Og!')

        # If a player enters a room with a monsters but has other weapons
    if 'Item' in rooms[currentRoom] and 'Skeleton King' in rooms[currentRoom]['Item']:
        if 'Hockey Stick' in weapon:
            del rooms[currentRoom]['Item']
            print('Watch out! A Skeleton King has appeared!\n')
            print('We\'ll play hockey with his bones!\n')
            print('A monster, is this a nightmare?')
        else:
            print('The Skeleton King has attacked you... find weapons!')

        # if a player enters a room with a monster but has other weapons
    if 'Item' in rooms[currentRoom] and 'Killer Klown' in rooms[currentRoom]['Item']:
        if 'Knife' in weapon:
            del rooms[currentRoom]['Item']
            print('Watch out! A Killer Klown has appeared!\n')
            print('Send it back to outer space with that knife!\n')
            print('This can\'t be real?')
        else:
            print('The Killer Klown has attacked you... find a knife!')

        # if a player enters a room with a monster but has other weapons
    if 'Item' in rooms[currentRoom] and 'Green Blob' in rooms[currentRoom]['Item']:
        if 'Gas Can' in inventory:
            del rooms[currentRoom]['Item']
            print('Watch out! The Green Blob will eat you!\n')
            print('I guess this Green Blob has a melting point!\n')
            print('Surely I\'ll wake up soon, right?')
        else:
            print('The Blob has eaten your shoe... Quick burn it!')

        # if a player enters backyard without required items
    if 'Item' in rooms[currentRoom] and 'Death Dealer' in rooms[currentRoom]['Item']:
        if 'Shrooms' in inventory:
            del rooms[currentRoom]['Item']
            print('The Death Dealer has come for you!\n')
            print('Find all important items to escape its grip!\n')
            print('It\'ll all be over soon...\n')

        ## Define how a player was tricked and lose the gamen
    if (currentRoom == 'Backyard' and 'Potion' in inventory
            and 'Shrooms'in inventory and 'Rope' in inventory
            and 'Knife' in weapon):
        print('''You're finally awake! What have you done!
        You murdered the entire family...
        You have the tools to end it all...''')
        break
