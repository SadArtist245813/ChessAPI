class Piece():
    def __init__(self, color, currentPosition, pastPosition):
        self.color = color
        self.name = ""
        self.symbol = ""
        self.current_position = currentPosition
        self.past_position = pastPosition

    def get_color(self):
        return self.color
    
    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.symbol
    
    def get_current_position(self):
        return self.currentPosition
    
    def get_past_position(self):
        return self.pastPosition
    
    def find_king_movements(self):
        return
    
    def find_queen_movements(self):
        return
    
    def find_rook_movements(self):
        return
    
    def find_bishop_movements(self):
        return
    
    def find_knight_movements(self):
        return
    
    def find_pond_movements(self):
        return

    def find_movements(self):
        match self.symbol:
            case "K":
                return self.find_king_movements()
            case "Q":
                return self.find_queen_movements()
            case "R":
                return self.find_rook_movements()
            case "B":
                return self.find_bishop_movements()
            case "N":
                return self.find_knight_movements()
            case "P":
                return self.find_pond_movements()
