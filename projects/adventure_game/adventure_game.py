import time


def print_pause(string):
    print(string)
    time.sleep(2)

def intro(items):
    print_pause("You find yourself standing in an open field, filled with grass and yellow  wildflowers.")
    print_pause("Rumour has it that a wicked fairies is somewhere around here, and has been terrfying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not verry effective) dagger.")
    get_choice(items)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response 
        elif option2 in response:
            return response
        else:
            print_pause("Please try again\n")
    return response

def get_choice(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = valid_input("What would you like to do?\n"
                "(Please enter 1 or 2)\n", "1", "2")
    if "1" in choice:
            print_pause("You approach the door of the house")
            fight(items)
    elif "2" in choice:
            print_pause("You peer cautiously into the cave")
            cave(items)
    else:
        print_pause("Please enter 1 or 2")


def cave(items):
    print_pause("It turns out to be only a very small cave")
    print_pause("You eye catches a flint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    items.append("sword")
    if "sword" in items:
        print_pause("you've been here before, and got all the food stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field")
        get_choice(items)
    else: 
        get_choice(items)

def house(items):
    print_pause("You are about to knock when the door opens and out steps a gorgon.")
    print_pause("Eep! This is the gorgon's house!")
    print_pause("The gorgon attacks you!")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")

def fight():
    choice2 = valid_input("You feel a bit under-prepared for this, what with only having a tiny dagger.\n"
    "Would you like to (1) fight or (2) run away?", "1", "2")
    if 1 in choice and sword not in items:
        print_pause("You do your best...")
        print_pause("you have been defeted!")
    elif:
        1 in choice and sword in items:
        



def adventure_game():
    items = []
    intro(items)
    get_choice(items)

adventure_game()