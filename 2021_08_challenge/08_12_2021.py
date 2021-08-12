# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """LeetCode 49

        Sort each string to obtain its signature. Group all the strings with
        the same signature together using a dict.

        O(N * MlogM), where N is the size of strs and M is the average length
        of each string. 113 ms, 30% ranking.
        """
        hashmap = defaultdict(list)
        for s in strs:
            hashmap[tuple(sorted(s))].append(s)
        return list(hashmap.values())


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Use letter count in an array of size 26 as signature to avoid sort

        O(N * M), 100 ms, 57% ranking.
        """
        hashmap = defaultdict(list)
        for s in strs:
            sig = [0] * 26
            for le in s:
                sig[ord(le) - 97] += 1
            hashmap[tuple(sig)].append(s)
        return list(hashmap.values())


sol = Solution2()
tests = [
    (['eat', 'tea', 'tan', 'ate', 'nat', 'bat'], [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]),
    ([''], [['']]),
    (['a'], [['a']]),
]

for i, (strs, ans) in enumerate(tests):
    res = sol.groupAnagrams(strs)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
