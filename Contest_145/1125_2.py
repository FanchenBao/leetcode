from typing import List, Dict

"""
07/15/2019

This solution is BRILLIANT (from https://leetcode.com/problems/smallest-sufficient-team/discuss/334572/Python-DP-Solution).

I heavily relied on the algorithm posted on that discussion to write the
following version, because that algorithm was simply too beautiful. There are
two important take-home messages:

1. To save time and space, any combination of unique characters can be repre-
sented by bitmasking. e.g. For a skill set of {a,b,c,d,e}, the full skill set's
bitmasking would be 0x11111; a skill set of {a,b e} would be 0x11001. This way,
any skill set can be represented by a simple integer, thus hashable. On the
other hand, union of two skill sets is also simple: just use the bit OR operator.

2. This method basically creates all possible combinations of people starting
with team size = 1. Yet the brilliance is to use a dictionary to keep track of
all possible skill sets seen so far, such that we just need to add the new
person's skill to all the skill sets seen already to produce new skill set with
new team. Embedded in this implementation is also the observation that if any
addition of new team member leads to repetition of skill set already seen, then
we compare whether the new addition leads to smaller team size compared to the
team alreay seen. And we keep the smaller team.

All in all, this is an eye-opening great algorithm.
"""


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        # note the position of each skill for bitmasking purpose
        skills = {v: i for i, v in enumerate(req_skills)}
        # key is the skill set, value is the min list of people for the skills
        dp: Dict[int, List[int]] = {0: []}
        for i, p in enumerate(people):
            his_skill = 0  # find the bitmasking of the current person's skill
            for s in p:
                his_skill |= 1 << skills[s]
            for skill_set, team in list(dp.items()):
                # new skill set after contribution from the current person
                with_him = skill_set | his_skill
                if with_him == skill_set:  # no improvement
                    continue
                else:
                    if with_him not in dp or len(team) + 1 < len(dp[with_him]):
                        dp[with_him] = team + [i]
        bitmask_req_skills = (1 << len(req_skills)) - 1
        return dp[bitmask_req_skills]


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
