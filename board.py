class Board():
    def __init__(self):
        self.LETTER_TO_NAME = {
            "R": "rook", "N": "knight", "B": "bishop",
            "Q": "queen", "K": "queen", "P": "pawn"
        }
        self.NUMBER_TO_LETTER = {
            1: "A", 2: "B", 3: "C", 4: "D",
            5: "E", 6: "F", 7: "G", 8: "H"
        }
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.fen_notation = ""

    def get_board(self):
        return self.board
    
    def get_LETTER_TO_NAME(self):
        return self.LETTER_TO_NAME

    def get_fen_notation(self):
        return self.fen_notation

    def find_letter(self, number):
        return self.NUMBER_TO_LETTER[number]
    
    def find_number(self, letter):
        for key, value in self.LETTER_TO_NAME.items():
            if value == letter:
                return key

    def split_position(self, position):
        return position[0], position[1]

    def piece_color(self, position:int):
        letter, number = self.split_position(position)
        piece = self.board[letter][number]
        return piece[0]

    def piece_color(self, piece:str):
        return piece[0]
    
    def piece_symbol(self, position:int):
        letter, number = self.split_position(position)
        piece = self.board[letter][number]
        return piece[1]
    
    def piece_symbol(self, piece:str):
        return piece[1]

    def set_fen_notation(self, old, new):
        pass

    def get_position(self, position):
        letter, number = self.split_position(position)
        return self.board[letter][number]

    def move_piece(self, old, new):
        old_letter, old_number = self.split_position(old)
        new_letter, new_number = self.split_position(new)
        self.board[new_letter][new_number] = self.board[old_letter][old_number]
        self.board[old_letter][old_number] = "  "
        self.set_fen_notation()

    def check_king_check(self, position):
        pass

    def find_rook_movements(self, position):
        symbol = self.piece_symbol(position)
        if symbol is not "R":
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
        if symbol is not "B":
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
        '''
        return movements
    
    def find_knight_movements(self, position):
        symbol = self.piece_symbol(position)
        if symbol is not "K":
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
            if ((1 <= key >= 8) is False) or ((1 <= value >= 8) is False):
                del temp[key]
            else:
                movements.append(self.find_letter(key) + str(value))

        return movements
    
    def find_pond_movements(self, position):
        return
    
    def find_queen_movements(self, position):
        movements = []
        movements += self.find_rook_movements(position)
        movements += self.find_bishop_movements(position)
        return movements

    def find_king_movements(self, position):
        return

    def find_movements(self, position):
        match self.piece_symbol(self.board[position]):
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