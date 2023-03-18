def scoreboard(who_ate_what: list[dict]) -> list[dict]:
    return sorted([
        {
            'name': entry['name'],
            'score': 5 * entry.get('chickenwings', 0) + 3 * entry.get('hamburgers', 0) + 2 * entry.get('hotdogs', 0)
        }
        for entry in who_ate_what
    ], key=lambda d: (-d['score'], d['name']))
