import random

# List of predefined words
words = ["apple", "banana", "orange", "grapes", "mango"]

# Select a random word
secret_word = random.choice(words)

# Create blanks for guessed word
guessed_word = ["_"] * len(secret_word)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    # User input
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if letter is in word
    if guess in secret_word:
        print("✅ Correct guess!")

        # Reveal letter positions
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# Result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)
