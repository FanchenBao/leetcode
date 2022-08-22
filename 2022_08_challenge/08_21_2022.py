# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """LeetCode 936

        This was the daily challenge back in 03/31/2021, which I couldn't solve
        after four hours.

        More than a year later, this is still an extremely difficult problem
        for me, but I was able to crack it after two hours of efforts (with
        the confirmation from the official solution that the idea of going
        backwards is correct). So there has been some progress.

        It is not difficult to see that the problem should be tackled backwards.
        The question is: how do we handle the logic? The solution below uses
        the concept of BFS to collect unprocessed strings after each scan.
        The benefit is that we only have to deal with one unprocessed string at
        a time, greatly simplifying the logic.

        Step 1: initial scan to obtain the left indices of full match of stamp
        in target. If no full match is available, it is not possible to stamp
        the target. Also, each time a full match is found, the substring to
        the left of the full match up till the right of the previous full match
        or beginning of target is the unprocessed substring. We put this
        unprocessed substring in a queue.

        Step 2: obtain the prefix and suffix sets of stamp. The reason for doing
        this is that when we handle the unprocessed substring, if its length
        is longer than stamp or if it is not a substring of stamp, the only
        way to stamp it is to match it to the prefix of stamp on the right-hand
        side, and suffix on the left-hand side. Using prefix and suffix sets
        of stamp makes such matching faster.

        Step 3: process each unprocessed string. There are two situations
            * unprocessed string is a substring of stamp. We can stamp once to
            cover it entirely. We just need to find one way to match the
            unprocessed string to the stamp, and we are done. The criteria for
            matching is that the stamp stays within the boundary of target.
            This means the first match might not be the correct one. We need to
            keep trying until a correct matching is found.
            * unprocessed string is not a substring of stamp. The only way to
            stamp it is via prefix and suffix matching. prefix matching happens
            on the right side of the unprocessed string. Hence, if the unprocessed
            string is the natural end of target, it cannot handle prefix matching.
            Similarly, suffix matching happens on the left side, and if the
            unprocessed string is the natural start of target, it cannot handle
            suffix matching.

            During prefix matching, we go from the end of the unprocessed string
            to the front, match each substring to the prefix set and keep track
            of the longest match. This is greedy. It works because if we don't
            take the longest match, we always have to do more matches to get
            the longest match. Might as well do the longest match to begin with.

            During suffix matching, we go from the front of the unprocessed
            string to the end, match each substring to the suffix set and keep
            track of the longest match. The rationale is the same as prefix
            matching.

            Prefix matching gives us the index of the longest prefix match. It
            is saved in a variable called `right` (because it denotes the
            right side of the unprocessed substring that can be matched by
            stamp). Similarly, suffix matching gives us `left`, which is the
            index on the left of the unprocessed substring that makes the
            longest suffix matching substring.

            After processing prefix and suffix matching, we obtain `left` and
            `right`, which supposedly denotes the boundaries of the inner substr
            that has not been processed. if this inner substr is of the same
            length as the original string, we can't do any matching. Return []
            Otherwise, we push the new unprocessed string to queue.
        Step 4: continue the BFS until all unprocessed substrings is taken care
        of. We have the answer when BFS ends.

        65 ms, faster than 98.51% 
        """
        if target[0] != stamp[0] or target[-1] != stamp[-1]:
            return []
        res, queue = [], []
        N, M = len(target), len(stamp)
        # initial scan
        left = idx = 0
        while True:
            idx = target.find(stamp, idx)
            if idx == -1:
                break
            queue.append((target[left:idx], left, idx - 1))  # unprocessed substr
            res.append(idx)
            idx += M
            left = idx
        queue.append((target[left:], left, N - 1))  # last unprocessed substr
        if not res:
            return []
        # obtain suffix and prefix sets
        suffix_set = set(stamp[i:] for i in range(M - 1, -1, -1))
        prefix_set = set(stamp[:i + 1] for i in range(M))
        # handle the unprocessed substrings, until there is none left
        while queue:
            tmp = []
            for s, l, r in queue:
                if not s:
                    continue
                # Unprocessed string is a substring of stamp
                if len(s) < M and s in stamp:
                    left = len(s)
                    idx = -1
                    while True:
                        idx = stamp.find(s, idx + 1)
                        if idx == -1:
                            break
                        if l - idx >= 0 and M - 1 - idx + l < N:
                            # as long as one matching fits the stamp in target,
                            # we are done
                            res.append(l - idx)
                            break
                    if idx >= 0:  # s already handled, move on to next in queue
                        continue
                # Right side of s, prefix matching
                right = len(s)
                if r != N - 1:
                    for i in range(len(s) - 1, -1, -1):
                        if len(s) - i > M:
                            break
                        if s[i:] in prefix_set:
                            right = i
                    if right != len(s):
                        res.append(l + right)
                # Left side of s, suffix matching
                left = -1
                if l != 0:
                    for i in range(len(s)):
                        if i + 1 > M:
                            break
                        if s[:i + 1] in suffix_set:
                            left = i
                    if left >= 0:
                        res.append(l + left + 1 - M)
                # no match on either side
                if right - (left + 1) == len(s):
                    return []
                # some inner string still unprocessed, add to the queue
                if left + 1 <= right - 1:
                    tmp.append((target[l + left + 1:l + right], l + left + 1, l + right - 1))
            queue = tmp
        return res[::-1]


class Solution2:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """This is from the solution a year ago, but with my current touch to
        optimize it.
        """
        if target[0] != stamp[0] or target[-1] != stamp[-1]:
            return []
        N, M = len(target), len(stamp)
        tgt = list(target)
        res = []
        # first scan, perform all suffix matching
        for i in range(N - M + 1):
            for j in range(M):
                if tgt[i + j] != stamp[j] and tgt[i + j] != '?':
                    break
            else:
                for j in range(M):
                    tgt[i + j] = '?'
                res.append(i)
        # All suffix matching is done; end of target should've been matched
        if tgt[-1] != '?':
            return []
        # second scan, perform all prefix matching, greedily
        i = N - 1
        while True:
            while i >= 0 and tgt[i] == '?':
                i -= 1
            if i < 0:
                break
            left = i + 1
            for j in range(max(0, i + 2 - M), i + 1):
                for k in range(M):
                    if tgt[j + k] != stamp[k] and tgt[j + k] != '?':
                        break
                else:
                    for k in range(M):
                        if tgt[j + k] != '?':
                            tgt[j + k] = '?'
                        else:  # the remaining must all be '?' already
                            break
                    res.append(j)
                    i = j - 1
                    break  # greedy. We only want the longest prefix match
            else:
                return []
        return res[::-1]


sol = Solution2()
tests = [
    # ("abc", "ababc", [0, 2]),
    # ("abca", "aabcaca", [3, 0, 1]),
    # ('h', 'hhhhh', [4,3,2,1,0]),
    # ("oz", "ooozz", [0,3,1,2]),
    # ("cab", "cabbb", [2, 1, 0]),
    # ("by", "bbybyybyby", [4, 0, 8, 6, 3, 1]),
    # ("zbs", "zbzbsbszbssbzbszbsss", [17,10,16,8,4,0,15,12,7,2]),
    # ("ffebb", "fffeffebbb", [0,5,1,4]),
    ("zjmhy", "zmjzjzjmhy", []),
]

for i, (stamp, target, ans) in enumerate(tests):
    res = sol.movesToStamp(stamp, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
