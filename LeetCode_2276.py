# from pudb import set_trace; set_trace()
from typing import List


class TreeNode:
    def __init__(self, lo: int, hi: int) -> None:
        self.lo = lo
        self.hi = hi
        self.count = 0
        self.left = None
        self.right = None

    def __repr__(self):
        return f'({self.lo}, {self.hi})'


class CountIntervals:

    def __init__(self):
        self.root = TreeNode(1, 10**9)

    def _update(self, node: TreeNode, lo: int, hi: int) -> None:
        if node.lo == lo and node.hi == hi:
            node.count = hi - lo + 1
            return
        mid = (node.lo + node.hi) // 2
        if not node.left:
            node.left = TreeNode(node.lo, mid)
        if not node.right:
            node.right = TreeNode(mid + 1, node.hi)
        if hi <= mid:
            self._update(node.left, lo, hi)
        elif lo > mid:
            self._update(node.right, lo, hi)
        else:
            self._update(node.left, lo, mid)
            self._update(node.right, mid + 1, hi)
        node.count = node.left.count + node.right.count

    def add(self, left: int, right: int) -> None:
        self._update(self.root, left, right)

    def count(self) -> int:
        return self.root.count


actions = ["CountIntervals","count","add","add","add","add","add","count","add","add"]
values = [[],[],[8,43],[13,16],[26,33],[28,36],[29,37],[],[34,46],[10,23]]
answers = [None,0,None,None,None,None,None,36,None,None]
ci = CountIntervals()
for act, val, ans in zip(actions[1:], values[1:], answers[1:]):
    if act == 'add':
        ci.add(*val)
    else:
        res = ci.count()
        if res != ans:
            print(f'Failed: {res=}, {ans=}')

