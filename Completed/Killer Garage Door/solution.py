import io


def controller(events: str) -> str:
    position = 0
    direction = 0
    paused = False
    res = io.StringIO()
    for event in events:
        if event == 'P':
            if position == 0:
                direction = 1
                paused = False
            elif position == 5:
                direction = -1
                paused = False
            else:
                paused = not paused
        elif not paused and event == 'O':
            direction = -direction
        if not paused:
            position += direction
            paused = position % 5 == 0
        res.write(str(position))
    return res.getvalue()
