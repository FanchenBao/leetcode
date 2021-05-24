# from pudb import set_trace; set_trace()
from typing import List, Dict
from collections import defaultdict
import math


class Solution1:

    def concat_save(self, w1: str, w2: str) -> int:
        m, n = len(w1), len(w2)
        for i in range(min(m, n) - 1, 0, -1):
            if w1[-i:] == w2[:i]:
                return i
        return 0

    def gen_graph(self, words: List[str]) -> Dict[int, Dict[int, int]]:
        graph = defaultdict(dict)
        N = len(words)
        for i in range(N):
            for j in range(i + 1, N):
                s1 = self.concat_save(words[i], words[j])
                s2 = self.concat_save(words[j], words[i])
                if s1 == 0 and s2 == 0:
                    continue
                if s1 >= s2:
                    graph[i][j] = s1
                if s1 <= s2:
                    graph[j][i] = s2
        return graph

    def shortestSuperstring(self, words: List[str]) -> str:
        """This solution FAILED

        This was my absolute best effort, but unfortunately still fell short.
        I had high hopes for this graph solution, but apparently it is not
        sufficient or I just haven't used the right approach on the graph.
        """
        graph = self.gen_graph(words)
        nodes = set(range(len(words)))  # all nodes

        def dfs(node: int, visited: List, cur_save: int, res) -> None:
            visited.append(node)
            if cur_save > res[0]:
                res[1] = visited[:]
                res[0] = cur_save
            if node in graph:
                for next_node, save in graph[node].items():
                    if next_node not in visited and next_node in nodes:
                        dfs(next_node, visited, cur_save + save, res)
            visited.pop()

        res_str = ''

        # each round of DFS, pick out the max saving path, remove it and repeat
        # again
        while graph:
            res = [-1, []]
            for node in graph.keys():
                dfs(node, [], 0, res)
            path = res[1]
            if path:
                temp = words[path[0]]
                for i in range(1, len(path)):
                    temp += words[path[i]][graph[path[i - 1]][path[i]]:]
                res_str += temp
            for p in path:
                if p in graph:
                    del graph[p]
                nodes.remove(p)
        return res_str + ''.join(words[i] for i in nodes)


class Solution2:
    def shortestSuperstring(self, words: List[str]) -> str:
        """Massive massive effort to code this up after reading the official
        solution and other people's posts for about an hour. A very complicated
        problem indeed. My initial solution was onto something, but it fell
        short because the way I was thinking about the problem is not general
        enough. Instead of finding the maximum overlap, the graph should be
        the minimum number of letters to append. This way, we can include all
        words in the graph and avoid the problem of isolated words.

        The most important aspect is the DP logic. The way of using bitmap to
        represent a set of words that have been used is absolutely brilliant.
        It allows for very fast way to check whether a word has been used, and
        makes it possible to use a set of words as a state usable as a key in
        a DP table.

        The logic can be summarized as such: go through all possible sets of
        words (2^N). For each set, we pick a word that is currently available in
        the set. Make that word the last one that has been added. Let's call
        that word i (by index). Then, find the previous word set before i is
        added. In the previous word set, go through all the words currently in
        the previous word set, and claim that that word, let's call it j, is the
        one added immediately before i. We can compute the length of superstring
        when j and i are added in succession as dp[pre_state][j] + graph[j][i].
        If this value is smaller than dp[state][i], that means we have found a
        better way to reach the current state that ends with adding word i. We
        also use a path[state][i] = j to record the immediate word before word
        i, which will help us reconstruct the path.

        We run this DP algorithm for all possible word set states, and keep
        track of the global min length of superstring and the last added word in
        the best scenario. Once DP is done, we can reconstruct the path from
        the last word and the path table. The rest is trivial compared to the
        massive effort of DP.

        This problem is termed the travelling salesman problem.

        O(2^N * N^2), 944 ms, 43% ranking
        """
        N = len(words)
        # Build the graph, where graph[i][j] is the number of letters to append
        # to the end of words[i] such that the new string covers both i and j.
        graph = [[math.inf] * N for _ in range(N)]
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j:
                    for o in range(min(len(w1), len(w2)) - 1, -1, -1):
                        if w1.endswith(w2[:o]):
                            graph[i][j] = len(w2) - o
                            break

        # dp[state][i] is the min length of superstring at the current state and
        # has just added words[i]. State is a bitmap version to record which
        # words have been used. If words indices 3, 1, 0 have been used, state
        # = 1011. Using bitmap allows us to easily record and manipulate the
        # state of currently used words.
        dp = [[math.inf] * N for _ in range(1 << N)]
        # path[state][i] is the index of the word added right before words[i] is
        # added. It helps track the last step that leads to adding words[i]
        path = [[math.inf] * N for _ in range(1 << N)]
        # overall min length of superstring and the index of the last added word
        min_len, last = math.inf, 0
        for state in range(1 << N):
            for i in range(N):  # go through all possible current last word
                if (state >> i) & 1:  # words[i] is in state
                    pre_state = state - (1 << i)  # previous state
                    if pre_state == 0:  # words[i] is the first word
                        dp[state][i] = len(words[i])
                        continue
                    for j in range(N):  # go through all possible previous word
                        # words[j] is in pre_state and in the previous state doing
                        # words[j] and then words[i] yields shorter superstring
                        if ((pre_state >> j) & 1) and dp[pre_state][j] + graph[j][i] < dp[state][i]:
                            dp[state][i] = dp[pre_state][j] + graph[j][i]
                            path[state][i] = j
                        if state == ((1 << N) - 1) and dp[state][i] < min_len:
                            min_len = dp[state][i]
                            last = i
        # Construct the path using the indices of the words
        best_path = []
        cur_state = (1 << N) - 1
        while cur_state:
            best_path.append(last)
            temp = cur_state
            cur_state -= (1 << last)
            last = path[temp][last]
        # Construct the resulting string
        pre_idx = best_path.pop()
        res = words[pre_idx]
        while best_path:
            cur_idx = best_path.pop()
            res += words[cur_idx][-graph[pre_idx][cur_idx]:]
            pre_idx = cur_idx
        return res


sol = Solution2()
tests = [
    (['a'], 'a'),
    (['catg', 'ctaagt', 'gcta', 'ttca', 'atgcatc'], 'gctaagttcatgcatc'),
    (['alex', 'loves', 'leetcode'], 'leetcodelovesalex'),
    (['abcde', 'cdea'], 'abcdea'),
    (['abcdef', 'efde', 'defab'], 'efdefabcdef'),
    (['xas', 'nxv', 'ownx', 'xvf', 'vfv'], 'ownxvfvxas'),
    (['lugeuklyt', 'thwokzob', 'rilsthwokz', 'onkrilsthw', 'kzobvtr', 'krilsthwo'], 'onkrilsthwokzobvtrlugeuklyt'),
    (['cedefifgstkyxfcuajfa', 'ooncedefifgstkyxfcua', 'assqjfwarvjcjedqtoz', 'fcuajfassqjfwarvjc', 'fwarvjcjedqtozctcd', 'zppedxfumcfsngp', 'kyxfcuajfassqjfwa', 'fumcfsngphjyfhhwkqa', 'fassqjfwarvjcjedq', 'ppedxfumcfsngphjyf', 'dqtozctcdk'], 'ooncedefifgstkyxfcuajfassqjfwarvjcjedqtozctcdkzppedxfumcfsngphjyfhhwkqa'),
]

for i, (words, ans) in enumerate(tests):
    res = sol.shortestSuperstring(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
