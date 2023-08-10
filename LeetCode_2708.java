class Solution {
    public long maxStrength(int[] nums) {
        /*
        This is NOT difficult, but the amount of thinking into all the possible cases is quite demanding.

        O(N), 2 ms, faster than 99.42%
         */
        ArrayList<Integer> negs = new ArrayList<>();
        long posProd = 1;
        long negProd = 1;
        boolean hasZero = false;
        boolean hasPos = false;
        int negCount = 0;
        int maxNeg = -Integer.MAX_VALUE;
        for (int n: nums) {
            if (n < 0) {
                negProd *= n;
                negCount += 1;
                maxNeg = Math.max(n, maxNeg);
            } else if (n > 0) {
                posProd *= n;
                hasPos = true;
            } else {
                hasZero = true;
            }
        }
        if (negCount > 1 && negProd < 0) {
            negProd /= maxNeg;
        }
        if (hasPos) {
            return Math.max(posProd * negProd, posProd);
        }
        if (negCount > 0) {
            return hasZero ? Math.max(negProd, 0) : negProd;
        }
        return 0;
    }
}
