# from pudb import set_trace; set_trace()
# from typing import List


class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip(' ').split(' ')[-1])


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        count = 0
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        return count
