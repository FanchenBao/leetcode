#include <iostream>
#include <set>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  int minimizeMax(vector<int> &nums, int p) {
    /*
     * LeetCode 2616
     *
     * Sort nums, then produce difference between each consecutive pairs.
     * Then sort the difference along with the left index. We will pick the
     * first p differences that do not have any overlap on indices.
     *
     * O(NlogN)
     */
    std::vector<std::pair<int, int>> nums_indices;
    for (int i = 0; i < nums.size(); i++)
      nums_indices.push_back({nums[i], i});
    std::sort(nums_indices.begin(), nums_indices.end());
    std::vector<std::vector<int>> diffs;
    for (int i = 0; i < nums_indices.size() - 1; i++)
      diffs.push_back({nums_indices[i + 1].first - nums_indices[i].first,
                       nums_indices[i].second, nums_indices[i + 1].second});
    std::sort(diffs.begin(), diffs.end());
    int res = 0;
    std::unordered_set<int> used_indices;
    for (const auto &ele : diffs) {
      if (used_indices.contains(ele[1]) || used_indices.contains(ele[2]))
        continue;
      res = std::max(res, ele[0]);
      used_indices.insert(ele[1]);
      used_indices.insert(ele[2]);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
