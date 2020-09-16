# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """Naive brute force, TLE"""
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = max(res, nums[i] ^ nums[j])
        return res


class Solution2:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """Look for potentials first to reduce search size. TLE"""
        length = len(bin(max(nums))) - 2
        bin_nums = [format(n, f'0{length}b') for n in nums]
        for pos in range(length):
            potentials = []
            for i, bn in enumerate(bin_nums):
                if bn[pos] == '1':
                    potentials.append(nums[i])
            if len(potentials) < len(nums):
                break
        res = 0
        for pot in potentials:
            for n in nums:
                res = max(res, pot ^ n)
        return res


class TrieNode:
    def __init__(self):
        self.next_nodes = [None, None]
        self.val = -1

class Solution3:
    def build_trie(self, num: int, root: TrieNode) -> None:
        node = root
        for i in range(31, -1, -1):
            d = num >> i & 1
            if node.next_nodes[d] is None:
                node.next_nodes[d] = TrieNode()
            node = node.next_nodes[d]
        node.val = num

    def findMaximumXOR(self, nums: List[int]) -> int:
        """This is a better Trie solution than my previous attempt (already
        deleted because its TrieNode set up is too bad). My previous attempt
        tried to find the max by traversing the trie. It worked, but due to
        bifurcating situations, the recursion could run very deep. The current
        solution does not search for the max from the trie. Instead, it
        computes the max XOR each number can get by checking, bit by bit,
        whether there exists another number in the trie that can make the XOR
        value for the bit 1. If there exists such value, the trie goes that
        specific branch. We keep track of the max XOR value each number can
        get, and return the largest of them.
        """
        root = TrieNode()
        for n in nums:
            self.build_trie(n, root)
        res = 0
        for n in nums:  # check the largest xor each num can get
            node = root
            cur = 0
            for i in range(31, -1, -1):
                d = n >> i & 1  # current bit from left to right
                if node.next_nodes[d ^ 1] is None:
                    node = node.next_nodes[d]
                else:
                    node = node.next_nodes[d ^ 1]
                    cur |= 1 << i
            res = max(res, cur)
        return res


class Solution4:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """Similar idea as the trie, but using a set to record prefixes
        
        This one is much faster. ranking at 72%.
        """
        mask, res = 0, 0
        for i in range(31, -1, -1):
            mask = mask | 1 << i
            prefixes = set(n & mask for n in nums)
            pot_max = res | 1 << i
            if any((pot_max ^ n) in prefixes for n in prefixes):
                res = pot_max
        return res


sol = Solution4()
tests = [
    ([96401, 56140, 27138, 31551, 46701, 7610, 35232, 57981, 5146, 21516, 7365, 86253, 6055, 13283, 47873, 14977, 20021, 73153, 98685, 60032, 2031, 66300, 20805, 62505, 88328, 92910, 5270, 54199, 10064, 91081, 52580, 22752, 54162, 95303, 38216, 21528, 81901, 52447, 94246, 87859, 77453, 64212, 97335, 92424, 89157, 65159, 59415, 80273, 23596, 79981, 79948, 16270, 88113, 23740, 67217, 7849, 51484, 78558, 62655, 68660, 29570, 56584, 89303, 17230, 31204, 14949, 21326, 25381, 82757, 36619, 56053, 60822, 47814, 91855, 18724, 91184, 35264, 6228, 21251, 50646, 70525, 50174, 15637, 69731, 39668, 40293, 69953, 16039, 25695, 15525, 98142, 91504, 23898, 23186, 90522, 38020, 60059, 66121, 98887, 3914, 2376, 88706, 11235, 54633, 61049, 66690, 59970, 62440, 92043, 78156, 47194, 59573, 90558, 29047, 7659, 43873, 37228, 65787, 49033, 15656, 49991, 6117, 43943, 5678, 4909, 9034, 93634, 23077, 31114, 30872, 49511, 6348, 5419, 79528, 69794, 66993, 33434, 86288, 66756, 566, 24187, 42325, 48815, 80849, 59778, 87773, 42690, 18734, 68078, 94754, 27900, 84656, 63814, 80803, 63278, 88180, 50959, 19317, 38210, 12470, 55399, 55126, 97730, 53965, 57281, 51010, 64870, 16273, 47997, 61182, 93630, 95325, 57347, 61746, 93336, 88271, 7324, 91124, 10222, 87021, 3534, 44543, 88079, 76130, 16658, 12099, 44424, 43109, 11219, 22198, 70703, 74394, 90628, 84871, 70348, 73298, 5118, 28051, 82789, 91278], 131036),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findMaximumXOR(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
