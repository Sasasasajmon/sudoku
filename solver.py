import numpy as np


def get_sudoku_object(input_str):
    input_format = ' '.join(digit for digit in input_str)
    return np.fromstring(input_format, dtype=int, sep=' ').reshape(9, 9)


def validate_new_value(sudoku_matrix, row, col):
    value = sudoku_matrix[row][col]
    is_row_valid = True if np.count_nonzero(sudoku_matrix[row] == value) == 1 else False
    is_column_valid = True if np.count_nonzero(sudoku_matrix[:, col] == value) == 1 else False
    smallsquare = get_smallsquare_list_for_value(sudoku_matrix, row, col)
    is_smallsquare_valid = True if np.count_nonzero(smallsquare == value) == 1 else False

    return is_row_valid and is_column_valid and is_smallsquare_valid


def get_smallsquare_list_for_value(sudoku_matrix, row, col):
    square_code = [row // 3, col // 3]
    square_row_border = square_code[0] * 3
    square_col_border = square_code[1] * 3
    smallsquare_list = sudoku_matrix[square_row_border: square_row_border + 3,
                                     square_col_border: square_col_border + 3].flatten()
    return smallsquare_list


example_sudoku = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'

sudoku = get_sudoku_object(example_sudoku)
print(sudoku)
print(validate_new_value(sudoku, 0, 0))
sudoku[0, 0] = 5
print(validate_new_value(sudoku, 0, 0))
