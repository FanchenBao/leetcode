class Solution {
    public int[][] imageSmoother(int[][] img) {
        /*
        LeetCode 661
        
        Lots of trial and error to smooth out the edge cases.
        
        O(MN), 6 ms, faster than 80.11% 
        */
        int M = img.length; int N = img[0].length;
        int[][] res = new int[M][N];
        for (int i = 0; i < M; i++) {
            int cur = (i == 0 ? 0 : img[i - 1][0]) + img[i][0] + (i == M - 1 ? 0 : img[i + 1][0]);
            for (int j = 0; j < N; j++) {
                cur += j == N - 1 ? 0 : ((i == 0 ? 0 : img[i - 1][j + 1]) + img[i][j + 1] + (i == M - 1 ? 0 : img[i + 1][j + 1]));
                cur -= j <= 1 ? 0 : ((i == 0 ? 0 : img[i - 1][j - 2]) + img[i][j - 2] + (i == M - 1 ? 0 : img[i + 1][j - 2]));
                int cnt = (i - 1 >= 0 ? 1 : 0) + (i + 1 < M ? 1 : 0) + (j - 1 >= 0 ? 1 : 0) + (j + 1 < N ? 1 : 0);
                if (cnt == 4)
                    cnt = 9;
                else if (cnt == 3)
                    cnt = 6;
                else if (cnt == 2)
                    cnt = ((i - 1 >= 0 && i + 1 < M) || (j - 1 >= 0 && j + 1 < N) ? 3 : 4);
                else if (cnt == 1)
                    cnt = 2;
                else
                    cnt = 1;
                res[i][j] = cur / cnt;
            }
        }
        return res;
    }
}

