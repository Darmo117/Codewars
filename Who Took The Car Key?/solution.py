def who_took_the_car_key(message: list[str]) -> str:
    return ''.join(chr(int(s, 2)) for s in message)
