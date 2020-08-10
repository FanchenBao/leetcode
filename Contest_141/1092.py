#! /usr/bin/env python3
from time import time
from copy import deepcopy

beg = time()

"""
    Date: 06/22/2019

    It was not a difficult one, but I got stuck early on. The intuition was to first identify the LCS between the two given strings. The result string must contain this LCS to be shortest. Then, we simply fill in the gaps of LCS by all the chars that are not matched.
"""


class Solution:
    def LCS(self, str1, str2):
        """ identify the LCS of str1 and str2. This function actually finds the string itself, not the length """
        len1 = len(str1)
        len2 = len(str2)
        matrix = [[""] * (len1 + 1) for i in range(len2 + 1)]
        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                if str1[j - 1] == str2[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + str1[j - 1]
                else:
                    matrix[i][j] = (
                        matrix[i - 1][j]
                        if len(matrix[i - 1][j]) >= len(matrix[i][j - 1])
                        else matrix[i][j - 1]
                    )
        return matrix[len2][len1]

    def shortestCommonSupersequence(self, str1, str2):
        lcs = self.LCS(str1, str2)
        res = ""
        i = 0
        j = 0
        for (
            l
        ) in (
            lcs
        ):  # insert all letters from str1 and str2 that are not matched, along with the matched ones
            while str1[i] != l:
                res += str1[i]
                i += 1
            while str2[j] != l:
                res += str2[j]
                j += 1
            res += l
            i += 1
            j += 1
        res += str1[i:] + str2[j:]
        return res

    def TimeLimitExceeded(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        matrix = [[0] * (len1 + 1) for i in range(len2 + 1)]
        for j in range(1, len1 + 1):
            matrix[0][j] = [
                (str1[:j], j - 1, -1)
            ]  # format: supersequence, str1 end match pos, str2 end match pos
        for i in range(1, len2 + 1):
            matrix[i][0] = [(str2[:i], -1, i - 1)]

        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                # let str2 be base, add one letter from str1
                temp1 = set()
                currChar = str1[j - 1]
                for ele in matrix[i][j - 1]:
                    str1LastMatchPos = ele[1]
                    try:
                        currPos = ele[0][str1LastMatchPos + 1 :].index(
                            currChar
                        )
                    except Exception:
                        currPos = -1
                    if currPos >= 0:  # currChar already exists in ele[0]
                        temp1.add(
                            (ele[0], str1LastMatchPos + 1 + currPos, ele[2])
                        )
                    else:
                        strList = list(ele[0])
                        for p in range(str1LastMatchPos + 1, len(strList) + 1):
                            tempList = deepcopy(strList)
                            tempList.insert(p, currChar)
                            if p <= ele[2]:
                                temp1.add(("".join(tempList), p, ele[2] + 1))
                            else:
                                temp1.add(("".join(tempList), p, ele[2]))
                # let str1 be base, add one letter from str2
                temp2 = set()
                currChar = str2[i - 1]
                for ele in matrix[i - 1][j]:
                    str2LastMatchPos = ele[2]
                    try:
                        currPos = ele[0][str2LastMatchPos + 1 :].index(
                            currChar
                        )
                    except Exception:
                        currPos = -1
                    if currPos >= 0:  # currChar already exists in ele[0]
                        temp2.add(
                            (ele[0], ele[1], str2LastMatchPos + 1 + currPos)
                        )
                    else:
                        strList = list(ele[0])
                        for p in range(str2LastMatchPos + 1, len(strList) + 1):
                            tempList = deepcopy(strList)
                            tempList.insert(p, currChar)
                            if p <= ele[1]:
                                temp2.add(("".join(tempList), ele[1] + 1, p))
                            else:
                                temp2.add(("".join(tempList), ele[1], p))
                temp = list(temp1.union(temp2))
                temp.sort(key=lambda x: len(x[0]))
                minLen = len(temp[0][0])
                matrix[i][j] = [t for t in temp if len(t[0]) == minLen]

        # for row in matrix:
        #     print(row)
        return matrix[len2][len1][0][0]


sol = Solution()
print("res:", sol.shortestCommonSupersequence("abac", "cab"))


print("\nTime: {}".format(time() - beg))
