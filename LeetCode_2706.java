class Solution1 {
    public int buyChoco(int[] prices, int money) {
        /*
        Sort and get the first two prices. But actually, we don't even need to sort. We can simply find the two
        smallest. But sorting is easier.
         */
        Arrays.sort(prices);
        if (prices[0] + prices[1] <= money) {
            return money - prices[0] - prices[1];
        } else {
            return money;
        }
    }
}

class Solution2 {
    public int buyChoco(int[] prices, int money) {
        /*
        Find the smallest and second smallest
         */
        int min = 1000;
        int sec_min = 1000;
        for (int price: prices) {
            if (price < min) {
                sec_min = min;
                min = price;
            } else if (price < sec_min) {
                sec_min = price;
            }
        }
        if (min + sec_min <= money) {
            return money - min - sec_min;
        } else {
            return money;
        }
    }
}