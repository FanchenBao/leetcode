class Solution {
    public int eliminateMaximum(int[] dist, int[] speed) {
        /*
        LeetCode 1921
        
        The weapon can only shoot once per minute, which means the time that
        it can shoot is 0, 1, 2, ...
        
        We need to make sure that at time 0, 1, 2, ... no monster has arrived
        at the city. We can compute the time needed for each monster to reach
        the city, sort it from low to high, and compare it to the time when the
        weapon can shoot. If the weapon time is smaller than the monster arrival
        time, the monster can be eliminated. Otherwise, we lose the game.
        
        O(NlogN), 22 ms, faster than 41.15%
        */
        float[] time = new float[dist.length];
        for (int i = 0; i < dist.length; i++) time[i] = dist[i] / (float)speed[i];
        Arrays.sort(time);
        int t = 0;
        while (t < time.length && t < time[t]) t++;
        return t;
    }
}
