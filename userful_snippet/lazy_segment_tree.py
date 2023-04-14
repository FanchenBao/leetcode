class LazySegTree:
    def __init__(self, N:int) -> None:
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

        def init_tree(idx: int, ss: int, se: int) -> int:
            """Might not be necessary.
            """
            if ss > se:
                return 0
            if ss == se:
                tree[idx] = ??
            else:
                mid = (ss + se) // 2
                tree[idx] = init_tree(2 * idx + 1, ss, mid) + init_tree(2 * idx + 2, mid + 1, se)
            return tree[idx]


        def update(idx: int, ss: int, se: int, us: int, ue: int, diff??) -> None:
            if lazy[idx]:
                # problem-specific update requirement, might need to use
                # lazy[idx], might not
                tree[idx] = ??
                # propagate to children
                lazy[2 * idx + 1] = ??
                lazy[2 * idx + 2] = ??
                lazy[idx] = 0  # reset the flag

            if ss > se or us > se or ue < ss:
                return

            if ss >= us and se <= ue:
                # apply whatever update to the current tree node, and then
                # propagate
                tree[idx] = ??
                lazy[2 * idx + 1] = ??
                lazy[2 * idx + 2] = ??
            else:
                mid = (ss + se) // 2
                update(2 * idx + 1, ss, mid, us, ue, diff??)
                update(2 * idx + 2, mid + 1, se, us, ue, diff??)
                tree[idx] = tree[2 * idx + 1] + tree[2 * idx + 2]


        def query(idx: int, ss: int, se: int, qs: int, qe: int) -> int:
            if lazy[idx]:
                # update the node if there is a lazy update waiting
                tree[idx] = ??
                # propagate the update to children
                lazy[2 * idx + 1] = ??
                lazy[2 * idx + 2] = ??
                lazy[idx] = 0  # reset lazy flag

            if ss > se or us > se or ue < ss:
                return 0

            if ss >= us and se <= ue:
                return tree[idx]
            mid = (ss + se) // 2
            return query(2 * idx + 1, ss, mid, us, ue) + query(2 * idx + 2, mid + 1, se, us, ue)

