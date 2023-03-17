def underload(raw_code: str) -> str:
    code = list(raw_code)
    stack: list[str] = []
    output = ''
    string_mode = 0
    buffer = ''
    i = 0
    while i < len(code):
        c = code[i]
        if string_mode:
            if c == '(':
                string_mode += 1
            elif c == ')':
                string_mode -= 1
            if string_mode:
                buffer += c
            else:
                stack.append(buffer)
                buffer = ''
        else:
            match c:
                case ':':
                    stack.append(stack[-1])
                case '!':
                    stack.pop()
                case '~':
                    stack[-2:] = stack[-1:-3:-1]
                case '*':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b + a)
                case 'a':
                    stack[-1] = f'({stack[-1]})'
                case '^':
                    s = stack.pop()
                    for j, cc in enumerate(s):
                        code.insert(i + j + 1, cc)
                case 'S':
                    output += stack.pop()
                case '(':
                    string_mode = 1
                case ')':
                    raise Exception('unbalanced parentheses')
        i += 1
    if string_mode:
        raise Exception('unbalanced parentheses')
    return output
