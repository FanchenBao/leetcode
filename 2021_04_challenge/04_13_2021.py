# from pudb import set_trace; set_trace()
from typing import List


class NestedInteger:
    pass


class NestedIterator1:
    """LeetCode 341

    The key to solve this problem is to understand what NestedInteger is. It
    can either be a single integer, or a list of NestedInteger. Thus, we can
    write a recursion to solve the problem. If NestedInteger is a integer, we
    extract it and end the recursion. If not, we take the list, and recurse on
    it.

    O(N), 64 ms, 79% ranking.
    """

    def __init__(self, nestedList: [NestedInteger]):
        self.lst = []
        self._flatten(nestedList)
        self.idx = 0
        self.N = len(self.lst)

    def _flatten(self, nestedList: [NestedInteger]):
        for ni in nestedList:
            if ni.isInteger():
                self.lst.append(ni.getInteger())
            else:
                self._flatten(ni.getList())

    def next(self) -> int:
        self.idx += 1
        return self.lst[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx < self.N


class NestedIterator2:
    """None flatten solution.

    Basically inside stack, it's either integer or reference to a nestedList.
    The size of self.stack is always smaller or equal to the fully flattened
    list.
    """

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self._prepare(nestedList)

    def _prepare(self, nestedList: [NestedInteger]):
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        self.hasNext()
        return self.stack.pop()

    def hasNext(self) -> bool:
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            self._prepare(self.stack.pop().getList())
        return False


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
