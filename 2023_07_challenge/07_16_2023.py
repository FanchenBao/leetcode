# from pudb import set_trace; set_trace()
from typing import List, Set
import math
from collections import defaultdict


class Solution1:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """TLE
        """
        self.res = [0] * 61
        N = len(people)
        skill_indices = {s: i for i, s in enumerate(req_skills)}
        people_skill_states = []
        for skills in people:
            people_skill_states.append(0)
            for s in skills:
                people_skill_states[-1] |= (1 << skill_indices[s])
        fulfilled_state = (1 << len(req_skills)) - 1
        
        def backtrack(idx: int, skills_state: int, team: List[int]) -> None:
            if skills_state == fulfilled_state:
                if len(team) < len(self.res):
                    self.res = team[:]
                return
            if idx == N:
                return
            # do not pick people[idx]
            backtrack(idx + 1, skills_state, team)
            # pick people[idx]
            team.append(idx)
            new_state = skills_state | people_skill_states[idx]
            if new_state != skills_state:
                backtrack(idx + 1, new_state, team)
            team.pop()

        backtrack(0, 0, [])
        return self.res


class Solution2:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """LeetCode 1125

        After many many efforts, it worked!

        The initial idea of backtracking was correct, but it was too slow
        because we were repeating the same state that did not make any
        improvement to the final solution.

        In this solution, which is very similar to the one from yesterday, we
        use a dp-based backtrack.

        dp(idx, skill_state) records the smallest team that includes idx to
        achieve skill_state.

        In backtracking, when we have the idx and current_state, we check the
        dp. If dp(idx, current_state) already exists and the team is not bigger
        than the current one, there is no point of continuing, because we have
        already found a good team and moved on with it. There is no need to
        replace the previous team with the current one.

        We only make replacement if the current one has a smaller team. That is
        the rule of DP, which allows a three-state backtracking function to
        actually only have two states. This is similar to the solution from
        yesterday.

        In addition, we apply pre-computation on all the skills of each person
        to speed up the backtracking process.

        1020 ms, faster than 20.89%
        """
        dp = {}
        N = len(people)
        skill_indices = {s: i for i, s in enumerate(req_skills)}
        people_skill_states = []
        for skills in people:
            people_skill_states.append(0)
            for s in skills:
                people_skill_states[-1] |= (1 << skill_indices[s])
        
        def backtrack(idx: int, skills_state: int, team: List[int]) -> None:
            if idx == N:
                return
            # skip idx
            backtrack(idx + 1, skills_state, team)
            new_state = skills_state | people_skill_states[idx]
            if new_state == skills_state:  # idx does not contribute
                return
            if (idx, new_state) in dp and len(dp[(idx, new_state)]) <= len(team) + 1:
                return
            team.append(idx)
            dp[(idx, new_state)] = team[:]
            backtrack(idx + 1, new_state, team)
            team.pop()


        backtrack(0, 0, [])
        res = [0] * N
        fulfilled_state = (1 << len(req_skills)) - 1
        for i in range(N):
            team = dp.get((i, fulfilled_state), None)
            if team and len(team) < len(res):
                res = team
        return res


class Solution3:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """Inspired by previous solution from four years ago. It's similar to
        solution2, in which we are finding the smallest team ending at idx that
        can form a specific skill_state. However, instead of using backtracking,
        we go through all the states.

        O(MN), N = len(people), M = 2**(len(req_skills)), 155 ms, faster than 69.62%
        """
        dp = {}
        dp[0] = []
        skill_indices = {s: i for i, s in enumerate(req_skills)}
        for i, skills in enumerate(people):
            skill_state = 0
            for s in skills:
                skill_state |= (1 << skill_indices[s])
            for pre_state in list(dp.keys()):
                new_state = pre_state | skill_state
                if new_state == pre_state:
                    continue
                if new_state not in dp or len(dp[new_state]) > len(dp[pre_state]) + 1:
                    dp[new_state] = dp[pre_state] + [i]
        return dp[(1 << len(req_skills)) - 1]



sol = Solution3()
tests = [
    (["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]], [0, 2]),
    (["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]], [1,2]),
]

for i, (req_skills, people, ans) in enumerate(tests):
    res = sol.smallestSufficientTeam(req_skills, people)
    if len(res) == len(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
