
import time

def print_pause(string):
    print(string)
    time.sleep(2)

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response 
        elif option2 in response:
            return response
        else:
            print_pause("Sorry I don't understand")
    return response
    
def get_order():
    response = valid_input("Please place your order.\n"
                           "Would you like waffles or pancakes?\n",
                            "waffles", "pancakes" )
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly")
    order_again()


def order_again():
     response = valid_input("Would you like to place another order? "
                            "Please say 'yes' or 'no'.\n", "yes", "no").lower()
     if "no" in response:
         print_pause("OK, goodbye")
     if "yes" in response:
         print_pause("Very good, I'm happy to take another order.")
         get_order()

def order_breakfast():
    intro()
    get_order()
    order_again()

order_breakfast()

"""
Code before refactoring
    while True:
        while True:
            response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
            if "waffles" in response:
                print("Waffles it is!")
                time.sleep(2)
                break
            elif "pancakes" in response:
                print("Pancakes it is!")
                time.sleep(2)
                break
            else:
                print("Sorry, I don't understand.")
                time.sleep(2)
        print("Your order will be ready shortly.")
        time.sleep(2)



      while True:   
    order_again = input("Would you like to place another order? "
                            "Please say 'yes' or 'no'.\n").lower()
    if 'no' in order_again:
        print("OK, goodbye!")
        time.sleep(2)
        break
    elif 'yes' in order_again:
        print("Very good, I'm happy to take another order.")
        time.sleep(2)
    else:
            print("sorry I don't understand.")
    if 'no' in order_again:
         break         
"""

