import time
import random


def random_creature():
    nouns = ['farie', 'gorgon', 'gnome', 'oni', 'cyclops', 'witch']
    n = random.choice(nouns)
    creature = n
    return creature


def print_pause(string):
    print(string)
    time.sleep(2)


def intro(items, creature):
    # Prints the intro to the game using the time.
    # sleep function for slower printing of text.
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow  wildflowers.")
    print_pause("Rumour has it that a wicked {} is somewhere around here,"
                "and has been terrfying the nearby village.".format(creature))
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not verry effective) dagger.")
    get_choice(items, creature)


def valid_input(prompt, option1, option2):
    # function for assessing whether players input is valid.
    while True:
        response = input(prompt).lower()
        if option1 == response:
            return response
        elif option2 == response:
            return response
        else:
            print_pause("Please try again\n")
    return response


def get_choice(items, creature):
    # get input from the user and moves the story forward based on the input.
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = valid_input("What would you like to do?\n (Please enter"
                         " 1 or 2)\n", "1", "2")
    if "1" == choice:
        print_pause("You approach the door of the house")
        house(items, creature)
    elif "2" == choice:
        print_pause("You peer cautiously into the cave")
        cave(items, creature)
    else:
        print_pause("Please enter 1 or 2")


def cave(items, creature):
    print_pause("It turns out to be only a very small cave")
    if "sword" not in items:
        items.append("sword")
        print_pause("You eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the"
                    "sword with you")
        print_pause("You walk back out to the field")
        get_choice(items, creature)
    elif "sword" in items:
        print_pause("You\'ve been here before and gotten all the good"
                    "stuff. It's just an empty cave now.")
        get_choice(items, creature)


def house(items, creature):
    print_pause("You are about to knock when the door opens and out"
                "steps a {}.".format(creature))
    print_pause("Eep! This is the {}'s house!".format(creature))
    print_pause("The {} attacks you!".format(creature))
    if "sword" not in items:
        print("You feel a bit under-prepared for this, what with only"
              "having a tiny dagger.\n")
    fight(items, creature)


def fight(items, creature):
    choice = valid_input("What would you like to do?\n Would you like"
                         " to (1) fight or (2) run away?\n", "1", "2")
    if "1" == choice and "sword" not in items:
        print_pause("You do your best...")
        print_pause("You lose! You have been defeated!")
        play_again()
    elif "1" == choice and "sword" in items:
        print_pause("As the {} moves to attack, you unsheath your"
                    " new sword.".format(creature))
        print_pause("The Sword of Ogoroth shiens brightly in your"
                    "hand as you brace youself for the attack")
        print_pause("But the {} takes one look at your shiny new"
                    "toy and runs away!".format(creature))
        print_pause("You won! You have rid the town of the {}."
                    "You are victorious!".format(creature))
        play_again()
    elif "2" == choice:
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.")
        get_choice(items, creature)


def play_again(): 
    response = valid_input("Would you like to play again? (y/n) \n ", "y", "n")
    if "n" == response:
        print_pause("Thanks for playing! See you next time")
    if "y" == response:
        print("Excellent! Restarting the game..")
        adventure_game()


def adventure_game():
    creature = random_creature()
    items = []
    intro(items, creature)


adventure_game()
