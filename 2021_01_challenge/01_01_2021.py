# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """Since everything is unique in arr and pieces, that makes things a
        lot easier. We first create a dict with pieces, in which the key is
        the first number of each piece and the value is the remaining piece.

        Then we iterate through arr. The first number in arr must be one of the
        keys. Once it is matched, we walk through the remaining piece and arr
        to make sure each pair of numbers match.

        If any mistmatch happens, either between an arr number with the key or
        the walk through, return False. Otherwise, we return True at the end.

        O(N), 44 ms, 42 % ranking.
        """
        piece_dict = {p[0]: p[1:] for p in pieces}
        i = 0
        while i < len(arr):
            cur = arr[i]
            if cur not in piece_dict:
                return False
            for next_val in piece_dict[cur]:
                i += 1
                if next_val != arr[i]:
                    return False
            i += 1
        return True


class Solution2:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """The smart-ass solution.
        
        O(N), 40 ms, 73% ranking.
        """
        piece_dict = {p[0]: p for p in pieces}
        res = []
        for a in arr:
            res += piece_dict.get(a, [])
        return res == arr


sol = Solution2()
tests = [
   ([85], [[85]], True),
   ([15, 88], [[88], [15]], True),
   ([49, 18, 16], [[16, 18, 49]], False),
   ([91, 4, 64, 78], [[78], [4, 64], [91]], True),
   ([1, 3, 5, 7], [[2, 4, 6, 8]], False),
]

for i, (arr, pieces, ans) in enumerate(tests):
    res = sol.canFormArray(arr, pieces)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
