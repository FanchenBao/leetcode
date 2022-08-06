# from pudb import set_trace; set_trace()
from typing import List
from random import randint


class Solution0:
    def totalSteps(self, nums: List[int]) -> int:
        queue = nums
        res = 0
        while queue:
            temp = []
            for i, n in enumerate(queue):
                if i == 0 or n >= queue[i - 1]:
                    temp.append(n)
            if len(queue) == len(temp):
                break
            queue = temp
            res += 1
        return res


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        aux = [[0, 0]]  # ele = [index of previous peak larger than me, number of steps to remove me]
        N = len(nums)
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                break
            aux.append([i, 0])
        else:
            return 0
        aux.append([i - 1, 1])
        res = 1
        for j in range(i + 1, N):
            if nums[j] < nums[j - 1] < nums[j - 2]:
                aux.append(aux[-1])
            elif nums[j] < nums[j - 1] and nums[j - 1] >= nums[j - 2]:
                aux.append([j - 1, 1])
            elif nums[j] == nums[j - 1]:
                aux.append(aux[-1] if aux[-1][1] == 0 else [aux[-1][0], aux[-1][1] + 1])
            elif nums[j] > nums[j - 1]:
                pre_peak_idx = aux[-1][0]
                aux.append([-1, aux[-1][1] + 1])
                while nums[j] > nums[pre_peak_idx]:
                    aux[-1][1] = 0 if aux[pre_peak_idx][1] == 0 else (aux[pre_peak_idx][1] + 1)
                    if pre_peak_idx == aux[pre_peak_idx][0]:
                        aux[-1][0] = j
                        break
                    else:
                        pre_peak_idx = aux[pre_peak_idx][0]
                if aux[-1][0] < 0:  # not set yet
                    if nums[j] == nums[pre_peak_idx]:
                        if aux[pre_peak_idx][1] == 0:
                            aux[-1][0], aux[-1][1] = aux[pre_peak_idx]
                        else:
                            aux[-1][0], aux[-1][1] = aux[pre_peak_idx][0], aux[pre_peak_idx][1] + 1
                    else:
                        aux[-1][0] = pre_peak_idx
            # print(aux)
            res = max(res, aux[-1][1])
        return res


sol = Solution()
tests = [
    ([5,3,4,4,7,3,6,11,8,5,11], 3),
    ([4,5,7,7,13], 0),
    ([6, 10, 10, 2, 3], 2),
    ([7, 4, 1, 8, 10], 1),
    ([10, 5, 10, 9, 10], 1),
    ([9, 3, 10, 9, 2], 1),
    ([9, 1, 5, 10, 9], 2),
    ([1, 6, 8, 4, 9], 1),
    ([6, 1, 1, 10, 10], 2),
    ([4, 5, 2, 1, 7], 1),
    ([5, 1, 9, 3, 7], 2),
    ([6, 8, 5, 7, 1], 2),
    ([1, 4, 3, 3, 5, 10, 3, 6, 2, 1], 2),
    ([10, 9, 7, 2, 1, 2, 5, 6, 9, 8], 5),
    ([4, 1, 2, 6, 4, 1, 9, 3, 9, 1], 2),
    ([1, 1, 5, 10, 5, 8, 6, 2, 9, 7], 3),
    ([5, 10, 8, 2, 4, 6, 9, 7, 7, 7], 4),
    ([9, 2, 9, 7, 3, 3, 10, 2, 9, 9], 3),
    ([4, 9, 1, 5, 3, 2, 7, 6, 2, 6], 3),
    ([2, 9, 10, 6, 8, 3, 8, 9, 7, 10], 4),
    ([7, 8, 10, 4, 7, 8, 10, 2, 10, 6], 3),
    ([7, 7, 3, 5, 5, 7, 10, 5, 4, 8], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.totalSteps(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
