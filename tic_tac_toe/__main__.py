from game import TicTacToe
from players import Human, Computer
import random, time

def play_game(player, computer, game):

    # pick first player
    current = random.choice([player, computer])
    print(f'{current.name}("{current.letter}") will go first\n')

    # play game
    winner = None
    game.print_board()
    while not winner and len(game.available) > 0:
        square = current.get_move(game)
        game.place_move(current.letter, square)
        print(f'{current.name} places an "{current.letter}" in square {square + 1}\n')
        game.print_board()
        time.sleep(0.8)
        if game.winner: 
            winner = current
        else:
            current = player if current == computer else computer

    # display results
    print(f'{winner.name} won the game!\n') if winner else print('Draw! How surprising.\n')

    # ask for another game
    play_again = ''
    while play_again != 'Y' and play_again != 'N':
        play_again = input('Play again? (Y/N) ').upper()
    if play_again == 'Y': setup_game()

def setup_game():

    # determine versus human or versus computer
    play_against_comp = ''
    while not play_against_comp in ['Y', 'N']:
        play_against_comp = input('\nDo you want to play against the computer? (Y/N) ').upper()
    computer = True if play_against_comp == 'Y' else False

    # choose letters
    letter1 = ''
    name1 = input('Player 1, what shall we call you? ')
    name2 = ''
    if not computer: name2 = input('Player 2, What shall we call you? ')
        
    while not letter1 in ['X', 'O']:
        letter1 = input(f'{name1}, which letter do you want to be, X or O?: ').upper()
    letter2 = 'X' if letter1 == 'O' else 'O'

    # init game
    player1 = Human(letter1, name1)
    player2 = Computer(letter2) if computer else Human(letter2, name2)
    play_game(player1, player2, TicTacToe())

setup_game()


    