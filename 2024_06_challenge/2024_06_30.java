import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for a binary tree node.
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//    TreeNode() {}
//    TreeNode(int val) { this.val = val; }
//    TreeNode(int val, TreeNode left, TreeNode right) {
//        this.val = val;
//        this.left = left;
//        this.right = right;
//    }
//}

class DSU {
    int[] par;
    int[] rnk;
    int components;

    DSU(int n) {
        this.par = new int[n];
        this.rnk = new int[n];
        for (int i = 0; i < n; i++)
            this.par[i] = i;
        this.components = n; // number of distinct parents
    }

    public int find(int x) {
        if (this.par[x] != x)
            this.par[x] = find(this.par[x]);
        return this.par[x];
    }

    public boolean union(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            if (this.rnk[px] > this.rnk[py]) {
                this.par[py] = px;
            } else if (this.rnk[py] > this.rnk[px]) {
                this.par[px] = py;
            } else {
                this.rnk[px]++;
                this.par[py] = px;
            }
            this.components--; // when two nodes union, the number of parents decrease
            return true;
        }
        return false;
    }
}


class Solution1 {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        /*
         * LeetCode 1579
         *
         * Use union and find. First we handle all the type 3 edges (i.e. shared
         * by both Bob and Alice). We can remove any type 3 edges that is not
         * necessary.
         *
         * Then we handle Alice's edges alone, removing any unnecessary. We
         * do the same for Bob's edges.
         *
         * Finally we check if alice or bob's union contain more than one parents.
         *
         * 15 ms, faster than 59.24%
         */
        int res = 0;
        DSU alice = new DSU(n + 1);
        DSU bob = new DSU(n + 1);
        List<int[]> aliceEdges = new ArrayList<>();
        List<int[]> bobEdges = new ArrayList<>();
        for (int[] e : edges) {
            if (e[0] == 1) {
                aliceEdges.add(e);
            } else if (e[0] == 2) {
                bobEdges.add(e);
            } else {
                boolean aliceNeedEdge = alice.union(e[1], e[2]);
                boolean bobNeedEdge = bob.union(e[1], e[2]);
                if (!aliceNeedEdge && !bobNeedEdge)
                    res++;
            }
        }
        for (int[] e : aliceEdges) {
            if (!alice.union(e[1], e[2]))
                res++;
        }
        for (int[] e : bobEdges) {
            if (!bob.union(e[1], e[2]))
                res++;
        }
        int alicePar = -1;
        int bobPar = -1;
        for (int v = 1; v <= n; v++) {
            int ap = alice.find(v);
            int bp = bob.find(v);
            if ((alicePar != ap && alicePar != -1) || (bobPar != bp && bobPar != -1))
                return -1;
            alicePar = ap;
            bobPar = bp;
        }
        return res;
    }
}


class Solution2 {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        /*
         * Same solution as Solution1, but with a more performant Union-Find
         * where we keep track of the number of components in the set. Also,
         * we do not use extra space because we can simply loop through edges
         * twice to get alice and bob's own edges.
         *
         * 11 ms, faster than 84.45%
         */
        int res = 0;
        DSU alice = new DSU(n + 1);
        DSU bob = new DSU(n + 1);
        for (int[] e : edges) {
            if (e[0] == 3) {
                boolean aliceNeedEdge = alice.union(e[1], e[2]);
                boolean bobNeedEdge = bob.union(e[1], e[2]);
                if (!aliceNeedEdge && !bobNeedEdge)
                    res++;
            }
        }
        for (int[] e : edges) {
            if(e[0] == 1 && !alice.union(e[1], e[2]))
                res++;
            else if (e[0] == 2 && !bob.union(e[1], e[2]))
                res++;
        }
        // check components count. It has to be two because we have an extra
        // parent 0.
        return alice.components == 2 && bob.components == 2 ? res : -1;
    }
}





class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
