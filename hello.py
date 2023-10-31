def print_board(board):
    for row in range(len(board) - 1, -1, -1):
        for col in range(len(board[row])):
            print(board[row][col], end=' ')
        print()  # prints board but in reverse order to account for chips falling to the last row
    print()
def initialize_board(num_row, num_col):
    board = [["-"] * num_col for _ in range(num_row)]  # creates an array with the 2D Board character list
    return board
def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row
def check_if_winner(board, col, row, chip_type):
  directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1)] #accounts for any dir. win
  for length, height in directions:
      count = 1
      for i in range(1, 4):
          x_coord = col + length * i #x-coordinate
          y_coord = row + height * i #y-coordinate
          if not (0 <= x_coord < len(board[0]) and 0 <= y_coord < len(board)):
              break
          if board[y_place][x_place] != chip_type:
              break
          count += 1
      if count == 4:
          return True
  return False
def main():
    num_row = int(input("What would you like the height of the board to be?"))
    num_col = int(input("What would you like the length of the board to be?"))
    board = initialize_board(num_row, num_col)
    print_board(board)
    print("Player 1: x", "\nPlayer 2: o")
    chip_type = ['x', 'o']  # list so that it alternates between each player's chip
    gamer = ["Player 1", "Player 2"]  # gamer alternates between each player
    player_index = 0
    game_over = num_row * num_col  # max number of moves possible for no one to win by
    turns = 0  # number of turns
    while turns < game_over:
        player = chip_type[player_index]  # alternates the chip type
        gamers = gamer[player_index]  # alternates the player's turns
        col = int(input(f"{gamers}: Which column would you like to choose? "))
        if 0 <= col < num_col:
            row = insert_chip(board, col, player)
            print_board(board)
            if check_if_winner(board, col, row, player):
                print(f"{gamers} won the game!")
                break  # ends loop once someones has won
            turns += 1
            player_index = 1 - player_index
        else:
            print("Invalid column. Please choose a valid column.")
    if turns == game_over:  # refers to when all spaces on the board are taken and no one has won yet
        print("Draw. Nobody wins.")
if __name__ == '__main__':
    main()  #groups all functions under main()