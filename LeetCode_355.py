# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        """Each userId has a dict with two fields: 'tweets' and 'followees'.
        
        'tweets' record the tweets made by the user in chronological order. Each
        tweet pushed in contains a global timing tick, the tweet ID and the user
        ID.

        'followees' is a set that records the user ID that the current user
        follows.

        With this set up, postTweet(), follow(), and unfollow() are trivial (
        however, I was bitten by unfollow, where the test case allows calling
        unfollow when a user has not followed anyone).

        The difficult part is getNewsFeed. I used the technique for merging
        sorted list. Each followee plus the user himself form a list of sorted
        list of tweets. Since each tweet contains a timing tick, we can use
        heap to obtain the tweet with the latest timing tick. And then push into
        the heap the next tweet belonging to the user whose tweet has just been
        popped. We keep doing this, eliminating users whose tweets have been
        exhausted, until either no user is left or we have obtained the 10
        tweets.

        getNewsFeed runs in O(N + logN). 29 ms, 62% ranking.
        """
        self.data = defaultdict(
            lambda: {
                'tweets': [],
                'followees': set(),
            },
        )
        self.tick = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.data[userId]['tweets'].append((self.tick, tweetId, userId))
        self.tick -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        id_idx = {}
        for id_ in list(self.data[userId]['followees']) + [userId]:
            if self.data[id_]['tweets']:
                id_idx[id_] = len(self.data[id_]['tweets']) - 1
        
        res, heap = [], []
        for id_, idx in id_idx.items():
            heapq.heappush(heap, self.data[id_]['tweets'][idx])
        while id_idx and len(res) < 10:
            _, tid, uid = heapq.heappop(heap)
            res.append(tid)
            id_idx[uid] -= 1
            if id_idx[uid] >= 0:
                heapq.heappush(heap, self.data[uid]['tweets'][id_idx[uid]])
        return res        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.data[followerId]['followees'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.data[followerId]['followees']:
            self.data[followerId]['followees'].remove(followeeId)
        




# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
