import sys
from game import Game

title = ' Conway\'s Game of Life '
print(title)
print(('-' * len(title)))

while True:
    customSize = input('Do you want to customize the grid size? (Y / N) ')
    sizeResult = customSize.lower()
    if sizeResult in ['n', 'y']:
        break
    else:
        print('Invalid input. Please try again.')

# Initialize Game
if sizeResult == 'y':
    while True:
        try:
            rows = input('Number of rows? ')
            rows = int(rows)
        except ValueError:
            print('Unexpected value. Please try again.')
        else:
            break

    while True:
        try:
            columns = input('Number of columns? ')
            columns = int(columns)
        except ValueError:
            print('Unexpected value. Please try again.')
        else:
            break

    game = Game(rows=rows, columns=columns)
else:
    game = Game()

# Setup grid
while True:
    randomGrid = input('Randomize initial grid? (Y / N) ')
    gridResult = randomGrid.lower()
    if gridResult in ['n', 'y']:
        break
    else:
        print('Invalid input. Please try again.')

# Setup initial state
if gridResult == 'n':
    game.setUp()
else:
    game.setUp(randomGrid=True)
game.parseCells()
print('\nInitial State:\n%s' % game)

# Get next state
game.getNextState()
print('\nNew State:\n%s' % game)

# Check if user wants to quit
while True:
    quitGame = input('\nDo you want to quit? (Y / N) ')
    quitResult = quitGame.lower()
    if quitResult in ['n', 'y']:
        if quitResult == 'n':
            game.getNextState()
            print('\nNext State:\n%s' % game)
        else:
            break
    else:
        print('Invalid input. Please try again.')

# End the game
sys.exit(0)
