# from pudb import set_trace; set_trace()
from typing import List
from itertools import zip_longest


class Solution1:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """LeetCode 953

        The idea is to check the letter at each position for all the words in
        a sliding window manner. We check every consecutive pair of words. If
        the letters are the same, we record the words' indices for a further
        check in the next iteration. If the letters do not follow the order, we
        can return false immediately. If the letters do follow the order, we
        ignore them and move to the next pair. Finally, if the first word is
        longer than the second word, we return False.

        This way, after one iteration, we will only have the words that share
        the same letter left for further comparison. We end the comparison when
        there is no words to compare in the next iteration.

        O(MN), where M is the average length of the word, and N is the number of
        words. 36 ms, 61% ranking.
        """
        order_map = {le: i for i, le in enumerate(order)}
        N, i = len(words), 0  # i is the index of the letter in each word
        # a list of word indices that we will check in each iteration
        indices = list(range(N))
        while indices:
            # store the word indices that we will check in the next iteration
            temp = []
            for k in range(len(indices) - 1):
                # The words to be checked
                w1, w2 = words[indices[k]], words[indices[k + 1]]
                if i < len(w1) and i < len(w2):
                    if w1[i] == w2[i]:  # same letter
                        if not temp or temp[-1] != indices[k]:
                            # w1[i] not seen before, push both word indices
                            temp.extend([indices[k], indices[k + 1]])
                        elif temp and temp[-1] == indices[k]:
                            # w1[i] already seen, only push the second word index
                            temp.append(indices[k + 1])
                    elif order_map[w1[i]] > order_map[w2[i]]:
                        return False
                elif i < len(w1) and i == len(w2):  # w1 is longer than w2
                    return False
            indices = temp
            i += 1
        return True


class Solution2:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """This solution is inspired by the official solution. Apparently our
        Solution1 is unnecessarily complicated. We simply have to to pair wise
        comparison on all consecutive pairs. words is sorted if and only if all
        such pairs follow the order. Therefore, we don't have to check the
        letter at each position for all words. Instead, we check all the letters
        for each word pair.

        We also use zip and zip_longest to make the code cleaner.
        """
        order_map = {le: i for i, le in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            for l1, l2 in zip_longest(w1, w2):
                if l2 is None:
                    return False
                if l1 is None:
                    break
                if order_map[l1] > order_map[l2]:
                    return False
                elif order_map[l1] < order_map[l2]:
                    break
        return True


class Solution3:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """Smart solution from lee215.

        https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185/JavaC%2B%2BPython-Mapping-to-Normal-Order

        We swap the word with their respective numeric order.
        """
        order_map = {le: i for i, le in enumerate(order)}
        new_words = [[order_map[le] for le in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(new_words, new_words[1:]))


sol = Solution3()
tests = [
    (['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz', True),
    (['leetcode', 'hello'], 'hlabcdefgijkmnopqrstuvwxyz', False),
    (['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz', False),
    (['world', 'word', 'row'], 'worldabcefghijkmnpqstuvxyz', True),
    (['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz', False),
    (['app', 'apple'], 'abcdefghijklmnopqrstuvwxyz', True),
]

for i, (words, order, ans) in enumerate(tests):
    res = sol.isAlienSorted(words, order)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
