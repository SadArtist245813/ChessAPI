from board import Board

game = Board()

def print_board(board = game.board):
    if game.view_side == "w":
        temp_board = [row[::-1] for row in board[::-1]]
        for i in range(8):
            print(f"{temp_board[i]}")

    if game.view_side == "b":
        for i in range(8):
            print(f"{board[i]}")

def replace_print(movements):
    board = game.get_board().copy()
    for move in movements:
        letter, number = game.split_position(move)
        letter_number = game.find_number(letter)
        board[number - 1][letter_number - 1] = "//"
    print_board(board)
        
again = True
while again:
    print("\n1. View Board\n2. Move A Piece\n3. Get Board Position\n4. Get Position Movements\n5. Set View Side\n0. Exit\n")
    choice = input("Choice: ")
    match choice:
        case "1":
            print_board()

        case "2":
            print_board()
            print(game.get_fen_notation())
            old = input("Form: ")
            new = input("To: ")
            if game.move_piece(old, new) == False: 
                print("\nInvalid move")

        case "3":
            choice = input("Position: ")
            piece = game.get_position(choice)
            print(f"{piece}")

        case "4":
            print_board()
            choice = input("\nPosition: ")
            movements = game.find_movements(choice) 
            replace_print(movements)
            print(f"{movements}")

        case "5":
            choice = input("Which side to set view (w/b): ")
            print(f"{game.set_view_side(choice)}")
            print(f"{game.view_side}")

        case "0":
            again = False

        case _:
            print("\nInvalid choice")