class LazySegTree:
    def __init__(self, N: int) -> None:
        """This is NOT a plug-and-use lazy segment tree, but a well crafted
        template. When you encounter a problem that requires segment tree, this
        template might need to be adapted accordingly.

        Pay attention to what the lazy update refers to. The one requirement is
        that each update shall be applied the same to every element in a range.
        A common update is the add a diff value to every element in the range.

        Inspired by the lazy segment tree solution to Problem 2569
        """
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)  # for lazy propogation
        self.N = N

        def init_tree(self, idx: int, ss: int, se: int) -> int:
            """Might not be necessary.
            """
            if ss > se:
                return 0
            if ss == se:
                self.tree[idx] = ??
            else:
                mid = (ss + se) // 2
                self.tree[idx] = self.init_tree(2 * idx + 1, ss, mid) + self.init_tree(2 * idx + 2, mid + 1, se)
            return self.tree[idx]


        def update(self, idx: int, ss: int, se: int, us: int, ue: int, diff??) -> None:
            if self.lazy[idx]:
                # problem-specific update requirement, might need to use
                # self.lazy[idx], might not
                self.tree[idx] = ??
                # propagate to children
                self.lazy[2 * idx + 1] = ??
                self.lazy[2 * idx + 2] = ??
                self.lazy[idx] = 0  # reset the flag

            if ss > se or us > se or ue < ss:
                return

            if ss >= us and se <= ue:
                # apply whatever update to the current self.tree node, and then
                # propagate
                self.tree[idx] = ??
                self.lazy[2 * idx + 1] = ??
                self.lazy[2 * idx + 2] = ??
            else:
                mid = (ss + se) // 2
                self.update(2 * idx + 1, ss, mid, us, ue, diff??)
                self.update(2 * idx + 2, mid + 1, se, us, ue, diff??)
                self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]


        def query(self, idx: int, ss: int, se: int, qs: int, qe: int) -> int:
            if self.lazy[idx]:
                # update the node if there is a self.lazy update waiting
                self.tree[idx] = ??
                # propagate the update to children
                self.lazy[2 * idx + 1] = ??
                self.lazy[2 * idx + 2] = ??
                self.lazy[idx] = 0  # reset self.lazy flag

            if ss > se or qs > se or qe < ss:
                return 0

            if ss >= qs and se <= qe:
                return self.tree[idx]
            mid = (ss + se) // 2
            return self.query(2 * idx + 1, ss, mid, qs, qe) + self.query(2 * idx + 2, mid + 1, se, qs, qe)

