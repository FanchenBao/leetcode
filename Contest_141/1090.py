from typing import List


class Solution:
    def largestValsFromLabels(
        self,
        values: List[int],
        labels: List[int],
        num_wanted: int,
        use_limit: int,
    ) -> int:
        length = len(values)
        vala = []
        for i in range(length):
            vala.append((values[i], labels[i]))
        vala.sort(key=lambda x: x[0], reverse=True)

        labelUse = dict()
        for l in set(labels):
            labelUse[l] = 0

        res = 0
        for item in vala:
            if labelUse[item[1]] + 1 <= use_limit:
                labelUse[item[1]] += 1
                res += item[0]
                num_wanted -= 1
                if num_wanted == 0:
                    break
        return res
