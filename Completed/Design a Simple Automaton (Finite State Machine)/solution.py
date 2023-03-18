class Automaton:
    def __init__(self):
        self.states = {
            'q1': ('q1', 'q2'),
            'q2': ('q3', 'q2'),
            'q3': ('q2', 'q2'),
        }

    def read_commands(self, commands: list[str]) -> bool:
        state = 'q1'
        for c in commands:
            state = self.states[state][int(c)]
        return state == 'q2'


my_automaton = Automaton()
