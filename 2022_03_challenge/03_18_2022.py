# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
from collections import defaultdict
from random import randint


class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        """Memory limit exceed.
        """
        N = len(s)
        hashmap = {le: i for i, le in enumerate(s)}
        
        @lru_cache(maxsize=None)
        def dp(state: int, idx: int) -> str:
            if idx == N:
                return ''
            shift = ord(s[idx]) - 97
            if (state >> shift) & 1:
                return dp(state, idx + 1)
            if hashmap[s[idx]] == idx:  # we must take the current letter
                return s[idx] + dp(state | (1 << shift), idx + 1)
            return min(
                s[idx] + dp(state | (1 << shift), idx + 1),
                dp(state, idx + 1),
            )
        return dp(0, 0)


class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        """Monotonic stack. I see the hint.

        This one is so hard. The monotomic stack never occurred to me, but it
        makes sense. We can only pop the bigger letters on the stack if there
        are more copies of it later in the string. We use a hashmap to record
        the latest occurrence each letter and use a seen set to keep track of
        what letters have been used.

        The key trick is that once the last copy of a letter is encountered,
        the record on the hashmap must be set to a very small value, such that
        the previous copy will not accidentally be popped.

        O(N), 73 ms, 18% ranking.
        """
        stack = []
        hashmap = {le: i for i, le in enumerate(s)}
        seen = set()
        for i, le in enumerate(s):
            if hashmap[le] == i:  # last encounter of the letter
                hashmap[le] = -1
            if le not in seen:
                while stack and stack[-1][0] >= le and hashmap[stack[-1][0]] > stack[-1][1]:
                    seen.remove(stack.pop()[0])
                stack.append((le, i))
                seen.add(le)
        return ''.join(ele[0] for ele in stack)


class Solution3:
    def removeDuplicateLetters(self, s: str) -> str:
        """Better monotonic stack.

        We can directly use stack as seen, because the size of stack won't
        exceed 26.

        Another crucial observation is that we can check whether a letter to
        be popped has more copies by comparing the current index with hashmap.
        Previously, we compare the index of the letter to be popped with the
        index of the last occurrence. This is wrong and we have to create an
        extra step for last encounter of the letter to correct it. In this
        method, we simply compare the last occurrence index with the current
        index. If the last occurrence index is larger than the current index,
        then for sure there are more copies.
        """
        stack = []
        hashmap = {le: i for i, le in enumerate(s)}
        for i, le in enumerate(s):
            if le not in stack:
                while stack and stack[-1] > le and hashmap[stack[-1]] > i:
                    stack.pop()
                stack.append(le)
        return ''.join(stack)


class Solution4:
    def removeDuplicateLetters(self, s: str) -> str:
        """Greedy.

        We always want to pick the smallest letter available so far. Whether
        such smallest letter can be picked is contingent on whether the total
        letters available to pick after choosing the smallest letter match that
        of the input s. If they match, that means picking the smallest letter
        does not affect the ability to pick any of the other letters. We shall
        pick it. Otherwise, we cannot pick the smallest letter because picking
        it means some other letter cannot be picked. In this case, we simply
        move on to the next smallest letter.
        """
        set_s = set(s)
        for le in sorted(set_s):
            next_s = s[s.index(le):]
            if set(next_s) == set_s:
                return le + self.removeDuplicateLetters(next_s.replace(le, ''))
        return ''


sol1 = Solution1()
sol = Solution4()
# tests = [
#     ("bcabc"),
#     ("cbacdcbc"),
#     ("acdcb"),
#     ("hkmjfhbjefkwfj"),
#     ('gjvfnjbfkmreugijrnkeijrgnk'),
# ]
num_test = 100
str_len = 10
tests = [
    ''.join(chr(97 + randint(0, 25)) for _ in range(str_len)) for _ in range(num_test)
]


for i, s in enumerate(tests):
    res = sol.removeDuplicateLetters(s)
    ans = sol1.removeDuplicateLetters(s)
    if res != ans:
        print(f'Test {i}: {s}; Fail. Ans: {ans}, Res: {res}')
