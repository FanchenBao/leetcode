# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import heapq


class Solution1:
    def minJumps(self, arr: List[int]) -> int:
        """LeetCode 1345

        I am pretty proud of myself for solving this hard problem. The first
        time I did it was December 2020, and it took me more than three and
        half hours, and I am pretty sure I had to resort to the solution.

        This time, I have an ugly solution but it works. The idea is BFS. We
        start from the desitnation (i.e. the last index) and push all possible
        previous step to a queue. The shortest path appears once we reach index
        0. However, there is a trick to handle a specifically large test case.
        That is we always push into the queue from smaller index to large index
        and each time an index popped out, we always check whether itself is
        0 or whether itself minus one is zero. This is because these are the
        only two possiblilies that the zero index can be reached. Ideally, we
        shall only have to test the index itself, but to avoid waiting for the
        next round to check the current index minus one, we can check it
        immediately and if it is zero, then we save an entire round. This is
        the difference between passing OJ and TLE.

        Yet still, this is a hack.

        O(N), 846 ms, 29% ranking. (Note that there are four more test cases
        this time than last time)

        UDPATE: this solution is technically not correct, because it depends
        on the order of adding neighbors to the queue. In particular, if we add
        i - 1 before i + 1, then this solution fails the first test case.

        To resolve this issue, we need to always pop out the smallest value in
        the queue, which requires us to use a heapq. However, it also increases
        the time complexity. See a better implementation in Solution2.
        """
        pos = defaultdict(list)
        for i, a in enumerate(arr):
            pos[a].append(i)
        N = len(arr)
        visited = set([N - 1])
        queue = [N - 1]
        res = 0
        while queue:
            temp = []
            for i in queue:
                if i == 0:
                    return res
                if i - 1 == 0:  # A hack to avoid waiting for the next round
                    return res + 1
                for nei in pos[arr[i]] + [i + 1, i - 1]:
                    if nei not in visited and 0 <= nei < N:
                        temp.append(nei)
                        visited.add(nei)
            queue = temp
            res += 1


class Solution2:
    def minJumps(self, arr: List[int]) -> int:
        """This is essentially the same as Solution1, and is inspired by the
        solution I submitted in Dec. 2020. To avoid the impact of order of
        appending to the queue, we should remove the check for i - 1 == 0. And
        to aliviate the wasted time, we use a trick where the key and value
        of the pos dict is erased once the key has been visited. This is
        because the first time the key is visited, all of its neighbors in the
        pos dict will have ended up in the queue already. Therefore, when these
        neighbors are visited, we don't have to push any of its neighbor to
        the queue again. This guarantees that each unique value's value in
        the pos dict is only visited once.

        O(N), 1083 ms, 16% ranking.
        """
        pos = defaultdict(list)
        for i, a in enumerate(arr):
            pos[a].append(i)
        N = len(arr)
        visited = set([N - 1])
        queue = [N - 1]
        res = 0
        while queue:
            temp = []
            for i in queue:
                if i == 0:
                    return res
                for nei in pos[arr[i]] + [i - 1, i + 1]:
                    if nei not in visited and 0 <= nei < N:
                        temp.append(nei)
                        visited.add(nei)
                pos[arr[i]].clear()  # trick to avoid using pos[arr[i]] again
            queue = temp
            res += 1


class Solution3:
    def minJumps(self, arr: List[int]) -> int:
        """Same as Solution1, but with a heapq to guanrantee correctness
        
        O(NlogN), 802 ms, 32% ranking.
        """
        pos = defaultdict(list)
        for i, a in enumerate(arr):
            pos[a].append(i)
        N = len(arr)
        visited = set([N - 1])
        queue = [N - 1]
        res = 0
        while queue:
            temp = []
            while queue:
                i = heapq.heappop(queue)
                if i == 0:
                    return res
                if i - 1 == 0:  # A hack to avoid waiting for the next round
                    return res + 1
                for nei in pos[arr[i]] + [i + 1, i - 1]:
                    if nei not in visited and 0 <= nei < N:
                        heapq.heappush(temp, nei)
                        visited.add(nei)
            queue = temp
            res += 1
        

sol = Solution3()
tests = [
    ([100,-23,-23,404,100,23,23,23,3,404], 3),
    ([7], 0),
    ([7,6,9,6,9,6,9,7], 1),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minJumps(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
