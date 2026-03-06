board_num = [1,2,3,4,5,6,7,8,9]

def display_board():
    print("\n🎮 Current Board\n")
    print(board_num[0], "|", board_num[1], "|", board_num[2])
    print("----------")
    print(board_num[3], "|", board_num[4], "|", board_num[5])
    print("----------")
    print(board_num[6], "|", board_num[7], "|", board_num[8])
    print()

def game(player):
    position = int(input(f"🎯 Player {player}, enter a position (1-9): "))
    index_position = position - 1

    if board_num[index_position] == "X" or board_num[index_position] == "O":
        print("⚠️ Position already taken! Choose another.\n")
        game(player)
    else:
        board_num[index_position] = player
        print(f"✅ Player {player} placed at position {position}\n")

def check_winner(player):
    if (
        (board_num[0] == board_num[1] == board_num[2] == player) or
        (board_num[3] == board_num[4] == board_num[5] == player) or
        (board_num[6] == board_num[7] == board_num[8] == player) or
        (board_num[0] == board_num[3] == board_num[6] == player) or
        (board_num[1] == board_num[4] == board_num[7] == player) or
        (board_num[2] == board_num[5] == board_num[8] == player) or
        (board_num[0] == board_num[4] == board_num[8] == player) or
        (board_num[2] == board_num[4] == board_num[6] == player)
    ):
        return True
    return False


game_start = True
player = "❌"
game_count = 0

print("🎲 Welcome to Tic Tac Toe ❌⭕")
display_board()

while game_start:
    if game_count < 9:
        game(player)
        display_board()
        game_count += 1
    else:
        print("🤝 It's a Draw!")
        break

    if check_winner(player):
        print(f"🏆 The Winner is Player {player} 🎉")
        break

    if player == "❌":
        player = "⭕"
    else:
        player = "❌"




