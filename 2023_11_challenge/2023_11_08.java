class Solution {
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        /*
        LeetCode 2849
        
        Find the min steps needed to go from s to f, and then compare that to t.
        The min steps involve taking as many diagonals as possible.
        
        The really tricky part is when s and f overlap and t == 1. In such case,
        it is impossible to go from s to f with 1 step.
        */
        int minSteps = Math.min(Math.abs(sx - fx), Math.abs(sy - fy)) + Math.abs(Math.abs(sx - fx) - Math.abs(sy - fy));
        if (minSteps == 0)
            return t != 1;
        return t >= minSteps;
    }
}