# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter
from itertools import chain


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """I am not sure, but it seems like LeetCode was preparing us for this
        problem by asking us to solve a simple word search and implement a trie
        in the previous two days. I solve this problem by combinig these two
        approaches.

        Looking at the constraints of this problem, it has a word list as long
        as 3x10^4. So it is impossible to check every word by itself. The only
        logical solution is to use a trie, such that we can hit multple words
        in one run. This will be extremely helpful in test cases such as ['a',
        'aa', 'aaa', 'aaaa']. Thus, we first build the trie. As we are building
        the trie, we can also do a pruning by checking whether a word is even
        possible to be found in board. We use the same pruning method as word
        search. After finishing all this, we have a trie with all words in it
        having a potential to be matched in the board.

        Then we just match the word by finding the starting point, and then
        backtracking. One aspect that got me was that we need to use a set for
        result to avoid duplicates, because it is possible that a word can be
        found in multiple ways.

        O(L*M*N*3^K), L is the length of word list; M, N are the number of rows
        and cols of board; and K is the average length of each word.

        3064 ms, 66% ranking.

        UPDATE: Mr. Pochmann's solution actively pops the end of the word
        sentinel, such that each word will only be counted once. Very smart
        move.
        """
        _trie = lambda: defaultdict(_trie)
        board_count = Counter(chain(*board))
        root = _trie()

        for word in words:
            for w, c in Counter(word).items():
                if board_count[w] < c:
                    break
            else:
                node = root
                for w in word:
                    node = node[w]
                node['word'] = word  # signal the end of a word

        m, n = len(board), len(board[0])
        res = []

        def search(i: int, j: int, node) -> None:
            word = node.pop('word', '')
            if word:
                res.append(word)
            for k, v in node.items():
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == k:
                        board[ni][nj] = '.'
                        search(ni, nj, v)
                        board[ni][nj] = k

        for k, v in root.items():
            for i in range(m):
                for j in range(n):
                    if board[i][j] == k:
                        board[i][j] = '.'
                        search(i, j, v)
                        board[i][j] = k
        return res


sol = Solution()
tests = [
    ([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain'], ['eat', 'oath']),
    ([['o', 'a', 'b', 'n'], ['o', 't', 'a', 'e'], ['a', 'h', 'k', 'r'], ['a', 'f', 'l', 'v']], ['oa', 'oaa'], ['oa', 'oaa']),
]

for i, (board, words, ans) in enumerate(tests):
    res = sol.findWords(board, words)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
