#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maximumCount(vector<int> &nums) {
    /*
     * LeetCode 2529
     *
     * Binary search to find the position of the first positive and the last
     * negative.
     *
     * O(logN)
     */
    int pos_idx = std::upper_bound(nums.begin(), nums.end(), 0) - nums.begin();
    int neg_idx = std::lower_bound(nums.begin(), nums.end(), 0) - nums.begin();
    return std::max((int)nums.size() - pos_idx, neg_idx);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
