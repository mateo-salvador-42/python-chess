from rich.console import Console
from rich.text import Text
from abc import ABC
console = Console(force_terminal=True, color_system="256")

class GameManager():
    def __init__(self):
        self.PlayerList = []
        Player1Name = "Player1"
        Player2Name = "Player2"
        self.PlayerList.append(Player(Player1Name, 600))
        self.PlayerList.append(Player(Player2Name, 600))
        self.tour = self.PlayerList[0]
        self.board = Board()
        self.board.config_board(self.PlayerList[0], self.PlayerList[1])

    def parser(self, message):
        try:
            coord: str = input(message)
            if len(coord) != 2:
                raise TypeError("Bad coords, example formats 'e4'")
            else:
                if coord[0].isalpha() and coord[1].isnumeric() :
                    if (int(coord[1]) > 0 and int(coord[1]) <= 8) and (coord[0] >= "a" and coord[0] <= "h"):
                        print(self.board.board[int(coord[1]) - 1].line[int(ord(coord[0]) - 97) - 8].state.name)
                        return self.board.board[int(coord[1]) - 1].line[int(ord(coord[0]) - 97) - 8].state.name
                    else:
                        raise TypeError("Bad coords, example formats 'e4'")
                else:
                    raise TypeError("Bad coords, example formats 'e4'")

        except TypeError as e:
            print(e)
            self.parser(message)

    def play_round(self):
        pass


        
class Player():
    def __init__(self, name, timer):
        self.name = name
        self.timer = timer
        self.piece = []

class Pawn(ABC):
    def __init__(self, Owner):
        self.display = "   "
        self.owner = Owner
        self.name = ""

    def return_display(self):
        return self.display
    
class WhitePawn(Pawn):
    def __init__(self, Owner: Player):
        super().__init__(Owner)
        self.display = "♙"
        self.color = "white"
        self.name = "White Pawn"

class WhiteQueen(WhitePawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♕"
        self.color = "white"
        self.name = "White Queen"

class WhiteKing(WhitePawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♔"
        self.color = "white"
        self.name = "White King"

class WhiteRook(WhitePawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♖"
        self.color = "white"
        self.name = "White Rook"

class WhiteBishop(WhitePawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♗"
        self.color = "white"
        self.name = "White Bishop"

class WhiteKnight(WhitePawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♘"
        self.color = "white"
        self.name = "Knight"

class BlackPawn(Pawn):
    def __init__(self, Owner):
        self.display = "♟"
        self.owner = Owner
        self.color = "black"
        self.name = "Black Pawn"

class BlackQueen(BlackPawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♛"
        self.color = "black"
        self.name = "Black Queen"

class BlackKing(BlackPawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♔"
        self.color = "black"
        self.name = "Black King"

class BlackRook(BlackPawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♖"
        self.color = "black"
        self.name = "Black Rook"

class BlackBishop(BlackPawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♗"
        self.color = "black"
        self.name = "Black Bishop"

class BlackKnight(BlackPawn):
    def __init__(self, Owner):
        super().__init__(Owner)
        self.display = "♘"
        self.color = "black"
        self.name = "Knight"

class Case():
    def __init__(self, color, state):
        self.color = color
        self.state = state

    def change_state(self, new_state):
        self.state = new_state

    def return_display(self):
        bg = "grey23" if self.color == "black" else "grey84"
        if self.state:
            t = Text(f" {self.state.display} ")
            t.stylize(f"{self.state.color} on {bg}")
            return t
        else:
            t = Text("   ")
            t.stylize(f"on {bg}")
            return t

class Lane():
    def __init__(self, row):
        self.line = []
        self.row = row
        self.fill_raw()

    def fill_raw(self):
        if self.row % 2 == 0:
            for i in range(4):
                self.line.append(Case("white", None))
                self.line.append(Case("black", None))
        else:
            for i in range(4):
                self.line.append(Case("black", None))
                self.line.append(Case("white", None))

    def display_line(self):
        result = Text()
        for case in self.line:
            result.append_text(case.return_display())
        return result

class Board():
    def __init__(self):
        self.board = [Lane(i) for i in range(8)]

    def config_board(self, Player1: Player, Player2: Player):
        for case in self.board[6].line:
            case.change_state(WhitePawn(Player1))
        self.board[7].line[0].change_state(WhiteRook(Player1))
        self.board[7].line[7].change_state(WhiteRook(Player1))
        self.board[7].line[1].change_state(WhiteKnight(Player1))
        self.board[7].line[6].change_state(WhiteKnight(Player1))
        self.board[7].line[2].change_state(WhiteBishop(Player1))
        self.board[7].line[5].change_state(WhiteBishop(Player1))
        self.board[7].line[3].change_state(WhiteQueen(Player1))
        self.board[7].line[4].change_state(WhiteKing(Player1))

        for case in self.board[1].line:
            case.change_state(BlackPawn(Player2))
        self.board[0].line[0].change_state(BlackRook(Player2))
        self.board[0].line[7].change_state(BlackRook(Player2))
        self.board[0].line[1].change_state(BlackKnight(Player2))
        self.board[0].line[6].change_state(BlackKnight(Player2))
        self.board[0].line[2].change_state(BlackBishop(Player2))
        self.board[0].line[5].change_state(BlackBishop(Player2))
        self.board[0].line[3].change_state(BlackQueen(Player2))
        self.board[0].line[4].change_state(BlackKing(Player2))

    def display_plateau(self):
        for lane in self.board:
            console.print(lane.display_line())

Game = GameManager()
Game.board.display_plateau()
Game.parser("Choose a piece to play: ")