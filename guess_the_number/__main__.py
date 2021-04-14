import random

def user_guess_number(x):
    num = random.randint(1, x + 1)
    guess = None
    while guess != num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
    print(f"That's right! {num} is the correct number!! You're a genius!!!")

def computer_guess_number(x):
    low = 1
    high = x + 1
    guess = random.randint(low, high)
    guessed = None

    print(f"Think of a number between {low} and {x}.")

    while guessed != "Y":
        guessed = input(f"Is {guess} correct (Y), too high (H), or too low (L)? ").upper()
        if guessed == "H":
            high = guess
            guess = random.randint(low, high)
        elif guessed == "L":
            low = guess
            guess = random.randint(low, high)
        elif guessed != "Y":
            print("Please type either 'Y' for yes or 'N' for no.")

    print(f"The computer guessed your number, {guess}! Did you really think you could outsmart a computer!! Huh?! Did ya?!!")

def choose_game(x):
    game = None
    while game != "Y" and game != "C":
        game = input("Who does the guessing, you (Y) or the computer (C)? ").upper()
    user_guess_number(x) if game == "Y" else computer_guess_number(x)

choose_game(1000)
        
                
