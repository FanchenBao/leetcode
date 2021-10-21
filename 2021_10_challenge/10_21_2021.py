# from pudb import set_trace; set_trace()
from typing import List
from random import randint, choice


class RandomizedSet1:
    """This scheme worked! I am very surprised and happy at the same time. This
    scheme requires a list in order to do getRandom(). The problem with a list
    is that remove will take O(N) to complete (insert is not affected). To
    reduce the time complexity of remove, we need a compromise. The compromise
    is this: if the size of the current set is more than half of the size of
    the list, we simply don't remove anything from the list when a remove call
    is made. This is because we have more than 50% chance of returning a true
    value. When the size of the current set drops at or below half of the size
    of the list, that's when we need to do some housekeeping. Basically we need
    to pop from the list the values that are not supposed to be there. Since
    we have built up to a point where the number of values to delete in the list
    is half the list's size, it will take a very short traversal to locate one
    to be deleted. So we locate one to be deleted, swap it with the tail of
    the list, and then pop it. By doing this, we will ensure that the
    probability of obtaining a random value from the list that also exists in
    the current set is always more than 50%.

    In addition to this, we also implemented a scheme to replace the values in
    the list that are supposed to be deleted. This scheme works like this: when
    a random value generated from the list is not in the current set, we record
    its index, such that the next time a value is added, we don't append to the
    list, but put the new value in one of the empty indices. This is another
    way to actively inflate the number of true values in the list.

    Insert always takes O(1). On average getRandom and remove will take O(2),
    because the likelihood of obtaining the true value is larger than 50%.

    875 ms, 14% ranking.
    """

    def __init__(self):
        self.cur_set = set()
        self.lst = []
        self.empty_indices = set()

    def insert(self, val: int) -> bool:
        if val in self.cur_set:
            return False
        self.cur_set.add(val)
        for ei in self.empty_indices:
            self.lst[ei] = val
            break
        else:
            self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.cur_set:
            self.cur_set.remove(val)
            ret = True
        else:
            ret = False
        if len(self.cur_set) <= len(self.lst) // 2:
            for i in range(len(self.lst) - 1, -1, -1):
                if self.lst[i] not in self.cur_set:
                    self.lst[i], self.lst[-1] = self.lst[-1], self.lst[i]
                    self.lst.pop()
                    if i in self.empty_indices:
                        self.empty_indices.remove(i)
                    if len(self.lst) - 1 in self.empty_indices:
                        self.empty_indices.remove(len(self.lst) - 1)
                    break
        return ret        

    def getRandom(self) -> int:
        while True:
            idx = randint(0, len(self.lst) - 1)
            if self.lst[idx] not in self.cur_set:
                self.empty_indices.add(idx)
            else:
                return self.lst[idx]



class RandomizedSet:
    """This is from hiepit:

    https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/1532314/C%2B%2B-HashMap-and-List-Swap-last-element-when-remove-O(1)-in-Time-Clean-and-Concise

    We are so close to the smart solution. The key point is to always remove
    the value from the list. We can do so by first remembering each value's
    index. When we remove, we simply swap the to-remove value to the end of
    the list and then pop it. By doing this, we ensure that at any moment, the
    list always contains all the values in the current set.
    """

    def __init__(self):
        self.cur_dict = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.cur_dict:
            return False
        self.lst.append(val)
        self.cur_dict[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cur_dict:
            return False
        idx = self.cur_dict[val]
        # must update the index before removing from self.cur_dict, because
        # it is possible that the value to be removed is already at the end
        # of self.lst
        self.cur_dict[self.lst[-1]] = idx
        del self.cur_dict[val]
        self.lst[idx], self.lst[-1] = self.lst[-1], self.lst[idx]
        self.lst.pop()
        return True    

    def getRandom(self) -> int:
        return choice(self.lst)



sol = Solution3()
tests = [
    ('abab', True),
    ('aba', False),
    ('abcabcabcabc', True),
    ('abcabcababcabcab', True),
    ('abcbac', False),
    ('aabaabaab', True),
    ('a', False),
    ('aaaaaaa', True),
    ('aaaaab', False),
]

for i, (s, ans) in enumerate(tests):
    res = sol.repeatedSubstringPattern(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
