import enum


class Mode(enum.Enum):
    STACK = 0
    MATH = 1
    HEAP = 2
    IO = 3
    FLOW = 4


class WS:
    def __init__(self, code: str, input_: str = ''):
        self.code = code
        self.input = input_
        self.stack = []
        self.heap = {}
        self.mode = None
        self.output = ''
        self.i = 0
        self.ops = {
            Mode.STACK: self.stack_op,
            Mode.MATH: self.math_op,
            Mode.HEAP: self.heap_op,
            Mode.IO: self.io_op,
            Mode.FLOW: self.flow_op,
        }

    @staticmethod
    def unbleach(code: str) -> str:
        return code.replace(' ', 's').replace('\t', 't').replace('\n', 'n')

    def eval(self) -> str:
        while self.i < len(self.code):
            c = self.code[self.i]
            c2 = self.code[self.i + 1] if self.i < len(self.code) - 1 else ''

            if self.mode is None:
                if c == ' ':  # Stack manipulation
                    self.mode = Mode.STACK
                    self.i += 1
                elif c + c2 == '\t ':
                    self.mode = Mode.MATH
                    self.i += 2
                elif c + c2 == '\t\t':
                    self.mode = Mode.HEAP
                    self.i += 2
                elif c + c2 == '\t\n':
                    self.mode = Mode.IO
                    self.i += 2
                elif c == '\t':
                    self.mode = Mode.FLOW
                    self.i += 1
            else:
                self.ops[self.mode]()

        return self.output

    def stack_op(self):
        c = self.code[self.i]
        c2 = self.code[self.i + 1] if self.i < len(self.code) - 1 else ''
        if c == ' ':
            pass
        elif c + c2 == '\t ':
            pass
        elif c + c2 == '\t\n':
            pass
        elif c + c2 == '\n ':
            pass
        elif c + c2 == '\n\t':
            pass
        elif c + c2 == '\n\n':
            pass


def whitespace(code: str, inp: str = '') -> str:
    return WS(code, inp).eval()
