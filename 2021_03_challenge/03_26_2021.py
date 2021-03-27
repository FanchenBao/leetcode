# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """LeetCode 916

        The key observation is that we do not have to examine each b in B,
        because there might be overlaps among the bs. If two bs have common
        letters, that letter only needs to be checked once. Therefore, we first
        condence B into one item for checking by mergeing bs via their counter
        verision. We keep the maximum counts of each letter in the final merged
        counter. Then we loop through each word in A, get its counter, and
        compared the a counter with the merged B counter. The rule is that the
        letter count in a counter must be bigger or equal to the same letter
        count in the merged B counter.

        O(Nn + M(m + 26)), where M, N is the length of A and B, and m, n are the
        max number of letters in the words of A and B, and 26 is the maximum
        number of letters in the merged B counter.

        904 ms, 52% ranking
        """
        cb_all = Counter()
        for b in B:
            cb = Counter(b)
            for k, c in cb.items():
                cb_all[k] = max(cb_all[k], c)
        res = []
        for a in A:
            ca = Counter(a)
            for k, c in cb_all.items():
                if ca[k] < c:
                    break
            else:
                res.append(a)
        return res


class Solution2:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """Found this counter magic solution from the discussion. Very cool!
        The two pieces of magic is one: counter union, and two counter
        subtraction. Read here for their usage
        https://www.geeksforgeeks.org/operations-on-python-counter/
        """
        cb_all = Counter()
        for b in B:
            cb_all |= Counter(b)
        return [a for a in A if not cb_all - Counter(a)]


sol = Solution2()
tests = [
    (['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['e', 'o'], ['facebook', 'google', 'leetcode']),
    (['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['l', 'e'], ['apple', 'google', 'leetcode']),
    (['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['e', 'oo'], ['facebook', 'google']),
    (['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['lo', 'eo'], ['google', 'leetcode']),
    (['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['ec', 'oc', 'ceo'], ['facebook', 'leetcode']),
]

for i, (A, B, ans) in enumerate(tests):
    res = sol.wordSubsets(A, B)
    if sorted(res) == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
