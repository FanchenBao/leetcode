class Solution {
    public int kthGrammar(int n, int k) {
        /*
        LeetCode 779
        
        The table is a complete binary tree, which we can index using
        1 for the root. Thus, each left child is double the parent idx
        while the right child is double plus one.
        
        We find the idx of the target value on the last row, then go
        backwards to produce the path.
        
        After that, we go from top to bottom following the path to
        find out what the target value is.
        
        O(N), 1 ms, faster than 100.00%
        */
        Stack<Integer> path = new Stack<>();
        path.push((int)Math.pow(2, n - 1) + k - 1);
        while (path.peek() > 1) path.push(path.peek() / 2);
        path.pop();
        int res = 0; int node;
        while (!path.isEmpty()) {
            if (path.pop() % 2 == 0) res = res == 0 ? 0 : 1;
            else res = res == 0 ? 1 : 0;
        }
        return res;
    }
}


class Solution {
    public int kthGrammar(int n, int k) {
        /*
        From the official solution with the recursion method.
        
        The observation is that the first half of each row are always
        the same from row to row. The second half of each row is always
        the flipped version of the first half. Thus, to find out
        kthGrammar(n, k), we decide whether k is in the first half or
        second half. If it is in the first half, we simply find the same
        position in row n - 1. Otherwise, we find the flipped version of
        the same location in the first half.
        
        O(N), 0 ms, faster than 100.00%
        */
        if (n == 1) return 0;
        int half = (int)Math.pow(2, n - 2);
        return k > half ? 1 - kthGrammar(n, k - half) : kthGrammar(n - 1, k);
    }
}


class Solution {
    public int kthGrammar(int n, int k) {
        /*
        From the third math solution.
        
        In the second solution, we observe that each time we flip
        the value, k must be larger than half. Each time we flip,
        half of the row size is deducted from k. Thus, the problem
        can be converted to finding out how many times we need to
        deduct half the size of some row such that k is reduced to
        1.
        
        In other words, we need to find out a way to write k - 1 as
        a sum of some power of twos. This can be resolved by finding
        the binary representation of k - 1. Then the number of one bits
        represent the number of times the value is flipped.
        
        O(logK), 0 ms, faster than 100.00%
        */
        return Integer.bitCount(k - 1) % 2 == 0 ? 0 : 1;
    }
}