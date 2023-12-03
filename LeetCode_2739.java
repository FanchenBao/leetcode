class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        /*
        Did not think this through. The tricky part is that when
        additional gas is added to the main tank when the main tank
        has 4 liter, it becomes 5 and is able to obtain one more
        liter from additional tank.
        
        4 ms, faster than 99.70%
        */
        int res = 0;
        while (mainTank >= 5 && additionalTank > 0) {
            res += 50;
            mainTank -= 4;
            additionalTank--;
        }
        return mainTank * 10 + res;
    }
}


class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        /*
        Math solution
        */
        int q = mainTank / 4;;
        if (mainTank % 4 == 0)
            q--;
        return (Math.min(q, additionalTank) + mainTank) * 10;
    }
}