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


class Solution {
    public int[][] imageSmoother(int[][] img) {
        /*
        This method uses divmod to hide two values in one number.
        Say we want to hide p and r, then for a given X, we can hide
        these two values in Y = p * X + r.

        Here, we assign r as the original value in img, thus X must be
        256, because we can get r by performing Y % 256.

        p becomes the average.
        */
        int M = img.length; int N = img[0].length;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
               int cnt = 0; int sum = 0;
               for (int x = i - 1; x <= i + 1; x++) {
                   for (int y = j - 1; y <= j + 1; y++) {
                       if (x >= 0 && x < M && y >= 0 && y < N) {
                           sum += img[x][y] % 256;
                           cnt++;
                       }
                   }
               }
               img[i][j] += (sum / cnt) * 256;
            }
        }
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                img[i][j] /= 256;
            }
        }
        return img;
    }
}


class Solution {
    public int[][] imageSmoother(int[][] img) {
        /*
        This method stores the original value in the least significant
        8 bits, and the average value in the 8 bits right above the least
        significant 8 bits. We can do this because the values in img is
        not bigger than 256, which means they can all be represented by
        8 bits. Similarly, their mean can also be represented by 8 bits.
        */
        int M = img.length; int N = img[0].length;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
               int cnt = 0; int sum = 0;
               for (int x = i - 1; x <= i + 1; x++) {
                   for (int y = j - 1; y <= j + 1; y++) {
                       if (x >= 0 && x < M && y >= 0 && y < N) {
                           sum += img[x][y] & 255;
                           cnt++;
                       }
                   }
               }
               img[i][j] |= (sum / cnt) << 8 ;
            }
        }
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                img[i][j] >>= 8;
            }
        }
        return img;
    }
}

