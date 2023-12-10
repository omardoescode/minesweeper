# (int, int) (int, int) -> boolean
# validate if the given coordinates can be found in the given board, both the coordiantes
def validate_coordinates(row, column, board_size):
    pass

# (type, string) -> type
def validate_input(input_type, input_string): 
    try:
        return input_type(input(input_string))
    except ValueError:
        print("Invalid Value, please try again")
        return validate_input(type, input_string)
