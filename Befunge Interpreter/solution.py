import random


def interpret(code):
    RIGHT = 0, 1
    LEFT = 0, -1
    UP = -1, 0
    DOWN = 1, 0

    grid: list[list[str]] = [list(s) for s in code.split('\n')]
    output = ''
    stack = []
    ip = [0, 0]
    dir_ = RIGHT
    string = False
    skip = False
    stop = False

    while not stop:
        if skip:
            skip = False
        else:
            match grid[ip[0]][ip[1]]:
                case c if string:
                    if c == '"':  # Exit string mode
                        string = False
                    else:  # Push ASCII code of current instruction
                        stack.append(ord(c))
                case ('0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9') as d:  # Push digit
                    stack.append(int(d))
                case '+':  # Add top 2
                    stack.append(stack.pop() + stack.pop())
                case '-':  # Subtract top 2
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case '*':  # Multiply top 2
                    stack.append(stack.pop() * stack.pop())
                case '/':  # Divide top 2
                    a, b = stack.pop(), stack.pop()
                    stack.append(b // a if a else 0)
                case '%':  # Modulo of top 2
                    a, b = stack.pop(), stack.pop()
                    stack.append(b % a if a else 0)
                case '!':  # Negate top
                    stack.append(int(not stack.pop()))
                case '`':  # Push 1 if top < below, else push 0
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b > a))
                case '>':  # Go rightwards
                    dir_ = RIGHT
                case '<':  # Go leftwards
                    dir_ = LEFT
                case '^':  # Go upwards
                    dir_ = UP
                case 'v':  # Go downwards
                    dir_ = DOWN
                case '?':  # Go into random direction
                    dir_ = random.choice((RIGHT, LEFT, UP, DOWN))
                case '_':  # Go right if top == 0, else go left
                    dir_ = RIGHT if stack.pop() == 0 else LEFT
                case '|':  # Go down if top == 0, else go up
                    dir_ = DOWN if stack.pop() == 0 else UP
                case '"':  # Begin string mode
                    string = True
                case ':':  # Duplicate top or push 0 if empty stack
                    if stack:
                        stack.append(stack[-1])
                    else:
                        stack.append(0)
                case '\\':  # Swap top 2
                    if len(stack) == 1:
                        stack.append(stack[0])
                        stack[0] = 0
                    elif len(stack) > 1:
                        stack[-2], stack[-1] = stack[-1], stack[-2]
                case '$':  # Discard top
                    stack.pop()
                case '.':  # Print top as ASCII character
                    output += str(stack.pop())
                case ',':  # Print top as integer
                    output += chr(stack.pop())
                case '#':  # Skip next
                    skip = True
                case 'p':  # Put top at (x, y) in grid
                    y, x, v = stack.pop(), stack.pop(), stack.pop()
                    grid[y][x] = chr(v)
                case 'g':  # Push value at (x, y)
                    y, x = stack.pop(), stack.pop()
                    stack.append(ord(grid[y][x]))
                case '@':  # Stop execution
                    stop = True
        # Move IP
        ip[0] = (ip[0] + dir_[0]) % len(grid)
        ip[1] = (ip[1] + dir_[1]) % len(grid[ip[0]])

    return output
