# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution1:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """I checked the hint.

        The hint is a very very important piece of information. It suggests
        that the person with the shortest hight among the un-positioned people
        can have his position identified deterministically. For instance, if
        the shortest person is [4, 4]. That means its position in the queue
        must be at queue[4+1], because nobody is shorter than him, which means
        all the positions in front of him must be taller or equal to him.
        Hence, its position must be queue[4+1].

        Then, the second shortest person comes out. For him, he does not have
        to worry about the shortest person already positioned, because to him
        the shortest person is invisible in terms of counting. Therefore, the
        second shortest person's positioning follows the same rule as the
        shortest person, i.e. counting the number of empty spots in front of
        it. For instance, if the second shortest is [5, 5]. Then he must be
        positioned at the (5 + 1)th empty spot. Since [4, 4] already occupies
        queue[4+1], [5, 5] will be located at queue[6], because there are five
        empty spots from queue[0] to queue[5].

        We use a dict to record all the positions for each height. And for each
        height, we go through the entire length of the result and count the
        number of empty spots. Once the count matches the position of the
        person, we put the person there.

        O(N^2), 428 ms, 20% ranking.
        """
        pos = defaultdict(set)
        for h, k in people:
            pos[h].add(k)
        res = [[] for _ in range(len(people))]
        for h in sorted(pos):
            count = -1
            for i in range(len(res)):
                if not res[i]:
                    count += 1
                    if count in pos[h]:
                        res[i] = [h, count]
                        pos[h].remove(count)
                        if not pos[h]:
                            break
        return res


class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """This is from https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC%2B%2BJava-Solution

        I think this idea is better than Solution1. It thinks about the tallest
        instead of shortest person. The benefit of thinking about the tallest
        people is that they do not care about how other people are queued. They
        only follow their ks. When the second tallest people come in, they only
        respect the ones already in the queue, and put themselves in between
        them such that there are exactly k number of taller guys to the left.
        This is equivalent to using the insert() method.

        On average, this should run in O(N^2logN), 130 ms, 37% ranking.
        """
        pos = defaultdict(list)
        for h, k in people:
            pos[h].append(k)
        res = []
        for h in sorted(pos, reverse=True):
            for k in sorted(pos[h]):
                res.insert(k, [h, k])
        return res


class BIT:
    def __init__(self, N: int):
        """Initialize a binary indexed tree.

        :param N: The size of the range, including min and max.
        """
        # use 1-based BIT, thus array size must be one larger than the range.
        self.bit = [0] * (N + 1)

    def update(self, pos: int, delta: int) -> None:
        """Update the value at `pos` by adding `delta`.

        Also update all the other ranges that contain `pos`.

        :param pos: The position inside a range whose value needs to be
            updated. Note that this position is one less than the index
            of the self.bit array.
        :param delta: The additional value that needs to be added to
            the value at the given position, and all the other ranges
            including the given position.
        """
        # KEY POINT: BIT index is 1-based, thus its index is one larger
        # than the given position.
        i = pos + 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += (i & -i)

    def query(self, max_r: int) -> int:
        """Query the sum of values in the range 0 to `max_r`.

        The meaning of "values" us defined by the `delta` parameter
        in self.update(). It is not necessarily prefix sum.

        :param max_r: The end of the range which we want to query.
        :return: Sum of values in the range 0 to `max_r`.
        """
        # KEY POINT: Bit index is 1-based, thus its index is one larger
        # than the given max range.
        i, res = max_r + 1, 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res


class Solution3:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """This post suggests using BIT to find the position to each k in
        O(logN) time with regards to solution1.

        https://leetcode.com/problems/queue-reconstruction-by-height/discuss/427157/Three-different-C%2B%2B-solutions.-from-O(n2)-to-O(nlogn).-faster-than-99.

        The key insight is that bit.query(i) equals to the number of empty
        spots from the beginning of the queue up to the ith position. Since we
        are selecting the shortest people first, for each [h, k] considered,
        k is equal to the number of spots not taken in the queue. We can use
        BIT to keep track of the number of empty spots in O(logN) time. Then
        we can use binary search to find the correct position whose bit.query(i)
        is equal to k. Binary search is possible because bit.query(i + 1) is
        always not smaller than bit.query(i)

        O(NlogN)
        """
        N = len(people)
        res = [[] for _ in range(N)]
        bit = BIT(N)
        # initialize BIT.
        for i in range(N):
            bit.update(i, 1)
        pos = defaultdict(list)
        for h, k in people:
            pos[h].append(k)
        for h in sorted(pos):
            temp = []
            for k in pos[h]:
                lo, hi = 0, N - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if bit.query(mid) > k:
                        hi = mid
                    else:
                        lo = mid + 1
                res[lo] = [h, k]
                temp.append(lo)
            for lo in temp:
                bit.update(lo, -1)
        return res


sol = Solution3()
tests = [
    ([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]], [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]),
    ([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]], [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]),
]

for i, (people, ans) in enumerate(tests):
    res = sol.reconstructQueue(people)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
