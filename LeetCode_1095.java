/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        /*
        This is a redo, following the official solution, where we identify
        the peek first and then search for the target on the left or right
        slope.
        
        O(logN), 0 ms, faster than 100.00%
        */
        // First find the position of the peek.
        int N = mountainArr.length();
        int lo = 0; int hi = N - 1; int mid;
        int pre; int cur; int nex;
        int peekIdx = -1;
        while (lo <= hi) {
            mid = (lo + hi) / 2;
            pre = mid - 1 >= 0 ? mountainArr.get(mid - 1) : -1;
            cur = mountainArr.get(mid);
            nex = mid + 1 < N ? mountainArr.get(mid + 1) : Integer.MAX_VALUE;
            if (pre < cur && cur > nex) {
                peekIdx = mid;
                break;
            }
            if (pre < cur && cur < nex) lo = mid + 1;
            else hi = mid - 1;
        }
        if (peekIdx < 0) peekIdx = lo;
        // Binary search the left slope first
        lo = 0; hi = peekIdx;
        while (lo <= hi) {
            mid = (lo + hi) / 2;
            cur = mountainArr.get(mid);
            if (target == cur) return mid;
            if (target < cur) hi = mid - 1;
            else lo = mid + 1;
        }
        // Binary search the right slope. Right slope is decreasing
        lo = peekIdx + 1; hi = N - 1;
        while (lo <= hi) {
            mid = (lo + hi) / 2;
            cur = mountainArr.get(mid);
            if (target == cur) return mid;
            if (target < cur) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }
}
