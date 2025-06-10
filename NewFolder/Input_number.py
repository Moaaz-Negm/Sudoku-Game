def input_number(board, number, position):
    """
    Inputs a number into the specified position in a Sudoku board.

    Parameters:
    - board (np.ndarray): 9x9 Sudoku puzzle array
    - number (int): number to input (1–9)
    - position (list or tuple): [row, col] in 0-based index

    Returns:
    - np.ndarray: the modified board
    """
    row, col = position
    if not (0 <= row < 9 and 0 <= col < 9):
        raise ValueError("Row and column must be between 0 and 8.")
    if not (1 <= number <= 9):
        raise ValueError("Number must be between 1 and 9.")
    
    board[row, col] = number
    
    return board
