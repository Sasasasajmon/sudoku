import numpy as np


def get_sudoku_board(input_str):
    input_format = ' '.join(digit for digit in input_str)
    return np.fromstring(input_format, dtype=int, sep=' ').reshape(9, 9)


def get_next_empty_cell(board):
    empty_cells = np.where(board == 0)
    if empty_cells[0].size != 0:
        return empty_cells[0][0], empty_cells[1][0]
    return None


def validate_new_value(board, value, row, col):
    is_row_valid = True if np.count_nonzero(board[row] == value) == 0 else False
    is_column_valid = True if np.count_nonzero(board[:, col] == value) == 0 else False
    smallsquare = get_smallsquare_list_for_value(board, row, col)
    is_smallsquare_valid = True if np.count_nonzero(smallsquare == value) == 0 else False

    return is_row_valid and is_column_valid and is_smallsquare_valid


def get_smallsquare_list_for_value(sudoku_matrix, row, col):
    square_code = [row // 3, col // 3]
    square_row_border = square_code[0] * 3
    square_col_border = square_code[1] * 3
    smallsquare_list = sudoku_matrix[square_row_border: square_row_border + 3,
                       square_col_border: square_col_border + 3].flatten()
    return smallsquare_list


def solve_sudoku(sudoku_board):
    empty_cell_coords = get_next_empty_cell(sudoku_board)
    if empty_cell_coords is None:
        print(sudoku_board)
        return True

    for digit in range(1, 10):
        is_digit_valid = validate_new_value(sudoku_board, digit, *empty_cell_coords)
        if is_digit_valid:
            sudoku_board[empty_cell_coords] = digit

            if solve_sudoku(sudoku_board):
                return True

            sudoku_board[empty_cell_coords] = 0

    return False


if __name__ == '__main__':
    example_sudoku = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
    example_sudoku_solution = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'

    sudoku = get_sudoku_board(example_sudoku)
    true_solution = get_sudoku_board(example_sudoku_solution)
    print(sudoku)
    print('--------------------------')
    solved_board = solve_sudoku(sudoku)

