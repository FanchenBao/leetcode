# from pudb import set_trace; set_trace()
from typing import List, Set


class Solution1:
    def canReach(self, arr: List[int], start: int) -> bool:
        """66% ranking.

        Standard DFS with backtracking with a set to record which indices have
        been visited.
        """
        seen = set()

        def dfs(idx: int, seen: Set[int]) -> bool:
            if idx in seen:
                return False
            if arr[idx] == 0:
                return True
            c1, c2 = False, False
            seen.add(idx)
            if idx + arr[idx] < len(arr):
                c1 = dfs(idx + arr[idx], seen)
            if idx - arr[idx] >= 0:
                c2 = dfs(idx - arr[idx], seen)
            if c1 or c2:
                return True
            seen.remove(idx)  # backtracking
            return False

        return dfs(start, seen)


class Solution2:
    def canReach(self, arr: List[int], start: int) -> bool:
        """Same idea but a bit more elegant.

        Two improvements to the previous method.
        1. We can deligate the check on idx at the beginning of the recursion
        function instead of before making the recursion call. This simplifies
        the logic of the recursion body itself.
        2. There is no need to backtrack, because once an idx has been visited,
        it will not be visited again. Backtracking is useless in this sense.

        Finally, this solution is O(N) in space complexity because an additional
        set is used to record which indices have been visited. If a O(1) space
        complexity is needed, the official solution suggests making changes
        directly to arr by turning the value negative when it is visited.
        """
        seen = set()

        def dfs(idx: int, seen: Set[int]) -> bool:
            if idx not in seen and 0 <= idx < len(arr):
                if arr[idx] == 0:
                    return True
                seen.add(idx)
                return dfs(idx + arr[idx], seen) or dfs(idx - arr[idx], seen)
            return False

        return dfs(start, seen)


sol = Solution2()
tests = [
    ([4, 2, 3, 0, 3, 1, 2], 5, True),
    ([4, 2, 3, 0, 3, 1, 2], 0, True),
    ([3, 0, 2, 1, 2], 2, False),
]

for i, (arr, start, ans) in enumerate(tests):
    res = sol.canReach(arr, start)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
