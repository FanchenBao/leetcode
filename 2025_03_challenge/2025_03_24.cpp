#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int countDays(int days, vector<vector<int>> &meetings) {
    /*
     * LeetCode 3169
     *
     * Line-sweep shall suffice.
     * O(NlogN), 89 ms, 23.47%
     */
    std::vector<std::pair<int, int>> points;
    for (auto &m : meetings) {
      points.push_back({m[0], 1});
      points.push_back({m[1] + 1, -1});
    }
    std::sort(points.begin(), points.end());
    int res = 0, pre = 1, psum = 0;
    for (auto &p : points) {
      if (psum == 0)
        res += p.first - pre;
      psum += p.second;
      pre = p.first;
    }
    if (psum == 0)
      res += days + 1 - pre;
    return res;
  }
};

class Solution2 {
public:
  int countDays(int days, vector<vector<int>> &meetings) {
    /*
     * Without linesweep, we can sort the intervals and check the current
     * start against the previous end. If there is a gap, we have found
     * some days without meeting.
     * O(NlogN)
     */
    std::sort(meetings.begin(), meetings.end());
    int res = 0, pre_end = 0;
    for (auto &m : meetings) {
      if (m[0] > pre_end)
        res += m[0] - pre_end - 1;
      pre_end = std::max(pre_end, m[1]);
    }
    return res + days - pre_end;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
