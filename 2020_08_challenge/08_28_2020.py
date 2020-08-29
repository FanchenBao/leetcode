# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def rand3(self):
        res = rand7() % 4
        return res if res else self.rand3()
            
    def rand10(self):
        """This approach works but with hideous performance"""
        ref = {111: 1, 112: 2, 113: 3, 121: 4, 122: 5, 123: 6, 131: 7, 132: 8, 133: 9, 211: 10}
        val = self.rand3() * 100 + self.rand3() * 10 + self.rand3()
        return ref[val] if val in ref else self.rand10()


class Solution2:
    def rand10(self):
        """This approach works too, but still with hideous performance"""
        res = int(str(rand7() - 1) + str(rand7() - 1), 7)
        while res > 10:
            res = int(str(rand7() - 1) + str(rand7() - 1), 7)
        return res


class Solution3:
    def rand10(self):
        """
        This is a similar method as Solution2, but much more efficient.

        The official name for this method is rejection sampling.
        """
        while True:
            i, j = rand7(), rand7()
            ref = 7 * (i - 1) + j
            if ref <= 40:
                return ref % 10 + 1


class Solution4:
    def rand10(self):
        """
        This method builds on top of Solution3. Instead of rejecting every value
        that is larger than 40, we can observe that any value in the range 41 to
        49 are also equally distributed. In other words, we have created a
        rand9() in that case. Then we simply call rand7() again, and this time
        we have 9 x 7 = 63 numbers to choose. If the value is between 61 to 63,
        we have created a rand3(). Then we call rand7() again, and this time
        we have 3 x 7 = 21 numbers to choose. If the value is 21, we start over.
        """
        while True:
            i, j = rand7(), rand7()
            ref = 7 * (i - 1) + j  # 49 numbers to choose from
            if ref <= 40:
                break
            else:
                m = rand7()
                ref = 7 * (ref % 10 - 1) + m  # 63 numbers to choose from
                if ref <= 60:
                    break
                else:
                    n = rand7()
                    ref = 7 * (ref % 10 - 1) + n  # 20 numbers to choose from
                    if ref <= 20:
                        break
        return ref % 10 + 1


class Solution5:
    def rand10(self):
        """Use septenary numbers exclusively. The ith call of rand7() produces
        a uniformly distributed number from 0 to 7**i - 1. If the number is
        smaller than 7**i // 10 * 10 - 1, then the number mod 10 can produce a
        uniformly distributed sampling from 0 to 9. If the number is larger
        than 7**i // 10 * 10 - 1, performing mod 10 will lead to bias (the mod
        10 of values larger than 7**i // 10 * 10 - 1 have higher likelihood of
        getting sampled). Thus, we do another call of rand7().
        """
        ref, i = rand7() - 1, 2
        while True:
            ref = ref * 7 + rand7() - 1
            if ref <= 7**i // 10 * 10 - 1:
                return ref % 10 + 1
            i += 1
