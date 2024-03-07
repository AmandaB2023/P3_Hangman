import random
import string
import os
from art import *
from time import sleep
from colorama import Fore, Style
from words import words
from hangman_visual import hangman_visual_dict



""" Prints logo """
def hello():
    Art = text2art("  HANGMAN  ")
    print(Art)


""" Clear function to clean-up the terminal."""
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


""" Ask for users name """
def get_user_name():
    print(f"""Welcome to Hangman""")
    name = ''
    while True:
        name = input(f"""{Fore.GREEN } What is your name ?\n
        {Style.RESET_ALL}""").capitalize()
        print(' Please enter at least 3 letters.')
        if name.isalpha() and len (name) > 2:
            print('')
            clear_screen()
            print("Hello, " + name)
            break
        else:
            print(f"""{Fore.RED}Please enter your name using letters only! and press Enter{Style.RESET_ALL}""")
    return name


"""Randomly choose word from list."""
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


""" Start game,set number of letters in word and check 
what letters the user has guessed."""
def start_game():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    # Get the users letter input.
    while len(word_letters) > 0 and lives > 0 :
        # letters used
        print('You have',lives, 'lives left and you have used these letters: ', '  '.join(used_letters))
        #The  current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_visual_dict[lives])
        print('Your current word is : ', ' '.join(word_list))
        print(f"The word has {len(word)} letters.")

        user_letter = input('Please select a letter and hit Enter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
            # Takes away a life if letter is not in the word.
                lives = lives - 1
                print('Sorry but your chosen letter,', user_letter, 'is not in the word.\n')

        elif user_letter in used_letters:
            print(f"""\n Oops you have already used that letter.
            Have another guess.""")
        else:
            print(f""" \n {Fore.RED} Sorry but that is not a valid letter.
            {Style.RESET_ALL}""")

    # Game ends when letter == 0 OR when lives == 0 OR user guesses the correct word.
    if lives == 0:
        print(hangman_visual_dict[lives])
        print('Uh Oh you died, sorry. The word was', word)
        sleep(2)
        start_game()
    else:
        clear_screen()
        print('YAY! You guessed the word', word, '!!')
        print('')
        print(f"""{Fore.CYAN} CONGRATULATIONS!!!{Style.RESET_ALL}""")
        sleep(2)
        clear_screen()
        restart()


game_options = {

    1: 'Play game ',
    2: 'Rules',
    3: 'Exit',
}


""" Prints menu options and asks user to selet an option"""
def print_menu(user_name):
    print(f"""{Fore.GREEN}Please select one of the following options by typing 
    the cooresponding number and hitting Enter.{Style.RESET_ALL}""")
    for key in game_options.keys():
        print(key, '--', game_options[key])
    while (True):
        option = ''
        try:
            option = int(input('Please enter your selected menu option here  :  '))
        except:
            ValueError
            print(f"""{Fore.RED}Incorrect input type.{Style.RESET_ALL}""")
        # Check what option was entered by the user.
        if option == 1:
            option1()
            start_game()
        elif option == 2:
            option2(user_name)
            rules(user_name)
        elif option == 3:
            option3(user_name)
            exit()
        else:
            print(f"""{Fore.GREEN}Checking what option you have choosen...{Style.RESET_ALL}""")
            sleep(2)
            clear_screen()
            print(f"""{Fore.RED}Sorry that option was invalid.
            Please enter a number between 1 and 3.{Style.RESET_ALL}""")
            print_menu(user_name)


def option1():
    clear_screen()
    sleep(1)
    print(f"""{Fore.GREEN}Lets Play.....\n {Style.RESET_ALL}""")
    sleep(0.5)


def option2(user_name):
    clear_screen()
    print(f"""{Fore.BLUE}The Rules {Style.RESET_ALL}""")


def option3(user_name):
    clear_screen()
    print(f"""{Fore.CYAN}Thanks for playing !!{Style.RESET_ALL}""")
    print("Goodbye, " + user_name)


""" Game rules and how to play."""
def rules(user_name):
    clear_screen
    print(f"""{Fore.BLUE}
    * Try to save the hangman by guessing the  random word.
    * Guess a single letter at a time until you find the corrrect word.
    * You will have 7 lives.
    * If you guess an incorrect letter, you will lose a life.
    * If you lose all 7 lives, the game will end.
    * You cannot exit the game once it begins.
        {Style.RESET_ALL} """)
    input(f"""Hit enter to go back to the menu. \n""")
    clear_screen()
    sleep(1)
    print_menu(user_name)


"""Restart function to restart the game."""
def restart():
    clear_screen()
    print(f"""{Fore.GREEN} Would you like to play again ? {Style.RESET_ALL}""")
    while True:
        restart = input(""" For Yes please press Y and hit Enter , 
                        For No just hit Enter\n""")
        if restart.upper() == 'Y':
            clear_screen()
            sleep(1)
            print(f"""{Fore.GREEN} Restarting...\n {Style.RESET_ALL}""")
            sleep(0.5)
            clear_screen()
            start_game()
        else:
            clear_screen()
            print(f""" {Fore.BLUE} Goodbye, Thanks for playing , we hope you had fun!!!{Style.RESET_ALL}""")
            exit()


def main():
    hello()
    user_name = get_user_name()
    print_menu(user_name)


if __name__=='__main__':
    main()

