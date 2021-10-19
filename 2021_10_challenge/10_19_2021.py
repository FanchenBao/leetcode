# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """LeetCode 496 

        Since each element in nums2 is unique, we can find the next greater
        number for each element in nums2 and record it in a dictionary. To find
        the next greater number, we use a stack. If the new value is smaller
        than top of stack (or stack is empty), we push the new value in.
        Otherwise we keep popping the stack until we reach a value bigger or
        stack becomes empty. Each time a value is popped, the popped value's
        next greater element is the current numebr.

        I forgot to keep popping, and that's why my first submission was
        incorrect.

        O(M + N), where M is the length of nums1 and N the length of nums2. The
        process of obtaining the next greater values runs at most in O(2N).

        42 ms, 92% ranking.

        UPDATE: we don't have to clear out stack, because we simply use dict.get
        method to force -1 on any value that is not in the dict.
        """
        next_greater = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                next_greater[stack.pop()] = n
            stack.append(n)
        return [next_greater.get(n, -1) for n in nums1]


sol = Solution()
tests = [
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 4], [1, 2, 3, 4], [3, -1]),
    ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7]),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.nextGreaterElement(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
