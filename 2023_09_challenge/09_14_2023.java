class Solution {
    Map<String, Map<String, Integer>> graph;
    List<String> res;
    String resStr;

    private void backtrack(String airport, int remTickets, List<String> itinerary) {
        if (remTickets == 0) {
            String cur = String.join("", itinerary);
            if (resStr == null || cur.compareTo(resStr) < 0) {
                resStr = cur;
                res = new ArrayList<>(itinerary);
            }
        } else {
            Map<String, Integer> subgraph = graph.get(airport);
            if (subgraph == null) {
                return;
            }
            for (String nextAirport : subgraph.keySet()) {
                if (subgraph.get(nextAirport) > 0) {
                    subgraph.put(nextAirport, subgraph.get(nextAirport) - 1);
                    itinerary.add(nextAirport);
                    backtrack(nextAirport, remTickets - 1, itinerary);
                    subgraph.put(nextAirport, subgraph.get(nextAirport) + 1);
                    itinerary.remove(itinerary.size() - 1);
                }
            }
        }
    }

    public List<String> findItinerary(List<List<String>> tickets) {
        /*
        LeetCode 332
        
        Brute force, backtracking, TLE
         */
        graph = new HashMap<>();
        for (List<String> fromto : tickets) {
            String from = fromto.get(0); String to = fromto.get(1);
            graph.putIfAbsent(from, new HashMap<>());
            graph.get(from).put(to, graph.get(from).getOrDefault(to, 0) + 1);
        }
        backtrack("JFK", tickets.size(), new ArrayList<>(List.of("JFK")));
        return res;
    }
}
