class Solution {
    public int findContentChildren(int[] g, int[] s) {
        /*
        LeetCode 455
        
        Make sure the biggest cookie is used to satisfy the
        kid with the largest greed.
        
        O(NlogN + MlogM), 8 ms, faster than 98.82%
        */
        Arrays.sort(g);
        Arrays.sort(s);
        int j = s.length - 1;
        int res = 0;
        for (int i = g.length - 1; i >= 0 && j >= 0; i--) {
            if (g[i] <= s[j]) {
                res++;
                j--;
            }
        }
        return res;
    }
}

