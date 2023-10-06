class Solution {
    public List<Integer> majorityElement(int[] nums) {
        /*
        LeetCode 229
        
        This is O(N) space and O(N) time.
        10 ms, faster than 49.32%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) {
            counter.put(n, counter.getOrDefault(n, 0) + 1);
        }
        List<Integer> res = new ArrayList<>();
        int lim = nums.length / 3;
        for (int k : counter.keySet()) {
            if (counter.get(k) > lim) {
                res.add(k);
            }
        }
        return res;
    }
}


class Solution {
    public List<Integer> majorityElement(int[] nums) {
        /*
        From the official solution: Boyer-Moore algorithm

        We want to find the top two majority elements in nums. We set up two candidates
        and two corresponding counts. If a third element is encountered, both counts
        decrement. If any count decrements to zero, we swap the candidate with the current
        value. Eventually, we will end up with two candidates. If any element indeed has
        more than 1/3 count, it will be one of the two eventual candidates. However, it
        is also possible that we do not have an element with more than 1/3 count. Therefore
        we have to count the candidates again just to make sure.
        
        Notice that when cad1 or cad2 matches the current element, we increment
        by 2. This is to accommodate the decrement, since for each mismatch,
        we decrement 1 on both counts. In other words, a mismatched element
        is counted twice. Hence each matched element must count twice as well.

        O(N) time and O(1) space, 2 ms, faster than 98.52%
         */
        int cad1 = Integer.MAX_VALUE; int cad2 = Integer.MAX_VALUE;
        int cnt1 = 0; int cnt2 = 0;
        for (int n: nums) {
            if (cad1 == n) {
                cnt1 += 2; continue;
            } else if (cad2 == n) {
                cnt2 += 2; continue;
            }
            if (cnt1 != 0 && cnt2 != 0) {
                cnt1--; cnt2--;
            }
            if (cnt1 == 0) {
                cad1 = n; cnt1 = 1;
            } else if (cnt2 == 0) {
                cad2 = n; cnt2 = 1;
            }
        }
        cnt1 = 0; cnt2 = 0;
        for (int n : nums) {
            if (n == cad1) cnt1++;
            if (n == cad2) cnt2++;
        }
        int lim = nums.length / 3;
        List<Integer> res = new ArrayList<>();
        if (cnt1 > lim) res.add(cad1);
        if (cnt2 > lim && cad2 != cad1) res.add(cad2);
        return res;
    }
}


class Solution {
    public List < Integer > majorityElement(int[] nums) {
        // Better implementation of Boyer-Moore algorithm.

        // 1st pass
        int count1 = 0;
        int count2 = 0;

        int candidate1 = Integer.MAX_VALUE;
        int candidate2 = Integer.MAX_VALUE;

        for (int n: nums) {
            if (candidate1 == n) {
                count1++;
            } else if (candidate2 == n) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = n;
                count1++;
            } else if (count2 == 0) {
                candidate2 = n;
                count2++;
            } else {
                count1--;
                count2--;
            }
        }

        // 2nd pass
        List result = new ArrayList <> ();

        count1 = 0;
        count2 = 0;

        for (int n: nums) {
            if (n == candidate1) count1++;
            if (n == candidate2) count2++;
        }

        int n = nums.length;
        if (count1 > n/3) result.add(candidate1);
        if (count2 > n/3) result.add(candidate2);

        return result;
    }
}