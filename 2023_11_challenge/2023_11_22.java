class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        /*
        LeetCode 1424
        
        All the cells on the same diagonal has the identical i + j sum. Traverse nums
        row by row and put all the values of the same diagonal in a list. Then grab
        the list from the smallest i + j sum to the largest.
        
        O(NM), 48 ms, faster than 18.43% 
         */
        Map<Integer, List<Integer>> diags = new HashMap<>();
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.get(i).size(); j++) {
                diags.putIfAbsent(i + j, new ArrayList<>());
                diags.get(i + j).add(nums.get(i).get(j));
            }
        }
        List<Integer> resList = new ArrayList<>();
        List<Integer> keys = new ArrayList<>(diags.keySet());
        Collections.sort(keys);
        for (int k : keys) {
            for (int i = diags.get(k).size() - 1; i >= 0; i--) {
                resList.add(diags.get(k).get(i));
            }
        }
        int[] res = new int[resList.size()];
        for (int i = 0; i < resList.size(); i++) res[i] = resList.get(i);
        return res;
    }
}


class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        /*
        This is the BFS solution from the official solution. The main idea is that if we
        consider each cell in nums as a node, the next diagonal values are the current
        node's down and right neighbors. Thus, if we BFS from the top left, each round
        of BFS constitutes a diagonal in order.
        
        The solution also uses a trick to avoid the usage of a hashset to avoid duplicates.
        If a node is on the left edge, we consider its down and right neighbors. Otherwise,
        we only consider its right neighbor.
        
        O(MN), 20 ms, faster than 91.42%
         */
        List<Integer> resList = new ArrayList<>();
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 0});
        while (!queue.isEmpty()) {
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                int[] tup = queue.poll();
                resList.add(nums.get(tup[0]).get(tup[1]));
                if (tup[1] == 0 && tup[0] + 1 < nums.size())
                    queue.add(new int[]{tup[0] + 1, tup[1]});
                if (tup[1] + 1 < nums.get(tup[0]).size())
                    queue.add(new int[]{tup[0], tup[1] + 1});
            }
        }
        int[] res = new int[resList.size()];
        for (int i = 0; i < resList.size(); i++) res[i] = resList.get(i);
        return res;
    }
}
