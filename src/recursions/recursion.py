class Recursion:

    # store lists as class variables
    numbers = [ 9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]

    numb_2 = [  8, 10, 2, 14, 4]

    numb_3 = [  260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
                318, 303, 153, 290, 201, 594, 457, 607, 592, 246
    ]
    numb_4 = [  260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
                318, 303, 153, 290, 201, 594, 457, 607, 592, 246,
                132, 135, 584, 432, 591, 204, 417, 405, 362, 658,
                136, 751, 583, 536, 293, 493, 431, 780, 563, 703,
                400, 618, 397, 320, 513, 708, 319, 317, 685, 347,
                758, 439, 145, 378, 158, 384, 551, 110, 408, 648,
                847, 498,  50,  19,     # 64 numbers
    ]


    def __init__(self):
        """
        Constructor.
        """

    def sum(self, _numbers) -> int:
        if not _numbers:                    
            return 0
        n1, r = _numbers[0], _numbers[1:]   # reduction: first number + remaining list
        return n1 + self.sum(r)


    def fib(self, _n) -> int:
        if _n < 2:
            return _n
        return self.fib(_n - 1) + self.fib(_n - 2)

    def fib_memo(self, _n, memo=None) -> int:
        if memo is None:
            memo = {}
        if _n < 2:
            return _n
        if _n not in memo:
            memo[_n] = self.fib_memo(_n - 1, memo) + self.fib_memo(_n - 2, memo)
        return memo[_n]

    def fib_gen(self, _n):
        memo = {}
        yield (list(range(_n + 1)), [self.fib_memo(i, memo) for i in range(_n + 1)])


    def perm(self, _numbers) -> list:
        res = []
        if len(_numbers) <= 1:
            return [list(_numbers)]
        for i, n1 in enumerate(_numbers):
            r = _numbers[:i] + _numbers[i + 1:]
            for p in self.perm(r):
                res.append([n1] + p)
        return res


    def pset(self, _numbers) -> list:
        res = []
        if not _numbers:
            return [[]]
        n1, r = _numbers[0], _numbers[1:]
        for sub in self.pset(r):
            res.append(sub)
            res.append([n1] + sub)
        return res


    def find(self, _numbers, match_func) -> list:
        res = []
        for n in _numbers:
            if match_func(n):
                res.append(n)
        return res


    def find_adjacent(self, pair, _numbers, _i=0) -> list:
        res = []
        for i in range(_i, len(_numbers) - 1):
            if [_numbers[i], _numbers[i + 1]] == list(pair):
                res.append(i)
        return res


    def find_pairs(self, n, _numbers) -> list:
        res = []
        for i, a in enumerate(_numbers):
            for b in _numbers[i + 1:]:
                if a + b == n:
                    pair = sorted([a, b])
                    if pair not in res:
                        res.append(pair)
        return res


    def find_all_sums(self, n, _numbers) -> list:
        if n <= 0 or not _numbers:
            return []
        n1, r = _numbers[0], _numbers[1:]
        res = []
        if n1 == n:
            res.append([n1])
        elif n1 < n:
            for sol in self.find_all_sums(n - n1, r):
                res.append([n1] + sol)
        res += self.find_all_sums(n, r)
        seen, unique = set(), []
        for sol in res:
            key = tuple(sorted(sol))
            if key not in seen:
                seen.add(key)
                unique.append(sol)
        return unique
