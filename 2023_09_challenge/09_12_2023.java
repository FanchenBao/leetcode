class Solution {
    public int minDeletions(String s) {
        /*
        LeetCode 1647

        Find the frequencies of eahc letter. Find the counts of each frequency. The problem can be transformed into given
        the unique frequencies, how do we reduce the duplicated freq such that the duplicates get reduced to a unique
        unoccupied freq.

        This idea is to go through the freqs in non-decreasing order. For each new freq and its previous one, we can
        obtain the number of unoccupied freqs. For the current freq, if its count is more than 1, the extra freq shall
        be decreased to fit in the previous unoccupied freqs. If these unoccupied freqs are all filled, we look for
        the previous previous one, until the entire supply of unoccupied freqs get exhausted, at which time we have to
        reduce the freq to zero.

        We use a stack to keep track of all the unoccupied freqs.

        O(N), 57 ms, faster than 14.42%
         */
        Map<Character, Integer> charCounter = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            charCounter.put(s.charAt(i), charCounter.getOrDefault(s.charAt(i), 0) + 1);
        }
        Map<Integer, Integer> freqCounter = new HashMap<>();
        for (Integer v : charCounter.values()) {
            freqCounter.put(v, freqCounter.getOrDefault(v, 0) + 1);
        }
        Integer[] freqs = freqCounter.keySet().toArray(new Integer[0]);
        Arrays.sort(freqs);
        Stack<int[]> stack = new Stack<>(); // stack[i] = [first unoccupied freq, the number of consecutive unoccupied freq]
        int res = 0; int pre = 1; // pre is the smallest available value in the previous gap
        for (Integer f : freqs) {
            if (f - pre >= 1) {
                stack.push(new int[]{pre, f - pre});
            }
            int c = freqCounter.get(f);
            while (c - 1 > 0 && !(stack.isEmpty())) {
                // If we have some unoccupied positions before, use them as much as we can
                int[] ava = stack.pop();
                if (c - 1 >= ava[1]) {
                    res += f * ava[1] - (ava[0] + ava[0] + ava[1] - 1) * ava[1] / 2;
                    c -= ava[1];
                } else {
                    res += f * (c - 1) - (2 * ava[0] + 2 * ava[1] - c) * (c - 1) / 2;
                    ava[1] -= c - 1;
                    stack.push(ava);
                    c = 1; // all c - 1 counts of f have been dealt with
                }
            }
            if (c - 1 > 0) {
                // the remaining values shall all turn to zero
                res += f * (c - 1);
            }
            pre = f + 1;
        }
        return res;
    }
}
