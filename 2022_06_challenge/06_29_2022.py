# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """LeetCode 406

        This is brute force. We sort people by height in desc. If heights are
        the same, we sort by order in asce. The idea is that when the current
        height is being considered, everyone to the left is taller or equal to
        the current height, and everyone to the right is shorter to the current
        height. Thus, the position of the current height can be directly
        determiend by its order. We just need to insert it to that position.

        O(N^2), 157 ms, faster than 52.05%
        """
        people.sort(key=lambda tup: (-tup[0], tup[1]))
        res = []
        for tup in people:
            if tup[1] >= len(res):
                res.append(tup)
            else:
                res.insert(tup[1], tup)
        return res
        

sol = Solution()
tests = [
    ([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]], [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]),
    ([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]], [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]),
]

for i, (people, ans) in enumerate(tests):
    res = sol.reconstructQueue(people)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
