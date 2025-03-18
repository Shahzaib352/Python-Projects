# Hungman Game
import random

list_of_secret_words = ["happy","birthday", "retrieval","testimony","punishment","jury", "survival", "death", "friendship", "guess", "lucky", "heaven","spy","hello","sad","cherry","mango","banana"]
secret_word = random.choice(list_of_secret_words)

def display_word(secret_word, guessed_letters):
    # create a list of underscores
    display = [letter if letter in guessed_letters else "_" for letter in secret_word]
    # join a list to a string and print it
    print(" ".join(display))
    
def play_hungman():
    secret_word = random.choice(list_of_secret_words)
    guessed_letters = set() # a set to store guessed letters
    max_guesses = 10
    incorrect_guesses = 0
    # Game loop
    while incorrect_guesses < max_guesses:
        display_word(secret_word, guessed_letters)
        print(f"Remaining guesses: { max_guesses - incorrect_guesses }")
        guess = input("Guess a letter: ").lower()
        # check the guessed letter
        if guess in guessed_letters:
            print("You have already guessed the letter.")
        elif guess in secret_word:
            guessed_letters.add(guess)
            print("Correct Letter!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect Letter! You have '{max_guesses - incorrect_guesses}' guesses left.")
        # check if the player guessed all the letters
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congrats! You have saved the Hungman and guessed the word '{secret_word}',")
            break
    else:
        print(f"Alas! The Hungman died. The word was '{secret_word}'.")
        
if __name__ == "__main__":
    while True:
        play_hungman()
        if input("Do you want to play againg? y/n: ").lower() == 'n': 
            break
