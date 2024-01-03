class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        /*
        LeetCode 2610
        
        Since each row must contain distinct integers, each copy
        of the same integer occupys a differen row. Thus, we can
        keep a counter of each integer, and add a new row to the
        result when there are more copies of an integer than the
        number of rows.
        
        O(N), 3 ms, faster than 77.12%
        */
        int[] counter = new int[nums.length + 1];
        List<List<Integer>> res = new ArrayList<>();
        for (int n : nums) {
            counter[n]++;
            if (res.size() < counter[n])
                res.add(new ArrayList<>());
            res.get(counter[n] - 1).add(n);
        }
        return res;
    }
}

