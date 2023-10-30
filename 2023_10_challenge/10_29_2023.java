class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        /*
        LeetCode 458 (Fail)

        Wasn't able to solve it on my own, so I read the hints. It turns out that the hints already contain
        the solution.

        What is clear is that we need to find the total number of states x pigs with T tests can represent.
        When T = 1, each pig has two states: live or die. Then with x pigs, we have 2^x number of states.

        With more tests, each pig can represent more states. For example, when T = 2, a pig can be:
        live live
        live die
        die

        When T = 3, a pig can be
        live live live
        live live die
        live die
        die

        Follow this pattern, it is easy to see that with T number of tests, a pig can have T + 1 number of states.
        Thus the problem is equivalent to find the smallest integer x such that (T + 1) ^ x >= N, where N is the
        number of buckets.
         */
        double res = Math.log(buckets) / Math.log(minutesToTest / minutesToDie + 1);
        if (Math.abs(res - (int)res) <= 0.0000001) return (int)res;
        return (int)res + 1;
    }
}
