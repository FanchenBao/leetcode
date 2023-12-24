class Solution {
    public boolean isPathCrossing(String path) {
        /*
        LeetCode 1496
        
        Use a hashmap + hashset to keep track of what points have been
        visited.
        
        O(N), 1 ms, faster than 96.48%
         */
        Map<Integer, Set<Integer>> visited = new HashMap<>();
        int x = 0; int y = 0;
        visited.putIfAbsent(x, new HashSet<>());
        visited.get(x).add(y);
        for (int i = 0; i < path.length(); i++) {
            if (path.charAt(i) == 'N')
                y++;
            else if (path.charAt(i) == 'S')
                y--;
            else if (path.charAt(i) == 'E')
                x++;
            else
                x--;
            if (visited.containsKey(x) && visited.get(x).contains(y))
                return true;
            visited.putIfAbsent(x, new HashSet<>());
            visited.get(x).add(y);
        }
        return false;
    }
}

