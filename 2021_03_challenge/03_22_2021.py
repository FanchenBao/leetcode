# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import re


class Solution:
    """LeetCode 966

    TLE
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}

    def vowel_match(self, word: str, query: str) -> bool:
        if len(word) != len(query):
            return False
        for wl, ql in zip(word, query):
            if wl != ql and (wl not in self.vowels or ql not in self.vowels):
                return False
        return True

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = [''] * len(queries)
        for i, q in enumerate(queries):
            c_match = False
            v_match = False
            for w in wordlist:
                if q == w:
                    res[i] = w
                    break
                elif not c_match and q.lower() == w.lower():
                    res[i] = w
                    c_match = True
                elif not v_match and not c_match and self.vowel_match(w.lower(), q.lower()):
                    res[i] = w
                    v_match = True
        return res


class Solution2:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """This is a VERY VERY convoluted method. It uses a Trie to preprocess
        the wordlist. And for each query, we go through the Trie to see if
        anything matches. The to go through the Trie is that, if the query's
        letter is a vowel, we dfs into any vowels available, both upper and
        lower case. If the letter is a consonant, we go through its upper and
        lower case should they exist in the Trie.

        At the end, if we have reached the end of a Trie branch, we determine
        whether the match is a full match, a captilization match, or a vowel
        match. The full match has higher priority than cap match, which has higher
        priority than vowel match.

        The runtime depends on how many branches we visit during the traversal
        of the Trie. The worst case is that the Trie consists of only vowels or
        both upper and lower letters. Then we looking at 10 branches per level,
        which can result in astronomical runtime. But the average case should
        be O(N), because we expect each Trie level will not branch out too much.

        308 ms, 16% ranking.
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        TrieNode = lambda: defaultdict(TrieNode)
        root = TrieNode()
        for i, word in enumerate(wordlist):
            node = root
            for w in word:
                node = node[w]
            if 'idx' not in node:
                node['idx'] = i

        def dfs(query, idx, node):
            if idx == len(query):
                if 'idx' in node:
                    if query == wordlist[node['idx']]:
                        data['F'].append(node['idx'])
                    elif query.lower() == wordlist[node['idx']].lower():
                        data['C'].append(node['idx'])
                    else:
                        data['V'].append(node['idx'])
            else:
                le = query[idx]
                if le in vowels:
                    for v in vowels:
                        if v in node:
                            dfs(query, idx + 1, node[v])
                else:
                    if le.lower() in node:
                        dfs(query, idx + 1, node[le.lower()])
                    if le.upper() in node:
                        dfs(query, idx + 1, node[le.upper()])

        res = []
        for query in queries:
            data = {'F': [], 'C': [], 'V': []}
            dfs(query, 0, root)
            if data['F']:
                res.append(query)
            elif data['C']:
                res.append(wordlist[min(data['C'])])
            elif data['V']:
                res.append(wordlist[min(data['V'])])
            else:
                res.append('')
        return res


class Solution3:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """This is the official solution using two hashmaps and a set. It is a
        better solution both in runtime and logic.

        188 ms, 49% ranking.
        """
        f_match = set(wordlist)
        c_match = {}  # all matching via changing capitalization
        v_match = {}  # all matching via swapping vowels
        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in c_match:
                c_match[lower_word] = word
            # must use lowercase world to avoid further comparison in
            # capitalization
            swapped_word = re.sub(r'[aeiou]', '*', lower_word)
            if swapped_word not in v_match:
                v_match[swapped_word] = word

        res = []
        for query in queries:
            lower_query = query.lower()
            swapped_query = re.sub(r'[aeiou]', '*', lower_query)
            if query in f_match:
                res.append(query)
            elif lower_query in c_match:
                res.append(c_match[lower_query])
            elif swapped_query in v_match:
                res.append(v_match[swapped_query])
            else:
                res.append('')
        return res


sol = Solution3()
tests = [
    (["KiTe", "kite", "hare", "Hare"], ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"], ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]),
    (["KiTe", "kite", "hare", "Hare"], ["kite", "kitE", "kiTe", "kIte", "Kite", "kiTE", "kITe", "KIte"], ["kite", "KiTe", "KiTe", "KiTe", "KiTe", "KiTe", "KiTe", "KiTe"]),
    (["eb", "ab"], ["aB"], ["ab"]),
    (["YellOw"], ["yollow"], ["YellOw"]),
]

for i, (wordlist, queries, ans) in enumerate(tests):
    res = sol.spellchecker(wordlist, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
