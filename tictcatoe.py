def print_board(board):
    print('\n-------------')
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print('-------------')


def check(board):
    win_cond = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_cond:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False


def game():
    board = [' ']*9
    player_1 = "X"
    player_2 = "O"
    for i in range(9):
        print_board(board)
        move = int(input(f"Ход игрока {player_1} (1-9): ")) - 1
        board[move] = player_1
        if check(board):
            print_board(board)
            print(f"Победа игрока {player_1}!")
            break
        player_1, player_2 = player_2, player_1
    else:
        print_board(board)
        print("Ничья")


game()