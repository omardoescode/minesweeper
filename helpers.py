# (int, int) (int, int) -> boolean
# validate if the given coordinates can be found in the given board, both the coordiantes
def validate_coordinates(row, column, board_size):
    rows, columns = board_size
    
    if row in range(rows) and column in range(columns):
        return True
    else:
        return False

# (type, string) -> type
def validate_input(input_type, input_string): 
    try:
        return input_type(input(input_string))
    except ValueError:
        print("Invalid Value, please try again")
        return validate_input(type, input_string)
