# from pudb import set_trace; set_trace()
from typing import List
from itertools import product


class Solution1:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        """LeetCode 816

        We first apply commas to divide s into two substrings of digits. If
        both the l and r string digits are themselves integers, that is a result
        already.

        Then, we partition the l and r into possible decimals, respectively.
        The rule for decimals is that after the partition, the left portion of
        the decimal is a valid integer, and the right portion does not end with
        '0'.

        After obtaining the valid decimals for the l and r, we assemble the rest
        of the result. If l is a valid integer, we add all valid right decimals
        to it. Same with when r is a valid integer. Finally, we add all
        combinations of the left and right decimals.

        For complexity analysis, see solution2. 48 ms, 61% ranking.
        """
        work_str = s[1:-1]
        all_commas = [[work_str[:i], work_str[i:]] for i in range(1, len(work_str))]
        res = []
        for l, r in all_commas:
            lint = str(int(l)) == l
            rint = str(int(r)) == r
            if lint and rint:
                res.append(f'({l}, {r})')
            l_deci = []
            for i in range(1, len(l)):
                lt, rt = l[:i], l[i:]
                if str(int(lt)) == lt and rt[-1] != '0':
                    l_deci.append(lt + '.' + rt)
            r_deci = []
            for i in range(1, len(r)):
                lt, rt = r[:i], r[i:]
                if str(int(lt)) == lt and rt[-1] != '0':
                    r_deci.append(lt + '.' + rt)
            if lint:
                for rd in r_deci:
                    res.append(f'({l}, {rd})')
            if rint:
                for ld in l_deci:
                    res.append(f'({ld}, {r})')
            for ld in l_deci:
                for rd in r_deci:
                    res.append(f'({ld}, {rd})')
        return res


class Solution2:
    def make(self, frag: str):
        n = len(frag)
        for i in range(1, n + 1):
            l, r = frag[:i], frag[i:]
            if (l == '0' or not l.startswith('0')) and not r.endswith('0'):
                # check for integer and decimal is combined
                yield l + ('.' if i != n else '') + r

    def ambiguousCoordinates(self, s: str) -> List[str]:
        """This is the official solution.

        https://leetcode.com/problems/ambiguous-coordinates/solution/

        The same idea, but I think it has a better implementation. Because it
        does not separate the integer check and decimal check into two different
        steps. Instead, it combines the two, thus we can call itertools.product
        when we obtain the final result.

        Also, the use of yield is definitely a good touch.

        Regarding complexity, lee215 has a good formula to follow:
        https://leetcode.com/problems/ambiguous-coordinates/discuss/123851/C%2B%2BJavaPython-Solution-with-Explanation

        In the outer loop, we go with 1, 2, 3, ..., n
        In the inner loop, self.make(l) has O(i), self.make(r) has O(n - i)
        Thus, the product has O(i(n - i))
        Thus, the total is 1(n - 1) + 2(n - 2) + 3(n - 3) + .. + (n - 1) = O(N^3)

        Someone says its O(N^4), because they count string building as O(N). I
        don't think so.
        """
        work_str = s[1:-1]
        res = []
        for l, r in [[work_str[:i], work_str[i:]] for i in range(1, len(work_str))]:
            for c1, c2 in product(self.make(l), self.make(r)):
                res.append(f'({c1}, {c2})')
        return res


sol = Solution2()
tests = [
    ('(0123)', ['(0, 123)', '(0, 12.3)', '(0, 1.23)', '(0.1, 23)', '(0.1, 2.3)', '(0.12, 3)']),
    ('(123)', ['(1, 23)', '(12, 3)', '(1.2, 3)', '(1, 2.3)']),
    ('(00011)', ['(0.001, 1)', '(0, 0.011)']),
    ('(100)', ['(10, 0)']),
    ('(00000001)', ['(0, 0.000001)']),
]

for i, (s, ans) in enumerate(tests):
    res = sol.ambiguousCoordinates(s)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
