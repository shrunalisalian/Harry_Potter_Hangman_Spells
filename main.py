# write a function to get valid words: words without "-" or " "
import random
import string 
from word_list import words

def get_valid_words(words):
    word = random.choice(words) # choses a word randomly from the given list
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def main():
    # computer has to randomly choose a word and the user has to guess a letter in that word
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters that the user has guessed

    attempts = 6 
    while len(word_letters) > 0 and attempts > 0:

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Welcome to Harry Potter Hangman Spell Game: ", " ".join(word_list))

        # getting user input
        user_letter = input(" Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters: 
                word_letters.remove(user_letter)
            else: 
                attempts -=1 # decrease number of attempts if wrong guess
                print(f"Wrong guess you have {attempts} attempts left")
        elif user_letter in used_letters:
            print(" Letter already used")
        else:
            print("Invalid input")
        print(" You have used these letters: ",", ".join(sorted(used_letters)))

    if attempts == 0:
        print("Game over. The word is {}".format(word))
    else:
        print("Congrats! You have guessed the word {}".format(word))

if __name__ == "__main__":
    main()

