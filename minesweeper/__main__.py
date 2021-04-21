from __future__ import annotations
from typing import List, Set, Tuple, Optional
import random

class Mine_Sweeper:
    def __init__(self, size: int = 10, bomb_count: Optional[int] = None):
        self.size: int = size
        self.bomb_count: int = bomb_count if bomb_count else size ** 2 // 10
        self.board: List[List[str]] = [[' ' for col in range(size)] for row in range(size)]
        self.dug: Set[Tuple[int, int]] = set()
        self.plant_bombs()

    def plant_bombs(self) -> Mine_Sweeper:
        planted_bombs: int = 0
        while planted_bombs < self.bomb_count:
            row: int = random.randint(0, self.size - 1)
            col: int = random.randint(0, self.size - 1)
            loc: Tuple[int, int] = (row, col)
            if not loc in self.dug:
                self.board[row][col] = '*'
                planted_bombs += 1
        return self

    def is_valid_loc(self, row: int, col: int) -> bool:
        return all([row in range(0, self.size), col in range(0, self.size)])

    def is_bomb(self, row: int, col: int) -> bool:
        return self.board[row][col] == '*'

    def sweep(self, loc: Tuple[int, int], count: int = 0) -> Mine_Sweeper:
        if loc in self.dug: return self

        neighbors: List[Tuple[int, int]] = []
        row: int = loc[0]
        col: int = loc[1]

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if self.is_valid_loc(r, c):
                    if self.is_bomb(r, c):
                        count += 1
                    else:
                        neighbors.append((r,c))

        self.board[row][col] = str(count)
        self.dug.add(loc)

        if count == 0:
            for neighbor in neighbors:
                self.sweep(neighbor)

        return self

    def dig_all(self) -> Mine_Sweeper:
        for r, row in enumerate(self.board):
            for c, col in enumerate(row):
                self.dug.add((r, c))
        return self

    def print(self) -> Mine_Sweeper:
        def pad(square: str) -> str: 
            return ' ' * (2 - len(square)) + square
        border: str = '   --' + '---' * self.size
        header: str = ' '.join([pad(str(i)) for i in range(self.size)])

        print('    ', header)
        print(border)
        for r, row in enumerate(self.board):
            row = [self.board[r][c] if (r, c) in self.dug else ' ' for c, col in enumerate(row)]
            row_as_str: str = ' |'.join(row)
            print(f'{pad(str(r))} ||{row_as_str} |')
        print(border)

        return self

def play() -> None:
    size: int = int(input('What size shall the board be? Max is 20 & Min is 4: '))
    if size > 20: size = 20
    if size < 4: size = 4
    game = Mine_Sweeper(size)

    done: bool = False
    safe: bool = True
    
    while not done and safe:
        game.print()
        valid_location = False
        row: int
        col: int
        while not valid_location:
            loc: str = input('Pick a location. Format is row,col (ex. 0,0): ').strip()
            row = int(loc[0])
            col = int(loc[-1])
            if (game.is_valid_loc(row, col)): valid_location = True
        if game.is_bomb(row, col):
            safe = False
        else:
            game.sweep((row, col))
            if len(game.dug) == size ** 2 - game.bomb_count: done = True
    
    game.dig_all().print()
    print('YOU HAVE WON') if safe else print('YOU HAVE LOST')

play()