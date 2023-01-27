# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque
import heapq


class Solution1:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Navive BFS, MLE

        The problem is that this algorithm cannot handle cycles. We can allow
        visiting nodes that have been visited before, but ONLY IF the second
        visit improves upon the previous one by reducing the price.
        """
        graph = [[] for _ in range(n)]
        for a, b, p in flights:
            graph[a].append((b, p))

        queue = deque([(src, 0, 0)])
        res = math.inf
        while queue:
            city, price, stops = queue.popleft()
            if stops > k + 1:
                break
            if city == dst:
                res = min(res, price)
            else:
                for nex, p in graph[city]:
                    queue.append((nex, price + p, stops + 1))
        return res if res < math.inf else -1


class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """DFS with backtracking. TLE
        """
        graph = [[] for _ in range(n)]
        for a, b, p in flights:
            graph[a].append((b, p))

        self.res = math.inf

        def dfs(city, price, stops, visited) -> None:
            if stops > k + 1 or city in visited:
                return
            if city == dst:
                self.res = min(self.res, price)
                return
            visited.add(city)
            for nex, p in graph[city]:
                dfs(nex, price + p, stops + 1, visited)
            visited.remove(city)

        dfs(src, 0, 0, set())
        return self.res


class Solution3:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """LeetCode 787

        Let's Dijkstra this thing

        This is a very convoluted implementation of Dijkstra. The basic idea is
        to Dijkstra once. If we hit src within k stops, we are good. If not, we
        reuse all the previous unused cities to run Dijkstra again with sub-
        optimal choices. To enable this, I use two heaps, with heap2 always
        collecting the sub-optimal choices popped by heap1. And once heap1 is
        no go, we swap and go again.

        219 ms, faster than 54.94%
        """
        graph = [[] for _ in range(n)]
        for a, b, p in flights:
            graph[a].append((b, p))

        prices = [math.inf] * n
        prices[src] = 0
        heap1, heap2 = [(0, src, 0)], []  # [price, city, stops]

        while heap1:
            while heap1 and heap1[0][0] > prices[heap1[0][1]]:
                heapq.heappush(heap2, heapq.heappop(heap1))
            if not heap1 or heap1 and heap1[0][2] > k + 1:
                while heap1:
                    price, city, stops = heapq.heappop(heap1)
                    if stops <= k + 1:
                        heapq.heappush(heap2, (price, city, stops))
                heap1, heap2 = heap2, []
                prices = [math.inf] * n
                prices[src] = 0
                continue
            price, city, stops = heapq.heappop(heap1)
            if city == dst:
                return price
            for nex, p in graph[city]:
                if price + p < prices[nex]:
                    prices[nex] = price + p
                    heapq.heappush(heap1, (price + p, nex, stops + 1))

        return -1


class Solution4:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Better Dijkstra.

        Use the traditional Dijkstra but without keeping track of the distance.
        This is because if the optimal way fails, we can continue with the
        sub-optimal way that is already in the queue. The trick to avoid cycles
        is to keep track of the number of stops to reach each city. If we have
        to reach the same city again, it must be with fewer stops. Otherwise,
        the result won't be better than the previous time that city was visited.

        133 ms, faster than 67.75%
        """
        graph = [[] for _ in range(n)]
        for a, b, p in flights:
            graph[a].append((b, p))

        visited = {src: 0}  # {city: number of stops}
        heap = [(0, src, 0)]  # [price, city, stops]
        while heap:
            price, city, stops = heapq.heappop(heap)
            if visited.get(city, math.inf) < stops or stops > k + 1:
                continue
            if city == dst:
                return price
            visited[city] = stops
            for nex, p in graph[city]:
                heapq.heappush(heap, (price + p, nex, stops + 1))
        return -1


class Solution5:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """BFS, from the official solution.
        
        The difference between this BFS and Solution 1 is that we are not taking
        all the nodes at all levels. Instead, for each level, we only take the
        nodes that improve the pricing for that node. Otherwise, there is no
        point taking it any more. We use a prices array to keep track of the
        cheapest way to reach all the cities.

        O(N + K * E), 221 ms, faster than 54.74% 
        """
        graph = [[] for _ in range(n)]
        for a, b, p in flights:
            graph[a].append((b, p))

        prices = [math.inf] * n
        queue = [(0, src)]  # (price, city)
        while queue and k + 1 >= 0:
            tmp = []
            for price, city in queue:
                if prices[city] <= price:  # previous price is low enough, no need to use current price
                    continue
                prices[city] = price
                for nex, p in graph[city]:
                    tmp.append((price + p, nex))
            k -= 1
            queue = tmp
        return prices[dst] if prices[dst] < math.inf else -1


class Solution6:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Updated version of Solution 1, with the prices array to check whether
        a revisit to a previously visited node is allowed.

        115 ms, faster than 74.98%
        """
        graph = [[] for _ in range(n)]
        for a, b, p in flights:
            graph[a].append((b, p))

        queue = deque([(src, 0, 0)])
        prices = [math.inf] * n
        while queue:
            city, price, stops = queue.popleft()
            if stops > k + 1:
                break
            if prices[city] <= price:
                continue
            else:
                prices[city] = price
                for nex, p in graph[city]:
                    queue.append((nex, price + p, stops + 1))
        return prices[dst] if prices[dst] < math.inf else -1


class Solution7:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Bellman Ford from official solution.

        O(K * E + N)
        """
        prices = [math.inf] * n
        prices[src] = 0
        while k + 1:
            tmp = [math.inf] * n
            tmp[src] = 0
            for a, b, p in flights:
                tmp[b] = min(tmp[b], prices[b], prices[a] + p)
            prices = tmp
            k -= 1
        return prices[dst] if prices[dst] < math.inf else -1


sol = Solution7()
tests = [
    (4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1, 700),
    (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1, 200),
    (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0, 500),
    (5, [[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]], 0, 4, 3, 40),
]

for i, (n, flights, src, dst, k, ans) in enumerate(tests):
    res = sol.findCheapestPrice(n, flights, src, dst, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
