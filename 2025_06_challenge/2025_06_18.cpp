#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> divideArray(vector<int> &nums, int k) {
    /*
     * LeetCode 2966
     *
     * Sort the array and use greedy. We get the triplets in order. Whenever
     * a triple fails the requirement, we return empty array.
     *
     * O(NlogN), 56 ms, 30%
     */
    std::sort(nums.begin(), nums.end());
    std::vector<std::vector<int>> res;
    for (int i = 2; i < nums.size(); i += 3) {
      if (nums[i] - nums[i - 2] <= k) {
        res.push_back({nums[i - 2], nums[i - 1], nums[i]});
      } else {
        return {};
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
