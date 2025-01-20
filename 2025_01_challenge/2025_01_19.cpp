#include <algorithm>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int trapRainWater(vector<vector<int>> &heightMap) {
    /*
     * LeetCode 407
     *
     * I had to revisit problem 42 because I was not very sure of the solution.
     * I knew it can be solved by monotonic decreasing array, which is the
     * standard solution. However, for the current problem, the two pointer
     * solution seems to be more appropriate. I need a little primer from my
     * previous solution in problem 42 to recall the essence of the two-pointer
     * solution.
     *
     * For the current problem, we can run the two pointer solution for each
     * row and record the amount of water trapped above each height. However,
     * the water recorded for this run is not guaranteed. We need to do a
     * second run for each column and update the amount of water that can
     * be held above each cell. We take the min of the amount of water above
     * a cell between the horizontal and vertical run.
     *
     * Finally, we sum up all the water and that is our answer.
     *
     * O(MN)
     */
    int M = heightMap.size(), N = heightMap[0].size();
    // max height reachable with water for each cell
    std::vector<std::vector<int>> water(M, std::vector<int>(N, INT_MAX));
    // go horizontal and fill water using the two pointer method
    for (int i = 0; i < M; i++) {
      int lo = 0, hi = N - 1;
      int lmax = heightMap[i][lo], rmax = heightMap[i][hi];
      while (lo <= hi) {
        if (lmax <= rmax) {
          if (heightMap[i][lo] <= lmax)
            water[i][lo] = lmax;
          else
            lmax = heightMap[i][lo];
          lo++;
        } else {
          if (heightMap[i][hi] <= rmax)
            water[i][hi] = rmax;
          else
            rmax = heightMap[i][hi];
          hi--;
        }
      }
    }
    // go vertical and update the water. We can only take the min water of the
    // two directions
    for (int j = 0; j < N; j++) {
      int lo = 0, hi = M - 1;
      int tmax = heightMap[lo][j], bmax = heightMap[hi][j];
      while (lo <= hi) {
        if (tmax <= bmax) {
          if (heightMap[lo][j] <= tmax)
            water[lo][j] = std::min(water[lo][j], heightMap[lo][j]);
          else
            tmax = heightMap[lo][j];
          lo++;
        } else {
          if (heightMap[hi][j] <= bmax)
            water[hi][j] = std::min(water[hi][j], heightMap[hi][j]);
          else
            bmax = heightMap[hi][j];
          hi--;
        }
      }
    }
    // go through water to find minimum height
    int min_water_height = INT_MAX;
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++)
        min_water_height = std::min(min_water_height, water[i][j]);
    }
    int res = 0;
    for (auto row : heightMap) {
      for (auto r : row) {
        if (r < min_water_height)
          res += min_water_height - r;
      }
    }
    return res;
  }
};

class Solution2 {
public:
  int trapRainWater(vector<vector<int>> &heightMap) {
    /*
     * I was not able to solve this problem myself. I was tryig to naively
     * extend the 2D solution from problem 47 to this 3D version, but going
     * horizontally and them vertically does not work.
     *
     * The real solution is to use BFS as an extension of the original 2D
     * solution. In the 2D solution, we use two pointers to find the min of
     * the two borders, and progress from the smaller border. In the 3D
     * version, we use the same approach. We find the smallest of all the
     * borders (e.g., the outer edge of the grid at the beginning). From
     * there, we progress using BFS. A min heap can be used to quickly pop
     * the current lowest border. If we encounter a higher cell, we add
     * that to the heap. If we encounter a lower cell, since we know the
     * current lowest border, the amount of water that can be held above the
     * current lower border is the difference between it and the lowest
     * border. After that, we can set the water-filled cell to the same
     * height as the lowest border and throw it to the heap as well.
     *
     * We keep doing this until all the cells are processed.
     *
     * O(MNlogMN), 192 ms, 6.61%
     *
     * UPDATE: do not wait until everything in the heap gets popped. We can
     * keep track of the number of cells not visited. Once all cells have been
     * visited, we can end the loop.
     *
     * 179 ms, 6.89%
     *
     */
    std::priority_queue<std::vector<int>> min_heap;
    int M = heightMap.size(), N = heightMap[0].size();
    std::vector<std::vector<int>> dirs({{0, 1}, {0, -1}, {1, 0}, {-1, 0}});
    // put the edges in the heap
    for (int j = 0; j < N; j++) {
      min_heap.push({-heightMap[0][j], 0, j});
      min_heap.push({-heightMap[M - 1][j], M - 1, j});
      // mark cell as been included in the heap
      heightMap[0][j] = -1;
      heightMap[M - 1][j] = -1;
    }
    for (int i = 1; i < M - 1; i++) {
      min_heap.push({-heightMap[i][0], i, 0});
      min_heap.push({-heightMap[i][N - 1], i, N - 1});
      // mark cell as been included in the heap
      heightMap[i][0] = -1;
      heightMap[i][N - 1] = -1;
    }
    int res = 0;
    int remaining = M * N - min_heap.size();
    while (!min_heap.empty() && remaining > 0) {
      auto ele = min_heap.top();
      min_heap.pop();
      int h = -ele[0], i = ele[1], j = ele[2];
      for (auto dir : dirs) {
        int ni = i + dir[0], nj = j + dir[1];
        if (0 <= ni && ni < M && 0 <= nj && nj < N && heightMap[ni][nj] >= 0) {
          if (heightMap[ni][nj] < h)
            res += h - heightMap[ni][nj];
          min_heap.push({-std::max(heightMap[ni][nj], h), ni, nj});
          heightMap[ni][nj] = -1;
          remaining--;
        }
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
