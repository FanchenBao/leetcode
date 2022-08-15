# from pudb import set_trace; set_trace()
from typing import List, Set
from collections import defaultdict
from functools import lru_cache
import math


class Solution1:
    def does_differ_by_one(self, w1: str, w2: str) -> bool:
        num_diff = 0
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                num_diff += 1
        return num_diff == 1

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """DFS, TLE"""
        if endWord not in wordList:
            return []
        graph = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.does_differ_by_one(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        if beginWord not in graph:
            for w in wordList:
                if self.does_differ_by_one(beginWord, w):
                    graph[beginWord].append(w)

        visited = set()

        @lru_cache(maxsize=None)
        def dfs(cur_word: str, path_str: str) -> List[List[str]]:
            if cur_word == endWord:
                return [[endWord]]
            visited.add(cur_word)
            res = []
            for next_word in graph[cur_word]:
                if next_word not in visited:
                    paths = dfs(next_word, path_str + cur_word)
                    if not res or (paths and len(res[0]) == 1 + len(paths[0])):
                        for p in paths:
                            res.append([cur_word] + p)
                    elif paths and len(res[0]) > 1 + len(paths[0]):
                        res = [[cur_word] + p for p in paths]
            visited.remove(cur_word)
            return res
        return dfs(beginWord, '')


class Solution2:
    def does_differ_by_one(self, w1: str, w2: str) -> bool:
        num_diff = 0
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                num_diff += 1
        return num_diff == 1

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """BFS, TLE"""
        if endWord not in wordList:
            return []
        graph = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.does_differ_by_one(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        if beginWord not in graph:
            for w in wordList:
                if self.does_differ_by_one(beginWord, w):
                    graph[beginWord].append(w)

        queue = [(beginWord, [beginWord])]
        res = []
        while queue:
            temp = []
            for cur_word, path in queue:
                for next_word in graph[cur_word]:
                    if next_word == endWord:
                        res.append(path + [next_word])
                    elif next_word not in path:
                        temp.append((next_word, path + [next_word]))
            if res:
                break
            queue = temp
        return res


class Solution3:
    
    def find_dag_neighbors(self, word: str, words_set: Set[str]) -> Set[str]:
        res = set()
        for i in range(len(word)):
            for j in range(26):  # swap letter at each position
                new = word[:i] + chr(j + 97) + word[i + 1:]
                if new != word and new in words_set:
                    res.add(new)
        return res

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """LeetCode 126

        Got hit by TLE on both naive DFS and BFS. Gave up and checked my
        solution before. The trick is to first create a DAG and then DFS the
        DAG to find the solution. The DAG simply indicates layers of words that
        eventually can lead to the endWord. For instance, the example

        "hit", "cog", ["hot","dot","dog","lot","log","cog"]

        will create a DAG like this:

        [hit] --> [hot] --> [dot, lot] --> [dog, log] --> [cog]

        DAG can be represented by a dictionary, where each word is the key and
        the value is a set of words that are the next level in the DAG while
        also being neighbors of the key.

        The DAG can be constructed via BFS.

        SURPRISE!! The old solution got TLE as well!! My Lord!
        """
        # build the DAG via BFS
        dag = defaultdict(set)
        words_set = set(wordList)
        if endWord not in words_set:
            return []
        if beginWord in words_set:
            words_set.remove(beginWord)
        queue = set([beginWord])
        while queue:
            temp = set()
            for cur_word in queue:
                if cur_word == endWord:
                    dag[cur_word].add('')
                    break
                dag_neighbors = self.find_dag_neighbors(cur_word, words_set)
                dag[cur_word] = dag_neighbors
                temp = temp.union(dag_neighbors)
            if endWord in dag:
                break
            words_set -= temp
            queue = temp
        if endWord not in dag:  # endWord is in wordList but it can never be reached
            return []
        # Build answer via DFS
        res = []

        def dfs(cur_word: str, path: List[str]) -> None:
            if cur_word == endWord:
                res.append(path + [cur_word])
                return
            path.append(cur_word)
            for nei in dag[cur_word]:
                dfs(nei, path)
            path.pop()

        dfs(beginWord, [])
        return res


class Solution4:
    
    def does_differ_by_one(self, w1: str, w2: str) -> bool:
        num_diff = 0
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                num_diff += 1
        return num_diff == 1

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """LeetCode 126

        The old implementation of DAG uses a lot of set operations, which might
        be the reason why it timed out. Let's not use that many set and see if
        we have a better chance of passing. The DAG + DFS approach is very
        appealing to me and I want to make it work.

        TLE again. This solution still uses set.union, which I think is the
        culprit of TLE. We need to achieve set.union for the next queue without
        actually using set.
        """
        if endWord not in wordList:
            return []
        # build the original graph
        graph = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.does_differ_by_one(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        if beginWord not in graph:
            for w in wordList:
                if self.does_differ_by_one(beginWord, w):
                    graph[beginWord].append(w)
        # build the DAG via BFS
        dag = defaultdict(list)
        queue, visited = [beginWord], set([beginWord])
        while queue:
            temp = set()
            for cur_word in queue:
                if cur_word == endWord:
                    dag[cur_word].append('')
                    break
                for next_word in graph[cur_word]:
                    if next_word not in visited:
                        temp.add(next_word)
                        dag[cur_word].append(next_word)
            if endWord in dag:
                break
            visited = visited.union(temp)
            queue = temp
        if endWord not in dag:  # endWord is in wordList but it can never be reached
            return []
        # Build answer via DFS
        res = []

        def dfs(cur_word: str, path: List[str]) -> None:
            if cur_word == endWord:
                res.append(path + [cur_word])
                return
            path.append(cur_word)
            for nei in dag[cur_word]:
                dfs(nei, path)
            path.pop()

        dfs(beginWord, [])
        return res


class Solution5:
    
    def does_differ_by_one(self, w1: str, w2: str) -> bool:
        num_diff = 0
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                num_diff += 1
        return num_diff == 1

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """LeetCode 126

        The difficult part of BFS is that when we are deciding whether to put
        a next word in the next queue, we need to allow duplicates such that
        different parent word can link to the same child word. This is allowed
        in a DAG. However, if we do so, we will have to use union to update the
        visited set.

        To avoid the costly union operation, we need a better way to decide
        whether which words are visited. This post offers a smart way to do so:
        using distance to beginWord. A not visited word must have distance to
        beginWord one bigger than its parent word. Yet, we are allowing the
        same word to be attached to multiple parent word, because as long as
        the distance requirement is satisfied, it is fine.

        That is just one small optimization. The really big optimization is
        that when we construct the answer via DFS, we must go from endWord to
        beginWord. This is because the BFS step includes a lot of words that
        do not lead to endWord. Those are wasted effort if we DFS from begin
        to end. However, we are certain that if we go from end to begin, all
        paths lead back to begin. Hence there is no wasted efforts. Therefore,
        the DFS has to be backwards, which means the DAG has to be pointing
        backwards as well (child pointing back to parent.)

        Ref: https://leetcode.com/problems/word-ladder-ii/discuss/2423520/Python-or-BFS-%2B-Backtracking-or-Simple-Code
        """
        if endWord not in wordList:
            return []
        # build the original graph
        graph = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.does_differ_by_one(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        if beginWord not in graph:
            for w in wordList:
                if self.does_differ_by_one(beginWord, w):
                    graph[beginWord].append(w)
        # build a backwards DAG (child pointing back to parents) via BFS
        dag_back = defaultdict(list)
        dist_to_begin = defaultdict(int)
        dist_to_begin[beginWord] = 0
        queue = [beginWord]
        while queue:
            temp = []
            for cur_word in queue:
                if cur_word == endWord:
                    break
                for next_word in graph[cur_word]:
                    if next_word not in dist_to_begin:  # first encounter
                        temp.append(next_word)
                        dist_to_begin[next_word] = 1 + dist_to_begin[cur_word]
                    # as long as the distance of next_word shows that it is
                    # the first time next_word is encountered in the current
                    # branch, it is okay. It is allowed to have multiple
                    # branches ending at next_word (i.e. next_word has many
                    # parents)
                    if 1 + dist_to_begin[cur_word] == dist_to_begin[next_word]:
                        dag_back[next_word].append(cur_word)
            if endWord in dag_back:
                break
            queue = temp
        if endWord not in dag_back:  # endWord is in wordList but it can never be reached
            return []
        # Build answer via DFS
        res = []

        def dfs(cur_word: str, path: List[str]) -> None:
            if cur_word == beginWord:
                res.append((path + [cur_word])[::-1])
                return
            path.append(cur_word)
            for prev_word in dag_back[cur_word]:
                dfs(prev_word, path)
            path.pop()

        dfs(endWord, [])
        return res


sol = Solution5()
tests = [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]),
    ("hit", "cog", ["hot","dot","dog","lot","log"], []),
    ("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"], [['qa', 'ca', 'cm', 'sm', 'sq'], ['qa', 'ca', 'ci', 'si', 'sq'], ['qa', 'ca', 'cr', 'sr', 'sq'], ['qa', 'ca', 'co', 'so', 'sq'], ['qa', 'ba', 'br', 'sr', 'sq'], ['qa', 'ba', 'bi', 'si', 'sq'], ['qa', 'ba', 'be', 'se', 'sq'], ['qa', 'ra', 're', 'se', 'sq'], ['qa', 'ra', 'rn', 'sn', 'sq'], ['qa', 'ra', 'rh', 'sh', 'sq'], ['qa', 'ra', 'rb', 'sb', 'sq'], ['qa', 'fa', 'fe', 'se', 'sq'], ['qa', 'fa', 'fr', 'sr', 'sq'], ['qa', 'fa', 'fm', 'sm', 'sq'], ['qa', 'ya', 'yo', 'so', 'sq'], ['qa', 'ya', 'yb', 'sb', 'sq'], ['qa', 'ya', 'ye', 'se', 'sq'], ['qa', 'ma', 'mt', 'st', 'sq'], ['qa', 'ma', 'mb', 'sb', 'sq'], ['qa', 'ma', 'me', 'se', 'sq'], ['qa', 'ma', 'mo', 'so', 'sq'], ['qa', 'ma', 'mn', 'sn', 'sq'], ['qa', 'ma', 'mi', 'si', 'sq'], ['qa', 'ma', 'mr', 'sr', 'sq'], ['qa', 'ga', 'go', 'so', 'sq'], ['qa', 'ga', 'ge', 'se', 'sq'], ['qa', 'ha', 'ho', 'so', 'sq'], ['qa', 'ha', 'hi', 'si', 'sq'], ['qa', 'ha', 'he', 'se', 'sq'], ['qa', 'na', 'nb', 'sb', 'sq'], ['qa', 'na', 'no', 'so', 'sq'], ['qa', 'na', 'ne', 'se', 'sq'], ['qa', 'na', 'ni', 'si', 'sq'], ['qa', 'la', 'ln', 'sn', 'sq'], ['qa', 'la', 'le', 'se', 'sq'], ['qa', 'la', 'lt', 'st', 'sq'], ['qa', 'la', 'lo', 'so', 'sq'], ['qa', 'la', 'li', 'si', 'sq'], ['qa', 'la', 'lr', 'sr', 'sq'], ['qa', 'ta', 'tm', 'sm', 'sq'], ['qa', 'ta', 'ti', 'si', 'sq'], ['qa', 'ta', 'to', 'so', 'sq'], ['qa', 'ta', 'tc', 'sc', 'sq'], ['qa', 'ta', 'th', 'sh', 'sq'], ['qa', 'ta', 'tb', 'sb', 'sq'], ['qa', 'pa', 'ph', 'sh', 'sq'], ['qa', 'pa', 'po', 'so', 'sq'], ['qa', 'pa', 'pb', 'sb', 'sq'], ['qa', 'pa', 'pm', 'sm', 'sq'], ['qa', 'pa', 'pi', 'si', 'sq'], ['qa', 'pa', 'pt', 'st', 'sq']]),
]

for i, (beginWord, endWord, wordList, ans) in enumerate(tests):
    res = sol.findLadders(beginWord, endWord, wordList)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
