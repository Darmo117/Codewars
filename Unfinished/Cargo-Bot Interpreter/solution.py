import copy

if __name__ == '__main__':
    import collections as colls

    Crate = colls.namedtuple('Crate', ('color',))
    Command = colls.namedtuple('Command', ('command', 'flag'))


# noinspection PyUnboundLocalVariable
def cargobot(initial_state: list[list[Crate]], programs: list[list[Command]], max_steps: int) -> list[list[Crate]]:
    print(initial_state, programs, max_steps)
    state = copy.deepcopy(initial_state)
    claw_state: Crate | None = None
    claw_pos = 0
    i = 0

    def run(program: list[Command], index: int):
        nonlocal claw_pos, claw_state, i

        for instr in program:
            if i > max_steps:
                break
            print(instr, claw_state, claw_pos, state)
            match instr.command, instr.flag:
                case ['LEFT', flag]:
                    if not flag or not claw_state and flag == 'NONE' or claw_state and (
                            flag == 'ANY' or flag == claw_state.color):
                        claw_pos = max(0, claw_pos - 1)
                case ['RIGHT', flag]:
                    if not flag or not claw_state and flag == 'NONE' or claw_state and (
                            flag == 'ANY' or flag == claw_state.color):
                        claw_pos = min(len(state) - 1, claw_pos + 1)
                case ['DOWN', flag]:
                    print(flag)
                    if claw_state and (not flag or flag == 'ANY' or flag == claw_state):
                        state[claw_pos].append(claw_state)
                        claw_state = None
                    elif not claw_state and state[claw_pos] and (not flag or flag == 'NONE'):
                        claw_state = state[claw_pos].pop()
                case [prog, flag] if index == 1:
                    if not flag or not claw_state and flag == 'NONE' or claw_state and (
                            flag == 'ANY' or claw_state.color == flag):
                        prog_id = int(prog[-1])
                        run(programs[prog_id - 1], prog_id)
            i += 1
        print(claw_state, claw_pos, state)

    run(programs[0], 1)

    print(claw_state, claw_pos, state)
    return state


if __name__ == '__main__':
    cargobot([[Crate(color='YELLOW'), Crate(color='RED')], [Crate(color='BLUE')], []], [
        [Command(command='DOWN', flag=None), Command(command='RIGHT', flag=None), Command(command='DOWN', flag=None)],
        [], [], []], 3)
