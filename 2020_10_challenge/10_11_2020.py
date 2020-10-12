# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        """90% ranking
        I did took a hint "stack" for this question, but didn't realize how
        stack could be used until the last moment.

        The intuition is that for each new letter for the res, we have to add
        it. Yet, before adding it, we need to check whether the letters already
        added to the res make it the best fit for the new letter. They way to
        check it is to find the already existing letters that are bigger than
        the new letter. If these bigger existing letters will appear again
        after the new letter, then res will be smaller if we do not include
        these bigger existing letters now and incorporating them later.

        For the actual implementation, there is a trick that we cannot search
        through the entire res from front to end to look for bigger existing
        letters to eliminate. This is because it is guaranteed that for each
        letter in res, the sequence from the front to the letter is the best
        fit. So if we want to eliminate bigger existing letters while also
        maintaining the property that the result after elimination is also the
        best fit, we have to make sure the eliminated letters are right in
        front of the new letter. If there is a gap between the eliminated
        letters and the new letter, then the gap does not represent the optimal
        fit. Hence, we use a stack to track to pop the end letters in res to
        make sure that there is no gap between all eliminated letters and the
        new letter.
        """
        counter = Counter(s)
        res = []
        for le in s:
            if le not in res:
                while res and counter[res[-1]] and res[-1] > le:
                    res.pop()
                res.append(le)
            counter[le] -= 1
        return ''.join(res)


class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        """Greedy approach.

        The idea of this approach is that the final answer must start with one
        of the smalest latters in s. So we create a list of unique letters in
        s in ascending order, and try one by one as our starting letter. Say
        we pick the smallest letter as the starting one and we choose the first
        appearance of such letter (this is the greedy part). That means we must
        discard all the letters ahead of it. And since we already pick the
        letter, we also need to eliminate the leeter in all the letters after
        it. Now that our first letter is secured, we subject the remaining
        letters through the same search process. This continues until we have
        an answer.
        """
        for le in sorted(set(s)):
            next_s = s[s.index(le):]
            if set(next_s) == set(s):
                return le + self.removeDuplicateLetters(next_s.replace(le, ''))
        return ''


sol = Solution2()
tests = [
    ('bcabc', 'abc'),
    ('cbacdcbc', 'acdb'),
    ('cba', 'cba'),
    ('wlkdw', 'lkdw'),
    ('qweeqrqrq', 'qwer'),
    ('eiorgorio', 'egori'),
    ('defwkfonfjfweon', 'defkjwon'),
    ("bbcaac", 'bac'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.removeDuplicateLetters(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
