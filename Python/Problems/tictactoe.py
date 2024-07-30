import random


def draw_board(spaces):
    
    
    print(f"     |     |     ")
    print(f"  {spaces[0]}  |  {spaces[1]}  |  {spaces[2]}  ")
    print(f"_____|_____|_____")
    print(f"     |     |     ")
    print(f"  {spaces[3]}  |  {spaces[4]}  |  {spaces[5]}  ")
    print(f"_____|_____|_____")
    print(f"     |     |     ")
    print(f"  {spaces[6]}  |  {spaces[7]}  |  {spaces[8]}  ")
    print(f"     |     |     \n")
    
    return spaces

def get_user_input(spaces):

    while True:
        symbol = 'X'
        user_input = int(input("Enter 1-9 (top left to bottom right): ")) - 1
        if user_input >= 0 and user_input <= 8:
            if spaces[user_input] != " ":  
                print("Space taken!")
            else:
                spaces[user_input] = 'X'
                break

    return spaces

def get_computer_input(spaces):

    symbol = 'O'
    while True:
        user_input = random.randint(0,8)
        if spaces[user_input] == ' ':
            spaces[user_input] = symbol
            break
    return spaces

def check_win(spaces):
    
    win_conditions = {(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)}
    
    for combination in win_conditions:
        s1,s2,s3 = combination
        
        if spaces[s1] == "X" and spaces[s2] == "X" and spaces[s3] == "X":
            print("You wiN!")
            return True
        
        elif spaces[s1] == "O" and spaces[s2] == "O" and spaces[s3] == "O":
            print("You Lose!")
            return True
        
    # if spaces[0] == "X" and spaces[0] == spaces[1] and spaces[0] == spaces[2]:
    #     print("You win!")
    # elif spaces[0] == "O" and spaces[0] == spaces[1] and spaces[0] == spaces[2]:
    #     print("You lose!")
    
    return False

def check_draw(spaces):
    for space in spaces:
        if space == " ":
            return False
    print("It's a draw!")
    return True

def main():
    """
    draw the board
    get the user input,
    draw_board
    check_win
    get the computer input
    draw_board
    check_win 
    """
    playing = True
    draw = False
    spaces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while playing:
        draw_board(spaces)
        
        # user block
        spaces = get_user_input(spaces)
        draw_board(spaces)
        is_win = check_win(spaces)
        is_draw = check_draw(spaces)
        
        if is_win or is_draw:
            play_again = input("Would you like to play again (y,n): ")
            if play_again == "y" or play_again == "Y": 
                playing = True
                spaces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
            elif play_again == "n" or play_again == "N": 
                playing = False
                print("Thanks for playing!")
            else:
                print("You typed incorrectly, so we're quitting")
            
        # computer block
        spaces = get_computer_input(spaces)
        draw_board(spaces)
        is_win = check_win(spaces)
        is_draw = check_draw(spaces)
        
        
        if is_win or is_draw:
            play_again = input("Would you like to play again (y,n): ")
            if play_again == "y" or play_again == "Y": 
                playing = True
                spaces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
            elif play_again == "n" or play_again == "N": 
                playing = False
                print("Thanks for playing!")
            else:
                print("You typed incorrectly, so we're quitting")
    return

if __name__ == "__main__":
    
    main()
    