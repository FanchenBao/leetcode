# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """LeetCode 954

        First, we get all the odd numbers out and create a counter for all
        the even numbers (even_count). Since the odd numbers can only be
        mulitplied, we can check whether 2 * odd is in even_count. If it is, we
        decrement even_count. Otherwise, we can return False immediately.

        After checking the odd numbers, we now check the even numbers. Note that
        we can have both positive and negative even numbers. The good thing is
        that the positive even number can only be paired with other positive
        even numbers, and same for the negative. Thus, we can write one function
        to check both the positives and the negatives.

        To check, we go from the largest even number down to smallest, because
        the largest even number can only be divided by two (for negatives, we
        go with the largest negative number). For each big even number, we check
        whether big_even // 2 has more than 0 count in even_counter. If it does
        not, we return False. If it does, we decrement even_count for both
        big_even and big_even // 2, and continue until we exhaust all even
        numbers.

        O(Nlog(N)), 676 ms, 63% ranking.
        """
        odds = []
        even_count = Counter()
        for a in arr:
            if a % 2:
                odds.append(a)
            else:
                even_count[a] += 1
        for o in odds:
            pot = o * 2
            if not even_count[pot]:
                return False
            even_count[pot] -= 1
            if not even_count[pot]:
                del even_count[pot]
        pos_evens = sorted([k for k in even_count.keys() if k >= 0], reverse=True)
        neg_evens = sorted([k for k in even_count.keys() if k < 0])

        def check_evens(sorted_evens: List[int]) -> bool:
            i = 0
            while i < len(sorted_evens):
                big_even = sorted_evens[i]
                if even_count[big_even] > 0:
                    pot = big_even // 2
                    if not even_count[pot]:
                        return False
                    even_count[pot] -= 1
                    even_count[big_even] -= 1
                if not even_count[big_even]:
                    i += 1
            return True

        return check_evens(pos_evens) and check_evens(neg_evens)


class Solution2:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """Solution1 is unnecessarily complicated. We can easily combine all
        three situations (odd, positive even, and negative even) into one
        algorithm.

        Ref: https://leetcode.com/problems/array-of-doubled-pairs/solution/
        """
        count = Counter(arr)
        for a in sorted(arr, key=abs):  # good trick key=abs
            if count[a]:
                if not count[2 * a]:
                    return False
                count[a] -= 1
                count[2 * a] -= 1
        return True


sol = Solution2()
tests = [
    ([3, 1, 3, 6], False),
    ([2, 1, 2, 6], False),
    ([4, -2, 2, -4], True),
    ([1, 2, 4, 16, 8, 4], False),
    ([0, 0], True),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.canReorderDoubled(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
