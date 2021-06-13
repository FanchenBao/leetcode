# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution0:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """Naive O(N^2) solution. TLE
        """
        res = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                concat = words[i] + words[j]
                if concat == concat[::-1]:
                    res.append([i, j])
                concat = words[j] + words[i]
                if concat == concat[::-1]:
                    res.append([j, i])
        return res


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """LeetCode 336

        Instead of the naive O(N^2), we can analyze each word, and see what
        other word is needed in order to form a palindrome with the current
        word. The check needs to be on both sides of the current word. Let's say
        we are checking to add a word to the right of the current word. We say
        0 letter from the right side of the current word is shared in the new
        palindrome. Then the other word must be word[::-1]. We then say 1 letter
        from the right side of the current word is shared, then the other word
        must be word[:n - 1][::-1]. We can then say 2 letters from the right
        side of the current word is shared, then these 2 letters must themselves
        also be palindrome, then the other word must be word[:n - 2][::-1], etc.

        We record any pairs that satisfy the requirement above for both on the
        right and left side. To avoid duplicates, we record the result in a set
        before finally returning the list version.

        One more thing, we must build a word to index mapping to know which
        index each palindrome pair corresponds to.

        O(NM^2), where M is the average length of a word.

        596 ms, 59% ranking

        UPDATE: from this solution
        https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation

        I finally understand the trick of not including repeats. The trick is
        that when a full word's reverse exists in the words list, we only allow
        it to be placed to either left or right side of the original word. This
        means if words[0] is under consideration, and words[1] == words[0][::-1]
        then we only allow [0, 1], but not [1, 0]. We will do [1, 0] when
        words[1] is being considered. This leads to the conditional check
        `j != 0`. And we also do not need a set to prevent duplication.

        Without the need to use a set, the runtime improves to 544 ms, 73%
        ranking.
        """
        idx_map = {w: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            n = len(w)
            for j in range(n + 1):
                if w[n - j:] == w[n - j:][::-1]:  # check pal on the right side
                    pal = w[:n - j][::-1]
                    if pal != w and pal in idx_map:
                        res.append([i, idx_map[pal]])
                if j != 0 and w[:j] == w[:j][::-1]:  # check pal on the left side
                    pal = w[j:][::-1]
                    if pal != w and pal in idx_map:
                        res.append([idx_map[pal], i])
        return res


sol = Solution()
tests = [
    (['abcd', 'dcba', 'lls', 's', 'sssll'], [[0, 1], [1, 0], [3, 2], [2, 4]]),
    (['bat', 'tab', 'cat'], [[0, 1], [1, 0]]),
    (['a', ''], [[0, 1], [1, 0]]),
    (['aaa', 'aa', 'a'], [[0, 2], [1, 0], [0, 1], [2, 0], [1, 2], [2, 1]]),
    (['aaa', 'aa', 'a', ''], [[0, 2], [0, 3], [3, 0], [2, 0], [1, 2], [1, 3], [0, 1], [1, 0], [3, 1], [2, 1], [3, 2], [2, 3]]),
    (['g', 'lrlg', 'uzoxy', 'ogdm', 'hhlx'], [[0, 1]]),
]


for i, (words, ans) in enumerate(tests):
    res = sol.palindromePairs(words)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')

# sol0 = Solution0()
# sol = Solution()
# max_word_length = 10
# max_N = 5
# num_test = 1000

# tests = [list(set(''.join([chr(97 + randint(0, 25)) for _ in range(randint(1, max_word_length))]) for _ in range(randint(0, max_N)))) for _ in range(num_test)]

# for i, words in enumerate(tests):
#     ans = sorted(sol0.palindromePairs(words))
#     res = sorted(sol.palindromePairs(words))
#     if ans == res:
#         # print(f'Test {i}: PASS')
#         pass
#     else:
#         print(f'Test {i}; Fail. {ans=}, {res=}, {words=}')
