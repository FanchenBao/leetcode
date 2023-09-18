class Tuple {
    int idx;
    int state;

    Tuple(int idx, int state) {
        this.idx = idx; // idx of the node in graph
        this.state = state; // current graph state of which nodes have been visited
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.idx, this.state);
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (other == null || other.getClass() != this.getClass()) {
            return false;
        }
        Tuple o = (Tuple) other;
        return o.idx == this.idx && o.state == this.state;
    }
}

class Solution {
    public int shortestPathLength(int[][] graph) {
        /*
        LeetCode 847 (Failed)

        We've been having a series of failures. This is a new one. I have to check my previous solutions.

        The DP solution is really complicated, and I don't like it. This BFS is very simple. It's akin to how we usually
        do BFS to find the shortest path. The only difference is that in the current case, we are allowed to revisit
        a previously visited node. However, the spirit is the same. We BFS, do not repeat a previously conducted step,
        and the first time we have visited all the nodes is the shortest path.

        Now the question is how do we determine a previously conducted step? The answer is if we have a state of all
        the nodes that have been visited, and the current node to visit, these two combined can serve as the key for
        a conducted step. Thus, we use a Tuple class to represent each step. We make sure a same step is not conducted
        again.

        Since the total number of nodes is only 12, a bitmask is sufficient to represent the state of visited nodes.

        One last thing to note is that the number of steps is one less than the number of nodes visited.

        64 ms
         */
        int end = (1 << graph.length) - 1;
        Set<Tuple> visited = new HashSet<>(); // store states that have been visited.
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < graph.length; i++) {
            queue.add(new int[]{i, 1 << i, 0});
            visited.add(new Tuple(i, 1 << i));
        }
        int idx; int state; int steps = 0;
        while (!queue.isEmpty()) {
            int[] tmp = queue.remove();
            idx = tmp[0]; state = tmp[1]; steps = tmp[2];
            if (state == end) {
                break;
            }
            for (int nextIdx : graph[idx]) {
                Tuple next = new Tuple(nextIdx, state | 1 << nextIdx);
                if (!visited.contains(next)) {
                    queue.add(new int[]{nextIdx, state | 1 << nextIdx, steps + 1});
                    visited.add(next);
                }
            }
        }
        return steps;
    }
}


class Solution {
    public int shortestPathLength(int[][] graph) {
        /*
        LeetCode 847 (Failed)

        Same solution as the others with BFS, but instead of using a HashSet with Tuple as key, we simply use a 2D
        array to keep track.

        Should be much much faster.
        
        10 ms, faster than 83.70%
        O(N^2 * 2^N)
         */
        int end = (1 << graph.length) - 1;
        int[][] visited = new int[graph.length][end + 1]; // store states that have been visited.
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < graph.length; i++) {
            queue.add(new int[]{i, 1 << i, 0});
            visited[i][1 << i] = 1;
        }
        int idx; int state; int steps = 0;
        while (!queue.isEmpty()) {
            int[] tmp = queue.remove();
            idx = tmp[0]; state = tmp[1]; steps = tmp[2];
            if (state == end) {
                break;
            }
            for (int nextIdx : graph[idx]) {
                int nextState = state | 1 << nextIdx;
                if (visited[nextIdx][nextState] == 0) {
                    queue.add(new int[]{nextIdx, nextState, steps + 1});
                    visited[nextIdx][nextState] = 1;
                }
            }
        }
        return steps;
    }
}
