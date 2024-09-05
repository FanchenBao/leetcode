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


class Solution {
    int[][] DIRS = new int[][]{{1, 0}, {0, -1}, {-1, 0}, {0, 1}}; // N, W, S, E

    private void getNextPos(int[] pos, int command, Map<Integer, List<Integer>> rowObs, Map<Integer, List<Integer>> colObs) {
        // pos is composed of three elements: [i, j, direction]
        if (command == -1) {
            pos[2] = (pos[2] + 3) % 4;
        } else if (command == -2) {
            pos[2] = (pos[2] + 1) % 4;
        } else {

            int ni = pos[0] + this.DIRS[pos[2]][0] * command;
            int nj = pos[1] + this.DIRS[pos[2]][1] * command;
            if (ni == pos[0]) {
                // moving east-west
                if (rowObs.containsKey(ni)) {
                    int idx = Collections.binarySearch(rowObs.get(ni), pos[1]);
                    if (this.DIRS[pos[2]][1] > 0) {
                        idx = idx >= 0 ? idx + 1 : -(idx + 1);
                        pos[1] = idx >= rowObs.get(ni).size() || rowObs.get(ni).get(idx) > nj ? nj : rowObs.get(ni).get(idx) - 1;
                    } else {
                        idx = idx >= 0 ? idx - 1 : -(idx + 1) - 1;
                        pos[1] = idx < 0 || rowObs.get(ni).get(idx) < nj ? nj : rowObs.get(ni).get(idx) + 1;
                    }
                } else {
                    pos[1] = nj;
                }
            } else {
                // moving north-south
                if (colObs.containsKey(nj)) {
                    int idx = Collections.binarySearch(colObs.get(nj), pos[0]);
                    if (this.DIRS[pos[2]][0] > 0) {
                        idx = idx >= 0 ? idx + 1 : -(idx + 1);
                        pos[0] = idx >= colObs.get(nj).size() || colObs.get(nj).get(idx) > ni ? ni : colObs.get(nj).get(idx) - 1;
                    } else {
                        idx = idx >= 0 ? idx - 1 : -(idx + 1) - 1;
                        pos[0] = idx < 0 || colObs.get(nj).get(idx) < ni ? ni : colObs.get(nj).get(idx) + 1;
                    }
                } else {
                    pos[0] = ni;
                }
            }
        }
    }

    public int robotSim(int[] commands, int[][] obstacles) {
        /*
         * LeetCode 874
         *
         * Full simulation using binary search to check whether the next
         * command will encounter an obstacle either on the row or col.
         *
         * O(NlogM + MlogM), where N = len(commands), M = len(obstacles)
         * 27 ms, faster than 59.83% 
         */
        Map<Integer, List<Integer>> rowObs = new HashMap<>();
        Map<Integer, List<Integer>> colObs = new HashMap<>();
        for (int[] obs : obstacles) {
            rowObs.putIfAbsent(obs[1], new ArrayList<>());
            colObs.putIfAbsent(obs[0], new ArrayList<>());
            rowObs.get(obs[1]).add(obs[0]);
            colObs.get(obs[0]).add(obs[1]);
        }
        for (List<Integer> vals : rowObs.values())
            Collections.sort(vals);
        for (List<Integer> vals : colObs.values())
            Collections.sort(vals);
        int[] pos = new int[]{0, 0, 0}; // start at (0, 0) and going North
        int res = 0;
        for (int c : commands) {
            getNextPos(pos, c, rowObs, colObs);
            res = Math.max(res, pos[0] * pos[0] + pos[1] * pos[1]);
        }
        return res;
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
