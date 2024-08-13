import random
import time
import os


def Menu():
    print("   _______  _______  _______  _______  _______  _______  _______ ")
    print("Welcome To Russian Roulette")
    print("If you survive, you win.")
    print("If you die, you lose.")


    while True:
        try:
            choice = int(input("Choose an option: \n1. Multiplayer\n2. Single Player\n\nYour choice: "))
            if choice == 1 or choice == 2:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    os.system('cls')
    return choice

def Single_Player():
    while True:
        print("Single Player mode starting....")
        time.sleep(3)
        os.system('cls')

        print("You have a revolver with 1 bullet in 1 chamber.")
        time.sleep(2)
        os.system('cls')
        input("Press Enter to load the bullet into a random chamber...")
        time.sleep(3)
        os.system('cls')  

        bullet_position = random.randint(1, 6)
        print("The bullet has been loaded into a random chamber.")

        while True:
            try:
                player_chamber = int(input("\nChoose a chamber to fire (1-6): "))
                if 1 <= player_chamber <= 6:
                    break
                else:
                    print("This is a revolver! Please enter a number between 1 and 6.")
            except ValueError:
                print("Gun jammed, please enter a number between 1 and 6.")

        print("\nSpinning the chamber...")
        time.sleep(2)  

        if player_chamber == bullet_position:
            print("Bang! You will face God.")
        else:
            print("Click! God gave you one more chance, you're safe right now.")

        while True:
            option = input("\nDo you want to continue or return to the menu? (Y/N): ").strip().lower()
            if option == 'y':
                break  
            elif option == 'n':
                return  
            else:
                print("Invalid option. Please enter 'Y' to continue or 'N' to return to the menu.")

def Multiplayer():
    while True:
        print("Multiplayer mode starting....")
        time.sleep(3)
        os.system('cls')

        print("You will play with your friend")
        time.sleep(3)
        os.system('cls')
        input("Press Enter to load the bullet into a random chamber...")
        time.sleep(3)
        os.system('cls')

        bullet_position = random.randint(1, 6)
        print("The bullet has been loaded into a random chamber.")

        for shot in range(1, 7):
            input(f"\nPlayer {shot % 2 + 1}, press Enter to fire (Attempt {shot}/6)...")
            print("Spinning the chamber...")
            time.sleep(2)
            print("Player puts the gun to their head and shoots!")
            time.sleep(2)
            os.system('cls')
            
            if shot == bullet_position:
                print(f"Bang! Player {shot % 2 + 1} is hit!")
                print(f"Player {shot % 2 + 1} will face God.")
                print("*God will forgive you, but we don't.")
                break
            else:
                print("Click! You're safe.")
                time.sleep(2)
                print("*Gun moved.")
                time.sleep(2)
                os.system('cls')

        # Prompt for continuation or return to menu
        while True:
            option = input("\nDo you want to continue or return to the menu? (Y/N): ").strip().lower()
            if option == 'y':
                break  # Restart the Multiplayer loop
            elif option == 'n':
                return  # Exit the Multiplayer function and return to the menu
            else:
                print("Invalid option. Please enter 'Y' to continue or 'N' to return to the menu.")

while True:
    user_choice = Menu()

    if user_choice == 2:
        Single_Player()
        print("wait a second...")
        time.sleep(3)
        os.system('cls')
    elif user_choice == 1:
        Multiplayer()
        print("wait a second...")
        time.sleep(3)
        os.system('cls')
