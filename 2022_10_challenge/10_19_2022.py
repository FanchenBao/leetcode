# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
import heapq


class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """LeetCode 692

        O(NlogN), 128 ms, faster than 28.68%

        However, the requirement is to achieve O(NlogK) time. So this solution
        doesn't count.
        """
        return [w for w, _ in sorted(Counter(words).items(), key=lambda tup: (-tup[1], tup[0]))[:k]]


class Node:
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count

    def __lt__(self, other) -> bool:
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count


class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """What a shame. Whenever the question is about the top (or bottom) k
        elements, always use a priority queue. All we need to do is to keep
        the size of the queue at k. If new ones need to be added, we always
        pop the top to keep the queue size at k.

        Thus, we do N insertion, and each insert requires log(K) operation to
        reorganize.

        Since we want to keep the top k most frequent, the queue must be a
        min heap. This way, we always pop the smallest in the queue when new
        element is added.

        O(NlogK), 146 ms, faster than 7.88%
        """
        counter = Counter(words)
        heap = []
        for word, count in counter.items():
            heapq.heappush(heap, Node(word, count))
            if len(heap) > k:
                heapq.heappop(heap)
        return [heapq.heappop(heap).word for _ in range(k)][::-1]


sol = Solution2()
tests = [
    (["i","love","leetcode","i","love","coding"], 2, ["i","love"]),
    (["the","day","is","sunny","the","the","the","sunny","is","is"], 4, ["the","is","sunny","day"]),
]

for i, (words, k, ans) in enumerate(tests):
    res = sol.topKFrequent(words, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
