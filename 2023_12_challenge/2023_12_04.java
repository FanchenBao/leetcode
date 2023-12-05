class Solution {
    public String largestGoodInteger(String num) {
        /*
        LeetCode 2264
        
        2 ms, faster than 80.64%
        */
        String res = "";
        int cnt = 1;
        for (int i = 1; i < num.length(); i++) {
            if (num.charAt(i) == num.charAt(i - 1)) {
                cnt++;
                if (cnt == 3) {
                    String tmp = num.substring(i - 2, i + 1);
                    if (tmp.compareTo(res) > 0)
                        res = tmp;
                }
            } else {
                cnt = 1;
            }
        }
        return res;
    }
}
