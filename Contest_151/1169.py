#! /usr/bin/env python3
from typing import List, Dict, Set
from collections import defaultdict

# from pprint import pprint as pp
"""08/26/2019

Solution1:
Felt pretty bad about this one. It's an easy enough problem, and I brute forced
it by first reorganizing the given data, and then do pair-wise comparison for
transactions happening in different cities belonging to the same person. If
such comparison finds that transactions happen within 60 minute, I report both
as invalid. Along the way, I also check for whether a transaction has more than
$1000 in cost. A lot of comparisons and the code seems spaghetti. Clocked in at
300 ms, 26%.

Solution2:
Much cleaner than Solution1. I sorted the original list first based on time,
then reorganize data based on name. Then the rest of the transaction info in
the same name is sorted from small to large on time. Then I do pair-wise check
and can break the check once the time difference is bigger than 60. Along the
way, I also do the check for amount. This solution clocked in at 112 ms, 69%.
"""


class Solution1:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Reorganize data
        tran_dict: Dict[str, Dict[str, List[List[str]]]] = defaultdict(
            lambda: defaultdict(list)
        )
        for t in transactions:
            t_list = t.split(",")
            tran_dict[t_list[0]][t_list[3]].append(t_list[1:3])
        # pp(tran_dict)
        res = set()
        for name, city_dict in tran_dict.items():
            city_list = list(city_dict.keys())
            for i in range(len(city_list) - 1):
                for j in range(i + 1, len(city_list)):
                    list_1 = city_dict[city_list[i]]
                    list_2 = city_dict[city_list[j]]
                    for ele_1 in list_1:
                        for ele_2 in list_2:
                            if int(ele_1[1]) > 1000:
                                res.add(",".join([name, *ele_1, city_list[i]]))
                            if abs(int(ele_1[0]) - int(ele_2[0])) <= 60:
                                res.add(",".join([name, *ele_1, city_list[i]]))
                                res.add(",".join([name, *ele_2, city_list[j]]))
            # check amount for the last city
            for ele in city_dict[city_list[-1]]:
                if int(ele[1]) > 1000:
                    res.add(",".join([name, *ele, city_list[-1]]))
        return list(res)


class Solution2:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res: Set[str] = set()
        split_tran: List[List[str]] = [t.split(",") for t in transactions]
        split_tran.sort(key=lambda x: (int(x[1])))  # sort on time
        # reorganize data
        tran_dict: Dict[str, List[List[str]]] = defaultdict(list)
        for t in split_tran:
            tran_dict[t[0]].append(t[1:])
        for name, rest in tran_dict.items():
            for i in range(len(rest) - 1):
                if int(rest[i][1]) > 1000:  # check for amount
                    res.add(",".join([name, *rest[i]]))
                for j in range(i + 1, len(rest)):  # check for time
                    if (int(rest[j][0]) - int(rest[i][0])) <= 60 and rest[i][
                        2
                    ] != rest[j][2]:
                        res.add(",".join([name, *rest[i]]))
                        res.add(",".join([name, *rest[j]]))
                    elif (int(rest[j][0]) - int(rest[i][0])) > 60:
                        break
            if int(rest[-1][1]) > 1000:
                res.add(",".join([name, *rest[-1]]))
        return list(res)


sol = Solution2()
transactions = [
    "bob,649,842,prague",
    "alex,175,1127,mexico",
    "iris,164,119,paris",
    "lee,991,1570,mexico",
    "lee,895,1876,taipei",
    "iris,716,754,moscow",
    "chalicefy,19,592,singapore",
    "chalicefy,820,71,newdelhi",
    "maybe,231,1790,paris",
    "lee,158,987,mexico",
    "chalicefy,415,22,montreal",
    "iris,803,691,milan",
    "xnova,786,804,guangzhou",
    "lee,734,1915,prague",
    "bob,836,1904,dubai",
    "iris,666,231,chicago",
    "iris,677,1451,milan",
    "maybe,860,517,toronto",
    "iris,344,1452,bangkok",
    "lee,664,463,frankfurt",
    "chalicefy,95,1222,montreal",
    "lee,293,1102,istanbul",
    "maybe,874,36,hongkong",
    "maybe,457,1802,montreal",
    "xnova,535,270,munich",
    "iris,39,264,istanbul",
    "chalicefy,548,363,barcelona",
    "lee,373,184,munich",
    "xnova,405,957,mexico",
    "chalicefy,517,266,luxembourg",
    "iris,25,657,singapore",
    "bob,688,451,beijing",
    "bob,263,1258,tokyo",
    "maybe,140,222,amsterdam",
    "xnova,852,330,barcelona",
    "xnova,589,837,budapest",
    "lee,152,981,mexico",
    "alex,893,1976,shenzhen",
    "xnova,560,825,prague",
    "chalicefy,283,399,zurich",
    "iris,967,1119,guangzhou",
    "alex,924,223,milan",
    "chalicefy,212,1865,chicago",
    "alex,443,537,taipei",
    "maybe,390,5,shanghai",
    "bob,510,1923,madrid",
    "bob,798,343,hongkong",
    "iris,643,1703,madrid",
    "bob,478,928,barcelona",
    "maybe,75,1980,shanghai",
    "xnova,293,24,newdelhi",
    "iris,176,268,milan",
    "alex,783,81,moscow",
    "maybe,560,587,milan",
    "alex,406,776,istanbul",
    "lee,558,727,paris",
    "maybe,481,1504,munich",
    "maybe,685,602,madrid",
    "iris,678,788,madrid",
    "xnova,704,274,newdelhi",
    "chalicefy,36,1984,paris",
    "iris,749,200,amsterdam",
    "lee,21,119,taipei",
    "iris,406,433,bangkok",
    "bob,777,542,taipei",
    "maybe,230,1434,barcelona",
    "iris,420,1818,zurich",
    "lee,622,194,amsterdam",
    "maybe,545,608,shanghai",
    "xnova,201,1375,madrid",
    "lee,432,520,dubai",
    "bob,150,1634,singapore",
    "maybe,467,1178,munich",
    "iris,45,904,beijing",
    "maybe,607,1953,tokyo",
    "bob,901,815,tokyo",
    "maybe,636,558,milan",
    "bob,568,1674,toronto",
    "iris,825,484,madrid",
    "iris,951,930,dubai",
    "bob,465,1080,taipei",
    "bob,337,593,chicago",
    "chalicefy,16,176,rome",
    "chalicefy,671,583,singapore",
    "iris,268,391,chicago",
    "xnova,836,153,jakarta",
    "bob,436,530,warsaw",
    "alex,354,1328,luxembourg",
    "iris,928,1565,paris",
    "xnova,627,834,budapest",
    "xnova,640,513,jakarta",
    "alex,119,16,toronto",
    "xnova,443,1687,taipei",
    "chalicefy,867,1520,montreal",
    "alex,456,889,newdelhi",
    "lee,166,3,madrid",
    "bob,65,1559,zurich",
    "alex,628,861,moscow",
    "maybe,668,572,mexico",
    "bob,402,922,montreal",
]
print(sol.invalidTransactions(transactions))
