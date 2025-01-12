# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        """
        Very similar to the implementation of Dijkstra

        647 ms, 30.49%
        """
        self.map = {tid: [p, uid] for uid, tid, p in tasks}
        self.max_heap: List[List[int]] = []
        for _, tid, p in tasks:
            heapq.heappush(self.max_heap, [-p, -tid])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.map[taskId] = [priority, userId]
        heapq.heappush(self.max_heap, [-priority, -taskId])

    def edit(self, taskId: int, newPriority: int) -> None:
        if self.map[taskId][0] != newPriority:
            self.map[taskId][0] = newPriority
            heapq.heappush(self.max_heap, [-newPriority, -taskId])

    def rmv(self, taskId: int) -> None:
        del self.map[taskId]

    def execTop(self) -> int:
        while self.max_heap:
            neg_p, neg_tid = self.max_heap[0]
            if -neg_tid not in self.map or (
                -neg_tid in self.map and self.map[-neg_tid][0] != -neg_p
            ):
                heapq.heappop(self.max_heap)
            else:
                break
        if self.max_heap:
            _, neg_tid = heapq.heappop(self.max_heap)
            return self.map.pop(-neg_tid)[1]
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
