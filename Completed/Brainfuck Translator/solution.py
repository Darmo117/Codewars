import re


def brainfuck_to_c(source_code: str) -> str:
    # Optimize Brainfuck code
    while True:
        new_code = re.sub(r'\+-|-\+|<>|><|\[]|[^<>\[\].,+-]', '', source_code)
        if len(new_code) == len(source_code):
            break
        source_code = new_code

    if not source_code:
        return ''

    # Translate to C
    c_code = ''
    indent = '  '
    indent_level = 0
    parens = 0

    i = 0
    while i < len(source_code):
        match source_code[i]:
            case ('+' | '-' | '<' | '>') as op:
                n = 0
                while i < len(source_code) and source_code[i] == op:
                    n += 1
                    i += 1
                if op in '><':
                    star = ''
                    op = '+' if op == '>' else '-'
                else:
                    star = '*'
                c_code += indent * indent_level + f'{star}p {op}= {n};\n'
            case '.':
                c_code += indent * indent_level + 'putchar(*p);\n'
                i += 1
            case ',':
                c_code += indent * indent_level + '*p = getchar();\n'
                i += 1
            case '[':
                c_code += indent * indent_level + 'if (*p) do {\n'
                indent_level += 1
                parens += 1
                i += 1
            case ']':
                if not indent_level:
                    return 'Error!'
                indent_level -= 1
                parens -= 1
                c_code += indent * indent_level + '} while (*p);\n'
                i += 1

    if parens:
        return 'Error!'
    return c_code
