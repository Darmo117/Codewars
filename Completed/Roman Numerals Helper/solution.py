class RomanNumerals:
    DEC_TO_ROM = ('IV', 'XL', 'CD', 'M-')
    ROM_TO_DEC = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    @classmethod
    def to_roman(cls, n):
        res = ''
        i = 0

        while n > 0:
            q, r = divmod(n, 10)
            unit, five = cls.DEC_TO_ROM[i]
            i += 1
            if r < 4:
                res = unit * r + res
            elif r == 4:
                res = unit + five + res
            elif r == 9:
                res = unit + cls.DEC_TO_ROM[i][0] + res
            elif r > 4:
                res = five + unit * (r - 5) + res
            n = q

        return res

    @classmethod
    def from_roman(cls, rn):
        print(rn)
        res = 0
        digits = list(rn)

        i = 0
        while i < len(digits):
            d = digits[i]
            v = cls.ROM_TO_DEC[d]
            res += v
            if d in 'IXCM' and i < len(digits) - 1:
                up = cls.ROM_TO_DEC[digits[i + 1]]
                if v * 5 == up or v * 10 == up:
                    res += up - 2 * v
                    i += 1
            i += 1

        return res
