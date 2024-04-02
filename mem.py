import time
import pyfiglet
import pygame
from art import *
import ascii

pygame.init()
pygame.mixer.init()

######### Lists and inventory ###########
health_value = 15
Wellness = 100
progress = []

location_status = None
map = ascii.maps
food = ['food', {'name': 'Apples', 'quantity': 1, 'price': .10}]
weapons = ['weapons', {'name': 'Knife', 'condition': 'dull', 'quantity': 1, 'price': 1.00}]

inventory = [map, food, weapons]

########## Command Functions ###########

def display_ascii(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

def gameHelp():
    print('Type "*commands" for a list of commands')

def health():
    return health_value

def sleep():
    global health_value
    health_value += 20
    if health_value > 100:
        health_value = 100
        print("Your Health is MAX")
    print("You slept for a few hours.")
    print(f"Health increased to {health_value}.")

def start_walk():
    print("You are walking")

def make_choice(a,b,c):
    print(a)
    print(b)
    print(c)
    while True:
        user_input = input("\nEnter a command or 'h' for help: ")
        if user_input.lower() == "*inventory":
            print(inv())
        elif user_input.lower() == "h":
            print(gameHelp())
        elif user_input.lower() == "*commands":
            print(commands_list())
        elif user_input.lower() == "1":
            print(inv())
        elif user_input.lower() == "2":
            sleep()
        elif user_input.lower() == "3":
            print(start_walk())
        elif user_input.lower() == "health":
            print(f"Health: {health()}")
        elif user_input.lower() == "quit":
            print("Exiting the game.")
            break
        else:
            print("Invalid command. Please try again.")

def start_game():
    play_music(r'C:\Users\waynec.PATIENTFOCUS\Desktop\PythonStuff\MemoryLane\Music\2021-08-17_-_8_Bit_Nostalgia_-_www.FesliyanStudios.com.mp3')


    display_ascii('Memory Lane!')
    print("Created By : Wayne Collier and Monica Weiss-Sharp")
    print(" ")
    time.sleep(2)
    print("It begins...")
    time.sleep(1)
    print("You awaken and find yourself beneath an old oak tree.")
    time.sleep(1)
    print("Dry blood seems to be on your right arm and on the right side of your face")
    time.sleep(1)
    print("You come to your feet.")
    time.sleep(1)
    print(f"Health: {health()}")
    print("What would you like to do: ")

    option_1 = "1 - Check your pockets"
    option_2 = "2 - Sleep a few hours"
    option_3 = "3 - Start walking down the road"
    make_choice(option_1, option_2, option_3)


def commands_list():
    print('*inventory')
    print('health')
    print('*commands')
    print('*quit')

def inv():
    for item in inventory:
        print("\nInventory List:")
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

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    start_game()

main()
