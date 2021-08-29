# from pudb import set_trace; set_trace()
from random import randint
import math
import sys


def solution(A) -> int:
    # sys.stderr.write(
    #   'Tip: Use sys.stderr.write() to write debug messages on the output tab.\n'
    # )
    sorted_A = sorted(A)
    i, j = 0, len(A) - 1
    res = -math.inf
    while i < j:
        res = max(res, sorted_A[i] + sorted_A[j])
        i += 1
        j -= 1
    return res


tests = [([randint(-1000000000, 1000000000) for _ in range(1000)], 0) for _ in range(5)]
# tests = [
#     (12001, 11),
#     (510, 5),
#     (7007, 0),
# ]

for i, (A, ans) in enumerate(tests):
    res = solution(A)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {A}')



