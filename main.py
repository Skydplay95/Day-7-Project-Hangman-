#Step 2

import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

#import word list form a file
from hangman_words import word_list

#chose a random word in the list
chosen_word = random.choice(word_list)

#import logo and print it
import hangman_art

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

lives = 6

display = []
for letter in chosen_word:
    display.append("_")

#condition to loop, purpose is to user make multiple guess
end_game = False
while end_game == False:

    guess = input("Guess a letter: ").lower()

    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    #check if guess letter by user as already been found
    if guess in display:
        print(f"You already find the {guess} letter")

    count = 0
    for letter in chosen_word:
        count += 1
        if letter == guess:
            display[count - 1] = guess
            #print("Right")

    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

    #reduce lives by one if wrong guess and tell user if letter in the word, if live = 0 end game
    if not guess in chosen_word:
        print(f"{guess} not in the word to guess")
        lives -= 1

        print(lives)
        if lives == 0:
            end_game = True
            print("Sorry you lose")

    print(f"{' '.join(display)}")

    #if no more blank in display game end by user win
    if not "_" in display:
        end_game = True
        print("Great, You guess the word, You win")

    #print the ascii art of hangman from hang man art
    print(hangman_art.stages[lives])
