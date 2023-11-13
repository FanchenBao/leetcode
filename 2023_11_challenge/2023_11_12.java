class Solution {
    Map<Integer, List<Integer>> stopsToRoute = new HashMap<>();
    List<Set<Integer>> routeGraph = new ArrayList<>();

    public int numBusesToDestination(int[][] routes, int source, int target) {
        /*
        LeetCode 815 TLE!!!
        
        Find the routes that contain source and the routes that contain target.
        Use the routes array to construct a graph for all the routes.
        Then use BFS to find the shortest path from any route that contains
        source to any route that contains target.
        
        Two tricky part. First, if source == target, we don't have to take any
        bus.
        
        Second, if source or target does not belong to any routes, it is not
        possible to reach from source to target.
        
        Let N = len(routes), M = total number of stops inside routes (including
        repeition)
        
        O(M + N + M' * N^2 + N) TLE
        */
        if (source == target)
            return 0;
        for (int i = 0; i < routes.length; i++) {
            for (int stop : routes[i]) {
                stopsToRoute.putIfAbsent(stop, new ArrayList<>());
                stopsToRoute.get(stop).add(i);
            }
        }
        if (!stopsToRoute.containsKey(source) || !stopsToRoute.containsKey(target))
            return -1;
        for (int i = 0; i < routes.length; i++) routeGraph.add(new HashSet<>());
        for (List<Integer> rs : stopsToRoute.values()) {
            for (int i = 0; i < rs.size(); i++) {
                for (int j = i + 1; j < rs.size(); j++) {
                    routeGraph.get(rs.get(i)).add(rs.get(j));
                    routeGraph.get(rs.get(j)).add(rs.get(i));
                }
            }
        }
        // BFS to find the shortest path from source to target
        List<Integer> queue = new ArrayList<>(stopsToRoute.get(source));
        List<Integer> tmp;
        Set<Integer> tgtRoutes = new HashSet<>(stopsToRoute.get(target));
        Set<Integer> seen = new HashSet<>(queue);
        int res = 0;
        while (!queue.isEmpty()) {
            tmp = new ArrayList<>();
            for (int r : queue) {
                if (tgtRoutes.contains(r)) return res + 1;
                for (int child : routeGraph.get(r)) {
                    if (!seen.contains(child)) {
                        tmp.add(child);
                        seen.add(child);
                    }
                }
            }
            queue = tmp;
            res++;
        }
        return -1;
    }
}


class Solution {
    Map<Integer, List<Integer>> stopsToRoute = new HashMap<>();

    public int numBusesToDestination(int[][] routes, int source, int target) {
        /*
        Change the way for BFS. Instead of creating all the edges among the
        routes, we only examine the routes that will be involved during BFS.
        
        O(N^2 * M), where N = len(routes), M = all the stops
        */
        if (source == target)
            return 0;
        for (int i = 0; i < routes.length; i++) {
            for (int stop : routes[i]) {
                stopsToRoute.putIfAbsent(stop, new ArrayList<>());
                stopsToRoute.get(stop).add(i);
            }
        }
        if (!stopsToRoute.containsKey(source) || !stopsToRoute.containsKey(target))
            return -1;
        List<Integer> queue = new ArrayList<>(stopsToRoute.get(source));
        List<Integer> tmp;
        Set<Integer> tgtRoutes = new HashSet<>(stopsToRoute.get(target));
        Set<Integer> seenRoutes = new HashSet<>(queue);
        Set<Integer> seenStops = new HashSet<>(); seenStops.add(source);
        int res = 0;
        while (!queue.isEmpty()) {
            tmp = new ArrayList<>();
            for (int r : queue) {
                if (tgtRoutes.contains(r)) return res + 1;
                for (int stop : routes[r]) {
                    if (!seenStops.contains(stop)) {
                        seenStops.add(stop);
                        for (int nextR : stopsToRoute.get(stop)) {
                            if (!seenRoutes.contains(nextR)) {
                                seenRoutes.add(nextR);
                                tmp.add(nextR);
                            }
                        }
                    }
                }
            }
            queue = tmp;
            res++;
        }
        return -1;
    }
}
