from replit import clear
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
#print(f'Pssst, the solution is {chosen_word}.')

#initialize number of lives
lives = 6

#create a display with each blank correspond to a letter of the random word
display = []
for letter in chosen_word:
    display.append("_")

#condition to loop, purpose is to user make multiple guess
end_game = False

while end_game == False:

    guess = input("Guess a letter: ").lower()

    #clear the terminal so it's more readeable
    clear()

    #check if guess letter by user as already been found
    if guess in display:
        print(f"You already find the {guess} letter")

    #initialize count
    count = 0
    #loop to each letter in random work
    for letter in chosen_word:
        count += 1
        if letter == guess:
            #count - 1 to accord it to the index and replace blank by guess
            display[count - 1] = guess

    #reduce lives by one if wrong guess and tell user if letter in the word, if live = 0 end game
    if not guess in chosen_word:
        print(f"{guess} not in the word to guess")
        lives -= 1

        #if no more lives, stop the game
        print(lives)
        if lives == 0:
            end_game = True
            print(
                "Sorry you lose, you haven't found the word, you'll be better next time"
            )

    #join all value of the display list
    print(f"{' '.join(display)}")

    #if no more blank in display game end by user win
    if not "_" in display:
        end_game = True
        print("Great, You guess the word, You win")

    #print the ascii art of hangman from hang man art
    print(hangman_art.stages[lives])
