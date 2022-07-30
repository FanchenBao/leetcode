# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        """Use counter. Very straightforward.

        O(N), 610 ms, faster than 53.30%
        """
        counter = Counter()
        for msg, sen in zip(messages, senders):
            counter[sen] += len(msg.split())
        max_count = max(counter.values())
        return max(k for k, v in counter.items() if v == max_count)
        

sol = Solution()
tests = [
    (["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], ["Alice","userTwo","userThree","Alice"], 'Alice'),
    (["How is leetcode for everyone","Leetcode is useful for practice"], ["Bob","Charlie"], 'Charlie'),
]

for i, (messages, senders, ans) in enumerate(tests):
    res = sol.largestWordCount(messages, senders)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
