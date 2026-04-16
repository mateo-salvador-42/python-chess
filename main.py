class Pion():
    def __init__(self):
        self.name = "Pawn"
        self.display = ""

    def return_display(self):
        return self.display


class Case():
    def __init__(self, color, state):
        self.color = color
        self.state = state
        if state:
            self.change_state(state)

    def change_state(self, pion):
        self.state = pion

    def return_display(self):
        if self.state:
            return self.state.display
        else:
            if self.color == "black":
                return "⬛"
            elif self.color == "white":
                return "⬜"


class Ligne():
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
        result = ""
        for case in self.line:
            result += case.return_display()
        return result


class Plateau():
    def __init__(self):
        self.plateau = []
        for i in range(8):
            self.plateau.append(Ligne(i))

    def display_plateau(self):
        for line in self.plateau:
            print(line.display_line())


plateau = Plateau()

plateau.display_plateau()
