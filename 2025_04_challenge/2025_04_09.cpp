#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minOperations(vector<int> &nums, int k) {
    /*
     * LeetCode 3375
     *
     * Sort nums. If the nums[0] is smaller than k, there is no way
     * to coerce nums[0] into k.
     *
     * Otherwise, there is always a way to reach k. We move from right to left.
     * Each time there is a diff between adjacent values, we change the bigger
     * values to align with the smaller one.
     *
     * O(NlogN), 16 ms, 24.53%
     */
    std::sort(nums.begin(), nums.end());
    if (nums[0] < k)
      return -1;
    int res = 0;
    for (int i = nums.size() - 2; i >= 0; i--) {
      if (nums[i] != nums[i + 1])
        res++;
    }
    if (nums[0] != k)
      return res + 1;
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
