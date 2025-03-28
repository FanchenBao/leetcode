#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minimumIndex(vector<int> &nums) {
    /*
     * LeetCode 2780
     *
     * Prefix count and suffix count of the dominion number
     *
     * O(N), 63 ms, 16.80%
     */
    std::map<int, int> counter;
    for (int n : nums)
      counter[n]++;
    int dominion = -1, dom_count = 0;
    for (auto const &[k, v] : counter) {
      if (v > nums.size() / 2) {
        dominion = k;
        dom_count = v;
        break;
      }
    }
    int pcount = 0;
    for (int i = 0; i < nums.size(); i++) {
      pcount += nums[i] == dominion;
      if (pcount > (i + 1) / 2 &&
          (dom_count - pcount) > (nums.size() - i - 1) / 2)
        return i;
    }
    return -1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
