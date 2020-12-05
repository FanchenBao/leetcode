# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Check even and odd positions. O(n). 160 ms, 73% ranking.
        """
        odd_can, even_can = 0, 0
        length = len(flowerbed)
        for i in range(0, length, 2):  # check even indices
            if not flowerbed[i]:
                cond1 = i == 0 or not flowerbed[i - 1]
                cond2 = i == length - 1 or not flowerbed[i + 1]
                if cond1 and cond2:
                    even_can += 1
        for i in range(1, length, 2):  # check odd indices
            if not flowerbed[i]:
                cond1 = not flowerbed[i - 1]
                cond2 = i == length - 1 or not flowerbed[i + 1]
                if cond1 and cond2:
                    odd_can += 1
        return odd_can >= n or even_can >= n


class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Greedy. O(n), 164 ms, 58% ranking.

        To prove greedy, we need to show that given two consecutive empty spots,
        we can always plant in the first empty spot to achieve best result.

        Let's assume the two empty spots are i and i + 1. Suppose we choose to
        plant at i + 1 and achieve more fllowers than planting at i. This means
        the number of flowers planted from i + 3 to end is more than the
        number of flowers planted from i + 2 to end. This is not possible
        because latter covers more range than former. Therefore, it is
        impossible to plant at i + 1 to reach better result than planting at i.

        Hence, we can use greedy, i.e. as soon as we find an empty pot that
        satisfies the requirement, we plant a flower.
        """
        count = 0
        for i in range(len(flowerbed)):
            if not flowerbed[i] and (i == 0 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]):
                flowerbed[i] = 1
                count += 1
        return count >= n


sol = Solution2()
tests = [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),
    ([1], 1, False),
    ([0], 1, True),
]

for i, (flowerbed, n, ans) in enumerate(tests):
    res = sol.canPlaceFlowers(flowerbed, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
