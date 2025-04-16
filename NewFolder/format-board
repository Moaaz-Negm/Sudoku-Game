def format_board(board):
        col_labels = "    A B C D E F G H I"
        lines = [col_labels]
        for i, row in enumerate(board):
            row_str = f"{i+1} | " + " ".join(str(x) for x in row)
            lines.append(row_str)
        return "\n".join(lines)

    puzzle_str = format_board(puzzle)
    solution_str = format_board(solution)
    
    return puzzle, solution
