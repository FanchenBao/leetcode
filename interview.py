# from pudb import set_trace; set_trace()
from collections import defaultdict
import math


def solution(inputArray):
    diff = [inputArray[i + 1] - inputArray[i] for i in range(len(inputArray) - 1)]
    res = cur_max = 0
    # Kadane
    for d in diff:
        cur_max = max(cur_max + d, d)
        res = max(res, cur_max)
    return res

    
# tests = [([randint(-1000000000, 1000000000) for _ in range(1000)], 0) for _ in range(5)]
tests = [
    ([2,3,10,6,4,8,1], 8),
    ([4,3,1], 0),
]

for i, (inputArray, ans) in enumerate(tests):
    res = solution(inputArray)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')



