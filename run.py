import os


"""
Clear function to clean-up the terminal.
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
            print(f""" Hello, " + name """)
            break
        else:
            print(f""" Please enter your name using letters only. """)
    return name