# from pudb import set_trace; set_trace()
from typing import List, Tuple
from math import gcd, sqrt
from collections import deque, Counter, defaultdict


class Solution1:
    def max_component(self, A):
        cfs = {A.popleft()}
        count = 1
        while A:
            size_A_before = len(A)
            for _ in range(len(A)):
                val = A.popleft()
                new_cfs = set()
                addition = False
                for cf in cfs:
                    gcd_val = gcd(val, cf)
                    if gcd_val > 1:
                        new_cfs.add(gcd_val)
                        new_cfs.add(val // gcd_val)
                        new_cfs.add(cf // gcd_val)
                        addition = True
                    else:
                        new_cfs.add(cf)
                if 1 in new_cfs:
                    new_cfs.remove(1)
                if not addition:
                    A.append(val)
                else:
                    count += 1
                cfs = new_cfs
            if size_A_before == len(A):  # no val has been removed from A
                return count
        return count

    def largestComponentSize(self, A: List[int]) -> int:
        """TLE"""
        A = deque(A)
        max_count = 0
        while A:
            cur_count = self.max_component(A)
            max_count = max(max_count, cur_count)
        return max_count


# class DJU:
#     def __init__(self, A: List[int]):
#         self.unions = list(range(len(A)))
#         self.pos = {a: i for i, a in enumerate(A)}

#     def find(self, n) -> int:
#         """Find root of n, and compress its path

#         :param n: The node whose root is to be found.
#         :return: The pos of the current node n and the root.
#         """
#         path = []
#         root = self.pos[n]
#         while self.unions[root] != root:  # find the root of the current union
#             path.append(root)
#             root = self.unions[root]
#         for pos in path:  # compress path
#             self.unions[pos] = root
#         return root

#     def union(self, n1, n2) -> int:
#         """Merge the unions of n1 and n2.

#         :param n1: One of the node to be merged.
#         :param n2: The other node to be merged.
#         :return: Root after union
#         """
#         r1 = self.find(n1)
#         r2 = self.find(n2)
#         if r1 > r2:
#             self.unions[r1] = r2
#         elif r1 < r2:
#             self.unions[r2] = r1
#         return min(r1, r2)


class Solution2:
    def largestComponentSize(self, A: List[int]) -> int:
        """TLE"""
        dju = DJU(A)
        factors = defaultdict(set)
        for i, a in enumerate(A):
            pa, ra = dju.compress(a)
            if pa != ra:
                a_val = a
                for fac in factors[ra]:
                    a_val = a_val // gcd(a_val, fac)
                if a_val == 1:  # current value a will not have any impact
                    continue
            for b in A[i + 1:]:
                cf = gcd(a, b)
                if cf > 1:
                    root = dju.union(a, b)
                    factors[root].add(cf)
        return Counter(dju.unions).most_common(1)[0][1]


class DJU:
    """This disjoint union supports union and find (with path compression).

    It is based on the original index of the given elements, thus there is no
    need to set up an additional mapping from the element value to its index.
    """

    def __init__(self, A: List[int]):
        self.unions = list(range(len(A)))

    def find(self, idx) -> int:
        """Find root of idx. Perform path compression along the way

        :param idx: The index whose root is to be found.
        :return: The pos of the current node n and the root.
        """
        if self.unions[idx] != idx:
            self.unions[idx] = self.find(self.unions[idx])  # compression
        return self.unions[idx]

    def union(self, i, j) -> None:
        """Merge the nodes of indices i and j

        :param i: Index of one of the node to be merged.
        :param j: Index of the other node to be merged.
        """
        self.unions[self.find(i)] = self.find(j)


class Solution:
    def generate_primes(self, n):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return self.generate_primes(n // i).union(set([i]))
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:
        """This is not my solution. I have to learn from the forum to realize
        two things:

        1. Prime factoring is fast, and should be used in favor of GCD, because
        it allows for easy grouping of the numbers. Prime factoring is of
        O(llog(n)) complexity. This grouping only requires traversing the
        original array once, which is vastly faster than my other O(n^2)
        solution.

        2. Path compression is crucial for union-find. The forum sample code
        provides a much neater way to do path compression (recursion).
        """
        dju = DJU(A)
        prime_groups = defaultdict(list)
        for i, a in enumerate(A):
            for p in self.generate_primes(a):
                prime_groups[p].append(i)
        for _, prime_group in prime_groups.items():
            for j in range(len(prime_group) - 1):
                dju.union(prime_group[j], prime_group[j + 1])
        return max(Counter(dju.find(i) for i in range(len(A))).values())


sol = Solution()

tests = [
    ([20, 50, 9, 63], 2),
    ([4, 6, 15, 35], 4),
    ([2, 3, 6, 7, 4, 12, 21, 39], 8),
    ([12, 3, 4, 5, 6, 7, 8, 5, 23, 46, 78], 8),
    ([1], 1),
    ([32, 98, 9, 43, 66, 49, 83, 94, 95], 6),
    ([99, 68, 70, 77, 35, 52, 53, 25, 62], 8),
    ([65, 27, 100, 37, 12, 19, 4, 58, 91, 5], 8),
    ([65, 35, 43, 76, 15, 11, 81, 22, 55, 92, 31], 9),
]

for i, (test, ans) in enumerate(tests):
    res = sol.largestComponentSize(test)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
