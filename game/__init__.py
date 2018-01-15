__all__ = ['defaults', 'cell', 'game']

try:
    from game.defaults import STATES, PY_3
    from game.game import Game
    from game.cell import Cell
except ImportError:
    from defaults import STATES
    from game import Game
    from cell import Cell
