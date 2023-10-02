class Solution {
    public int minDeletions(String s) {
        /*
        Last time I solved this was Sep 12, and I remembered that I struggled
        a lot. That was why I kept this problem here so that I can try another
        method sometime later.
        
        Now it is sometime later and miraculously I have found a better solution.
        This one is based on the idea that we first find the frequencies of
        each letter.
        
        Then we find the frequencies of the frequencies.
        
        The goal is to make each frequency's frequenc equal to 1. What we can
        do is to first sort the letter frequencies. Then we start from the
        largest frequency. If a target frequency has already only got one
        count, we skip it because there is nothing to remove.
        
        Otherwise, we need to determine what new frequency to demote the
        current frequency to. To make the demotion as efficient as possible
        (i.e. with the lowest number of deletion), we need to find the largest
        frequency with zero count. We can simply iterate from the current
        frequency down to find it.
        
        This won't take too much time, because the total number of letter
        frequencies is not more than 26. So iteration from the current frequency
        down to an unused frequency shall be very fast. The worst case would
        be that we iterate all the way down to zero, which will cost no more
        than 26 loops.
        
        Then we are down.
        
        O(N), 11 ms, faster than 43.65%
        */
        int[] charFreq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            charFreq[s.charAt(i) - 97] += 1;
        }
        Map<Integer, Integer> freqFreq = new HashMap<>();
        for (int f : charFreq) {
            freqFreq.put(f, freqFreq.getOrDefault(f, 0) + 1);
        }
        Integer[] sortedFreqKeys = freqFreq.keySet().toArray(new Integer[0]);
        Arrays.sort(sortedFreqKeys);
        int res = 0;
        for (int i = sortedFreqKeys.length - 1; i >= 0; i--) {
            int curFreq = sortedFreqKeys[i];
            for (int nextFreq = curFreq - 1; nextFreq > 0 && freqFreq.get(curFreq) > 1; nextFreq--) {
                if (freqFreq.getOrDefault(nextFreq, 0) == 0) {
                    freqFreq.put(nextFreq, 1);
                    freqFreq.put(curFreq, freqFreq.get(curFreq) - 1);
                    res += curFreq - nextFreq;
                }
            }
            if (freqFreq.get(curFreq) > 1) {
                res += curFreq * (freqFreq.get(curFreq) - 1);
                freqFreq.put(curFreq, 1);
            }
        }
        return res;
    }
}


class Solution {
    public int minDeletions(String s) {
        /*
        Inspired by https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/discuss/927549/C%2B%2BJavaPython-3-Greedy
        
        Same idea but Better implementation.
        
        O(N), 8 ms, faster than 74.22%
        */
        int[] charFreq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            charFreq[s.charAt(i) - 97]++;
        }
        Set<Integer> used = new HashSet<>(); // whether a letter count has been used before.
        int res = 0;
        for (int i = 0; i < 26; i++) {
            while (charFreq[i] > 0 && used.contains(charFreq[i])) {
                charFreq[i]--;
                res++;
            }
            if (charFreq[i] > 0) {
                used.add(charFreq[i]);
            }
        }
        return res;
    }
}
