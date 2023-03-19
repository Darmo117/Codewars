class Message:
    def __init__(self, s: str):
        self.words = [s]

    def __call__(self, s: str = ''):
        if s:
            self.words.append(s)
            return self
        return ' '.join(self.words)


create_message = Message
