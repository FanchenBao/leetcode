#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minCapability(vector<int> &nums, int k) {
    /*
     * LeetCode 2560
     *
     * Standard binary search. O(NlogN)
     *
     * Update: use max_element method
     */
    int lo = 1, hi = *(std::max_element(nums.begin(), nums.end())) + 1;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      int cnt = 0, prerob = -2;
      for (int i = 0; i < nums.size(); i++) {
        if (nums[i] <= mid && i > prerob + 1) {
          cnt++;
          prerob = i;
        }
      }
      if (cnt >= k)
        hi = mid;
      else
        lo = mid + 1;
    }
    return lo;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
