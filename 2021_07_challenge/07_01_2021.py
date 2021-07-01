# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def __init__(self):
        self.res = [[0]]
        for i in range(1, 17):
            temp = self.res[i - 1]
            add_on = 2**(i - 1)
            self.res.append(temp + [add_on + t for t in temp[::-1]])

    def grayCode(self, n: int) -> List[int]:
        """LeetCode 89

        To obtain the grey code for n, we look at the grey code of n - 1. All
        we need to do is to reverse the grey code of n - 1, and add 2^(n - 1) to
        each value in the reversed grey code. Then we concatenate the two arrays
        and we have the new grey code for n.

        O(2^N) if we compute each grey code from scratch. We can also do one
        computation at the beginning and store the result, which will make it
        faster. 144 ms, 28% ranking.
        """
        return self.res[n]


class Solution2:
    def grayCode(self, n: int) -> List[int]:
        """Same solution but compute from scratch each time.

        96 ms, 96% ranking.
        """
        res = [0]
        for i in range(n):
            res += [r | 1 << i for r in res[::-1]]
        return res


class Solution3:
    def grayCode(self, n: int) -> List[int]:
        """Approach 5 in the official solution. It is not easy to find the
        pattern that i ^ G(i) = i // 2, and then the task of proving that
        G(i) = i ^ (i >> 1) is also not trivial. But it is a good practice for
        understanding XOR and also a good read on the proof.
        """
        return [i ^ (i >> 1) for i in range(2**n)]


sol = Solution3()
tests = [
    (2, [0, 1, 3, 2]),
    (1, [0, 1]),
]

for i, (n, ans) in enumerate(tests):
    res = sol.grayCode(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
