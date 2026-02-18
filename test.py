from board import Board

game = Board()

def print_board(self):
        if game.view_side == "w":
            temp_board = [row[::-1] for row in game.board[::-1]]
            for i in range(8):
                print(f"{temp_board[i]}")

        if self.view_side == "b":
            for i in range(8):
                print(f"{self.board[i]}")

again = True
while again:
    print("\n1. View Board\n2. Move A Piece\n3. Get Board Position\n4. Get Position Movements\n5. Set View Side\n0. Exit\n")
    choice = input("Choice: ")
    match choice:
        case "1":
            game.print_board()

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
            print(game.get_LETTER_TO_NAME())
            choice = input("Choice: ")
            movements = game.find_movements(choice)
            print(f"{movements}")

        case "5":
            choice = input("Which side to set view (w/b): ")
            print(f"{game.set_view_side(choice)}")
            print(f"{game.view_side}")

        case "0":
            again = False

        case _:
            print("\nInvalid choice")