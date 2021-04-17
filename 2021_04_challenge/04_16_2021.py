# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def removeDuplicates(self, s: str, k: int) -> str:
        """LeetCode 1209

        The idea is to do pair-wise check on s, count how many letters are
        in a adjacent duplicate. Once we get the count, we know only count - k
        of that letter can pass on to the next level string. At each level, we
        create a new string by accepting count - k duplicate letters from the
        previous string. We end the loop when the new string is the same as the
        old string.

        The inner loop is O(N), the outer loop depends on how many times we need
        to run the deletion. The worst case is each time we delete only two.
        Then the outer loop runs in O(N / 2). This means in total, the worst
        case is O(N^2). 108 ms, 17% ranking.
        """
        while True:
            ns = ''
            i, count = 0, 1
            while i < len(s) - 1:
                if s[i] == s[i + 1]:
                    count += 1
                else:
                    ad = (count - k) * s[i] if count >= k else count * s[i]
                    ns += ad
                    count = 1
                i += 1
            ad = (count - k) * s[i] if count >= k else count * s[i]
            ns += ad
            if ns == s:
                break
            s = ns
        return s


class Solution2:
    def removeDuplicates(self, s: str, k: int) -> str:
        """This comes from the hint, using a stack."""
        old_stack = [[le, 1] for le in s]
        while True:
            new_stack = []
            has_pop = False
            for le, c in old_stack:
                if not new_stack or new_stack[-1][0] != le:
                    new_stack.append([le, c])
                else:
                    new_stack[-1][1] += c
                    if new_stack[-1][1] >= k:
                        new_stack[-1][1] -= k
                        if not new_stack[-1][1]:
                            has_pop = True
                            new_stack.pop()
            if not has_pop:
                break
            old_stack = new_stack
        return ''.join(le * c for le, c in new_stack)


class Solution3:
    def removeDuplicates(self, s: str, k: int) -> str:
        """This is the stack solution from lee215. Much much better than the one
        I conjured above. The key idea is that we only need to iterate s once.
        e.g. given 'aabbba' and k = 3. After we remove 'bbb', we don't have to
        wait until the next iteration to remove 'aaa'. We can remove 'aaa' right
        after 'bbb' is removed, because the last 'a' falls on top of the stack,
        sees that we already have two 'a's, and immediately merges with them and
        gets deleted. Therefore, the outer loop is unnecessary.
        """
        stack = [['*', 0]]
        for le in s:
            if stack and stack[-1][0] == le:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([le, 1])
        return ''.join(le * c for le, c in stack)


class Solution4:
    def removeDuplicates(self, s: str, k: int) -> str:
        """The two-pointer solution also from lee215. Very brilliant.
        The key is to keep two lists, one storing the final outcome, and the
        other stores the number of adjacent duplicates at each position. Note
        that the positions in the final outcome list and the count list are
        always the same, but they are different from the position in s.

        As we iterate through s, we use pairwise comparison to determine whether
        we have encountered sufficient number of adjacent duplicates. Once that
        is achieved, we move the index of outcome list k steps to the left. This
        is equivalent to deleting those duplicates.

        We make sure that the index of the outcome list always points one step
        ahead of the current end of the outcome string.
        """
        N = len(s)
        res_lst = [''] * N
        count = [1] * N
        i = 0
        for j in range(N):
            res_lst[i] = s[j]
            count[i] = count[i - 1] + 1 if i > 0 and res_lst[i] == res_lst[i - 1] else 1
            if count[i] == k:
                i -= k
            i += 1
        return ''.join(res_lst[:i])


sol = Solution4()
tests = [
    ('abcd', 2, 'abcd'),
    ('deeedbbcccbdaa', 3, 'aa'),
    ('pbbcggttciiippooaais', 2, 'ps'),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.removeDuplicates(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
