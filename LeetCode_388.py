# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """The insight is that each time a new line is encountered, we will have
        to deal with a new item. The number of tabs determine to which previous
        item the current item belongs. It so happens that if we use a stack to
        keep track of the previous items, then if the length of the stack is
        equal to the number of tabs, then the current item belongs to the last
        item in the stack, or in other words, we can append the current item to
        the stack.

        If, however, the current has fewer tabs than the length of the stack,
        the the current item must belong to some item (or no item) before the
        end of the stack. Thus, we pop the stack until the size of the stack is
        equal to the number of tabs. Then we append the current item.

        To obtain the number of chars in an absolute path, we simply join the
        stack with separator set to the slash and then count its length.

        O(N), N = len(input). 28 ms, 82% ranking.
        """
        stack, res = [], 0
        for it in input.split('\n'):
            num_tabs = it.count('\t')
            while len(stack) > num_tabs:
                stack.pop()
            stack.append(it[num_tabs:])
            if '.' in it:  # this is a file
                res = max(res, len('/'.join(stack)))
        return res


sol = Solution()
tests = [
    ("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20),
    ('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext', 32),
    ('a', 0),
    ("file1.txt\nfile2.txt\nlongfile.txt", 12),
]

for i, (input, ans) in enumerate(tests):
    res = sol.lengthLongestPath(input)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
