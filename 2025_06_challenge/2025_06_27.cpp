#include <algorithm>
#include <iostream>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> maxSubsequence(vector<int> &nums, int k) {
    /*
     * LeetCode 2099
     *
     * Sort the nums and find the largest k numbers. Then return these k
     * numbers in their original sequence.
     */
    std::vector<int> sorted_nums = nums;
    std::sort(sorted_nums.begin(), sorted_nums.end());
    std::unordered_map<int, int> counter;
    for (int i = sorted_nums.size() - 1; i >= int(sorted_nums.size() - k);
         i--) {
      counter[sorted_nums[i]]++;
    }
    std::vector<int> res;
    for (int i = 0; i < nums.size() && !counter.empty(); i++) {
      auto it = counter.find(nums[i]);
      if (it != counter.end()) {
        res.push_back(it->first);
        it->second--;
        if (it->second == 0)
          counter.erase(it);
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> nums{-35};
  int k = 1;
  Solution sol;
  sol.maxSubsequence(nums, k);
}
