class Solution {
    public int knightDialer(int n) {
        /*
        LeetCode 935
        
        DP, O(10N), 116 ms, faster than 24.46%
         */
        if (n == 1)
            return 10;
        int MOD = 1000000007;
        long[] dp = new long[]{1,1,1,1,1,1,1,1,1,1,1};
        List<List<Integer>> dict = List.of(
                List.of(4, 6),
                List.of(6, 8),
                List.of(7, 9),
                List.of(4, 8),
                List.of(0, 3, 9),
                List.of(),
                List.of(0, 1, 7),
                List.of(2, 6),
                List.of(1, 3),
                List.of(2, 4)
        );
        for (int i = 2; i <= n; i++) {
            long[] tmp = new long[10];
            for (int j = 0; j < 10; j++) {
                for (int neigh : dict.get(j))
                    tmp[j] = (tmp[j] + dp[neigh]) % MOD;
            }
            dp = tmp;
        }
        long res = 0;
        for (long c : dp) res = (res + c) % MOD;
        return (int)res;
    }
}


class Solution {
    public int knightDialer(int n) {
        /*
        LeetCode 935
        
        DP, O(10N)
        
        Update: use int array for the dict
        
        24 ms, faster than 74.46% 
         */
        if (n == 1)
            return 10;
        int MOD = 1000000007;
        long[] dp = new long[]{1,1,1,1,1,1,1,1,1,1,1};
        int[][] dict = {
            {4, 6},
            {6, 8},
            {7, 9},
            {4, 8},
            {3, 9, 0},
            {},
            {1, 7, 0},
            {2, 6},
            {1, 3},
            {2, 4}
        };
        for (int i = 2; i <= n; i++) {
            long[] tmp = new long[10];
            for (int j = 0; j < 10; j++) {
                for (int neigh : dict[j])
                    tmp[j] = (tmp[j] + dp[neigh]) % MOD;
            }
            dp = tmp;
        }
        long res = 0;
        for (long c : dp) res = (res + c) % MOD;
        return (int)res;
    }
}


class Solution {
    public int knightDialer(int n) {
        /*
        LeetCode 935
        
        DP, O(10N)
        
        Update Update: use efficient iteration, which means we will skip
        the duplicate situations. For instance,
        * 1, 3, 7, 9 fall under the same condition. We call this group A
        * 2 and 8 fall under the same condition. We call this group B
        * 4 and 6 fall under the same condition. We call this group C
        * 0 is its own condition. We call this group D

        A -> B, C
        B -> A
        C -> A, D
        D -> C

        We initialzie A = 4, B = 2, C = 2, D = 1
        A = 2 * B + 2 * C
        B = A (overall, the four As get hit once each)
        C = A + 2 * D (overall, the four As get hit once each, the one D twice)
        D = C (overall, the two Cs get hit once each)
        
        O(N), 5 ms, faster than 98.64%

         */
        if (n == 1)
            return 10;
        int MOD = 1000000007;
        long A = 4; long B = 2; long C = 2; long D = 1;
        for (int i = 2; i <= n; i++) {
            long AA = (2 * B + 2 * C) % MOD;
            long BB = A;
            long CC = (A + 2 * D) % MOD;
            long DD = C;
            A = AA; B = BB; C = CC; D = DD;
        }
        return (int)((A + B + C + D) % MOD);
    }
}

