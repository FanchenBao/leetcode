# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len(set(''.join(morse[ord(le) - 97] for le in word) for word in words))


sol = Solution()
tests = [
    (["gin","zen","gig","msg"], 2),
    (["a"], 1),
]

for i, (words, ans) in enumerate(tests):
    res = sol.uniqueMorseRepresentations(words)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
