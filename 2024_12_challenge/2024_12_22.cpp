#include <algorithm>
#include <deque>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> leftmostBuildingQueries(vector<int> &heights,
                                      vector<vector<int>> &queries) {
    /*
     * LeetCode 2940
     *
     * Sort the queries by the bigger query index in desc. Then go from right
     * to left on heights and build a monotonic increasing deque.
     *
     * For each query, add the heights to the right of the bigger query index
     * into the monotonic increasing deque. Then binary search the deque with
     * the larger heights in the query. The left most height in the deque that
     * is bigger than the larger height is the answer index.
     *
     * This is correct because monotonic increasing deque guarantees that the
     * first index whose heights[index] is bigger than the query is the left
     * most. All heights that have been popped are smaller than the heights to
     * their left.
     *
     * O(MlogM + N), 359 ms, faster than 36.95%
     */
    int M = queries.size();
    for (int i = 0; i < M; i++) {
      queries[i].push_back(i);
      if (queries[i][0] > queries[i][1]) {
        // Make sure that the smaller query index is always at the beginning
        int tmp = queries[i][0];
        queries[i][0] = queries[i][1];
        queries[i][1] = tmp;
      }
    }
    std::sort(queries.begin(), queries.end(),
              [](vector<int> &a, vector<int> &b) {
                if (a[1] == b[1])
                  return a[0] < b[0];
                return a[1] > b[1];
              });
    std::deque<int> mon; // save indices of heights directly
    int j = heights.size() - 1;
    std::vector<int> res(M);
    auto cmp = [&](int val, int idx) { return val < heights[idx]; };
    for (auto q : queries) {
      while (j >= q[1]) {
        while (!mon.empty() && heights[mon.front()] <= heights[j])
          mon.pop_front();
        mon.push_front(j);
        j--;
      }
      int tgt = std::max(heights[q[0]], heights[q[1]]);
      auto it = std::upper_bound(mon.begin(), mon.end(), tgt, cmp);
      if (heights[*(--it)] == tgt && *it == q[1] &&
          (heights[q[0]] < tgt || q[0] == q[1]))
        // if the previous value of the matched upper bound is equal to
        // the target, we need to decide whether this previous value's
        // index is a valid stop for both q[0] and q[1].
        // It is valid if  index == q[1] (q[1] does not need to move)
        // and heights at q[0] is smaller than tgt (q[0] is allowed to
        // move) or q[0] == q[1] (q[0] also does not need to move)
        res[q[2]] = *it;
      else if (++it == mon.end())
        res[q[2]] = -1;
      else
        res[q[2]] = *it;
    }
    return res;
  }
};

int main() {
  std::vector<int> heights{6, 4, 8, 5, 2, 7};
  std::vector<std::vector<int>> queries{{0, 1}, {0, 3}, {2, 4},
                                        {3, 4}, {2, 2}, {4, 5}};
  Solution sol;
  sol.leftmostBuildingQueries(heights, queries);
}
