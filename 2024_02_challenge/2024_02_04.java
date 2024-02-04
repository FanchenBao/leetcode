class Solution {

    private boolean contains(int[] a1, int[] a2) {
        /*
        Does a1 contains a2
         */
        for (int i = 0; i < a1.length; i++) {
            if (a1[i] < a2[i])
                return false;
        }
        return true;
    }

    public String minWindow(String s, String t) {
        /*
        LeetCode 76
        
        Binary search with sliding window
        
        O(N + Mlog(M)), 25 ms, faster than 33.70%
        */
        int lo = t.length() - 1;
        int hi = s.length() + 1;
        int[] tcount = new int[58];
        for (int i = 0; i < t.length(); i++) tcount[t.charAt(i) - 'A']++;
        String res = "";
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid == 0)  // length cannot be zero
                break;
            int[] currCount = new int[58];
            String curRes = null;
            for (int i = 0; i < s.length(); i++) {
                currCount[s.charAt(i) - 'A']++;
                if (i + 1 < mid)
                    continue;
                if (contains(currCount, tcount)) {
                    curRes = s.substring(i - mid + 1, i + 1);
                    break;
                }
                currCount[s.charAt(i - mid + 1) - 'A']--;
            }
            if (curRes == null) {
                lo = mid + 1;
            } else {
                res = curRes;
                hi = mid;
            }
        }
        return res;
    }
}

class Solution {
    public String minWindow(String s, String t) {
        /*
        The official sliding window solution that runs in O(M + N)
        It uses a shrinked version of s that contains ONLY the letters that also appear
        in t. Then we use two pointers, where i is on the right and j on the left. We always
        expand i first, and if the current window of shrinked S covers t, we move j forward
        until the substring between i and j no longer contains t.
        
        O(M + N) 9 ms, faster than 73.24%
         */
        // Letter counter for s and t
        int[] cs = new int[58];
        int[] ct = new int[58];
        for (int i = 0; i < t.length(); i++) ct[t.charAt(i) - 'A']++;
        // record all the letters in s that exists in t
        List<int[]> shrinkedS = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (ct[s.charAt(i) - 'A'] > 0) 
                shrinkedS.add(new int[]{s.charAt(i), i});
        }
        int numOfMatchedLetters = 0;
        int[] resIdx = new int[]{0, s.length() + t.length()};
        int j = 0;
        for (int i = 0; i < shrinkedS.size(); i++) {
            int c = shrinkedS.get(i)[0] - 'A';
            cs[c]++;
            if (cs[c] <= ct[c])
                numOfMatchedLetters++;
            while (j <= i && numOfMatchedLetters == t.length()) {
                if (shrinkedS.get(i)[1] - shrinkedS.get(j)[1] < resIdx[1] - resIdx[0]) {
                    resIdx[0] = shrinkedS.get(j)[1];
                    resIdx[1] = shrinkedS.get(i)[1];
                }
                int cc = shrinkedS.get(j)[0] - 'A';
                cs[cc]--;
                if (cs[cc] < ct[cc])
                    numOfMatchedLetters--;
                j++;
            }
        }
        if (resIdx[1] - resIdx[0] + 1 >= t.length() && resIdx[1] - resIdx[0] + 1 <= s.length())
            return s.substring(resIdx[0], resIdx[1] + 1);
        return "";
    }
}

