import math

_WORDS = {
    # English
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    # German
    "null": 0, "eins": 1, "ein": 1, "zwei": 2, "drei": 3, "vier": 4,
    "fünf": 5, "fuenf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
    "zehn": 10,
    # Spanish
    "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
    "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
    # Russian
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4,
    "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
    "десять": 10,
    # Chinese
    "零": 0, "一": 1, "二": 2, "三": 3, "四": 4,
    "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
}

_ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
          "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10}


class Calculator(object):
    _instance = None

    # Singleton pattern by overriding __new__, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def _num(self, x):
        """Convert int, float, None or a numeric string/word to a number.

        None and unparseable strings default to 0.
        """
        if x is None:
            return 0
        if isinstance(x, (int, float)) and not isinstance(x, bool):
            return x
        if isinstance(x, str):
            s = x.strip()
            if s.upper() in _ROMAN:
                return _ROMAN[s.upper()]
            if s.lower() in _WORDS:
                return _WORDS[s.lower()]
            try:
                return int(s)
            except ValueError:
                pass
            try:
                return float(s)
            except ValueError:
                return 0
        raise ValueError(f"cannot interpret {x!r} as a number")

    def add(self, a, b):
        return self._num(a) + self._num(b)

    def sub(self, a, b):
        return self._num(a) - self._num(b)

    def mul(self, a, b):
        return self._num(a) * self._num(b)

    def div(self, a, b):
        a, b = self._num(a), self._num(b)
        if b == 0:
            return math.nan if a == 0 else math.copysign(math.inf, a)
        return a / b

    def factorize(self, n):
        n = self._num(n)
        if isinstance(n, float) and n.is_integer():
            n = int(n)
        if not isinstance(n, int) or n < 2:
            return []
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1 if d == 2 else 2
        if n > 1:
            factors.append(n)
        return factors
