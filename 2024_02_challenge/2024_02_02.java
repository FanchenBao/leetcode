class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        /*
        LeetCode 1291
        
        Iterate through all the sequential digit numbers from the lower bound
        of the number of digits, until the higher bound of the number of digits.
        
        We can simply iterate through them all because the total number of
        qualified numbers is not that many.
        
        0 ms, faster than 100.00% 
        */
        int[] powerOf10 = new int[]{1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
        List<Integer> res = new ArrayList<>();
        for (int d = (int)Math.floor(Math.log10(low)) + 1; d <= (int)Math.floor(Math.log10(high)) + 1; d++) {
            int curNum = 0;
            for (int i = 1; i <= d; i++) {
                curNum = curNum * 10 + i;
            }
            for (int j = 1; j <= 9 - d + 1; j++){
                if (curNum > high)
                    break;
                if (curNum >= low)
                    res.add(curNum);
                curNum = (curNum * 10 + (curNum % 10 + 1)) % powerOf10[d];
            }
        }
        return res;
    }
}


class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        /*
        This is the Queue solution. The key to realize that a queue is good for
        this problem is that we produce 234 from 23 instead of 123.        
         */
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= 9; i++) queue.add(i);
        List<Integer> res = new ArrayList<>();
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            if (cur >= low && cur <= high)
                res.add(cur);
            if (cur % 10 < 9)
                queue.add(cur * 10 + cur % 10 + 1);
        }
        return res;
    }
}

