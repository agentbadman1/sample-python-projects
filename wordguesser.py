# word guessing game

import random

def guesser():
    list = ["rishabh", "jeeban", "jeel", "mintu", "rushi"]
    word = random.choice(list)
    vc = "abcdefghijklmnopqrstuvwxyz"
    attempt = 5
    guessword = ""
    
    while True:

        mainword = ""

        for letter in word:
            if letter in guessword:
                mainword = mainword + letter
            else:
                mainword = mainword + "_"

        if mainword == word:
            print("You Win")
            print(f"The word was {word}")
            break

        print(f'Guess the word {mainword}')
        guess = input()

        if guess.lower() in vc:
            guessword = guessword + guess.lower()
        else:
            print("Please enter valid character")
            guess = input()

        if guess.lower() not in word:
            attempt = attempt - 1
            print(f"You have {attempt} left")

        if attempt ==0:
            print("You lose")
            print(f"The word was {word}")
            break


guesser()