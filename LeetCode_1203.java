class Solution {
    private ArrayList<Integer> topologicalSort(HashMap<Integer, Set<Integer>> graph, Integer[] nodes) {
        Queue<Integer> queue = new LinkedList<>();
        HashMap<Integer, Integer> indegrees = new HashMap<>();
        for (int par : nodes) {
            for (int child : graph.getOrDefault(par, Collections.emptySet())) {
                indegrees.put(child, indegrees.getOrDefault(child, 0) + 1);
            }
        }
        for (int par: nodes) {
            if (indegrees.getOrDefault(par, 0) == 0) {
                queue.add(par);
            }
        }
        ArrayList<Integer> order = new ArrayList<>();
        while (!queue.isEmpty()) {
            int par = queue.remove();
            for (int child : graph.getOrDefault(par, Collections.emptySet())) {
                indegrees.put(child, indegrees.get(child) - 1);
                if (indegrees.get(child) == 0) {
                    queue.add(child);
                }
            }
            order.add(par);
        }
        return order.size() == nodes.length ? order : new ArrayList<>();
    }

    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        /*
        Java implementation.

        63 ms, faster than 12.37%
         */
        int nonGroup = -1;
        for (int i = 0; i < group.length; i++) {
            if (group[i] < 0) {
                group[i] = nonGroup;
                nonGroup--;
            }
        }
        HashMap<Integer, Set<Integer>> itemGraph = new HashMap<>();
        HashMap<Integer, Set<Integer>> groupGraph = new HashMap<>();
        for (int i = 0; i < beforeItems.size(); i++) {
            List<Integer> befores = beforeItems.get(i);
            for (int b : befores) {
                itemGraph.computeIfAbsent(b, k -> new HashSet<>()).add(i);
                if (group[b] != group[i]) {
                    groupGraph.computeIfAbsent(group[b], k -> new HashSet<>()).add(group[i]);
                }
            }
        }
        // topological sort of the items
        Integer[] itemNodes = new Integer[n];
        for (int i = 0; i < n; i++) itemNodes[i] = i;
        ArrayList<Integer> itemOrder = topologicalSort(itemGraph, itemNodes);
        if (itemOrder.isEmpty()) { // loop in itemGraph
            return new int[0];
        }
        // topological sort of the groups
        HashMap<Integer, List<Integer>> groups = new HashMap<>();
        for (int item : itemOrder) {
            groups.computeIfAbsent(group[item], k -> new ArrayList<>()).add(item);
        }
        Integer[] groupNodes = groups.keySet().toArray(new Integer[0]);
        ArrayList<Integer> groupOrder = topologicalSort(groupGraph, groupNodes);
        if (groupOrder.isEmpty()) { // loop in groupGraph
            return new int[0];
        }
        // combine the results of both topological sort
        List<Integer> res = new ArrayList<>();
        for (int g : groupOrder) {
            res.addAll(groups.get(g));
        }
        int[] resArray = new int[n];
        for (int i = 0; i < n; i++) resArray[i] = res.get(i);
        return resArray;
    }
}
