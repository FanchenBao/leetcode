# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """92% ranking
        I tried to find a mathematics solution, but things got a bit too
        complicated and I lost patience. The algorithmic solution fills the
        champagne row by row, until there is no more spillage to the next row.
        We index each row from 0, then any jth glass in this row will spill to
        the next row with index j and j + 1.
        """
        rows = [[poured]]
        for i in range(query_row + 1):
            cur_row = rows[i]
            next_row = [0] * (len(cur_row) + 1)
            spilled = False
            for j in range(len(cur_row)):
                if cur_row[j] > 1:
                    next_row[j] += (cur_row[j] - 1) / 2
                    next_row[j + 1] += (cur_row[j] - 1) / 2
                    cur_row[j] = 1
                    spilled = True
            if not spilled:
                break
            else:
                rows.append(next_row)
        return rows[query_row][query_glass] if len(rows) >= query_row + 1 else 0


class Solution2:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """Use the smart DP solution. Howver, this is slower because it goes
        through all the rows, whereas Solution1 has an early stoppage.
        """
        res = [poured] + [0] * query_row  # use this ONE list to do DP
        for i in range(1, query_row + 1):
            for j in range(i, -1, -1):
                res[j] = max(res[j] - 1, 0) / 2 + max(res[j - 1] - 1, 0) / 2
        return min(res[query_glass], 1)


sol = Solution2()
tests = [
    (1, 1, 1, 0.0),
    (2, 1, 1, 0.5),
    (100000009, 33, 17, 1.0),
]

for i, (poured, query_row, query_glass, ans) in enumerate(tests):
    res = sol.champagneTower(poured, query_row, query_glass)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
