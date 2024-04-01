#sudo chown -R testuser:testuser /var/www/test/public_html


import time
import pyfiglet
import keyboard
import ascii
import pygame

pygame.init()
pygame.mixer.init()

from PIL import Image
from art import *

######### Lists and inventory ###########
#list
health = 15
Welness = 100
progress = []

location_status = None
map = ascii.maps
food = ['food',{'name':'Apples', 'quantity':1, 'price':.10}]
weapons = ['weapons',{'name':'Knife','condition':'dull','quantity':1,'price':1.00 }]

#dictonary/object 
inventory = [map,food,weapons]


########## Command Functions ###########

def display_ascii(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

#don't think I'm using this
def convert_image_to_ascii(image_path):
    img = Image.open(image_path)
    ascii_art = text2art(str(img), font='block', chr_ignore=True)
    print(ascii_art)

def gameHelp():
    print('You asked for help so here it is...')
    print('Type "*commands" for a list of commands')

def start_game():
    display_ascii('Memory Lane!')
    print("Created By : Wayne Collier and Monica Weiss-Sharp")  
    print(" ")
    time.sleep(2) 
    print("It begins...")
    time.sleep(1)  
    print("You awaken and find yourself benieth an old oak tree.")
    time.sleep(1) 
    print(ascii.tree)
    time.sleep(1)

   # play_music('./Music/2021-08-17_-_8_Bit_Nostalgia_-_www.FesliyanStudios.com.mp3')

    print("Dry blood seems to be on your right arm and on the right side of your face")
    time.sleep(1)  
    print("You look around...")
    time.sleep(1)  
    print(".................")
    time.sleep(1)  
    print("It seems to be mid morning")
    time.sleep(1)  
    print(".................")
    time.sleep(1)  
    print("But")
    time.sleep(1)  
    print(".................")
    time.sleep(1)  
    print("You're not sure who you are.")
    time.sleep(1)  

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

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    # each of these functions can be the "levels" of the game the player is 
    # currently on 

   # start_game()
    while True:

            user_input = input("\nWhat would you like to do? Enter a command or h for help: ")

            if user_input.lower() == "*inventory":
                print("\nInventory List:")
                for item in inventory:
                    if item[0] == 'maps':
                        print(f"Map : {item[1]}")
                    elif item[0] == 'food':
                        f2 = item[1]
                        print("Food")
                        print("-------")
                        print(f"Name : {f2['name']}")
                        print(f"Quantity : {f2['quantity']}")
                        print(f"Price : {f2['price']}")
                    elif item[0] == 'weapons':
                        w2 = item[1]
                        print("Weapons")
                        print("---------")
                        print(f"Name : {w2['name']}")
                        print(f"Condition : {w2['condition']}")
                        print(f"Quantity : {w2['quantity']}")
                        print(f"Price : {w2['price']}")
                        #for items in item:
                            

            elif user_input.lower() == "h":
                print(gameHelp())
            elif user_input.lower() == "*commands":
                print(commands_list())
            elif user_input.lower() == "*c":
                print(commands_list())
            elif user_input.lower() == "*co":
                print(commands_list())
            elif user_input.lower() == "*com":
                print(commands_list())    
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





