import random, math

class Human():
    def __init__(self, letter, name):
        self.letter = letter
        self.name = name

    def get_move(self, game):
        spot = None
        while not spot in game.available:
            spot = int(input(f'{self.name}, choose an available spot: ')) - 1
        return spot

class Computer():
    def __init__(self, letter):
        self.letter = letter
        self.name = 'Computer'
        self.opponent = 'O' if letter == 'X' else 'X'

    def minimax(self, state, letter):
        if state.winner:
            score = len(state.available) + 1
            if state.winner == self.opponent: score *= -1
            return { 'score': score }
        elif len(state.available) == 0:
            return { 'score': 0 }

        best = { 'score': -math.inf if letter == self.letter else math.inf }
        next_letter = 'O' if letter == 'X' else 'X'

        for spot in state.available.copy():
            state.place_move(letter, spot)
            sim = self.minimax(state, next_letter)
            sim['spot'] = spot
            if letter == self.letter and sim['score'] > best['score']:
                best = sim
            elif letter == self.opponent and sim['score'] < best['score']:
                best = sim
            state.reverse_move(letter, spot)

        return best

    def get_move(self, game):
        if len(game.available) == 9: # if first move
            return random.choice(game.available)
        else:
            return self.minimax(game, self.letter)['spot']
