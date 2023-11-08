class Solution {
    public int sumDistance(int[] nums, String s, int d) {
        /*
        First of all, the collision doesn't matter, because it takes no time
        and it's as if the robots are just passing each other by.
        
        Then we can easily obtain the final positions of all robots after d.
        The question now is to find the total distance between all pairs.
        
        The method here starts with a sum of all prefix sums, and then progressively
        compute the distance starting from each robot going to the right.
        
        However, it feels slow.
        
        O(NlogN), 12 ms, faster than 10.49%
        */
        int MOD = 1000000007;
        long[] pos = new long[nums.length];
        for (int i = 0; i < nums.length; i++) {
            pos[i] = (long)nums[i] + (s.charAt(i) == 'L' ? -d : d);
        }
        Arrays.sort(pos);
        long[] dis = new long[pos.length - 1];
        for (int i = 0; i < dis.length; i++) dis[i] = pos[i + 1] - pos[i];
        long pres = 0; long S = 0;
        for (long dd : dis) {
            pres = (pres + dd) % MOD;
            S = (S + pres) % MOD;
        }
        long res = S;
        for (int i = 0; i < dis.length - 1; i++) {
            S -= (dis.length - i) * dis[i];
            res = (res + S) % MOD;
        }
        return (int)(res + MOD) % MOD;
    }
}


class Solution {
    public int sumDistance(int[] nums, String s, int d) {
        /*
        With assistance from
        https://leetcode.com/problems/movement-of-robots/discuss/3622277/Easy-Beginner-Friendly-with-Explanations-Pass-Through-%2B-Prefix-Sum-or-C%2B%2B-Python
        
        The computation of the total distance is simplified. Think from the
        perspective of positions, not the distance between positions.
        
        Let the robots final positions be R0, R1, R2, ...
        
        Then all the distances ending at R1 is R1 - R0
        Ending at R2: R2 - R1 + R2 - R0 = 2 * R2 - (R0 + R1)
        Ending at R3: 3 * R3 - (R0 + R1 + R2)
        
        Thus, all we need is a prefix sum of Rs.
        
        O(NlogN), 10 ms, faster than 78.32%
        */
        int MOD = 1000000007;
        long[] pos = new long[nums.length];
        for (int i = 0; i < nums.length; i++) {
            pos[i] = (long)nums[i] + (s.charAt(i) == 'L' ? -d : d);
        }
        Arrays.sort(pos);
        long res = 0; long pres = pos[0];
        for (int i = 1; i < pos.length; i++) {
            res = (res + i * pos[i] - pres) % MOD;
            pres = (pres + pos[i]) % MOD;
        }
        return (int)(res + MOD) % MOD;
    }
}