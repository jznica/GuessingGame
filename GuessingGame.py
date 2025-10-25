#GuessingGame.py

import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)
guesssWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guesssWord))
    guess = input('Guess a letter: ').lower()
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guesssWord[i] = guess
                print('Great guess!')
    else:
        attempts -= 1
        print(f'Wrong guess! You have {attempts} attempts left.' + str(attempts))
        if '_' not in guesssWord:
            print('\nCongratulations! You guessed the word: ' + word)
            break
    if attempts == 0 and '_' in guesssWord:
        print('\nGame Over! The word was: ' + word)