# from pudb import set_trace; set_trace()
from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        """It took a few tries to fully comprehend the API of NestedIntegers.
        The result is that each time when we push an integer into the stack, we
        must push a NestedInteger.

        Another tricky part is parsing the negative values, but I just realized
        that we can actually ask Python to parse it for us.

        O(N), 72 ms, 66% ranking.
        """
        stack = []
        N, i = len(s), 0
        while i < N:
            if s[i] == '[':
                stack.append(s[i])
            elif s[i] == ']':
                vals = []
                while stack and stack[-1] != '[':
                    vals.append(stack.pop())
                stack.pop()  # pop left bracket
                ni = NestedInteger()
                for val in vals[::-1]:
                    ni.add(val)
                stack.append(ni)
            elif s[i] in '-0123456789':
                j = i
                while j < N and s[j] != ',' and s[j] != ']':
                    j += 1
                stack.append(NestedInteger(int(s[i:j])))
                i = j - 1
            i += 1
        return stack[0]
        

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
