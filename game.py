import random

import string

def menu():
    print("""Choose a difficulty
         1._ Easy (all vowels are shown)
         2._ Medium (the first and the last letter are shown)
         3._ Hard (nothing is shown)
         """)

def easy_or_hard(secret_word, difficulty):
    guessed_letters = []
    i_won = False
    failed_attempts = 0

    print("I am thinking in a word. ¿Can you guess it?")

    # Check the difficulty to print the word 
    if difficulty == "1":
        word_displayed = ""
        vowels = "aeiou"

        for letter in secret_word:
            if letter in vowels:
                word_displayed += letter
                guessed_letters.append(letter)
            else:
                word_displayed += "_"
    else:
         word_displayed = "_" * len(secret_word)           

    # Show the partially guessed word
    print(f"Word: {word_displayed}")

    while failed_attempts < 10 and not i_won:
        # Ask the player to enter a letter
        letter = input("Enter a letter: ").lower()

        # Check if it is not empty and if it is not a word(point 7a)
        if not letter:
            print("You did not enter anything, pay attention ")
            continue

        if letter not in string.ascii_letters:
            print("You did not enter a letter, pay attention ")
            continue

        # Check if the letter has already been guessed
        if letter in guessed_letters:
            print("You have already tried with that letter. Try with another.")
            continue

        # Add the letter to the list of guessed letters
        guessed_letters.append(letter)

        # Check if the letter is in the secret word
        if letter in secret_word:
            print("¡Well done! The letter is in the word.")
        else:
            print("Sorry, the letter is not in the word.")
            failed_attempts += 1
            print(f"failed attempts : {failed_attempts}")

        # Show the partially guessed word
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")

        word_displayed = "".join(letters)
        print(f"Word: {word_displayed}")

        # Check if the complete word has been guessed
        if word_displayed == secret_word:
            print(f"¡Congratulations! You have guessed the secret word: {secret_word}")
            i_won = True

    #ran out of attempts
    if not i_won:        
        print(f"¡Oh no! You have reached your {failed_attempts} failed attempts.")
        print(f"The secret word was: {secret_word}")  

def medium(secret_word):
    guessed_letters = []
    i_won = False
    failed_attempts = 0

    print("I am thinking in a word. ¿Can you guess it?")
    word_displayed = secret_word[0] + "_" * (len(secret_word) -2) + secret_word[len(secret_word)-1]
    
    # Show the partially guessed word
    print(f"Word: {word_displayed}")

    while failed_attempts < 10 and not i_won:
        # Ask the player to enter a letter
        letter = input("Enter a letter: ").lower()

        # Check if it is not empty and if it is not a word(point 7a)
        if not letter:
            print("You did not enter anything, pay attention ")
            continue

        if letter not in string.ascii_letters:
            print("You did not enter a letter, pay attention ")
            continue
 
        # Check if the letter has already been guessed
        if letter in guessed_letters:
            print("You have already tried with that letter. Try with another.")
            continue

        # Add the letter to the list of guessed letters
        guessed_letters.append(letter)

        # Check if the letter is in the secret word
        if letter in secret_word:
            print("¡Well done! The letter is in the word.")
        else:
            print("Sorry, the letter is not in the word.")
            failed_attempts += 1
            print(f"failed attempts : {failed_attempts}")

        # Show the partially guessed word
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")

        word_displayed = secret_word[0] + "".join(letters[1:-1]) + secret_word[len(secret_word)-1]
        print(f"Word: {word_displayed}")
        # Check if the complete word has been guessed
        if word_displayed == secret_word:
            print(f"¡Congratulations! You have guessed the secret word: {secret_word}")
            i_won = True

    #ran out of attempts
    if not i_won:        
        print(f"¡Oh no! You have reached your {failed_attempts} failed attempts.")
        print(f"The secret word was: {secret_word}")                    

# Main

# List of possible words
words = ["python", "programacion", "computadora", "codigo", "desarrollo", "inteligencia"]

# Choose a random word
secret_word = random.choice(words)

print("¡Welcome to the guessing game!")

menu()

while True:
    difficulty = (input())
    if difficulty == "1" or difficulty == "2" or difficulty == "3":
        break
    else:
        print("You have entered an incorrect value, please enter '1, 2 or 3' ")
        continue

if difficulty == "1":
    easy_or_hard(secret_word, difficulty)
elif difficulty == "2":
    medium(secret_word)
else:
    easy_or_hard(secret_word, difficulty)
