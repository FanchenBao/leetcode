class Solution {
    public boolean winnerOfGame(String colors) {
        /*
        LeetCode 2038

        There is no trick here, because it is impossible to remove some colors and connect the colors on the left and
        right together. Thus, all we need to do is to find out the total number of moves Alice and Bob can make. Alice
        wins if she has more moves than Bob.

        O(N), 18 ms, faster than 18.53%
         */
        int[] moves = new int[]{0, 0};
        int[] cnt = new int[]{0, 0};
        cnt[colors.charAt(0) - 65] += 1;
        int idxCur; int idxPre;
        for (int i = 1; i < colors.length(); i++) {
            idxCur = colors.charAt(i) - 65;
            if (colors.charAt(i) != colors.charAt(i - 1)) {
                idxPre = colors.charAt(i - 1) - 65;
                moves[idxPre] += Math.max(0, cnt[idxPre] - 2);
                cnt[idxPre] = 0;
            }
            cnt[idxCur]++;
        }
        idxPre = colors.charAt(colors.length() - 1) - 65;
        moves[idxPre] += Math.max(0, cnt[idxPre] - 2);
        return moves[0] > moves[1];
    }
}


class Solution {
    public boolean winnerOfGame(String colors) {
        /*
        This is the official solution, which basically counts the moves from Alice and Bob directly.

        O(N), 17 ms, faster than 36.91%
         */
        int alice = 0; int bob = 0;
        for (int i = 1; i < colors.length() - 1; i++) {
            if (colors.charAt(i - 1) == colors.charAt(i) && colors.charAt(i) == colors.charAt(i + 1)) {
                if (colors.charAt(i) == 'A') {
                    alice++;
                } else {
                    bob++;
                }
            }
        }
        return alice > bob;
    }
}
