/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    MountainArray ma;
    int tgt;
    Map<Integer, Integer> cache = new HashMap<>();
    
    private int getVal(int idx) {
        if (cache.containsKey(idx)) return cache.get(idx);
        int res = ma.get(idx);
        cache.put(idx, res);
        return res;
    }
    
    private int bisectLeftInc(int lo, int hi) {
        int mid;
        lo--;
        while (lo < hi) {
            mid = (lo + hi + 1) / 2;
            if (getVal(mid) >= tgt) hi = mid - 1;
            else lo = mid;
        }
        return hi + 1;
    }
    
    private int bisectLeftDec(int lo, int hi) {
        // the array is sorted desc
        int mid;
        lo--;
        while (lo < hi) {
            mid = (lo + hi + 1) / 2;
            if (getVal(mid) > tgt) lo = mid;
            else hi = mid - 1;
        }
        return hi + 1;
    }
    
    private int helper(int lo, int hi) {
        if (hi - lo + 1 <= 3) {
            for (int i = lo; i <= hi; i++) {
                if (getVal(i) == tgt) {
                    return i;
                }
            }
            return -1;
        }
        int mid; int j;
        int prevVal; int postVal; int midVal;
        int tmp;
        mid = (lo + hi) / 2;
        midVal = getVal(mid);
        prevVal = getVal(mid - 1);
        postVal = getVal(mid + 1);

        if (prevVal < midVal && midVal < postVal) {
            // mid is on an increasing edge
            if (midVal == tgt) return mid;
            if (midVal > tgt) {
                j = bisectLeftInc(lo, mid - 1);
                if (j < mid && getVal(j) == tgt) return j;
            }
            return helper(mid + 1, hi);
        } else if (prevVal > midVal && midVal > postVal) {
            // mid is on an decreasing edge
            // We always have to try to match tgt on the left
            tmp = helper(lo, mid - 1);
            if (tmp >= 0) return tmp;
            // only when the left fails to match tgt, we go for the mid
            if (midVal == tgt) return mid;
            // or to the right of mid
            j = bisectLeftDec(mid + 1, hi);
            if (j <= hi && getVal(j) == tgt) return j;
        } else {
            // mid is peak
            if (midVal < tgt) return -1;
            if (midVal == tgt) return mid;
            // always do the left edge first
            j = bisectLeftInc(lo, mid - 1);
            if (j < mid && getVal(j) == tgt) return j;
            j = bisectLeftDec(mid + 1, hi);
            if (j <= hi && getVal(j) == tgt) return j;
        }
        return -1;
    }
    
    public int findInMountainArray(int target, MountainArray mountainArr) {
        /*
        LeetCode 1095

        Just binary search, but the requirement that we must find the min index
        and the restriction on the usage of MountainArray.get() means that we
        have to consider two things.

        1. Under any circumstance, always try the left side first. This is to
        ensure that a smaller index always has precedence over larger ones.

        2. Use a cache to avoid repeated calls to MountainArray.get().

        Another thing to note is that since the mountain array does not contain
        repeats on each edge, we could use bisect right.
        */
        ma = mountainArr;
        tgt = target;
        return helper(0, mountainArr.length() - 1);
    }
}