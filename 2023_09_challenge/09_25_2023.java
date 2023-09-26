class Solution {
    public char findTheDifference(String s, String t) {
        /*
        LeetCode 389
        
        12 ms, faster than 10.41%
        */
        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            counter.put(s.charAt(i), counter.getOrDefault(s.charAt(i), 0) + 1);
        }
        char res = ' ';
        for (int j = 0; j < t.length(); j++) {
            res = t.charAt(j);
            if (counter.getOrDefault(res, 0) == 0) {
                break;
            }
            counter.put(res, counter.get(res) - 1);
        }
        return res;
    }
}


class Solution {
    public char findTheDifference(String s, String t) {
        /*
        Use XOR to quickly identify the odd one out. And use string.toCharArray to
        loop through each character more easily
        
        1 ms, faster than 100.00%
         */
        int xor = 0;
        for (char cs : s.toCharArray()) {
            xor ^= cs;
        }
        for (char ct : t.toCharArray()) {
            xor ^= ct;
        }
        return (char)xor;
    }
}
