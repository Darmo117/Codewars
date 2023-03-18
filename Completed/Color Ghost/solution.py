import random


class Ghost:
    COLORS = ('white', 'yellow', 'purple', 'red')

    def __init__(self):
        self.color = random.choice(self.COLORS)
