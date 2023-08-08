import java.util.Arrays;

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        /*
        LeetCode 74

        Finally back at Java. Two rounds of binary search. The first round find which row we shall investigate. The
        second round search through the target row.

        O(M + log(M) + log(N)), 0 ms, faster than 100.00%
         */
        int M = matrix.length;
        int[] firstCol = new int[M];
        for (int i = 0; i < M; i++){
            firstCol[i] = matrix[i][0];
        }
        int binsearchRowIdx = Arrays.binarySearch(firstCol, target);
        if (binsearchRowIdx >= 0) {
            return true;
        }
        int rowIdx = -(binsearchRowIdx + 1) - 1;
        if (rowIdx < 0) {
            return false;
        }
        int binsearchColIdx = Arrays.binarySearch(matrix[rowIdx], target);
        return binsearchColIdx >= 0;
    }
}

public class Main {
    public static void main(String[] args) {
        int[][][] matrices = {
                {
                    {1, 3, 5, 7},
                    {10, 11, 16, 20},
                    {23, 30, 34, 60},
                },
                {
                    {1, 3, 5, 7},
                    {10, 11, 16, 20},
                    {23, 30, 34, 60},
                },
        };
        int[] targets = {3, 13};
        boolean[] answers = {true, false};
        Solution sol = new Solution();
        for (int i = 0; i < answers.length; i++) {
            boolean res = sol.searchMatrix(matrices[i], targets[i]);
            if (res == answers[i]) {
                System.out.printf("Test %d: PASS\n", i);
            } else {
                System.out.printf("Test %d: Fail; ans: %s; res: %s\n", i, answers[i], res);
            }
        }
    }
}