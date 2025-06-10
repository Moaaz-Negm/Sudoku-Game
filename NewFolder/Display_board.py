def display_board(board):
    # Loop through each row in the board
    for i in range(9):
        # Add a horizontal separator every 3 rows, except at the top
        if i % 3 == 0 and i != 0:
            print("-" * 21) 

        # Loop through each column in the row
        for j in range(9):
            # Add a vertical separator every 3 columns, except at the start
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            # Print the number with spacing, no newline yet
            if j == 8:
                # At the end of the row, print the last number and move to the next line
                print(board[i][j])
            else:
                # Print the number followed by a space, stay on the same line
                print(str(board[i][j]) + " ", end="")
