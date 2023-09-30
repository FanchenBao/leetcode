class Solution {
    public int candy(int[] ratings) {
        /*
        Inspired by https://leetcode.com/problems/candy/discuss/42769/A-simple-solution

        Initialize all positions to have 1 candy.

        Do a left to right pass. If ratings[i] > ratings[i - 1], make res[i] = res[i - 1] + 1.

        Do a right to left pass. If ratings[i] > ratings[i + 1], make res[i] = max(res[i + 1] + 1, res[i])

        To prove, suppose we have ratings[j] > ratings[j - 1]. Then left-to-right gives lr[j] = lr[j - 1] + 1.
        Right-to-left gives rl[j] = rl[j - 1]. Then

        res[j] = max(lr[j], rl[j]) = max(lr[j - 1] + 1, rl[j - 1])
        res[j - 1] = max(lr[j - 1], rl[j - 1])

        Apparently res[j] > res[j - 1], which fits what the ratings want.

        O(N), 3 ms, faster than 77.99%
         */
        int[] candies = new int[ratings.length];
        Arrays.fill(candies, 1);
        // left to right
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        // right to left
        for (int j = ratings.length - 2; j >= 0; j--) {
            if (ratings[j] > ratings[j + 1]) {
                candies[j] = Math.max(candies[j], candies[j + 1] + 1);
            }
        }
        int res = 0;
        for (int c : candies) {res += c;}
        return res;
    }
}
