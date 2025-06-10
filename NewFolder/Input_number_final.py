def input_number_final(board):
    
    display_board(board)
    
    print("Enter your move (row column number) or 'q' to quit:")
    user_input = input().strip()
    if user_input.lower() == 'q':
        print("Thanks for playing!")
          
    try:
            row, col, num = map(int, user_input.split())
            if board[row][col] == 0:
                board[row][col] = num
                display_board(board)
            else:
                print("Cell is already filled!")
    
    
    
    except (ValueError, IndexError):
    
        print("Invalid input. Please enter as: row col num (0-indexed)")
