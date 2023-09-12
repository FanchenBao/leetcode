class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        /*
        LeetCode 1282

        Go through each person and map its required group size to a groupMap. Once the desired group has reached the
        pre-defined size, remove it from the map and start a new one.

        O(N), 7 ms, faster than 55.15%
         */
        HashMap<Integer, List<Integer>> groupMap = new HashMap<>();
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < groupSizes.length; i++) {
            int s = groupSizes[i];
            if (groupMap.getOrDefault(s, Collections.emptyList()).size() == s) {
                res.add(groupMap.get(s));
                groupMap.remove(s);
            }
            groupMap.putIfAbsent(s, new ArrayList<>());
            groupMap.get(s).add(i);
        }
        res.addAll(groupMap.values());
        return res;
    }
}
