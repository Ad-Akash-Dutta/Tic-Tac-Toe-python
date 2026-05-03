def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    # All 8 possible winning combinations (3 rows, 3 columns, 2 diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe():
    # Step 1: Initialize the board with numbers 1-9 so players know where to type
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    moves_made = 0

    print("Welcome to Tic-Tac-Toe!")
    
    while moves_made < 9:
        display_board(board)
        
        try:
            choice = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
            
            # Step 2: Validate the move
            if choice < 0 or choice > 8 or board[choice] in ["X", "O"]:
                print("Invalid move! That spot is taken or out of range. Try again.")
                continue
            
            # Step 3: Update the board
            board[choice] = current_player
            moves_made += 1
            
            # Step 4: Check if the current move won the game
            if check_win(board, current_player):
                display_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                return

            # Step 5: Switch players
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

    display_board(board)
    print("It's a draw!")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()