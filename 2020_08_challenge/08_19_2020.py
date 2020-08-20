# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def convert(self, word: str) -> str:
        return word + 'ma' if word[0] in {'a', 'e', 'i', 'o', 'u'} else word[1:] + word[0] + 'ma'

    def toGoatLatin(self, S: str) -> str:
        return ' '.join([self.convert(word) + 'a' * (i + 1) for i, word in enumerate(S.split(' '))])



sol = Solution()
print(sol.toGoatLatin('a b c d e f g h i j k l m n o p q r s t u v w x y z'))
