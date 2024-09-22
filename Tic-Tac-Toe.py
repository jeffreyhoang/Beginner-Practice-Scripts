gameboard = [" ", "|", " ", "|", " ",
             "-", "+", "-", "+", "-",
             " ", "|", " ", "|", " ",
             "-", "+", "-", "+", "-",
             " ", "|", " ", "|", " "]


# print gameboard
def print_board(board):
    for x in range(5):
        print(board[x], end=" ")
    print("")
    for x in range(5, 10):
        print(board[x], end=" ")
    print("")
    for x in range(10, 15):
        print(board[x], end=" ")
    print("")
    for x in range(15, 20):
        print(board[x], end=" ")
    print("")
    for x in range(20, 25):
        print(board[x], end=" ")
    print("")


# take player input and insert character
def player_input(board, player):
    index = int(input("Enter a move (1-9): "))
    while index < 1 or index > 9 or not valid_index(board, index):
        print(str(index) + " is not a valid index")
        index = int(input("Enter a move (1-9): "))
    if index == 1:
        board[0] = player
    elif index == 2:
        board[2] = player
    elif index == 3:
        board[4] = player
    elif index == 4:
        board[10] = player
    elif index == 5:
        board[12] = player
    elif index == 6:
        board[14] = player
    elif index == 7:
        board[20] = player
    elif index == 8:
        board[22] = player
    else:
        board[24] = player
    print_board(board)


def valid_index(board, index):
    if index == 1 and board[0] == " ":
        return True
    elif index == 2 and board[2] == " ":
        return True
    elif index == 3 and board[4] == " ":
        return True
    elif index == 4 and board[10] == " ":
        return True
    elif index == 5 and board[12] == " ":
        return True
    elif index == 6 and board[14] == " ":
        return True
    elif index == 7 and board[20] == " ":
        return True
    elif index == 8 and board[22] == " ":
        return True
    elif index == 9 and board[24] == " ":
        return True
    else:
        return False


# check for win or tie
def check(board):
    if board[0] == board[2] and board[2] == board[4] and board[0] != " ":
        return True
    elif board[10] == board[12] and board[12] == board[14] and board[10] != " ":
        return True
    elif board[20] == board[22] and board[22] == board[24] and board[20] != " ":
        return True
    elif board[0] == board[10] and board[10] == board[20] and board[0] != " ":
        return True
    elif board[2] == board[12] and board[12] == board[22] and board[2] != " ":
        return True
    elif board[4] == board[14] and board[14] == board[24] and board[4] != " ":
        return True
    elif board[0] == board[12] and board[12] == board[24] and board[0] != " ":
        return True
    elif board[4] == board[12] and board[12] == board[20] and board[4] != " ":
        return True
    else:
        return False

count = 0
print_board(gameboard)
while count < 9:
    if count % 2 == 1:
        print("")
        print("Player X's turn")
        player_input(gameboard, "X")
        count+=1
        if check(gameboard):
            print("Player X Wins")
            break;
    else:
        print("")
        print("Player Y's turn")
        player_input(gameboard, "Y")
        count+=1
        if check(gameboard):
            print("Player Y Wins")
            break;

