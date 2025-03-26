#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool check(std::map<int, int> ranges) {
    int pre_end = -1, good_cuts = 0;
    for (auto const &[k, v] : ranges) {
      if (k >= pre_end) {
        if (pre_end >= 0)
          good_cuts++;
        if (good_cuts == 2)
          return true;
      }
      pre_end = std::max(pre_end, v);
    }
    return false;
  }

  bool checkValidCuts(int n, vector<vector<int>> &rectangles) {
    /*
     * LeetCode 3394
     *
     * for each given left/bottom coord, find its associated largest coord.
     * Then go through all the x pairs or y pairs and check if a valid set of
     * cuts is available.
     *
     * O(NlogN), 455 ms, 15.98%
     */
    std::map<int, int> xs; // key = left bound, value = largest right bound
                           // given the left bound
    std::map<int, int> ys; // key = lower bound, value = largest upper bound
                           // given the lower bound
    for (auto &rec : rectangles) {
      xs[rec[0]] = std::max(xs[rec[0]], rec[2]);
      ys[rec[1]] = std::max(ys[rec[1]], rec[3]);
    }
    std::cout << check(xs) << check(ys) << std::endl;
    return check(xs) || check(ys);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
