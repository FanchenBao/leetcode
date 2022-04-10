# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict, Counter


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        """The encrypt part is trivial.

        The decrypt part is triky because it might be very time consuming to
        generate all possible decrypts. However, since dictionary is finite
        with at most 100 * 100 runtime to check each letter in each word, I
        decided to check whether each word in dictionary fits the decrypts.
        The checking procedure follows a BFS scheme, where we go through each
        word in dictionary, check whether it has the same length as the decrypts
        and whether at the current position, the word's letter is contained in
        the decrypts. Any mismatch results in the word being discarded. We run
        this until either all words in dictionary are discarded or all
        positions in the decrypts are checked.

        This method passes. It's not too hard.

        init: O(26)
        encrypt: O(len(word1))
        decrypt: O(len(word2) + M), where M is the total number of letters (not
        words) in dictionary

        1096 ms, 28% ranking.
        """
        self.kv = {k: v for k, v in zip(keys, values)}
        self.vk = defaultdict(set)
        for k, v in zip(keys, values):
            self.vk[v].add(k)
        self.dictionary = dictionary

    def encrypt(self, word1: str) -> str:
        return ''.join(self.kv[w] for w in word1)

    def decrypt(self, word2: str) -> int:
        decrypts = [self.vk[word2[i:i + 2]] for i in range(0, len(word2), 2)]
        queue = self.dictionary
        i, k = 0, len(decrypts)
        while i < k and queue:
            temp = []
            for word in queue:
                if len(word) == k and word[i] in decrypts[i]:
                    temp.append(word)
            queue = temp
            i += 1
        return len(queue)


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        """Solution from lee215.

        https://leetcode.com/problems/encrypt-and-decrypt-strings/discuss/1909025/JavaC%2B%2BPython-Two-Hashmaps-with-Explanation

        Just encrypt all the words in dictionary, and find their frequencies.
        Thus, in decrypt, we check if word2 appears as one of the encrypts of
        the words in dictionary.

        Notice the trick in encrypt. Because there is no guarantee that all the
        words in dictionary are encryptable. Thus, if any word cannot be
        encrypted, we simply use a non-English symbol to represent a failed
        encryption. Since word1 is guaranteed to be encryptable, this trick
        won't affect encrypt, but it will make the non-encryptable words in
        dictionary standout.

        Then when we query word2, all the non-encryptable words in dictionary
        won't play a part.

        So good.

        280 ms, 82% ranking.
        """
        self.kv = {k: v for k, v in zip(keys, values)}
        self.counter = Counter(self.encrypt(word) for word in dictionary)

    def encrypt(self, word1: str) -> str:
        return ''.join(self.kv.get(w, '*') for w in word1)

    def decrypt(self, word2: str) -> int:
        return self.counter[word2]
        



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
