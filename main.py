# Hangman game

# The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
# When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over. 
# For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

import random
from collections import Counter

word_collection = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

word_collection = word_collection.split(' ')

# randomly choose a secret word from our collection
secret_word = random.choice(word_collection)

if __name__ == '__main__':
    print("Guess the word! HINT: word is a name of a fruit.")

    for i in secret_word:
        # printing underscore for each letter in secret word
        print('_', end = ' ')
    print()

    playing = True
    # storing the letter guessed by player
    letter_guessed = ''
    chances = len(secret_word) + 2
    correct = 0
    flag = 0 # flag is updated when the word is correctly guessed

    try:
        while (chances != 0) and (flag == 0):
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print("Enter only a letter!")
                continue

            # validation of the guess
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter")
                continue
            elif guess in letter_guessed:
                print("You have already guessed that letter")
                continue

            # if letter is guessed correctly
            if guess in secret_word:
                c = secret_word.count(guess) # counts the number of times guess occurs in secret_word
                for _ in range(c):
                    letter_guessed += guess # adding the guess to letter_guessed as many times as it occurs in secret_word

            # printing the word
            for char in secret_word:
                if (char in letter_guessed and (Counter(letter_guessed) != Counter(secret_word))):
                    print(char, end = ' ')
                    correct += 1

            # if user has guessed all the letters, the game ends
            if (Counter(letter_guessed) == Counter(secret_word)):
                print('The word is: ', end = ' ')
                print(secret_word)
                flag = 1
                print('Congratulations, You won!')
                break # break out of the for loop
                break # break out of the while loop

            # if user has used all of his chances
            elif (chances == 0) and (Counter(letter_guessed) != Counter(secret_word)):
                print()
                print('You lost! Try again.')
                print('The secret word was {}'.format(secret_word))


    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()