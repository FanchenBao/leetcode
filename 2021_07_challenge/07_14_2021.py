# from pudb import set_trace; set_trace()
from typing import List
import collections


class Solution1:
    def customSortString(self, order: str, str: str) -> str:
        """LeetCode 791

        Feel like cheating, but custom sort is what Python provides. All we
        need to do is to provide a new order based on the given order. The new
        order will be passed to the key argument such that Python's sort can
        handle the custom sort for us.

        O(NlogN), 24 ms, 96% ranking.
        """
        order_map = {o: i for i, o in enumerate(order)}
        return ''.join(sorted(str, key=lambda ele: order_map.get(ele, 26)))


class Solution2:
    def customSortString(self, order: str, str: str) -> str:
        order_map = {o: i for i, o in enumerate(order)}
        to_sort, not_sort = [], ''
        for s in str:
            if s in order_map:
                to_sort.append(order_map[s])
            else:
                not_sort += s
        return ''.join([order[i] for i in sorted(to_sort)]) + not_sort


class Solution3:
    def customSortString(self, order: str, str: str) -> str:
        """The essence of sorting is to pick out the element in str that follows
        the same order as in order. Thus, we can iterate through order, and for
        each letter, we can see how many exist in str. We simply extract those
        letters from str and the new string thus created is sorted based on the
        order.

        Reference: https://leetcode.com/problems/custom-sort-string/discuss/1336811/Python-Counter-solution-explained

        O(N), 24 ms
        """
        counter = collections.Counter(str)
        res = ''
        for o in order:
            if o in counter:
                res += o * counter[o]
                counter.pop(o)
        return res + ''.join(k * v for k, v in counter.items())


sol = Solution3()
tests = [
    ('cba', 'abcd', 'cbad'),
    ('cba', '', ''),
    ('', '', '')
]

for i, (order, str, ans) in enumerate(tests):
    res = sol.customSortString(order, str)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
