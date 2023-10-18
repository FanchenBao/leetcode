class Solution {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        int[] indegrees = new int[n];
        for (int i = 0; i < n; i++) {
            if (leftChild[i] >= 0) indegrees[leftChild[i]]++;
            if (rightChild[i] >= 0) indegrees[rightChild[i]]++;
        }
        int[] count = new int[2];
        int root = -1;
        for (int i = 0; i < n; i++) {
            if (indegrees[i] > 1) return false; // some node has more than one indegree, impossible for binary tree
            if (indegrees[i] == 0) root = i;
            count[indegrees[i]]++;
        }
        if (count[0] != 1) return false; // more than one possible root.
        
        // Traverse the tree and make sure that the graph is connected
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(root); visited.add(root);
        int cur;
        while (!queue.isEmpty()) {
            cur = queue.poll();
            if (leftChild[cur] >= 0) {
                if (visited.contains(leftChild[cur])) return false; // cycle detected
                queue.add(leftChild[cur]); visited.add(leftChild[cur]);
            }
            if (rightChild[cur] >= 0) {
                if (visited.contains(rightChild[cur])) return false; // cycle detected
                queue.add(rightChild[cur]); visited.add(rightChild[cur]);
            }
        }
        return visited.size() == n;
    }
}
