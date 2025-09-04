#!/usr/biin/python3
def print_board(board):
    """
    Print the current state of the Tic Tac Toe board.

    Parameters:
        board (list of list of str): A 3x3 matrix representing the game board.

    Returns:
        None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Check if a player has won the game.

    Parameters:
        board (list of list of str): A 3x3 matrix representing the game board.

    Returns:
        bool: True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_draw(board):
    """
    Check if the game board is full and there is no winner (i.e., a draw).

    Parameters:
        board (list of list of str): A 3x3 matrix representing the game board.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Run a two-player Tic Tac Toe game in the console.

    Returns:
        None
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"\nPlayer {player}'s turn.")

        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid coordinates. Please enter values between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = player

            if check_winner(board):
                print_board(board)
                print(f"\nPlayer {player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("\nIt's a draw!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter numeric values.")


# Run the game
if __name__ == "__main__":
    tic_tac_toe()

