def print_board(board):
    """
    Print the tic-tac-toe board.

    Parameters:
    - board (list): The 3x3 tic-tac-toe board represented as a nested list.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the tic-tac-toe board.

    Parameters:
    - board (list): The 3x3 tic-tac-toe board represented as a nested list.

    Returns:
    - bool: True if there is a winner, False otherwise.
    """
    # Check rows and columns
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] != " ") or \
           (board[0][i] == board[1][i] == board[2][i] != " "):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] != " ") or \
       (board[0][2] == board[1][1] == board[2][0] != " "):
        return True

    return False

def tic_tac_toe():
    """
    Play a game of tic-tac-toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if (row not in range(3)) or (col not in range(3)):
                raise ValueError("Invalid row or column index!")
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError as e:
            print("Error:", e)

# Start the tic-tac-toe game
tic_tac_toe()

