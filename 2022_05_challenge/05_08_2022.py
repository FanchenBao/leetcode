# from pudb import set_trace; set_trace()
from typing import List



class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        """LeetCode 341

        Use recursion to flatten the nested list in a lazy and easy way.

        """
        self.lst = []
        self._flatten(nestedList)
        self.idx = 0
        self.N = len(self.lst)
    
    def _flatten(self, nested_list: List[NestedInteger]) -> None:
        for ni in nested_list:
            if ni.isInteger():
                self.lst.append(ni.getInteger())
            else:
                self._flatten(ni.getList())

    def next(self) -> int:
        self.idx += 1
        return self.lst[self.idx - 1]
    
    def hasNext(self) -> bool:
        return self.idx < self.N


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
