class Solution {
    public List<List<Integer>> generate(int numRows) {
        /*
        LeetCode 118

        1 ms, faster than 89.25%
        */
        List<List<Integer>> res = new ArrayList<>();
        // Handle first row
        res.add(new ArrayList<>());
        res.get(0).add(1);
        if (numRows == 1) {
            return res;
        }
        // Handle the others
        for (int i = 2; i <= numRows; i++) {
            List<Integer> curRow = new ArrayList<>();
            curRow.add(1);
            List<Integer> lastRow = res.get(res.size() - 1);
            for (int j = 0; j < lastRow.size() - 1; j++) {
                curRow.add(lastRow.get(j) + lastRow.get(j + 1));
            }
            curRow.add(1);
            res.add(curRow);
        }
        return res;
    }
}
