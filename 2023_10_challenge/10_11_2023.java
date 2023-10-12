class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] people) {
        /*
        LeetCode 2251
        
        The problem is essentially given an array of intervals, find the number of overlaps at any given time. It can
        be solved by counting at each interval start and end the current number of overlaps. Then we can go through
        the desired time from left to right and find which gap it belongs to and obtain the count accordingly.
        
        I have been through this type of calendar scheduling problem two times with Google. The first time was back in
        2019 for a summer internship. The problem was given as a hackerrank-ish online assessment. The second time was
        last October in a video interview where almost exactly the same scheduling problem was asked. Both problems
        could be solved by this method with some twists of course.
        
        O(NlogN + MlogM), 92 ms, faster than 46.15%
         */
        int[][] comb = new int[flowers.length * 2][2];
        for (int i = 0; i < flowers.length; i++) {
            comb[2 * i][0] = flowers[i][0]; comb[2 * i][1] = 1; // start
            comb[2 * i + 1][0] = flowers[i][1] + 1; comb[2 * i + 1][1] = -1; // end
        }
        Arrays.sort(comb, Comparator.comparingInt(tup -> tup[0]));
        List<int[]> counts = new ArrayList<>();
        counts.add(new int[]{0, 0});
        int pos; int count; int last;
        for (int[] tup : comb) {
            last = counts.size() - 1;
            pos = tup[0];
            count = counts.get(last)[1] + tup[1];
            if (pos == counts.get(last)[0]) {
                counts.get(last)[1] = count;
            } else {
                counts.add(new int[]{pos, count});
            }
        }
        counts.add(new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE});
        // Get sorted people and attach their index info.
        int[][] sortedPeople = new int[people.length][2];
        for (int i = 0; i < people.length; i++) {sortedPeople[i][0] = people[i]; sortedPeople[i][1] = i;}
        Arrays.sort(sortedPeople, Comparator.comparingInt(tup -> tup[0]));
        // Find the answer
        int j = 0;
        int[] res = new int[sortedPeople.length];
        for (int[] sortedPerson : sortedPeople) {
            while (j < counts.size() && counts.get(j)[0] <= sortedPerson[0]) {j++;}
            res[sortedPerson[1]] = counts.get(j - 1)[1];
        }
        return res;
    }
}


class Solution {
    private int bisectRight(int[] arr, int tgt) {
        int lo = 0; int hi = arr.length; int mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (arr[mid] > tgt) {hi = mid;} else {lo = mid + 1;}
        }
        return lo;
    }

    public int[] fullBloomFlowers(int[][] flowers, int[] people) {
        /*
        This is the binary search with diff method. It is essentially the same as before, but it has much simpler
        implementation.

        Sort all the starts and all the ends. Then binary search each pos in people in starts and ends. The index of
        starts represents the number of flowers added. The index of ends represents the number of flowers removed.
        Their difference is the answer.
        
        We have to roll our own bisect_right. And for the ends, it should be
        1 more than the original end to allow bisect-right to work. If we
        do not add 1 to the original end, we need bisect_left.

        O(NlogN + MlogN), 35 ms, faster than 97.69%
         */
        int[] los = new int[flowers.length];
        int[] his = new int[flowers.length];
        for (int i = 0; i < flowers.length; i++) {los[i] = flowers[i][0]; his[i] = flowers[i][1] + 1;}
        Arrays.sort(los); Arrays.sort(his);
        int[] res = new int[people.length];
        int loIdx; int hiIdx;
        for (int i = 0; i < people.length; i++) {
            res[i] = bisectRight(los, people[i]) - bisectRight(his, people[i]);
        }
        return res;
    }
}
