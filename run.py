import random
import string
import os
from time import sleep
import time
from colorama import Fore, Style
from words import words
from hangman_visual import hangman_visual_dict
from welcome import logo

"""
Prints logo
"""
def hello():
    print(logo)

"""
Clear's function to clean-up the terminal.
"""
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_user_name():
    name = ''
    while True:
        name = input ("What is your name ?\n").capitalize()
        if name.isalpha() == True:
            print('')
            clear_screen()
            print(f"""{Fore.YELLOW }Hello, " + name {Style.RESET_ALL}""")
            break
        else:     
            print(f"""{Fore.RED}Please enter your name using letters only!{Style.RESET_ALL}""")
    return name


def restart():
    clear_screen()
    print('Would you like to play again ?')
    restart = input('Yes / No(Y/N)\n')
    if restart.upper() == 'Y':
        clear_screen()
        time.sleep(1)
        print ("Restarting...\n")
        time.sleep(0.5)
        clear_screen()
        print_menu()
    elif restart.upper() =='N':
        clear_screen()
        print('Goodbye')
        exit()


"""
Randomly choose word from list.
"""        
def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

"""
Start game , set number of letter in word 
and check what letters the user has gussed.
""" 
def start_game():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 7

    # get the users letter input
    while len(word_letters) > 0 and lives > 0 : 
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        # the  current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_visual_dict[lives])
        print('Your current word is : ', ' '.join(word_list))

        user_letter = input('Select a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1  # takes away a life if letter is not in word
                print('\n Your letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print(f"""\n Oops you have already used that letter. Have another guess.""")
    

        else:
            print(f""" \n Sorry but that is not a valid letter.""")

    """
    Game ends when letter == 0 OR when lives == 0 OR user guesses the correct word.
    """
    if lives == 0:
        print(hangman_visual_dict[lives])
        print('Uh Oh you died, sorry. The word was', word)
        time.sleep(2)
        start_game()
    else:
        print('YAY! You guessed the word', word, '!!')
        print('')
        print('CONGRATULATIONS!!!')
        time.sleep(2)
        clear_screen()
        restart()


game_options = {
    1: 'Play game ',
    2: 'Rules',
    3: 'Exit' ,
}

def print_menu(user_name):
    print(f"""Please select one of the following options by typing the corresonding number and hitting enter""")
    for key in game_options.keys():
        print (key, '--', game_options[key] )
    while(True):
        option = ''
        try:
            option = int(input('Enter your selected menu option here :    '))
        except:
            print('Incorrect input type.')
        """
        Check what option was entered by the user.
        """ 
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
            print("Checking what option you have choosen...")
            sleep(2)
            clear_screen()
            print(f"""Sorry that option was invalid. Please enter a number between 1 and 3.""")
            print_menu(user_name)
            


def option1():
    clear_screen()
    time.sleep(1)
    print ("Lets Play...\n")
    time.sleep(0.5)


def option2(user_name):
    clear_screen()
    print('The Rules ')


def option3(user_name):
    clear_screen()
    print('Thanks for playing !!')
    print("Goodbye,  " +    user_name)


def rules(user_name):
    clear_screen
    """
    Game rules and how to play.
    """
    print(f"""
    * Try to save the hangman by guessing the word.
    * Guess  a single letter at a time untill you find the word.
    * You will have 7 lives .
    * If you guess wrong, you will lose a life.
    * if you loose all 7 lives the game will end.
    * You cannot exit the game once it begins.
        """)
    input('Hit any key and press enter to go back to the nenu. \n') 
    clear_screen() 
    sleep(1)
    print_menu(user_name)

def main():
    hello()
    user_name = get_user_name()
    print_menu(user_name)    


if __name__=='__main__':
    main()

