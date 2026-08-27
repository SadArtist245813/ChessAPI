from datetime import datetime

class Board:
    def __init__(self):
        self.BOARD_WIDTH = 8
        self.BOARD_LENGTH = 8
        self.EMPTY_PIECE = "  "
        self.PIECES = ["R", "N", "B", "Q", "K", "P"]
        self.LETTER_TO_NAME = {
            "R": "rook", "N": "knight", "B": "bishop",
            "Q": "queen", "K": "king", "P": "pawn"
        }

        self.LETTER_TO_COLOR = {
            "w": "White",
            "b": "Black"
        }

        self.NUMBER_TO_LETTER = {
            8: "A", 7: "B", 6: "C", 5: "D", 4: "E", 3: "F", 2: "G", 1: "H"
        }

        self.event = "Live Chess"
        self.site = "Python API"
        self.date = datetime.now().strftime("%y.%m.%d")
        self.round = 1
        self.white_player_name = "Player 1"
        self.black_player_name = "Player 2"
        self.result = "*"

        self.board = [
            ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],   
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["bR", "bN", "bB", "bK", "bQ", "bB", "bN", "bR"]
        ]

        self.starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0"
        self.view_side = "w"
        self.turn = "w"
        self.move_lock = True
        
        self.can_castle = { "K": True, "Q": True, "k": True, "q": True }
        self.game_moves = 0
        self.rule_50_move = 0
        self.white_king_position = "E1"
        self.black_king_position = "E8"
        self.white_king_check = False
        self.black_king_check = False

        self.move_history = [] # list of {"From": "  ", "To": "  ", "Piece": "  "}

    # Return board (seld.board)
    def get_board(self):
        return self.board

    # Change the side the board would be viewed in (self.view_side)
    def set_view_side(self, option=None):
        if option == None:
            if self.view_side == "w":
                self.view_side = "b"
            else:
                self.view_side = "w"
            return True
        else:
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

    def get_move_lock(self):
        return self.move_lock

    def set_move_lock(self, option=None):
        if option == None:
            if self.move_lock == True:
                self.move_lock = False
            else:
                self.move_lock = True
        else:
            self.move_lock = option       
    
    def set_turn(self, turn):
        self.turn = turn

    def get_turn(self):
        return self.turn

    def get_fen_notation(self):
        pass

    # Converts position number to letter
    def find_letter(self, number):
        return self.NUMBER_TO_LETTER[number]
    
    # Converts position letter to number
    def find_number(self, letter):
        for key, value in self.NUMBER_TO_LETTER.items():
            if value == letter:
                return key
            
    # Returns chess notations based on entered variable type. For easier API use.
    def get_chess_notation(self, variable):
        if isinstance(variable, tuple):
            letter = self.find_letter(variable[0])
            return letter + str(variable[1])
        elif isinstance(variable, str):
            return variable
        return None

    # Splits the board position into letter and number
    def split_position(self, position):
        return position[0], int(position[1])

    # Return board position's piece
    def get_position(self, position):
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        return self.board[number - 1][letter_number - 1]

    # Changes the position's values
    def set_position(self, position, piece):
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        self.board[number - 1][letter_number - 1] = piece

    # Set a last move (self.move_history)
    def set_last_move(self, old, new):
        last_move = {"From": old, "To": new, "Piece": self.get_position(new)}
        self.move_history.append(last_move)

    # Gets the last (self.move_history)
    def get_last_move(self):
        if len(self.move_history) != 0:
            return self.move_history[len(self.move_history) - 1]
        return {"From": "  ", "To": "  ", "Piece": "  "}

    # Returns color of the piece from the board position
    def piece_color(self, position):
        piece = self.get_position(position)
        return piece[0]
    
    # Return the piece symbol of the position
    def piece_symbol(self, position):
        piece = self.get_position(position)
        return piece[1]

    # Change board turn
    def change_turn(self):
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"                
    
    def check_board_bounds(self, letter_number, number):
        if (1 <= letter_number <= 8) and (1 <= number <= 8):
            return True
        return False
        
    def check_opposite(self, position1, position2):
        if self.get_position(position1)[0] == self.get_position(position2)[0]:
            return False
        else:
            return True
        
    def check_move_conditions(self, position_1, position_2):    
        if self.get_position(position_2) != "  ":
            if self.check_opposite(position_1, position_2):
                return True
            else:
                return False
        return True

    def find_rook_movements(self, position):
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        # Up
        for i in range(number + 1, 9):
            move = letter + str(i)
            if self.get_position(move) == "  ":
                movements.append(move)
            elif self.check_move_conditions(position, move):
                movements.append(move)
                break
            else:
                break

        # Left
        for i in range(letter_number + 1, 9):
            move = self.find_letter(i) + str(number)
            if self.get_position(move) == "  ":
                movements.append(move)
            elif self.check_move_conditions(position, move):
                movements.append(move)
                break
            else:
                break

        # Down
        for i in range(number - 1, 0, -1):
            move = letter + str(i)
            if self.get_position(move) == "  ":
                movements.append(move)
            elif self.check_move_conditions(position, move):
                movements.append(move)
                break
            else:
                break

        # Right
        for i in range(letter_number - 1, 0, -1):
            move = self.find_letter(i) + str(number)
            if self.get_position(move) == "  ":
                movements.append(move)
            elif self.check_move_conditions(position, move):
                movements.append(move)
                break
            else:
                break

        return movements
    
    def find_bishop_movements(self, position):
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []
        
        # up right
        for i in range(1, 9):
            temp_letter_number = letter_number - i
            temp_number = number + i
            if (1 <= temp_letter_number <= 8) and (1 <= temp_number <= 8):
                move = self.find_letter(temp_letter_number) + str(temp_number)
                if self.get_position(move) == "  ":
                    movements.append(move)
                elif self.check_move_conditions(position, move):
                    movements.append(move)
                    break
                else:
                    break
            else:
                break

        # up left
        for i in range(1, 9):
            temp_letter_number = letter_number + i
            temp_number = number + i
            if (1 <= temp_letter_number <= 8) and (1 <= temp_number <= 8):
                move = self.find_letter(temp_letter_number) + str(temp_number)
                if self.get_position(move) == "  ":
                    movements.append(move)
                elif self.check_move_conditions(position, move):
                    movements.append(move)
                    break
                else:
                    break
            else:
                break

        # down left
        for i in range(1, 9):
            temp_letter_number = letter_number + i
            temp_number = number - i
            if (1 <= temp_letter_number <= 8) and (1 <= temp_number <= 8):
                move = self.find_letter(temp_letter_number) + str(temp_number)
                if self.get_position(move) == "  ":
                    movements.append(move)
                elif self.check_move_conditions(position, move):
                    movements.append(move)
                    break
                else:
                    break
            else:
                break

        # down right
        for i in range(1, 9):
            temp_letter_number = letter_number - i
            temp_number = number - i
            if (1 <= temp_letter_number <= 8) and (1 <= temp_number <= 8):
                move = self.find_letter(temp_letter_number) + str(temp_number)
                if self.get_position(move) == "  ":
                    movements.append(move)
                elif self.check_move_conditions(position, move):
                    movements.append(move)
                    break
                else:
                    break
            else:
                break

        return movements
        
    def find_knight_movements(self, position):
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        # Knight math
        temp = []
        temp.append((letter_number - 1, number + 2))
        temp.append((letter_number + 2, number + 1))
        temp.append((letter_number + 2, number - 1))
        temp.append((letter_number + 1, number + 2))
        temp.append((letter_number + 1, number - 2))
        temp.append((letter_number - 1, number - 2))
        temp.append((letter_number - 2, number - 1))
        temp.append((letter_number - 2, number + 1))

        # Check bounds
        for letter_number, number in temp:
            if self.check_board_bounds(letter_number, number):
                move = self.find_letter(letter_number) + str(number)
                if self.check_move_conditions(position, move):
                    movements.append(move)

        return movements
    
    def find_white_pond_movements(self, position):
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        # One forward
        if number < 8 and self.get_position(letter + str(number + 1)) == "  ":
            movements.append(letter + str(number + 1))
        else:
            return movements

        # Two forward
        if number == 2:
            if self.get_position(letter + str(4)) == "  ":
                movements.append(letter + str(4))

        # Take right
        if letter_number > 1:
            top_right = self.find_letter(letter_number - 1) + str(number + 1)
            if self.get_position(top_right) != "  " and self.piece_color(top_right) == "b":
                movements.append(top_right)

        # Take left
        if letter_number < 8:
            top_left = self.find_letter(letter_number + 1) + str(number + 1)
            if self.get_position(top_left) != "  " and self.piece_color(top_left) == "b":
                movements.append(top_left)

        # En Passant
        last_move = self.get_last_move()
        if (letter_number > 1 and last_move["Piece"] == "bP" and
            last_move["From"] == (self.find_letter(letter_number - 1) + str(7)) and
            last_move["To"] == (self.find_letter(letter_number - 1) + str(5)) and int(last_move["To"][1]) == number):
            movements.append(self.find_letter(letter_number - 1) + str(number + 1))

        if (letter_number < 8 and last_move["Piece"] == "bP" and
            last_move["From"] == (self.find_letter(letter_number + 1) + str(7)) and
            last_move["To"] == (self.find_letter(letter_number + 1) + str(5)) and int(last_move["To"][1]) == number):
            movements.append(self.find_letter(letter_number + 1) + str(number + 1))
            
        return movements

    def find_black_pond_movements(self, position):   
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        # One forward
        if number > 1 and self.get_position(letter + str(number - 1)) == "  ":
                movements.append(letter + str(number - 1))
        else:
            return movements

        # Two forward
        if number == 7:
            if self.get_position(letter + str(5)) == "  ":
                movements.append(letter + str(5))

        # Take right
        if letter_number > 1:
            top_right = self.find_letter(letter_number - 1) + str(number - 1)
            if self.get_position(top_right) != "  " and self.piece_color(top_right) == "w":
                movements.append(top_right)

        # Take left
        if letter_number < 8:
            top_left = self.find_letter(letter_number + 1) + str(number - 1)
            if self.get_position(top_left) != "  " and self.piece_color(top_left) == "w":
                movements.append(top_left)
        
        # En Passant
        last_move = self.get_last_move()
        if (letter_number > 1 and last_move["Piece"] == "wP" and
            last_move["From"] == (self.find_letter(letter_number - 1) + str(2)) and
            last_move["To"] == (self.find_letter(letter_number - 1) + str(4)) and int(last_move["To"][1]) == number):
            movements.append(self.find_letter(letter_number - 1) + str(3))

        if (letter_number < 8 and last_move["Piece"] == "wP" and
            last_move["From"] == (self.find_letter(letter_number + 1) + str(2)) and
            last_move["To"] == (self.find_letter(letter_number + 1) + str(4)) and int(last_move["To"][1]) == number):
            movements.append(self.find_letter(letter_number + 1) + str(3))
            
        return movements

    # Correlate the color to the correct pond function
    def find_pond_movements(self, position):
        color = self.piece_color(position)
        movements = []

        if color == "w":
            movements = self.find_white_pond_movements(position)
        
        if color == "b":
            movements = self.find_black_pond_movements(position)

        return movements

    # Find possible queen movements (rook + bishop)
    def find_queen_movements(self, position):
        movements = []
        movements += self.find_rook_movements(position)
        movements += self.find_bishop_movements(position)
        return movements

    def find_king_movements(self, position):
        symbol = self.piece_symbol(position)
        color = self.piece_color(position)
        letter, number = self.split_position(position)
        letter_number = self.find_number(letter)
        movements = []

        if symbol != "K":
            return movements
        
        temp = []
        temp.append((letter_number + 1, number + 1)) # up left
        temp.append((letter_number, number + 1)) # up
        temp.append((letter_number - 1, number + 1)) # up right
        temp.append((letter_number - 1, number)) # right
        temp.append((letter_number - 1, number - 1)) # down right
        temp.append((letter_number, number - 1)) # down
        temp.append((letter_number + 1, number - 1)) # down left
        temp.append((letter_number + 1, number)) # left
        
        
        # Check if the king can move out of check (if in check)
        if color == "w" and self.white_king_check or color == "b" and self.black_king_check:
            movement_sets = self.find_all_possible_moves(king_call=True)
            for piece_position, movements in movement_sets.items():
                piece_color = self.piece_color(piece_position)
                for move in movements:
                    for possible_move in temp:
                        print({"Move": move, "Possible Move": possible_move, "Piece Color": piece_color, "Color": color})
                        if move == possible_move and piece_color != color:
                            temp.remove(possible_move)
        
        # Check bounds
        for letter_number, number in temp:
            if self.check_board_bounds(letter_number, number):
                move = self.find_letter(letter_number) + str(number)
                if self.check_move_conditions(position, move):
                    movements.append(move)

        return movements

    # Has the system to go to the correct movement finding functions based on position's piece
    def find_movements(self, position):
        position = self.get_chess_notation(position)
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
            case _:
                return []

    # Find the movements of every piece on the board
    def find_all_possible_moves(self, king_call=False):
        board_movements = {}
        for letter_number in range(8):
            letter = self.find_letter(letter_number + 1)
            for number in range(8):
                position = letter + str(number + 1)
                piece = self.get_position(position)
                if piece != "  " and (not king_call or self.piece_symbol(position) != "K"):
                    movements = self.find_movements(position)
                    if movements != []:
                        board_movements[position] = movements

        return board_movements

    def king_in_check(self):
        white_king_check = False
        black_king_check = False
        movement_sets = self.find_all_possible_moves()
        for piece_position, movements in movement_sets.items():
            piece_color = self.piece_color(piece_position)
            for move in movements:
                if piece_color == "w" and move == self.black_king_position:
                    black_king_check = True
                    print(f"Black King in Check by {piece_position}")
                    print(f"Black King Position: {self.black_king_position}")
                if piece_color == "b" and move == self.white_king_position: 
                    white_king_check = True
                    print(f"White King in Check by {piece_position}")
                    print(f"White King Position: {self.white_king_position}")
                
        self.white_king_check = white_king_check
        self.black_king_check = black_king_check


    # The math to move a piece
    def move(self, old, new):
        # Handle en passant capture
        old_letter, old_number = self.split_position(old)
        new_letter, new_number = self.split_position(new)
        old_letter_number = self.find_number(old_letter)
        new_letter_number = self.find_number(new_letter)
        
        piece_color = self.piece_color(old)
        piece_symbol = self.piece_symbol(old)

        # En passant capture
        if piece_symbol == "P" and old_letter_number != new_letter_number and self.get_position(new) == "  ":
            if piece_color == "w":
                self.set_position(new_letter + str(new_number - 1), "  ")
            elif piece_color == "b":
                self.set_position(new_letter + str(new_number + 1), "  ")

        # Move piece
        self.set_position(new, self.get_position(old))
        self.set_position(old, "  ")
        self.set_last_move(old, new)

        # Track king position
        if piece_symbol == "K":
            if piece_color == "w":
                self.white_king_position = new
            if piece_color == "b":
                self.black_king_position = new

        # Set king check status
        self.king_in_check()

    # Move a piece
    def move_piece(self, old, new):
        old = self.get_chess_notation(old)
        new = self.get_chess_notation(new)
        try:
            if self.move_lock == True:
                # Check if correct turn
                piece_color = self.piece_color(old)
                if piece_color != self.turn:
                    return False

                # Check if can properly move
                movements = self.find_movements(old)
                if new in movements:
                    self.move(old, new)
                    self.change_turn()
                else:
                    return False
            else:
                # Move without conditions (only for: move_lock = Flase)
                self.move(old, new)

            return True
        except Exception as e:
            print(f"\"On Move\" Error: {e}")
            return False

    # Sets the game based on fen notation format
    # Explination of how fen notation works: https://www.chess.com/terms/fen-chess
    def set_game(self, fen_notation):
        board = [[]]
        board_drawn = False
        for char in fen_notation:
            print([row[::-1] for row in board[::-1]])
            if char == " " or char == "-":
                board_drawn = True
                continue

            if board_drawn == True:
                if char == "w" or char == "b":
                    self.set_turn(char)
                    continue

                if char in self.can_castle.keys():
                    self.can_castle[char] = True
                    continue

            if char.isdigit():
                [board[0].append("  ") for _ in range(int(char))]
                continue

            if char.islower():
                board[0].insert(0, "b" + char.upper())
                continue

            if char.isupper():
                board[0].insert(0, "w" + char)
                continue

            if char == "/":
                board.insert(0, [])
                continue

        self.board = board

    # Reset to starting position
    # Starting postition: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0"
    def reset_board(self):
        self.set_game(self.starting_position)
        self.turn = "w"

    def algebraic_notation(self):
        pass

    def match_PGN_headers(self, headers):
        for key, value in headers.items():
            '''
            self.event = "Live Chess"
            self.site = "Python API"
            self.date = datetime.now().strftime("%y.%m.%d")
            self.round = 1
            self.white_player_name = "Player 1"
            self.black_player_name = "Player 2"
            self.result = "*"
            '''

            print(key, value)

            match(key):
                case "Event":
                    self.event = value
                case "Site":
                    self.site = value
                case "Date":
                    self.date = value
                case "Round":
                    self.round = value
                case "White":
                    self.white_player_name = value
                case "Black":
                    self.black_player_name = value
                case "Result":
                    self.result = value

    # Read PGN file using file variable
    def read_PGN(self, file):
        moves = ""
        headers = {}
        for line in file:
            # End of file
            if not line:
                break

            if line.startswith('[') and line.endswith(']'):
                tag_end = line.find(' ')
                tag = line[1:tag_end]
                tag_value = line[tag_end+2:-1]
                headers[tag] = tag_value
        else:
            pass
        
        self.match_PGN_headers(headers)
        for line in file:
            moves += line.strip() + " "

        print(headers)
        print("File Read")

    # Read PGN file using file loaction
    def import_PGN(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.read_PGN(file)

    def export_PGN(self):
        pass