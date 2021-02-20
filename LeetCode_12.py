# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    data = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
        4: 'IV',
        9: 'IX',
        40: 'XL',
        90: 'XC',
        400: 'CD',
        900: 'CM',
    }

    def intToRoman(self, num: int) -> str:
        """This one is full on DP. We are building up data as more numbers are
        fed to this algorithm. Everytime, we take the trailing values of a
        number. For instance, given 1994, we take 4, 90, 900, and 1000. For
        each trailing number, we check if it is in data already. If not, we
        assemble it by substracting the smallest unit proportional to the
        trailing number itself. For instance, given 8, it will be subtracted by
        1 as the smallest unit. Given 80, it will be subtracted by 10.

        Eventually, all the Roman symbols are pushed to a stack, which we can
        reverse and join to find the answer.

        O(N), 52 ms, 56% ranking.
        """
        tens, temp = 10, num
        stack = []
        while temp:
            cur = temp % tens
            temp -= cur
            t_stack, t_cur = [], cur
            while t_cur:
                if t_cur in self.data:
                    t_stack.append(self.data[t_cur])
                    break
                t_cur -= tens // 10  # substract from the current unit
                t_stack.append(self.data[tens // 10])
            if cur not in self.data:
                self.data[cur] = ''.join(t_stack[::-1])
            stack.append(self.data[cur])
            tens *= 10
        self.data[num] = ''.join(stack[::-1])
        return self.data[num]


class Solution2:
    def intToRoman(self, num: int) -> str:
        """A much much cleaner solution. We subtract from the biggest to
        smallest. No need to be concerned with a DP data.

        O(N), 52 ms.
        """
        units = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sybls = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i, res = 0, ''
        while num:
            if num >= units[i]:
                num -= units[i]
                res += sybls[i]
            else:
                i += 1
        return res


sol = Solution2()
tests = [
    (3, 'III'),
    (4, 'IV'),
    (6, 'VI'),
    (9, 'IX'),
    (11, 'XI'),
    (58, 'LVIII'),
    (1994, 'MCMXCIV'),
]

for i, (num, ans) in enumerate(tests):
    res = sol.intToRoman(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
