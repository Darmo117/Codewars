def goto(level, button) -> int:
    if not isinstance(level, int) or not isinstance(button, str):
        return 0
    button = int(button)
    if not (0 <= button <= 3) or not (0 <= level <= 3):
        return 0
    return button - level
