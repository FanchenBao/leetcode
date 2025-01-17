#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int xorAllNums(vector<int> &nums1, vector<int> &nums2) {
    /*
     * LeetCode 2425
     *
     * Write out all the pairs, we will see that for each number in nums1, it
     * will be XOR to itself len(nums2) times. This means if len(nums2) is
     * even, all the XOR of each number in nums1 become zero. Otherwise, we
     * have total XOR of every number in nums1.
     *
     * The same applies to nums2.
     *
     * O(M + N), 0 ms, 100%
     */
    int res = 0;
    if (nums1.size() % 2 == 1) {
      for (int n : nums2)
        res ^= n;
    }
    if (nums2.size() % 2 == 1) {
      for (int n : nums1)
        res ^= n;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
