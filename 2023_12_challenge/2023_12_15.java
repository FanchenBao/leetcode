class Solution {
    public String destCity(List<List<String>> paths) {
        /*
        LeetCode 1436
        
        Way too slow!! 3 ms, faster than 34.58%
         */
        Map<String, Integer> outDegrees = new HashMap<>();
        for (List<String> path : paths) {
            String src = path.get(0);
            String des = path.get(1);
            outDegrees.put(src, outDegrees.getOrDefault(src, 0) + 1);
            outDegrees.put(des, outDegrees.getOrDefault(des, 0));
        }
        for (String city : outDegrees.keySet()) {
            if (outDegrees.get(city) == 0)
                return city;
        }
        return "";
    }
}


class Solution {
    public String destCity(List<List<String>> paths) {
        /*
        Inspired by the official solution.
        
        2 ms, faster than 79.52%
         */
        Set<String> srcs = new HashSet<>();
        for (List<String> path : paths) {
            srcs.add(path.get(0));
        }
        for (List<String> path : paths) {
            if (!srcs.contains(path.get(1)))
                return path.get(1);
        }
        return "";
    }
}
