from rich.console import Console
from rich.text import Text

console = Console(force_terminal=True, color_system="256")

class Pion():
    def __init__(self):
        self.display = "♝"

    def return_display(self):
        return self.display

class Case():
    def __init__(self, color, state):
        self.color = color
        self.state = state

    def return_display(self):
        content = f" {self.state.return_display()} " if self.state else "   "
        bg = "grey23" if self.color == "black" else "grey84"
        t = Text(content)
        t.stylize(f"on {bg}")
        return t

class Ligne():
    def __init__(self, row):
        self.line = []
        self.row = row
        self.fill_raw()

    def fill_raw(self):
        if self.row % 2 == 0:
            for i in range(4):
                self.line.append(Case("white", Pion()))
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

class Plateau():
    def __init__(self):
        self.plateau = [Ligne(i) for i in range(8)]

    def display_plateau(self):
        for ligne in self.plateau:
            console.print(ligne.display_line())

plateau = Plateau()
plateau.display_plateau()