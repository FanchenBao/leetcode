class Solution {
    public int candy(int[] ratings) {
        /*
        LeetCode 135
        
        Two passes. Left to right, identify the valleys, rising, peak, and ignore. Do the same for right to left. When
        hit a valley, set the candies to 1. When hit rising, increment the candy count. When hit peak, retain the max
        count. When hit ignore, just ignore.
        
        At the end, talley all the candies. If there is a position where no candy has been allocated, set it to 1.
        O(N), 5 ms, faster than 23.69%  
         */
        int[] modRats = new int[ratings.length + 2];
        modRats[0] = Integer.MAX_VALUE; modRats[modRats.length - 1] = Integer.MAX_VALUE;
        System.arraycopy(ratings, 0, modRats, 1, ratings.length);
        int[] candies = new int[ratings.length]; // default values are zeroes
        // Lef to right.
        // Valleys: [1,0,1], [0,0,1] (set the middle to 1)
        // Rising: [0,1,2] (increment middle by 1)
        // Peak: [0,1,0], [0,1,1] (increment middle by 1, and also take the max)
        // Ignore: [2,1,0], [1,1,0], [0,0,0], [1,0,0]
        for (int i = 1; i < modRats.length - 1; i++) {
            if (modRats[i] <= modRats[i - 1] && modRats[i] < modRats[i + 1]) {
                // check valley
                candies[i - 1] = 1;
            } else if (modRats[i] > modRats[i - 1] && modRats[i] < modRats[i + 1]) {
                // check rising
                candies[i - 1] = candies[i - 2] + 1;
            } else if (modRats[i] > modRats[i - 1] && modRats[i] >= modRats[i + 1]) {
                // check peak
                candies[i - 1] = Math.max(candies[i - 1], candies[i - 2] + 1);
            }
        }
        // Right to left.
        // Valleys: [1,0,1], [1,0,0] (set the middle to 1)
        // Rising: [2,1,0] (increment middle by 1)
        // Peak: [0,1,0], [1,1,0] (increment middle by 1, and also take the max)
        // Ignore: [0,1,2], [0,1,1], [0,0,0], [0,0,1]
        for (int i = modRats.length - 2; i >= 1; i--) {
            if (modRats[i] < modRats[i - 1] && modRats[i] <= modRats[i + 1]) {
                // check valley
                candies[i - 1] = 1;
            } else if (modRats[i] < modRats[i - 1] && modRats[i] > modRats[i + 1]) {
                // check rising
                candies[i - 1] = candies[i] + 1;
            } else if (modRats[i] >= modRats[i - 1] && modRats[i] > modRats[i + 1]) {
                // check peak
                candies[i - 1] = Math.max(candies[i - 1], candies[i] + 1);
            }
        }
        int res = 0;
        for (int c : candies) {
            res += c == 0 ? 1 : c;
        }
        return res;
    }
}
