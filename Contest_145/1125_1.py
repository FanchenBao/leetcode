from typing import List

"""
07/14/2019

The following is a depth-first search method. It anchors on a certain person,
then recursively call the helper function on the rest of the people to
satisfy the remaining skills. The helper function returns the indices of the
least number of people that can satisfy the skills.

The original version timed out. Thus I included memoization, and it passed OJ
with terrible performance (2068 ms, 6.38%).

Since memoization is used, it is very likely that this solution can be optimized
with DP. But possibly, there exists a better solution.

Update: 07/15/2019
I used bitmasking for creating keys for memo. This resulted in 1968 ms runtime.

I used optimzation method from here () to remove people whose skill set is a
subset of someone else's. This can reduce the total number of recursion calls.
Runtime now becomes 524 ms.
"""


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        req = set(req_skills)
        peo = [set(p) for p in people]
        # optimization: remove people who have skills subset of anyone else
        for i, p_i in enumerate(peo):
            for j, p_j in enumerate(peo):
                if i != j and p_i >= p_j:
                    peo[j] = set()
        # note the position of each skill for bitmasking purpose
        skills_index = {v: i for i, v in enumerate(req_skills)}
        return self.helper(req, peo, 0, dict(), skills_index)

    def helper(self, req_skills, people, start, memo, skills_index):
        if not req_skills:  # req_skills have all been fulfilled
            return []
        bitmask_req_skills = 0
        for s in req_skills:
            bitmask_req_skills |= 1 << skills_index[s]  # create key for memo
        if bitmask_req_skills in memo:
            return memo[bitmask_req_skills]
        size = 60
        res = []
        found = False
        for i in range(start, len(people)):
            remain = req_skills - people[i]
            if remain == req_skills:  # current p does not match any skills
                continue
            team = self.helper(remain, people, start + 1, memo, skills_index)
            if len(team) + 1 <= size:
                found = True
                size = len(team) + 1
                res = team + [i]
                if size == 1:
                    break
        # return a list of size 60 to guarantee failed attempt
        memo[bitmask_req_skills] = res if found else [-1] * 60
        return memo[bitmask_req_skills]


sol = Solution()
# print(sol.smallestSufficientTeam(
#     ["a", "b", "c", "d", "e", "f"],
#     [["a", "b", "c"], ["a", "b", "d"], ["c", "e", "f"], ["d", "e"], ["e", "b"], ["f", "c"]]))
print(
    sol.smallestSufficientTeam(
        ["mwobudvo", "goczubcwnfze", "yspbsez", "pf", "ey", "hkq"],
        [
            [],
            ["mwobudvo"],
            ["hkq"],
            ["pf"],
            ["pf"],
            ["mwobudvo", "pf"],
            [],
            ["yspbsez"],
            [],
            ["hkq"],
            [],
            [],
            ["goczubcwnfze", "pf", "hkq"],
            ["goczubcwnfze"],
            ["hkq"],
            ["mwobudvo"],
            [],
            ["mwobudvo", "pf"],
            ["pf", "ey"],
            ["mwobudvo"],
            ["hkq"],
            [],
            ["pf"],
            ["mwobudvo", "yspbsez"],
            ["mwobudvo", "goczubcwnfze"],
            ["goczubcwnfze", "pf"],
            ["goczubcwnfze"],
            ["goczubcwnfze"],
            ["mwobudvo"],
            ["mwobudvo", "goczubcwnfze"],
            [],
            ["goczubcwnfze"],
            [],
            ["goczubcwnfze"],
            ["mwobudvo"],
            [],
            ["hkq"],
            ["yspbsez"],
            ["mwobudvo"],
            ["goczubcwnfze", "ey"],
        ],
    )
)
