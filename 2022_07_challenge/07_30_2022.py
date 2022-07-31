# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """LeetCode 916

        O(N + M), where N and M are length of words1 and words2.
        1558 ms, faster than 32.67%
        """
        uni_counter = Counter()
        for word in words2:
            for le, c in Counter(word).items():
                uni_counter[le] = max(uni_counter[le], c)
        res = []
        for word in words1:
            counter = Counter(word)
            if len(uni_counter) <= len(counter):
                for le, c in uni_counter.items():
                    if counter[le] < c:
                        break
                else:
                    res.append(word)
        return res


class Solution2:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """Repeat what I did in March last year. There are Counter magic in
        Python: https://www.geeksforgeeks.org/operations-on-python-counter/
        """
        uni_counter = Counter()
        for word in words2:
            uni_counter |= Counter(word)
        return [word for word in words1 if not uni_counter - Counter(word)]
        

sol = Solution2()
tests = [
    (["amazon","apple","facebook","google","leetcode"], ["e","o"], ["facebook","google","leetcode"]),
    (["amazon","apple","facebook","google","leetcode"], ["l","e"], ["apple","google","leetcode"])
]

for i, (words1, words2, ans) in enumerate(tests):
    res = sol.wordSubsets(words1, words2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
