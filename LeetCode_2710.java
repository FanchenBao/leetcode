class Solution1 {
    public String removeTrailingZeros(String num) {
        /*
        1 ms, faster than 100.00%
         */
        int len = num.length();
        for (; num.charAt(len - 1) == '0'; len--);
        return num.substring(0, len);
    }
}


class Solution2 {
    public String removeTrailingZeros(String num) {
        /*
        Regex, for fun, but it's so slow: 17 ms, faster than 7.57%
         */
        return num.replaceAll("^(\\d+?)0*$", "$1");
    }
}
