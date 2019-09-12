class TurnManager:
    def __init__(self):
        self.overall = 1
        self.turn = 1

    def add_turn(self):
        if self.turn == 9:
            self.turn = 1
            self.overall += 1
        else:
            self.turn += 1
            self.overall += 1
