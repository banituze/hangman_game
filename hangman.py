secret_word = "python"

hangman_pics = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========""",
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========""",
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    ========="""
]

while True: 
    guessed_letters = []
    max_tries = 6
    tries = 0
    attempts = 0
    max_attempts = 3

    print("\nWelcome to Hangman!")
    print("You have to guess the word letter by letter.")
    print(f"You have {max_tries} tries to guess the word.")
    print(f"You can make {max_attempts} attempts for repeated guesses.")

    while tries < max_tries:
        print(hangman_pics[tries])
        available_letters = "".join([letter for letter in "abcdefghijklmnopqrstuvwxyz" if letter not in guessed_letters])
        print(f"Available letters: {available_letters}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input")
            continue

        if guess in secret_word:
            if guess in guessed_letters:
                print("You already guessed that letter.")
                attempts += 1
                print(f"Attempts: {attempts}/{max_attempts}")
                if attempts == max_attempts:
                    print("Too many repeated guesses! Game over!")
                    break
            else:
                print("Good guess!")
                guessed_letters.append(guess)
        else:
            tries += 1
            print(f"Wrong! {max_tries - tries} tries left")

        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        print(f"Current word: {display}")

        if "_" not in display:
            print("You won!")
            print(f"The word was: {secret_word}")
            break

    if "_" in display:
        print(hangman_pics[-1])
        print("You lost!")
        print(f"The word was: {secret_word}")

    replay = input("Do you want to play again? (Y/N): ").lower()
    if replay != "y":
        print("Goodbye!")
        break

