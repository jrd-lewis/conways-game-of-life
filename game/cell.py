import random
try:
    from game.defaults import STATES, PY_3
except ImportError:
    from defaults import STATES, PY_3


class Cell(object):
    """Wrapper for a given Cell in the grid"""

    def __init__(self, x, y, value, **kwargs):
        self.states = kwargs.get('states', STATES)
        self.rows = kwargs.get('rows', 6)
        self.columns = kwargs.get('columns', 8)
        assert(x < self.columns)
        self.x = x  # Column Number
        assert(y < self.rows)
        self.y = y  # Row Number
        self.coords = [y, x]
        self.output = value
        self.state = self.parseState(value)
        self.neighbors = self.getNeighbors()

    def __str__(self):
        return self.output

    def parseState(self, value=None):
        if not value:
            self.state = self.states.get(self.output, '')
            return self.state
        return self.states[value]

    def setState(self, value):
        for output, state in self.states.items():
            if state == value:
                self.output = output

    def getNeighbors(self):
        neighbors = []
        if PY_3:
            rows = range(self.rows)
            columns = range(self.columns)
        else:
            rows = xrange(self.rows)
            columns = xrange(self.columns)
        # All horizontal adjacent cells
        for x in columns:
            cell = [self.y, x]
            if x != self.x and x in [self.x - 1, self.x + 1]:
                neighbors.append(cell)
        # All vertical adjacent cells
        for y in rows:
            cell = [y, self.x]
            if y != self.y and y in [self.y - 1, self.y + 1]:
                neighbors.append(cell)
        # All diagonal adjacent cells
        for y in rows:
            for x in columns:
                cell = [y, x]
                if x in [self.x - 1, self.x + 1] and y in [self.y - 1, self.y + 1]:
                    neighbors.append(cell)
        return neighbors
