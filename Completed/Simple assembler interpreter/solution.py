def simple_assembler(program: list[str]) -> dict[str, int]:
    registers = {}
    ip = 0

    def get_value(r: str) -> int:
        if r in registers:
            return registers[r]
        return int(r)

    while ip < len(program):
        match program[ip].split():
            case ['mov', x, y]:
                registers[x] = get_value(y)
            case ['inc', x]:
                registers[x] += 1
            case ['dec', x]:
                registers[x] -= 1
            case ['jnz', x, y]:
                if get_value(x):
                    ip += get_value(y) - 1
        ip += 1

    return registers
