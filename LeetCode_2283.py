# from pudb import set_trace; set_trace()
from typing import List
from collection import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        """
        O(N), 44 ms, faster than 70.63%
        """
        counter = Counter(num)
        return all(counter[str(i)] == int(dig) for i, dig in enumerate(num))

        

sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
