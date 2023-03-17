import re


def assembler_interpreter(program: str) -> str | int:
    registers: dict[str, int] = {}
    labels: dict[str, int] = {}
    cmp_cache = 0
    call_stack = []
    output = ''
    ip = 0

    lines = program.split('\n')

    # Remove leading whitespace and cache all labels
    for i, line in enumerate(lines):
        lines[i] = lines[i].lstrip()
        if m := re.match(r'(\w+):', line):
            label, = m.groups()
            if label not in labels:
                labels[label] = i

    def get_value(r: str) -> int:
        if r in registers:
            return registers[r]
        return int(r)

    while ip < len(lines):
        instr = lines[ip]

        if m := re.match(r'mov\s+(\w+),\s+(\w+)', instr):
            x, y = m.groups()
            registers[x] = get_value(y)
        elif m := re.match(r'inc\s+(\w+)', instr):
            x, = m.groups()
            registers[x] += 1
        elif m := re.match(r'dec\s+(\w+)', instr):
            x, = m.groups()
            registers[x] -= 1
        elif m := re.match(r'add\s+(\w+),\s+(\w+)', instr):
            x, y = m.groups()
            registers[x] += get_value(y)
        elif m := re.match(r'sub\s+(\w+),\s+(\w+)', instr):
            x, y = m.groups()
            registers[x] -= get_value(y)
        elif m := re.match(r'mul\s+(\w+),\s+(\w+)', instr):
            x, y = m.groups()
            registers[x] *= get_value(y)
        elif m := re.match(r'div\s+(\w+),\s+(\w+)', instr):
            x, y = m.groups()
            registers[x] //= get_value(y)
        elif m := re.match(r'jmp\s+(\w+)', instr):
            label, = m.groups()
            ip = labels[label]
            continue
        elif m := re.match(r'cmp\s+(\w+),\s+(\w+)', instr):
            x, y = m.groups()
            cmp_cache = get_value(x) - get_value(y)
        elif m := re.match(r'jne\s+(\w+)', instr):
            label, = m.groups()
            if cmp_cache:
                ip = labels[label]
                continue
        elif m := re.match(r'je\s+(\w+)', instr):
            label, = m.groups()
            if not cmp_cache:
                ip = labels[label]
                continue
        elif m := re.match(r'jge\s+(\w+)', instr):
            label, = m.groups()
            if cmp_cache >= 0:
                ip = labels[label]
                continue
        elif m := re.match(r'jg\s+(\w+)', instr):
            label, = m.groups()
            if cmp_cache > 0:
                ip = labels[label]
                continue
        elif m := re.match(r'jle\s+(\w+)', instr):
            label, = m.groups()
            if cmp_cache <= 0:
                ip = labels[label]
                continue
        elif m := re.match(r'jl\s+(\w+)', instr):
            label, = m.groups()
            if cmp_cache < 0:
                ip = labels[label]
                continue
        elif m := re.match(r"msg\s+((?:\w+|'[^']+')(?:,\s+(?:\w+|'[^']+'))*)", instr):
            # We assume that strings do not contain any single quote
            args, = m.groups()
            in_string = False
            buffer = ''
            for c in args:
                if c == "'":
                    in_string = not in_string
                elif in_string:
                    output += c
                elif re.match(r'[\w-]', c):
                    buffer += c
                else:
                    if buffer:
                        output += str(get_value(buffer))
                        buffer = ''
                    if c == ';':
                        break
            if buffer:
                output += str(get_value(buffer))
        elif m := re.match(r'call\s+(\w+)', instr):
            label, = m.groups()
            call_stack.append(ip)
            ip = labels[label]
            continue
        elif re.match(r'ret', instr):
            ip = call_stack.pop()
        elif re.match(r'end', instr):
            return output

        ip += 1

    return -1
