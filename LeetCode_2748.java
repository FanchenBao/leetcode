class Solution {
    public int gcd(int a, int b) {
       if (b==0) return a;
       return gcd(b,a%b);
    }

    public int countBeautifulPairs(int[] nums) {
        /*
        This is the O(N) solution. 5 ms, faster than 95.50%
         */
        int res = 0;
        int[] counter = new int[10];
        for (int i = 1; i < nums.length; i++) counter[nums[i] % 10]++;
        for (int i = 0; i < nums.length - 1; i++) {
            int f = Integer.toString(nums[i]).charAt(0) - '0';
            for (int k = 1; k <= 9; k++) {
                if (gcd(f, k) == 1)
                    res += counter[k];
            }
            counter[nums[i + 1] % 10]--;
        }
        return res;
    }
}

