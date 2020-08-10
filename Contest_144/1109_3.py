"""
07/08/2019

This is the segment tree solution according to a different implementation. The
basic set up derives from this website:
"https://blog.csdn.net/Yaokai_AssultMaster/article/details/79599809#commentBox"

However, I've made some necessary changes to make the implementation more
understandable to me. The core idea of this implementation is to set up the
segment tree as a complete binary tree with the leaf nodes going in the same
order as the given array. Thus, we can easily find the index of the array
element in segtree (if the element's index is i in array, its index in segtree
is i + n where n is the length of the array). The implementation of segtree in
1109_2.py is not a complete binary tree but a full binary tree (i.e. the array
representation of the tree contains dummy elements)

In my implementation, each parent node represents includes the range from its
left and right children. The root of segment tree is indexed 1 in the segtree
array, thus for any parent node i, its left child is 2i, and right child 2i+1.
With this set up, for any given range, either for query or initiation, if the
range start's segtree array index is even, then the range can be represented
at least partially by the range start's parent node. If range start's segtree
array index is odd, then its parent node is not part of the range. We need to
check the value of the range start, and increment range start by 1. Similarly,
if range end's segtree array index is odd, its parent node partially represents
the range, and we are good. If it is even, then we check its value, and then
decrement range end by 1. Then we go for the parent node and repeat the same
procedures, until range start is larger than range right, in which case we end
the loop, or range start is equal to range right, in which case we check the
segtree array value at range start, and then end the array.

The above implemnetation is strictly log(n). Overall complexity is O(nlog(n))
This solution is accepted by OJ.
"""


class Solution:
    def corpFlightBookings(self, bookings, n):
        # treat as complete binary tree with root at index 1
        segtree = [0] * (2 * n)
        for book in bookings:
            self.segtreeInit(book, segtree, n)
        return [self.query(segtree, i + n) for i in range(n)]

    def segtreeInit(self, book, segtree, n):
        s = book[0] - 1 + n
        e = book[1] - 1 + n
        while s < e:
            if s % 2:  # s is odd, need to increment s
                segtree[s] += book[2]
                s += 1
            if not e % 2:  # e is even, need to decrement e
                segtree[e] += book[2]
                e -= 1
            # move to parent node
            s //= 2
            e //= 2
        if s == e:
            segtree[s] += book[2]

    def query(self, segtree, q):
        res = 0
        while q:
            res += segtree[q]
            q //= 2
        return res


bookings = [[1, 2, 20], [1, 2, 50]]
n = 2
sol = Solution()
print(sol.corpFlightBookings(bookings, n))
