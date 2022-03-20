# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_point = 0
        bob_arrow = None
        for s in range(1 << 12):
            str_s = f'{s:012b}'
            point = 0
            temp_arrow = [0] * 12
            for i in range(12):
                if str_s[i] == '1':
                    temp_arrow[i] = aliceArrows[i] + 1
                    point += i
            arrows_used = sum(temp_arrow)
            # Note that Bob could use fewer than needed arrows. In this case,
            # we simply dump the unused arrows to position 0.
            if arrows_used <= numArrows and point > max_point:
                max_point = point
                temp_arrow[0] += numArrows - arrows_used
                bob_arrow = temp_arrow
        return bob_arrow
        
        
sol = Solution()
tests = [
    (9, [1,1,0,1,0,0,2,1,0,1,2,0], [0,0,0,0,1,1,0,0,1,2,3,1]),
    (3, [0,0,1,0,0,0,0,0,0,0,0,2], [0,0,0,0,0,0,0,0,1,1,1,0]),
    (89, [3,2,28,1,7,1,16,7,3,13,3,5], [21,3,0,2,8,2,17,8,4,14,4,6]),
]

for i, (numArrows, aliceArrows, ans) in enumerate(tests):
    res = sol.maximumBobPoints(numArrows, aliceArrows)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
