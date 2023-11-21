class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        /*
        LeetCode 2391

        Very straightforward solution. No trick, no DP. Since each garbage must be picked up,
        the time for picking up all the garbage is the sum of the string length in the garbage
        array.

        Then we need to figure out the number of stops each truck must travel. A truck only
        needs to travel as far as the last house that has its designated garbage. Thus, we
        can iterate from right to left on garbage and designate the first encounter of a
        garbage type as the last house that its corresponding truck must arrive. We can use
        a prefix sum array to quickly obtain the amount of traveling time for the truck.

        O(N * 10 * 3), 3 ms, faster than 96.97% 
         */
        int res = 0;
        for (String s : garbage) res += s.length();
        int[] presum = new int[garbage.length];
        for (int i = 1; i < garbage.length; i++) presum[i] = presum[i - 1] + travel[i - 1];
        int totalChecked = 0;
        int[] checked = new int[3];
        String trucks = "MPG";
        for (int i = garbage.length - 1; i >= 0 && totalChecked < 3; i--) {
            for (int j = 0; j < 3; j++) {
                if (checked[j] == 0 && garbage[i].indexOf(trucks.charAt(j)) >= 0) {
                    checked[j] = 1;
                    res += presum[i];
                    totalChecked++;
                }
            }
        }
        return res;
    }
}
