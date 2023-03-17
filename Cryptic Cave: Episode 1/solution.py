def podium_code():
    return ''.join(f'{i // 60}:{i % 60:02}\n' for i in range(720))
