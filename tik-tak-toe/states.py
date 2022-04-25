from dataclasses import dataclass
from enum import Enum



class GameStateChoice(Enum):
    idle = 0
    x_turned = 1
    o_turned = 2
    x_won = 3
    o_won = 4


class BoardStateChoice(Enum):
    x = 'x'
    o = 'o'
    n = None


Position = int[0, 1, 2]


class State:
    def __init__(self):
        self._board_state: list[BoardStateChoice] = [BoardStateChoice.n for _ in range(9)]
        self._game_state: GameStateChoice = GameStateChoice.idle
        self._game_state_board_state_map = {
            BoardStateChoice.x: GameStateChoice.x_turned,
            BoardStateChoice.o: GameStateChoice.o_turned,
        }
        self._turn_state_won_state_map = {
            GameStateChoice.x_turned: GameStateChoice.x_won,
            GameStateChoice.o_turned: GameStateChoice.o_won,
        }
        self._possible_pathes = {
            0: [(0,3,6), (0,1,2), (0,4,8)],
            1: [(0,1,2), (1,4,7)],
            2: [(0,1,2), (2,4,6), (2,5,8)],
            3: [(0,3,6), (3,4,5)],
            4: [(0,4,8), (1,4,7), (2,4,6), (3,5,4)],
            5: [(2,5,8), (3,4,5)],
            6: [(0,3,6), (6,7,8)],
            7: [(1,4,7), (6,7,8)],
            8: [(0,4,8), (6,7,8),(2,5,8)],
        }


    def mark_position(self, x:Position, y:Position, choice:BoardStateChoice):
        if choice == choice.n:
            raise ValueError
        
        if self._game_state in (GameStateChoice.o_won, GameStateChoice.x_won):
            return
        
        offset = self._calculate_offset(x,y)
        self._board_state[offset] = choice
        self._game_state = self._game_state_board_state_map[choice]
        self._calculate_finished_state(offset)


    def get_mark_by_position(self, x:Position, y:Position) -> BoardStateChoice:
        offset = self._calculate_offset(x,y)
        return self._board_state[offset]


    def get_game_state(self):
        return self._game_state


    def _calculate_offset(self, x:Position, y:Position) -> int:
        offset = x*3+y
        if offset < len(self._board_state):
            return offset
        raise IndexError


    def _calculate_finished_state(self, current_position):
        last_turn = self._game_state
        for path in self._possible_pathes[current_position]:
            i = 0
            for position in path:
                if last_turn == self._board_state[position]:
                    i += 1
            if i == 2:
                self._game_state = self._turn_state_won_state_map(self._game_state)
                break
