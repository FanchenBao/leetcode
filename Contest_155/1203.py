#! /usr/bin/env python3
from typing import List, Dict, Set
from collections import defaultdict
from random import randint

"""10/12/2019

"""

MAX = 2**31 - 1
MIN = -(2**31)


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        before_groups: Dict[int, List[int]] = defaultdict(list)
        for i, items in enumerate(beforeItems):
            for j, it in enumerate(items):
                # i has no group but its ancestor is in a group
                if group[it] >= 0 and group[i] < 0:
                    items[j] = group[it] + n
                # i is in a group but its ancestor has no group
                elif group[i] >= 0 and group[it] < 0:
                    before_groups[group[i] + n].append(it)  # delegate to group
                    del items[j]  # no more ancesotr for i
                # i and it both belongs to different groups
                elif group[i] >= 0 and group[it] >= 0 and group[i] != group[it]:
                    before_groups[group[i] + n].append(group[it] + n)
                    del items[j]
        # print(before_groups)
        # print(beforeItems)
        overall_pos: Dict[int, int] = defaultdict(lambda: -1)
        pos_in_group: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(lambda: -1))
        used_pos: Set[int] = set()
        for i, items in enumerate(beforeItems):
            if not items:  # no ancestor
                # does not belong to group and haven't been assigned pos yet
                if group[i] < 0 and overall_pos[i] < 0:
                    overall_pos[i] = self.get_random_pos(MIN, MAX, used_pos)
                elif group[i] >= 0 and overall_pos[group[i] + n] < 0:
                    overall_pos[n + group[i]] = self.get_random_pos(MIN, MAX, used_pos)
            else:  # there are ancestors
                for anc in items:
                    if group[i] < 0:
                        if not self.process_pos(i, anc, overall_pos, beforeItems, before_groups, used_pos):
                            return []
                    else:  # i and anc belong to the same group
                        if not self.process_pos(i, anc, pos_in_group[group[i]], beforeItems, before_groups, used_pos):
                            return []

    def find_anc_pos(self, anc: int, beforeItems: List[List[int]], before_groups: Dict[int, List[int]], curr_pos: int, used_pos: Set[int]) -> int:
        pass

    def process_pos(self, curr: int, anc: int, pos_dict, beforeItems: List[List[int]], before_groups: Dict[int, List[int]], used_pos: Set[int]) -> bool:
        if pos_dict[anc] < 0:
            pos_dict[anc] = self.find_anc_pos(anc, beforeItems, before_groups, pos_dict[curr], used_pos)
        if pos_dict[anc] < 0:  # impossible arrangement found
            return False
        if pos_dict[curr] < 0 or (pos_dict[curr] >= 0 and pos_dict[anc] >= pos_dict[curr]):
            pos_dict[curr] = self.get_random_pos(pos_dict[anc] + 1, MAX, used_pos)
        return True

    def get_random_pos(self, lo: int, hi: int, used_pos: Set[int]):
        pos = randint(lo, hi)
        while pos in used_pos:
            pos = randint(lo, hi)
        used_pos.add(pos)
        return pos






sol = Solution()
n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
sol.sortItems(n, m, group, beforeItems)