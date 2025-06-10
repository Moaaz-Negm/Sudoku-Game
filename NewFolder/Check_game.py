def check_game(updated_matrix, correct_matrix): # function that checks the game
    
    strikes = 0 # variable strikes is set to zero
    
    if updated_matrix == correct_matrix: # conditions whether the updated matrix matches with the correct matrix
       
        print('Game correct')
    
    else:           # if the functions doesnt meet what is excpected, we go next to the strike counter(included with moaaz)
        strikes= strikes + 1            # adds a strike as soon as a mistake is made

    return strikes          # tells us at end how many strikes are made
