from words import words
from hangman_visual import lives_visual_dict
import random, string

def get_valid_word(words):
    word = random.choice(words)
    while ("-" in word or " " in word): word = random.choice(words)
    return word

def play_hangman():
    word = get_valid_word(words).upper()
    chars = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed = list()
    correct = 0
    lives = 7

    while (correct < len(chars) and lives > 0):
        current = [char if char in guessed else '_ ' for char in word]
        print(f"\nGuessed Letters: {' '.join(guessed)}")
        print(f"\n{''.join(current)}")

        guess = input("\nGuess a letter: ").upper()
        if (guess in guessed):
            print(f"\nYou already guessed {guess.upper()}. Try again.")
        elif (guess in chars):
            guessed.append(guess)
            correct += 1
            print(lives_visual_dict[lives])
        elif (guess in alphabet):
            guessed.append(guess)
            lives -= 1
            print(lives_visual_dict[lives])
        else:
            print(f"\n{guess} is not in the alphabet")
        print("\n=====================================================================")

    print("\nYOU LOSE!") if (lives == 0) else print("\nYOU WIN")
    print(f"\nCORRECT WORD: {word}")

play_hangman()


