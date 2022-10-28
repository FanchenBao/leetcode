# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """LeetCode 49

        This one turns counter into a string for hashing.

        O(MN), where N = len(strs), M is the average length of word in strs.
        387 ms, faster than 5.01%
        """
        res_dict = defaultdict(list)
        for word in strs:
            c = Counter(word)
            k = ''.join(f'{le}{c[le]}' for le in sorted(c))
            res_dict[k].append(word)
        return list(res_dict.values())


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Hash with tuple.

        Same complexity, but much much faster. 154 ms, faster than 75.38%
        """
        res_dict = defaultdict(list)
        for word in strs:
            c = [0] * 26
            for le in word:
                c[ord(le) - 97] += 1
            res_dict[tuple(c)].append(word)
        return list(res_dict.values())

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
