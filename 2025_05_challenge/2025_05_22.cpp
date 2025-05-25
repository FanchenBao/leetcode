#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxRemoval(vector<int> &nums, vector<vector<int>> &queries) {
    /*
     * LeetCode 3362
     *
     * We will use greedy + priority queue.
     *
     * First, we sort queries by left. Then we iterate through each position.
     * To reduce the number of queries used, we want a query to be as large
     * as possible. For each number, we can iterate through queries and find
     * all the queries that include the current number. We push the right of
     * the query into the priority queue (max heap). Then depending on the
     * size of the number and whether any previous queries have already covered
     * the current number, we take the top x rights from the priority queue.
     * Once we take the rights, we also update a linesweep array, such that
     * we know the impact of taking these queries on future numbers.
     *
     * We keep doing this under all the numbers are covered.
     *
     * O(NlogN)
     */
    int N = nums.size();
    std::priority_queue<int> queue;
    std::vector<int> linesweep(N + 1);
    std::sort(queries.begin(), queries.end());
    int query_count = 0, qidx = 0;
    for (int i = 0; i < N; i++) {
      if (i > 0)
        linesweep[i] += linesweep[i - 1];
      while (qidx < queries.size()) {
        int l = queries[qidx][0], r = queries[qidx][1];
        if (l <= i && i <= r)
          queue.push(r);
        else if (i < l)
          break;
        qidx++;
      }
      int needed = std::max(nums[i] - linesweep[i], 0);
      while (!queue.empty() && needed > 0 && queue.top() >= i) {
        linesweep[i]++;
        linesweep[queue.top() + 1]--;
        queue.pop();
        needed--;
      }
      if (needed)
        return -1;
      query_count += needed;
    }
    return queries.size() - query_count;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
