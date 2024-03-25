#pip install pyfiglet
#pip install art

import time
import pyfiglet
import keyboard
import ascii

from PIL import Image
from art import *



def display_ascii(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

def convert_image_to_ascii(image_path):
    img = Image.open(image_path)
    ascii_art = text2art(str(img), font='block', chr_ignore=True)
    print(ascii_art)

def start_game():
    display_ascii('Memory Lane!')
    print("Created By : Wayne Collier and Monica Weiss-Sharp")
    time.sleep(4)  # Add a delay for dramatic effect
    print(" ")
    time.sleep(4)  # Add a delay for dramatic effect
    print("It begins...")
    time.sleep(4)  # Add a delay for dramatic effect
    print("You awaken and find yourself benieth an old oak tree.")
    time.sleep(4)  # Add a delay for dramatic effect
    print(ascii.tree)
    
    # if __name__ == "__main__":
    #     image_path = "/home/wayne/Coding/Python/MemLane/Images/tree.jpeg"
    #     convert_image_to_ascii(image_path)
    
    time.sleep(5)
    print("Dry blood seems to be on your right arm and on the right side of your face")
    time.sleep(4)  # Add a delay for dramatic effect
    print("You look around...")
    time.sleep(4)  # Add a delay for dramatic effect
    print(".................")
    time.sleep(4)  # Add a delay for dramatic effect
    print("It seems to be mid morning")
    time.sleep(4)  # Add a delay for dramatic effect
    print(".................")
    time.sleep(4)  # Add a delay for dramatic effect
    print("But")
    time.sleep(4)  # Add a delay for dramatic effect
    print(".................")
    time.sleep(4)  # Add a delay for dramatic effect
    print("You're not sure who you are.")
    time.sleep(4)  # Add a delay for dramatic effect

def enter_lane():
    print("\nYou decide to walk down the lane.")
    print("As you venture further, the surroundings become increasingly unfamiliar.")
    time.sleep(2)

def encounter_enemy():
    print("\nSuddenly, you encounter a fierce enemy blocking your path!")
    print("You must defeat the enemy to continue your journey.")

    # Add code here for combat mechanics (e.g., player attacks, enemy attacks, health points, etc.)

def reach_goal():
    print("\nCongratulations! You have successfully navigated through Memory Lane.")
    print("You reach the end of the lane and discover a hidden treasure.")
    print("Thanks for playing!")

def check_for_escape():
    return keyboard.is_pressed('esc')

def main():
    start_game()
    
    # while True:
    #     if check_for_escape():
    #         print("You pressed Escape. Exiting the game.")
    #         break

    #enter_lane()
    #encounter_enemy()  # You can expand this to include other encounters or challenges
    #reach_goal()

if __name__ == "__main__":
    main()


#Earth!Moon@Sun#Stars$


