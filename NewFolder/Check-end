def check_end (upt_game, correct_Matrix):
    
    if strikes >= Max_Strikes:
        return 'Lost' # max strikes reached game ends
    for row in range(9):
        for col in range(9):
            num = upt_game [row] [col]
            
            if num != correct_Matrix[row][col]:
            
                return 'incorrect value(s) present'
        break
    else:
        return 'won, game ended'
