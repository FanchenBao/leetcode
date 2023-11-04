class Solution {
    public List<String> buildArray(int[] target, int n) {
        /*
        LeetCode 1441
        
        Once the problem is fully comprehended, the solution is
        very straightforward.
        
        O(N), 0 ms, faster than 100.00% 
        */
        List<String> res = new ArrayList<>();
        int j = 0;
        for (int i = 1; j < target.length; i++) {
            res.add("Push");
            if (target[j] != i) res.add("Pop");
            else j++;
        }
        return res;
    }
}
