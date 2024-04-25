import random

def choose_word():
    words = {
        "python": "Named after a type of snake, it's a popular programming language.",
        "hangman": "This game involves guessing letters to uncover a hidden word.",
        "programming": "The act of writing instructions for computers to execute.",
        "challenge": "Something that requires effort and skill to overcome.",
        "solution": "The answer to a problem or puzzle.",
        "game": "An activity engaged in for amusement or recreation.",
        "fish": "They breathe through gills and live in water.",
        "teddybear": "A stuffed toy often given as a gift.",
        "photoshop": "A popular software for editing images.",
        "philphs": "An electronic device used for communication and accessing the internet.",
        "illustration": "A visual interpretation or depiction of a concept or idea."
    }
    return random.choice(list(words.items()))

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word, clue = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Here's a riddle clue: ", clue)
    print("Guess the word:", display_word(word, guessed_letters))

    while incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()

        if guess == word:
            print("Congratulations! You guessed the word:", word)
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1

        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word:", word)
            return

    print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
