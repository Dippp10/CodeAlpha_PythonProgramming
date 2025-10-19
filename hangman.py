import random

def hangman():
    # Predefined list of 5 words
    words = ["python", "hangman", "program", "code", "alpha"]
    word = random.choice(words)  # Randomly select a word

    guessed_letters = []
    attempts = 6  # Limit incorrect guesses to 6
    word_display = ["_"] * len(word)

    print("🎯 Welcome to Hangman!")
    print("You have 6 chances to guess the word.\n")

    while attempts > 0 and "_" in word_display:
        print("Word:", " ".join(word_display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("❗ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!\n")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print("❌ Wrong guess!\n")
            attempts -= 1

    if "_" not in word_display:
        print(f"🎉 Congratulations! You guessed the word '{word}'.")
    else:
        print(f"😞 Out of attempts! The word was '{word}'.")

# Run the game
hangman()
