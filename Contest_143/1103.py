"""
06/29/2019

Straightforward solution. Notice that count cannot be used to indicate index. I had to
use a separate index variable to achieve that.
"""


class Solution:
    def distributeCandies(self, candies, num_people):
        res = [0] * num_people
        count = 1
        index = 0
        while True:
            if candies >= count:
                res[index % num_people] += count
                candies -= count
            else:
                res[index % num_people] += candies
                break
            count += 1
            index += 1
        return res


sol = Solution()
print(sol.distributeCandies(10, 3))
