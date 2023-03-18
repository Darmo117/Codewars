def running_pace(distance: int, time: str) -> str:
    h, m = map(int, time.split(':'))
    minutes = h * 60 + m
    pace = int(minutes // distance)
    return f'{pace // 60}:{pace % 60:02}'
