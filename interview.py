# from pudb import set_trace; set_trace()
from collections import defaultdict
import math


def solution(numbers):
    max_even = max_odd = -math.inf  # number can be negative
    for n in numbers:
        if n % 2:
            max_odd = max(max_odd, n)
        else:
            max_even = max(max_even, n)
    if max_even == -math.inf:
        max_even = 0
    if max_odd == -math.inf:
        max_odd = 0
    return max_even + max_odd


# tests = [([randint(-1000000000, 1000000000) for _ in range(1000)], 0) for _ in range(5)]
tests = [
    ([5, 3, 10, 6, 11], 21),
    ([20, 10, 7, 5], 27),
    ([7, 13, 15, 13], 15),
    ([2, 6, 4, 6], 6),
    ([1], 1),
    ([2], 2),
    ([1, 2], 3),
    ([-1], -1),
    ([-1, -2], -3),
]

for i, (numbers, ans) in enumerate(tests):
    res = solution(numbers)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')



