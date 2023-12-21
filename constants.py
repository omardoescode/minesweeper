DIFFICULTIES = {
    1: "easy",
    2: "medium",
    3: "hard",
}

NUMBER_OF_MINES = {"easy": 10, "medium": 40, "hard": 99}

BOARD_SIZE = {
    "easy": (8, 8),
    "medium": (16, 16),
    "hard": (30, 16),
}
VALUE_COLORS = {
    1: "light_blue",
    2: "green",
    3: "light_red",
    4: "blue",
    5: "red",
    6: "cyan",
    7: "dark_grey",
    8: "light_grey",
}


COORDINATES_TRANSITIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 0),
    (-1, 1),
    (-1, -1),
]


say_welcome = lambda name: print(
    f"""Hola {name}! Welcome to the most exhilarating game ever crafted by the brilliant minds at ByteBusters. I go by the name Revolt, and my mission is to guide you through this thrilling adventure.

Before you dive in, let me equip you with the knowledge you need to conquer this challenge:

In each move, you must choose a row and column. The fate of the game rests in your hands as you decide whether to click or flag that chosen spot/cell.

Remember the symbols:
- X: Covered cell
- F: Flaged cell
- Numbers (0-8): Indicates neighboring mines
- M: You clicked a mine, and unfortunately, the game is lost.

To enter a command, it has to be in the following format: <row> <column> <f|opional>
Examples:
- 1 1: Click the cell with coordinates (1, 1)
- 1 1 f: Toggle the flag in the coordinates (1, 1)

Now, venture forth and may your clicks be true!
"""
)
