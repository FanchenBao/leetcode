"""
Date: 06/22/2019

Not too difficult a problem, and I realized that I needed to use a queue type data structure at the beginning. However, I encountered two problems along the way. First, I didn't realize that as previous trips were pushed to the queue, they must be sorted according to the end destination. This resulted in ditching deque as it could not be sorted. A more efficient implementation should be priority queue, but I tried a regular list and it got the job done. The second problem was that once a new location was encountered, we must drop off all the people that can be dropped off. That means we had to loop through the queue and pop off all trips that had been completed already. After figuring out these two issues, the algorithm was not difficult.
"""


class Solution:
    def carPooling(self, trips, capacity):
        trips.sort(key=lambda x: x[1])
        numPass = 0
        dropOffs = []
        for trip in trips:
            currLoc = trip[1]
            while (
                dropOffs and dropOffs[0][2] <= currLoc
            ):  # need to drop off people first
                numPass -= dropOffs[0][0]
                dropOffs.pop(0)
            numPass += trip[0]
            if numPass > capacity:
                return False
            dropOffs.append(trip)
            dropOffs.sort(key=lambda x: x[2])
        return True


sol = Solution()
print(sol.carPooling([[3, 2, 8], [4, 4, 6], [10, 8, 9]], 11))
