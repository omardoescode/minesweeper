DIFFICULTIES = {
    1: 'easy',
    2: 'medium',
    3: 'hard',
}
NUMBER_OF_MINES = {
    "easy":10,
    "medium": 40,
    "hard": 99
}

BOARD_SIZE = {
    "easy": (8, 8),
    "medium": (16, 16),
    "hard": (30, 16),
}

COORDINATES_TRANSITIONS = [(0,1), (0,-1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]

WELCOME_MESSAGE = """Hola! Welcome to the most exhilarating game ever crafted by the brilliant minds at ByteBusters. I go by the name Revolt, and my mission is to guide you through this thrilling adventure.

Before you dive in, let me equip you with the knowledge you need to conquer this challenge:

In each move, you must choose a row and column. The fate of the game rests in your hands as you decide whether to click or flag that chosen spot/cell.

Remember the symbols:
- X: Covered cell
- F: Flaged cell
- Numbers (0-8): Indicates neighboring mines
- M: You clicked a mine, and unfortunately, the game is lost.

Remember, clicking on a covered cell is only safe if the number of flags surrounding it matches the indicated number. Stay vigilant!

But beware, my friend, for the treacherous mines lie in wait. A single misstep, a click on the wrong spot, and it's game over. Choose your moves wisely, and let your strategic prowess shine.

Now, venture forth and may your clicks be true!
"""