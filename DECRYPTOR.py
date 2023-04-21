'''BABIERA,ALEXA | CMPE 103 LAB EXERCISE NO. 1 (PROBLEM 3) | OOP|APRIL 07,2023 '''
# import the necessary module
from pyfiglet import figlet_format
import pygame
from termcolor import colored
import pyfiglet
from colorama import Back, Fore, Style, init
import time

# formatting the header
art = figlet_format(" PROBLEM 2\nDECRYPTION", font='block', width=500)
c_art = colored(art, 'yellow')

print(Fore.LIGHTCYAN_EX + "=" * 100)
for line in c_art.split("\n"):
    print(line.center(100))
print(Fore.LIGHTCYAN_EX + "=" * 100)

print(Fore.YELLOW + "=" * 100)
print(Fore.WHITE + '''PROBLEM 2 - DECRYPTION
Write a program that will accept a string as encypted text and then the program will decrypt it using the following character substitute:
'a'= *, 'e'= &, 'i'= #, 'o'= +, 'u'= ! ''')
print(Fore.YELLOW + "=" * 100)


# Program takes in user's input (message)
message = input(
    Fore.CYAN + "Enter an encrypted message \n(ex. th& q!#ck br+wn f+x ) : ")
changed_char = ""

# loop the message to check each character
for i in range(len(message)):
    # replace characters
    # replace * with a
    if message[i] == "*":
        # set a control :
        changed_char += "a"
    # replace & with e
    elif message[i] == "&":
        changed_char += "e"
    # replace # with i
    elif message[i] == "#":
        changed_char += "i"
    # replace + with 0
    elif message[i] == "+":
        # set a control
        changed_char += "o"
    # replace ! with u
    elif message[i] == "!":
        # set a control
        changed_char += "u"
    else:
        changed_char += message[i]