#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> mergeArrays(vector<vector<int>> &nums1,
                                  vector<vector<int>> &nums2) {
    /*
     * LeetCode 2570
     *
     * Leverage sorted map
     */
    std::map<int, int> m;
    for (const auto &p : nums1)
      m[p[0]] += p[1];
    for (const auto &p : nums2)
      m[p[0]] += p[1];
    std::vector<std::vector<int>> res;
    for (const auto &p : m)
      res.push_back({p.first, p.second});
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
