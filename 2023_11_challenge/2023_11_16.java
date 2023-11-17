class Solution {
    public String findDifferentBinaryString(String[] nums) {
        /*
        LeetCode 1980
        
        Turn nums into a set and then check from 1 to (2 << n) - 1 to see which does not
        exist in the nums set.
        
        O(N^2, 14 ms, faster than 19.64%
         */
        Set<String> numsSet = new HashSet<>(Arrays.asList(nums));
        int i = 0;
        String fmt = "%" + nums.length + "s";
        String b = String.format(fmt, Integer.toBinaryString(i)).replace(" ", "0");
        while (numsSet.contains(b))
            b = String.format(fmt, Integer.toBinaryString(++i)).replace(" ", "0");
        return b;
    }
}


class Solution {
    public String findDifferentBinaryString(String[] nums) {
        /*
        Check values in nums one by one and see if num + 1 is the next value.

        Sort nums first.
        
        O(NlogN + N^2), 13 ms, faster than 20.55%
         */
        Arrays.sort(nums);
        int cur = 0;
        String fmt = "%" + nums.length + "s";
        String b = String.format(fmt, Integer.toBinaryString(cur)).replace(" ", "0");
        for (int i = 0; i < nums.length && nums[i].equals(b); i++)
            b = String.format(fmt, Integer.toBinaryString(++cur)).replace(" ", "0");
        return b;
    }
}

class Solution {
    public String findDifferentBinaryString(String[] nums) {
        /*
        Convert binary string to integers so as to reduce the number of times we
        have to convert integer to string. I think integer to string takes longer
        than string to integer.
        
        O(NlogN + N^2), 11 ms, faster than 21.27%
         */
        Arrays.sort(nums);
        int cur = 0;
        for (int i = 0; i < nums.length && Integer.parseInt(nums[i], 2) == cur; i++)
            cur++;
        String fmt = "%" + nums.length + "s";
        return String.format(fmt, Integer.toBinaryString(cur)).replace(" ", "0");
    }
}


class Solution {
    public String findDifferentBinaryString(String[] nums) {
        /*
        Use random number. Technically O(infinity)
        
        13 ms, faster than 20.55%
         */
        Set<Integer> numsSet = new HashSet<>();
        for (String s : nums) numsSet.add(Integer.parseInt(s, 2));
        Random ran = new Random();
        int r = 0; int max = 1 << nums.length;
        while (numsSet.contains(r))
            r = ran.nextInt(max);
        String fmt = "%" + nums.length + "s";
        return String.format(fmt, Integer.toBinaryString(r)).replace(" ", "0");
    }
}


class Solution {
    public String findDifferentBinaryString(String[] nums) {
        /*
        Cantor's Diagonal Argument.
        
        Very very good solution. The answer is a string such that at position i,
        it is different from position i at nums[i]. This will guarantee that the
        answer string is different from all the nums at at least one position. 
        
        O(N), 0 ms, faster than 100.00%
         */
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < nums.length; i++)
            res.append((nums[i].charAt(i) - '0') ^ 1);
        return res.toString();
    }
}
