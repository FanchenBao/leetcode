# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def fizzBuzz(self, n: int) -> List[str]:
        """Naive approach."""
        return ['FizzBuzz' if not i % 15 else 'Fizz' if not i % 3 else 'Buzz' if not i % 5 else str(i) for i in range(1, n + 1)]


class Solution2:
    def fizzBuzz(self, n: int) -> List[str]:
        """use a hashmap"""
        hashmap = {3: 'Fizz', 5: 'Buzz'}
        res = []
        for i in range(1, n + 1):
            cur_str = ''
            for k, v in hashmap.items():
                if i % k == 0:
                    cur_str += v
            res.append(cur_str if cur_str else str(i))
        return res


sol = Solution2()
print(sol.fizzBuzz(15))