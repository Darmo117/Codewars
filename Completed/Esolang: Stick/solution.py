def interpreter(code: str) -> str:
    stack = [0]
    output = ''
    ip = 0
    while ip < len(code):
        c = code[ip]
        match c:
            case '^':
                stack.pop()
            case '!':
                stack.append(0)
            case '+':
                stack[-1] = (stack[-1] + 1) % 256
            case '-':
                stack[-1] = (stack[-1] - 1) % 256
            case '*':
                print(stack[-1])
                output += chr(stack[-1])
            case '[':
                if not stack[-1]:
                    while code[ip] != ']':
                        ip += 1
            case ']':
                if stack[-1]:
                    while code[ip] != '[':
                        ip -= 1
                    ip -= 1
        ip += 1
    return output
