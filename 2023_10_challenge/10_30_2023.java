
class Solution {
    public int[] sortByBits(int[] arr) {
        /*
        LeetCode 1356
        
        My knowledge in Java is lacking. Thus, I have no idea how to
        solve this problem without converting arr to an ArrayList of
        Integer first.
        
        O(NlogN), 8 ms, faster than 53.21%
        */
        List<Integer> arrList = new ArrayList<>();
        for (int a : arr) arrList.add(a);
        arrList.sort((o1, o2) -> {
            int cntBitO1 = Integer.bitCount(o1);
            int cntBitO2 = Integer.bitCount(o2);
            if (cntBitO1 > cntBitO2) return 1;
            else if (cntBitO1 < cntBitO2) return -1;
            else return o1.compareTo(o2);
        });
        int[] res = new int[arr.length];
        for (int i = 0; i < arrList.size(); i++) res[i] = arrList.get(i);
        return res;
    }
}


class Solution {
    public int[] sortByBits(int[] arr) {
        /*
        LeetCode 1356

        Use Integer array instead of ArrayList. Probably can be
        faster.
        
        9 ms, faster than 47.46% 
         */
        Integer[] arrInt = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) arrInt[i] = arr[i];
        Arrays.sort(arrInt, (o1, o2) -> {
            int cntBitO1 = Integer.bitCount(o1);
            int cntBitO2 = Integer.bitCount(o2);
            if (cntBitO1 > cntBitO2) return 1;
            else if (cntBitO1 < cntBitO2) return -1;
            else return o1.compareTo(o2);
        });
        int[] res = new int[arr.length];
        for (int i = 0; i < arrInt.length; i++) res[i] = arrInt[i];
        return res;

    }
}
