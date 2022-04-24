# from pudb import set_trace; set_trace()
from typing import List
from random import choice
import string


class Codec:
    def __init__(self):
        """LeetCode 535

        For each longUrl, generate a random string of any size. To avoid too
        many collisions, we set the random string to have size of 16

        50 ms, faster than 40.69%

        UPDATE: My idea is the same as Mr. Pochmann, but he pointed out that
        using just one dict leads to the same longUrl getting hashed to
        different values if it is encoded more than once. Thus, we need another
        dict to keep track of the hash for each longUrl. Also, my calculation
        for the length of the tiny url is not correct. Since for each position
        in the tiny url, we have 26 * 2 + 10 = 36 different options. A size of
        six leads to 36^6 different ways. This is more than enough for the
        problem.

        83 ms, faster than 5.19%
        """
        self.long_to_short = {}
        self.short_to_long = {}
        self.bases = string.digits + string.ascii_letters

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.long_to_short:
            while True:
                h = ''.join(choice(self.bases) for _ in range(6))
                if h not in self.short_to_long:
                    self.short_to_long[h] = longUrl
                    self.long_to_short[longUrl] = h
                    break
        return self.long_to_short[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_to_long[shortUrl]

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
