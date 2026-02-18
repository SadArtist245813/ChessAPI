class Board:
    def __init__(self):
        self.BOARD_WIDTH = 8
        self.BOARD_LENGTH = 8
        self.EMPTY_PIECE = "  "
        self.LETTER_TO_NAME = {
            "R": "rook", "N": "knight", "B": "bishop",
            "Q": "queen", "K": "king", "P": "pawn"
        }

        self.LETTER_TO_COLOR = {
            "w": "White",
            "b": "Black"
        }

        self.NUMBER_TO_LETTER = {
            8: "A", 7: "B", 6: "C", 5: "D",
            4: "E", 3: "F", 2: "G", 1: "H"
        }

        self.board = [
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
        ]

        self.view_side = "w"
        self.fen_notation = ""
        self.turn = "w"
        self.white_king_position = "D1"
        self.black_king_position = "D8"
        self.white_king_check = False
        self.black_king_check = False
        self.last_move = {
            "From": "",
            "To": "",
            "Piece": ""
        }

    # Return board (seld.board)
    def get_board(self):
        return self.board

    # Change the side the board would be viewed in (self.view_side)
    def set_view_side(self, option):
        try:
            option.lower()
        except Exception as e:
            return False

        if option == "w" or option == "white":
            self.view_side = "w"
            return True

        if option == "b" or option == "black":
            self.view_side = "b"
            return True

        return False

    def get_LETTER_TO_NAME(self):
        return self.LETTER_TO_NAME

    def get_fen_notation(self):
        return self.fen_notation

    # Converts position number to letter
    def find_letter(self, number):
        return self.NUMBER_TO_LETTER[number]
    
    # Converts position letter to number
    def find_number(self, letter):
        for key, value in self.NUMBER_TO_LETTER.items():
            if value == letter:
                return key

    # Splits the board position into letter and number
    def split_position(self, position):
        return position[0], int(position[1])

    # Returns color of the piece from the board position
    def piece_color(self, position):
        piece = self.get_piece(position)
        return piece[0]
    
    # Return the piece symbol of the position
    def piece_symbol(self, position):
        piece = self.get_piece(position)
        return piece[1]

    # Return board position piece
    def get_position(self, position):
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        return self.board[number - 1][letter_number - 1]

    # Changes the position's values
    def set_position(self, position, piece):
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        self.board[number - 1][letter_number - 1] = piece

    # Move a piece
    def move_piece(self, old, new):
        self.set_position(new, self.get_position(old))
        self.set_position(old, "  ")

    def check_king_check(self, movements, position):
        if self.turn == "w":
            for move in movements:
                if move == self.white_king_position
                    self.white_king_check = True
                    return True

        if self.turn = "b":
            for move in movements:
                if move == slef.black_king_position:
                    self.black_king_check == True
                    return True

        return False

    def find_rook_movements(self, position):
        symbol = self.piece_symbol(position)
        if symbol != "R":
            return None
        
        letter, number = self.split_position(position)
        movements = []

        for i in range(1, 9):
            movements.append(self.find_letter(i) + str(number))

        for i in range(1, 9):
            movements.append(letter + str(i))

        return movements
    
    def find_bishop_movements(self, position):
        symbol = self.piece_symbol(position)
        if symbol != "B":
            return None
        
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        #later

        '''
        # Bishop positions top left
        for i in range(1, 9):
            for j in range(1, 9):
                if (1 <= i >= 8) and (1 <= j >= 8):
                    movements.append(self.find_letter(letter_number - 1) + str(number + j))

        # Bishop positions top right
        for i in range(1, 9):
            for j in range(1, 9):
                if (1 <= i >= 8) and (1 <= j >= 8):
                    movements.append(self.find_letter(letter_number + 1) + str(number + 1))

        # Bishop positions bottom right
        for i in range(1, 9):
            for j in range(1, 9):
                letter_number + i
                number - j
                if (1 <= i >= 8) and (1 <= j >= 8):
                    movements.append(self.find_letter(letter_number + 1) + str(number - j))

        # Bishop positions bottom left
        for i in range(1, 9):
            for j in range(1, 9):
                if (1 <= i >= 8) and (1 <= j >= 8):
                    movements.append(self.find_letter(letter_number - 1) + str(number - j))

        return movements
        '''
        
    def find_knight_movements(self, position):
        symbol = self.piece_symbol(position)
        if symbol != "K":
            return None
        
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        #knight math
        temp = {}
        temp[letter_number - 1] = number + 2
        temp[letter_number + 2] = number + 1
        temp[letter_number + 2] = number - 1
        temp[letter_number + 1] = number + 2
        temp[letter_number + 1] = number - 2
        temp[letter_number - 1] = number - 2
        temp[letter_number - 2] = number - 1
        temp[letter_number - 2] = number + 1

        #check board bounds
        for key, value in temp.items():
            if ((1 <= key >= 8) == False) or ((1 <= value >= 8) == False):
                del temp[key]
            else:
                movements.append(self.find_letter(key) + str(value))

        return movements
    
    def find_white_pond_movements(self, position):
        symbol = self.piece_symbol(position)
        color = self.piece_color(position)
        if symbol != "P" or color != "w":
            return None
        
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        if number < 8:
            movements.append(letter + str(number + 1))
        else:
            return movements

        if number == 2:
            movements.append(letter + str(4))

        if letter_number > 1:
            if self.get_piece(position) != "  ":
                movements.append(self.find_letter(letter_number - 1) + str(number + 1))

        if letter_number < 9:
            if self.get_piece(position) != "  ":
                movements.append(self.find_letter(letter_number + 1) + str(number + 1))
                
        if (self.last_move["Piece"] == "P" and
            self.last_move["From"] == (self.find_letter(letter_number - 1) + str(7)) and
            self.last_move["To"] == (self.find_letter(letter_number - 1) + str(5))):
            movements.append(self.find_letter(letter_number - 1) + str(6))

        if (self.last_move["Piece"] == "P" and
            self.last_move["From"] == (self.find_letter(letter_number + 1) + str(7)) and
            self.last_move["To"] == (self.find_letter(letter_number + 1) + str(5))):
            movements.append(self.find_letter(letter_number + 1) + str(6))
            
        return movements

    def find_black_pond_movements(self, position):
        symbol = self.piece_symbol(position)
        color = self.piece_color(position)
        if symbol != "P" or color != "w":
            return None
        
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        if number > 1:
            movements.append(letter + str(number + 1))
        else:
            return movements

        if number == 7:
            movements.append(letter + str(4))

        if letter_number > 1:
            if self.get_piece(position) != "  ":
                movements.append(self.find_letter(letter_number - 1) + str(number + 1))

        if letter_number < 9:
            if self.get_piece(position) != "  ":
                movements.append(self.find_letter(letter_number + 1) + str(number + 1))
                
        if (self.last_move["Piece"] == "P" and
            self.last_move["From"] == (self.find_letter(letter_number - 1) + str(2)) and
            self.last_move["To"] == (self.find_letter(letter_number - 1) + str(4))):
            movements.append(self.find_letter(letter_number - 1) + str(3))

        if (self.last_move["Piece"] == "P" and
            self.last_move["From"] == (self.find_letter(letter_number + 1) + str(2)) and
            self.last_move["To"] == (self.find_letter(letter_number + 1) + str(4))):
            movements.append(self.find_letter(letter_number + 1) + str(3))
            
        return movements

    def find_pond_movements(self, position):
        symbol = self.piece_symbol(position)
        color = self.piece_color(position)
        if symbol != "P":
            return None

        movements = []
        if color == "w":
            movements = self.find_white_pond_movements(position)
        else:
            movements = self.find_black_pond_movements(position)

        return movements
    
    def find_queen_movements(self, position):
        movements = []
        movements += self.find_rook_movements(position)
        movements += self.find_bishop_movements(position)
        return movements

    def find_king_movements(self, position):
        symbol = self.piece_symbol(position)
        if symbol != "K" or self.king_check == True:
            return None

        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        if number - 1 > 0:
            movements.append(letter + str(1))

        # not done

        return movements

    def find_movements(self, position):
        match self.piece_symbol(position):
            case "K":
                return self.find_king_movements(position)
            case "Q":
                return self.find_queen_movements(position)
            case "R":
                return self.find_rook_movements(position)
            case "B":
                return self.find_bishop_movements(position)
            case "N":
                return self.find_knight_movements(position)
            case "P":
                return self.find_pond_movements(position)