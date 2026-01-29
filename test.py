from .board import Board

game = Board()

again = True
while again:
    print("1. Play Chess\n2. Get Board Position\n 3. Test Movements Functions\n")
    choice = int(input("Choice: "))
    match choice:
        case 1:
            print(game.get_board())
            print(game.get_fen_notation())
            old = input("Form: ")
            new = input("To: ")
            game.move_piece(old, new)
        case 3:
            print(game.get_LETTER_TO_NAME())
            choice = input("Choice: ")
            game.find_movements(choice)
        case 0:
            again = False