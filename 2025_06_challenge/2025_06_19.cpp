#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int partitionArray(vector<int> &nums, int k) {
    /*
     * LeetCode 2294
     *
     * Since we can pick and choose any elements from nums to form the
     * subsequence, we might as well sort nums, and find the min number of
     * subarray that satisfy the requirements.
     *
     * O(NlogN), 32 ms, 75%
     */
    std::sort(nums.begin(), nums.end());
    int res = 0;
    int min = nums[0];
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] - min > k) {
        res++;
        min = nums[i];
      }
    }
    return res + 1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
