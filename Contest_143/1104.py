from math import log

"""
06/29/2019

Not difficult, but it was a bit complicated to accurately compute the index of a given lable
and the lable of a given index. Once these two computation was available, finding the route
was easy.
"""


class Solution:
    def pathInZigZagTree(self, label: int):
        pos = (self.locatePos(label) - 1) // 2
        res = [label]
        while pos >= 0:
            res.insert(0, self.findLable(pos))
            pos = (pos - 1) // 2
        return res

    def findLable(self, p):
        lvl = int(log(p + 2, 2))
        if 2 ** lvl < p + 2:
            lvl += 1
        if lvl % 2:
            return p + 1
        else:
            startPos = 2 ** (lvl - 1) - 1
            step = p - startPos
            return 2 ** lvl - 1 - step

    def locatePos(self, num):
        lvl = int(log(num + 1, 2))
        if 2 ** lvl < num + 1:
            lvl += 1
        if lvl % 2:  # odd level
            return num - 1
        else:
            start = 2 ** lvl - 1
            step = start - num
            return 2 ** (lvl - 1) + step - 1


sol = Solution()
print(sol.pathInZigZagTree(26))
