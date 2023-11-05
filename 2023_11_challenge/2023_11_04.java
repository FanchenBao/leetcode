class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        /*
        LeetCode 1503
        
        The trick is to realize that it is impossible to simulate the entire
        process. However, we can observe that each time two ants meet and they
        switch direction, it is as if the left going ant is now represented
        by the right going ant, and the right going ant is now represented by
        the left going ant. This means regardless of how many times an ant has
        to switch direction, the end result is that each ant spends the same
        amount of time on the plank as if it has never changed diretction.
        
        Thus the solution is to find the left most ant that goes right, and the
        right most ant that goes left, and find the max between the two.
        
        O(N + M), 0 ms, faster than 100.00%
        */
        int maxLeft = 0; int minRight = n;
        for (int l : left) maxLeft = Math.max(l, maxLeft);
        for (int r : right) minRight = Math.min(r, minRight);
        return Math.max(maxLeft, n - minRight);
    }
}