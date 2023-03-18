def calc(expr: str):
    instructions = expr.split()
    stack = [0]
    for instr in instructions:
        match instr:
            case '+':
                stack.append(stack.pop() + stack.pop())
            case '-':
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            case '*':
                stack.append(stack.pop() * stack.pop())
            case '/':
                x, y = stack.pop(), stack.pop()
                stack.append(y / x)
            case v:
                if '.' in v:
                    stack.append(float(v))
                else:
                    stack.append(int(v))
    return stack[-1]
