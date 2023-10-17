class Solution {
    public List<Integer> getRow(int rowIndex) {
        /*
        LeetCode 119
        
        1 ms, faster than 79.70% 
         */
        List<Integer> cur = new ArrayList<>(); cur.add(1);
        if (rowIndex == 0) return cur;
        for (int i = 1; i <= rowIndex; i++) {
            cur.add(1);
            for (int j = cur.size() - 2; j > 0; j--) cur.set(j, cur.get(j) + cur.get(j - 1));
        }
        return cur;
    }
}
