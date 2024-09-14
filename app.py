# Rock paper scissors game that the user can play with computer in the vscode console.
# The computer's choice is random.
# The user can see the computer's choice.
# The user can see the result of the game.
# The user can see the score.
# The user can reset the score.
# The user can play again.
# The user can close the game.
# The user can see the rules of the game.
# The user can see the credits.
# The user can see the version of the game.
# The user can see the license.
# Rock beats scissors, scissors beats paper, paper beats rock.
# The user can choose rock, paper, or scissors by typing the whole word.
# The user can choose rock, paper, or scissors by typing the first letter of the word.

# Imports
import random
import tkinter as tk
from tkinter import messagebox

# Constants
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
WIN = 'win'
LOSE = 'lose'
DRAW = 'draw'

# Variables
score = 0

# Functions
def computer_choice():
    choices = [ROCK, PAPER, SCISSORS]
    return random.choice(choices)

def play(user_choice):
    computer = computer_choice()
    if user_choice == computer:
        result = DRAW
    elif user_choice == ROCK and computer == SCISSORS:
        result = WIN
    elif user_choice == PAPER and computer == ROCK:
        result = WIN
    elif user_choice == SCISSORS and computer == PAPER:
        result = WIN
    else:
        result = LOSE
    global score
    if result == WIN:
        score += 1
    elif result == LOSE:
        score -= 1
    return computer, result

def play_game():
    user_choice = input('Choose rock, paper, or scissors: ')
    if user_choice == 'r':
        user_choice = ROCK
    elif user_choice == 'p':
        user_choice = PAPER
    elif user_choice == 's':
        user_choice = SCISSORS
    computer, result = play(user_choice)
    print(f'Computer: {computer}')
    print(f'Result: {result}')
    print(f'Score: {score}')
    play_again()

def reset():
    global score
    score = 0

def play_again():
    play_game()

def close():
    window.destroy()

def rules():
    messagebox.showinfo('Rules', 'Rock beats scissors, scissors beats paper, paper beats rock.')

def credits():
    messagebox.showinfo('Credits', 'Made by SammyBloom.')

def version():
    messagebox.showinfo('Version', '1.0.0')

def license():
    messagebox.showinfo('License', 'MIT License')

# Main
window = tk.Tk()
window.title('Rock Paper Scissors')
window.geometry('400x400')
button_play = tk.Button(window, text='Play', command=play_game)
button_play.pack()
button_reset = tk.Button(window, text='Reset', command=reset)
button_reset.pack()
button_close = tk.Button(window, text='Close', command=close)
button_close.pack()
button_rules = tk.Button(window, text='Rules', command=rules)
button_rules.pack()
button_credits = tk.Button(window, text='Credits', command=credits)
button_credits.pack()
button_version = tk.Button(window, text='Version', command=version)
button_version.pack()
button_license = tk.Button(window, text='License', command=license)
button_license.pack()
window.mainloop()

# Run
if __name__ == '__main__':
    play_game()