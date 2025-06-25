#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> findKDistantIndices(vector<int> &nums, int key, int k) {
    /*
     * LeetCode 2200
     *
     * Find the indices of values in nums that are equal to key. Then iterate
     * through all indices to find the ones that differ from the indices less
     * than k.
     *
     * O(N)
     */
    std::vector<int> kis;
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == key)
        kis.push_back(i);
    }
    int i = 0, j = 0;
    std::vector<int> res;
    while (i < nums.size() && j < kis.size()) {
      if (std::abs(i - kis[j]) <= k) {
        res.push_back(i);
        i++;
      } else if (i < kis[j]) {
        i++;
      } else {
        j++;
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
