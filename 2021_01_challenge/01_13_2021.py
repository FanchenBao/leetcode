# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """Been pondering over this problem for way too long. Then I saw that
        it was labeled as medium. How could it be? Then I checked the question
        again, and viola! There it is: "each boat carries at most 2 people at
        the same time". I thought there is no limit on the number of people a
        boat can carry. Well, with only 2 people per boat, this question can be
        resolved, as the solution pointed out, using Greedy. We sort the people
        array. For the heaviest person, if its value combined with the current
        min is larger than limit, it has to occupy its own boat. If the
        combined value is smaller or equal to limit, we have two choices.
        Either have the heavy person occupy its own boat, or have the two
        people occupy the boat. In the first scenario, we use one boat, and
        we need to find the best solution for the remaining n - 1 people. In
        the second solution, we use one boat but only need to find the best
        solution for the remaining n - 2 people. Note that the n - 2 people is
        included in the n - 1 people. This means for the n - 1 people, its
        solution cannot be better than the one for the n - 2 people; otherwise
        the n - 2 people would have the same solution as well. Therefore, by
        combining the min and max, of the sorted people array, we can find the
        optimal solution.


        O(N), 456 ms, 52% ranking.
        """
        people.sort()
        i, j = 0, len(people) - 1
        res = 0
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            res += 1
        return res + 1 if i == j else res

        


# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
