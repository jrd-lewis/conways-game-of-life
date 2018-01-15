import unittest
import random
import sys
sys.path.insert(0, "../")
from game import Game, Cell


class TestGame(unittest.TestCase):

    def setUp(self):
        self._game = Game()

    def test_canParseCells(self):
        self._game.setUp(randomGrid=True)
        self._game.parseCells()
        x = random.randint(0, self._game.columns - 1)
        y = random.randint(0, self._game.rows - 1)
        cell = self._game.grid[y][x]
        self.assertIsInstance(cell, Cell)

    def test_canGetNextState(self):
        self._game.setUp()
        self._game.parseCells()
        initialState = str(self._game)
        self._game.getNextState()
        currentState = str(self._game)
        print(currentState)
        self.assertNotEqual(initialState, currentState)

    def test_canRunAgain(self):
        self._game.setUp(randomGrid=True)
        self._game.parseCells()
        initialState = str(self._game)
        stateTwo = self._game.getNextState()
        stateThree = self._game.getNextState()
        self.assertNotEqual(initialState, stateTwo)
        self.assertNotEqual(stateTwo, stateThree)

    def test_canCustomizeGridSize(self):
        rows = 4
        columns = 4
        game = Game(rows=rows, columns=columns)
        game.setUp(randomGrid=True)
        self.assertEqual(len(game.grid), rows)
        randomRow = random.randint(0, rows - 1)
        randomCell = game.grid[randomRow][0]
        self.assertEqual(len(randomCell), columns)


if __name__ == '__main__':
    unittest.main()
