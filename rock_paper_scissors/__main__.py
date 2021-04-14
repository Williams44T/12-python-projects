import random

moves = {
    "r": "ROCK",
    "p": "PAPER",
    "s": "SCISSORS",
}

def player_won(p, c):
    return (p == 'r' and c == 's') \
        or (p == 'p' and c == 'r') \
        or (p == 's' and c == 'p')

def play_game():
    player = input("Choose: Rock(R), Paper(P), or Scissors(S): ").lower()
    computer = random.choice(['r', 'p', 's'])
    if (player == computer): 
        print(f"   Draw! Both players chose {moves[player]}")
        return "tie"
    if (player_won(player, computer)):
        print(f"   {moves[player]} beats {moves[computer]}! You win!!")
        return "win"
    else:
        print(f"   {moves[computer]} beats {moves[player]}! You lose!!")
        return "lose"

def begin_games():
    player_wins = 0
    computer_wins = 0
    draws = 0
    count = int(input("How many games of rock-paper-scissors shall we play? "))
    for i in range(count):
        result = play_game()
        if (result == 'tie'): draws += 1
        elif (result == 'win'): player_wins += 1
        else: computer_wins += 1
        print(f"     You: {player_wins}, Me: {computer_wins}, Draws: {draws}")
        if (i < count - 1): print(f"     {count - (i + 1)} more game(s) remaining")

    if (player_wins == computer_wins):
        print("DRAW!")
    elif (player_wins > computer_wins):
        print("YOU WIN!!")
    else:
        print("YOU LOSE!!")

begin_games()




