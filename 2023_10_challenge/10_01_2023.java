class Solution {
    char[] chars;
    
    private void reverse(int lo, int hi) {
        int i = lo; int j = hi; char tmp;
        while (i < j) {
            tmp = chars[i];
            chars[i] = chars[j];
            chars[j] = tmp;
            i++; j--;
        }
    }
    
    public String reverseWords(String s) {
        /*
        LeetCode 557
        
        O(N), 3 ms, faster than 98.87%
        */
        chars = s.toCharArray();
        int i = 0; int j = 0;
        for (; j < chars.length; j++) {
            if (chars[j] == ' ') {
                reverse(i, j - 1);
                i = j + 1;
            }
        }
        reverse(i, j - 1);
        return String.valueOf(chars);
    }
}
