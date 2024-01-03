import termcolor


# (int, int) (int, int) -> boolean
# validate if the given coordinates can be found in the given board, both the coordiantes
def validate_coordinates(row, column, board_size):
    rows, columns = board_size
    return row in range(rows) and column in range(columns)


# (type, string) -> type
def validate_input(input_type, input_string, predicate=lambda _: True):
    try:
        val = input_type(input(input_string))
        if not predicate(val):
            raise Exception()
        return val
    except KeyboardInterrupt:
        raise KeyboardInterrupt("Program Terminated")
    except:
        print("Invalid Value, please try again")
        return validate_input(input_type, input_string, predicate)


def every(func, lst):
    if lst == []:
        return True
    return func(lst[0]) and every(func, lst[1:])


def some(func, lst):
    if lst == []:
        return False
    return func(lst[0]) or some(func, lst[1:])


def flat(lst):
    if not lst:  # lst is empty
        return []
    return [*lst[0], *flat(lst[1:])]


# T, str -> void
# given data of any type T, and a string that indicates a color, print the data with the given color
def print_colored(data, color):
    colored_text = colored(str(data), color=color)
    return colored_text
