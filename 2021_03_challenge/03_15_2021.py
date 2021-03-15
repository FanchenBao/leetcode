# from pudb import set_trace; set_trace()
from typing import List
import random
import string


class Codec1:
    """I do not like this solution. It uses a separate dictionary to record the
    number of times any letter repeats itself consecutively. By doing so, we
    avoid writing the same letter repeatedly. During decoding, we check the
    dict to see whether any letter has more than one consecutive repeats. If it
    does, we expand the letter.

    I don't like this solution because it doesn't save any space. We basically
    use external memory to seemingly reduce the size of the input string, while
    in fact, nothing has shrunk.

    O(N), 44 ms, 14% ranking.
    """

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.shrink = {}
        res, i = '', 0
        while i < len(longUrl):
            c = 1
            while i + c < len(longUrl) and longUrl[i + c] == longUrl[i]:
                c += 1
            res += longUrl[i]
            if c > 1:
                self.shrink[len(res) - 1] = c
            i += c
        return res

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        res = ''
        for i in range(len(shortUrl)):
            res += shortUrl[i] * self.shrink.get(i, 1)        
        return res


class Codec2:
    """Apparently I have misunderstood the question and made it too complicated.
    I thought there exists a method to actually shrink a long string into a
    short string. But it turns out the converged method from most people uses
    additional dictionaries to save the mapping between the short and long URL.
    With such use of external dictionaries that directly performs hashing, the
    problem is actually trivial. We simply produce a random string of size 6
    (why size 6? because the example shows that the short url has the last part
    with size 6), and use that as the key for the long url. Then we simply store
    them as key-longurl pair. When decoding, we look for the key from the end
    of the short url, and obtain the long url from the dictionary.

    O(N), 36 ms, 52% ranking.
    """
    keys_longUrl = {}
    alphabet = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            key = ''.join(random.choices(self.alphabet, k=6))
            if key not in self.keys_longUrl:
                break
        self.keys_longUrl[key] = longUrl
        return 'http://tinyurl.com/' + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.keys_longUrl[shortUrl[-6:]]


sol = Codec2()
tests = [
    ('https://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com/bbbbbbbbbbbbbbbbbbbbbb/ccccccccccccccccccccccccccccccccccccccccccc', 'https://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com/bbbbbbbbbbbbbbbbbbbbbb/ccccccccccccccccccccccccccccccccccccccccccc'),
    ('https://leetcode.com/problems/design-tinyurl', 'https://leetcode.com/problems/design-tinyurl'),
    ('http://www.leetcode.com/faq/?id=10', 'http://www.leetcode.com/faq/?id=10')
]

for i, (longUrl, ans) in enumerate(tests):
    interm = sol.encode(longUrl)
    res = sol.decode(interm)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
