def last_digit(n, e):
    if e == 0:
        return 1
    match n % 10:
        case (0 | 1 | 5 | 6) as d:
            return d
        case 2:
            d = e % 100 / 4 % 1  # Keep last 2 digits of exponent, divide by 4 then keep only decimal part
            return {
                0.00: 6,
                0.25: 2,
                0.50: 4,
                0.75: 8,
            }[d]
        case 3:
            d = e % 100 / 4 % 1
            return {
                0.00: 1,
                0.25: 3,
                0.50: 9,
                0.75: 7,
            }[d]
        case 4:
            return 4 if e % 2 == 1 else 6
        case 7:
            d = e % 100 / 4 % 1
            return {
                0.00: 1,
                0.25: 7,
                0.50: 9,
                0.75: 3,
            }[d]
        case 8:
            d = e % 100 / 4 % 1
            return {
                0.00: 6,
                0.25: 8,
                0.50: 4,
                0.75: 2,
            }[d]
        case 9:
            return 9 if e % 2 == 1 else 1
