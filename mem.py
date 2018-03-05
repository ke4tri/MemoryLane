#pip install pyfiglet
#pip install art
#sudo chown -R testuser:testuser /var/www/test/public_html

import time
import pyfiglet
import keyboard
import ascii

from PIL import Image
from art import *

#list
health = [15]
progress = []

location_status = None
maps = {'name':'Map', 'quantity':1}
food = {'name':'Apples', 'quantity':1, 'price':.10}
weapons = {'name':'Knife','condition':'dull','quantity':1,'price':1.00 }

#dictonary/object 
inventory = [pockets,food,weapons]



def display_ascii(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

#don't think I'm using this
def convert_image_to_ascii(image_path):
    img = Image.open(image_path)
    ascii_art = text2art(str(img), font='block', chr_ignore=True)
    print(ascii_art)

def start_game():
    display_ascii('Memory Lane!')
    print("Created By : Wayne Collier and Monica Weiss-Sharp")
    time.sleep(4)  
    print(" ")
    time.sleep(4) 
    print("It begins...")
    time.sleep(4)  
    print("You awaken and find yourself benieth an old oak tree.")
    time.sleep(4) 
    print(ascii.tree)
    time.sleep(5)
    print("Dry blood seems to be on your right arm and on the right side of your face")
    time.sleep(4)  
    print("You look around...")
    time.sleep(4)  
    print(".................")
    time.sleep(4)  
    print("It seems to be mid morning")
    time.sleep(4)  
    print(".................")
    time.sleep(4)  
    print("But")
    time.sleep(4)  
    print(".................")
    time.sleep(4)  
    print("You're not sure who you are.")
    time.sleep(4)  

def enter_lane():
    print("\nYou decide to walk down the lane.")
    print("As you venture further, the surroundings become increasingly unfamiliar.")
    time.sleep(2)

def encounter_enemy():
    print("\nSuddenly, you encounter a fierce enemy blocking your path!")
    print("You must defeat the enemy to continue your journey.")

def reach_goal():
    print("\nCongratulations! You have successfully navigated through Memory Lane.")
    print("You reach the end of the lane and discover a hidden treasure.")
    print("Thanks for playing!")

def commands_list():
    print('*inventory')
    print('*commands')
    print('*quit')

def check_for_escape():
    return keyboard.is_pressed('esc')

def main():
    start_game()
    while True:

            user_input = input("\nWhat would you like to do? Enter a command: ")

            if user_input.lower() == "*inventory":
                print("\nInventory List:")
                for item in inventory:
                    print(item)
            elif user_input.lower() == "*commands":
                print(commands_list)
            elif user_input.lower() == "quit":
                print("Exiting the game.")
                break
            else:
                print("Invalid command. Please try again.")
    #enter_lane()
    #encounter_enemy()  # You can expand this to include other encounters or challenges
    #reach_goal()

if __name__ == "__main__":
    main()

    #adding commit for test of clock
    #testing github clocks again





