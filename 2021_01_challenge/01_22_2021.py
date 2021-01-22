# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, defaultdict


class Solution1:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """The key insight is that if word1 and word2 contain the same letters,
        and the same count for each letter, the two words can always be matched
        via swapping. Therefore, our task becomes examining whether we can match
        the letter counts between word1 and word2 using transformation.

        We arbitrarily select word1 as the reference and get a reference
        counter1. For word2, we get a reverse counter (rev_counter) which is a
        dict with number of counts as key and a list of letters that correspond
        to such count as value. We go through the count in rev_counter one by
        one. For each count `c`, we pop one of its letter and check the desired
        number of count for that letter in counter1. If `desired == c`, we are
        good here and can move on to the next letter in `rev_counter[c]`.
        Otherwise, we need to check whether in `rev_counter[desired]` exists. If
        the answer is yes, we can perform the transformation, which is to
        associate the new letter `rev_counter[desired].pop()` with `c`, and
        append it to `rev_counter[c]`. We continue this action until all letters
        in `rev_counter[c]` is exhausted. Then we move on to the next `c`.

        Anytime during the operation, if `rev_counter[desired]` does not exist,
        we return False. Otherwise, we return True at the end.

        O(N), 132 ms, 84% ranking.
        """
        if len(word1) != len(word2):  # easy checks:
            return False
        # preparation
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        rev_counter = defaultdict(list)
        for w, c in counter2.items():
            rev_counter[c].append(w)
        # use the same w and c from above to start the check
        for c in list(rev_counter.keys()):
            while True:
                while c in rev_counter:
                    w = rev_counter[c].pop()
                    if not rev_counter[c]:  # we have popped everything
                        del rev_counter[c]
                    desired = counter1.get(w, 0)  # desired count
                    if desired != c:
                        break
                else:  # rev_counter[c] has been exhausted. Move on to next c
                    break
                if desired in rev_counter:
                    w = rev_counter[desired].pop()
                    if not rev_counter[desired]:  # we have popped everything
                        del rev_counter[desired]
                    rev_counter[c].append(w)  # transform the count for w
                else:  # desired cannot be obtained in re_counter
                    return False
        return True


class Solution2:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """Time to shatter your confidence. Apparently, this is a one-liner
        problem.

        The idea is quite the same but with much better intuition. So what we
        need is still to check is two things:

        1. Whether the words contain the same letters.
        2. Whether the frequency of letters are the same.

        The first check is easy. We can do that by taking sets on both words.
        Once the first check passes, we need to check whether the frequency of
        letter counts match between the two words. If they match, operation 2
        (transform) can always rearrange the ownership of the frequency to align
        the two words (e.g. {a: 2, b: 1} => {a: 1, b: 2}) (or in other words
        swap the frequencies). Then operation 1 (swap) can always rearrange the
        letters in the actual words to make the match (or in other words, swap
        the letters).

        Frequency check can be done using Counter of Counter.

        O(N), 128 ms, 91% ranking.
        """
        c1 = Counter(word1)
        c2 = Counter(word2)
        # Use counter of counter to do frequency check
        # and counter.keys() for letter match check
        return Counter(c1.values()) == Counter(c2.values()) and c1.keys() == c2.keys()


sol = Solution2()
tests = [
    ('abc', 'bca', True),
    ('a', 'aa', False),
    ('cabbba', 'abbccc', True),
    ('cabbba', 'aabbss', False),
    ('abbccc', 'aabbcc', False),
]

for i, (word1, word2, ans) in enumerate(tests):
    res = sol.closeStrings(word1, word2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
