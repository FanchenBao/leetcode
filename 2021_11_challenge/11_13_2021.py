# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """LeetCode 739

        DP, going from back to front. We record two arrays. One is for answer,
        recording the number of days to wait until encountering a higher temp
        in the future. The other is the corresponding index of that higher-temp
        day. For any given day, we check the next day. If its temp is higher,
        we are done. If its temp is lower, we obtain the first day in the
        future that has higher temp than the next day, and compare the current
        day to that future date. We keep doing this, until we find a day that
        has higher temp than current, or nothing. Along the way, we keep track
        the number of days each jump accumulates.

        On average, this is O(N). 1288 ms, 45% ranking.

        UPDATE: this solution can be further optimized to achieve O(1) extra
        space. Since I already record the number of days to reach the next higer
        temp, I can compute the next higher temp's index. This means, I do not
        have to maintain a separate list for it.
        """
        N = len(temperatures)
        res = [0] * N
        for i in range(N - 2, -1, -1):
            j = i + 1
            while res[j] and temperatures[j] <= temperatures[i]:
                j += res[j]
            res[i] = (j - i) * (temperatures[j] > temperatures[i])
        return res


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Monotonic stack. From the official solution"""
        N = len(temperatures)
        stack, res = [], [0] * N
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                pi, pt = stack.pop()
                res[pi] = i - pi
            stack.append((i, t))
        return res


sol = Solution1()
tests = [
    ([73,74,75,71,69,72,76,73],[1,1,4,2,1,1,0,0]),
    ([30,40,50,60],[1,1,1,0]),
    ([30,60,90],[1,1,0]),
    ([50], [0]),
    ([50, 50, 50], [0, 0, 0]),
]

for i, (temperatures, ans) in enumerate(tests):
    res = sol.dailyTemperatures(temperatures)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
