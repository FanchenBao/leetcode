class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        /*
        LeetCode 1337

        Sort it, but the two comparator sort in Java is quite verbose.
        5 ms, faster than 10.18%
         */
        int[][] lst = new int[mat.length][2];
        for (int i = 0; i < mat.length; i++) {
            for (int a : mat[i]) {
                lst[i][0] += a;
            }
            lst[i][1] = i;
        }
        Comparator<int[]> first = Comparator.comparingInt(tup -> tup[0]);
        Comparator<int[]> second = Comparator.comparingInt(tup -> tup[1]);
        Arrays.sort(lst, first.thenComparing(second));
        int [] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = lst[i][1];
        }
        return res;
    }
}
