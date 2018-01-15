import unittest
import sys
sys.path.insert(0, "../")
from game import Cell


class TestCell(unittest.TestCase):

    def setUp(self):
        self._cell = Cell(1, 1, '.')

    def test_hasState(self):
        self.assertIsNotNone(self._cell.state)

    def test_hasNeighbors(self):
        neighbors = self._cell.getNeighbors()
        self.assertGreaterEqual(len(neighbors), 1)
        self.assertLessEqual(len(neighbors), 8)


if __name__ == '__main__':
    unittest.main()
