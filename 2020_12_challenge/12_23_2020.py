# from pudb import set_trace; set_trace()
from typing import List
from itertools import permutations
from random import randint



class Solution0:
    def nextGreaterElement(self, n: int) -> int:
        """For testing purpose only. This is the ground truth but with
        terrible run time.
        """
        upper_limit = 2**31 - 1
        for pot_lst in sorted(permutations(str(n))):
            pot = int(''.join(pot_lst))
            if pot > n and pot < upper_limit:
                return pot
        return -1


class Solution1:
    def nextGreaterElement(self, n: int) -> int:
        """Search from the end backwards. Each time a digit is encountered,
        check whether the remaining pool of digits have any that is bigger
        than the current digit. If there is, pick the smallest bigger digit to
        replace the currend digit. Then, we rearrange the remaining digits to
        form the smallest number. Finally, we combine the first half (the
        start until the replaced digit) and the second half (the rearranged
        smallest number) to form the result.
        

        O(N), 28 ms, 74% ranking.
        """
        counter = [0] * 10
        new_num = list(str(n))
        res = -1
        for i in range(len(new_num) - 1, -1, -1):
            cur_d = int(new_num[i])
            counter[cur_d] += 1
            # check whether there exists a digit bigger than cur_d
            for alt_d in range(cur_d + 1, 10):
                if counter[alt_d]:  # if exists, our search is done
                    new_num[i] = str(alt_d)
                    counter[alt_d] -= 1
                    break
            else:  # no bigger digit found
                continue
            f_half = ''.join(new_num[:i + 1])
            s_half = ''.join(str(d) * counter[d] for d in range(10))
            res = int(f_half + s_half)
            break
        return -1 if res > 2**31 - 1 else res  # don't forget to check limit


class Solution2:
    def nextGreaterElement(self, n: int) -> int:
        """Same idea but without the use of a counter.

        The smart part is that we don't need to track anything. To have a
        chance of generating the next greater element, the number must have a
        peak in digiit value going from the end to the front. If there is no
        peak, i.e. the digits are sorted in descent order, we do not have a
        valid result. To identify a peak, we only need to check adjacent digits
        Once a peak is identified, we need to find the smallest digits on the
        second half that is bigger than the current digit. Since we know that
        the second half must be sorted in descending order, we only need to
        traverse the second half bottom up and stop at the first digit that is
        bigger than the current one.

        The rest is the same.

        O(N), 24 ms, 91% ranking. It is faster because we don't have to create
        an extra counter array.
        """
        new_num = list(str(n))
        res = -1
        for i in range(len(new_num) - 2, -1, -1):
            if int(new_num[i]) < int(new_num[i + 1]):
                for j in range(len(new_num) - 1, i, -1):
                    if int(new_num[j]) > int(new_num[i]):
                        # swap the smallest bigger dig with the current dig
                        new_num[i], new_num[j] = new_num[j], new_num[i]
                        f_half = ''.join(new_num[:i + 1])
                        s_half = ''.join(sorted(new_num[i + 1:]))
                        res = int(f_half + s_half)
                        break
                break
        return -1 if res > 2**31 - 1 else res  # don't forget to check limit


sol0 = Solution0()
sol = Solution2()
# tests = [
#     (12, 21),
#     (21, -1),
#     (4595, 4955),
    # (739354885, 739355488),
#     (1999999999, -1),
#     (1, -1),
#     (100, -1),
# ]

tests = [randint(1, 2**10 - 1) for _ in range(100)]


# for i, (n, ans) in enumerate(tests):
#     res = sol.nextGreaterElement(n)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')

for i, n in enumerate(tests):
    ans = sol0.nextGreaterElement(n)
    res = sol.nextGreaterElement(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, n: {n}')
