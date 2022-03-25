from enum import Enum
import random
from typing import List, NamedTuple


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9, 9)) -> None:
        # initialize basic instance variables
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # fill the grid with empty cells
        self._grid: List[List[Cell]] = [
            [Cell.EMPTY for c in range(columns)]for r in range(rows)]
        self.__random_fill_block_grid(sparseness=sparseness)

    def __random_fill_block_grid(self, sparseness) -> None:
        '''Generate Randome Block In Grid'''
        for row in range(self._rows):
            for column in range(self._columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def goal_check(self, maze_location: MazeLocation) -> bool:
        return maze_location == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        possible_directions = [
            (ml.row-1 > -1 and self._grid[ml.row-1][ml.column] !=
             Cell.BLOCKED, MazeLocation(ml.row-1, ml.column)),  # left
            (ml.row+1 < self._rows and self._grid[ml.row+1][ml.column] !=
             Cell.BLOCKED, MazeLocation(ml.row+1, ml.column)),  # right
            (ml.column+1 < self._columns and self._grid[ml.row][ml.column+1] !=
             Cell.BLOCKED, MazeLocation(ml.row, ml.column+1)),  # up
            (ml.column-1 > -1 and self._grid[ml.row][ml.column-1] !=
             Cell.BLOCKED, MazeLocation(ml.row, ml.column-1))  # down
        ]
        for check, location in possible_directions:
            if check:
                locations.append(location)
        return locations

    def __repr__(self) -> str:
        output_str: str = ''
        for row in self._grid:
            output_str += "".join([c.value for c in row]) + "\n"
        return output_str


def main():
    maze: Maze = Maze()


if __name__ == '__main__':
    main()
