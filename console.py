from .board import Board

class Console(Board):
    def __init__(self):
        super().__init__()

    # Print the board (self.baord)
    def print_board(self):
        if super().view_side == "w":
            temp_board = [row[::-1] for row in super().board[::-1]]
            for i in range(8):
                print(f"{temp_board[i]}")

        if super().view_side == "b":
            for i in range(8):
                print(f"{self.board[i]}")

    def play_chess(self):
        pass