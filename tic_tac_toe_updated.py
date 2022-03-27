import random
board_play = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']] #starting list that represents a blank board that's global
end_game = False
win = False # this variable will be used in case either the player wins or the computer wins to ask if another game if requested
def display_board(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] + '   |   ' + board [0][1] + '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] + '   |   ' + board [1][1] + '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] + '   |   ' + board [2][1] + '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

# The function accepts the board's current status, asks the user about their move, 
# checks the input, and updates the board according to the user's decision:
def enter_move(board):
    win = False #reset win to zero in case a game just ended and another game was requested afterwards
    flag = False #Dummy variable to keep looping until either a good move is made or the player stops the game
    while flag == False:
        try:
            move = int(input('Enter the square you would like to take, or -1 to end the game: '))
        except:
            print('Please enter the digit of an available square.')
        if move < -1 or move > 9 or move == 0:
            print('Please choose a square number between 1 and 9')
        elif move == -1:
            print('You\'ve ended the game')
            global end_game
            end_game = True
            break
        elif board[(move-1)//3][(move - 1) % 3] == 'O' or board[(move-1)//3][(move - 1) % 3] == 'X':
            print('That square is already chosen. Please choose another: ')
        else: #if a good move is indeed made:
            #print(move)
            board[(move-1)//3][(move - 1) % 3] = 'O'
            display_board(board)
            flag = True
    
# The function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers:
def make_list_of_free_fields(board):
    lst_free_fields = []
    for row in board:
        for square in row:
            if square != 'O' and square != 'X':
                free_field = ((int(square)-1)//3, (int(square) - 1) % 3)
                lst_free_fields.append(free_field) 
    #print(lst_free_fields)
    return (lst_free_fields)
#print(make_list_of_free_fields(board_new))
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

# The function analyzes the board's status in order to check if 
# the player using 'O's or 'X's has won the game:
def victory_for(board, sign):
    global win #in case a victory occurs, this will be recognized outside of this function
    if sign == 'O':
        vertically = horizontally = diagonally = 0 #set variables about method of winning to zero for now
        #see if any methods of victory have been achieved by the player:
        if (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
            vertically = 1
        if (board[0][0] == board[0][1] == board[0][2] == sign) or (board[1][0] == board[1][1] == board[1][2] == sign) or (board[2][0] == board[2][1] == board[2][2] == sign):
            horizontally = 1
        if (board[0][0] == board[1][1] == board[2][2] == sign) or (board[2][0] == board[1][1] == board[0][2] == sign):
            diagonally = 1
        # print(vertically)
        # print(horizontally)
        # print(diagonally)
        
        #if exactly one victory method is achieved:
        if vertically + horizontally + diagonally > 0 and vertically + horizontally + diagonally < 2:
            statement = 'You win '
            if vertically == 1:
                statement = statement + 'vertically'
            if horizontally == 1:
                statement = statement + 'horizontally'
            if diagonally == 1:
                statement = statement + 'diagonally'
            print(statement + '.')
            
        #if more than one victory method is achieved:
        if vertically + horizontally + diagonally > 1:
            statement = 'You win '
            if vertically == 1:
                statement = statement + 'vertically '
                if horizontally == 1:
                    statement = statement + 'and horizontally '
                if diagonally == 1:
                    statement = statement + 'and diagonally'
            elif horizontally == 1:
                statement = statement + 'horizontally '
                if diagonally == 1:
                    statement = statement + 'and diagonally'
            print(statement + '.')
        
        #set win to be True so it the program afterwards can proceed accordingly:
        if vertically + horizontally + diagonally > 0:
            win = True
            
    if sign == 'X':
        vertically = horizontally = diagonally = 0 #set variables about method of winning to zero for now
        #see if any methods of victory have been achieved by the computer:
        if (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
            vertically = 1
        if (board[0][0] == board[0][1] == board[0][2] == sign) or (board[1][0] == board[1][1] == board[1][2] == sign) or (board[2][0] == board[2][1] == board[2][2] == sign):
            horizontally = 1
        if (board[0][0] == board[1][1] == board[2][2] == sign) or (board[2][0] == board[1][1] == board[0][2] == sign):
            diagonally = 1
        # print(vertically)
        # print(horizontally)
        # print(diagonally)
        
        #if exactly one method of victory is achieved by the computer:
        if vertically + horizontally + diagonally > 0 and vertically + horizontally + diagonally < 2:
            statement = 'The computer wins '
            if vertically == 1:
                statement = statement + 'vertically'
            if horizontally == 1:
                statement = statement + 'horizontally'
            if diagonally == 1:
                statement = statement + 'diagonally'
            print(statement)
            
        #if more than one method of victory is achieved by the computer:      
        if vertically + horizontally + diagonally > 1:
            statement = 'The computer wins '
            if vertically == 1:
                statement = statement + 'vertically '
                if horizontally == 1:
                    statement = statement + 'and horizontally '
                if diagonally == 1:
                    statement = statement + 'and diagonally'
            elif horizontally == 1:
                statement = statement + 'horizontally '
                if diagonally == 1:
                    statement = statement + 'and diagonally'
            print(statement)
        
        #set win to be True so it the program afterwards can proceed accordingly:
        if vertically + horizontally + diagonally > 0:
            win = True
#victory_for(board_play, 'X')
    


# The function draws the computer's move and updates the board.
#It is more efficient to choose randomly from available fields than to randomly choosing from the board
#and then filtering to see if it was an available move:
def draw_move(board):
    win = False
    x =  make_list_of_free_fields(board)
    #print(x)
    computer_move = random.choice(x)
    #print(computer_move)
    board[computer_move[0]][computer_move[1]] = 'X'
    print('Here is the board after the computer\'s move:')
    #print(board)
# print(board_play)

#Here is the game in action:
print('Welcome to Tic-Tac_Toe!')
while end_game == False:
    display_board(board_play) #Display the board
    enter_move(board_play) # Player enters a move
    victory_for(board_play, 'O') # Check for player victory
    
    #If player did win:
    if win == True:
        again = input('Would you like to play again? Enter yes or y to play again: ').lower
        if again == 'yes' or 'y':
            print('OK, here is another round!')
            board_play = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            win = False
            continue #Need to have the 'continue' entries within the while loop, and not explicitly in the functions only!
        else: 
            print('Good game! Thanks for playing')
            quit()

    if len(make_list_of_free_fields(board_play)) == 0: # If there is no winner and there are no more available spots
        print('This game is a tie')
        again = input('Would you like to play again? Enter yes or y to play again: ').lower
        if again == 'yes' or 'y':
            print('OK, here is another round!')
            board_play = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            continue #Need to have the 'continue' entries within the while loop, and not explicitly in the functions only!
        else: 
            print('Good game! Thanks for playing')
            quit()
        
    draw_move(board_play) # Computer enters a move
    victory_for(board_play, 'X') # Check for computer victory
    
    #If computer did win:
    if win == True:
        again = input('Would you like to play again? Enter yes or y to play again: ').lower
        if again == 'yes' or 'y':
            print('OK, here is another round!')
            board_play = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            win = False
            continue #Need to have the 'continue' entries within the while loop, and not explicitly in the functions only!
        else: 
            print('Good game! Thanks for playing')
            quit()