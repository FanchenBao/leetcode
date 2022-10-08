# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """LeetCode 16
        
        Surprisingly, the solution that had worked before no longer worked
        today. Although that was fixable (do not use block if statement, use
        if in a single line. e.g. `foo = bar if condition else baz`), it might
        be worthwhile to explore some other solutions.

        I got this solution purely by luck. it uses two pointers, lo and hi,
        but do not have the third value fixed. We will binary search to look
        for the third one.
        
        The best third value is `target - nums[lo] - nums[hi]`.
        Binary search it in nums to find its idx. Since we are coming from
        left and right and going inwards, any idx that is outside the boundary
        of lo and hi can be discarded, BUT we must still compute a sum for it.
        If the idx is to the left of lo, that means lo and
        hi are too big, we move hi left. Otherwise we move lo right.

        If the idx is in between lo and hi, we can analyze two scenarios for
        the third value (nums[idx - 1] and nums[idx], if idx - 1 doesn't
        overlap with lo and idx doesn't overlap with hi).
        
        We pick the scenario closest to target. Then based on whether the
        current 3sum result is larger than target or smaller, we move hi left
        or lo right, respectively.

        And since the answer is unique, we won't be facing the situation where
        the two scenarios have equal distance to the target. This means at each
        step, we have a clear signal which pointer to move.

        O(NlogN), 496 ms, faster than 95.47%
        """
        nums.sort()
        diff = math.inf
        res = 0
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            r = target - nums[lo] - nums[hi]
            idx = bisect_right(nums, r)
            if idx <= lo:
                s = nums[lo] + nums[hi] + nums[lo + 1]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    res = s
                hi -= 1
            elif idx > hi:
                s = nums[lo] + nums[hi] + nums[hi - 1]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    res = s
                lo += 1
            else:
                diff_l = diff_r = math.inf
                if idx - 1 > lo:
                    s = nums[lo] + nums[hi] + nums[idx - 1]
                    diff_l = abs(s - target)
                    if diff_l < diff:
                        diff = diff_l
                        res = s
                if idx < hi:
                    s = nums[lo] + nums[hi] + nums[idx]
                    diff_r = abs(s - target)
                    if diff_r < diff:
                        diff = diff_r
                        res = s
                if diff_l < diff_r:
                    lo += 1
                else:
                    hi -= 1
        return res


class Solution2:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Much much simpler binary search, but has O(N^2) runtime

        The original solution TLE. Someone suggested not using block if. Let's
        see if it works.
        """
        nums.sort()
        diff = math.inf
        res = 0
        for i in range(len(nums) - 2):
            n = nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[lo] + nums[hi] + n
                cur_diff = abs(s - target)
                res = s if cur_diff < diff else res
                diff = min(cur_diff, diff)
                # if abs(s - target) < diff:
                #     diff = abs(s - target)
                #     res = s
                if s > target:
                    hi -= 1
                elif s < target:
                    lo += 1
                else:
                    return s
        return res


sol = Solution2()
tests = [
    ([-1,2,1,-4], 1, 2),
    ([0,0,0], 1, 0),
    ([0,1,2], 0, 3),
    ([713,375,483,-225,-624,173,-210,114,433,226,-189,-269,-250,881,559,686,-738,-441,245,-661,622,-15,522,-801,-350,700,791,-434,-239,-253,-609,-214,24,756,132,-983,930,461,101,506,-506,-606,-641,719,2,535,-657,-788,637,-926,5,-706,233,-226,-191,515,-166,799,-872,879,416,785,234,196,889,336,463,-699,-605,740,738,11,-93,353,-370,171,579,494,283,712,-310,-511,332,-571,-134,232,449,-631,626,-299,72,689,119,299,721,632,430,-531,641,-26,847,164,-815,-406,-910,-116,-33,58,-968,-107,-839,138,612,624,222,-559,-403,708,538,-149,835,-694,329,-48,820,-12,215,-122,-920,14,832,577,-818,319,-395,702,-582,671,-749,-53,850,-525,-779,984,946,920,117,511,318,-599,-757,915,-301,822,-826,257,446,-546,773,-846,-130,158,-141,314,807,988,-241,-740,-256,202,722,-556,111,-962,-759,600,254,769,-152,-800,-164,-244,-621,963,-880,649,37,168,572,-13,50,605,-979,-701,541,-439,-845,-20,-991,-372,-23,-43,-668,961,-262,-195,-190,-677,-316,-41,873,-675,871,943,425,27,921,-695,694,951,-502,0,-610,-61,-494,443,424,485,-756,954,-186,808,922,-558,277,687,19,-469,617,584,-461,982,-627,-22,47,-844,-271,-852,-518,441,-344,-151,-832,33,-643,675,289,815,-124,183,-727,82,-566,958,-109,-293,-946,486,159,-384,-65,453,-776,18,-488,-274,-464,35,-913,990,-24,-659,560,-298,250,163,-765,-126,477,-296,656,276,-935,-218,414,288,503,311,-397,498,186,794,-654,12,434,735,445,221,49,-197,-125,-391,-417,-764,167,-802,29,-103,94,865,-211,633,-782,-601,-172,447,-713,420,149,-794,-864,-177,-942,685,938,292,716,514,-243,-447,517,-304,431,-89,-475,-308,-120,793,941,481,-270,872,-973,570,-289,308,-94,724,-471,-486,-507,-25,194,8,542,86,280,-685,-555,473,586,-547,120,774,429,-843,-718,-16,304,199,26,368,92,378,-742,710,64,-64,-882,328,-848,917,-50,427,749,-955,160,-543,861,-608,-618,-823,-862,170,725,403,565,743,627,662,-850,-382,-129,519,-623,-284,-205,575,-829,-56,-286,939,418,-133,-110,761,-117,401,-37,352,212,-692,592,-716,281,-564,778,775,635,218,-821,-42,46,-127,784,-90,-686,927,-66,787,766,444,359,750,-514,647,-232,-769,-889,-781,501,227,824,705,809,110,-161,913,-162,-487,-435,851,-158,746,-648,631,666,-373,-495,558,-837,89,-168,-575,243,190,-222,676,-176,505,608,596,-85,-267,583,-333,-533,-200,-415,287,-674,-115,-474,739,-538,669,-97,45,495,107,660,-462,122,-300,580,-291,792,-453,16,935,247,645,-545,-389,-206,877,390,819,955,-902,-4,417,-28,4,845,623,285,325,923,-150,-529,320,-748,-944,-828,804,907,831,-831,-998,683,322,-258,783,-2,450,-497,-775,83,150,-878,-35,-112,-827,-565,599,-949,-335,-508,628,707,-468,-656,-59,-737,-519,143,629,-670,521,-917,469,-81,900,595,140,-676,305,748,653,-876,-783,13,516,925,358,752,312,-577,720,-988,78,-702,630,908,681,-505,398,625,-18,-365,910,-378,-361,856,-753,-230,-598,604,127,854,240,187,456,-816,-322,723,-34,874,-583,823,532,-336,-807,118,-58,379,-612,744,-220,-47,476,992,-437,253,154,-473,882,548,229,811,767,715,-673,-38,741,-956,408,-971,21,964,-890,-836,-277,-690,-999,105,180,439,-833,-357,-376,-709,465,732,991,313,867,509,126,-728,-886,-198,-457,-278,296,-10,345,144,699,-342,137,-970,246,152,-964,-704,339,932,-67,-855,-381,857,-603,-491,57,-553,709,-62,-982,-552,-355,611,924,-235,-255,-787,688,31,875,462,-840,-114,621,-188,-854,947,706,432,980,-541,116,135,-957,-223,23,-866,162,-842,176,-294,-337,448,-490,383,-578,-911,768,365,-204,-351,-388,241,-528,-1,814,25,-268,806,261,-887,789,125,918,-958,781,-422,-918,-181,282,-346,-217,372,479,-449,652,-562,-901,400,-394,-236,-936,-717,862,-155,-688,540,-425,-691,75,-377,362,949,93,475,974,-485,44,-798,-493,54,-743,-73,-1000,-637,397,-568,-972,-669,644,-897,-594,324,-975,236,-312,736,263,-482,-323,-905,487,-143,578,734,95,457,-891,-708,-822,-767,338,-758,573,-557,-859,-451,419,269,782,38,85,-698,354,-173,-147,-664,-658,-21,-396,-739,60,-906,-700,839,-7,962,-517,-883,-438,502,293,-169,-667,-313,-224,615,-340,370,389,852,731,169,-364,718,537,-327,-121,65,182,410,-154,-63,238,948,616,-703,-542,-712,-762,-307,894,385,405,-725,508,916,979,407,-187,-600,-649,914,108,-813,665,347,-108,765,-408,-240,-379,569,303,546,-74,197,-984,-924,-838,42,490,-247,81,-931,109,-139,561,562,601,892,553,-732,-635,888,454,350,670,539,442,555,237,-588,-925,145,-808,-476,-536,-215,-19,-812,-805,-745,614,317,-352,-961,-443,966,-655,-684,919,131,-997,904,-892,985,-260,-483,323,-92,-245,-407,-792,697,96,438,-730,967,478,166,829,757,291,-413,-532,-137,6,153,901,-584,-593,-280,489,-400,300,301,-526,-863,-614], 428, 428),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.threeSumClosest(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
