import random
try:
    from game.defaults import STATES, PY_3
    from game.cell import Cell
except ImportError:
    from defaults import STATES, PY_3
    from cell import Cell


class Game(object):
    """docstring for Game"""

    def __init__(self, **kwargs):
        self.rows = kwargs.get('rows', 6)
        self.columns = kwargs.get('columns', 8)
        self.states = kwargs.get('states', STATES)
        self.grid = []

    def __str__(self):
        output = ''
        for y, row in enumerate(self.grid):
            for cell in row:
                output += str(cell)
            if y == self.rows - 1:
                break
            else:
                output += '\n'
        return output

    def setUp(self, randomGrid=False):
        if PY_3:
            rows = range(self.rows)
            columns = range(self.columns)
        else:
            rows = xrange(self.rows)
            columns = xrange(self.columns)
        if randomGrid:
            states = list(self.states.keys())
            for y in rows:
                row = ['']
                for x in columns:
                    choice = random.choice(states)
                    row[0] += choice
                self.grid.append(row)
        else:
            self.grid = []
            print('Input your grid.')
            while True:
                for y in rows:
                    row = []
                    while True:
                        if PY_3:
                            rowInput = input('Row %s: ' % (y + 1))
                        else:
                            rowInput = raw_input('Row %s: ' % (y + 1))
                        if len(rowInput) == self.columns:
                            break
                        else:
                            print('Row length (%s) does not match required length (%s).' % (len(rowInput), self.columns))
                    row.append(rowInput)
                    self.grid.append(row)
                break

    def parseCells(self, setup=True, **kwargs):
        if not setup:
            grid = kwargs.get('grid', self.grid)
            for y, row in enumerate(grid):
                for x, cell in enumerate(row):
                    cell.parseState()
        else:
            for y, row in enumerate(self.grid):
                self.grid[y] = []
                for x, state in enumerate(row[0]):
                    cell = Cell(x, y, state, columns=self.columns, rows=self.rows)
                    self.grid[y].append(cell)

    def getNextState(self):
        nextState = self.grid

        for row in nextState:
            for cell in row:
                neighbors = cell.neighbors
                liveNeighbors = []
                # Loop through of the cell's neighbors
                for coords in sorted(neighbors):
                    y = coords[0]
                    x = coords[1]
                    # Lookup each neighbor's state from the grid
                    neighbor = self.grid[y][x]
                    if neighbor.state == 'alive':
                        liveNeighbors.append(neighbor.coords)

                if cell.state == 'alive':
                    # Check rules for live cells
                    if len(liveNeighbors) < 2:
                        # Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
                        cell.setState('dead')
                    elif len(liveNeighbors) > 3:
                        # Any live cell with more than three live neighbors dies, as if by overcrowding.
                        cell.setState('dead')
                    elif len(liveNeighbors) in [2, 3]:
                        # Any live cell with two or three live neighbors lives on to the next generation.
                        cell.setState('alive')
                elif cell.state == 'dead' and len(liveNeighbors) == 3:
                    # Any dead cell with exactly three live neighbors becomes a live cell.
                    cell.setState('alive')
        self.parseCells(setup=False, grid=nextState)
        self.grid = nextState
        return str(self)
